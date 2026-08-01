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
Unit code: S06
Unit focus: Room and empty-classroom scripts
Current prompt:

```markdown
# S06 - Room and empty-classroom scripts

## Role
Act as the implementation partner for this bounded PauseSpace InnovationLab session. Preserve student ownership and the approved static, privacy-first architecture.

## Read First
Open README.md, TASKS.md, docs/ProjectPlan.md, docs/Architecture.md, docs/DecisionLog.md, the listed in-scope files, and current tests. Inspect before proposing changes.

## Current State
Confirm the repository checkpoint and report what already works, failing tests, known issues, and active task S06 / P2. Do not assume missing work is complete.

## Session Objective
Draft, student-rewrite, and read aloud the remaining scripts.

## Scope
In scope: content/own-room.json; content/empty-classroom.json. Make only changes required for “Room and empty-classroom scripts”. Preserve all working behavior outside this boundary.

## Requirements
Draft own-room and empty-classroom content using the approved structure; keep future/academic stress references non-diagnostic and bounded. Keep the four authoritative scenes and the approved static, local-first, non-diagnostic boundary; use synthetic or properly anonymized data only.

## Implementation Sequence
1) Verify baseline and tests. 2) Create a checkpoint. 3) State the smallest runnable change. 4) Implement in small steps. 5) Run focused tests after each step. 6) Run the session acceptance checks. 7) Update TASKS, Decision Log and Co-build Log.

## Files
Create or modify only: content/own-room.json; content/empty-classroom.json. Explicitly preserve deployed assets, approved scripts, unrelated styles, test evidence and prior decisions.

## Tests and Acceptance Criteria
Acceptance gate: Both pass timing and language review. Read both scripts aloud; record duration; run schema/rubric checks; confirm all four scenes now share the same content contract. Report exact commands, expected versus actual results, manual checks, and evidence paths. Never invent passing results.

## Evidence to Save
Save dated evidence under evidence/S06/: relevant screenshots or recordings, command/test output, reviewed artifacts, defect references, and the pre/post-session checkpoint IDs. Do not save personal or identifying data.

## Student Manual Work
Student rewrites all final wording and compares tone and pacing across the four scripts. The student must review every diff and write the final Co-build Log decision in their own words.

## Security and Safety
Do not collect names, mental-health histories, family details, mood scores, microphone data, analytics identifiers, or secrets. Do not add diagnosis, treatment, emergency promises, forced breathing, autoplay, or unreviewed support contacts.

## Do Not Do
Do not add frameworks, backend, login, AI runtime chat, cloud sync, trackers, streaks, rankings, unrelated refactors, hidden scope, hard-coded secrets, copied imagery, or the next session’s work.

## TASKS.md Session Activation
Before implementation, update only the editable fields in `TASKS.md`:
- `Unit code: S06`
- `Unit focus: Room and empty-classroom scripts`
- `Current prompt: paste this complete S06 prompt only`
- Replace the three placeholder acceptance lines with this session's observable acceptance criteria.

Do not recreate or overwrite `TASKS.md`. Preserve the full S01-S22 checklist, completed checkmarks, known issues, and last test evidence. After acceptance passes, mark only S06 complete, record actual evidence, and set the next unit only as preparation.

## Checkpoint and Rollback
Record the pre-session checkpoint identifier. If acceptance fails, keep the last runnable state, log the defect, and provide the exact rollback path without erasing evidence.

## Completion Report
List changed files; summarize decisions; show tests and manual checks; identify limitations and unresolved risks; update traceability; name the next safe step without implementing it.

## Stop Condition
Stop when S06 acceptance criteria pass and evidence is saved. Do not begin the next session.
```

## Acceptance Criteria for Current Unit
- A1 — Four-scene content contract: `content/own-room.json` and `content/empty-classroom.json` conform to `content/schema.json`, and all four scenes (exam-room, sports-field, own-room, empty-classroom) share the same content contract (same required keys, segment structure, 180 s budget). (Auto-verifiable.)
- A2 — Language review: both new scripts pass the choice-language rubric — no commands (incl. forced breathing), promises, or judgments; future/academic references are non-diagnostic and bounded. (Auto-verifiable scan; the full timed read-aloud is the student’s manual check.)
- A3 — Evidence + read-aloud: timing recorded and revision history saved under `evidence/S06/` with pre/post checkpoint IDs; “read aloud” and “student rewrite + cross-scene tone/pacing comparison” are student-owned manual gates — scripts stay `review.status = draft` until then. (Manual, student-owned gate.)

## Completed Units
- [x] S01
- [x] S02
- [x] S03
- [x] S04
- [x] S05
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
- Automated (S06): `evidence/S06/scripts-checks.txt` — 22/22 PASS (validator `evidence/S06/validate_scripts.py`, exit 0). Covers all four scenes conform to `content/schema.json` (structure + timing budget), rubric clean (no commands/promises/judgments/forced breathing), spoken-duration fits the 180 s budget, all four share the same content contract (keys / 180 s / 4 segments / labels / draft), and S01-S05 regression (git diff vs `bdf0ff3` = no change).
- Automated (preserved): S05 12/12; S04 10/10; S03 14/14; S02 14/14; S01 12/12.
- Content/data validation (S06): all four scene files parse as valid JSON; independent email/secret/token scan of S06 scene files is clean.
- Accessibility/device: Not applicable to S06 (script content only, no UI). Deferred to B-11 / later sessions.
- Manual demo path: Not applicable to S06 (no app to demo). **Manual gate (A3) OPEN** — the student must rewrite all wording, compare tone/pacing across the four scripts, and perform the read-alouds; scripts stay `review.status=draft` until then.
- Note: untracked OA01 (Optional AI Audio Extension) files are present in the tree; not part of S06; security-clean; commit separately if kept (see `evidence/S06/checkpoint-post.txt`).
