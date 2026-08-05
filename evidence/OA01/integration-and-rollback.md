# OA01 integration & rollback (after S17)
Captured: 2026-08-05.

## Current release mapping (UNCHANGED — no scene/player files modified)
Each scene JSON already carries `audio.src = assets/audio/<scene-id>.mp3` (set in S04/S05 as a
placeholder path). The four supplied MP3s now exist at exactly those paths, so the filename
mapping is satisfied without any change to content/*.json, the player, or the views:

| Scene | audio.src (pre-existing) | File present? | Role | Selected for release? |
|---|---|---|---|---|
| exam-room | assets/audio/exam-room.mp3 | yes | ambient | NO — pending human listening |
| sports-field | assets/audio/sports-field.mp3 | yes | ambient | NO — pending human listening |
| own-room | assets/audio/own-room.mp3 | yes | ambient | NO — pending human listening |
| empty-classroom | assets/audio/empty-classroom.mp3 | yes | ambient | NO — pending human listening |

No track is selected for release: every track is `pending-human-listening`. The supplied files
are preserved in place (not moved/renamed/recompressed). Existing/student-recorded audio and the
`generated/` directory are untouched.

## Manifest
`assets/audio/audio-manifest.placeholder.json` records the four tracks, hashes, derived
duration, role=ambient, sourceLabel=user-supplied-placeholder, reviewStatus=pending-human-listening,
provenance/licensing=pending-review, and the transcript-only fallback. (It does NOT select any
track for release.)

## Deployability gap (reported; not "fixed" — no file relocation)
`src/tools/serve.mjs` (S11) serves only `dist/`. The build (`npm run build`) copies only
`src/{index.html,styles.css,app.js}` into `dist/`. Therefore `assets/audio/*.mp3` is NOT served
by the current dev server and is NOT present in `dist/`. This is consistent with the app/player
not yet being wired (audio playback is a later session). Minimal architectural correction (for a
later session, NOT done here): serve `assets/` at `/assets/` (extend serve.mjs) or copy
`assets/audio` into `dist/assets/audio` at build time. No source file was relocated or duplicated.

## Rollback (non-destructive)
Pre-OA01 checkpoint: `a4953ba`. Nothing committed this pass. To undo the OA01 artifacts:
```
rm -f assets/audio/audio-manifest.placeholder.json tests/supplied-audio.test.mjs
rm -rf evidence/OA01   # (or keep the evidence; it is non-destructive)
git restore TASKS.md docs/DecisionLog.md docs/CoBuildLog.md OPTIONAL_EXTENSIONS.md
```
The scene JSONs' `audio.src` is unchanged (it was already the placeholder path), so rollback
does not require touching content/*.json or the supplied MP3s.
