# Optional AI Audio Extension

## Baseline Freeze

OA01 is an additive option. It does not alter the approved S01-S22 sequence,
the 22 core hours, setup, contingency, or any baseline requirement. The
distributed `TASKS.md` remains unchanged.

## Recommended Insertion Point

Run OA01 after S12, once the repository, content schema, and state contract
exist, and before S13/S14 integrates scene content and the player. S07 and S12
must both be complete.

## Architecture Boundary

Approved scripts -> development-time TTS command -> generated MP3 directory ->
human review -> explicit release mapping -> static/offline site.

The browser never receives the provider key and never calls the provider.
Original/student-recorded tracks are preserved. Generated tracks are selected
only through an explicit, reversible mapping.

## Required Human Review

For each full track, compare audio against the approved transcript and review
pronunciation, pacing, warmth, pauses, volume consistency, clipping/noise,
duration, and safety language. Record reviewer roles, not personal names.

## Provider Decision Gate

Do not proceed until the student/teacher approves provider, model, voice,
locale, cost cap, data handling, and redistribution/showcase rights. Use
official documentation and stop if any right or retention claim is unclear.

## Release Rule

AI-generated narration may be selected only when every track is approved,
locally bundled, disclosed accurately, and proven to work without runtime AI.
If OA01 is skipped or fails, continue with the original S01-S22 recording path.
