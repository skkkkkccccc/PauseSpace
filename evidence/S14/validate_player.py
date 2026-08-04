#!/usr/bin/env python3
"""S14 accessible-player-and-viewing-modes validator.

Confirms src/components/{AudioPlayer,ModePicker}.js + tests/player.test.js exist;
the S14 player tests pass; baseline npm test + build pass; build output unchanged
(no TTS); no autoplay/TTS APIs in components; no secrets; and only expected files
changed vs the S14 pre-session checkpoint 81251cc. Exits 0 only if all pass.

    python3 evidence/S14/validate_player.py
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
results = []
PRE = "81251cc"
SECRET = re.compile(r"AKIA[0-9A-Z]{16}|-----BEGIN|sk-[A-Za-z0-9]{20}")


def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}{(' — ' + detail) if detail else ''}")


def run(cmd):
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)


for f in ["src/components/AudioPlayer.js", "src/components/ModePicker.js", "tests/player.test.js"]:
    check(f"exists: {f}", (ROOT / f).exists())

t = run(["node", "--test", "tests/player.test.js"])
check("S14 player tests pass (node --test, fail 0)", t.returncode == 0 and "fail 0" in t.stdout, f"rc={t.returncode}")

nt = run(["npm", "test"])
check("npm test (baseline smoke) still passes", nt.returncode == 0 and "fail 0" in nt.stdout, f"rc={nt.returncode}")

bd = run(["npm", "run", "build"])
check("npm run build still passes", bd.returncode == 0, f"rc={bd.returncode}")
dist = sorted(p.name for p in (ROOT / "dist").iterdir()) if (ROOT / "dist").exists() else []
check("build output unchanged (no player/TTS in dist)", set(dist) == {"index.html", "styles.css", "app.js"}, str(dist))

src = "".join((ROOT / f).read_text(encoding="utf-8") for f in ["src/components/AudioPlayer.js", "src/components/ModePicker.js"])
low = src.lower()
check("A1/A2 no runtime audio element / autoplay attribute / TTS API in components",
      "<audio" not in src and "<video" not in src and "autoplay=" not in low
      and "speechsynthesis" not in low and "new Audio(" not in src and "TextToSpeech" not in src)
check("no secret pattern in S14 components", not SECRET.search(src))

proc = run(["git", "diff", "--name-only", PRE])
changed = [l for l in proc.stdout.splitlines() if l.strip()]
allowed = {"TASKS.md", "docs/DecisionLog.md", "docs/CoBuildLog.md"}
unexpected = [c for c in changed if c not in allowed]
check("regression: only expected files modified (S14 components/tests are new/untracked)",
      not unexpected, ("unexpected: " + str(unexpected)) if unexpected else f"modified: {changed}")

passed = sum(1 for _, ok, _ in results if ok)
print("\n" + "=" * 60)
print(f"RESULT: {passed}/{len(results)} checks passed")
print("=" * 60)
sys.exit(0 if passed == len(results) else 1)
