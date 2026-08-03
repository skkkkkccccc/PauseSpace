# Audio Generation Record (OA01 — optional)

> **Status: scaffolding delivered; four scripts APPROVED; generation BLOCKED on
> the provider decision.** No audio has been generated. No provider is chosen.
> No release mapping applied. This record is honest — it does not fabricate
> reviews, approvals, or generation results.

## Prerequisite gate (OA01 §Current State)
| Prerequisite | Status |
|---|---|
| S07 complete (evidence exists) | ✅ |
| S12 complete (evidence exists) | ✅ |
| Four scripts: stable version IDs + exact transcripts + timed read-aloud + student approval + mentor/adult approval | ✅ Approved 2026-08-03 (`review.status=approved`; versions frozen v1) |
| Git working tree clean / changes documented | ✅ (pre-extension checkpoint `8b88e96`) |
| No original/student audio overwritten | ✅ (`assets/audio/` has only docs; no MP3s) |

## Required provider decision
❌ **PENDING.** `config/audio-generation.env.example` is placeholder-only. No
provider/model/voice/locale/cost/redistribution-rights approved. Per OA01 the
provider is **not** chosen silently and generation does not proceed without it.

## What was built (safe, no generation)
- `scripts/lib/tts-provider.mjs` — dry-run plan (no network, no secret in output),
  transcript SHA-256, `generationBlockedReason()` (refuses unapproved script or
  no/unapproved provider), `generate()` that returns a safe error (no network)
  unless an approved provider is wired. No third-party SDK imported.
- `scripts/generate-audio.mjs` — CLI: `--dry-run` (zero provider requests; reports
  each scene's status/hash/planned output; states the generation gate) and
  `--scene <id> [--preview]` (refuses without an approved provider; writes no MP3).
- `tests/audio-generation.test.mjs` — 9 tests (no-secret dry-run; refusal of draft
  script / unconfigured / unapproved provider via fixtures; CLI dry-run safety;
  CLI generation blocked; deterministic hash).
- `assets/audio/generated/` (empty) + `assets/audio/audio-manifest.generated.json`
  (empty tracks; provider pending).
- `package.json` — `audio:dry-run`, `audio:generate`, `test:audio` (zero deps).

The production build (`npm run build`) copies only `src/{index.html,styles.css,app.js}`
to `dist/` — it contains **no** TTS SDK, key, or runtime generation path.

## Dry-run result (real; see `evidence/OA01/dry-run.txt`)
All four scenes report `status=approved approved=true`. Provider unconfigured.
"Scripts approved; generation still BLOCKED: no approved provider configured."
Zero network calls. No MP3s written.

## To finish OA01 (only the provider decision remains)
1. ✅ Scripts approved (2026-08-03).
2. Approve exactly one TTS provider/model/voice/locale + per-run cost cap, with
   verified redistribution/showcase rights, via the gitignored local env file.
3. Re-run OA01 from the gate: dry-run → one preview → preview approval → the
   remaining three (one at a time) → per-track human review → reversible release
   mapping → AI-narration disclosure.

## Rollback
Nothing committed this session; no original audio file was modified. Remove the
OA01 scaffolding and revert the approval with:
```
git restore TASKS.md package.json docs/DecisionLog.md docs/CoBuildLog.md docs/ContentReview.md content/exam-room.json content/sports-field.json content/own-room.json content/empty-classroom.json
rm -rf scripts tests/audio-generation.test.mjs assets/audio/generated assets/audio/audio-manifest.generated.json docs/AudioGenerationRecord.md evidence/OA01
```
(Preserve the S12 `tests/` files — only remove `tests/audio-generation.test.mjs`.)
