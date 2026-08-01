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
Unit code: S11
Unit focus: Repository kickoff
Current prompt:

```markdown
# S11 - Repository kickoff

## Role
Act as the implementation partner for this bounded PauseSpace InnovationLab session. Preserve student ownership and the approved static, privacy-first architecture.

## Read First
Open README.md, TASKS.md, docs/ProjectPlan.md, docs/Architecture.md, docs/DecisionLog.md, the listed in-scope files, and current tests. Inspect before proposing changes.

## Current State
Confirm the repository checkpoint and report what already works, failing tests, known issues, and active task S11 / P4. Do not assume missing work is complete.

## Session Objective
Create runnable static structure, task state, lint/test scripts, env boundary.

## Scope
In scope: README.md; TASKS.md; package.json; src/. Make only changes required for “Repository kickoff”. Preserve all working behavior outside this boundary.

## Requirements
Create the minimal native HTML/CSS/JavaScript repository; add deterministic scripts for local run, lint, test, and build; keep runtime secret-free. Keep the four authoritative scenes and the approved static, local-first, non-diagnostic boundary; use synthetic or properly anonymized data only.

## Implementation Sequence
1) Verify baseline and tests. 2) Create a checkpoint. 3) State the smallest runnable change. 4) Implement in small steps. 5) Run focused tests after each step. 6) Run the session acceptance checks. 7) Update TASKS, Decision Log and Co-build Log.

## Files
Create or modify only: README.md; TASKS.md; package.json; src/. Explicitly preserve deployed assets, approved scripts, unrelated styles, test evidence and prior decisions.

## Tests and Acceptance Criteria
Acceptance gate: Clean checkout runs with documented commands. From a clean checkout run install, test, build, and local preview commands exactly as documented; save command output and checkpoint ID. Report exact commands, expected versus actual results, manual checks, and evidence paths. Never invent passing results.

## Evidence to Save
Save dated evidence under evidence/S11/: relevant screenshots or recordings, command/test output, reviewed artifacts, defect references, and the pre/post-session checkpoint IDs. Do not save personal or identifying data.

## Student Manual Work
Student executes the first run, explains the folder structure, and updates TASKS without overwriting history. The student must review every diff and write the final Co-build Log decision in their own words.

## Security and Safety
Do not collect names, mental-health histories, family details, mood scores, microphone data, analytics identifiers, or secrets. Do not add diagnosis, treatment, emergency promises, forced breathing, autoplay, or unreviewed support contacts.

## Do Not Do
Do not add frameworks, backend, login, AI runtime chat, cloud sync, trackers, streaks, rankings, unrelated refactors, hidden scope, hard-coded secrets, copied imagery, or the next session’s work.

## TASKS.md Session Activation
Before implementation, update only the editable fields in `TASKS.md`:
- `Unit code: S11`
- `Unit focus: Repository kickoff`
- `Current prompt: paste this complete S11 prompt only`
- Replace the three placeholder acceptance lines with this session's observable acceptance criteria.

Do not recreate or overwrite `TASKS.md`. Preserve the full S01-S22 checklist, completed checkmarks, known issues, and last test evidence. After acceptance passes, mark only S11 complete, record actual evidence, and set the next unit only as preparation.

## Checkpoint and Rollback
Record the pre-session checkpoint identifier. If acceptance fails, keep the last runnable state, log the defect, and provide the exact rollback path without erasing evidence.

## Completion Report
List changed files; summarize decisions; show tests and manual checks; identify limitations and unresolved risks; update traceability; name the next safe step without implementing it.

## Stop Condition
Stop when S11 acceptance criteria pass and evidence is saved. Do not begin the next session.
```

## Acceptance Criteria for Current Unit
- A1 — Runnable static repo: `package.json` + `src/` define a minimal native HTML/CSS/JS app with **zero runtime dependencies** and **no runtime secrets**. (Auto-verifiable.)
- A2 — Documented deterministic commands run from a clean checkout: README documents install/test/lint/build/preview; `npm install`, `npm test`, `npm run lint`, and `npm run build` succeed, and `npm start` serves the app — real command output saved. (Auto-verifiable + actual run.)
- A3 — Evidence + first run: pre/post checkpoint IDs and real command output saved under `evidence/S11/`; the student executes the first run and explains the folder structure — student-owned manual gates. (Manual, student-owned gate.)

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
- Automated (S11): `evidence/S11/run-output.txt` — clean-checkout command run (node v24.18.0, npm 11.16.0): `npm install` exit 0 (0 vulnerabilities, zero deps); `npm test` exit 0 (3/3 via node:test); `npm run lint` exit 0 (clean); `npm run build` exit 0 (src→dist/, 3 files); `npm start` HTTP 200 (serves dist/). Structural validator `evidence/S11/validate_repo.py` = 18/18.
- Automated (preserved): S10 16/16; S09 12/12; S08 12/12; S07 11/11; S06 22/22; S05 12/12; S04 10/10; S03 14/14; S02 14/14; S01 12/12.
- Content/data validation (S11): `package.json` valid JSON; no secrets in src (regex scan).
- Accessibility/device: Not the focus of S11 (repository kickoff); the app shell is minimal. Formal a11y/device testing comes at the feature build (S12+).
- Manual demo path: The app runs locally (`npm run preview` → http://localhost:3000). **Manual gate (A3) OPEN** — the student executes the first run and explains the folder structure.
