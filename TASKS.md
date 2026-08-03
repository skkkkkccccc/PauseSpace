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
Unit code: S12
Unit focus: Data and state contracts
Current prompt:

```markdown
# S12 - Data and state contracts

## Role
Act as the implementation partner for this bounded PauseSpace InnovationLab session. Preserve student ownership and the approved static, privacy-first architecture.

## Read First
Open README.md, TASKS.md, docs/ProjectPlan.md, docs/Architecture.md, docs/DecisionLog.md, the listed in-scope files, and current tests. Inspect before proposing changes.

## Current State
Confirm the repository checkpoint and report what already works, failing tests, known issues, and active task S12 / P4. Do not assume missing work is complete.

## Session Objective
Implement scene schema, loader, player state machine, storage versioning.

## Scope
In scope: src/data/; src/state/; tests/. Make only changes required for “Data and state contracts”. Preserve all working behavior outside this boundary.

## Requirements
Implement scene validation/loader, explicit player states and transitions, versioned progress payload, migration/reset behavior, and safe error objects. Keep the four authoritative scenes and the approved static, local-first, non-diagnostic boundary; use synthetic or properly anonymized data only.

## Implementation Sequence
1) Verify baseline and tests. 2) Create a checkpoint. 3) State the smallest runnable change. 4) Implement in small steps. 5) Run focused tests after each step. 6) Run the session acceptance checks. 7) Update TASKS, Decision Log and Co-build Log.

## Files
Create or modify only: src/data/; src/state/; tests/. Explicitly preserve deployed assets, approved scripts, unrelated styles, test evidence and prior decisions.

## Tests and Acceptance Criteria
Acceptance gate: Valid samples pass; malformed data fails safely. Run unit tests for valid, missing, malformed, stale-version, interrupted-playback, and reset cases; save the test report. Report exact commands, expected versus actual results, manual checks, and evidence paths. Never invent passing results.

## Evidence to Save
Save dated evidence under evidence/S12/: relevant screenshots or recordings, command/test output, reviewed artifacts, defect references, and the pre/post-session checkpoint IDs. Do not save personal or identifying data.

## Student Manual Work
Student draws and explains the state machine, then adds at least one edge-case test personally. The student must review every diff and write the final Co-build Log decision in their own words.

## Security and Safety
Do not collect names, mental-health histories, family details, mood scores, microphone data, analytics identifiers, or secrets. Do not add diagnosis, treatment, emergency promises, forced breathing, autoplay, or unreviewed support contacts.

## Do Not Do
Do not add frameworks, backend, login, AI runtime chat, cloud sync, trackers, streaks, rankings, unrelated refactors, hidden scope, hard-coded secrets, copied imagery, or the next session’s work.

## TASKS.md Session Activation
Before implementation, update only the editable fields in `TASKS.md`:
- `Unit code: S12`
- `Unit focus: Data and state contracts`
- `Current prompt: paste this complete S12 prompt only`
- Replace the three placeholder acceptance lines with this session's observable acceptance criteria.

Do not recreate or overwrite `TASKS.md`. Preserve the full S01-S22 checklist, completed checkmarks, known issues, and last test evidence. After acceptance passes, mark only S12 complete, record actual evidence, and set the next unit only as preparation.

## Checkpoint and Rollback
Record the pre-session checkpoint identifier. If acceptance fails, keep the last runnable state, log the defect, and provide the exact rollback path without erasing evidence.

## Completion Report
List changed files; summarize decisions; show tests and manual checks; identify limitations and unresolved risks; update traceability; name the next safe step without implementing it.

## Stop Condition
Stop when S12 acceptance criteria pass and evidence is saved. Do not begin the next session.
```

## Acceptance Criteria for Current Unit
- A1 — Scene data contract: `src/data/` implements scene validation + loader (mirrors `content/schema.json`); valid samples pass and missing/malformed data fails **safely** (safe error objects, no throws). (Auto-verifiable via tests.)
- A2 — Player state machine + versioned storage: `src/state/` implements explicit player states/transitions (**exit always allowed**, no forced completion) and versioned progress (version field, migration of stale versions, reset, safe error objects). (Auto-verifiable via tests.)
- A3 — Test report + edge case: `tests/` cover valid, missing, malformed, stale-version, interrupted-playback, and reset; the test report is saved under `evidence/S12/`; the student draws/explains the state machine and adds at least one edge-case test personally — student-owned manual gates. (Manual, student-owned gate.)

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
- Automated (S12): `evidence/S12/test-report.txt` — `node --test tests/*.test.mjs` → **16/16 pass** (scene-loader 6, player 5, progress 5: valid/missing/malformed/stale-version/interrupted-playback/reset); `npm test` (S11 smoke) still 3/3; no secrets in new modules; structural validator `evidence/S12/validate_contracts.py` = 10/10.
- Automated (preserved): S11 3/3 (npm test) + clean install/lint/build/start; S10 16/16; S09 12/12; S08 12/12; S07 11/11; S06 22/22; S05 12/12; S04 10/10; S03 14/14; S02 14/14; S01 12/12.
- Content/data validation (S12): scene-loader validates against `content/schema.json` (exam-room sample); progress payload is versioned with no scores/streaks/identifying data.
- Accessibility/device: Not the focus of S12 (data/state contracts, no UI). Deferred to the feature build.
- Manual demo path: **Manual gate (A3) OPEN** — the student draws/explains the state machine and adds at least one edge-case test personally. Note: `npm test` runs the src/test smoke only; S12 tests run via `node --test tests/*.test.mjs` (wiring `tests/` into the npm script is a later-session item — package.json is out of S12 scope).
