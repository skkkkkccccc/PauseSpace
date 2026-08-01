// PauseSpace app entry (S11 minimal skeleton).
// Native ES module, no dependencies, no network calls, runtime secret-free.

/** The four launch scenes (must match content/*.json). */
export const SCENE_IDS = ["exam-room", "sports-field", "own-room", "empty-classroom"];

/** Number of launch scenes. */
export function sceneCount() {
  return SCENE_IDS.length;
}

/** True if id is one of the launch scenes. */
export function isKnownScene(id) {
  return SCENE_IDS.includes(id);
}

// Browser-only render (no-op when imported by node tests).
if (typeof document !== "undefined") {
  const el = document.getElementById("app");
  if (el) {
    el.innerHTML =
      "<h1>PauseSpace</h1>" +
      "<p class=\"muted\">A short, calm moment. Not diagnosis, treatment, counselling, or emergency support.</p>" +
      "<p>Scenes: " + sceneCount() + "</p>" +
      "<ul>" + SCENE_IDS.map((s) => "<li>" + s + "</li>").join("") + "</ul>";
  }
}
