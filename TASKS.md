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
Unit code: S03
Unit focus: Scene evidence synthesis
Current prompt:

```markdown
# S03 - Scene evidence synthesis

## Role
Act as the implementation partner for this bounded PauseSpace InnovationLab session. Preserve student ownership and the approved static, privacy-first architecture.

## Read First
Open README.md, TASKS.md, docs/ProjectPlan.md, docs/Architecture.md, docs/DecisionLog.md, the listed in-scope files, and current tests. Inspect before proposing changes.

## Current State
Confirm the repository checkpoint and report what already works, failing tests, known issues, and active task S03 / P1. Do not assume missing work is complete.

## Session Objective
Cluster anonymized observations and justify the four launch scenes.

## Scope
In scope: docs/ResearchFindings.md; docs/DecisionLog.md. Make only changes required for “Scene evidence synthesis”. Preserve all working behavior outside this boundary.

## Requirements
Code anonymized observations without inventing frequency; build one evidence card per fixed scene; separate observation, inference, risk, and design response. Keep the four authoritative scenes and the approved static, local-first, non-diagnostic boundary; use synthetic or properly anonymized data only.

## Implementation Sequence
1) Verify baseline and tests. 2) Create a checkpoint. 3) State the smallest runnable change. 4) Implement in small steps. 5) Run focused tests after each step. 6) Run the session acceptance checks. 7) Update TASKS, Decision Log and Co-build Log.

## Files
Create or modify only: docs/ResearchFindings.md; docs/DecisionLog.md. Explicitly preserve deployed assets, approved scripts, unrelated styles, test evidence and prior decisions.

## Tests and Acceptance Criteria
Acceptance gate: Each scene has evidence, need, risk, and design response. Trace every scene claim to an anonymized note or mark it as an assumption; save clustering evidence and the scene decision record. Report exact commands, expected versus actual results, manual checks, and evidence paths. Never invent passing results.

## Evidence to Save
Save dated evidence under evidence/S03/: relevant screenshots or recordings, command/test output, reviewed artifacts, defect references, and the pre/post-session checkpoint IDs. Do not save personal or identifying data.

## Student Manual Work
Student performs the clustering, explains counter-evidence, and signs the four-scene decision. The student must review every diff and write the final Co-build Log decision in their own words.

## Security and Safety
Do not collect names, mental-health histories, family details, mood scores, microphone data, analytics identifiers, or secrets. Do not add diagnosis, treatment, emergency promises, forced breathing, autoplay, or unreviewed support contacts.

## Do Not Do
Do not add frameworks, backend, login, AI runtime chat, cloud sync, trackers, streaks, rankings, unrelated refactors, hidden scope, hard-coded secrets, copied imagery, or the next session’s work.

## TASKS.md Session Activation
Before implementation, update only the editable fields in `TASKS.md`:
- `Unit code: S03`
- `Unit focus: Scene evidence synthesis`
- `Current prompt: paste this complete S03 prompt only`
- Replace the three placeholder acceptance lines with this session's observable acceptance criteria.

Do not recreate or overwrite `TASKS.md`. Preserve the full S01-S22 checklist, completed checkmarks, known issues, and last test evidence. After acceptance passes, mark only S03 complete, record actual evidence, and set the next unit only as preparation.

## Checkpoint and Rollback
Record the pre-session checkpoint identifier. If acceptance fails, keep the last runnable state, log the defect, and provide the exact rollback path without erasing evidence.

## Completion Report
List changed files; summarize decisions; show tests and manual checks; identify limitations and unresolved risks; update traceability; name the next safe step without implementing it.

## Stop Condition
Stop when S03 acceptance criteria pass and evidence is saved. Do not begin the next session.
```

## Acceptance Criteria for Current Unit
- A1 — Four evidence cards: `docs/ResearchFindings.md` contains one evidence card per launch scene (4 total); each card has Need, Evidence, Inference, Risk, and Design response. (Auto-verifiable.)
- A2 — Traceability + no invented frequency: every scene claim traces to a coded anonymized observation (`O-xx`) or is explicitly marked `[assumption]`; the findings contain no invented frequencies (no percentages, fractions, or participant counts). (Auto-verifiable.)
- A3 — Decision record + sign-off: the four-scene decision is recorded in `docs/DecisionLog.md`; pre/post checkpoint IDs and check output saved under `evidence/S03/`; the decision is “signed” only after the student performs the clustering, explains counter-evidence, and signs the four-scene decision. (Manual, student-owned gate.)

## Completed Units
- [x] S01
- [x] S02
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
- Automated (S03): `evidence/S03/findings-checks.txt` — 14/14 PASS (validator `evidence/S03/validate_findings.py`, exit 0). Covers 4 scene cards (Need/Evidence/Inference/Risk/Design response), every claim traced to `O-xx` or `[assumption]`, no invented frequency, no clinical/PII data terms, scene decision record present, and S01+S02 regression (git diff vs `fb146e9` = no change).
- Automated (preserved): S02 `evidence/S02/research-checks.txt` — 14/14 PASS; S01 `evidence/S01/baseline-checks.txt` — 12/12 PASS.
- Content/data validation (S03): coded observations are anonymized; independent frequency and email/secret/token scans of `docs/ResearchFindings.md` are clean.
- Accessibility/device: Not applicable to S03 (documentation-only session, no UI). Deferred to B-11 / later sessions.
- Manual demo path: Not applicable to S03 (no app to demo). **Manual sign-off gate (A3) is OPEN** — four-scene decision is "pending student clustering, counter-evidence explanation, and sign-off"; scene themes are candidate assumptions (D8).
