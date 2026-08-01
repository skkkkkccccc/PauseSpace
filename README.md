# PauseSpace

A mobile-first, static Web App for four approximately three-minute, scene-based attention-reset experiences for high-school students.

## Boundaries
- No account, backend, database, analytics, mood score, microphone capture, runtime AI chat, streak, or ranking.
- Not diagnosis, treatment, counselling, or emergency support.
- All release scripts require student revision, read-aloud testing, and adult approval.

## Working method
Read `TASKS.md`, `docs/ProjectPlan.md`, `docs/Architecture.md`, and the active prompt before changing anything. Keep the project runnable, run tests, save evidence, update the Co-build Log, and stop at the active session boundary.

## Run (repository, since S11)
Minimal native HTML/CSS/JS — no frameworks, no backend, **zero runtime dependencies**, runtime secret-free. Requires Node.js >= 20.

```bash
npm install      # install (zero deps; succeeds offline)
npm test         # run unit tests (node:test)
npm run lint     # scan src for secrets, external URLs, trackers, medical claims
npm run build    # copy src/{index.html,styles.css,app.js} -> dist/
npm start        # serve dist/ at http://localhost:3000
npm run preview  # build, then start
```

Layout: `src/index.html`, `src/styles.css`, `src/app.js` (app); `src/test/` (tests); `src/tools/` (lint/build/serve scripts). Scene content lives in `content/`; design tokens in `design/tokens.css`; the low-fi prototype in `design/prototype/`.
