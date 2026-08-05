# OA01 — Supplied Audio Validation and Integration (After S17)

## Role

Act as the implementation partner for the optional PauseSpace unit `OA01`.
Execute this unit only after `S17` has passed and before `S18` begins.

Treat the four supplied MP3 files as candidate placeholder audio. Their presence
does not prove that they contain narration, match the approved transcripts, or
are ready for release. Inspect, classify, review, and integrate them truthfully.

Preserve the approved `S01–S22` baseline, all existing narration and audio, and
the static, privacy-first architecture.

## Authoritative Supplied-Audio Location

The user will place the four MP3 files directly in:

```text
./asset/audio/
```

Expected files:

```text
asset/audio/
├── empty-classroom.mp3
├── exam-room.mp3
├── own-room.mp3
└── sports-field.mp3
```

This directory is the authoritative supplied-audio input. Do not search for a
ZIP archive. Do not expect `imports/OA01/`, `assets/audio/generated/`, or an
`audio_placeholder` subdirectory.

Do not download, regenerate, rename, move, recompress, normalize, replace, or
overwrite these four source files. If a file is missing, duplicated, corrupt,
or named differently, stop and report the exact discrepancy.

## Read First

Before proposing or making changes, read completely:

- `README.md`
- `TASKS.md`
- `OPTIONAL_EXTENSIONS.md`, if present
- `docs/ProjectPlan.md`, if present
- `docs/Architecture.md`, if present
- `docs/DecisionLog.md`
- `docs/CoBuildLog.md`
- `docs/ContentReview.md`, if present
- `prompts/GlobalEngineeringContract.md`
- `prompts/OptionalAudioSessionOA01.md`, if present
- the `S17` prompt and its actual completion evidence
- all four authoritative scene-content JSON files
- the current audio manifest, scene loader, audio player, asset-path handling,
  service-worker/PWA configuration, and related tests

If an optional file does not exist, report that fact. Continue only when the
repository still contains enough authoritative information to execute safely.

## Prior-State Gate

Before modifying files:

1. Run `git status --short` and record the current checkpoint commit ID.
2. Confirm that `S17` is complete and its evidence exists.
3. Confirm that `S18` has not started and no later baseline session is active.
4. Confirm that the working tree contains no unrelated or unexplained changes.
5. Confirm that all four expected MP3 files exist under `asset/audio/`.
6. Confirm that `OA01` remains optional and does not renumber, replace, or
   rewrite any baseline session.
7. Identify the current narration/audio mapping and its rollback path.

If any gate fails, stop. Report the blocker without changing the repository.

## Session Objective

Validate and classify the four supplied MP3 files, preserve them in place,
record technical and human-review evidence, create a deterministic manifest,
and connect only approved files to their matching PauseSpace scenes.

Do not call a TTS provider. Do not request an API key. Do not claim that a file
contains TTS narration unless speech is actually present and matches the
approved transcript.

## Deterministic Scene Mapping

| Source file | Scene ID |
| --- | --- |
| `asset/audio/empty-classroom.mp3` | `empty-classroom` |
| `asset/audio/exam-room.mp3` | `exam-room` |
| `asset/audio/own-room.mp3` | `own-room` |
| `asset/audio/sports-field.mp3` | `sports-field` |

Do not infer a different scene from metadata or audio mood. Filename mapping is
authoritative unless the user explicitly corrects it.

## Critical Content-Classification Gate

For each MP3, use technical inspection and full human listening to classify it
as exactly one of:

- `narration` — spoken narration with no meaningful ambient layer;
- `ambient` — background or scene audio with no spoken narration;
- `mixed` — spoken narration combined with ambient audio.

Apply these rules:

- Never label ambient-only audio as `tts` or `narration`.
- When speech is present, compare it against the approved, versioned transcript.
- A word, sentence, language, or ordering mismatch blocks narration approval.
- Ambient-only audio may be approved as scene ambience or placeholder audio,
  but it does not complete the AI-narration requirement.
- Mixed audio may replace narration only after transcript match, accessibility,
  volume balance, and human-review gates pass.
- Existing transcripts must remain available independently of the audio.

## Scope

