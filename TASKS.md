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
Unit code: S16
Unit focus: Pause map & local privacy controls
Current prompt:

```markdown
# S16 - Pause map & local privacy controls

## Role
Act as the implementation partner for this bounded PauseSpace InnovationLab session. Preserve student ownership and the approved static, privacy-first architecture.

## Read First
Open README.md, TASKS.md, docs/ProjectPlan.md, docs/Architecture.md, docs/DecisionLog.md, the listed in-scope files, and current tests. Inspect before proposing changes.

## Current State
Confirm the repository checkpoint and report what already works, failing tests, known issues, and active task S16 / P5. Do not assume missing work is complete.

## Session Objective
Implement completion lighting, versioned localStorage, reset, privacy note.

## Scope
In scope: src/state/progressStore.js; src/views/Map.js. Make only changes required for “Pause map & local privacy controls”. Preserve all working behavior outside this boundary.

## Requirements
Implement schema-validated completion lights only; provide local-data explanation, full reset, corrupt-data recovery, and storage-version migration; store no free text or mood score. Keep the four authoritative scenes and the approved static, local-first, non-diagnostic boundary; use synthetic or properly anonymized data only.

## Implementation Sequence
1) Verify baseline and tests. 2) Create a checkpoint. 3) State the smallest runnable change. 4) Implement in small steps. 5) Run focused tests after each step. 6) Run the session acceptance checks. 7) Update TASKS, Decision Log and Co-build Log.

## Files
Create or modify only: src/state/progressStore.js; src/views/Map.js. Explicitly preserve deployed assets, approved scripts, unrelated styles, test evidence and prior decisions.

## Tests and Acceptance Criteria
Acceptance gate: Progress survives refresh, resets fully, and stores no sensitive text. Test refresh persistence, duplicate completion, partial/corrupt payload, old version, private browsing limitation, and complete reset; inspect storage manually. Report exact commands, expected versus actual results, manual checks, and evidence paths. Never invent passing results.

## Evidence to Save
Save dated evidence under evidence/S16/: relevant screenshots or recordings, command/test output, reviewed artifacts, defect references, and the pre/post-session checkpoint IDs. Do not save personal or identifying data.

## Student Manual Work
Student inspects localStorage, explains every stored field, and demonstrates reset and corruption recovery. The student must review every diff and write the final Co-build Log decision in their own words.

## Security and Safety
Do not collect names, mental-health histories, family details, mood scores, microphone data, analytics identifiers, or secrets. Do not add diagnosis, treatment, emergency promises, forced breathing, autoplay, or unreviewed support contacts.

## Do Not Do
Do not add frameworks, backend, login, AI runtime chat, cloud sync, trackers, streaks, rankings, unrelated refactors, hidden scope, hard-coded secrets, copied imagery, or the next session’s work.

## TASKS.md Session Activation
Before implementation, update only the editable fields in `TASKS.md`:
- `Unit code: S16`
- `Unit focus: Pause map & local privacy controls`
- `Current prompt: paste this complete S16 prompt only`
- Replace the three placeholder acceptance lines with this session's observable acceptance criteria.

Do not recreate or overwrite `TASKS.md`. Preserve the full S01-S22 checklist, completed checkmarks, known issues, and last test evidence. After acceptance passes, mark only S16 complete, record actual evidence, and set the next unit only as preparation.

## Checkpoint and Rollback
Record the pre-session checkpoint identifier. If acceptance fails, keep the last runnable state, log the defect, and provide the exact rollback path without erasing evidence.

## Completion Report
List changed files; summarize decisions; show tests and manual checks; identify limitations and unresolved risks; update traceability; name the next safe step without implementing it.

## Stop Condition
Stop when S16 acceptance criteria pass and evidence is saved. Do not begin the next session.
```

## Acceptance Criteria for Current Unit
- A1 — Versioned local storage + reset: `src/state/progressStore.js` provides **schema-validated completion lights** (the 4 known scenes only), refresh persistence, full reset, and corrupt/old-version recovery via the S12 progress migration; it stores **only a `visited` flag** (no free text / mood score / names). (Auto-verifiable.)
- A2 — Pause map view: `src/views/Map.js` renders the 4 scenes with **non-judgmental** completion lights + the local-privacy note + reset; no scores/streaks/rankings. (Auto-verifiable; private-browsing + manual localStorage inspection are the manual gate.)
- A3 — Evidence + review: tests + manual storage inspection saved under `evidence/S16/`; the student inspects localStorage, explains every stored field, and demonstrates reset + corruption recovery — student-owned manual gate. (Manual, student-owned gate.)

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
- [x] S15
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
- Automated (S16): `evidence/S16/map-checks.txt` — `node --test tests/map.test.mjs` → **9/9 pass** (refresh persistence; duplicate idempotent; corrupt/partial recovery; old-version migration; complete reset; stores only a visited flag / no mood score; unknown scene refused; map renders lights + privacy + reset); `npm test` 3/3; `npm run build` OK (dist unchanged); validator `evidence/S16/validate_map.py` = 10/10.
- Automated (preserved): S15 8/8; S14 13/13; S13 7/7; S12 16/16; S11 3/3 + clean install/lint/build/start; S10 16/16; S09 12/12; S08 12/12; S07 11/11; S06 22/22; S05 12/12; S04 10/10; S03 14/14; S02 14/14; S01 12/12.
- Content/data validation (S16): progress payload stores only `{version, scenes:{id:{visited}}, updatedAt}` — no free text / mood score / names; corrupt + old-version + partial payloads recover to empty.
- Accessibility/device: map is keyboard-operable + non-judgmental; formal device + private-browsing checks are the student manual gate.
- Manual demo path: **Manual gate (A3) OPEN** — the student inspects localStorage, explains every stored field, and demonstrates reset + corruption recovery. Note: `npm test` runs src/test smoke only; S16 map tests run via `node --test tests/map.test.mjs`. `content.zip` still tracked (benign); recommend `git rm`.
