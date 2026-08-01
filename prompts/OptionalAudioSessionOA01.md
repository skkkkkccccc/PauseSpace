# OA01 - Optional AI-Generated Narration Production and Curation

## Role
Act as the implementation and audio-production partner for this optional, bounded PauseSpace extension. Preserve student authorship of the approved scripts, the static privacy-first architecture, and the complete S01-S22 baseline.

## Read First
Read these files completely before proposing changes:
- `README.md`
- `TASKS.md`
- `OPTIONAL_EXTENSIONS.md`
- `docs/ProjectPlan.md`
- `docs/Architecture.md`
- `docs/ContentReview.md`
- `docs/DecisionLog.md`
- `docs/CoBuildLog.md`
- `docs/OptionalAIAudioExtension.md`
- `prompts/GlobalEngineeringContract.md`
- the four approved scene-content JSON files
- the current package manifest, dependency manifest, test configuration, and audio asset documentation

Inspect the actual repository first. Do not assume that a provider, model, voice, package manager, audio tool, or file path exists.

## Current State and Prerequisite Gate
Confirm and report:
1. S07 and S12 are complete and their evidence exists.
2. All four narration scripts have stable version IDs, exact transcript text, timed read-aloud evidence, student approval, and mentor/adult approval.
3. The Git working tree is clean or every existing change is truthfully documented.
4. The pre-extension checkpoint commit ID is recorded.
5. No prior approved or student-recorded audio will be deleted or overwritten.

If any prerequisite is missing, stop and report the blocker. Do not generate audio.

## Session Objective
Create four reviewable AI-generated narration tracks from the exact approved PauseSpace scripts during development, curate them through human review, bundle only approved MP3 assets locally, and leave the deployed site free of runtime AI calls and secrets.

This is an optional enhancement. It does not renumber S01-S22, change the 22-core-session total, replace the baseline traceability ledger, or silently redefine the original recording requirement.

## Required Provider Decision
Before implementation, ask the student/teacher to approve exactly one TTS provider, model, voice, language/locale, and expected cost boundary. Record:
- official provider and API/SDK documentation used;
- model and voice identifiers exactly as configured;
- whether script text is transmitted to a remote service;
- retention/data-use settings that can be verified;
- redistribution and showcase rights for generated audio;
- expected cost and a hard per-run spending limit;
- pronunciation policy for names, acronyms, numbers, and bilingual text.

Do not choose a provider, model, or voice silently. If licensing, retention, price, or redistribution rights are unclear, stop before generation.

## Scope
In scope:
- a development-only TTS generation command;
- one approved provider adapter;
- placeholder-only configuration documentation;
- deterministic input selection from the four approved scripts;
- script-version hashing and generation provenance;
- one-track preview before batch continuation;
- human review, regeneration, and approval records;
- four locally bundled MP3 files under a generated-audio directory;
- an explicit, reversible release-audio mapping after approval;
- focused audio validation and existing regression checks.

Out of scope:
- runtime TTS or runtime calls from the browser;
- automatic script rewriting;
- voice cloning, impersonation, or biometric voice samples;
- collecting microphone recordings from users;
- personalized narration based on mood or mental-health data;
- background music or ambient-sound generation;
- deleting or overwriting original/student-recorded audio;
- changing S01-S22 titles, completion history, or baseline requirements.

## Files
Create only when required by the inspected repository:
- `scripts/generate-audio.mjs`
- `scripts/lib/tts-provider.mjs`
- `tests/audio-generation.test.mjs`
- `assets/audio/generated/`
- `assets/audio/audio-manifest.generated.json`
- `docs/AudioGenerationRecord.md`
- `.env.audio.example` or the repository's approved placeholder-only equivalent

Modify only when necessary:
- `package.json` or the actual dependency manifest, adding bounded audio commands;
- the four scene-content files, but only to apply an explicitly approved and reversible generated-audio mapping;
- `TASKS.md`, `OPTIONAL_EXTENSIONS.md`, `docs/DecisionLog.md`, and `docs/CoBuildLog.md`.

Explicitly preserve:
- all existing S01-S22 prompt files and checklist entries;
- prior audio assets and their metadata;
- approved transcript wording and version IDs;
- unrelated source, styles, tests, evidence, and deployment settings.

