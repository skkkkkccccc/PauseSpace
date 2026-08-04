// Completion view (S15): return / replay / find-support choices + a non-emergency
// support route. Choices are independent of completion tracking (no streak/score).
// Support content is static, locally reviewed, and shown only when approved; the
// user can always leave. No emergency/diagnostic claims.
import { escapeHtml } from "./escape-html.js";

export const COMPLETION_ACTIONS = ["return", "replay", "find-support", "exit"];

/** True only when support is locally approved and not release-blocked. */
export function isSupportApproved(support) {
  return !!(support && support.reviewStatus === "approved" && !support.releaseBlocked);
}

/** Render the support panel; unapproved/missing support is never shown in full. */
export function renderSupport(support) {
  if (!support) {
    return '<div class="support state--missing" role="region" aria-label="Support">' +
      '<p>Support information is not available.</p></div>';
  }
  if (!isSupportApproved(support)) {
    return '<div class="support state--pending" role="region" aria-label="Support">' +
      '<p>Support information is being reviewed and is not shown until locally approved.</p></div>';
  }
  const boundary = support.boundary ? '<p class="support__boundary">' + escapeHtml(support.boundary) + '</p>' : "";
  const phrases = (support.phrases || [])
    .map((p) => '<li class="support-phrase">' + escapeHtml(p.text) + '</li>').join("");
  const contacts = (support.contacts || [])
    .filter((c) => c && c.approved)
    .map((c) => '<li class="support-contact"><span class="support-contact__label">' + escapeHtml(c.label) + ':</span> ' + escapeHtml(c.value) + '</li>')
    .join("");
  return '<div class="support" role="region" aria-label="Support">' +
    boundary +
    (phrases ? '<ul class="support-phrases">' + phrases + '</ul>' : '') +
    (contacts ? '<ul class="support-contacts">' + contacts + '</ul>' : '') +
    '</div>';
}

/** Render the completion view from { scene, support, showSupport }. */
export function completionView(state) {
  const s = state || {};
  const title = (s.scene && s.scene.title) ? s.scene.title : "Scene";
  const showSupport = !!s.showSupport;
  return '<section class="view view--completion" aria-label="Completion">' +
    '<h1 class="view__title">' + escapeHtml(title) + '</h1>' +
    '<p class="view__lede">You can return, replay, or find support — any time.</p>' +
    '<div class="completion-actions">' +
    '<button class="btn" type="button" data-action="return" aria-label="Return to the menu">Return</button>' +
    '<button class="btn" type="button" data-action="replay" aria-label="Replay this scene">Replay</button>' +
    '<button class="btn" type="button" data-action="find-support" aria-label="Find support" aria-expanded="' + showSupport + '">Find support</button>' +
    '<button class="btn btn--ghost" type="button" data-action="exit" aria-label="Leave">Leave</button>' +
    '</div>' +
    (showSupport ? renderSupport(s.support) : '') +
    '</section>';
}
