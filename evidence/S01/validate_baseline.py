#!/usr/bin/env python3
"""S01 baseline acceptance validator.

Checks the S01 deliverables against acceptance criteria A1-A3. Prints a
PASS/FAIL report. Exits 0 only if every check passes. Run from the repo root:

    python3 evidence/S01/validate_baseline.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXPECT = [f"B-{i:02d}" for i in range(1, 15)]  # B-01..B-14
EXPECT_UNITS = [f"S{i:02d}" for i in range(1, 23)]  # S01..S22

results = []


def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))
    flag = "PASS" if ok else "FAIL"
    print(f"[{flag}] {name}{(' — ' + detail) if detail else ''}")


def read(rel):
    p = ROOT / rel
    return p.read_text(encoding="utf-8") if p.exists() else ""


trace = read("docs/Traceability.md")
plan = read("docs/ProjectPlan.md")
tasks = read("TASKS.md")
readme = read("README.md")

# --- A1: every B-01..B-14 present in BOTH tables with the four required fields ---
# Table A holds owner + status + category; Table B holds impl path + verification + measure.
# Structural check: each ID appears in Table A and in Table B sections.
table_a = trace.split("## Table B")[0]  # everything before Table B (includes legend + Table A)
table_b = trace.split("## Table B")[1].split("## Non-goals")[0] if "## Table B" in trace else ""

missing_a = [b for b in EXPECT if b not in table_a]
missing_b = [b for b in EXPECT if b not in table_b]
check("A1a every B-01..B-14 present in Table A (requirement+category+owner+status)",
      not missing_a, ("missing: " + ", ".join(missing_a)) if missing_a else "all 14 present")
check("A1b every B-01..B-14 present in Table B (impl path+verification+measure)",
      not missing_b, ("missing: " + ", ".join(missing_b)) if missing_b else "all 14 present")

# Category labels explicitly separated
cats = ["Mandatory", "Recommended", "Enhancement", "Out-of-scope"]
missing_cats = [c for c in cats if c.lower() not in trace.lower()]
check("A1c all four category labels present (mandatory/recommended/enhancement/out-of-scope)",
      not missing_cats, ("missing: " + ", ".join(missing_cats)) if missing_cats else "all present")

# --- A2: scope freeze, no silent change ---
proposal_elements = [
    "four scenes", "anonymous", "local-only progress", "original",
    "co-build log", "six-week", "poster", "two-minute video",
]
missing_elems = [e for e in proposal_elements if e.lower() not in plan.lower()]
check("A2a ProjectPlan locks all eight proposal elements",
      not missing_elems, ("missing: " + ", ".join(missing_elems)) if missing_elems else "all 8 locked")

nongoals = ["account", "backend", "analytics", "microphone", "diagnosis", "streak"]
missing_ng = [n for n in nongoals if n.lower() not in plan.lower()]
check("A2b ProjectPlan lists explicit non-goals",
      not missing_ng, ("missing terms: " + ", ".join(missing_ng)) if missing_ng else "key non-goals present")

# README boundaries unchanged (still contains the core no-X list)
boundary_terms = ["No account", "backend", "analytics", "microphone capture", "diagnosis"]
missing_boundary = [t for t in boundary_terms if t.lower() not in readme.lower()]
check("A2c README.md boundaries preserved (no silent scope change)",
      not missing_boundary, ("missing: " + ", ".join(missing_boundary)) if missing_boundary else "boundaries intact")

# --- supporting checks ---
# JSON samples parse
for jf in ["config/sample-config.json", "data/sample/scene.sample.json"]:
    try:
        json.loads(read(jf))
        check(f"JSON valid: {jf}", True)
    except Exception as e:  # noqa
        check(f"JSON valid: {jf}", False, str(e))

# TASKS.md integrity: 22-unit checklist S01..S22 preserved, S01 active
units = re.findall(r"- \[ \] (S\d{2})", tasks)
check("TASKS.md S01-S22 checklist intact (22 unchecked units)",
      sorted(units) == EXPECT_UNITS, f"{len(units)} units found")
check("TASKS.md current unit is S01", "Unit code: S01" in tasks)
check("TASKS.md known issues preserved",
      "Deployment host" in tasks and "support contacts" in tasks)

# Evidence + checkpoint references exist in the workspace
check("Pre-session checkpoint recorded (evidence/S01/checkpoint-pre.txt)",
      (ROOT / "evidence/S01/checkpoint-pre.txt").exists())

# --- summary ---
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 60)
print(f"RESULT: {passed}/{total} checks passed")
print("=" * 60)
sys.exit(0 if passed == total else 1)
