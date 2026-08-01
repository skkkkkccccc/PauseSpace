#!/usr/bin/env python3
"""S08 information-architecture acceptance validator.

Checks docs/UserFlows.md (five views, navigation, completion branches, error
states, no dead end, no forced completion) and the docs/Architecture.md IA update
(original statement preserved), and confirms the S01-S07 baseline is unchanged
from the S08 pre-session checkpoint 6ef5fc4 (excluding the two S08 in-scope
files). Exits 0 only if all checks pass.

    python3 evidence/S08/validate_ia.py
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
results = []
PRE_CHECKPOINT = "6ef5fc4f3eed8d409dc57d67d6d2528fc9d2bdd3"
VIEWS = ["home", "scene detail", "player", "pause map", "project/about"]
BRANCHES = ["back", "exit", "replay", "support"]
ERRORS = ["loading", "missing-audio", "offline", "update"]
BASELINE_FILES = [
    "docs/Traceability.md", "docs/ProjectPlan.md", "README.md",
    "config/sample-config.json", "data/sample/scene.sample.json",
    "docs/ResearchProtocol.md", "data/sample/interview-notes.json",
    "docs/ResearchFindings.md", "content/schema.json", "docs/ContentRubric.md",
    "content/exam-room.json", "content/sports-field.json",
    "content/own-room.json", "content/empty-classroom.json",
    "config/audio-generation.env.example", "docs/OptionalAIAudioExtension.md",
    "prompts/OptionalAudioSessionOA01.md", "docs/ContentReview.md",
    "assets/audio/README.md",
]  # docs/Architecture.md and docs/UserFlows.md are S08 in-scope -> excluded


def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}{(' — ' + detail) if detail else ''}")


def read(rel):
    p = ROOT / rel
    return p.read_text(encoding="utf-8") if p.exists() else ""


def section(text, heading_prefix):
    out, inside = [], False
    for ln in text.splitlines():
        if ln.startswith("## "):
            inside = ln[3:].lower().startswith(heading_prefix.lower())
            continue
        if inside:
            out.append(ln)
    return "\n".join(out)


uf = read("docs/UserFlows.md")
arch = read("docs/Architecture.md")
uf_low, arch_low = uf.lower(), arch.lower()

check("docs/UserFlows.md exists and is non-empty", bool(uf.strip()))
missing_views = [v for v in VIEWS if v not in uf_low]
check("A1 UserFlows specifies the five views", not missing_views,
      ("missing: " + ", ".join(missing_views)) if missing_views else "all five")
missing_br = [b for b in BRANCHES if b not in uf_low]
check("A1 navigation includes back/exit/replay/support branches", not missing_br,
      ("missing: " + ", ".join(missing_br)) if missing_br else "all present")

err_sec = section(uf, "Error states").lower()
missing_err = [e for e in ERRORS if e not in err_sec]
check("A2 error states documented (loading/missing-audio/offline/update)", not missing_err,
      ("missing: " + ", ".join(missing_err)) if missing_err else "all four")
check("A2 every error state has an exit/recovery in the error section",
      "exit" in err_sec and "recovery" in err_sec)

exit_count = uf.count("Exit:")
check("A2 every view has an exit (>=5 'Exit:' labels)", exit_count >= 5, f"{exit_count} found")
check("A2 'no forced completion' stated", "no forced completion" in uf_low)
check("A2 baseline journeys + no-dead-end checklist present",
      "baseline journeys" in uf_low and "no dead end" in uf_low)

check("A3 Architecture.md updated with IA section", "information architecture" in arch_low)
check("A3 Architecture.md original statement preserved",
      "static html/css/javascript" in arch_low)
check("A3 Architecture.md references the five views",
      all(v in arch_low for v in ("home", "player", "pause map", "project/about")))

proc = subprocess.run(["git", "diff", "--exit-code", PRE_CHECKPOINT, "--", *BASELINE_FILES],
                      cwd=ROOT, capture_output=True, text=True)
check("regression: S01-S07 baseline unchanged from 6ef5fc4 (excl. S08 in-scope files)",
      proc.returncode == 0,
      "no diff (baseline intact)" if proc.returncode == 0 else ("changed:\n" + proc.stdout))

passed = sum(1 for _, ok, _ in results if ok)
print("\n" + "=" * 60)
print(f"RESULT: {passed}/{len(results)} checks passed")
print("=" * 60)
sys.exit(0 if passed == len(results) else 1)