## Implementation Requirements
1. Accept provider credentials only through an ignored local environment file or the provider's official secure credential mechanism. Never pass a key as a command-line argument.
2. Keep provider configuration outside browser-delivered source. The production build must contain no key, TTS SDK, secret endpoint wrapper, or runtime generation path.
3. Read only the four approved script fields. Refuse draft, unapproved, missing-version, or transcript-mismatched content.
4. Compute and record a SHA-256 hash for each exact source transcript before generation.
5. Provide a dry-run that reports scene ID, script version, input hash, planned provider/model/voice, output path, and estimated request count without contacting the provider.
6. Generate only one preview track first. Do not batch the remaining tracks until the student and mentor/adult reviewer approve the preview.
7. Use stable, non-identifying filenames such as `exam-room.v1.ai.mp3`; never put credentials, names, prompts, or timestamps containing personal data in filenames.
8. Generate the other three tracks one at a time. Apply bounded retries and stop on provider, quota, content, or file-validation errors; never create an uncontrolled retry loop.
9. Preserve the exact approved wording. If pronunciation requires text changes, return to the content-review decision process and create a new script version before regeneration.
10. Record provider, model, voice, locale, source version/hash, generation date, output hash, duration, file size, license/provenance reference, review status, and non-identifying reviewer roles for every track.
11. Keep generated tracks separate from original/student-recorded tracks. Do not overwrite current files.
12. After all four tracks pass human review, apply one explicit release-audio mapping to same-origin relative MP3 paths. Preserve the previous mapping in the checkpoint history and document how to switch back.
13. Ensure transcripts remain available independently of audio and that audio failure never blocks exit, navigation, or support information.
14. Add a visible project-level disclosure that narration was AI-generated and student-curated if generated tracks are selected for release.

## Implementation Sequence
1. Inspect the repository, tests, content status, audio documentation, and current mappings.
2. Record the checkpoint and provider decision; stop if any prerequisite or rights question is unresolved.
3. Add placeholder-only configuration and a dry-run path.
4. Add one provider adapter with minimal dependencies and focused tests.
5. Run the dry-run for all four scenes and inspect the planned requests.
6. Generate only the `exam-room` preview.
7. Student and mentor/adult reviewer evaluate the preview and record pass/fail evidence.
8. If approved, generate the remaining tracks individually; otherwise revise settings and regenerate only the failed preview.
9. Validate files and metadata; perform human review of every track.
10. Apply the reversible release mapping only after all four tracks pass.
11. Run focused and existing regression checks.
12. Update extension state, logs, evidence, and the completion report; stop before S13 or the next unfinished baseline session.

Keep the project runnable after every step.

## Commands and Checks
Adapt commands to the inspected package manager and repository, but provide equivalent scripts with these stable intentions:
- `npm run audio:dry-run`
- `npm run audio:generate -- --scene exam-room --preview`
- `npm run audio:generate -- --scene sports-field`
- `npm run audio:generate -- --scene own-room`
- `npm run audio:generate -- --scene empty-classroom`
- `npm run test:audio`
- `npm test`
- `npm run build`

Do not claim these commands exist before creating and testing them. Report every exact command, exit status, expected result, actual result, and evidence path.

## Tests and Acceptance Criteria
OA01 passes only when all of the following are true:
- S07 and S12 prerequisites are verified.
- The provider/model/voice/cost/licensing/data-handling decision is approved and recorded.
- Dry-run mode makes zero provider requests and exposes no secret.
- Generation refuses draft or transcript-hash-mismatched input.
- A single preview gate occurs before the remaining three requests.
- Four non-empty MP3 files exist under the generated-audio directory and each opens successfully.
- Duration, file size, output hash, and exact transcript hash are recorded for every track.
- Student and mentor/adult review each track for transcript match, pronunciation, pacing, warmth, pauses, volume consistency, clipping/noise, duration, and non-diagnostic safety language.
- Every released track has `reviewStatus: approved`; failed variants remain documented but are not selected for release.
- The release mapping uses same-origin relative files and can be reverted without deleting assets.
- No provider key or secret appears in Git status, diff, logs, screenshots, source maps, build output, or MP3 metadata.
- Existing automated tests and the production build pass.
- The built site performs no runtime request to the TTS provider.
- Transcript-only and missing-audio behavior remain usable.
- AI-generated narration is disclosed accurately if selected for release.

