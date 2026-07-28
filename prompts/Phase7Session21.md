# S21 - Deployment & recovery rehearsal

## Role
Act as the implementation partner for this bounded PauseSpace InnovationLab session. Preserve student ownership and the approved static, privacy-first architecture.

## Read First
Open README.md, TASKS.md, docs/ProjectPlan.md, docs/Architecture.md, docs/DecisionLog.md, the listed in-scope files, and current tests. Inspect before proposing changes.

## Current State
Confirm the repository checkpoint and report what already works, failing tests, known issues, and active task S21 / P7. Do not assume missing work is complete.

## Session Objective
Deploy static build, smoke test, record rollback and offline demo route.

## Scope
In scope: docs/Deployment.md; docs/Recovery.md. Make only changes required for “Deployment & recovery rehearsal”. Preserve all working behavior outside this boundary.

## Requirements
Create the production static build and deployment record; verify HTTPS/static hosting behavior, clean-device use, rollback artifact, cache recovery, and offline demo route. Keep the four authoritative scenes and the approved static, local-first, non-diagnostic boundary; use synthetic or properly anonymized data only.

## Implementation Sequence
1) Verify baseline and tests. 2) Create a checkpoint. 3) State the smallest runnable change. 4) Implement in small steps. 5) Run focused tests after each step. 6) Run the session acceptance checks. 7) Update TASKS, Decision Log and Co-build Log.

## Files
Create or modify only: docs/Deployment.md; docs/Recovery.md. Explicitly preserve deployed assets, approved scripts, unrelated styles, test evidence and prior decisions.

## Tests and Acceptance Criteria
Acceptance gate: Fresh-device smoke test and rollback rehearsal pass. Run a fresh-device smoke test and an actual rollback rehearsal; record deployed version, artifact checksum, known limitations, and demo fallback. Report exact commands, expected versus actual results, manual checks, and evidence paths. Never invent passing results.

## Evidence to Save
Save dated evidence under evidence/S21/: relevant screenshots or recordings, command/test output, reviewed artifacts, defect references, and the pre/post-session checkpoint IDs. Do not save personal or identifying data.

## Student Manual Work
Student performs the deployment and rollback commands and rehearses the offline demonstration without network. The student must review every diff and write the final Co-build Log decision in their own words.

## Security and Safety
Do not collect names, mental-health histories, family details, mood scores, microphone data, analytics identifiers, or secrets. Do not add diagnosis, treatment, emergency promises, forced breathing, autoplay, or unreviewed support contacts.

## Do Not Do
Do not add frameworks, backend, login, AI runtime chat, cloud sync, trackers, streaks, rankings, unrelated refactors, hidden scope, hard-coded secrets, copied imagery, or the next session’s work.

## TASKS.md Session Activation
Before implementation, update only the editable fields in `TASKS.md`:
- `Unit code: S21`
- `Unit focus: Deployment & recovery rehearsal`
- `Current prompt: paste this complete S21 prompt only`
- Replace the three placeholder acceptance lines with this session's observable acceptance criteria.

Do not recreate or overwrite `TASKS.md`. Preserve the full S01-S22 checklist, completed checkmarks, known issues, and last test evidence. After acceptance passes, mark only S21 complete, record actual evidence, and set the next unit only as preparation.

## Checkpoint and Rollback
Record the pre-session checkpoint identifier. If acceptance fails, keep the last runnable state, log the defect, and provide the exact rollback path without erasing evidence.

## Completion Report
List changed files; summarize decisions; show tests and manual checks; identify limitations and unresolved risks; update traceability; name the next safe step without implementing it.

## Stop Condition
Stop when S21 acceptance criteria pass and evidence is saved. Do not begin the next session.
