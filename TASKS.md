# TASKS.md - PauseSpace

## Project Goal
Build PauseSpace as a privacy-first, static, scene-based attention-reset Web App, aligned to the approved 22-session course plan.

## Global Rules
- Preserve the four approved scenes and the five-view product structure.
- No account, backend, database, analytics, mood score, microphone capture, runtime AI counselling, streak, or ranking.
- Do not present PauseSpace as diagnosis, treatment, counselling, or emergency support.
- Use only synthetic or properly anonymized research data.
- All final scripts, recordings, support wording, and public claims require student revision and mentor/adult review.
- No secrets, credentials, private research notes, or identifying participant data in Git.
- Do not implement a future session before the current session passes acceptance.

## Current Unit
Unit code: S10
Unit focus: Visual and accessibility system
Current prompt:

```markdown
# S10 - Visual and accessibility system

## Role
Act as the implementation partner for this bounded PauseSpace InnovationLab session. Preserve student ownership and the approved static, privacy-first architecture.

## Read First
Open README.md, TASKS.md, docs/ProjectPlan.md, docs/Architecture.md, docs/DecisionLog.md, the listed in-scope files, and current tests. Inspect before proposing changes.

## Current State
Confirm the repository checkpoint and report what already works, failing tests, known issues, and active task S10 / P3. Do not assume missing work is complete.

## Session Objective
Define original art direction, tokens, reduced motion, focus and touch targets.

## Scope
In scope: design/tokens.css; docs/Accessibility.md. Make only changes required for “Visual and accessibility system”. Preserve all working behavior outside this boundary.

## Requirements
Define original color/type/spacing/touch/focus tokens; specify reduced motion, contrast, keyboard order, transcripts, status messaging, and responsive breakpoints. Keep the four authoritative scenes and the approved static, local-first, non-diagnostic boundary; use synthetic or properly anonymized data only.

## Implementation Sequence
1) Verify baseline and tests. 2) Create a checkpoint. 3) State the smallest runnable change. 4) Implement in small steps. 5) Run focused tests after each step. 6) Run the session acceptance checks. 7) Update TASKS, Decision Log and Co-build Log.

## Files
Create or modify only: design/tokens.css; docs/Accessibility.md. Explicitly preserve deployed assets, approved scripts, unrelated styles, test evidence and prior decisions.

## Tests and Acceptance Criteria
Acceptance gate: WCAG 2.2 AA-oriented checklist passes prototype review. Run the accessibility checklist on the prototype; verify focus visibility, 44px-class touch targets, contrast, zoom, reduced motion, and original/licensed assets. Report exact commands, expected versus actual results, manual checks, and evidence paths. Never invent passing results.

## Evidence to Save
Save dated evidence under evidence/S10/: relevant screenshots or recordings, command/test output, reviewed artifacts, defect references, and the pre/post-session checkpoint IDs. Do not save personal or identifying data.

## Student Manual Work
Student chooses the visual direction, checks it on a phone, and documents asset provenance. The student must review every diff and write the final Co-build Log decision in their own words.

## Security and Safety
Do not collect names, mental-health histories, family details, mood scores, microphone data, analytics identifiers, or secrets. Do not add diagnosis, treatment, emergency promises, forced breathing, autoplay, or unreviewed support contacts.

## Do Not Do
Do not add frameworks, backend, login, AI runtime chat, cloud sync, trackers, streaks, rankings, unrelated refactors, hidden scope, hard-coded secrets, copied imagery, or the next session’s work.

## TASKS.md Session Activation
Before implementation, update only the editable fields in `TASKS.md`:
- `Unit code: S10`
- `Unit focus: Visual and accessibility system`
- `Current prompt: paste this complete S10 prompt only`
- Replace the three placeholder acceptance lines with this session's observable acceptance criteria.

Do not recreate or overwrite `TASKS.md`. Preserve the full S01-S22 checklist, completed checkmarks, known issues, and last test evidence. After acceptance passes, mark only S10 complete, record actual evidence, and set the next unit only as preparation.

## Checkpoint and Rollback
Record the pre-session checkpoint identifier. If acceptance fails, keep the last runnable state, log the defect, and provide the exact rollback path without erasing evidence.

## Completion Report
List changed files; summarize decisions; show tests and manual checks; identify limitations and unresolved risks; update traceability; name the next safe step without implementing it.

## Stop Condition
Stop when S10 acceptance criteria pass and evidence is saved. Do not begin the next session.
```

## Acceptance Criteria for Current Unit
- A1 — Design tokens: `design/tokens.css` defines original color/type/spacing tokens, a `--touch-min` of at least 44px, a visible-focus token/rule, a reduced-motion media query, and responsive breakpoints. (Auto-verifiable.)
- A2 — Accessibility spec + prototype a11y check: `docs/Accessibility.md` is a WCAG 2.2 AA-oriented checklist (reduced motion, contrast, keyboard order, transcripts, status messaging, breakpoints, touch, focus, zoom, original/licensed assets); the automated check on the prototype passes (zoom allowed, ≥44px touch targets, AA contrast, no motion, focus not disabled, no copied/external assets). (Auto-verifiable; the student phone check is the manual gate.)
- A3 — Evidence + sign-off: pre/post checkpoint IDs and check output saved under `evidence/S10/`; the student chooses the visual direction, checks it on a phone, and documents asset provenance — student-owned manual gates. (Manual, student-owned gate.)

## Completed Units
- [x] S01
- [x] S02
- [x] S03
- [x] S04
- [x] S05
- [x] S06
- [x] S07
- [x] S08
- [x] S09
- [ ] S10
- [ ] S11
- [ ] S12
- [ ] S13
- [ ] S14
- [ ] S15
- [ ] S16
- [ ] S17
- [ ] S18
- [ ] S19
- [ ] S20
- [ ] S21
- [ ] S22

## Known Issues
- Deployment host; owner: student and mentor; next action: decide before S21.
- Locally approved support contacts; owner: mentor/adult reviewer; next action: approve before S15 release gate.

## Last Test Evidence
- Automated (S10): `evidence/S10/a11y-checks.txt` — 16/16 PASS (validator `evidence/S10/validate_a11y.py`, exit 0). Covers tokens.css defines color/type/spacing/touch(44px)/focus/reduced-motion/breakpoints, Accessibility.md covers all WCAG 2.2 AA topics, and the S09 prototype passes a11y (zoom allowed, ≥44px touch, computed AA contrast on 3 pairs, no motion, focus not disabled, no copied/external assets); S01-S09 regression (git diff vs `910a89f` = no change, excluding S10 in-scope files).
- Automated (preserved): S09 12/12; S08 12/12; S07 11/11; S06 22/22; S05 12/12; S04 10/10; S03 14/14; S02 14/14; S01 12/12.
- Content/data validation (S10): new files non-empty; secret-scan "hits" are the word "token" in "design tokens" — no real credentials.
- Accessibility/device: WCAG 2.2 AA checklist run against the prototype (automated contrast/touch/zoom/motion/focus/assets all pass). Formal device/AT testing deferred to the app build (S11+); the student phone check is the manual gate.
- Manual demo path: Tokens + checklist are reviewable; **manual gate (A3) OPEN** — the student chooses the visual direction, checks it on a phone, and documents asset provenance.
