// PauseSpace scene loader + validation (S12). Mirrors content/schema.json.
// Pure functions; safe error objects {ok, code, message}; never throws on
// malformed input. No personal data; runs on scene objects (synthetic content).
const REQUIRED = ["id", "title", "durationSeconds", "segments", "exit", "transcript", "audio", "review"];
const STATUS = new Set(["draft", "in-review", "approved"]);
const SEG_REQUIRED = ["order", "label", "startSecond", "endSecond", "text"];
const SEG_ALLOWED = new Set([...SEG_REQUIRED, "optional"]);
const TOP_ALLOWED = new Set([...REQUIRED, "moment", "focus"]);

function err(code, message) {
  return { ok: false, code, message };
}

/** Validate one scene against the content/schema.json contract. */
export function validateScene(scene) {
  try {
    if (scene == null || typeof scene !== "object" || Array.isArray(scene))
      return err("invalid_type", "scene must be an object");
    const errors = [];
    for (const k of Object.keys(scene)) if (!TOP_ALLOWED.has(k)) errors.push("extra key: " + k);
    for (const k of REQUIRED) if (!(k in scene)) errors.push("missing: " + k);
    if (errors.length) return err("missing_fields", errors.join("; "));

    if (typeof scene.id !== "string" || !scene.id) errors.push("id must be a non-empty string");
    if (typeof scene.title !== "string" || !scene.title) errors.push("title must be a non-empty string");
    const d = scene.durationSeconds;
    if (!(typeof d === "number" && Number.isInteger(d) && d >= 1 && d <= 300))
      errors.push("durationSeconds must be an integer 1..300");
    if (!Array.isArray(scene.segments) || scene.segments.length === 0)
      errors.push("segments must be a non-empty array");
    else
      scene.segments.forEach((s, i) => {
        if (s == null || typeof s !== "object") { errors.push("segment " + i + " must be an object"); return; }
        for (const k of Object.keys(s)) if (!SEG_ALLOWED.has(k)) errors.push("segment " + i + " extra key " + k);
        for (const k of SEG_REQUIRED) if (!(k in s)) errors.push("segment " + i + " missing " + k);
        if (typeof s.text !== "string" || !s.text) errors.push("segment " + i + " text empty");
      });
    const ex = scene.exit;
    if (!(ex && typeof ex.language === "string" && ex.language)) errors.push("exit.language must be non-empty");
    const tr = scene.transcript;
    if (!(tr && tr.sameOrigin === true && typeof tr.text === "string" && tr.text))
      errors.push("transcript requires sameOrigin=true and text");
    const au = scene.audio;
    if (!(au && au.sameOrigin === true && typeof au.src === "string" && au.src))
      errors.push("audio requires sameOrigin=true and src");
    const rv = scene.review;
    if (!(rv && STATUS.has(rv.status))) errors.push("review.status must be draft | in-review | approved");

    if (errors.length) return err("invalid_scene", errors.join("; "));
    return { ok: true };
  } catch (e) {
    return err("unsafe", "validation threw: " + (e && e.message));
  }
}

/** Validate a list of scenes; returns {ok, valid[], failed{}}. Safe on bad input. */
export function loadScenes(scenes) {
  if (!Array.isArray(scenes)) return err("invalid_input", "scenes must be an array");
  const valid = [];
  const failed = {};
  for (const sc of scenes) {
    const id = sc && typeof sc === "object" && typeof sc.id === "string" ? sc.id : "<unknown>";
    const r = validateScene(sc);
    if (r.ok) valid.push(sc);
    else failed[id] = r;
  }
  return { ok: Object.keys(failed).length === 0, valid, failed };
}
