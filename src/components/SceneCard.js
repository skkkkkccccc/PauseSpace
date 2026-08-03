// SceneCard component (S13). Renders one scene card from validated scene data.
// All text comes from the scene object — no hard-coded scene copy. Safe insertion.
import { escapeHtml } from "../views/escape-html.js";

export function sceneCard(scene) {
  const s = scene || {};
  const id = escapeHtml(s.id);
  const title = escapeHtml(s.title);
  const moment = escapeHtml(s.moment);
  const minutes = Math.max(1, Math.round((s.durationSeconds || 0) / 60));
  return (
    '<article class="scene-card" data-scene="' + id + '">' +
    '<h2 class="scene-card__title">' + title + '</h2>' +
    (moment ? '<p class="scene-card__moment">' + moment + '</p>' : '') +
    '<p class="scene-card__duration">About ' + minutes + ' minute' + (minutes === 1 ? '' : 's') + '</p>' +
    '<button class="scene-card__open" type="button" data-scene="' + id + '">Open</button>' +
    '</article>'
  );
}
