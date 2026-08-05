# OA01 human-review checklist (PENDING — student + mentor/teacher)
Prepared: 2026-08-05. The coding agent must NOT make the approval decision.

The student and mentor/teacher must listen to each file in full on headphones AND
ordinary speakers, then record a decision per track. Until this is complete, NO
track is selected for release (all `reviewStatus = pending-human-listening`).

## Per-track review (one row each)
For each file — confirm scene mapping, classification, and suitability; record
timestamped problems and a decision (approved / rejected / needs revision).

| Scene / file | Mapping confirmed? | Classification (ambient) confirmed by listening? | Volume balance / artifacts / abrupt transitions | Suitable for scene? | Decision |
|---|---|---|---|---|---|
| empty-classroom — assets/audio/empty-classroom.mp3 (sha256 2ce372d1…) | ☐ | ☐ | ☐ | ☐ | ______ |
| exam-room — assets/audio/exam-room.mp3 (sha256 d11f5bd7…) | ☐ | ☐ | ☐ | ☐ | ______ |
| own-room — assets/audio/own-room.mp3 (sha256 f291d705…) | ☐ | ☐ | ☐ | ☐ | ______ |
| sports-field — assets/audio/sports-field.mp3 (sha256 585d14ac…) | ☐ | ☐ | ☐ | ☐ | ______ |

## Items requiring explicit human approval before release
1. **Provenance & licensing** of each supplied MP3 — confirm original or properly licensed; permitted for educational demo + public showcase + redistribution. (Currently `provenance/licensing = pending-review`.)
2. **Classification confirmation** — confirm each track is ambient (no inadvertent speech) by listening.
3. **Release selection** — only after 1 & 2 approve a track may its `reviewStatus` move to `approved` and be selected in the scene/player release mapping.
4. **Missing-audio fallback** — verify one scene's fallback (transcript + missing-audio message) works when audio is absent.

## Reminder
Ambient placeholder audio is acceptable as scene ambience but does **not** complete AI-generated
narration. Do not mark OA01 narration complete on the basis of these files.
