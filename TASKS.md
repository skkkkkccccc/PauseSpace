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
Unit code: S01
Unit focus: Baseline freeze & success criteria
Current prompt:

```markdown
# S01 - Baseline freeze & success criteria

## Role
Act as the implementation partner for this bounded PauseSpace InnovationLab session. Preserve student ownership and the approved static, privacy-first architecture.

## Read First
Open README.md, TASKS.md, docs/ProjectPlan.md, docs/Architecture.md, docs/DecisionLog.md, the listed in-scope files, and current tests. Inspect before proposing changes.

## Current State
Confirm the repository checkpoint and report what already works, failing tests, known issues, and active task S01 / P1. Do not assume missing work is complete.

## Session Objective
Lock the proposal ledger, unknowns, non-goals, measurable evidence.

## Scope
In scope: docs/ProjectPlan.md; docs/Traceability.md. Make only changes required for “Baseline freeze & success criteria”. Preserve all working behavior outside this boundary.

## Requirements
Extract B-01–B-14 into a traceability ledger; label mandatory/recommended/enhancement/out-of-scope; define observable success measures and unresolved decisions. Keep the four authoritative scenes and the approved static, local-first, non-diagnostic boundary; use synthetic or properly anonymized data only.

## Implementation Sequence
1) Verify baseline and tests. 2) Create a checkpoint. 3) State the smallest runnable change. 4) Implement in small steps. 5) Run focused tests after each step. 6) Run the session acceptance checks. 7) Update TASKS, Decision Log and Co-build Log.

## Files
Create or modify only: docs/ProjectPlan.md; docs/Traceability.md. Explicitly preserve deployed assets, approved scripts, unrelated styles, test evidence and prior decisions.

## Tests and Acceptance Criteria
Acceptance gate: Approved baseline and no silent scope changes. Validate that every baseline ID has an implementation path, verification method, owner, and status; save the approved ledger and checkpoint reference. Report exact commands, expected versus actual results, manual checks, and evidence paths. Never invent passing results.

## Evidence to Save
Save dated evidence under evidence/S01/: relevant screenshots or recordings, command/test output, reviewed artifacts, defect references, and the pre/post-session checkpoint IDs. Do not save personal or identifying data.

## Student Manual Work
Student compares the ledger line-by-line with the proposal and personally approves every non-goal. The student must review every diff and write the final Co-build Log decision in their own words.

## Security and Safety
Do not collect names, mental-health histories, family details, mood scores, microphone data, analytics identifiers, or secrets. Do not add diagnosis, treatment, emergency promises, forced breathing, autoplay, or unreviewed support contacts.

## Do Not Do
Do not add frameworks, backend, login, AI runtime chat, cloud sync, trackers, streaks, rankings, unrelated refactors, hidden scope, hard-coded secrets, copied imagery, or the next session’s work.

## TASKS.md Session Activation
Before implementation, update only the editable fields in `TASKS.md`:
- `Unit code: S01`
- `Unit focus: Baseline freeze & success criteria`
- `Current prompt: paste this complete S01 prompt only`
- Replace the three placeholder acceptance lines with this session's observable acceptance criteria.

Do not recreate or overwrite `TASKS.md`. Preserve the full S01-S22 checklist, completed checkmarks, known issues, and last test evidence. After acceptance passes, mark only S01 complete, record actual evidence, and set the next unit only as preparation.

## Checkpoint and Rollback
Record the pre-session checkpoint identifier. If acceptance fails, keep the last runnable state, log the defect, and provide the exact rollback path without erasing evidence.

## Completion Report
List changed files; summarize decisions; show tests and manual checks; identify limitations and unresolved risks; update traceability; name the next safe step without implementing it.

## Stop Condition
Stop when S01 acceptance criteria pass and evidence is saved. Do not begin the next session.
```

## Acceptance Criteria for Current Unit
- A1 — Ledger completeness: every baseline ID B-01–B-14 in `docs/Traceability.md` has all four fields populated (implementation path, verification method, owner, status) and a mandatory/recommended/enhancement/out-of-scope label. (Auto-verifiable by ledger inspection.)
- A2 — Scope freeze, no silent change: `docs/ProjectPlan.md` locks the eight proposal elements (four ~3-minute scenes; anonymous/no-account use; local-only progress; original audio/visuals; AI Co-build Log; six-week delivery; poster; two-minute video), lists explicit non-goals and unresolved decisions, and leaves the README.md / TASKS.md boundaries unchanged. (Auto-verifiable.)
- A3 — Evidence + approval: pre/post-session checkpoint IDs and command/test output saved under `evidence/S01/`; baseline is marked “approved” only after the student compares the ledger line-by-line with the proposal and personally approves every non-goal. (Manual, student-owned gate.)

## Completed Units
- [ ] S01
- [ ] S02
- [ ] S03
- [ ] S04
- [ ] S05
- [ ] S06
- [ ] S07
- [ ] S08
- [ ] S09
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
- Automated: `evidence/S01/baseline-checks.txt` — 12/12 PASS (validator `evidence/S01/validate_baseline.py`, exit 0). Covers ledger completeness (B-01–B-14 in both tables), category separation, scope freeze, README boundaries unchanged, TASKS.md checklist integrity.
- Content/data validation: `config/sample-config.json` and `data/sample/scene.sample.json` parse as valid JSON (independent re-check recorded in `evidence/S01/baseline-checks.txt`).
- Accessibility/device: Not applicable to S01 (documentation-only session, no UI yet). Deferred to B-11 / later sessions.
- Manual demo path: Not applicable to S01 (no app to demo). **Manual approval gate (A3) is OPEN** — baseline is "frozen, pending student approval" until the student signs off every non-goal.
