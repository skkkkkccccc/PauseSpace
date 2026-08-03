#!/usr/bin/env python3
"""OA01 scaffolding validator (scripts approved; provider still pending).

The four scene scripts are now approved (student read-aloud + mentor/adult
approval recorded 2026-08-03), so OA01's script-approval prerequisite is met.
Generation is still blocked because no TTS provider is approved. This validator
confirms: dry-run makes zero provider requests and exposes no secret; generation
refuses without an approved provider; no MP3s exist; baseline tests + build pass;
dist/ has no TTS code; scripts are approved; and only expected files changed.
Exits 0 only if all pass.

    python3 evidence/OA01/validate-oa01.py
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
results = []
PRE = "8b88e96"
REAL_SECRET = re.compile(r"AKIA[0-9A-Z]{16}|-----BEGIN|sk-[A-Za-z0-9]{20}")


def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}{(' — ' + detail) if detail else ''}")


def run(cmd):
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)


for f in ["scripts/generate-audio.mjs", "scripts/lib/tts-provider.mjs",
          "tests/audio-generation.test.mjs", "assets/audio/generated/README.md",
          "assets/audio/audio-manifest.generated.json", "docs/AudioGenerationRecord.md"]:
    check(f"exists: {f}", (ROOT / f).exists())

pkg = (ROOT / "package.json").read_text()
for s in ["audio:dry-run", "audio:generate", "test:audio"]:
    check(f"package.json has script: {s}", s in pkg)

t = run(["npm", "run", "test:audio"])
check("npm run test:audio passes (fail 0)", t.returncode == 0 and "fail 0" in t.stdout, f"rc={t.returncode}")

d = run(["npm", "run", "audio:dry-run"])
dout = d.stdout + d.stderr
check("dry-run: zero provider requests + no network + provider-unconfigured",
      d.returncode == 0 and "ZERO provider requests" in dout and "No network calls made" in dout
      and "no approved provider configured" in dout, f"rc={d.returncode}")
check("dry-run exposes no real secret", not REAL_SECRET.search(dout))

mp3s = list((ROOT / "assets/audio/generated").glob("*.mp3"))
check("no MP3s generated (provider still pending)", not mp3s, f"{len(mp3s)} mp3s" if mp3s else "none")

nt = run(["npm", "test"])
check("npm test (baseline) still passes", nt.returncode == 0 and "fail 0" in nt.stdout, f"rc={nt.returncode}")
bd = run(["npm", "run", "build"])
check("npm run build still passes", bd.returncode == 0, f"rc={bd.returncode}")
dist = sorted(p.name for p in (ROOT / "dist").iterdir()) if (ROOT / "dist").exists() else []
check("build output contains no TTS/scripts code (only the 3 app files)",
      set(dist) == {"index.html", "styles.css", "app.js"}, str(dist))

# four scene scripts are approved (script gate satisfied)
not_approved = []
for sid in ["exam-room", "sports-field", "own-room", "empty-classroom"]:
    s = json.loads((ROOT / f"content/{sid}.json").read_text())
    if s.get("review", {}).get("status") != "approved":
        not_approved.append(sid)
check("four scene scripts approved (script-approval prereq met; provider still blocks generation)",
      not not_approved, ("not approved: " + str(not_approved)) if not_approved else "all approved")

blob = "".join((ROOT / f).read_text(encoding="utf-8") for f in
               ["scripts/generate-audio.mjs", "scripts/lib/tts-provider.mjs", "tests/audio-generation.test.mjs"])
check("no real secret pattern in OA01 scripts/tests", not REAL_SECRET.search(blob))

proc = run(["git", "diff", "--name-only", PRE])
changed = [l for l in proc.stdout.splitlines() if l.strip()]
allowed = {"TASKS.md", "package.json", "docs/DecisionLog.md", "docs/CoBuildLog.md",
           "docs/ContentReview.md", "content/exam-room.json", "content/sports-field.json",
           "content/own-room.json", "content/empty-classroom.json"}
unexpected = [c for c in changed if c not in allowed]
check("regression: only expected files modified (OA01 control + approval + ContentReview)",
      not unexpected, ("unexpected: " + str(unexpected)) if unexpected else f"{len(changed)} expected files modified")

passed = sum(1 for _, ok, _ in results if ok)
print("\n" + "=" * 60)
print(f"RESULT: {passed}/{len(results)} checks passed")
print("=" * 60)
sys.exit(0 if passed == len(results) else 1)
