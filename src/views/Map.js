// Pause map view (S16): a non-judgmental view of the four scenes with completion
// lights + the local-privacy note + reset. No scores, streaks, or rankings.
import { escapeHtml } from "./escape-html.js";
import { PRIVACY_NOTE } from "../state/progressStore.js";

export function mapView(state) {
  const s = state || {};
  const scenes = Array.isArray(s.scenes) ? s.scenes : [];
  const lights = s.lights || {};
  const items = scenes.map((sc) => {
    const id = (sc && sc.id) || "";
    const lit = !!lights[id];
    const title = escapeHtml((sc && sc.title) || id);
    return '<li class="map-item' + (lit ? " is-complete" : "") + '" data-scene="' + escapeHtml(id) + '" data-complete="' + lit + '">' +
      '<span class="map-light" aria-hidden="true">' + (lit ? "●" : "○") + "</span>" +
      '<span class="map-title">' + title + "</span>" +
      "</li>";
  }).join("");

  return '<section class="view view--map" aria-label="Pause map">' +
    '<h1 class="view__title">Pause map</h1>' +
    '<p class="view__lede">A calm view of the scenes — no scores, streaks, or rankings.</p>' +
    (items ? '<ul class="map-list">' + items + "</ul>" : '<p class="state state--empty">No scenes.</p>') +
    '<p class="privacy-note">' + escapeHtml(PRIVACY_NOTE) + "</p>" +
    '<button class="btn" type="button" data-action="reset" aria-label="Reset all local progress">Reset local progress</button>' +
    '<button class="btn btn--ghost" type="button" data-action="home" aria-label="Back">Back</button>' +
    "</section>";
}
