# Traceability — PauseSpace baseline ledger (B-01–B-14)

> **Status: FROZEN at S01 (2026-07-28) — pending student line-by-line approval.**
> This ledger is the AI implementation partner's extraction of the documented
> PauseSpace constraints into baseline requirements B-01–B-14. It is paired with
> `docs/ProjectPlan.md` (the locked proposal ledger). The student must compare
> every row and every non-goal with the proposal and personally approve them
> before the baseline is marked "approved." Until then status is "frozen, pending
> student approval."

## How to read this ledger
- **Category:** Mandatory | Recommended | Enhancement (deferred) | Out-of-scope.
- **Status:** Defined (captured, not yet implemented) · Boundary (non-negotiable, enforced throughout) · Pending (needs external input) · Active (in progress).
- **Owner:** Student · Mentor/Adult reviewer · Student + Mentor/Adult.
- Every B-ID appears in **Table A** (requirement + category + source + owner + status) **and** **Table B** (implementation path + verification method + success measure). Tables join on ID.

## Table A — Master matrix

| ID | Baseline requirement | Category | Source | Owner | Status |
|---|---|---|---|---|---|
| B-01 | Four ~3-minute, scene-based attention-reset experiences (one per approved scene), for high-school students | Mandatory | README, TASKS, ProjectPlan | Student + Mentor/Adult | Defined; scripts pending |
| B-02 | Mobile-first static Web App (HTML/CSS/JS); no backend | Mandatory | README, Architecture | Student | Defined; repo scaffold later (S11) |
| B-03 | Five-view product structure preserved | Mandatory | TASKS | Student | Defined; view map needs student confirmation |
| B-04 | Anonymous use: no account, login, or identity collection | Mandatory (boundary) | README, TASKS | Student | Boundary; enforced |
| B-05 | Local-only progress via validated localStorage; no sync/analytics/trackers/streak/ranking | Mandatory (boundary) | README, TASKS, Architecture | Student | Boundary; schema later |
| B-06 | No microphone capture; no runtime AI counselling/chat | Mandatory (boundary) | README, TASKS | Student | Boundary; enforced |
| B-07 | Original same-origin MP3 audio + original visuals; licensing respected | Mandatory | ProjectPlan, Architecture | Student + Mentor/Adult | Defined; assets produced later |
| B-08 | Versioned scene JSON + same-origin transcripts; `contentVersion` tracked | Mandatory | Architecture, config/sample-config.json | Student | Defined; content authored later |
| B-09 | Non-diagnostic boundary: not diagnosis/treatment/counselling/emergency support | Mandatory (safety) | README, TASKS | Student + Mentor/Adult | Boundary; copy review at release |
| B-10 | Age-appropriate, mentor/adult-approved support contacts and content | Mandatory | README, TASKS | Mentor/Adult | Pending approval before S15 gate |
| B-11 | Accessibility: reduced motion, contrast, keyboard focus order, touch targets, transcripts, status messaging, responsive breakpoints | Mandatory | TestPlan, Phase3Session10 | Student | Defined; tokens/spec later (S10) |
| B-12 | Deterministic player state; optional PWA shell for offline use | Mandatory (state) / Recommended (PWA shell) | Architecture | Student | Defined; implemented later |
| B-13 | Full test-plan coverage executed; never mark an unrun test as passing | Mandatory | TestPlan, RELEASE_CHECKLIST | Student | Plan exists; tests run in later sessions |
| B-14 | Six-week delivery with student revision, read-aloud testing, and adult approval; deliverables: poster, two-minute video, defense, manifest; AI Co-build Log maintained | Mandatory | ProjectPlan, RELEASE_CHECKLIST | Student + Mentor/Adult | Active; Co-build Log started |

## Table B — Implementation path, verification, success measure

