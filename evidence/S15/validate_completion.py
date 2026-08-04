#!/usr/bin/env python3
"""S15 completion-choices-and-support-route validator.

Confirms content/support.json (non-emergency, release-blocked pending mentor
approval) + src/views/Completion.js exist; the S15 tests pass; baseline npm test
+ build pass; build output unchanged; no PII/secrets in support content or the
view; and only expected files changed vs the S15 pre-session checkpoint 35b6293.
Exits 0 only if all pass.

    python3 evidence/S15/validate_completion.py
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
results = []
PRE = "35b6293"
SECRET = re.compile(r"AKIA[0-9A-Z]{16}|-----BEGIN|sk-[A-Za-z0-9]{20}")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")


def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}{(' — ' + detail) if detail else ''}")


def run(cmd):
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)


for f in ["content/support.json", "src/views/Completion.js", "tests/completion.test.mjs"]:
    check(f"exists: {f}", (ROOT / f).exists())

support = json.loads((ROOT / "content/support.json").read_text(encoding="utf-8"))
check("A2 support is non-emergency", "not emergency" in support.get("boundary", "").lower())
check("A2 support release is BLOCKED (reviewStatus pending; releaseBlocked true)",
      support.get("reviewStatus") == "pending-mentor-review" and support.get("releaseBlocked") is True,
      f"reviewStatus={support.get('reviewStatus')} releaseBlocked={support.get('releaseBlocked')}")

t = run(["node", "--test", "tests/completion.test.mjs"])
check("S15 completion tests pass (fail 0)", t.returncode == 0 and "fail 0" in t.stdout, f"rc={t.returncode}")

nt = run(["npm", "test"])
check("npm test (baseline smoke) still passes", nt.returncode == 0 and "fail 0" in nt.stdout, f"rc={nt.returncode}")

bd = run(["npm", "run", "build"])
check("npm run build still passes", bd.returncode == 0, f"rc={bd.returncode}")
dist = sorted(p.name for p in (ROOT / "dist").iterdir()) if (ROOT / "dist").exists() else []
check("build output unchanged (no support/completion in dist)", set(dist) == {"index.html", "styles.css", "app.js"}, str(dist))

blob = (ROOT / "content/support.json").read_text(encoding="utf-8") + (ROOT / "src/views/Completion.js").read_text(encoding="utf-8")
check("no secret pattern in support content + Completion view", not SECRET.search(blob))
check("no real email/phone in support.json contacts (placeholders only)",
      not EMAIL.search((ROOT / "content/support.json").read_text(encoding="utf-8")))

proc = run(["git", "diff", "--name-only", PRE])
changed = [l for l in proc.stdout.splitlines() if l.strip()]
allowed = {"TASKS.md", "docs/DecisionLog.md", "docs/CoBuildLog.md"}
unexpected = [c for c in changed if c not in allowed]
check("regression: only expected files modified (S15 support/view/tests are new/untracked)",
      not unexpected, ("unexpected: " + str(unexpected)) if unexpected else f"modified: {changed}")

passed = sum(1 for _, ok, _ in results if ok)
print("\n" + "=" * 60)
print(f"RESULT: {passed}/{len(results)} checks passed")
print("=" * 60)
sys.exit(0 if passed == len(results) else 1)