### In scope

- validating the four named MP3 files in `asset/audio/`;
- deterministic scene mapping;
- file hashes and technical inspection;
- narration/ambient/mixed classification;
- transcript comparison when speech exists;
- complete human listening review;
- a generated/supplied-audio manifest;
- minimal scene/player mapping changes for approved tracks;
- fallback, accessibility, playback, build, and offline/PWA tests;
- evidence and append-only project-log updates.

### Out of scope

- any TTS or audio-generation provider call;
- API keys, provider configuration, or runtime AI;
- script or transcript rewriting;
- destructive audio processing;
- deleting or overwriting existing/student-recorded audio;
- autoplay;
- visual redesign or unrelated refactoring;
- S18 or any later baseline-session work;
- claiming placeholder or ambient audio is completed narration.

## Implementation Sequence

1. Create `evidence/OA01/` if needed. Preserve any earlier OA01 evidence.
2. Inventory exactly the four expected MP3 files. Reject symlinks, unexpected
   formats, duplicate scene mappings, or extra executable content.
3. Compute SHA-256 hashes without modifying the files. Save them to:

   ```text
   evidence/OA01/checksums.sha256
   ```

4. Inspect and record, where supported by installed tools:

   - container and codec;
   - duration;
   - sample rate;
   - channels;
   - bitrate;
   - file size;
   - corrupt frames or decode errors;
   - peak level, integrated loudness, and clipping risk;
   - long leading, internal, or trailing silence;
   - embedded metadata.

   Record actual results only. Do not fabricate unavailable measurements.

5. Listen to every track from beginning to end using headphones and ordinary
   speakers. Record:

   - whether speech is present;
   - pronunciation and transcript match when applicable;
   - warmth, pacing, clarity, and intelligibility;
   - loudness balance and intrusive artifacts;
   - abrupt starts, startling transitions, and ending behavior;
   - suitability for the named scene;
   - reviewer decision: `approved`, `rejected`, or `needs revision`.

6. Apply the classification gate and record one role per track: `narration`,
   `ambient`, or `mixed`.
7. Create or update:

   ```text
   asset/audio/audio-manifest.placeholder.json
   ```

   Reuse the repository's existing manifest schema if one exists. Otherwise,
   include at least:

   - scene ID;
   - source path relative to the project root;
   - public/runtime path actually used by the application;
   - audio role;
   - source label: `user-supplied-placeholder`;
   - SHA-256 hash;
   - duration and technical format;
   - transcript version and match status, when applicable;
   - human-review status;
   - non-identifying reviewer-role placeholder;
   - approval-date placeholder;
   - provenance/licensing status;
   - fallback asset or behavior.

8. Keep the four supplied MP3s at their exact paths. Do not create replacement
   audio copies merely to rename or reorganize them.
9. Inspect how this project serves static assets. If `asset/audio/` is already
   deployable, map approved files through the existing asset resolver. If it is
   not deployable, stop and report the minimal architectural correction before
   relocating or duplicating any source file.
10. Update scene/player mappings only for tracks that passed their applicable
    gates:

    - ambient files use ambient controls and do not replace narration;
    - narration files retain transcript controls and missing-audio fallback;
    - mixed files preserve transcript access and independent volume behavior
      where supported by the approved architecture.

11. Keep playback user-initiated. Audio failure must never block navigation,
    exit, transcript access, or support information.
12. Add or update focused tests for:

    - all four scene-to-file mappings;
    - manifest schema and role values;
    - missing/corrupt-file fallback;
    - narration versus ambient control behavior;
    - transcript availability;
    - offline/PWA availability according to the existing caching strategy.

13. Run the focused tests, existing regression suite, and production build.
14. Save actual outputs under `evidence/OA01/`.
15. Update `OPTIONAL_EXTENSIONS.md`, `TASKS.md`, `docs/DecisionLog.md`, and
    `docs/CoBuildLog.md` append-only and truthfully. Preserve all `S01–S22`
    checklist entries and history.
16. Stop after the OA01 acceptance decision. Do not activate or implement S18.

## Required Evidence

Save at minimum:

