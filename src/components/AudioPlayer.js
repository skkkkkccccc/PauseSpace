// Accessible audio control surface (S14). User-initiated only — NO autoplay.
// Uses the S12 player FSM for state. Shows an error when audio is missing.
// All controls are keyboard-operable buttons; reduced-motion is honored; reset is
// safe; going to background pauses; resume never auto-plays.
import { transition } from "../state/player.mjs";
import { normalizeMode } from "./ModePicker.js";
import { escapeHtml } from "../views/escape-html.js";

/** A scene has usable (same-origin, non-empty) audio. */
export function hasAudio(scene) {
  return !!(scene && scene.audio && scene.audio.sameOrigin === true && scene.audio.src);
}

/** Primary control for a given FSM state (idle/ready -> Play, i.e. user-initiated). */
export function primaryAction(state) {
  switch (state) {
    case "playing": return { label: "Pause", action: "pause" };
    case "paused": return { label: "Resume", action: "resume" };
    case "ended": return { label: "Replay", action: "replay" };
    case "exited": return { label: "Restart", action: "reset" };
    default: return { label: "Play", action: "start" }; // idle/ready
  }
}

/** On background (mobile): pause if playing. Never auto-resume. */
export function onBackground(player) {
  if (player && player.state === "playing") return transition(player, "pause");
  return { ok: true, to: player && player.state };
}
/** On resume: do NOT auto-resume — wait for the user. */
export function onResume(player) {
  return { ok: true, to: player && player.state, autoResumed: false };
}

/** Render the player controls from { scene, player, mode, transcriptOpen, reducedMotion }. */
export function audioPlayer(state) {
  const s = state || {};
  const scene = s.scene;
  const mode = normalizeMode(s.mode);
  const reduced = !!s.reducedMotion;
  const mins = Math.max(1, Math.round(((scene && scene.durationSeconds) || 0) / 60));

  if (!hasAudio(scene)) {
    return '<div class="audio-player audio-player--error" role="alert" data-reduced-motion="' + reduced + '">' +
      '<p class="state state--error">Audio is not available for this scene. You can read the transcript.</p>' +
      '<button class="btn" type="button" data-action="back" aria-label="Back">Back</button>' +
      '</div>';
  }

  const pa = primaryAction(s.player && s.player.state);
  const showTranscript = (s.transcriptOpen != null) ? !!s.transcriptOpen : (mode === "eyes-open");
  const transcriptText = (scene && scene.transcript && scene.transcript.text) ? scene.transcript.text : "";

  return '<div class="audio-player" data-mode="' + mode + '" data-reduced-motion="' + reduced + '" role="group" aria-label="Scene player">' +
    '<button class="btn btn--primary" type="button" data-action="' + pa.action + '" aria-label="' + pa.label + '">' + pa.label + '</button>' +
    '<button class="btn" type="button" data-action="reset" aria-label="Reset">Reset</button>' +
    '<progress class="audio-progress" max="100" value="0" aria-label="Progress"></progress>' +
    '<span class="audio-time">0:00 / ' + mins + ':00</span>' +
    '<button class="btn btn--ghost" type="button" data-action="toggle-transcript" aria-pressed="' + showTranscript + '" aria-label="Toggle transcript">Transcript</button>' +
    (showTranscript && transcriptText ? '<p class="audio-transcript">' + escapeHtml(transcriptText) + '</p>' : '') +
    '<button class="btn" type="button" data-action="exit" aria-label="Exit">Exit</button>' +
    '</div>';
}
