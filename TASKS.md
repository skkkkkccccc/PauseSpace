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
Unit code: S18
Unit focus: Automated and device testing
Current prompt:

```markdown
# S18 - Automated and device testing

## Role
Act as the implementation partner for this bounded PauseSpace InnovationLab session. Preserve student ownership and the approved static, privacy-first architecture.

## Read First
Open README.md, TASKS.md, docs/ProjectPlan.md, docs/Architecture.md, docs/DecisionLog.md, the listed in-scope files, and current tests. Inspect before proposing changes.

## Current State
Confirm the repository checkpoint and report what already works, failing tests, known issues, and active task S18 / P6. Do not assume missing work is complete.

## Session Objective
Run unit, integration, E2E, accessibility, browser, and audio fallback tests.

## Scope
In scope: tests/; docs/TestReport.md. Make only changes required for “Automated and device testing”. Preserve all working behavior outside this boundary.

## Requirements
Execute the approved unit, integration, E2E, accessibility, responsive, browser, audio-fallback, privacy, offline, and recovery suites; log defects instead of broad refactoring. Keep the four authoritative scenes and the approved static, local-first, non-diagnostic boundary; use synthetic or properly anonymized data only.

## Implementation Sequence
1) Verify baseline and tests. 2) Create a checkpoint. 3) State the smallest runnable change. 4) Implement in small steps. 5) Run focused tests after each step. 6) Run the session acceptance checks. 7) Update TASKS, Decision Log and Co-build Log.

## Files
Create or modify only: tests/; docs/TestReport.md. Explicitly preserve deployed assets, approved scripts, unrelated styles, test evidence and prior decisions.

## Tests and Acceptance Criteria
Acceptance gate: Critical journeys pass; failures become defect entries. Save commands, environment, expected/actual results and artifacts; require all critical journeys to pass or remain explicitly release-blocking. Report exact commands, expected versus actual results, manual checks, and evidence paths. Never invent passing results.

## Evidence to Save
Save dated evidence under evidence/S18/: relevant screenshots or recordings, command/test output, reviewed artifacts, defect references, and the pre/post-session checkpoint IDs. Do not save personal or identifying data.

## Student Manual Work
Student personally reproduces one failure, verifies one fix, and signs the honest test summary. The student must review every diff and write the final Co-build Log decision in their own words.

## Security and Safety
Do not collect names, mental-health histories, family details, mood scores, microphone data, analytics identifiers, or secrets. Do not add diagnosis, treatment, emergency promises, forced breathing, autoplay, or unreviewed support contacts.

## Do Not Do
Do not add frameworks, backend, login, AI runtime chat, cloud sync, trackers, streaks, rankings, unrelated refactors, hidden scope, hard-coded secrets, copied imagery, or the next session’s work.

## TASKS.md Session Activation
Before implementation, update only the editable fields in `TASKS.md`:
- `Unit code: S18`
- `Unit focus: Automated and device testing`
- `Current prompt: paste this complete S18 prompt only`
- Replace the three placeholder acceptance lines with this session's observable acceptance criteria.

Do not recreate or overwrite `TASKS.md`. Preserve the full S01-S22 checklist, completed checkmarks, known issues, and last test evidence. After acceptance passes, mark only S18 complete, record actual evidence, and set the next unit only as preparation.

## Checkpoint and Rollback
Record the pre-session checkpoint identifier. If acceptance fails, keep the last runnable state, log the defect, and provide the exact rollback path without erasing evidence.

## Completion Report
List changed files; summarize decisions; show tests and manual checks; identify limitations and unresolved risks; update traceability; name the next safe step without implementing it.

## Stop Condition
Stop when S18 acceptance criteria pass and evidence is saved. Do not begin the next session.
```

## Acceptance Criteria for Current Unit
- A1 — Automated suites run: the unit / integration / offline / audio-fallback / privacy suites execute via `node --test tests/*.test.{mjs,js}`, `npm test`, `npm run lint`, `npm run build`; commands, environment, and pass/fail counts are saved; every critical automated journey passes (or any failure is logged as an explicitly release-blocking defect). (Auto-verifiable.)
- A2 — TestReport: `docs/TestReport.md` records commands, environment, expected vs actual per suite, critical-journey status, defect entries, and the manual suites still pending (E2E, accessibility/AT, browser matrix, device). (Auto-verifiable structure; honest.)
- A3 — Evidence + sign-off: run output + TestReport saved under `evidence/S18/` and `docs/`; the student personally reproduces one failure, verifies one fix, and signs the honest summary — student-owned manual gate. (Manual, student-owned gate.)

## Optional Extension Units
- [ ] OA01 - AI-generated narration production and curation

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
- [x] S10
- [x] S11
- [x] S12
- [x] S13
- [x] S14
- [x] S15
- [x] S16
- [x] S17
- [ ] S18
- [ ] S19
- [ ] S20
- [ ] S21
- [ ] S22

## Known Issues
- Deployment host; owner: student and mentor; next action: decide before S21.
- Locally approved support contacts; owner: mentor/adult reviewer; next action: approve before S15 release gate.

## Last Test Evidence
- Automated (S18): `evidence/S18/test-run.txt` — `node --test tests/*.test.{mjs,js}` → **73/73 pass** (unit/integration/offline/audio-fallback across S12–S17 + OA01); `npm test` 3/3; `npm run lint` clean; `npm run build` OK; repo secret scan → **no real secrets** (matches are detector-pattern definitions). `docs/TestReport.md` records commands/env/expected-vs-actual/critical-journey status/defects/manual suites pending.
- Automated (preserved): OA01 5/5; S17 6/6; S16 9/9; S15 8/8; S14 13/13; S13 7/7; S12 16/16; S11 3/3 + clean install/lint/build/start; S10 16/16; S09 12/12; S08 12/12; S07 11/11; S06 22/22; S05 12/12; S04 10/10; S03 14/14; S02 14/14; S01 12/12.
- Content/data validation (S18): 0 automated defects (0 failures across 76 automated tests); critical automated journeys pass.
- Accessibility/device: NOT run on a device — E2E, accessibility/AT, browser matrix, on-device, and OA01 real-audio listening remain **manual student gates** (not claimed passing).
- Manual demo path: **Manual gate (A3) OPEN** — the student reproduces one failure, verifies one fix, and signs the honest summary. App/player not yet wired into `dist/` (E2E pending wiring). `content.zip` still tracked (recommend `git rm`).
