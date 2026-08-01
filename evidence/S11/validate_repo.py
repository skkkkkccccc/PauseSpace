#!/usr/bin/env python3
"""S11 repository-kickoff acceptance validator (structural).

Checks package.json (zero-dep, native ESM, all scripts), src/ layout, README
command docs, no secrets in src, and that no prior-session baseline file was
modified (only README/TASKS/logs). The actual command runs (install/test/lint/
build/start) are captured separately in evidence/S11/run-output.txt.

    python3 evidence/S11/validate_repo.py
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
results = []
PRE = "8dd681b8e27b3bd7105d4bccec94e034ea2e3974"


def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}{(' — ' + detail) if detail else ''}")


def read(rel):
    p = ROOT / rel
    return p.read_text(encoding="utf-8") if p.exists() else ""


pkg = json.loads(read("package.json"))
check("package.json parses", isinstance(pkg, dict) and "name" in pkg)
for s in ["test", "lint", "build", "start", "preview"]:
    check(f"package.json has script: {s}", s in pkg.get("scripts", {}))
check("A1 zero runtime dependencies",
      not pkg.get("dependencies") and not pkg.get("devDependencies"), "no deps")
check("A1 native ESM (type: module)", pkg.get("type") == "module")

for f in ["src/index.html", "src/styles.css", "src/app.js",
          "src/test/smoke.test.mjs", "src/tools/lint.mjs",
          "src/tools/build.mjs", "src/tools/serve.mjs"]:
    check(f"exists: {f}", (ROOT / f).exists())

readme = read("README.md").lower()
check("A2 README documents run commands",
      all(c in readme for c in ["npm install", "npm test", "npm run lint",
                                "npm run build", "npm start"]))

blob = "".join(read(f) for f in ["src/index.html", "src/styles.css", "src/app.js"])
SECRET = re.compile(r"password|api[_-]?key|bearer|authorization\s*:|AKIA[0-9A-Z]{16}|-----BEGIN")
check("A1 no secrets in src app files", not SECRET.search(blob))

proc = subprocess.run(["git", "diff", "--name-only", PRE], cwd=ROOT, capture_output=True, text=True)
changed = [l for l in proc.stdout.splitlines() if l.strip()]
allowed = {"README.md", "TASKS.md", "docs/DecisionLog.md", "docs/CoBuildLog.md"}
unexpected = [c for c in changed if c not in allowed]
check("regression: no prior baseline file modified (only README/TASKS/logs)",
      not unexpected, ("unexpected: " + str(unexpected)) if unexpected else f"allowed modifications: {changed}")

passed = sum(1 for _, ok, _ in results if ok)
print("\n" + "=" * 60)
print(f"RESULT: {passed}/{len(results)} checks passed")
print("=" * 60)
sys.exit(0 if passed == len(results) else 1)
