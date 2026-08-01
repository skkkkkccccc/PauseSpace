# PauseSpace — low-fidelity mobile prototype (S09)

A static, clickable vertical slice for **one scene** (exam-room). This is a
prototype to support a usability test — it is deliberately low-fidelity and is
**not** the production app.

## Run it
Open `index.html` in a browser (double-click, or use a phone-sized viewport).
No server, no build, no dependencies. Best viewed at a mobile width (~390–420 px).

## What it covers
Scene card (Home) → Scene detail → Player → Completion, plus an About view.
- The Player steps through the four exam-room script segments (synthetic copy
  from `content/exam-room.json`) with a progress bar.
- **Explicit exit controls** on every view; the user can leave at any time
  (no forced completion).
- Mobile-first layout with large tap targets.

## Boundaries (prototype only)
- Synthetic copy; **no real audio** (placeholder).
- No backend, no account, no tracking, no network calls, no frameworks.
- Not diagnosis, treatment, counselling, or emergency support.
- Only the exam-room scene is wired up (the other three scenes are out of scope
  for this prototype).

## Files
- `index.html` — the prototype (HTML + inline CSS + inline JS).
