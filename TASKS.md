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
Unit code: S04
Unit focus: Content architecture
Current prompt:

```markdown
# S04 - Content architecture

## Role
Act as the implementation partner for this bounded PauseSpace InnovationLab session. Preserve student ownership and the approved static, privacy-first architecture.

## Read First
Open README.md, TASKS.md, docs/ProjectPlan.md, docs/Architecture.md, docs/DecisionLog.md, the listed in-scope files, and current tests. Inspect before proposing changes.

## Current State
Confirm the repository checkpoint and report what already works, failing tests, known issues, and active task S04 / P2. Do not assume missing work is complete.

## Session Objective
Define a reusable three-minute script structure and choice-language rubric.

## Scope
In scope: content/schema.json; docs/ContentRubric.md. Make only changes required for “Content architecture”. Preserve all working behavior outside this boundary.

## Requirements
Define ordered script segments, timing budget, optionality/exit fields, transcript/audio metadata, and review state; encode prohibited claims in the rubric. Keep the four authoritative scenes and the approved static, local-first, non-diagnostic boundary; use synthetic or properly anonymized data only.

## Implementation Sequence
1) Verify baseline and tests. 2) Create a checkpoint. 3) State the smallest runnable change. 4) Implement in small steps. 5) Run focused tests after each step. 6) Run the session acceptance checks. 7) Update TASKS, Decision Log and Co-build Log.

## Files
Create or modify only: content/schema.json; docs/ContentRubric.md. Explicitly preserve deployed assets, approved scripts, unrelated styles, test evidence and prior decisions.

## Tests and Acceptance Criteria
Acceptance gate: Schema validates; rubric blocks commands, promises, and judgments. Validate one synthetic scene against the schema; confirm invalid duration, missing exit language, and unapproved status fail safely. Report exact commands, expected versus actual results, manual checks, and evidence paths. Never invent passing results.

## Evidence to Save
Save dated evidence under evidence/S04/: relevant screenshots or recordings, command/test output, reviewed artifacts, defect references, and the pre/post-session checkpoint IDs. Do not save personal or identifying data.

## Student Manual Work
Student authors the rubric examples and explains why commands, promises, and judgments are rejected. The student must review every diff and write the final Co-build Log decision in their own words.

## Security and Safety
Do not collect names, mental-health histories, family details, mood scores, microphone data, analytics identifiers, or secrets. Do not add diagnosis, treatment, emergency promises, forced breathing, autoplay, or unreviewed support contacts.

## Do Not Do
Do not add frameworks, backend, login, AI runtime chat, cloud sync, trackers, streaks, rankings, unrelated refactors, hidden scope, hard-coded secrets, copied imagery, or the next session’s work.

## TASKS.md Session Activation
Before implementation, update only the editable fields in `TASKS.md`:
- `Unit code: S04`
- `Unit focus: Content architecture`
- `Current prompt: paste this complete S04 prompt only`
- Replace the three placeholder acceptance lines with this session's observable acceptance criteria.

Do not recreate or overwrite `TASKS.md`. Preserve the full S01-S22 checklist, completed checkmarks, known issues, and last test evidence. After acceptance passes, mark only S04 complete, record actual evidence, and set the next unit only as preparation.

## Checkpoint and Rollback
Record the pre-session checkpoint identifier. If acceptance fails, keep the last runnable state, log the defect, and provide the exact rollback path without erasing evidence.

## Completion Report
List changed files; summarize decisions; show tests and manual checks; identify limitations and unresolved risks; update traceability; name the next safe step without implementing it.

## Stop Condition
Stop when S04 acceptance criteria pass and evidence is saved. Do not begin the next session.
```

## Acceptance Criteria for Current Unit
- A1 — Schema validates a synthetic scene: `content/schema.json` is a parseable JSON Schema and one synthetic scene validates against it (structure + timing budget + required fields). (Auto-verifiable.)
- A2 — Safe failure on invalid input: scenes with invalid duration, missing exit language, or unapproved review status each fail validation safely (rejected without crashing). (Auto-verifiable.)
- A3 — Rubric + review: `docs/ContentRubric.md` encodes rules rejecting commands, promises, and judgments with accepted/rejected examples; pre/post checkpoint IDs and check output saved under `evidence/S04/`; the rubric examples are student-authored and a scene is “approved” only after student review. (Manual, student-owned gate.)

## Completed Units
- [x] S01
- [x] S02
- [x] S03
- [x] S04
- [ ] S05
- [ ] S06
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
- **Reprocessed 2026-07-30:** re-ran `evidence/S04/validate_content.py` on the staged S04 deliverables → 10/10 PASS (exit 0); independent JSON + PII scans clean; S03 still 14/14. No deliverable content changes. **S04 accepted and marked complete** (A3 satisfied: student confirmed the content rubric correct on 2026-07-30).
- Automated (S04): `evidence/S04/content-checks.txt` — 10/10 PASS (validator `evidence/S04/validate_content.py`, exit 0). Covers schema parseable as JSON Schema, synthetic scene validates (structure + timing budget + release-ready), invalid duration / missing exit language / unapproved status each fail safely, rubric covers command/promise/judgment, no PII/secrets, and S01-S03 regression (git diff vs `e869ba7` = no change).
- Automated (preserved): S03 `evidence/S03/findings-checks.txt` — 14/14; S02 `evidence/S02/research-checks.txt` — 14/14; S01 `evidence/S01/baseline-checks.txt` — 12/12.
- Content/data validation (S04): `content/schema.json` and `evidence/S04/sample-scene-valid.json` parse as valid JSON; independent email/secret/token scan of S04 deliverables is clean.
- Accessibility/device: Not applicable to S04 (schema + rubric only, no UI). Deferred to B-11 / later sessions.
- Manual demo path: Not applicable to S04 (no app to demo). **A3 satisfied (2026-07-30):** student reviewed and confirmed the content rubric is correct (blocks commands/promises/judgments with accepted/rejected examples). S04 marked complete.
