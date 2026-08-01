# TASKS.md - PauseSpace

## Project Goal
Build PauseSpace as a privacy-first, static, scene-based attention-reset Web App, aligned to the approved 22-session course plan.

## Global Rules
- Preserve the four approved scenes and the five-view product structure.
- No account, backend, database, analytics, mood score, microphone capture, runtime AI counselling, streak, or ranking.
- Do not present PauseSpace as diagnosis, treatment, counselling, or emergency support.
- Use only synthetic or properly anonymized research data.
- All final scripts, recordings, support wording, and public claims require student revision and mentor/adult review.
- No secrets, credentials, private research notes, or identifying participant data in Git.
- Do not implement a future session before the current session passes acceptance.

## Current Unit
Unit code: S07
Unit focus: Content review & recording plan
Current prompt:

```markdown
# S07 - Content review & recording plan

## Role
Act as the implementation partner for this bounded PauseSpace InnovationLab session. Preserve student ownership and the approved static, privacy-first architecture.

## Read First
Open README.md, TASKS.md, docs/ProjectPlan.md, docs/Architecture.md, docs/DecisionLog.md, the listed in-scope files, and current tests. Inspect before proposing changes.

## Current State
Confirm the repository checkpoint and report what already works, failing tests, known issues, and active task S07 / P2. Do not assume missing work is complete.

## Session Objective
Run adult review, revision log, audio setup, naming and licensing checks.

## Scope
In scope: docs/ContentReview.md; assets/audio/README.md. Make only changes required for “Content review & recording plan”. Preserve all working behavior outside this boundary.

## Requirements
Resolve every content-review comment; freeze approved script versions; define quiet recording setup, filenames, levels, retake log, transcript match, and license evidence. Keep the four authoritative scenes and the approved static, local-first, non-diagnostic boundary; use synthetic or properly anonymized data only.

## Implementation Sequence
1) Verify baseline and tests. 2) Create a checkpoint. 3) State the smallest runnable change. 4) Implement in small steps. 5) Run focused tests after each step. 6) Run the session acceptance checks. 7) Update TASKS, Decision Log and Co-build Log.

## Files
Create or modify only: docs/ContentReview.md; assets/audio/README.md. Explicitly preserve deployed assets, approved scripts, unrelated styles, test evidence and prior decisions.

## Tests and Acceptance Criteria
Acceptance gate: All four scripts approved before recording. Require adult approval for all four scripts; verify filenames and transcript version IDs; save a short test recording and review record. Report exact commands, expected versus actual results, manual checks, and evidence paths. Never invent passing results.

## Evidence to Save
Save dated evidence under evidence/S07/: relevant screenshots or recordings, command/test output, reviewed artifacts, defect references, and the pre/post-session checkpoint IDs. Do not save personal or identifying data.

## Student Manual Work
Student records the test sample, listens on phone and headphones, and decides whether the setup is acceptable. The student must review every diff and write the final Co-build Log decision in their own words.

## Security and Safety
Do not collect names, mental-health histories, family details, mood scores, microphone data, analytics identifiers, or secrets. Do not add diagnosis, treatment, emergency promises, forced breathing, autoplay, or unreviewed support contacts.

## Do Not Do
Do not add frameworks, backend, login, AI runtime chat, cloud sync, trackers, streaks, rankings, unrelated refactors, hidden scope, hard-coded secrets, copied imagery, or the next session’s work.

## TASKS.md Session Activation
Before implementation, update only the editable fields in `TASKS.md`:
- `Unit code: S07`
- `Unit focus: Content review & recording plan`
- `Current prompt: paste this complete S07 prompt only`
- Replace the three placeholder acceptance lines with this session's observable acceptance criteria.

Do not recreate or overwrite `TASKS.md`. Preserve the full S01-S22 checklist, completed checkmarks, known issues, and last test evidence. After acceptance passes, mark only S07 complete, record actual evidence, and set the next unit only as preparation.

## Checkpoint and Rollback
Record the pre-session checkpoint identifier. If acceptance fails, keep the last runnable state, log the defect, and provide the exact rollback path without erasing evidence.

## Completion Report
List changed files; summarize decisions; show tests and manual checks; identify limitations and unresolved risks; update traceability; name the next safe step without implementing it.

## Stop Condition
Stop when S07 acceptance criteria pass and evidence is saved. Do not begin the next session.
```

## Acceptance Criteria for Current Unit
- A1 — Content review record: `docs/ContentReview.md` holds a review record for all four scripts (script version ID, transcript version ID, rubric result, resolved comments, adult-approval status) plus filename/version conventions and a frozen-version rule. (Auto-verifiable structure; adult approval itself is the manual gate.)
- A2 — Recording plan + conventions: `assets/audio/README.md` defines quiet setup, filename convention, levels, retake log, transcript-match, and license/origin evidence; each scene's `audio.src` matches the filename convention. (Auto-verifiable.)
- A3 — Adult approval + test recording: adult approval of all four scripts and a saved short test recording (student records, listens on phone + headphones) are student/adult-owned manual gates — scripts stay `review.status=draft` and recording stays pending until then. Pre/post checkpoint IDs and check output saved under `evidence/S07/`. (Manual, student-owned gate.)

## Completed Units
- [x] S01
- [x] S02
- [x] S03
- [x] S04
- [x] S05
- [x] S06
- [ ] S07
- [ ] S08
- [ ] S09
- [ ] S10
- [ ] S11
- [ ] S12
- [ ] S13
- [ ] S14
- [ ] S15
- [ ] S16
- [ ] S17
- [ ] S18
- [ ] S19
- [ ] S20
- [ ] S21
- [ ] S22

## Known Issues
- Deployment host; owner: student and mentor; next action: decide before S21.
- Locally approved support contacts; owner: mentor/adult reviewer; next action: approve before S15 release gate.

## Last Test Evidence
- Automated (S07): `evidence/S07/review-checks.txt` — 11/11 PASS (validator `evidence/S07/validate_review.py`, exit 0). Covers ContentReview has all four review records (script + transcript version IDs, rubric, adult-approval PENDING, frozen rule), audio README covers setup/filenames/levels/retake/transcript/license, each scene `audio.src` matches `assets/audio/<scene-id>.mp3`, rubric re-check clean on all four, and S01-S06 regression (git diff vs `d9762c6` = no change).
- Automated (preserved): S06 22/22; S05 12/12; S04 10/10; S03 14/14; S02 14/14; S01 12/12.
- Content/data validation (S07): new docs non-empty; independent email/secret/token scan of S07 docs is clean.
- Accessibility/device: Not applicable to S07 (review + recording plan, no UI). Deferred to B-11 / later sessions.
- Manual demo path: Not applicable to S07 (no app to demo). **Manual gate (A3) OPEN** — an adult must approve all four scripts and the student must record a short test sample and listen on phone + headphones; scripts stay `review.status=draft` and recording stays pending until then.
