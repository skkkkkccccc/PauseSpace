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
Unit code: S14
Unit focus: Accessible player & viewing modes
Current prompt:

```markdown
# S14 - Accessible player & viewing modes

## Role
Act as the implementation partner for this bounded PauseSpace InnovationLab session. Preserve student ownership and the approved static, privacy-first architecture.

## Read First
Open README.md, TASKS.md, docs/ProjectPlan.md, docs/Architecture.md, docs/DecisionLog.md, the listed in-scope files, and current tests. Inspect before proposing changes.

## Current State
Confirm the repository checkpoint and report what already works, failing tests, known issues, and active task S14 / P5. Do not assume missing work is complete.

## Session Objective
Implement audio controls plus explicit eyes-open / eyes-closed choice, reduced motion, errors, keyboard use and safe reset.

## Scope
In scope: src/components/AudioPlayer.js; src/components/ModePicker.js; tests/player.test.js. Make only changes required for “Accessible player & viewing modes”. Preserve all working behavior outside this boundary.

## Requirements
Implement play/pause/restart/progress/time/transcript/error controls; add reversible eyes-open/eyes-closed presentation choices; honor keyboard, focus, reduced-motion, and no-autoplay rules. Keep the four authoritative scenes and the approved static, local-first, non-diagnostic boundary; use synthetic or properly anonymized data only.

## Implementation Sequence
1) Verify baseline and tests. 2) Create a checkpoint. 3) State the smallest runnable change. 4) Implement in small steps. 5) Run focused tests after each step. 6) Run the session acceptance checks. 7) Update TASKS, Decision Log and Co-build Log.

## Files
Create or modify only: src/components/AudioPlayer.js; src/components/ModePicker.js; tests/player.test.js. Explicitly preserve deployed assets, approved scripts, unrelated styles, test evidence and prior decisions.

## Tests and Acceptance Criteria
Acceptance gate: Player and both reversible modes work on mobile and keyboard; no autoplay or sensory-deprivation implication. Test every player transition, missing audio, rapid input, keyboard path, both viewing modes, reset, background/resume, and reduced-motion behavior on mobile. Report exact commands, expected versus actual results, manual checks, and evidence paths. Never invent passing results.

## Evidence to Save
Save dated evidence under evidence/S14/: relevant screenshots or recordings, command/test output, reviewed artifacts, defect references, and the pre/post-session checkpoint IDs. Do not save personal or identifying data.

## Student Manual Work
Student operates the complete control set with keyboard and touch and explains why viewing mode never changes safety claims. The student must review every diff and write the final Co-build Log decision in their own words.

## Security and Safety
Do not collect names, mental-health histories, family details, mood scores, microphone data, analytics identifiers, or secrets. Do not add diagnosis, treatment, emergency promises, forced breathing, autoplay, or unreviewed support contacts.

## Do Not Do
Do not add frameworks, backend, login, AI runtime chat, cloud sync, trackers, streaks, rankings, unrelated refactors, hidden scope, hard-coded secrets, copied imagery, or the next session’s work.

## TASKS.md Session Activation
Before implementation, update only the editable fields in `TASKS.md`:
- `Unit code: S14`
- `Unit focus: Accessible player & viewing modes`
- `Current prompt: paste this complete S14 prompt only`
- Replace the three placeholder acceptance lines with this session's observable acceptance criteria.

Do not recreate or overwrite `TASKS.md`. Preserve the full S01-S22 checklist, completed checkmarks, known issues, and last test evidence. After acceptance passes, mark only S14 complete, record actual evidence, and set the next unit only as preparation.

## Checkpoint and Rollback
Record the pre-session checkpoint identifier. If acceptance fails, keep the last runnable state, log the defect, and provide the exact rollback path without erasing evidence.

## Completion Report
List changed files; summarize decisions; show tests and manual checks; identify limitations and unresolved risks; update traceability; name the next safe step without implementing it.

## Stop Condition
Stop when S14 acceptance criteria pass and evidence is saved. Do not begin the next session.
```

## Acceptance Criteria for Current Unit
- A1 — Player control surface: `src/components/AudioPlayer.js` renders play/pause/restart/progress/time/transcript/error controls from the player FSM state; **user-initiated only (no autoplay)**; missing audio → error state; exit always available (no forced completion). (Auto-verifiable.)
- A2 — Viewing modes + accessibility: `src/components/ModePicker.js` provides **reversible eyes-open/eyes-closed** modes (presentation only — **never changes safety claims**); keyboard-operable controls (`<button type="button">` + `data-action`/`aria`); reduced-motion honored; safe reset; background pauses with no auto-resume. (Auto-verifiable; mobile+keyboard manual check.)
- A3 — Evidence + review: tests + a manual mobile+keyboard control exercise saved under `evidence/S14/`; the student operates the full control set with keyboard+touch and explains why viewing mode never changes safety claims — student-owned manual gate. (Manual, student-owned gate.)

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
- Automated (S14): `evidence/S14/player-checks.txt` — `node --test tests/player.test.js` → **13/13 pass** (modes valid/reversible; control per state with no autoplay; rapid input consistent; missing-audio error; keyboard buttons; reset; background pause/no auto-resume; reduced-motion; exit always; no autoplay/TTS); `npm test` 3/3; `npm run build` OK (dist unchanged); validator `evidence/S14/validate_player.py` = 10/10.
- Automated (preserved): S13 7/7; S12 16/16; S11 3/3 + clean install/lint/build/start; S10 16/16; S09 12/12; S08 12/12; S07 11/11; S06 22/22; S05 12/12; S04 10/10; S03 14/14; S02 14/14; S01 12/12.
- Content/data validation (S14): player controls derive from the S12 FSM; viewing modes are reversible and never change the safety/non-diagnostic note; no `<audio>` element / no autoplay / no runtime TTS in S14.
- Accessibility/device: keyboard-operable buttons (`type=button`, `data-action`, `aria-label`); reduced-motion carried; formal mobile+AT exercise is the student manual gate.
- Manual demo path: **Manual gate (A3) OPEN** — the student operates the full control set with keyboard+touch and explains why viewing mode never changes safety claims. Note: `npm test` runs the src/test smoke only; S14 player tests run via `node --test tests/player.test.js`. Untracked `content.zip` flagged (not committed).
