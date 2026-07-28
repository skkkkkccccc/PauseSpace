# Research Protocol — PauseSpace peer feedback (S02)

> **Status: SYNTHETIC / DRAFT — for student role-play only.** No real
> participants are interviewed until the student has role-played interviewer and
> participant, rewritten any leading or intrusive question, and obtained
> mentor/adult review. PauseSpace is not diagnosis, treatment, counselling, or
> emergency support.

This protocol gathers **task-based, usability feedback** about the PauseSpace
scenes. It deliberately collects **no** names, contact details, or personal or
psychological histories. All notes are synthetic or anonymized (see
`data/sample/interview-notes.json`).

## Assent and consent
Before any activity, the student researcher reads this short, age-appropriate
script to the participant:

> "This is a student project. I'm building PauseSpace, a small web app with short
> calm-focus scenes, and I'd like your honest feedback on how it works. Taking
> part is completely voluntary — you can skip any question or stop at any time,
> for any reason, with no consequences. I will not record your name or any contact
> details, and my notes will be anonymous or synthetic. This is not a medical,
> counselling, or diagnostic activity. A teacher/mentor is overseeing the project.
> Do you agree to take part? You can say no."

For participants under 18, the student follows their school/mentor's assent and
guardian-awareness process before any real interview, consistent with the
project's standing mentor/adult-review requirement.

## Voluntary participation and stop rules
- Participation is optional. A "no" is accepted immediately and finally.
- The participant may skip any single question without giving a reason.
- The participant may pause or stop at any time. The agreed stop phrases are
  **"I'd like to stop"** or simply **"stop"**. On stop, the activity ends
  immediately and any notes from that session are discarded or fully anonymized.
- The participant's voice is **not** recorded (microphone capture is out of scope
  for PauseSpace). Notes are written by the student researcher only.
- No incentive that could feel coercive is offered.

## Task questions (neutral, non-diagnostic)
Use these neutral, task-focused questions. Each probes the experience or the
interface — never a clinical state.

1. Walk me through what you did from the moment the scene started.
2. Was anything on the screen hard to see, read, or tap on your phone?
3. Could you hear the audio clearly? (yes / no / where)
4. How easy was it to move between the views? (easy / hard / why)
5. About how long did the scene feel to you? (too short / about right / too long)
6. What did you do right after the scene ended?
7. Was there anything that got in the way of using it?
8. If you could change one thing about how it looks or works, what would it be?
9. Which view did you spend the most time on, and why?
10. Would you use this again during a short break? What would make it more useful?

## Questions to avoid (do not ask)
Do **not** ask any of the following — rewrite or drop them if they appear:
- The participant's name, username, email, phone, school, or any contact detail.
- Anything about conditions, diagnoses, medication, or self-diagnosis.
- Anything about the participant's household or family situation.
- Any request to rate a feeling or symptom on a numeric scale (for example,
  "rate your stress 1–10").
- Any question that could identify the person or collect a personal history.

## Data-minimization checklist
Review **every** question and note against this list before saving:
- [ ] No participant names or usernames are collected.
- [ ] No contact details (email, phone, handles).
- [ ] No mental-health or psychological histories.
- [ ] No clinical or diagnostic labels and no self-diagnosis prompts.
- [ ] No family or household details.
- [ ] No mood scores or symptom ratings.
- [ ] No microphone or voice recording of the participant.
- [ ] No analytics identifiers or device fingerprints.
- [ ] Notes are synthetic or anonymized; nothing identifying is committed to Git.
- [ ] Voluntary participation and the stop rule were stated before starting.

## Note template and storage
- Record notes using the schema in `data/sample/interview-notes.json`
  (fields: `sessionId`, `sceneId`, `taskObservations`, `usability`,
  `durationPerception`, `wouldChange`, `reviewStatus`).
- `sessionId` is a synthetic code (for example `sample-session-001`), **not** a
  person identifier.
- Keep all real research notes outside Git (`.gitignore` already excludes
  `private-research/` and `*.log`); only synthetic/anonymized samples are
  committed.
