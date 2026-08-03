// Home view (S13). Renders four scene cards from validated JSON. Malformed
// content fails visibly (an error item, no throw). Empty state when no scenes.
// No scene copy is hard-coded here — all text comes from the scene objects.
import { sceneCard } from "../components/SceneCard.js";
import { validateScene } from "../data/scene-loader.mjs";
import { escapeHtml } from "./escape-html.js";

export function homeView(scenes) {
  const list = Array.isArray(scenes) ? scenes : [];
  if (list.length === 0) {
    return '<section class="view view--home" aria-label="Home">' +
      '<p class="state state--empty">No scenes available.</p>' +
      '</section>';
  }
  const cards = [];
  const errors = [];
  for (const sc of list) {
    const v = validateScene(sc);
    if (v.ok) cards.push(sceneCard(sc));
    else errors.push('<li class="state state--error" role="alert">Scene ' +
      escapeHtml((sc && sc.id) || "unknown") + ' could not be shown.</li>');
  }
  return (
    '<section class="view view--home" aria-label="Home">' +
    '<h1 class="view__title">PauseSpace</h1>' +
    '<p class="view__lede">A short, calm moment. Pick one scene.</p>' +
    (cards.length ? '<div class="scene-grid">' + cards.join("") + '</div>' : '') +
    (errors.length ? '<ul class="scene-errors">' + errors.join("") + '</ul>' : '') +
    '</section>'
  );
}
