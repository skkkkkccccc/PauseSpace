// Reversible eyes-open / eyes-closed viewing mode (S14). The mode changes
// PRESENTATION ONLY — it never changes PauseSpace's safety / non-diagnostic claims.
// (Eyes-closed = audio-focused; it is not sensory deprivation.)
export const MODES = ["eyes-open", "eyes-closed"];
export const DEFAULT_MODE = "eyes-open";

export function isValidMode(m) {
  return MODES.includes(m);
}
export function normalizeMode(m) {
  return isValidMode(m) ? m : DEFAULT_MODE;
}
// Reversible: always flips to the other mode.
export function toggleMode(m) {
  return normalizeMode(m) === "eyes-closed" ? "eyes-open" : "eyes-closed";
}

const SAFETY_NOTE = "PauseSpace is not diagnosis, treatment, counselling, or emergency support. Viewing mode changes presentation only.";

export function modePicker(state) {
  const mode = normalizeMode(state && state.mode);
  const reduced = !!((state && state.reducedMotion) || false);
  const options = MODES.map((m) => {
    const label = m === "eyes-closed" ? "Eyes closed (audio only)" : "Eyes open";
    const pressed = m === mode ? "true" : "false";
    return '<button class="mode-option" type="button" data-mode="' + m + '" aria-pressed="' + pressed + '" aria-label="' + label + '">' + label + '</button>';
  }).join("");
  return '<div class="mode-picker" data-reduced-motion="' + reduced + '" role="group" aria-label="Viewing mode (presentation only)">' +
    options +
    '<p class="mode-note">' + SAFETY_NOTE + '</p>' +
    '</div>';
}
