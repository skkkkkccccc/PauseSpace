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
Unit code: S02
Unit focus: Ethical peer research
Current prompt:

```markdown
# S02 - Ethical peer research

## Role
Act as the implementation partner for this bounded PauseSpace InnovationLab session. Preserve student ownership and the approved static, privacy-first architecture.

## Read First
Open README.md, TASKS.md, docs/ProjectPlan.md, docs/Architecture.md, docs/DecisionLog.md, the listed in-scope files, and current tests. Inspect before proposing changes.

## Current State
Confirm the repository checkpoint and report what already works, failing tests, known issues, and active task S02 / P1. Do not assume missing work is complete.

## Session Objective
Prepare consent-aware interview prompts and synthetic note template.

## Scope
In scope: docs/ResearchProtocol.md; data/sample/interview-notes.json. Make only changes required for “Ethical peer research”. Preserve all working behavior outside this boundary.

## Requirements
Draft assent/consent language, voluntary participation and stop rules; write neutral task questions; provide a synthetic note schema that excludes names and psychological histories. Keep the four authoritative scenes and the approved static, local-first, non-diagnostic boundary; use synthetic or properly anonymized data only.

## Implementation Sequence
1) Verify baseline and tests. 2) Create a checkpoint. 3) State the smallest runnable change. 4) Implement in small steps. 5) Run focused tests after each step. 6) Run the session acceptance checks. 7) Update TASKS, Decision Log and Co-build Log.

## Files
Create or modify only: docs/ResearchProtocol.md; data/sample/interview-notes.json. Explicitly preserve deployed assets, approved scripts, unrelated styles, test evidence and prior decisions.

## Tests and Acceptance Criteria
Acceptance gate: Questions avoid diagnosis and collecting personal histories. Review every question against the data-minimization checklist; validate the synthetic JSON sample; save the reviewed protocol and blank note template. Report exact commands, expected versus actual results, manual checks, and evidence paths. Never invent passing results.

## Evidence to Save
Save dated evidence under evidence/S02/: relevant screenshots or recordings, command/test output, reviewed artifacts, defect references, and the pre/post-session checkpoint IDs. Do not save personal or identifying data.

## Student Manual Work
Student role-plays interviewer and participant, then rewrites any leading or intrusive question. The student must review every diff and write the final Co-build Log decision in their own words.

## Security and Safety
Do not collect names, mental-health histories, family details, mood scores, microphone data, analytics identifiers, or secrets. Do not add diagnosis, treatment, emergency promises, forced breathing, autoplay, or unreviewed support contacts.

## Do Not Do
Do not add frameworks, backend, login, AI runtime chat, cloud sync, trackers, streaks, rankings, unrelated refactors, hidden scope, hard-coded secrets, copied imagery, or the next session’s work.

## TASKS.md Session Activation
Before implementation, update only the editable fields in `TASKS.md`:
- `Unit code: S02`
- `Unit focus: Ethical peer research`
- `Current prompt: paste this complete S02 prompt only`
- Replace the three placeholder acceptance lines with this session's observable acceptance criteria.

Do not recreate or overwrite `TASKS.md`. Preserve the full S01-S22 checklist, completed checkmarks, known issues, and last test evidence. After acceptance passes, mark only S02 complete, record actual evidence, and set the next unit only as preparation.

## Checkpoint and Rollback
Record the pre-session checkpoint identifier. If acceptance fails, keep the last runnable state, log the defect, and provide the exact rollback path without erasing evidence.

## Completion Report
List changed files; summarize decisions; show tests and manual checks; identify limitations and unresolved risks; update traceability; name the next safe step without implementing it.

## Stop Condition
Stop when S02 acceptance criteria pass and evidence is saved. Do not begin the next session.
```

## Acceptance Criteria for Current Unit
- A1 — Neutral questions: every question in the “Task questions” section of `docs/ResearchProtocol.md` avoids diagnosis and personal/psychological histories; an automated scan of that section finds no clinical/diagnostic or identifying terms. (Auto-verifiable.)
- A2 — Data minimization: `docs/ResearchProtocol.md` includes assent/consent, voluntary participation, and an explicit stop rule, and its data-minimization checklist enumerates every forbidden data category; `data/sample/interview-notes.json` is valid JSON and contains no names, contact details, or psychological/clinical data. (Auto-verifiable.)
- A3 — Evidence + review: pre/post-session checkpoint IDs and check output saved under `evidence/S02/`; the protocol is marked “reviewed” only after the student role-plays interviewer and participant and rewrites any leading or intrusive question. (Manual, student-owned gate.)

## Completed Units
- [x] S01
- [ ] S02
- [ ] S03
- [ ] S04
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
- Automated (S02): `evidence/S02/research-checks.txt` — 14/14 PASS (validator `evidence/S02/validate_research.py`, exit 0). Covers JSON validity + required schema fields, no forbidden identifying/clinical keys, no forbidden terms/PII in values, protocol sections present, neutral task questions, data-minimization checklist completeness, and S01-baseline regression (git diff vs `3e8ef01` = no change).
- Automated (S01, preserved): `evidence/S01/baseline-checks.txt` — 12/12 PASS.
- Content/data validation (S02): `data/sample/interview-notes.json` is valid JSON with `synthetic=true`; independent email/secret/token scan of S02 files is clean.
- Accessibility/device: Not applicable to S02 (documentation-only session, no UI). Deferred to B-11 / later sessions.
- Manual demo path: Not applicable to S02 (no app to demo). **Manual review gate (A3) is OPEN** — protocol is "draft, pending student role-play and rewrite of any leading or intrusive question."
