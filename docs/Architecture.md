# Architecture

Static HTML/CSS/JavaScript; versioned scene JSON; same-origin MP3 and transcripts; deterministic player state; validated localStorage progress; optional PWA shell; no backend.

## Information architecture (added S08; detail in `docs/UserFlows.md`)

The app has **five views** with deterministic, client-side navigation:

1. **Home** — landing and scene selection.
2. **Scene detail** — preview a scene (title, ~3 min, what to expect) before starting.
3. **Player** — plays the ~3-minute scene; pause/resume, optional replay, exit always available.
4. **Pause map** — local-only overview of the four scenes (available/visited); no scores, streaks, or rankings.
5. **Project/About** — what PauseSpace is and is not (non-diagnostic), approved support contacts, credits/licensing.

**Navigation and completion:** every view provides Back and Exit; the Player never
forces completion (the user can stop or leave at any point). **Error states** —
loading, missing-audio, offline, and update — each have a recovery path and an
exit, so there are no dead ends. Full flow map, baseline journeys, and the
no-dead-end / no-forced-completion checklist live in `docs/UserFlows.md`.

The data contract for each scene is `content/schema.json`; the four launch scenes
are `content/exam-room.json`, `content/sports-field.json`, `content/own-room.json`,
and `content/empty-classroom.json`. Progress uses the validated localStorage key
`pausespace.progress.v1` (`config/sample-config.json`); no backend, no analytics.
