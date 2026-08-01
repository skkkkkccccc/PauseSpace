# Accessibility — PauseSpace (S10)

WCAG **2.2 Level AA** is the target for the production app. Tokens live in
`design/tokens.css`. This spec is applied at the app build (S11+); the
prototype-review column records the S09 prototype state (honest, not invented).

## Checklist (WCAG 2.2 AA-oriented)
| Area | Requirement | Prototype review |
|---|---|---|
| Reduced motion | Honor `prefers-reduced-motion`; no essential motion | Pass — prototype has no transitions/animations |
| Contrast | ≥ 4.5:1 body text; ≥ 3:1 large text / UI | Pass — computed AA on the prototype palette (`evidence/S10/a11y-checks.txt`) |
| Touch targets | ≥ 44×44 CSS px | Pass — buttons use 16px padding (~ ≥44px height) |
| Focus visibility | Visible focus on every interactive element; never removed without replacement | Pass (default) — no `outline:none`; production will use `--ps-focus` |
| Keyboard order | DOM order matches reading/operable order | Pass — sections are sequential; production must keep tab order |
| Zoom | Usable at 200% page zoom; viewport must not disable zoom | Pass — viewport has no `user-scalable=no`/`maximum-scale=1` |
| Transcripts | Each scene provides a transcript; the UI exposes it | Provided — `transcript.text` per scene; UI must surface it (S11) |
| Status / messages | Programmatic status via `aria-live`/roles; sections labelled | Partial — prototype uses `aria-label` on sections; production adds `aria-live` for player status |
| Responsive | Mobile-first breakpoints (≥600px, ≥900px) | Defined — `design/tokens.css` |
| Assets | Original or properly licensed; no copied/unlicensed media | Pass — prototype uses no images; production keeps original/licensed, same-origin |

## Notes and open items for the build (S11+)
- Add an explicit visible-focus style app-wide using `--ps-focus` (the prototype relies on the browser default, which is acceptable but not branded).
- Expose each scene's transcript in the UI (data is present in `content/*.json`).
- Add `aria-live` regions for player progress/completion status messaging.
- Keep DOM/tab order aligned with the reading order in `docs/UserFlows.md`.

## Asset provenance
- All assets must be original (student/adult-owned) or properly licensed, and
  same-origin. The student documents provenance per asset (origin, license,
  version) in the asset manifest at the build session. No copied or unlicensed
  imagery/audio. (See also `assets/audio/README.md` and `docs/ContentReview.md`.)
