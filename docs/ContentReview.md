# Content Review — PauseSpace scripts (S07)

> **Status: review record established; approvals PENDING.** The four scripts are
> still AI drafts (`review.status = draft`) pending the student rewrite + read
> aloud (S06 gate) **and** adult approval (S07 gate). **No script may be recorded
> until its row shows adult approval = approved.** PauseSpace is not diagnosis,
> treatment, counselling, or emergency support.

## Review policy
- **Adult approval is required for all four scripts before any recording.**
- The choice-language rubric (`docs/ContentRubric.md`) is applied to every script; a script is approvable only when the rubric scan is clean.
- On approval, the script version is **frozen**; any later wording change requires a new version ID and re-approval.
- No personal stories or identifying reviewer data are recorded (synthetic / anonymized only).

## Filename and version conventions
- **Scene IDs:** `exam-room`, `sports-field`, `own-room`, `empty-classroom`.
- **Script version ID:** `<scene-id>.v<N>` (for example `exam-room.v1`).
- **Transcript version ID:** must equal the script version ID (`<scene-id>.v<N>`).
- **Audio filename:** `assets/audio/<scene-id>.mp3` (matches each scene's `audio.src`).

## Per-script review record
| Scene | Script version | Transcript version | Rubric | Comments resolved | Adult approval |
|---|---|---|---|---|---|
| exam-room | exam-room.v1 | exam-room.v1 | pass (choice language) | none open — pending review | PENDING |
| sports-field | sports-field.v1 | sports-field.v1 | pass (choice language) | none open — pending review | PENDING |
| own-room | own-room.v1 | own-room.v1 | pass (choice language) | none open — pending review | PENDING |
| empty-classroom | empty-classroom.v1 | empty-classroom.v1 | pass (choice language; academic refs bounded/non-diagnostic) | none open — pending review | PENDING |

(Rubric "pass" = automated scan clean — see `evidence/S07/review-checks.txt`. "Comments resolved" shows no open AI-draft comments; student/adult review may raise new comments, which must be resolved and the version bumped before approval.)

## Frozen versions
Versions are frozen only at adult approval. Until then the scripts remain `draft`
and may still be rewritten by the student. After approval, the frozen version ID
is the one referenced by the matching `assets/audio/<scene-id>.mp3` recording.

## Open items (manual gates)
1. Student rewrites all final wording and reads each aloud (S06 gate).
2. Adult reviews and approves all four scripts (S07 gate) — set each row to `approved` and freeze the version.
3. Then proceed to recording per `assets/audio/README.md`.
