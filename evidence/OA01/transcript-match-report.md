# OA01 transcript-match report (after S17)
Captured: 2026-08-05.

## Result: not applicable (ambient-only)
All four supplied tracks are classified **ambient** (see content-classification.md) — they contain
no spoken narration to compare against the approved transcripts. Therefore the transcript-match
gate does not apply to these files in this pass.

## Transcript availability (must remain independent of audio)
Each scene's transcript remains present and same-origin in its content JSON (the runtime
fallback when audio is missing/unavailable):
- exam-room: transcript.text length 537 chars; review.status approved; version exam-room.v1
- sports-field: 548 chars; approved; sports-field.v1
- own-room: 515 chars; approved; own-room.v1
- empty-classroom: 542 chars; approved; empty-classroom.v1

## Rule respected
- Ambient audio does not replace narration. The approved transcripts remain the authoritative
  spoken wording and stay available independently of these audio files.
- If a future supplied/generated track is classified `narration` or `mixed`, its speech must be
  compared word-for-word against the matching transcript version; any mismatch blocks narration
  approval. (No such track exists in this pass.)
