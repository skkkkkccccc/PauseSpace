# User Flows — PauseSpace information architecture (S08)

> **Status: AI-proposed IA; pending the student paper walkthrough.** PauseSpace is
> not diagnosis, treatment, counselling, or emergency support. Every view and
> error state below has an **exit**, and **no completion is ever forced** — the
> user can stop or leave at any point. Local-only; no scores, streaks, or rankings.

## The five views
| # | View | Purpose | Entry | Exit |
|---|---|---|---|---|
| 1 | Home | Landing; pick a scene or go to Pause map / Project/About | App open | Exit: to any view, or leave the app |
| 2 | Scene detail | Preview one scene (title, ~3 min, what to expect) before starting | Tap a scene from Home/Pause map | Exit: back to Home (or Pause map) |
| 3 | Player | Plays the ~3-minute scene; pause/resume, replay (optional), exit always available | Start from Scene detail | Exit: return to Scene detail / Home at any time |
| 4 | Pause map | Local-only overview of the four scenes (available / visited) — no scores, streaks, or rankings | From Home | Exit: to Home / Scene detail |
| 5 | Project/About | What PauseSpace is and is not (non-diagnostic), approved support contacts, credits/licensing | From Home | Exit: back to Home |

## Navigation rules
- Navigation is **deterministic** and client-side (static site; no backend).
- **Every view provides Back and Exit.** No view traps the user.
- **No forced completion:** the Player never requires the user to finish; pause/exit are always available, and the user can leave at any point.
- **No dead ends:** every screen offers at least one forward path and one exit.

## Completion branches
- **Back:** return to the previous view (e.g., Player → Scene detail → Home).
- **Exit:** leave the Player (or the app) at any time; progress (if any) is local-only and never penalized.
- **Replay:** optionally restart the current scene from Scene detail/Player; never automatic.
- **Support:** from any view, reach Project/About → approved support contacts; then back.

## Baseline journeys
Each journey appears once and ends in an exit (no dead end, no forced completion):
- **J1 First visit:** Home → Scene detail → Player → (finish **or** exit early) → Pause map / Home.
- **J2 Replay a scene:** Pause map / Home → Scene detail → Player → replay **or** exit.
- **J3 Browse/About:** Home → Project/About → (read; optional support) → back to Home.
- **J4 Choose not to start:** Home → Scene detail → back to Home (no pressure to begin).

## Error states (each has a recovery and an exit)
- **Loading:** show a calm loading indicator while a scene/audio loads; Exit: the user can leave at any time.
- **Missing-audio:** if audio fails to load, show the transcript with a short message; Recovery/Exit: retry, continue with transcript only, or exit to Scene detail.
- **Offline:** the app is usable offline (local/PWA shell when included); if a required asset is absent, show a graceful message; Recovery/Exit: exit to Home — never a dead end.
- **Update:** if a newer content version is available, show a dismissible notice (no forcing); Recovery/Exit: dismiss and continue, or exit.

## No-dead-end / no-forced-completion checklist
- [ ] Every view has Back + Exit.
- [ ] Every error state has a recovery path and an exit.
- [ ] The Player can be paused or left at any moment; finishing is never required.
- [ ] No screen leaves the user with no forward path or no exit.
