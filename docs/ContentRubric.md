# Content Rubric — PauseSpace scene-script language (S04)

> **Status: structure + initial examples by the AI implementation partner. The
> student authors the final examples and explains, in their own words, why each
> command, promise, and judgment is rejected** (S04 §Student Manual Work). A scene
> is `review.status = approved` only after this rubric is applied line-by-line.

PauseSpace scripts use **choice language**: invitations, options, and neutral
sensory observations. They never **command**, **promise**, or **judge**. This
keeps the experience non-diagnostic, pressure-free, and consistent with the
boundaries in README.md and TASKS.md (no forced breathing, no autoplay, not
diagnosis/treatment/counselling/emergency support).

## How to use
Check every script line against the three prohibited categories below before
setting `review.status` to `approved`. If a line fails, rewrite it as choice
language (see “Accepted vs rejected examples”) or drop it.

## Prohibited: Commands
Do not tell the user what to do, feel, or how to breathe. Imperatives directed at
the body or mind create pressure and can feel coercive; breathing instructions in
particular are **forced breathing**, which is out of scope.
- Reject: “Breathe in now.” / “Stop thinking.” / “You must focus.” / “Close your eyes.” / “Do this now.”

## Prohibited: Promises
Do not guarantee an outcome or make therapeutic/medical claims. PauseSpace is not
diagnosis, treatment, counselling, or emergency support.
- Reject: “This will calm you.” / “This reduces stress.” / “You will feel better.” / “A cure for anxiety.” / “Therapeutic relief.”

## Prohibited: Judgments
Do not evaluate, moralize, compare, or diagnose the user or their experience.
- Reject: “Good job.” / “That’s the wrong way.” / “You’re too distracted.” / “Normal people focus faster.”

## Allowed: Choice language
- Invitations: “You might notice one detail…”
- Options: “If you like, you can return to the menu.”
- Neutral observations: “The scene shows a slow-moving image and steady sound.”
- No pressure, no labels, no required response, and the user can stop at any time.

## Accepted vs rejected examples
| Line | Verdict | Category if rejected |
|---|---|---|
| “You might let your attention rest on the screen for a moment.” | accepted | — |
| “If you like, notice one detail you can see or hear.” | accepted | — |
| “When you are ready, you can return to the menu.” | accepted | — |
| “Breathe in deeply now.” | rejected | command (forced breathing) |
| “This will calm you down.” | rejected | promise |
| “Good, you’re doing it right.” | rejected | judgment |
| “You must focus on the centre.” | rejected | command |
| “Reduces anxiety in three minutes.” | rejected | promise (medical/therapeutic) |

(The student replaces or extends these examples and writes the rationale.)

## Review checklist (per scene)
- [ ] No line is a command (no imperatives about breathing, focus, posture, or attention).
- [ ] No line is a promise (no outcome guarantees or therapeutic/medical claims).
- [ ] No line is a judgment (no evaluation, moralizing, comparison, or diagnosis).
- [ ] Every line is invitation/option/neutral observation; the user can stop at any time.
- [ ] Exit/stop language is present (matches `content/schema.json` `exit.language`).
- [ ] No forced breathing; no autoplay; no diagnosis/treatment/counselling/emergency claims.
