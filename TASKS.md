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
Unit code: S17
Unit focus: PWA and demo resilience
Current prompt:

```markdown
# S17 - PWA and demo resilience

## Role
Act as the implementation partner for this bounded PauseSpace InnovationLab session. Preserve student ownership and the approved static, privacy-first architecture.

## Read First
Open README.md, TASKS.md, docs/ProjectPlan.md, docs/Architecture.md, docs/DecisionLog.md, the listed in-scope files, and current tests. Inspect before proposing changes.

## Current State
Confirm the repository checkpoint and report what already works, failing tests, known issues, and active task S17 / P5. Do not assume missing work is complete.

## Session Objective
Add manifest, service worker, offline shell, update/error messaging.

## Scope
In scope: public/manifest.webmanifest; public/sw.js. Make only changes required for “PWA and demo resilience”. Preserve all working behavior outside this boundary.

## Requirements
Add install metadata and a conservative cache strategy for the app shell and approved content; implement version/update/error messaging and documented cache invalidation. Keep the four authoritative scenes and the approved static, local-first, non-diagnostic boundary; use synthetic or properly anonymized data only.

## Implementation Sequence
1) Verify baseline and tests. 2) Create a checkpoint. 3) State the smallest runnable change. 4) Implement in small steps. 5) Run focused tests after each step. 6) Run the session acceptance checks. 7) Update TASKS, Decision Log and Co-build Log.

## Files
Create or modify only: public/manifest.webmanifest; public/sw.js. Explicitly preserve deployed assets, approved scripts, unrelated styles, test evidence and prior decisions.

## Tests and Acceptance Criteria
Acceptance gate: Previously loaded core route works offline; update path is documented. Run first-load/second-load/offline/update/missing-asset tests; verify the previously loaded critical route works and a new release is not trapped behind stale cache. Report exact commands, expected versus actual results, manual checks, and evidence paths. Never invent passing results.

## Evidence to Save
Save dated evidence under evidence/S17/: relevant screenshots or recordings, command/test output, reviewed artifacts, defect references, and the pre/post-session checkpoint IDs. Do not save personal or identifying data.

## Student Manual Work
Student performs the offline and update rehearsal on a phone and records the exact recovery steps. The student must review every diff and write the final Co-build Log decision in their own words.

## Security and Safety
Do not collect names, mental-health histories, family details, mood scores, microphone data, analytics identifiers, or secrets. Do not add diagnosis, treatment, emergency promises, forced breathing, autoplay, or unreviewed support contacts.

## Do Not Do
Do not add frameworks, backend, login, AI runtime chat, cloud sync, trackers, streaks, rankings, unrelated refactors, hidden scope, hard-coded secrets, copied imagery, or the next session’s work.

## TASKS.md Session Activation
Before implementation, update only the editable fields in `TASKS.md`:
- `Unit code: S17`
- `Unit focus: PWA and demo resilience`
- `Current prompt: paste this complete S17 prompt only`
- Replace the three placeholder acceptance lines with this session's observable acceptance criteria.

Do not recreate or overwrite `TASKS.md`. Preserve the full S01-S22 checklist, completed checkmarks, known issues, and last test evidence. After acceptance passes, mark only S17 complete, record actual evidence, and set the next unit only as preparation.

## Checkpoint and Rollback
Record the pre-session checkpoint identifier. If acceptance fails, keep the last runnable state, log the defect, and provide the exact rollback path without erasing evidence.

## Completion Report
List changed files; summarize decisions; show tests and manual checks; identify limitations and unresolved risks; update traceability; name the next safe step without implementing it.

## Stop Condition
Stop when S17 acceptance criteria pass and evidence is saved. Do not begin the next session.
```

## Acceptance Criteria for Current Unit
- A1 — PWA manifest: `public/manifest.webmanifest` is a valid web app manifest (install metadata; non-diagnostic description; original theme/background colors). Icons are placeholders pending production (documented). (Auto-verifiable.)
- A2 — Service worker resilience: `public/sw.js` caches the app shell conservatively, serves the previously-loaded shell offline, falls back safely on missing assets, and uses a **versioned cache + skipWaiting + cleanup** so a new release is not trapped behind stale cache. (Auto-verifiable via mock tests: install caches shell; offline serves cached shell; missing-asset fallback; new version clears old cache.)
- A3 — Evidence + rehearsal: tests + the documented update/cache-invalidation path saved under `evidence/S17/`; the student performs the offline + update rehearsal on a phone and records the exact recovery steps — student-owned manual gate. (Manual, student-owned gate.)

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
- [x] S16
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
- Automated (S17): `evidence/S17/pwa-checks.txt` — `node --test tests/sw.test.mjs` → **6/6 pass** (install caches shell + skipWaiting; second-load idempotent; offline serves cached shell; missing-asset 503; new version clears old cache / not trapped + clients.claim; non-GET ignored); `npm test` 3/3; `npm run build` OK (dist unchanged); validator `evidence/S17/validate_pwa.py` = 17/17.
- Automated (preserved): S16 9/9; S15 8/8; S14 13/13; S13 7/7; S12 16/16; S11 3/3 + clean install/lint/build/start; S10 16/16; S09 12/12; S08 12/12; S07 11/11; S06 22/22; S05 12/12; S04 10/10; S03 14/14; S02 14/14; S01 12/12.
- Content/data validation (S17): manifest is valid JSON with a non-diagnostic description + original colors; sw.js has VERSION + install/activate/fetch + skipWaiting + cache cleanup; no secrets.
- Accessibility/device: PWA is keyboard/screen-reader compatible by construction; the real phone offline+update rehearsal is the student manual gate.
- Manual demo path: **Manual gate (A3) OPEN** — the student performs the offline + update rehearsal on a phone and records the exact recovery steps. Note: `npm test` runs src/test smoke only; S17 SW tests run via `node --test tests/sw.test.mjs` (vm-mock). Manifest/sw not yet served; icons are placeholders. Untracked `assets/audio/audio place folder/` + tracked `content.zip` flagged (recommend remove / `git rm`).