Save evidence under `evidence/OA01/`, including:
- pre/post checkpoint IDs;
- provider-decision and rights review;
- redacted dry-run and generation logs;
- input and output hashes;
- audio validation report;
- four human-review records;
- release-mapping diff;
- test/build results;
- a runtime network-panel screenshot or equivalent proof showing no TTS request.

Do not store API keys, full provider responses containing secrets, personal names, biometric samples, private research notes, or identifying reviewer data.

## Student Manual Work
The student must:
1. approve the provider, model, voice, locale, and cost cap;
2. listen to the preview on phone speaker and headphones before any remaining generation;
3. listen to all four complete tracks while following the approved transcripts;
4. mark exact timestamps for every pronunciation, pacing, tone, volume, or wording problem;
5. decide which variants are accepted and explain why in the Co-build Log;
6. verify the release mapping and personally test one missing-audio fallback;
7. write the AI-generated-audio disclosure in their own words.

The coding agent may assist, but it must not make the final voice, safety, or release decision.

## Security, Privacy, Safety, and Licensing
- Never expose or commit provider credentials.
- Send only approved narration text; send no participant, user, wellbeing, account, or research data.
- Do not clone or imitate a real person's voice.
- Do not generate diagnostic, treatment, emergency, coercive-breathing, or guaranteed-outcome language.
- Keep play user-initiated; no autoplay.
- Confirm the selected provider and voice permit the intended educational demo, public showcase, and redistribution.
- Preserve an offline transcript and deterministic audio-failure fallback.
- Record uncertainty honestly; do not fabricate review or generation results.

## Do Not Do
- Do not renumber, rewrite, delete, or mark complete any S01-S22 unit.
- Do not count OA01 inside the approved 22 core hours or 27-hour baseline.
- Do not overwrite original/student-recorded audio.
- Do not silently switch the release mapping.
- Do not add a backend, account system, analytics, runtime AI, cloud sync, mood score, tracker, streak, ranking, or unrelated refactor.
- Do not use a guessed API, model, voice, license, price, or retention claim.
- Do not run all four generation requests before preview approval.
- Do not suppress failed audio, content, build, or security checks.
- Do not begin S13 or another baseline unit.

## TASKS.md Optional Activation
The packaged baseline `TASKS.md` must remain unchanged until OA01 is explicitly selected.

When selected after S12:
1. Append once, without deleting or rewriting history:
   `## Optional Extension Units`
   `- [ ] OA01 - AI-generated narration production and curation`
2. Set:
   `Unit code: OA01`
   `Unit focus: Optional AI-generated narration production and curation`
   `Current prompt: prompts/OptionalAudioSessionOA01.md`
3. Replace only the current-unit acceptance criteria with the OA01 criteria.
4. Preserve the complete S01-S22 checklist, completed checks, known issues, decisions, and test evidence.

After OA01 passes, mark only OA01 complete, record actual evidence, and restore the next unfinished baseline unit as preparation only. If OA01 fails, keep it active and do not advance.

## Checkpoint and Rollback
Record the pre-OA01 checkpoint. Keep every generated asset under a separate directory and make the release mapping a small reversible diff. If any acceptance criterion fails:
- retain the last runnable baseline state;
- deselect generated audio from the release mapping;
- preserve logs and failed review evidence;
- report the exact non-destructive recovery path;
- do not delete original audio or rewrite checkpoint history.

## Completion Report
Report:
- provider/model/voice decision and verified rights boundary;
- files created, modified, and explicitly preserved;
- generation request count and redacted cost result;
- exact test commands and actual outcomes;
- each track's input hash, output hash, duration, and review status;
- secret-scan and runtime-network results;
- release mapping and rollback path;
- limitations, failed variants, and unresolved risks;
- the next unfinished baseline unit, without implementing it.

## Stop Condition
Stop when OA01 passes and evidence is saved, or when a prerequisite, provider, rights, cost, safety, or secret-management blocker is found. Do not begin S13 or any other baseline unit.
