#!/usr/bin/env python3
"""S17 PWA-and-demo-resilience validator.

Confirms public/manifest.webmanifest (valid, non-diagnostic) + public/sw.js
(versioned cache; install/activate/fetch; skipWaiting; cleanup) + tests/sw.test.mjs
exist; the S17 SW tests pass; baseline npm test + build pass; build output
unchanged; no secrets; and only expected files changed vs the S17 pre-session
checkpoint 55e1f2c. Exits 0 only if all pass.

    python3 evidence/S17/validate_pwa.py
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
results = []
PRE = "55e1f2c"
SECRET = re.compile(r"AKIA[0-9A-Z]{16}|-----BEGIN|sk-[A-Za-z0-9]{20}")


def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}{(' — ' + detail) if detail else ''}")


def run(cmd):
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)


for f in ["public/manifest.webmanifest", "public/sw.js", "tests/sw.test.mjs"]:
    check(f"exists: {f}", (ROOT / f).exists())

manifest = json.loads((ROOT / "public/manifest.webmanifest").read_text(encoding="utf-8"))
for k in ["name", "short_name", "start_url", "display", "theme_color", "background_color"]:
    check(f"manifest has {k}", k in manifest)
check("A1 manifest description is non-diagnostic", "not diagnosis" in manifest.get("description", "").lower())

sw = (ROOT / "public/sw.js").read_text(encoding="utf-8")
check("A2 sw has VERSION + install/activate/fetch + skipWaiting + cleanup",
      "VERSION" in sw and "install" in sw and "activate" in sw and "fetch" in sw
      and "skipWaiting" in sw and "caches.delete" in sw)

t = run(["node", "--test", "tests/sw.test.mjs"])
check("S17 SW tests pass (fail 0)", t.returncode == 0 and "fail 0" in t.stdout, f"rc={t.returncode}")

nt = run(["npm", "test"])
check("npm test (baseline smoke) still passes", nt.returncode == 0 and "fail 0" in nt.stdout, f"rc={nt.returncode}")

bd = run(["npm", "run", "build"])
check("npm run build still passes", bd.returncode == 0, f"rc={bd.returncode}")
dist = sorted(p.name for p in (ROOT / "dist").iterdir()) if (ROOT / "dist").exists() else []
check("build output unchanged (manifest/sw not wired into dist)", set(dist) == {"index.html", "styles.css", "app.js"}, str(dist))

blob = sw + (ROOT / "public/manifest.webmanifest").read_text(encoding="utf-8")
check("no secret pattern in manifest + sw", not SECRET.search(blob))

proc = run(["git", "diff", "--name-only", PRE])
changed = [l for l in proc.stdout.splitlines() if l.strip()]
allowed = {"TASKS.md", "docs/DecisionLog.md", "docs/CoBuildLog.md"}
unexpected = [c for c in changed if c not in allowed]
check("regression: only expected files modified (S17 manifest/sw/tests are new/untracked)",
      not unexpected, ("unexpected: " + str(unexpected)) if unexpected else f"modified: {changed}")

passed = sum(1 for _, ok, _ in results if ok)
print("\n" + "=" * 60)
print(f"RESULT: {passed}/{len(results)} checks passed")
print("=" * 60)
sys.exit(0 if passed == len(results) else 1)
