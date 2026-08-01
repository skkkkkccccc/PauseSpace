#!/usr/bin/env python3
"""S06 room-and-empty-classroom-scripts acceptance validator.

Validates ALL FOUR scene scripts (exam-room, sports-field, own-room,
empty-classroom) against content/schema.json (structure + timing budget), runs
the choice-language rubric, confirms the four scenes SHARE THE SAME CONTENT
CONTRACT, and checks the S01-S05 baseline is unchanged from the S06 pre-session
checkpoint bdf0ff3. Exits 0 only if all checks pass.

    python3 evidence/S06/validate_scripts.py
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
results = []
PRE_CHECKPOINT = "bdf0ff3ffa9b14f38e5dbffb7eca0a989e40a5a1"
SCENES = ["content/exam-room.json", "content/sports-field.json",
          "content/own-room.json", "content/empty-classroom.json"]
BASELINE_FILES = [
    "docs/Traceability.md", "docs/ProjectPlan.md", "README.md",
    "config/sample-config.json", "data/sample/scene.sample.json",
    "docs/ResearchProtocol.md", "data/sample/interview-notes.json",
    "docs/ResearchFindings.md", "content/schema.json", "docs/ContentRubric.md",
    "content/exam-room.json", "content/sports-field.json",
]
SEGMENT_ALLOWED = {"order", "label", "startSecond", "endSecond", "optional", "text"}
TOP_ALLOWED = {"id", "title", "moment", "focus", "durationSeconds", "segments",
               "exit", "transcript", "audio", "review"}
PROHIBITED = [
    "breathe in", "breathe out", "breathe deeply", "take a deep breath",
    "hold your breath", "inhale", "exhale",
    "will calm", "will relax", "will make you", "reduces stress", "reduce stress",
    "relieve stress", "cures", "cure for", "heals", "therapeutic", "treatment",
    "good job", "well done", "you should", "you must", "you have to", "wrong",
    "abnormal", "diagnosis", "diagnosed", "anxiety", "depression",
]


def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}{(' — ' + detail) if detail else ''}")


schema = json.loads((ROOT / "content/schema.json").read_text(encoding="utf-8"))
DUR_MIN = schema["properties"]["durationSeconds"]["minimum"]
DUR_MAX = schema["properties"]["durationSeconds"]["maximum"]
STATUS_ENUM = set(schema["properties"]["review"]["properties"]["status"]["enum"])


def structural_errors(s):
    e = []
    if not isinstance(s, dict):
        return ["not an object"]
    if set(s) - TOP_ALLOWED:
        e.append(f"extra top-level keys: {sorted(set(s) - TOP_ALLOWED)}")
    for k in ("id", "title", "durationSeconds", "segments", "exit", "transcript", "audio", "review"):
        if k not in s:
            e.append(f"missing: {k}")
    if e:
        return e
    if not (isinstance(s["id"], str) and s["id"]):
        e.append("id empty")
    if not (isinstance(s["title"], str) and s["title"]):
        e.append("title empty")
    d = s["durationSeconds"]
    if not (isinstance(d, int) and not isinstance(d, bool) and DUR_MIN <= d <= DUR_MAX):
        e.append(f"durationSeconds must be int in [{DUR_MIN},{DUR_MAX}]")
    segs = s["segments"]
    if not (isinstance(segs, list) and segs):
        e.append("segments must be non-empty array")
    else:
        for i, sg in enumerate(segs):
            for k in ("order", "label", "startSecond", "endSecond", "text"):
                if k not in sg:
                    e.append(f"segment {i} missing {k}")
            if set(sg) - SEGMENT_ALLOWED:
                e.append(f"segment {i} extra keys")
    ex = s["exit"]
    if not (isinstance(ex, dict) and isinstance(ex.get("language"), str) and ex["language"]):
        e.append("exit.language must be non-empty")
    tr = s["transcript"]
    if not (isinstance(tr, dict) and tr.get("sameOrigin") is True and tr.get("text")):
        e.append("transcript requires sameOrigin=true + text")
    au = s["audio"]
    if not (isinstance(au, dict) and au.get("sameOrigin") is True and au.get("src")):
        e.append("audio requires sameOrigin=true + src")
    rv = s["review"]
    if not (isinstance(rv, dict) and rv.get("status") in STATUS_ENUM):
        e.append(f"review.status must be one of {sorted(STATUS_ENUM)}")
    return e


def business_errors(s):
    e = []
    prev = 0
    for i, sg in enumerate(s.get("segments", [])):
        st, en, order = sg.get("startSecond"), sg.get("endSecond"), sg.get("order")
        if order != i + 1:
            e.append(f"segment {i} order={order} expected {i + 1}")
        if isinstance(st, (int, float)) and isinstance(en, (int, float)):
            if en < st:
                e.append(f"segment {i} end<start")
            if st < prev:
                e.append(f"segment {i} overlaps")
            prev = en
    segs = s.get("segments", [])
    if segs:
        last = segs[-1].get("endSecond")
        dur = s.get("durationSeconds")
        if isinstance(last, (int, float)) and isinstance(dur, int) and last > dur:
            e.append(f"last endSecond {last} > duration {dur}")
    return e


def spoken_text(s):
    parts = [sg.get("text", "") for sg in s.get("segments", [])]
    parts.append(s.get("transcript", {}).get("text", ""))
    parts.append(s.get("exit", {}).get("language", ""))
    return " ".join(parts)


loaded = {}
for rel in SCENES:
    s = json.loads((ROOT / rel).read_text(encoding="utf-8"))
    loaded[rel] = s
    sid = s.get("id", rel)
    se = structural_errors(s)
    be = business_errors(s)
    check(f"{sid}: conforms to content/schema.json (structure)", not se, "; ".join(se) if se else "OK")
    check(f"{sid}: timing budget (ordered, within duration)", not be, "; ".join(be) if be else "OK")
    low = spoken_text(s).lower()
    hits = [p for p in PROHIBITED if p in low]
    check(f"{sid}: rubric — no commands/promises/judgments/forced breathing", not hits,
          ("found: " + ", ".join(hits)) if hits else "clean")
    words = len(spoken_text(s).split())
    est = round(words / (100 / 60))
    check(f"{sid}: spoken duration fits budget (est ~{est}s <= {s['durationSeconds']}s, words={words})",
          30 <= est <= s["durationSeconds"], f"est {est}s")
    check(f"{sid}: review.status is draft (pending student rewrite/read-aloud)",
          s.get("review", {}).get("status") == "draft")

# ---------- A1: all four scenes share the same content contract ----------
keysets = {tuple(sorted(s.keys())) for s in loaded.values()}
durations = {s["durationSeconds"] for s in loaded.values()}
seg_counts = {len(s["segments"]) for s in loaded.values()}
seg_labels = {tuple(sg["label"] for sg in s["segments"]) for s in loaded.values()}
statuses = {s["review"]["status"] for s in loaded.values()}
check("A1 four scenes share the same content contract (keys/duration/segments/labels/status)",
      len(keysets) == 1 and len(durations) == 1 and len(seg_counts) == 1
      and len(seg_labels) == 1 and len(statuses) == 1,
      f"keysets={len(keysets)} durations={durations} seg_counts={seg_counts} "
      f"label_sets={len(seg_labels)} statuses={statuses}")

# ---------- regression ----------
proc = subprocess.run(["git", "diff", "--exit-code", PRE_CHECKPOINT, "--", *BASELINE_FILES],
                      cwd=ROOT, capture_output=True, text=True)
check("regression: S01-S05 baseline unchanged from bdf0ff3",
      proc.returncode == 0,
      "no diff (baseline intact)" if proc.returncode == 0 else ("changed:\n" + proc.stdout))

passed = sum(1 for _, ok, _ in results if ok)
print("\n" + "=" * 60)
print(f"RESULT: {passed}/{len(results)} checks passed")
print("=" * 60)
sys.exit(0 if passed == len(results) else 1)
