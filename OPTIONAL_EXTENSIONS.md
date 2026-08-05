# Optional Extensions

Optional units that extend the S01–S22 baseline without renumbering, replacing, or
altering it. They do not count toward the 22 core sessions.

## OA01 — Audio (optional)
- **Status (2026-08-05, after S17):** supplied-audio validation executed. Four
  user-supplied MP3s at `assets/audio/` were verified, hashed, and classified
  **ambient** (per `assets/audio/SCENE_AUDIO_NOTES.txt`). No TTS provider was
  called, no API key was used, and no supplied file was modified, moved, renamed,
  recompressed, or normalized.
- `assets/audio/audio-manifest.placeholder.json` records the four tracks
  (role `ambient`, `sourceLabel user-supplied-placeholder`,
  `reviewStatus pending-human-listening`).
- **AI-generated narration is NOT completed (0 of 4 tracks are narration).**
  Ambient placeholder audio does not complete the narration requirement and is
  never labeled `tts`/`narration`.
- **Release selection is BLOCKED** until the student + mentor complete the human
  listening review (`evidence/OA01/human-review-checklist.md`) and confirm
  provenance/licensing. No track is selected for release yet.
- The earlier OA01 TTS-generation scaffolding (parked at commit `2d80457`) remains
  available; a provider decision is still pending if AI narration is pursued later.
- Evidence: `evidence/OA01/` (source-inventory, checksums, audio-technical-report,
  content-classification, transcript-match-report, human-review-checklist,
  manifest-validation, test-and-build-results, offline-playback-check,
  integration-and-rollback).