| ID | Implementation path (later sessions) | Verification method | Success measure |
|---|---|---|---|
| B-01 | Versioned scene JSON (`data/scenes/*`) + transcript + same-origin MP3 per scene; per-scene player view | `scene count == 4`; each `durationSeconds ≈ 180`; transcript + audio + `review.status` present; manual read-aloud | 4 scenes, ~3 min each, content + accessibility reviewed |
| B-02 | `index.html` + app JS/CSS; deterministic run/lint/test/build scripts (S11) | opens via static serve; no backend calls; mobile-first viewport check | loads offline-capable on a phone browser; lint + test + build pass |
| B-03 | 5-view router/view set (candidate: Welcome, Scene select, Player, Support, About/Progress — **TBC by student**) | exactly 5 views; deterministic navigation; each reachable | 5 views match the student-approved map; each reachable & responsive |
| B-04 | No auth/identity code or identity fields in any form/storage | privacy/security scan; no login UI present | zero identity collection; privacy review pass |
| B-05 | Validated localStorage (key `pausespace.progress.v1`); input validation; no outbound requests | storage audit; network panel shows no egress; schema validation tests | progress persists, validates/rejects bad input, zero network egress |
| B-06 | No `getUserMedia`/microphone APIs; no LLM/runtime-chat client | code scan for mic/AI-client APIs; manual check | no microphone permission requested; no runtime AI chat |
| B-07 | `assets/audio/*.mp3` same-origin; original art (S10); asset manifest with origin + license per asset | manifest complete; no externally-hosted media; licensing review | 100% original or properly licensed, all same-origin, manifest complete |
| B-08 | Versioned scene JSON (`contentVersion: 1`) + transcripts; schema validation | schema validation tests; transcript per scene; content review | all scenes conform to schema; transcripts present & reviewed |
| B-09 | Disclaimer/support copy; no diagnostic language; only approved support contacts | copy review for diagnostic/treatment claims; safety review | all public copy passes non-diagnostic review |
| B-10 | Support view with approved contacts; age-appropriateness review | only approved contacts shown; content suitability review | support contacts approved by mentor/adult; content age-appropriate |
| B-11 | `design/tokens.css` + `docs/Accessibility.md` (S10); implement per WCAG considerations | accessibility tests (keyboard, contrast, reduced motion, screen-reader status); device checks | passes accessibility checklist; works with assistive tech |
| B-12 | Deterministic player state machine; optional service worker + manifest | state-determinism tests; offline smoke test (if PWA included) | deterministic playback; offline-capable if PWA included |
| B-13 | Test suites per layer; local/CI run scripts; evidence saved per session | each layer has recorded pass evidence; no unrun test marked passing | all test layers have real pass evidence at release |
| B-14 | S01–S22 session plan; per-session evidence; release checklist; Co-build Log | checklist complete; log current; deliverables exist | release checklist fully checked; Co-build Log complete; deliverables delivered |

## Non-goals (explicitly out-of-scope for v1)
- No account, login, or identity collection.
- No backend, database, or cloud sync.
- No analytics, trackers, mood scores, streaks, or rankings.
- No microphone capture; no runtime AI counselling/chat.
- No diagnosis, treatment, counselling, or emergency-support claims.
- No forced breathing, autoplay, or unreviewed support contacts.
- No copied or unlicensed imagery/audio; no identifying participant data.
- No implementation of a future session before the current session passes acceptance.

## Enhancements (deferred — not in the v1 baseline)
These are acknowledged but explicitly **not** in v1. Adopting any of them requires a
new Decision Log entry and re-baselining with student approval:
- More than four scenes.
- Optional gentle reminder/scheduling.
- Additional languages/localization.

## Unresolved decisions (tracked; not blocking S01 freeze)
| ID | Decision needed | Owner | By when |
|---|---|---|---|
| D1 | Confirm the exact five views against the proposal (B-03) | Student | Before view implementation |
| D2 | Choose the deployment host (B-02, B-13) | Student + Mentor | Before S21 |
| D3 | Approve locally approved support contacts (B-10) | Mentor/Adult | Before S15 release gate |
| D4 | Set the browser/device test matrix — local machine has Safari + Chrome only; Edge/Firefox absent (B-13) | Student + Mentor | Before release testing |
| D5 | Decide original-MP3 production/voice approach (B-07) | Student + Mentor | In content sessions |
| D6 | Include the optional PWA/offline shell in v1, or defer (B-12) | Student | Before offline testing |
| D7 | Student personally approves every non-goal and signs off the baseline (manual gate) | Student | S01 acceptance |

## Source grounding (no silent scope change)
Each B-ID is traceable to existing, committed documentation — README.md, TASKS.md
(Global Rules), docs/Architecture.md, docs/ProjectPlan.md, docs/TestPlan.md,
RELEASE_CHECKLIST.md, and the relevant session prompts. No new product capability
was added by this ledger; it only makes the already-approved scope explicit and
testable.
