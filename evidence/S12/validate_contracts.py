#!/usr/bin/env python3
"""S12 data-and-state-contracts acceptance validator.

Confirms src/data/, src/state/, and tests/ exist; runs the S12 unit tests
(node --test) and the S11 smoke (npm test) for no regression; scans new modules
for secrets; and checks no prior baseline file was modified. Exits 0 only if all
pass.

    python3 evidence/S12/validate_contracts.py
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
results = []
PRE = "9f71632fe984495381bd435cbad42b65e2becf78"
TESTS = ["tests/scene-loader.test.mjs", "tests/player.test.mjs", "tests/progress.test.mjs"]
MODULES = ["src/data/scene-loader.mjs", "src/state/player.mjs", "src/state/progress.mjs"]
SECRET = re.compile(r"password|api[_-]?key|bearer|authorization\s*:|AKIA[0-9A-Z]{16}|-----BEGIN")


def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}{(' — ' + detail) if detail else ''}")


for f in MODULES + TESTS:
    check(f"exists: {f}", (ROOT / f).exists())

t = subprocess.run(["node", "--test", *TESTS], cwd=ROOT, capture_output=True, text=True)
check("S12 unit tests pass (node --test, fail 0)",
      t.returncode == 0 and "fail 0" in t.stdout,
      f"rc={t.returncode}")

s = subprocess.run(["npm", "test"], cwd=ROOT, capture_output=True, text=True)
check("S11 smoke (npm test) still passes — no regression",
      s.returncode == 0 and "fail 0" in s.stdout, f"rc={s.returncode}")

blob = "".join((ROOT / f).read_text(encoding="utf-8") for f in MODULES if (ROOT / f).exists())
check("no secrets in new src/data + src/state modules", not SECRET.search(blob))

proc = subprocess.run(["git", "diff", "--name-only", PRE], cwd=ROOT, capture_output=True, text=True)
changed = [l for l in proc.stdout.splitlines() if l.strip()]
allowed = {"TASKS.md", "docs/DecisionLog.md", "docs/CoBuildLog.md"}
unexpected = [c for c in changed if c not in allowed]
check("regression: no prior baseline file modified (only TASKS/logs)",
      not unexpected, ("unexpected: " + str(unexpected)) if unexpected else f"modified: {changed}")

passed = sum(1 for _, ok, _ in results if ok)
print("\n" + "=" * 60)
print(f"RESULT: {passed}/{len(results)} checks passed")
print("=" * 60)
sys.exit(0 if passed == len(results) else 1)
