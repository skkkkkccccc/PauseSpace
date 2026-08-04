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
Unit code: S15
Unit focus: Completion choices & support route
Current prompt:

```markdown
# S15 - Completion choices & support route

## Role
Act as the implementation partner for this bounded PauseSpace InnovationLab session. Preserve student ownership and the approved static, privacy-first architecture.

## Read First
Open README.md, TASKS.md, docs/ProjectPlan.md, docs/Architecture.md, docs/DecisionLog.md, the listed in-scope files, and current tests. Inspect before proposing changes.

## Current State
Confirm the repository checkpoint and report what already works, failing tests, known issues, and active task S15 / P5. Do not assume missing work is complete.

## Session Objective
Implement return, replay, and find-support actions with non-emergency boundary.

## Scope
In scope: src/views/Completion.js; content/support.json. Make only changes required for “Completion choices & support route”. Preserve all working behavior outside this boundary.

## Requirements
Implement return, replay, and find-support choices; keep support content static, locally reviewed, non-emergency, and independent of completion tracking. Keep the four authoritative scenes and the approved static, local-first, non-diagnostic boundary; use synthetic or properly anonymized data only.

## Implementation Sequence
1) Verify baseline and tests. 2) Create a checkpoint. 3) State the smallest runnable change. 4) Implement in small steps. 5) Run focused tests after each step. 6) Run the session acceptance checks. 7) Update TASKS, Decision Log and Co-build Log.

## Files
Create or modify only: src/views/Completion.js; content/support.json. Explicitly preserve deployed assets, approved scripts, unrelated styles, test evidence and prior decisions.

## Tests and Acceptance Criteria
Acceptance gate: All branches work; support content is locally appropriate before release. Run all completion branches from every scene; test missing/unapproved support content; save local reviewer approval or keep release blocked. Report exact commands, expected versus actual results, manual checks, and evidence paths. Never invent passing results.

## Evidence to Save
Save dated evidence under evidence/S15/: relevant screenshots or recordings, command/test output, reviewed artifacts, defect references, and the pre/post-session checkpoint IDs. Do not save personal or identifying data.

## Student Manual Work
Student reviews every support phrase with the mentor and verifies the user can always leave. The student must review every diff and write the final Co-build Log decision in their own words.

## Security and Safety
Do not collect names, mental-health histories, family details, mood scores, microphone data, analytics identifiers, or secrets. Do not add diagnosis, treatment, emergency promises, forced breathing, autoplay, or unreviewed support contacts.

## Do Not Do
Do not add frameworks, backend, login, AI runtime chat, cloud sync, trackers, streaks, rankings, unrelated refactors, hidden scope, hard-coded secrets, copied imagery, or the next session’s work.

## TASKS.md Session Activation
Before implementation, update only the editable fields in `TASKS.md`:
- `Unit code: S15`
- `Unit focus: Completion choices & support route`
- `Current prompt: paste this complete S15 prompt only`
- Replace the three placeholder acceptance lines with this session's observable acceptance criteria.

Do not recreate or overwrite `TASKS.md`. Preserve the full S01-S22 checklist, completed checkmarks, known issues, and last test evidence. After acceptance passes, mark only S15 complete, record actual evidence, and set the next unit only as preparation.

## Checkpoint and Rollback
Record the pre-session checkpoint identifier. If acceptance fails, keep the last runnable state, log the defect, and provide the exact rollback path without erasing evidence.

## Completion Report
List changed files; summarize decisions; show tests and manual checks; identify limitations and unresolved risks; update traceability; name the next safe step without implementing it.

## Stop Condition
Stop when S15 acceptance criteria pass and evidence is saved. Do not begin the next session.
```

## Acceptance Criteria for Current Unit
- A1 — Completion branches: `src/views/Completion.js` offers return / replay / find-support / exit for every scene; the choices are **independent of completion tracking** (no streak/score/rank); exit is always available (no forced completion). (Auto-verifiable.)
- A2 — Support route + release gate: `content/support.json` is static, **non-emergency and non-diagnostic**; **unapproved support is not shown** (release blocked until mentor/adult approval — decision D3); missing support is handled safely; find-support toggles the panel. (Auto-verifiable; mentor approval is the manual gate.)
- A3 — Evidence + review: tests + the support-content review saved under `evidence/S15/`; the student reviews every support phrase with the mentor and verifies the user can always leave — student/mentor-owned manual gate. **Support release stays BLOCKED until mentor approval (D3).** (Manual, student-owned gate.)

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
- Automated (S15): `evidence/S15/completion-checks.txt` — `node --test tests/completion.test.mjs` → **8/8 pass** (return/replay/find-support/exit for every scene; exit always; independent of tracking; support non-emergency + release-blocked; unapproved not shown; approved renders approved-only; missing support safe; find-support toggle); `npm test` 3/3; `npm run build` OK (dist unchanged); validator `evidence/S15/validate_completion.py` = 12/12.
- Automated (preserved): S14 13/13; S13 7/7; S12 16/16; S11 3/3 + clean install/lint/build/start; S10 16/16; S09 12/12; S08 12/12; S07 11/11; S06 22/22; S05 12/12; S04 10/10; S03 14/14; S02 14/14; S01 12/12.
- Content/data validation (S15): support content static, non-emergency, non-diagnostic; `reviewStatus=pending-mentor-review`, `releaseBlocked=true`; no real contacts (placeholders only); completion choices independent of tracking.
- Accessibility/device: completion buttons are keyboard-operable (`type=button`, `data-action`, `aria-label`, `aria-expanded`); formal device check is the student manual gate.
- Manual demo path: **Manual gate (A3) OPEN + D3** — student+mentor review every support phrase; mentor approves support contacts (D3) before release; verify the user can always leave. Support release stays BLOCKED until D3. Note: `npm test` runs src/test smoke only; S15 tests run via `node --test tests/completion.test.mjs`. `content.zip` is tracked (benign content/ snapshot swept into S14 commit `35b6293`); recommend `git rm`.
