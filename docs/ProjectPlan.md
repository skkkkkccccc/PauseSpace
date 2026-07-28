# Project Plan

> **Status: LOCKED — S01 Baseline freeze (2026-07-28).**
> This is the AI implementation partner's proposed freeze of the student
> PauseSpace proposal. It is **pending the student's line-by-line approval** of
> every element and non-goal. After approval, any change requires a
> `docs/DecisionLog.md` entry and student sign-off. The detailed
> requirement-to-evidence mapping (B-01–B-14) lives in `docs/Traceability.md`.

Authoritative source: student PauseSpace proposal. Preserve four scenes, anonymous use, local-only progress, original audio/visuals, AI Co-build Log, six-week delivery, poster, and two-minute video.

## 1. Product one-liner
A mobile-first, static, privacy-first Web App delivering four roughly
three-minute, scene-based attention-reset experiences for high-school students.
It is not diagnosis, treatment, counselling, or emergency support.

## 2. Locked proposal elements (preserve)
1. **Four scenes** — four approved, ~3-minute, scene-based attention-reset
   experiences (one per scene). [B-01]
2. **Anonymous use** — no account, login, or identity collection. [B-04]
3. **Local-only progress** — validated localStorage; no cloud sync. [B-05]
4. **Original audio/visuals** — same-origin MP3 and original imagery, properly
   licensed. [B-07, B-08]
5. **AI Co-build Log** — maintained across every session. [B-14]
6. **Six-week delivery** — the 22-session plan (S01–S22). [B-14]
7. **Poster** — required course deliverable. [B-14]
8. **Two-minute video** — required course deliverable. [B-14]

Supporting locked facts: static HTML/CSS/JS with no backend/database [B-02]; the
five-view product structure [B-03]; deterministic player state [B-12]; the
non-diagnostic boundary [B-09]; age-appropriate, mentor-approved support contacts
[B-10]; the accessibility baseline [B-11]; and full test-plan coverage [B-13].

## 3. Non-goals (explicitly out-of-scope for v1)
- No account, login, or identity collection.
- No backend, database, or cloud sync.
- No analytics, trackers, mood scores, streaks, or rankings.
- No microphone capture; no runtime AI counselling/chat.
- No diagnosis, treatment, counselling, or emergency-support claims.
- No forced breathing, autoplay, or unreviewed support contacts.
- No copied or unlicensed imagery/audio; no identifying participant data.
- No implementation of a future session before the current session passes acceptance.

## 4. Measurable success measures (summary)
- 4 scenes, each ~180 s, each with a transcript, same-origin audio, and an approved review status.
- The app loads and runs static / offline-capable on a mobile browser with zero backend or network egress.
- Exactly 5 student-approved views, all reachable and responsive.
- 100% original or properly licensed, same-origin assets with a complete manifest.
- All test-plan layers (unit, integration, E2E, accessibility, device/browser, privacy/security, offline, deployment smoke, rollback) have real pass evidence at release.
- The release checklist is fully checked; the poster, two-minute video, defense, and manifest are delivered; the Co-build Log is complete.

Full per-requirement measures and verification methods: `docs/Traceability.md`.

## 5. Unknowns / unresolved decisions (tracked, not blocking the S01 freeze)
- **Deployment host** — decide before S21 (owner: student + mentor). [TASKS Known Issues]
- **Locally approved support contacts** — approve before the S15 release gate (owner: mentor/adult reviewer). [TASKS Known Issues]
- **Five-view map** — the exact five views are not enumerated in the repo; the candidate set needs student confirmation against the proposal. [B-03]
- **PWA/offline shell** — recommended; including it in v1 or deferring is a student decision. [B-12]
- **Browser/device test matrix** — the local machine has Safari + Chrome only (Edge/Firefox absent); the matrix must be set. [B-13]
- **Audio production method** — the original-MP3 production/voice approach is decided in the content sessions. [B-07]

Full list with owners and status: `docs/Traceability.md` § Unresolved decisions.

## 6. Approval gate (manual, student-owned)
Per the S01 prompt, the student must compare this ledger line-by-line with the
proposal and personally approve every non-goal before the baseline is marked
"approved." Until that sign-off, the baseline is "frozen, pending student
approval."
