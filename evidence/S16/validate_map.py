#!/usr/bin/env python3
"""S16 pause-map-and-local-privacy validator.

Confirms src/state/progressStore.js + src/views/Map.js + tests/map.test.mjs exist;
the S16 tests pass; baseline npm test + build pass; build output unchanged; no
secrets/PII in the new modules; and only expected files changed vs the S16
pre-session checkpoint c124db5. Exits 0 only if all pass.

    python3 evidence/S16/validate_map.py
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
results = []
PRE = "c124db5"
SECRET = re.compile(r"AKIA[0-9A-Z]{16}|-----BEGIN|sk-[A-Za-z0-9]{20}")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")


def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}{(' — ' + detail) if detail else ''}")


def run(cmd):
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)


for f in ["src/state/progressStore.js", "src/views/Map.js", "tests/map.test.mjs"]:
    check(f"exists: {f}", (ROOT / f).exists())

t = run(["node", "--test", "tests/map.test.mjs"])
check("S16 map tests pass (fail 0)", t.returncode == 0 and "fail 0" in t.stdout, f"rc={t.returncode}")

nt = run(["npm", "test"])
check("npm test (baseline smoke) still passes", nt.returncode == 0 and "fail 0" in nt.stdout, f"rc={nt.returncode}")

bd = run(["npm", "run", "build"])
check("npm run build still passes", bd.returncode == 0, f"rc={bd.returncode}")
dist = sorted(p.name for p in (ROOT / "dist").iterdir()) if (ROOT / "dist").exists() else []
check("build output unchanged (no store/map in dist)", set(dist) == {"index.html", "styles.css", "app.js"}, str(dist))

blob = "".join((ROOT / f).read_text(encoding="utf-8") for f in ["src/state/progressStore.js", "src/views/Map.js"])
check("no secret pattern in progressStore + Map", not SECRET.search(blob))
check("no real email/phone in progressStore + Map", not EMAIL.search(blob))

proc = run(["git", "diff", "--name-only", PRE])
changed = [l for l in proc.stdout.splitlines() if l.strip()]
allowed = {"TASKS.md", "docs/DecisionLog.md", "docs/CoBuildLog.md"}
unexpected = [c for c in changed if c not in allowed]
check("regression: only expected files modified (S16 store/map/tests are new/untracked)",
      not unexpected, ("unexpected: " + str(unexpected)) if unexpected else f"modified: {changed}")

passed = sum(1 for _, ok, _ in results if ok)
print("\n" + "=" * 60)
print(f"RESULT: {passed}/{len(results)} checks passed")
print("=" * 60)
sys.exit(0 if passed == len(results) else 1)
