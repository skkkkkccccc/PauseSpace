#!/usr/bin/env python3
"""S09 mobile-prototype acceptance validator.

Checks design/prototype/index.html (four-view clickable vertical slice, explicit
exit controls, mobile viewport, synthetic copy, self-contained with no external
network/backend), docs/UsabilityTasks.md (defined task + observation/issue
templates, no-coaching rule), and that the S01-S08 baseline is unchanged from the
S09 pre-session checkpoint 0ed8bd2. Exits 0 only if all checks pass.

    python3 evidence/S09/validate_prototype.py
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
results = []
PRE_CHECKPOINT = "0ed8bd20d6f56578b7c6b7f4a3f24830176d41b2"
VIEWS = ["view-home", "view-detail", "view-player", "view-done"]
BASELINE_FILES = [
    "docs/Traceability.md", "docs/ProjectPlan.md", "README.md",
    "config/sample-config.json", "data/sample/scene.sample.json",
    "docs/ResearchProtocol.md", "data/sample/interview-notes.json",
    "docs/ResearchFindings.md", "content/schema.json", "docs/ContentRubric.md",
    "content/exam-room.json", "content/sports-field.json",
    "content/own-room.json", "content/empty-classroom.json",
    "config/audio-generation.env.example", "docs/OptionalAIAudioExtension.md",
    "prompts/OptionalAudioSessionOA01.md", "docs/ContentReview.md",
    "assets/audio/README.md", "docs/Architecture.md", "docs/UserFlows.md",
]  # design/prototype/ and docs/UsabilityTasks.md are S09 in-scope -> excluded


def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}{(' — ' + detail) if detail else ''}")


def read(rel):
    p = ROOT / rel
    return p.read_text(encoding="utf-8") if p.exists() else ""


html = read("design/prototype/index.html")
ut = read("docs/UsabilityTasks.md")
hlow = html.lower()

# ---------- A1: clickable vertical slice ----------
check("design/prototype/index.html exists and is non-empty", bool(html.strip()))
check("HTML has DOCTYPE + <html> + <body>", html.lstrip().lower().startswith("<!doctype html>")
      and "<html" in hlow and "<body" in hlow and "</body>" in hlow and "</html>" in hlow)
missing_views = [v for v in VIEWS if v not in hlow]
check("A1 four views present (home/detail/player/done)", not missing_views,
      ("missing: " + ", ".join(missing_views)) if missing_views else "all four")
check("A1 explicit exit controls (exit class + 'Exit' label)",
      "exit" in hlow and "exit" in "".join(re.findall(r'class="([^"]*)"', html)).lower()
      and re.search(r">\s*exit", html, re.I))
check("A1 synthetic copy (exam-room + a script line)", "exam-room" in hlow
      and "return to the menu" in hlow)

# ---------- A2: self-contained, low-fi, mobile ----------
check("A2 mobile viewport meta", "width=device-width" in hlow)
check("A2 mobile container (max-width)", "max-width" in hlow)
external = re.findall(r'(?:src|href)\s*=\s*["\']https?://', html)
check("A2 no external network scripts/styles", not external and "fetch(" not in html,
      ("external: " + str(external)) if external else "self-contained")
check("A2 no backend / no frameworks / no analytics markers",
      not any(m in hlow for m in ["fetch(", "xhr", "<iframe", "google-analytics", "googletagman"]))

# ---------- A3: usability task doc ----------
check("docs/UsabilityTasks.md exists and is non-empty", bool(ut.strip()))
utlow = ut.lower()
need = ["task", "observation", "issue", "without coaching"]
missing_ut = [w for w in need if w not in utlow]
check("A3 UsabilityTasks defines task + observation/issue templates + no-coaching",
      not missing_ut, ("missing: " + ", ".join(missing_ut)) if missing_ut else "all present")

# ---------- regression ----------
proc = subprocess.run(["git", "diff", "--exit-code", PRE_CHECKPOINT, "--", *BASELINE_FILES],
                      cwd=ROOT, capture_output=True, text=True)
check("regression: S01-S08 baseline unchanged from 0ed8bd2 (excl. S09 in-scope files)",
      proc.returncode == 0,
      "no diff (baseline intact)" if proc.returncode == 0 else ("changed:\n" + proc.stdout))

passed = sum(1 for _, ok, _ in results if ok)
print("\n" + "=" * 60)
print(f"RESULT: {passed}/{len(results)} checks passed")
print("=" * 60)
sys.exit(0 if passed == len(results) else 1)
