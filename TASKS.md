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
Unit focus: Supplied audio validation and integration after S17
Current prompt: prompts/PauseSpace_OA01_After_S17_Supplied_Audio_Prompt.md

## Acceptance Criteria for Current Unit
- A1 — Supplied files verified: exactly four expected MP3s exist at `assets/audio/` (contract said `asset/audio/` — typo; canonical plural used; files not moved); SHA-256 hashes recorded; technical properties recorded (actual only; unavailable measurements marked not-measured). (Auto-verifiable — PASS.)
- A2 — Classification + manifest: each track classified truthfully — all four **ambient** per `assets/audio/SCENE_AUDIO_NOTES.txt` (no speech → transcript-match N/A; transcripts remain authoritative); `assets/audio/audio-manifest.placeholder.json` validates (hashes match files); transcripts + missing-audio fallback remain available. (Auto-verifiable — PASS.)
- A3 — Human review + release: each track has a completed human-review decision; only approved tracks selected for release; offline/PWA behavior verified; no provider call / API key / runtime TTS. **BLOCKED — human listening PENDING; no track approved for release; AI narration NOT completed (0 narration tracks).** (Manual, student/mentor-owned gate.)

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
- [x] S17
- [ ] S18
- [ ] S19
- [ ] S20
- [ ] S21
- [ ] S22

## Known Issues
- Deployment host; owner: student and mentor; next action: decide before S21.
- Locally approved support contacts; owner: mentor/adult reviewer; next action: approve before S15 release gate.

## Last Test Evidence
- Automated (OA01): `evidence/OA01/test-and-build-results.txt` — `node --test tests/supplied-audio.test.mjs` → **5/5 pass** (4 MP3s exist; scene→file mapping; manifest schema + hashes match files; transcripts available; no track selected for release); `evidence/OA01/manifest-validation.txt` manifest_valid=true (all 4 hashMatchesFile=true, role=ambient, reviewStatus=pending-human-listening); `npm test` 3/3; `npm run build` OK (dist unchanged).
- Automated (preserved): S17 6/6; S16 9/9; S15 8/8; S14 13/13; S13 7/7; S12 16/16; S11 3/3 + clean install/lint/build/start; S10 16/16; S09 12/12; S08 12/12; S07 11/11; S06 22/22; S05 12/12; S04 10/10; S03 14/14; S02 14/14; S01 12/12.
- Content/data validation (OA01): four supplied MP3s verified at `assets/audio/` (tracked); SHA-256 recorded; classified **ambient** per `SCENE_AUDIO_NOTES.txt`; transcript-match N/A (no speech); transcripts remain available; no provider call / API key / runtime TTS.
- Accessibility/device: transcripts + missing-audio fallback remain usable; real human listening + phone offline rehearsal are the student/mentor manual gates.
- Manual demo path: **Manual gate (A3) OPEN** — student + mentor must listen to all four files, confirm ambient classification + provenance/licensing, and approve/reject before any release selection. Ambient placeholder audio does NOT complete AI narration (0 narration tracks). Note: contract path `asset/audio/` is a typo for `assets/audio/`; `content.zip` still tracked (recommend `git rm`).
