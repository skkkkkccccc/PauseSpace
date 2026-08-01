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
Unit code: S09
Unit focus: Mobile prototype
Current prompt:

```markdown
# S09 - Mobile prototype

## Role
Act as the implementation partner for this bounded PauseSpace InnovationLab session. Preserve student ownership and the approved static, privacy-first architecture.

## Read First
Open README.md, TASKS.md, docs/ProjectPlan.md, docs/Architecture.md, docs/DecisionLog.md, the listed in-scope files, and current tests. Inspect before proposing changes.

## Current State
Confirm the repository checkpoint and report what already works, failing tests, known issues, and active task S09 / P3. Do not assume missing work is complete.

## Session Objective
Build a low-fidelity interactive prototype for one full scene.

## Scope
In scope: design/prototype/; docs/UsabilityTasks.md. Make only changes required for “Mobile prototype”. Preserve all working behavior outside this boundary.

## Requirements
Create one clickable mobile vertical slice from scene card through completion; use realistic synthetic copy and explicit exit controls; avoid engineering beyond the prototype. Keep the four authoritative scenes and the approved static, local-first, non-diagnostic boundary; use synthetic or properly anonymized data only.

## Implementation Sequence
1) Verify baseline and tests. 2) Create a checkpoint. 3) State the smallest runnable change. 4) Implement in small steps. 5) Run focused tests after each step. 6) Run the session acceptance checks. 7) Update TASKS, Decision Log and Co-build Log.

## Files
Create or modify only: design/prototype/; docs/UsabilityTasks.md. Explicitly preserve deployed assets, approved scripts, unrelated styles, test evidence and prior decisions.

## Tests and Acceptance Criteria
Acceptance gate: A peer completes the path without explanation. Run the defined usability task with one consenting peer; record only task observations; save prototype version and issue list. Report exact commands, expected versus actual results, manual checks, and evidence paths. Never invent passing results.

## Evidence to Save
Save dated evidence under evidence/S09/: relevant screenshots or recordings, command/test output, reviewed artifacts, defect references, and the pre/post-session checkpoint IDs. Do not save personal or identifying data.

## Student Manual Work
Student facilitates the test without coaching and decides which finding is actionable. The student must review every diff and write the final Co-build Log decision in their own words.

## Security and Safety
Do not collect names, mental-health histories, family details, mood scores, microphone data, analytics identifiers, or secrets. Do not add diagnosis, treatment, emergency promises, forced breathing, autoplay, or unreviewed support contacts.

## Do Not Do
Do not add frameworks, backend, login, AI runtime chat, cloud sync, trackers, streaks, rankings, unrelated refactors, hidden scope, hard-coded secrets, copied imagery, or the next session’s work.

## TASKS.md Session Activation
Before implementation, update only the editable fields in `TASKS.md`:
- `Unit code: S09`
- `Unit focus: Mobile prototype`
- `Current prompt: paste this complete S09 prompt only`
- Replace the three placeholder acceptance lines with this session's observable acceptance criteria.

Do not recreate or overwrite `TASKS.md`. Preserve the full S01-S22 checklist, completed checkmarks, known issues, and last test evidence. After acceptance passes, mark only S09 complete, record actual evidence, and set the next unit only as preparation.

## Checkpoint and Rollback
Record the pre-session checkpoint identifier. If acceptance fails, keep the last runnable state, log the defect, and provide the exact rollback path without erasing evidence.

## Completion Report
List changed files; summarize decisions; show tests and manual checks; identify limitations and unresolved risks; update traceability; name the next safe step without implementing it.

## Stop Condition
Stop when S09 acceptance criteria pass and evidence is saved. Do not begin the next session.
```

## Acceptance Criteria for Current Unit
- A1 — Clickable vertical slice: `design/prototype/` contains a mobile, clickable prototype covering scene card → scene detail → player → completion for one scene, with explicit exit controls and synthetic copy. (Auto-verifiable structure; the peer test is the manual gate.)
- A2 — Self-contained & low fidelity: the prototype is static (no backend, no external network scripts, no frameworks), with a mobile viewport and large tap targets. (Auto-verifiable.)
- A3 — Usability task + evidence: `docs/UsabilityTasks.md` defines the task and observation/issue templates; pre/post checkpoint IDs and check output saved under `evidence/S09/`; the peer usability test (a consenting peer completes the path without explanation; the student facilitates without coaching) and the saved issue list are student-owned manual gates. (Manual, student-owned gate.)

## Completed Units
- [x] S01
- [x] S02
- [x] S03
- [x] S04
- [x] S05
- [x] S06
- [x] S07
- [x] S08
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
- Automated (S09): `evidence/S09/prototype-checks.txt` — 12/12 PASS (validator `evidence/S09/validate_prototype.py`, exit 0). Covers prototype has 4 views (home/detail/player/done) + explicit exit controls + mobile viewport + synthetic copy, is self-contained (no backend/external network/frameworks/analytics), UsabilityTasks defines task + observation/issue templates + no-coaching, and S01-S08 regression (git diff vs `0ed8bd2` = no change, excluding S09 in-scope files).
- Automated (preserved): S08 12/12; S07 11/11; S06 22/22; S05 12/12; S04 10/10; S03 14/14; S02 14/14; S01 12/12.
- Content/data validation (S09): `design/prototype/index.html` parses cleanly via `html.parser`; independent email/secret/token scan of S09 files is clean.
- Accessibility/device: The prototype is mobile-first (viewport + large tap targets) but is **not** formally accessibility/device-tested; deferred to S10 / B-11. (S09 is a low-fidelity prototype.)
- Manual demo path: The prototype is clickable (open `design/prototype/index.html`). **Peer usability test (A3) OPEN** — the student must facilitate a no-coaching test with one consenting peer and save the issue list.
