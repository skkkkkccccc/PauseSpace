# Research Findings — Scene evidence synthesis (S03)

> **Status: SYNTHETIC / ASSUMPTION-BASED — pending student clustering and sign-off.**
> Observations here are coded and anonymized. No frequencies are invented: there
> are no counts, percentages, or "N out of M" statements. Every scene claim is
> traced to a coded observation (`O-xx`) or explicitly marked `[assumption]`.
> PauseSpace is not diagnosis, treatment, counselling, or emergency support.

## Data source and method
- Source material: the synthetic note `data/sample/interview-notes.json`
  (`sample-session-001`) from S02, plus assumptions that the student must confirm
  by clustering real, anonymized notes once gathered.
- Observations are **coded** (`O-01`…`O-08`) and carry no identifying data.
- Each scene is captured on one **evidence card** that separates Need, Evidence,
  Inference, Risk, and Design response (Requirement: separate observation,
  inference, risk, and design response).
- This document justifies the **four launch scenes** at a structural level. The
  specific scene **themes** are candidate assumptions, because the repo does not
  enumerate them (open decision D8).

## Coded observations (anonymized; no frequency)
| Code | Observation | Source |
|---|---|---|
| O-01 | The start control felt small on a phone screen. | synthetic note `sample-session-001` |
| O-02 | Returning to a simple menu after a scene was preferred. | synthetic note `sample-session-001` |
| O-03 | Audio that was easy to hear supported staying with the scene. | synthetic note `sample-session-001` |
| O-04 | A sense of how long a scene would take was wanted before starting. | synthetic note `sample-session-001` |
| O-05 | A small set of distinct scenes helps a person pick what fits the moment. | `[assumption]` — pending student clustering |
| O-06 | A short, fixed duration lowers any pressure to "do it right." | `[assumption]` — pending student clustering |
| O-07 | Calm, original (non-copied) audio and visuals support focus. | `[assumption]` — pending student clustering |
| O-08 | A way to pause or replay without losing place is expected. | `[assumption]` — pending student clustering |

## Scene evidence cards
Each card is one launch scene. Themes are candidates the student must confirm
against the proposal (D8).

### Scene 1 — Green space / nature (candidate theme — confirm against proposal)
- Need: A calming natural setting to gently redirect attention during a short break.
- Evidence: O-05, O-07 `[assumption]` support offering a nature option.
- Inference: A nature-themed scene is a reasonable launch option; specific visuals and audio are not yet confirmed.
- Risk: Generic or copied nature imagery would breach the originality/licensing boundary (B-07) and could feel generic.
- Design response: Use original nature visuals with same-origin audio; keep the scene ~3 minutes (B-01); confirm the theme with the student.

### Scene 2 — Slow water / rain (candidate theme — confirm against proposal)
- Need: A steady, low-demand sensory setting that is easy to stay with.
- Evidence: O-03, O-07 `[assumption]` support an audio-forward, calm option.
- Inference: A water/rain scene suits an audio-led calm focus; exact audio is unconfirmed.
- Risk: Audio that is hard to hear or too dynamic could break focus (O-03).
- Design response: Same-origin, easy-to-hear audio; original visuals; ~3 minutes; confirm theme with the student.

### Scene 3 — Night sky / stars (candidate theme — confirm against proposal)
- Need: A low-light, low-stimulation setting for winding down.
- Evidence: O-06, O-07 `[assumption]` support a short, calm, low-stimulation option.
- Inference: A night-sky scene is a reasonable low-stimulation launch option; specifics unconfirmed.
- Risk: Low-contrast visuals could fail accessibility (B-11) if not designed carefully.
- Design response: Meet contrast/motion accessibility (B-11); original visuals; ~3 minutes; confirm theme with the student.

### Scene 4 — Quiet street / urban calm (candidate theme — confirm against proposal)
- Need: A familiar, everyday setting that feels approachable.
- Evidence: O-05 `[assumption]` supports a distinct, everyday option alongside the others.
- Inference: An urban-calm scene broadens the choice set; specifics unconfirmed.
- Risk: Everyday settings risk branded/copied imagery (B-07) if sourced from stock.
- Design response: Original, unbranded visuals; same-origin audio; ~3 minutes; confirm theme with the student.

## Counter-evidence and open questions
- The four scene **themes are not documented in the repo**; they are candidate
  assumptions. Counter-evidence: the approved proposal may name different themes.
  The cards justify the **structure** (four scenes, each with evidence/need/risk/
  design response), not the specific themes. The student resolves this (D8).
- O-04 (sense of duration before starting) is **cross-cutting**, not scene-specific;
  it implies a shared design response: show scene length up front. Tracked for the
  UI sessions, not as a scene decision.
- O-01 (small start control) and O-02 (simple menu) are cross-cutting usability
  observations, addressed in later UI sessions, not in the scene decision.

## Traceability matrix
| Claim | Traced to |
|---|---|
| Four launch scenes are preserved (one experience per scene) | README; TASKS Global Rules; B-01 |
| Each scene is ~3 minutes | B-01; `docs/ProjectPlan.md` |
| Original, same-origin audio and visuals (no copied media) | B-07; `docs/Architecture.md` |
| Distinct scenes help a person choose what fits the moment | O-05 `[assumption]` |
| Short fixed duration lowers pressure | O-06 `[assumption]` |
| Calm original audio/visuals support focus | O-07 `[assumption]` |
| Specific scene themes (nature, water, sky, urban) | `[assumption]` — student to confirm (D8) |
| Start-control / menu / duration usability observations | O-01, O-02, O-04 (synthetic note `sample-session-001`) |

## Open decisions
- **D8** — Confirm the four scene themes against the proposal (the repo does not enumerate them). Owner: student.
- **D9** — Student performs the clustering of real anonymized notes (once gathered) and signs the four-scene decision. Owner: student.
- Evidence here is synthetic/assumption-based until real anonymized notes exist; no real participant data is used or stored.
