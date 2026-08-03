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
Unit code: S13
Unit focus: Home and scene views
Current prompt:

```markdown
# S13 - Home and scene views

## Role
Act as the implementation partner for this bounded PauseSpace InnovationLab session. Preserve student ownership and the approved static, privacy-first architecture.

## Read First
Open README.md, TASKS.md, docs/ProjectPlan.md, docs/Architecture.md, docs/DecisionLog.md, the listed in-scope files, and current tests. Inspect before proposing changes.

## Current State
Confirm the repository checkpoint and report what already works, failing tests, known issues, and active task S13 / P5. Do not assume missing work is complete.

## Session Objective
Implement responsive scene cards and detail view from JSON.

## Scope
In scope: src/views/; src/components/SceneCard.js. Make only changes required for “Home and scene views”. Preserve all working behavior outside this boundary.

## Requirements
Render four scene cards and one detail view from validated JSON; implement responsive navigation, empty/error states, semantic structure, and safe text insertion. Keep the four authoritative scenes and the approved static, local-first, non-diagnostic boundary; use synthetic or properly anonymized data only.

## Implementation Sequence
1) Verify baseline and tests. 2) Create a checkpoint. 3) State the smallest runnable change. 4) Implement in small steps. 5) Run focused tests after each step. 6) Run the session acceptance checks. 7) Update TASKS, Decision Log and Co-build Log.

## Files
Create or modify only: src/views/; src/components/SceneCard.js. Explicitly preserve deployed assets, approved scripts, unrelated styles, test evidence and prior decisions.

## Tests and Acceptance Criteria
Acceptance gate: Four cards render from data; no duplicated hard-coded content. Run component/integration tests and manual mobile-width checks; confirm no scene copy is duplicated in view code and malformed content fails visibly. Report exact commands, expected versus actual results, manual checks, and evidence paths. Never invent passing results.

## Evidence to Save
Save dated evidence under evidence/S13/: relevant screenshots or recordings, command/test output, reviewed artifacts, defect references, and the pre/post-session checkpoint IDs. Do not save personal or identifying data.

## Student Manual Work
Student compares the implementation with the approved flow and inspects the rendered DOM/data path. The student must review every diff and write the final Co-build Log decision in their own words.

## Security and Safety
Do not collect names, mental-health histories, family details, mood scores, microphone data, analytics identifiers, or secrets. Do not add diagnosis, treatment, emergency promises, forced breathing, autoplay, or unreviewed support contacts.

## Do Not Do
Do not add frameworks, backend, login, AI runtime chat, cloud sync, trackers, streaks, rankings, unrelated refactors, hidden scope, hard-coded secrets, copied imagery, or the next session’s work.

## TASKS.md Session Activation
Before implementation, update only the editable fields in `TASKS.md`:
- `Unit code: S13`
- `Unit focus: Home and scene views`
- `Current prompt: paste this complete S13 prompt only`
- Replace the three placeholder acceptance lines with this session's observable acceptance criteria.

Do not recreate or overwrite `TASKS.md`. Preserve the full S01-S22 checklist, completed checkmarks, known issues, and last test evidence. After acceptance passes, mark only S13 complete, record actual evidence, and set the next unit only as preparation.

## Checkpoint and Rollback
Record the pre-session checkpoint identifier. If acceptance fails, keep the last runnable state, log the defect, and provide the exact rollback path without erasing evidence.

## Completion Report
List changed files; summarize decisions; show tests and manual checks; identify limitations and unresolved risks; update traceability; name the next safe step without implementing it.

## Stop Condition
Stop when S13 acceptance criteria pass and evidence is saved. Do not begin the next session.
```

## Acceptance Criteria for Current Unit
- A1 — Four cards render from data; no hard-coded scene copy: `src/views/` + `src/components/SceneCard.js` render four scene cards + a detail view from the validated scene JSON (`content/*.json` via `src/data/scene-loader.mjs`); the view/component source contains no scene-specific copy. (Auto-verifiable.)
- A2 — Robust rendering: malformed content fails visibly (error state, no throw); empty state handled; safe text insertion (HTML-escaped); semantic structure; **no audio playback and no runtime TTS in S13**. (Auto-verifiable for malformed/empty/escape/no-TTS; mobile-width is the manual check.)
- A3 — Evidence + review: component/integration tests + a manual mobile-width check saved under `evidence/S13/`; the student compares with the approved flow (`docs/UserFlows.md`) and inspects the rendered DOM/data path — student-owned manual gate. (Manual, student-owned gate.)

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
- Automated (S13): `evidence/S13/views-checks.txt` — `node --test tests/views.test.mjs` → **7/7 pass** (four cards render from data; no hard-coded scene copy; malformed fails visibly; empty state; safe escape; no audio element/TTS); `npm test` 3/3; `npm run build` OK (dist unchanged); validator `evidence/S13/validate_views.py` = 13/13.
- Automated (preserved): S12 16/16; S11 3/3 + clean install/lint/build/start; S10 16/16; S09 12/12; S08 12/12; S07 11/11; S06 22/22; S05 12/12; S04 10/10; S03 14/14; S02 14/14; S01 12/12.
- Content/data validation (S13): views render from validated `content/*.json` via `src/data/scene-loader.mjs`; no scene copy hard-coded in view source; safe (escaped) text insertion.
- Accessibility/device: View HTML is semantic (`section`/`aria-label`); formal mobile-width + AT checks are the student manual gate. (OA01 TTS deferred — no runtime TTS in S13.)
- Manual demo path: **Manual gate (A3) OPEN** — the student compares with the approved flow (`docs/UserFlows.md`), inspects the rendered DOM/data path, and does a mobile-width check. Note: `npm test` runs the src/test smoke only; S13 view tests run via `node --test tests/views.test.mjs`.