```text
evidence/OA01/source-inventory.txt
evidence/OA01/checksums.sha256
evidence/OA01/audio-technical-report.md
evidence/OA01/content-classification.md
evidence/OA01/transcript-match-report.md
evidence/OA01/human-review-checklist.md
evidence/OA01/manifest-validation.txt
evidence/OA01/test-and-build-results.txt
evidence/OA01/offline-playback-check.md
evidence/OA01/integration-and-rollback.md
```

Evidence must contain actual commands, exit status, expected result, actual
result, reviewer decision, and relevant paths. Do not invent test or listening
results.

Do not store secrets, personal names, private wellbeing information, or
unredacted identifying metadata.

## Acceptance Criteria

OA01 passes only when all applicable conditions are true:

- `S17` is accepted and `S18` has not begun.
- Exactly four expected MP3 files exist under `asset/audio/`.
- Every file decodes successfully and has a recorded SHA-256 hash.
- Technical inspection reports actual format and quality findings.
- Every track has one truthful role: `narration`, `ambient`, or `mixed`.
- Every track has a completed human-review decision.
- Any speech selected as narration matches the approved transcript exactly.
- `asset/audio/audio-manifest.placeholder.json` validates.
- Only approved tracks are selected in scene/player mappings.
- Existing/student-recorded audio remains present and recoverable.
- Transcripts and missing-audio fallback remain usable.
- Playback is user-initiated; no autoplay is introduced.
- Focused tests, regression tests, and production build pass, or failures remain
  explicitly release-blocking.
- Required offline behavior is verified under the current PWA caching strategy.
- No provider call, API key, runtime TTS, secret, or unrelated feature is added.
- The rollback path to the pre-OA01 mapping is documented and tested safely.

If the files are ambient-only, OA01 may finish with the truthful status:

```text
placeholder scene audio integrated; AI narration not completed
```

Do not mark AI-generated narration complete in that case.

## Student/Teacher Manual Gate

The student and teacher/mentor must:

1. listen to all four complete files;
2. confirm the scene mapping;
3. confirm the classification of each track;
4. follow the approved transcript while listening whenever speech is present;
5. record timestamped problems;
6. approve or reject each file;
7. verify one missing-audio fallback;
8. approve the final release mapping and rollback path.

The coding agent may prepare the review materials, but it must not invent or
make the human approval decision.

## TASKS.md Optional Activation

Do not replace or regenerate `TASKS.md`.

When OA01 is explicitly started after S17:

1. Preserve the complete `S01–S22` checklist and all prior history.
2. Add OA01 once under an optional-extension section if it is not already
   present.
3. Set only the active-unit fields to:

   ```text
   Unit code: OA01
   Unit focus: Supplied audio validation and integration after S17
   Current prompt: PauseSpace_OA01_After_S17_Supplied_Audio_Prompt.md
   ```

4. Do not mark OA01 complete until every applicable acceptance criterion passes.
5. After OA01 is accepted, set `S18` as preparation only. Do not implement it.

## Checkpoint and Rollback

Record the pre-OA01 commit ID. Keep the mapping change small and reversible.

If any gate fails:

- keep the last runnable S17 state;
- leave failed tracks unselected;
- preserve the supplied MP3s and all evidence;
- restore the previous audio mapping without deleting assets;
- keep OA01 incomplete or record its limited placeholder-only outcome;
- report the exact non-destructive recovery path;
- do not advance to S18.

Create a post-OA01 checkpoint only after human acceptance and all required tests
pass.

## Completion Report

Report:

- pre/post checkpoint IDs;
- files created, modified, and explicitly preserved;
- each scene's file path, hash, duration, role, transcript-match status, and
  human-review status;
- exact test/build commands and actual outcomes;
- active release mapping and fallback behavior;
- offline/PWA result;
- rollback instructions;
- limitations, rejected files, and unresolved risks;
- whether the result is narration, ambience, mixed audio, or placeholder-only;
- `S18` as the next safe unit, without starting it.

## Stop Condition

Stop when OA01 is accepted and evidence is saved, or when a prerequisite,
content, quality, transcript, provenance, licensing, accessibility, test, or
offline-playback blocker is found. Do not begin S18.
