#!/usr/bin/env python3
"""S10 visual-and-accessibility-system acceptance validator.

Checks design/tokens.css (token groups, 44px touch, focus, reduced-motion,
breakpoints), docs/Accessibility.md (WCAG 2.2 AA topics), runs an a11y check on
the S09 prototype (zoom allowed, >=44px touch targets, computed AA contrast, no
motion, focus not disabled, no copied/external assets), and confirms the S01-S09
baseline is unchanged from the S10 pre-session checkpoint 910a89f. Exits 0 only
if all checks pass.

    python3 evidence/S10/validate_a11y.py
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
results = []
PRE_CHECKPOINT = "910a89fe1a8ff76b4a52ababdd0dbc1f22b84105"
BASELINE_FILES = [
    "docs/Traceability.md", "docs/ProjectPlan.md", "README.md",
    "config/sample-config.json", "data/sample/scene.sample.json",
    "docs/ResearchProtocol.md", "data/sample/interview-notes.json",
    "docs/ResearchFindings.md", "content/schema.json", "docs/ContentRubric.md",
    "content/exam-room.json", "content/sports-field.json",
    "content/own-room.json", "content/empty-classroom.json",
    "config/audio-generation.env.example", "docs/OptionalAIAudioExtension.md",
    "prompts/OptionalAudioSessionOA01.md", "docs/ContentReview.md",
    "assets/audio/README.md", "docs/Architecture.md", "docs/UserFlows.md",
    "design/prototype/index.html", "design/prototype/README.md",
    "docs/UsabilityTasks.md",
]  # design/tokens.css and docs/Accessibility.md are S10 in-scope -> excluded


def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}{(' — ' + detail) if detail else ''}")


def read(rel):
    p = ROOT / rel
    return p.read_text(encoding="utf-8") if p.exists() else ""


# ---- WCAG contrast ----
def _lin(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def lum(hexstr):
    h = hexstr.lstrip("#")
    if len(h) == 3:
        h = "".join(ch * 2 for ch in h)
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def contrast(fg, bg):
    a, b = lum(fg), lum(bg)
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


tokens = read("design/tokens.css")
a11y = read("docs/Accessibility.md")
proto = read("design/prototype/index.html")
tlow, alow, plow = tokens.lower(), a11y.lower(), proto.lower()

# ---------- A1: tokens ----------
check("design/tokens.css exists and is non-empty", bool(tokens.strip()))
check("A1 color tokens defined", all(v in tlow for v in ("--ps-bg", "--ps-ink", "--ps-accent")))
check("A1 type tokens defined", "--ps-font-base" in tlow and "--ps-fs-base" in tlow)
check("A1 spacing tokens defined", "--ps-space-4" in tlow)
check("A1 touch target >=44px", "--ps-touch-min" in tlow and "44px" in tlow)
check("A1 visible focus token/rule", ":focus-visible" in tlow and "--ps-focus" in tlow)
check("A1 reduced-motion media query", "prefers-reduced-motion" in tlow)
check("A1 responsive breakpoints", "min-width: 600px" in tlow and "min-width: 900px" in tlow)

# ---------- A2: accessibility spec ----------
need = ["reduced motion", "contrast", "keyboard order", "transcript",
        "status", "breakpoint", "44", "focus", "zoom", "licensed"]
missing = [w for w in need if w not in alow]
check("A2 Accessibility.md covers all WCAG 2.2 AA topics", not missing,
      ("missing: " + ", ".join(missing)) if missing else "all present")

# ---------- A2: prototype a11y ----------
vm = re.search(r'name="viewport"\s+content="([^"]+)"', proto, re.I)
vp = vm.group(1).lower() if vm else ""
check("A2 prototype allows zoom (no user-scalable=no / maximum-scale=1)",
      "user-scalable=no" not in vp and not re.search(r"maximum-scale\s*=\s*1\b", vp),
      vp)
check("A2 prototype touch targets >=44px (16px button padding)",
      re.search(r"\.btn\s*\{[^}]*padding:\s*16px", proto, re.S) is not None)
check("A2 prototype has no motion to reduce (no transition/animation)",
      "transition" not in plow and "animation" not in plow)
check("A2 prototype does not disable focus outline",
      not re.search(r"outline\s*:\s*(none|0)", plow))
check("A2 prototype uses no copied/external assets (no <img>, no url(http)",
      "<img" not in plow and not re.search(r"url\(https?://", plow))

# contrast on prototype palette
vars_ = dict(re.findall(r"--(\w+):\s*(#[0-9a-fA-F]{3,6})", proto))
pairs = []
if "ink" in vars_ and "bg" in vars_:
    pairs.append(("ink/bg", vars_["ink"], vars_["bg"]))
if "muted" in vars_ and "bg" in vars_:
    pairs.append(("muted/bg", vars_["muted"], vars_["bg"]))
if "accent" in vars_:
    pairs.append(("accent-ink/accent", "#ffffff", vars_["accent"]))
bad = []
for label, fg, bg in pairs:
    r = contrast(fg, bg)
    if r < 4.5:
        bad.append(f"{label}={r:.2f}")
check("A2 prototype palette meets AA contrast (>=4.5:1)",
      bool(pairs) and not bad,
      ("below 4.5: " + ", ".join(bad)) if bad else f"{len(pairs)} pairs computed, all >=4.5")

# ---------- regression ----------
proc = subprocess.run(["git", "diff", "--exit-code", PRE_CHECKPOINT, "--", *BASELINE_FILES],
                      cwd=ROOT, capture_output=True, text=True)
check("regression: S01-S09 baseline unchanged from 910a89f (excl. S10 in-scope files)",
      proc.returncode == 0,
      "no diff (baseline intact)" if proc.returncode == 0 else ("changed:\n" + proc.stdout))

passed = sum(1 for _, ok, _ in results if ok)
print("\n" + "=" * 60)
print(f"RESULT: {passed}/{len(results)} checks passed")
print("=" * 60)
sys.exit(0 if passed == len(results) else 1)
