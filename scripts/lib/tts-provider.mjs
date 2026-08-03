// OA01 TTS provider adapter (development-only). The dry-run path makes NO
// network requests and exposes no secret. The generate path requires an approved
// provider + credentials from the ignored local environment; with none
// configured (or an unapproved provider) it returns a safe error and makes NO
// network call. No third-party SDK is imported — the production build (dist/)
// contains no TTS code (build copies only src/{index.html,styles.css,app.js}).
import { createHash } from "node:crypto";

// Empty until the student/teacher approves exactly one provider (OA01 A1).
export const APPROVED_PROVIDERS = new Set([]);

/** SHA-256 of the exact transcript text (OA01 provenance). */
export function hashTranscript(text) {
  return createHash("sha256").update(text || "", "utf8").digest("hex");
}

/** Never return a raw credential. */
export function redact(s) {
  if (typeof s !== "string" || !s) return "";
  return s.length <= 6 ? "<redacted>" : s.slice(0, 2) + "***" + s.slice(-2);
}

export function isProviderConfigured(env) {
  const e = env || {};
  return !!(e.TTS_PROVIDER && e.TTS_API_KEY && e.TTS_MODEL && e.TTS_VOICE && e.TTS_LOCALE);
}

/** Dry-run plan for one scene. No network; the API key is never placed in output. */
export function dryRunPlan(scene, env) {
  const e = env || {};
  const text = scene && scene.transcript && scene.transcript.text;
  const hash = hashTranscript(text);
  return {
    sceneId: scene && scene.id,
    transcriptSha256: hash,
    output: "assets/audio/generated/" + (scene && scene.id) + "." + hash.slice(0, 8) + ".ai.mp3",
    provider: e.TTS_PROVIDER || "<unconfigured>",
    model: e.TTS_MODEL || "<unconfigured>",
    voice: e.TTS_VOICE || "<unconfigured>",
    locale: e.TTS_LOCALE || "<unconfigured>",
    estimatedRequests: 1,
    secretExposed: false,
  };
}

/**
 * Why generation would be blocked for a scene: unapproved script, or no
 * approved/configured provider. Used by dry-run reporting and generate().
 */
export function generationBlockedReason(scene, env) {
  const e = env || {};
  const status = scene && scene.review && scene.review.status;
  if (status !== "approved")
    return { blocked: true, code: "unapproved_script", message: "script status '" + status + "' — OA01 refuses draft/unapproved content" };
  if (!isProviderConfigured(e))
    return { blocked: true, code: "provider_not_configured", message: "no approved TTS provider/credentials" };
  if (!APPROVED_PROVIDERS.has(e.TTS_PROVIDER))
    return { blocked: true, code: "provider_not_approved", message: "provider not in the approved set" };
  return { blocked: false };
}

/**
 * Generate one track. Requires an approved script AND an approved, configured
 * provider. Returns a safe error (NO network call) otherwise. The real provider
 * call is intentionally NOT wired until a provider is approved by the student/teacher.
 */
export async function generate(scene, env) {
  const r = generationBlockedReason(scene, env);
  if (r.blocked)
    return { ok: false, code: r.code, message: r.message + "; no network call." };
  return { ok: false, code: "not_implemented", message: "No approved provider wired yet; no network call made." };
}
