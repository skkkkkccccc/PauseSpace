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
Unit code: S05
Unit focus: Exam and sports scripts
Current prompt:

```markdown
# S05 - Exam and sports scripts

## Role
Act as the implementation partner for this bounded PauseSpace InnovationLab session. Preserve student ownership and the approved static, privacy-first architecture.

## Read First
Open README.md, TASKS.md, docs/ProjectPlan.md, docs/Architecture.md, docs/DecisionLog.md, the listed in-scope files, and current tests. Inspect before proposing changes.

## Current State
Confirm the repository checkpoint and report what already works, failing tests, known issues, and active task S05 / P2. Do not assume missing work is complete.

## Session Objective
Draft, student-rewrite, and read aloud two scene scripts.

## Scope
In scope: content/exam-room.json; content/sports-field.json. Make only changes required for “Exam and sports scripts”. Preserve all working behavior outside this boundary.

## Requirements
Draft exam-room and sports-field content from their evidence cards; keep sensory cues concrete and breathing optional; record timing and revision history. Keep the four authoritative scenes and the approved static, local-first, non-diagnostic boundary; use synthetic or properly anonymized data only.

## Implementation Sequence
1) Verify baseline and tests. 2) Create a checkpoint. 3) State the smallest runnable change. 4) Implement in small steps. 5) Run focused tests after each step. 6) Run the session acceptance checks. 7) Update TASKS, Decision Log and Co-build Log.

## Files
Create or modify only: content/exam-room.json; content/sports-field.json. Explicitly preserve deployed assets, approved scripts, unrelated styles, test evidence and prior decisions.

## Tests and Acceptance Criteria
Acceptance gate: Both pass timing and language review. Read both scripts aloud; record duration; run schema/rubric checks; save student revisions and reviewer comments without recording personal stories. Report exact commands, expected versus actual results, manual checks, and evidence paths. Never invent passing results.

## Evidence to Save
Save dated evidence under evidence/S05/: relevant screenshots or recordings, command/test output, reviewed artifacts, defect references, and the pre/post-session checkpoint IDs. Do not save personal or identifying data.

## Student Manual Work
Student rewrites all final wording and performs both timed read-alouds. The student must review every diff and write the final Co-build Log decision in their own words.

## Security and Safety
Do not collect names, mental-health histories, family details, mood scores, microphone data, analytics identifiers, or secrets. Do not add diagnosis, treatment, emergency promises, forced breathing, autoplay, or unreviewed support contacts.

## Do Not Do
Do not add frameworks, backend, login, AI runtime chat, cloud sync, trackers, streaks, rankings, unrelated refactors, hidden scope, hard-coded secrets, copied imagery, or the next session’s work.

## TASKS.md Session Activation
Before implementation, update only the editable fields in `TASKS.md`:
- `Unit code: S05`
- `Unit focus: Exam and sports scripts`
- `Current prompt: paste this complete S05 prompt only`
- Replace the three placeholder acceptance lines with this session's observable acceptance criteria.

Do not recreate or overwrite `TASKS.md`. Preserve the full S01-S22 checklist, completed checkmarks, known issues, and last test evidence. After acceptance passes, mark only S05 complete, record actual evidence, and set the next unit only as preparation.

## Checkpoint and Rollback
Record the pre-session checkpoint identifier. If acceptance fails, keep the last runnable state, log the defect, and provide the exact rollback path without erasing evidence.

## Completion Report
List changed files; summarize decisions; show tests and manual checks; identify limitations and unresolved risks; update traceability; name the next safe step without implementing it.

## Stop Condition
Stop when S05 acceptance criteria pass and evidence is saved. Do not begin the next session.
```

## Acceptance Criteria for Current Unit
- A1 — Schema + timing: both `content/exam-room.json` and `content/sports-field.json` conform to `content/schema.json` (structure valid; ordered segments within the 180 s budget). (Auto-verifiable.)
- A2 — Language review: both scripts pass the choice-language rubric — no commands (incl. forced breathing), promises, or judgments in any spoken text; breathing is optional/invitational. (Auto-verifiable scan; the full timed read-aloud is the student’s manual check.)
- A3 — Evidence + read-aloud: timing recorded and revision history saved under `evidence/S05/` with pre/post checkpoint IDs; “read aloud” and “student rewrite of all final wording” are student-owned manual gates — scripts stay `review.status = draft` until then. (Manual, student-owned gate.)

## Completed Units
- [x] S01
- [x] S02
- [x] S03
- [x] S04
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
- Automated (S05): `evidence/S05/scripts-checks.txt` — 12/12 PASS (validator `evidence/S05/validate_scripts.py`, exit 0). Covers both scenes conform to `content/schema.json` (structure + timing budget), rubric clean (no commands/promises/judgments/forced breathing), spoken-duration fits the 180 s budget (exam-room ~133 s, sports-field ~136 s), `review.status=draft`, and S01-S04 regression (git diff vs `c264786` = no change).
- Automated (preserved): S04 `evidence/S04/content-checks.txt` — 10/10; S03 14/14; S02 14/14; S01 12/12.
- Content/data validation (S05): `content/exam-room.json` and `content/sports-field.json` parse as valid JSON; independent email/secret/token scan of S05 scene files is clean.
- Accessibility/device: Not applicable to S05 (script content only, no UI). Deferred to B-11 / later sessions.
- Manual demo path: Not applicable to S05 (no app to demo). **Manual gate (A3) OPEN** — the student must rewrite all final wording and perform both timed read-alouds; scripts stay `review.status=draft` until then.
