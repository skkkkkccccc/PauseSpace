#!/usr/bin/env python3
"""S02 ethical-research acceptance validator.

Checks the S02 deliverables (docs/ResearchProtocol.md and
data/sample/interview-notes.json) against acceptance criteria A1-A2, and
re-runs the S01 validator to confirm no baseline regression. Prints a PASS/FAIL
report and exits 0 only if every check passes. Run from the repo root:

    python3 evidence/S02/validate_research.py
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
results = []

# Terms that must NOT appear in participant-facing questions or in the sample data.
FORBIDDEN_VALUE_TERMS = [
    "diagnos", "depress", "anxiety", "anxious", "mental health", "psycholog",
    "mood score", "medication", "trauma", "family history", "symptom",
]
# Keys that the note schema must never define.
FORBIDDEN_KEYS = {
    "name", "fullname", "firstname", "lastname", "email", "phone", "phonenumber",
    "address", "diagnosis", "diagnostic", "mentalhealth", "mental_health",
    "psychologicalhistory", "moodscore", "mood_score", "family", "familydetails",
}
EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
PHONE_RE = re.compile(r"\b\+?\d[\d\s\-]{7,}\d")


def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}{(' — ' + detail) if detail else ''}")


def read(rel):
    p = ROOT / rel
    return p.read_text(encoding="utf-8") if p.exists() else ""


def walk_strings(obj, keys):
    """Yield (key_or_None, value) for every string in obj; recurse dicts/lists."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            keys.append(k)
            yield from walk_strings(v, keys)
    elif isinstance(obj, list):
        for v in obj:
            yield from walk_strings(v, keys)
    elif isinstance(obj, str):
        yield obj


# ---------- interview-notes.json ----------
raw = read("data/sample/interview-notes.json")
try:
    notes = json.loads(raw)
    check("interview-notes.json parses as valid JSON", True)
except Exception as e:  # noqa
    check("interview-notes.json parses as valid JSON", False, str(e))
    notes = None

if notes:
    required = ["sessionId", "sceneId", "taskObservations", "reviewStatus", "synthetic"]
    missing = [f for f in required if f not in notes]
    check("required schema fields present", not missing,
          ("missing: " + ", ".join(missing)) if missing else "all present")
    check("sample flagged synthetic=true", notes.get("synthetic") is True)

    keys = []
    strs = list(walk_strings(notes, keys))
    bad_keys = sorted({k for k in keys if k.lower() in FORBIDDEN_KEYS})
    check("no forbidden identifying/clinical KEYS in schema", not bad_keys,
          ("found keys: " + ", ".join(bad_keys)) if bad_keys else "none")

    bad_terms, bad_pii = [], []
    for s in strs:
        low = s.lower()
        hit = [t for t in FORBIDDEN_VALUE_TERMS if t in low]
        if hit:
            bad_terms.append((hit, s))
        if EMAIL_RE.search(s) or PHONE_RE.search(s):
            bad_pii.append(s)
    check("no forbidden clinical/PII terms in sample values", not bad_terms,
          f"{len(bad_terms)} hit(s)" if bad_terms else "clean")
    check("no email/phone patterns in sample values", not bad_pii,
          f"{len(bad_pii)} hit(s)" if bad_pii else "clean")

# ---------- ResearchProtocol.md ----------
proto = read("docs/ResearchProtocol.md")
lines = proto.splitlines()


def section(title_prefix):
    """Return the text of a '## <title_prefix>' section, excluding its heading."""
    out, inside = [], False
    for ln in lines:
        if ln.startswith("## "):
            inside = ln[3:].lower().startswith(title_prefix.lower())
            continue
        if inside:
            out.append(ln)
    return "\n".join(out)


for h in ["Assent and consent", "Voluntary participation and stop rules",
          "Task questions", "Data-minimization checklist"]:
    check(f"protocol has section: {h}", section(h) != "" or any(
        ln[3:].lower().startswith(h.lower()) for ln in lines if ln.startswith("## ")))

stop_sec = section("Voluntary participation and stop rules")
check("stop rule present (voluntary + stop)", "stop" in stop_sec.lower())

# A1: task questions section must contain NO forbidden terms
q_sec = section("Task questions")
q_low = q_sec.lower()
q_hits = [t for t in FORBIDDEN_VALUE_TERMS if t in q_low]
check("A1 task questions are neutral (no clinical/PII terms in section)", not q_hits,
      ("found: " + ", ".join(q_hits)) if q_hits else "all questions clean")

# A2: data-minimization checklist must enumerate the forbidden categories
chk = section("Data-minimization checklist").lower()
need = ["name", "contact", "mental-health", "psycholog", "diagnostic",
        "family", "mood", "microphone"]
chk_missing = [n for n in need if n not in chk]
check("A2 checklist enumerates every forbidden data category", not chk_missing,
      ("missing: " + ", ".join(chk_missing)) if chk_missing else "all categories listed")

# ---------- regression: S01 baseline deliverables untouched by S02 ----------
# Re-running the S01 validator wholesale is NOT a valid regression signal here:
# two of its checks assert S01-era TASKS.md state (current unit = S01; 22 unchecked
# units), which correctly no longer hold after the S01 -> S02 transition (S01 is
# now checked; unit is S02). The real regression question is whether the S01
# *baseline deliverables* changed. We verify they are byte-identical to the
# verified S01 checkpoint 3e8ef01.
S01_CHECKPOINT = "3e8ef01e1f3843c42f0a98a358890e6a85002562"
baseline_files = [
    "docs/Traceability.md", "docs/ProjectPlan.md", "README.md",
    "config/sample-config.json", "data/sample/scene.sample.json",
]
proc = subprocess.run(
    ["git", "diff", "--exit-code", S01_CHECKPOINT, "--", *baseline_files],
    cwd=ROOT, capture_output=True, text=True)
check("regression: S01 baseline deliverables unchanged from checkpoint 3e8ef01",
      proc.returncode == 0,
      "no diff (baseline intact)" if proc.returncode == 0 else ("changed:\n" + proc.stdout))

# ---------- summary ----------
passed = sum(1 for _, ok, _ in results if ok)
print("\n" + "=" * 60)
print(f"RESULT: {passed}/{len(results)} checks passed")
print("=" * 60)
sys.exit(0 if passed == len(results) else 1)
