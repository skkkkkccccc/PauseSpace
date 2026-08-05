# OA01 audio technical report (after S17)
Captured: 2026-08-05. Read-only inspection. Files NOT modified.

## Tooling available
- `file`, `stat`, `shasum -a 256`, `xxd`: available.
- `ffprobe` / `sox`: **NOT installed** → duration is derived; loudness/peak/clipping/silence are NOT measured (recorded as not-measured, not fabricated).

## Per-file results (identical format across all four)
| Scene | File | Size (bytes) | SHA-256 (first 12) | Format |
|---|---|---|---|---|
| empty-classroom | assets/audio/empty-classroom.mp3 | 4321676 | 2ce372d107fb… | MPEG ADTS, layer III, v1, 192 kbps, 44.1 kHz, Stereo, ID3v2.4 |
| exam-room | assets/audio/exam-room.mp3 | 4321664 | d11f5bd7e58b… | MPEG ADTS, layer III, v1, 192 kbps, 44.1 kHz, Stereo, ID3v2.4 |
| own-room | assets/audio/own-room.mp3 | 4321667 | f291d7051cbc… | MPEG ADTS, layer III, v1, 192 kbps, 44.1 kHz, Stereo, ID3v2.4 |
| sports-field | assets/audio/sports-field.mp3 | 4321670 | 585d14aced3a… | MPEG ADTS, layer III, v1, 192 kbps, 44.1 kHz, Stereo, ID3v2.4 |

Command: `file assets/audio/*.mp3` → "Audio file with ID3 version 2.4.0, contains: MPEG ADTS, layer III, v1, 192 kbps, 44.1 kHz, Stereo" (exit 0).

## Derived measurements (ffprobe unavailable)
- **Duration:** ~180 s each, derived from size ÷ bitrate (4321664 B ÷ 24000 B/s ≈ 180.07 s). Consistent with the scene 180 s budget and SCENE_AUDIO_NOTES.txt ("segment entry points: 0, 30, 120, 165"). NOT a precise measured duration.
- **Container/codec:** MPEG-1 Layer III (MP3); **bitrate:** 192 kbps (CBR per `file`); **sample rate:** 44.1 kHz; **channels:** stereo.

## NOT measured (no tool) — recorded honestly, not fabricated
- Corrupt-frame / full-decode audit (only `file` header parse run; no decode errors indicated).
- Peak level, integrated loudness (LUFS), clipping risk.
- Leading/internal/trailing silence.

## Embedded metadata
- ID3v2.4 tag present. Confirmed title tag for exam-room.mp3 = "Exam room" (xxd). Filename mapping is authoritative per the contract; other tags not individually enumerated.

## Provenance / licensing
- Source: user-supplied placeholder (no TTS provider call, no API key). Originality/licensing status: **pending student/mentor confirmation** (see human-review-checklist.md).
