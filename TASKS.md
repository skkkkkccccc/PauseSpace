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
Unit code: S08
Unit focus: Information architecture
Current prompt:

```markdown
# S08 - Information architecture

## Role
Act as the implementation partner for this bounded PauseSpace InnovationLab session. Preserve student ownership and the approved static, privacy-first architecture.

## Read First
Open README.md, TASKS.md, docs/ProjectPlan.md, docs/Architecture.md, docs/DecisionLog.md, the listed in-scope files, and current tests. Inspect before proposing changes.

## Current State
Confirm the repository checkpoint and report what already works, failing tests, known issues, and active task S08 / P3. Do not assume missing work is complete.

## Session Objective
Specify five views, navigation, completion branches, and error states.

## Scope
In scope: docs/UserFlows.md; docs/Architecture.md. Make only changes required for “Information architecture”. Preserve all working behavior outside this boundary.

## Requirements
Specify home, scene detail, player, pause map, and project/about views; include back/exit/replay/support branches plus loading, missing-audio, offline, and update states. Keep the four authoritative scenes and the approved static, local-first, non-diagnostic boundary; use synthetic or properly anonymized data only.

## Implementation Sequence
1) Verify baseline and tests. 2) Create a checkpoint. 3) State the smallest runnable change. 4) Implement in small steps. 5) Run focused tests after each step. 6) Run the session acceptance checks. 7) Update TASKS, Decision Log and Co-build Log.

## Files
Create or modify only: docs/UserFlows.md; docs/Architecture.md. Explicitly preserve deployed assets, approved scripts, unrelated styles, test evidence and prior decisions.

## Tests and Acceptance Criteria
Acceptance gate: Every baseline journey appears once and has an exit. Walk every baseline journey and error branch on the flow map; confirm no dead end and no forced completion. Report exact commands, expected versus actual results, manual checks, and evidence paths. Never invent passing results.

## Evidence to Save
Save dated evidence under evidence/S08/: relevant screenshots or recordings, command/test output, reviewed artifacts, defect references, and the pre/post-session checkpoint IDs. Do not save personal or identifying data.

## Student Manual Work
Student performs a paper walkthrough and annotates confusing labels or branches. The student must review every diff and write the final Co-build Log decision in their own words.

## Security and Safety
Do not collect names, mental-health histories, family details, mood scores, microphone data, analytics identifiers, or secrets. Do not add diagnosis, treatment, emergency promises, forced breathing, autoplay, or unreviewed support contacts.

## Do Not Do
Do not add frameworks, backend, login, AI runtime chat, cloud sync, trackers, streaks, rankings, unrelated refactors, hidden scope, hard-coded secrets, copied imagery, or the next session’s work.

## TASKS.md Session Activation
Before implementation, update only the editable fields in `TASKS.md`:
- `Unit code: S08`
- `Unit focus: Information architecture`
- `Current prompt: paste this complete S08 prompt only`
- Replace the three placeholder acceptance lines with this session's observable acceptance criteria.

Do not recreate or overwrite `TASKS.md`. Preserve the full S01-S22 checklist, completed checkmarks, known issues, and last test evidence. After acceptance passes, mark only S08 complete, record actual evidence, and set the next unit only as preparation.

## Checkpoint and Rollback
Record the pre-session checkpoint identifier. If acceptance fails, keep the last runnable state, log the defect, and provide the exact rollback path without erasing evidence.

## Completion Report
List changed files; summarize decisions; show tests and manual checks; identify limitations and unresolved risks; update traceability; name the next safe step without implementing it.

## Stop Condition
Stop when S08 acceptance criteria pass and evidence is saved. Do not begin the next session.
```

## Acceptance Criteria for Current Unit
- A1 — Five views + navigation + branches: `docs/UserFlows.md` specifies the five views (home, scene detail, player, pause map, project/about), navigation, and the back/exit/replay/support branches. (Auto-verifiable.)
- A2 — Error states + no dead end + no forced completion: the four error states (loading, missing-audio, offline, update) each have a recovery/exit; every view and baseline journey has an exit; the flows enforce no forced completion (the user can stop/exit at any point). (Auto-verifiable structural check; the full paper walkthrough is the student’s manual check.)
- A3 — Architecture update + walkthrough: `docs/Architecture.md` is updated with the IA (original statement preserved); pre/post checkpoint IDs and check output saved under `evidence/S08/`; the student paper walkthrough + annotation of confusing labels/branches is a student-owned manual gate. (Manual, student-owned gate.)

## Completed Units
- [x] S01
- [x] S02
- [x] S03
- [x] S04
- [x] S05
- [x] S06
- [x] S07
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
- Automated (S08): `evidence/S08/ia-checks.txt` — 12/12 PASS (validator `evidence/S08/validate_ia.py`, exit 0). Covers UserFlows specifies the five views + back/exit/replay/support branches, four error states each with exit/recovery, every view has an exit, no forced completion, baseline journeys + no-dead-end checklist, Architecture.md updated with IA (original preserved) referencing the five views, and S01-S07 regression (git diff vs `6ef5fc4` = no change, excluding S08 in-scope files).
- Automated (preserved): S07 11/11; S06 22/22; S05 12/12; S04 10/10; S03 14/14; S02 14/14; S01 12/12.
- Content/data validation (S08): new/modified docs non-empty; independent email/secret/token scan of S08 docs is clean.
- Accessibility/device: Not applicable to S08 (information architecture, no UI). Deferred to B-11 / later sessions.
- Manual demo path: Not applicable to S08 (no app to demo). **Manual gate (A3) OPEN** — the student must perform a paper walkthrough and annotate any confusing labels or branches; the IA stays proposed until then.
