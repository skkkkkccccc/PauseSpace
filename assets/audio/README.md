# Audio recording plan — PauseSpace (S07)

> **Status: plan only. The short test recording is PENDING** — the student
> records a sample, listens on a phone speaker and on headphones, and decides
> whether the setup is acceptable before recording the four scenes. Original or
> properly licensed audio only; same-origin; no copied/unlicensed media.

## Recording setup (quiet)
- Record in a quiet, softly furnished room (curtains, rugs, or soft surfaces) to reduce echo and reverb.
- Use a phone or USB mic placed close to the speaker (about a hand-span away), with a pop filter or slight off-axis angle to soften plosives.
- Put the device in airplane mode / do-not-disturb to avoid interruptions and notifications in the take.
- Record at the project's standard sample rate; keep the same setup for all four scenes for consistent tone and pacing.

## Filenames
- One file per scene, named exactly `assets/audio/<scene-id>.mp3`:
  - `assets/audio/exam-room.mp3`
  - `assets/audio/sports-field.mp3`
  - `assets/audio/own-room.mp3`
  - `assets/audio/empty-classroom.mp3`
- These match each scene JSON's `audio.src`. Files are same-origin and committed with the build; no external media URLs.

## Levels
- Target speech peak below about **-3 dBFS** (avoid clipping).
- Normalize across scenes to a consistent loudness (roughly **-16 to -14 LUFS** for calm speech) so no scene is markedly louder/quieter than another.
- Leave the calm pacing and pauses from the script intact — do not over-compress the quiet passages.

## Retake log
- Keep a retake log locally (outside Git, e.g. in the gitignored `private-research/`), one row per take:
  `scene | take # | date/time | notes (fluffed line, noise, levels) | keep?`
- Only the final approved MP3 per scene is committed; raw takes and the retake log stay out of Git.

## Transcript match
- Each recorded MP3 must match the scene's `transcript.text` exactly in wording.
- The transcript version ID must equal the script version ID (`<scene-id>.v<N>`) recorded in `docs/ContentReview.md`. Re-recording after a wording change requires a new version ID.

## License and origin evidence
- Recordings are **original** (student/adult voice) and therefore owned, **or** properly licensed with documented permission — never copied or unlicensed.
- Record provenance per asset in the asset manifest (a later session): origin, license/permission, and version. Same-origin MP3 only; no third-party embedded audio.

## Test recording (student manual — PENDING)
1. Record a short sample of one approved script using the setup above.
2. Listen on a **phone speaker** and on **headphones**.
3. Decide whether the setup is acceptable (quiet, clear, consistent level, no clipping/noise).
4. Record the decision (accept/reject + notes) under `evidence/S07/`. Do not commit raw audio unless it is the same-origin approved MP3.
