// Scene detail view (S13). Renders one scene's detail from validated JSON.
// Malformed content fails visibly (error view, no throw). Audio is shown as
// metadata only — there is NO audio playback and NO runtime TTS in S13.
import { validateScene } from "../data/scene-loader.mjs";
import { escapeHtml } from "./escape-html.js";

export function sceneDetailView(scene) {
  const v = validateScene(scene);
  if (!v.ok) {
    return '<section class="view view--detail" aria-label="Scene detail" role="alert">' +
      '<p class="state state--error">This scene could not be shown.</p>' +
      '<button class="btn btn--back" type="button" data-action="back">Back</button>' +
      '</section>';
  }
  const s = scene;
  const minutes = Math.max(1, Math.round((s.durationSeconds || 0) / 60));
  const segments = (s.segments || [])
    .map((seg) => '<p class="scene-segment">' + escapeHtml(seg.text) + '</p>')
    .join("");
  const audioSrc = (s.audio && s.audio.src) || "not available";
  return (
    '<section class="view view--detail" aria-label="Scene detail">' +
    '<button class="btn btn--back" type="button" data-action="back">Back</button>' +
    '<h1 class="view__title">' + escapeHtml(s.title) + '</h1>' +
    '<p class="view__focus">' + escapeHtml(s.focus || "") + '</p>' +
    '<p class="view__duration">About ' + minutes + ' minute' + (minutes === 1 ? '' : 's') + '.</p>' +
    '<div class="scene-script">' + segments + '</div>' +
    '<p class="view__audio state--meta">Audio: ' + escapeHtml(audioSrc) + ' (no playback in this build)</p>' +
    '</section>'
  );
}
