# OA01 offline / PWA playback check (after S17)
Captured: 2026-08-05.

## Existing caching strategy (S17, unchanged)
`public/sw.js` precaches only the app shell: `["/", "/index.html", "/styles.css", "/app.js"]`
(versioned `pausespace-v1`; cache-first; offline navigation fallback; missing-asset → 503).
It is a **conservative** shell cache. The four ~4.3 MB ambient MP3s are **NOT** in the precache
list (intentionally — large media is not force-cached).

## Offline behavior (verified via the S17 vm-mock; real device rehearsal is the student gate)
- **App shell:** loads offline (cached). Verified by `tests/sw.test.mjs` ("offline: previously-loaded shell is served").
- **Scene audio files:** NOT precached → on a cold offline visit the audio request would fail.
  The player's missing-audio path then applies (S14 `AudioPlayer` `hasAudio`/error state) and the
  **transcript remains available** (each scene's `transcript.text`). Navigation, exit, and support
  info are never blocked by audio failure.
- This matches the contract: "Audio failure must never block navigation, exit, transcript access,
  or support information" and "offline/PWA availability according to the existing caching strategy."

## Not done (out of scope)
- The SW was NOT modified to precache audio (would add ~17 MB and is a separate caching decision).
- Real on-device offline rehearsal is the student/mentor manual gate (see human-review-checklist.md).
