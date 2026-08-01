#!/usr/bin/env python3
"""S07 content-review-and-recording-plan acceptance validator.

Checks docs/ContentReview.md (per-script review records, version/transcript IDs,
adult-approval status, frozen rule) and assets/audio/README.md (setup, filenames,
levels, retake, transcript-match, license), confirms each scene's audio.src
matches the filename convention, re-runs the choice-language rubric on all four
scenes, and checks the S01-S06 baseline is unchanged from the S07 pre-session
checkpoint d9762c6. Exits 0 only if all checks pass.

    python3 evidence/S07/validate_review.py
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
results = []
PRE_CHECKPOINT = "d9762c68923e1edd0807435673ece57ecbf7cbd0"
SCENES = ["exam-room", "sports-field", "own-room", "empty-classroom"]
BASELINE_FILES = [
    "docs/Traceability.md", "docs/ProjectPlan.md", "README.md",
    "config/sample-config.json", "data/sample/scene.sample.json",
    "docs/ResearchProtocol.md", "data/sample/interview-notes.json",
    "docs/ResearchFindings.md", "content/schema.json", "docs/ContentRubric.md",
    "content/exam-room.json", "content/sports-field.json",
    "content/own-room.json", "content/empty-classroom.json",
    "config/audio-generation.env.example", "docs/OptionalAIAudioExtension.md",
    "prompts/OptionalAudioSessionOA01.md",
]
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


def read(rel):
    p = ROOT / rel
    return p.read_text(encoding="utf-8") if p.exists() else ""


def spoken_text(s):
    parts = [sg.get("text", "") for sg in s.get("segments", [])]
    parts.append(s.get("transcript", {}).get("text", ""))
    parts.append(s.get("exit", {}).get("language", ""))
    return " ".join(parts)


review = read("docs/ContentReview.md")
audio_doc = read("assets/audio/README.md")

# ---------- A1: ContentReview.md ----------
check("docs/ContentReview.md exists and is non-empty", bool(review.strip()))
missing_ids = [s for s in SCENES if s not in review.lower()]
check("ContentReview references all four scenes", not missing_ids,
      ("missing: " + ", ".join(missing_ids)) if missing_ids else "all four")
missing_ver = [f"{s}.v1" for s in SCENES if f"{s}.v1" not in review]
check("ContentReview has script version IDs (<scene>.v1)", not missing_ver,
      ("missing: " + ", ".join(missing_ver)) if missing_ver else "all four")
rv_low = review.lower()
check("ContentReview records transcript version IDs",
      "transcript version" in rv_low)
check("ContentReview records adult-approval status (PENDING)",
      "adult approval" in rv_low and "pending" in rv_low)
check("ContentReview has a frozen-version rule", "frozen" in rv_low)

# ---------- A2: assets/audio/README.md ----------
check("assets/audio/README.md exists and is non-empty", bool(audio_doc.strip()))
ad_low = audio_doc.lower()
need = ["setup", "filename", "levels", "retake", "transcript", "license"]
missing_doc = [w for w in need if w not in ad_low]
check("audio README covers setup/filenames/levels/retake/transcript/license",
      not missing_doc, ("missing: " + ", ".join(missing_doc)) if missing_doc else "all present")

# audio.src matches convention for each scene
bad_src = []
for sid in SCENES:
    s = json.loads((ROOT / f"content/{sid}.json").read_text(encoding="utf-8"))
    expect = f"assets/audio/{sid}.mp3"
    if s.get("audio", {}).get("src") != expect:
        bad_src.append((sid, s.get("audio", {}).get("src"), expect))
check("each scene audio.src matches assets/audio/<scene-id>.mp3", not bad_src,
      str(bad_src) if bad_src else "all four match")

# ---------- rubric re-check on all four scenes ----------
bad_rubric = []
for sid in SCENES:
    s = json.loads((ROOT / f"content/{sid}.json").read_text(encoding="utf-8"))
    low = spoken_text(s).lower()
    hits = [p for p in PROHIBITED if p in low]
    if hits:
        bad_rubric.append((sid, hits))
check("rubric re-check: all four scripts still choice-language clean",
      not bad_rubric, str(bad_rubric) if bad_rubric else "all clean")

# ---------- regression ----------
proc = subprocess.run(["git", "diff", "--exit-code", PRE_CHECKPOINT, "--", *BASELINE_FILES],
                      cwd=ROOT, capture_output=True, text=True)
check("regression: S01-S06 baseline unchanged from d9762c6",
      proc.returncode == 0,
      "no diff (baseline intact)" if proc.returncode == 0 else ("changed:\n" + proc.stdout))

passed = sum(1 for _, ok, _ in results if ok)
print("\n" + "=" * 60)
print(f"RESULT: {passed}/{len(results)} checks passed")
print("=" * 60)
sys.exit(0 if passed == len(results) else 1)
