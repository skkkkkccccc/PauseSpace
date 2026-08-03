#!/usr/bin/env python3
"""S13 home-and-scene-views acceptance validator.

Confirms src/views/ + src/components/SceneCard.js exist; the S13 view tests pass;
baseline npm test + build pass; the build output is unchanged (no TTS); no
scene-specific copy is hard-coded in view source; no <audio>/TTS in views; no
secrets; and only expected files changed vs the S13 pre-session checkpoint 2d80457.
Exits 0 only if all pass.

    python3 evidence/S13/validate_views.py
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
results = []
PRE = "2d80457"
SECRET = re.compile(r"AKIA[0-9A-Z]{16}|-----BEGIN|sk-[A-Za-z0-9]{20}")
SCENE_COPY = ["Exam room", "exam-room", "Sports field", "sports-field",
              "Own room", "own-room", "Empty classroom", "empty-classroom"]


def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}{(' — ' + detail) if detail else ''}")


def run(cmd):
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)


for f in ["src/components/SceneCard.js", "src/views/escape-html.js",
          "src/views/home.js", "src/views/scene-detail.js", "tests/views.test.mjs"]:
    check(f"exists: {f}", (ROOT / f).exists())

t = run(["node", "--test", "tests/views.test.mjs"])
check("S13 view tests pass (node --test, fail 0)", t.returncode == 0 and "fail 0" in t.stdout, f"rc={t.returncode}")

nt = run(["npm", "test"])
check("npm test (baseline smoke) still passes", nt.returncode == 0 and "fail 0" in nt.stdout, f"rc={nt.returncode}")

bd = run(["npm", "run", "build"])
check("npm run build still passes", bd.returncode == 0, f"rc={bd.returncode}")
dist = sorted(p.name for p in (ROOT / "dist").iterdir()) if (ROOT / "dist").exists() else []
check("build output unchanged (no TTS/views in dist)", set(dist) == {"index.html", "styles.css", "app.js"}, str(dist))

src = "".join((ROOT / f).read_text(encoding="utf-8") for f in
              ["src/components/SceneCard.js", "src/views/home.js", "src/views/scene-detail.js"])
hardcoded = [c for c in SCENE_COPY if c in src]
check("A1 no scene-specific copy hard-coded in view source", not hardcoded,
      ("hard-coded: " + str(hardcoded)) if hardcoded else "view text comes from data")
check("A2 no audio playback element/API or TTS call in views (no runtime audio/TTS in S13)",
      "<audio" not in src and "speechsynthesis" not in src.lower()
      and "new Audio(" not in src and "TextToSpeech" not in src)
check("no secret pattern in S13 view files", not SECRET.search(src))

proc = run(["git", "diff", "--name-only", PRE])
changed = [l for l in proc.stdout.splitlines() if l.strip()]
allowed = {"TASKS.md", "docs/DecisionLog.md", "docs/CoBuildLog.md"}
unexpected = [c for c in changed if c not in allowed]
check("regression: only expected files modified (S13 views/tests are new/untracked)",
      not unexpected, ("unexpected: " + str(unexpected)) if unexpected else f"modified: {changed}")

passed = sum(1 for _, ok, _ in results if ok)
print("\n" + "=" * 60)
print(f"RESULT: {passed}/{len(results)} checks passed")
print("=" * 60)
sys.exit(0 if passed == len(results) else 1)
