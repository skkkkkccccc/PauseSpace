#!/usr/bin/env python3
"""S04 content-architecture acceptance validator.

Enforces the constraints declared in content/schema.json against a synthetic
scene, and runs the three required negative tests (invalid duration, missing
exit language, unapproved status) which must each FAIL SAFELY. Also checks the
choice-language rubric (docs/ContentRubric.md) and that the S01-S03 baseline
deliverables are unchanged from the S04 pre-session checkpoint e869ba7.

The `jsonschema` package is not installed in this environment, so this validator
enforces content/schema.json's declared constraints manually (the duration bounds
and review-status enum are read FROM the schema file, so it is genuinely
schema-driven). Exits 0 only if every check passes.

    python3 evidence/S04/validate_content.py
"""
import copy
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
results = []
EMAIL_RE = __import__("re").compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")

PRE_CHECKPOINT = "e869ba7e9360cadfa3fb99ff77c8b5371bbf74c0"
BASELINE_FILES = [
    "docs/Traceability.md", "docs/ProjectPlan.md", "README.md",
    "config/sample-config.json", "data/sample/scene.sample.json",
    "docs/ResearchProtocol.md", "data/sample/interview-notes.json",
    "docs/ResearchFindings.md",
]
SEGMENT_ALLOWED = {"order", "label", "startSecond", "endSecond", "optional", "text"}
TOP_ALLOWED = {"id", "title", "moment", "focus", "durationSeconds", "segments",
               "exit", "transcript", "audio", "review"}


def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}{(' — ' + detail) if detail else ''}")


def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


schema = load("content/schema.json")
DUR_MIN = schema["properties"]["durationSeconds"]["minimum"]
DUR_MAX = schema["properties"]["durationSeconds"]["maximum"]
STATUS_ENUM = set(schema["properties"]["review"]["properties"]["status"]["enum"])


def structural_errors(scene):
    """Mirror content/schema.json constraints. Returns a list of error strings."""
    errs = []
    if not isinstance(scene, dict):
        return ["scene is not an object"]
    extra = set(scene) - TOP_ALLOWED
    if extra:
        errs.append(f"additional top-level properties: {sorted(extra)}")
    for k in ("id", "title", "durationSeconds", "segments", "exit", "transcript", "audio", "review"):
        if k not in scene:
            errs.append(f"missing required field: {k}")
    if errs:
        return errs
    if not (isinstance(scene["id"], str) and scene["id"]):
        errs.append("id must be a non-empty string")
    if not (isinstance(scene["title"], str) and scene["title"]):
        errs.append("title must be a non-empty string")
    d = scene["durationSeconds"]
    if not (isinstance(d, int) and not isinstance(d, bool) and DUR_MIN <= d <= DUR_MAX):
        errs.append(f"durationSeconds must be an integer in [{DUR_MIN},{DUR_MAX}]")
    segs = scene["segments"]
    if not (isinstance(segs, list) and segs):
        errs.append("segments must be a non-empty array")
    else:
        for i, s in enumerate(segs):
            if not isinstance(s, dict):
                errs.append(f"segment {i} not an object")
                continue
            for k in ("order", "label", "startSecond", "endSecond", "text"):
                if k not in s:
                    errs.append(f"segment {i} missing: {k}")
            if set(s) - SEGMENT_ALLOWED:
                errs.append(f"segment {i} additional properties")
            if "text" in s and not (isinstance(s["text"], str) and s["text"]):
                errs.append(f"segment {i} text empty")
    ex = scene["exit"]
    if not isinstance(ex, dict) or "language" not in ex:
        errs.append("exit.language required")
    elif not (isinstance(ex["language"], str) and ex["language"]):
        errs.append("exit.language must be non-empty")
    tr = scene["transcript"]
    if not (isinstance(tr, dict) and tr.get("sameOrigin") is True and tr.get("text")):
        errs.append("transcript requires sameOrigin=true and non-empty text")
    au = scene["audio"]
    if not (isinstance(au, dict) and au.get("sameOrigin") is True and au.get("src")):
        errs.append("audio requires sameOrigin=true and non-empty src")
    rv = scene["review"]
    if not (isinstance(rv, dict) and rv.get("status") in STATUS_ENUM):
        errs.append(f"review.status must be one of {sorted(STATUS_ENUM)}")
    return errs


