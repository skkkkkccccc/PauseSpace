#!/usr/bin/env python3
"""S03 scene-evidence-synthesis acceptance validator.

Checks docs/ResearchFindings.md (four scene cards; each with Need, Evidence,
Inference, Risk, Design response; every claim traced to O-xx or [assumption];
no invented frequency; no PII/clinical terms) and the scene decision record in
docs/DecisionLog.md, then confirms the S01+S02 baseline deliverables are
unchanged from the verified S02 checkpoint fb146e9. Exits 0 only if all pass.

    python3 evidence/S03/validate_findings.py
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
results = []
CARDS = ["Scene 1", "Scene 2", "Scene 3", "Scene 4"]
CARD_LABELS = ["Need:", "Evidence:", "Inference:", "Risk:", "Design response:"]

# Frequency-invention patterns (counts/percentages/fractions/counted subjects).
FREQ_PATTERNS = [
    re.compile(r"\d+\s*%"),
    re.compile(r"\d+\s*/\s*\d+"),
    re.compile(r"\d+\s+out\s+of\s+\d+", re.I),
    re.compile(r"\b\d+\s+(participants?|users?|people|respondents?|students?|subjects?)\b", re.I),
    re.compile(r"\b(majority|minority|plurality)\b", re.I),
]
FORBIDDEN_TERMS = [
    "diagnos", "depress", "anxiety", "anxious", "mental health", "psycholog",
    "mood score", "medication", "trauma",
]
EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")


def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}{(' — ' + detail) if detail else ''}")


def read(rel):
    p = ROOT / rel
    return p.read_text(encoding="utf-8") if p.exists() else ""


def card_section(text, title):
    """Lines under a '### <title>' heading, up to the next ## or ### heading."""
    out, inside = [], False
    for ln in text.splitlines():
        if ln.startswith("### "):
            inside = ln[4:].startswith(title)
            continue
        if ln.startswith("## "):
            inside = False
            continue
        if inside:
            out.append(ln)
    return "\n".join(out)


findings = read("docs/ResearchFindings.md")
check("docs/ResearchFindings.md exists and is non-empty", bool(findings.strip()))

# A1: four cards, each with the five labels
for c in CARDS:
    sec = card_section(findings, c)
    check(f"card present: {c}", sec.strip() != "")
    missing = [lab for lab in CARD_LABELS if lab not in sec]
    check(f"{c} has Need/Evidence/Inference/Risk/Design response",
          not missing, ("missing: " + ", ".join(missing)) if missing else "all present")

# A2a: every Evidence line traces to O-xx or [assumption]
ev_lines = [ln for ln in findings.splitlines() if ln.lstrip().startswith("- Evidence:")]
bad_ev = [ln for ln in ev_lines if ("O-" not in ln and "[assumption]" not in ln.lower())]
check("every Evidence line traces to O-xx or [assumption]", not bad_ev,
      f"{len(bad_ev)} untraced" if bad_ev else f"{len(ev_lines)} evidence lines traced")

# A2b: no invented frequency
freq_hits = []
for pat in FREQ_PATTERNS:
    for m in pat.finditer(findings):
        freq_hits.append(m.group(0))
check("no invented frequency (no counts/%/fractions)", not freq_hits,
      ("found: " + ", ".join(sorted(set(freq_hits)))) if freq_hits else "clean")

# Privacy: no clinical/PII DATA terms in findings. The non-diagnostic boundary
# disclaimer ("not diagnosis, treatment, counselling...") is REQUIRED language
# (it states what PauseSpace is NOT) and is allowed; we scan only the rest.
def is_disclaimer(ln):
    ll = ln.lower()
    return ("not diagnosis" in ll or "diagnosis, treatment" in ll
            or "not a medical" in ll or "not diagnosis, treatment" in ll)

scan_text = "\n".join(ln for ln in findings.splitlines() if not is_disclaimer(ln))
low = scan_text.lower()
term_hits = [t for t in FORBIDDEN_TERMS if t in low]
check("no clinical/PII data terms in findings (boundary disclaimer allowed)",
      not term_hits and not EMAIL_RE.search(findings),
      ("terms: " + ", ".join(term_hits)) if term_hits else "clean")

# Scene decision record present in DecisionLog
dl = read("docs/DecisionLog.md")
check("scene decision record present in docs/DecisionLog.md",
      "four-scene decision record" in dl.lower() or "four-scene decision" in dl.lower())

# Regression: S01+S02 baseline deliverables unchanged from fb146e9
S02_CHECKPOINT = "fb146e9922aad642757dafc7a826d2ced92ba94c"
baseline_files = [
    "docs/Traceability.md", "docs/ProjectPlan.md", "README.md",
    "config/sample-config.json", "data/sample/scene.sample.json",
    "docs/ResearchProtocol.md", "data/sample/interview-notes.json",
]
proc = subprocess.run(
    ["git", "diff", "--exit-code", S02_CHECKPOINT, "--", *baseline_files],
    cwd=ROOT, capture_output=True, text=True)
check("regression: S01+S02 baseline deliverables unchanged from fb146e9",
      proc.returncode == 0,
      "no diff (baseline intact)" if proc.returncode == 0 else ("changed:\n" + proc.stdout))

# Summary
passed = sum(1 for _, ok, _ in results if ok)
print("\n" + "=" * 60)
print(f"RESULT: {passed}/{len(results)} checks passed")
print("=" * 60)
sys.exit(0 if passed == len(results) else 1)
