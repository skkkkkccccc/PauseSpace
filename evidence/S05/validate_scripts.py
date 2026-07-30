#!/usr/bin/env python3
"""S05 exam-and-sports-scripts acceptance validator.

Validates content/exam-room.json and content/sports-field.json against
content/schema.json (structure + timing budget), runs the choice-language rubric
(no commands/promises/judgments/forced breathing in spoken text), records an
estimated spoken duration, and confirms the S01-S04 baseline is unchanged from
the S05 pre-session checkpoint c264786. Exits 0 only if all checks pass.

    python3 evidence/S05/validate_scripts.py
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
results = []
PRE_CHECKPOINT = "c26478666a3283396dea607096fcf4adfe453b18"
SCENES = ["content/exam-room.json", "content/sports-field.json"]
BASELINE_FILES = [
    "docs/Traceability.md", "docs/ProjectPlan.md", "README.md",
    "config/sample-config.json", "data/sample/scene.sample.json",
    "docs/ResearchProtocol.md", "data/sample/interview-notes.json",
    "docs/ResearchFindings.md", "content/schema.json", "docs/ContentRubric.md",
]
SEGMENT_ALLOWED = {"order", "label", "startSecond", "endSecond", "optional", "text"}
TOP_ALLOWED = {"id", "title", "moment", "focus", "durationSeconds", "segments",
               "exit", "transcript", "audio", "review"}
# Choice-language rubric: phrases that must NOT appear in spoken text.
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
            if not (isinstance(sg.get("text"), str) and sg.get("text")):
                e.append(f"segment {i} text empty")
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


# ---------- per-scene checks ----------
for rel in SCENES:
    scene = json.loads((ROOT / rel).read_text(encoding="utf-8"))
    sid = scene.get("id", rel)
    se = structural_errors(scene)
    be = business_errors(scene)
    check(f"{sid}: conforms to content/schema.json (structure)", not se,
          "; ".join(se) if se else "structure OK")
    check(f"{sid}: timing budget (segments ordered, within duration)", not be,
          "; ".join(be) if be else "OK")

    low = spoken_text(scene).lower()
    hits = [p for p in PROHIBITED if p in low]
    check(f"{sid}: rubric — no commands/promises/judgments/forced breathing", not hits,
          ("found: " + ", ".join(hits)) if hits else "clean (choice language)")

    words = len(spoken_text(scene).split())
    est = round(words / (100 / 60))  # ~100 wpm calm pace
    check(f"{sid}: spoken duration fits budget (est ~{est}s <= {scene['durationSeconds']}s, words={words})",
          30 <= est <= scene["durationSeconds"], f"est {est}s")

    check(f"{sid}: review.status is draft (pending student rewrite/read-aloud)",
          scene.get("review", {}).get("status") == "draft")

# ---------- rubric still present + regression ----------
rubric = (ROOT / "docs/ContentRubric.md").read_text(encoding="utf-8").lower()
check("choice-language rubric present (command/promise/judgment rules)",
      all(w in rubric for w in ("command", "promise", "judgment")))

proc = subprocess.run(["git", "diff", "--exit-code", PRE_CHECKPOINT, "--", *BASELINE_FILES],
                      cwd=ROOT, capture_output=True, text=True)
check("regression: S01-S04 baseline unchanged from c264786",
      proc.returncode == 0,
      "no diff (baseline intact)" if proc.returncode == 0 else ("changed:\n" + proc.stdout))

passed = sum(1 for _, ok, _ in results if ok)
print("\n" + "=" * 60)
print(f"RESULT: {passed}/{len(results)} checks passed")
print("=" * 60)
sys.exit(0 if passed == len(results) else 1)
