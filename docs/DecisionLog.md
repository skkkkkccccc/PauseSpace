# Decision Log

| Date | Decision | Alternatives | Evidence | Owner |
|---|---|---|---|---|
| 2026-07-28 | Freeze v1 baseline as requirements B-01–B-14 in `docs/Traceability.md`, paired with the locked proposal ledger in `docs/ProjectPlan.md` | Keep scope implicit across scattered docs only; or use a different requirement-ID scheme | `docs/Traceability.md`; `evidence/S01/baseline-checks.txt` (12/12 PASS) | Student (pending approval) |
| 2026-07-28 | Classify the PWA/offline shell as **Recommended (optional)**, not Mandatory; keep deterministic player state as Mandatory | Make PWA Mandatory; or cut offline support entirely | `docs/Traceability.md` B-12 | Student (pending) |
| 2026-07-28 | Leave the S01 checkbox unchecked; baseline status = "frozen, pending student approval" until the student personally signs off every non-goal | Auto-mark S01 complete once the technical checks pass | S01 prompt §Student Manual Work; `TASKS.md` | Student |
| 2026-07-28 | Do **not** commit S01 artifacts; leave them as uncommitted working-tree changes for student review and the student's own commit | Commit immediately on technical pass | Repo guardrail (commit only when asked); `evidence/S01/checkpoint-post.txt` | AI proposed / Student decides |
