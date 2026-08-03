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
Unit code: OA01
Unit focus: Optional AI-generated narration production and curation
Current prompt: prompts/OptionalAudioSessionOA01.md

## Acceptance Criteria for Current Unit
- A1 — Prerequisites + provider decision (manual gates): S07/S12 complete; the four scripts approved (`review.status=approved`) with read-aloud + mentor/adult approval; exactly one TTS provider/model/voice/locale/cost approved with verified redistribution rights. **Currently BLOCKING generation (scripts are draft; no provider chosen).**
- A2 — Safe generation tooling: dry-run makes zero provider requests and exposes no secret; generation refuses draft/unapproved/transcript-hash-mismatched input; one preview gate before the remaining three; bounded retries, stop on errors. (Auto-verifiable for dry-run/refusal — built.)
- A3 — Four reviewed MP3s + reversible release: four non-empty MP3s under `assets/audio/generated/` with input/output hashes, duration, size, `reviewStatus`; human review per track; reversible same-origin release mapping; no secret in git/build; the runtime site makes no TTS request; AI narration disclosed. **Blocked pending A1.**

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
- Automated (S12): `evidence/S12/test-report.txt` — `node --test tests/*.test.mjs` → **16/16 pass** (scene-loader 6, player 5, progress 5: valid/missing/malformed/stale-version/interrupted-playback/reset); `npm test` (S11 smoke) still 3/3; no secrets in new modules; structural validator `evidence/S12/validate_contracts.py` = 10/10.
- Automated (preserved): S11 3/3 (npm test) + clean install/lint/build/start; S10 16/16; S09 12/12; S08 12/12; S07 11/11; S06 22/22; S05 12/12; S04 10/10; S03 14/14; S02 14/14; S01 12/12.
- Content/data validation (S12): scene-loader validates against `content/schema.json` (exam-room sample); progress payload is versioned with no scores/streaks/identifying data.
- Accessibility/device: Not the focus of S12 (data/state contracts, no UI). Deferred to the feature build.
- Manual demo path: **Manual gate (A3) OPEN** — the student draws/explains the state machine and adds at least one edge-case test personally. Note: `npm test` runs the src/test smoke only; S12 tests run via `node --test tests/*.test.mjs` (wiring `tests/` into the npm script is a later-session item — package.json is out of S12 scope).