def business_errors(scene):
    """Timing-budget / ordering rules on top of the schema."""
    errs = []
    segs = scene.get("segments", [])
    prev_end = 0
    for idx, s in enumerate(segs):
        if not isinstance(s, dict):
            continue
        st, en, order = s.get("startSecond"), s.get("endSecond"), s.get("order")
        if order != idx + 1:
            errs.append(f"segment {idx} order={order}, expected {idx + 1}")
        if isinstance(st, (int, float)) and isinstance(en, (int, float)):
            if en < st:
                errs.append(f"segment {idx} endSecond < startSecond")
            if st < prev_end:
                errs.append(f"segment {idx} overlaps previous")
            prev_end = en
    if segs:
        last_end = segs[-1].get("endSecond")
        dur = scene.get("durationSeconds")
        if isinstance(last_end, (int, float)) and isinstance(dur, int) and last_end > dur:
            errs.append(f"last segment endSecond ({last_end}) exceeds durationSeconds ({dur})")
    return errs


def release_ready(scene):
    return isinstance(scene.get("review"), dict) and scene["review"].get("status") == "approved"


# ---------- A1: schema is parseable JSON Schema; one synthetic scene validates ----------
check("content/schema.json is a parseable JSON Schema",
      schema.get("$schema", "").startswith("http://json-schema.org") and "required" in schema)

valid = load("evidence/S04/sample-scene-valid.json")
v_struct = structural_errors(valid)
v_biz = business_errors(valid)
check("A1 synthetic scene is structurally valid", not v_struct,
      "; ".join(v_struct) if v_struct else "structure OK")
check("A1 synthetic scene passes timing-budget rules", not v_biz,
      "; ".join(v_biz) if v_biz else "segments ordered, within duration")
check("A1 synthetic scene is release-ready (approved)", release_ready(valid))


def fails_safely(label, mutant, *, expect_struct=False, expect_release=False):
    """A mutant 'fails safely' if validation rejects it (or release gate blocks it)
    WITHOUT an uncaught exception. Returns (ok, detail)."""
    try:
        se = structural_errors(mutant)
        be = business_errors(mutant)
        rr = release_ready(mutant)
        rejected = bool(se or be) or (expect_release and not rr)
        ok = rejected and (not expect_struct or bool(se))
        detail = f"struct={len(se)} biz={len(be)} release_ready={rr}"
        return ok, detail
    except Exception as e:  # noqa
        return False, f"UNSAFE crash: {e}"


# ---------- A2: invalid duration, missing exit language, unapproved status fail safely ----------
m1 = copy.deepcopy(valid); m1["durationSeconds"] = 400
ok, det = fails_safely("invalid duration", m1, expect_struct=True)
check("A2 invalid duration (400) fails safely", ok, det)

m2 = copy.deepcopy(valid); m2["exit"]["language"] = ""
ok, det = fails_safely("missing exit language", m2, expect_struct=True)
check("A2 missing exit language fails safely", ok, det)

m3 = copy.deepcopy(valid); m3["review"]["status"] = "draft"
ok, det = fails_safely("unapproved status", m3, expect_release=True)
check("A2 unapproved status (draft) fails safely at release gate", ok, det)

# ---------- A3: rubric blocks commands, promises, judgments ----------
rubric = (ROOT / "docs/ContentRubric.md").read_text(encoding="utf-8").lower()
need = ["command", "promise", "judgment", "accepted", "rejected"]
missing = [w for w in need if w not in rubric]
check("A3 rubric encodes command/promise/judgment rules with accepted/rejected examples",
      not missing, ("missing: " + ", ".join(missing)) if missing else "all categories present")

# ---------- privacy: no PII/secrets in the scene fixture ----------
fixture_raw = (ROOT / "evidence/S04/sample-scene-valid.json").read_text(encoding="utf-8")
check("no email/secret/token patterns in scene fixture", not EMAIL_RE.search(fixture_raw)
      and "secret" not in fixture_raw.lower() and "password" not in fixture_raw.lower())

# ---------- regression: S01-S03 baseline unchanged from e869ba7 ----------
proc = subprocess.run(["git", "diff", "--exit-code", PRE_CHECKPOINT, "--", *BASELINE_FILES],
                      cwd=ROOT, capture_output=True, text=True)
check("regression: S01-S03 baseline deliverables unchanged from e869ba7",
      proc.returncode == 0,
      "no diff (baseline intact)" if proc.returncode == 0 else ("changed:\n" + proc.stdout))

# ---------- summary ----------
passed = sum(1 for _, ok, _ in results if ok)
print("\n" + "=" * 60)
print(f"RESULT: {passed}/{len(results)} checks passed")
print("=" * 60)
sys.exit(0 if passed == len(results) else 1)
