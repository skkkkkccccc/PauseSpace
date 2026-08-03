# Generated audio (OA01)

This directory holds **AI-generated** narration tracks produced by the optional
OA01 extension, kept strictly separate from original/student-recorded audio.

**Status: empty — no tracks generated.** Generation is blocked until OA01's
prerequisite gate clears (see `docs/AudioGenerationRecord.md`):
1. the four scene scripts are approved (`review.status=approved`) with read-aloud
   and mentor/adult approval; and
2. exactly one TTS provider/model/voice/locale/cost is approved with verified
   redistribution rights.

Filenames are stable and non-identifying: `<scene-id>.<transcript-sha-8>.ai.mp3`.
The generation tool refuses draft scripts and never writes here until an approved
generation succeeds.
