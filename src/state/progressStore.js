// PauseSpace progress store (S16): completion lights + versioned localStorage +
// full reset + corrupt/old-version recovery. Built on the S12 versioned progress
// module. Stores ONLY a per-scene "visited" flag — no free text, mood score,
// names, or identifiers. No account, no server, no sync.
import {
  recordVisit, saveProgress, loadProgress, resetProgress, emptyPayload, makeStore,
} from "./progress.mjs";

export const SCENE_IDS = ["exam-room", "sports-field", "own-room", "empty-classroom"];
export const STORAGE_KEY = "pausespace.progress.v1";
export const PRIVACY_NOTE =
  "Your progress stays only on this device (browser localStorage). There is no account, server, or syncing. " +
  "We store only which scenes you have visited — no names, no notes, no mood scores. Use Reset to clear it anytime.";

/** Mark a scene complete (idempotent). Refuses unknown scene ids (schema-validated). */
export function recordCompletion(payload, sceneId) {
  if (!SCENE_IDS.includes(sceneId)) {
    return { ok: false, code: "unknown_scene", message: "unknown scene id" };
  }
  return { ok: true, payload: recordVisit(payload || emptyPayload(), sceneId) };
}

/** Return { sceneId: boolean } lights for the four scenes. */
export function completionLights(payload) {
  const scenes = (payload && payload.scenes) || {};
  const lights = {};
  for (const id of SCENE_IDS) lights[id] = !!(scenes[id] && scenes[id].visited);
  return lights;
}

/** True iff the payload stores only the allowed "visited" flag per scene. */
export function hasNoSensitiveData(payload) {
  const scenes = (payload && payload.scenes) || {};
  for (const v of Object.values(scenes)) {
    if (!v || typeof v !== "object") continue;
    for (const key of Object.keys(v)) if (key !== "visited") return false;
  }
  return true;
}

// Any non-ok load (empty / corrupt / future-version) -> clear + start empty.
function recover(store, key, result) {
  if (!result.ok) {
    resetProgress(store, key);
    return emptyPayload();
  }
  return result.data;
}

/** Bound store with markComplete / lights / reset / reload / explain. Injectable store. */
export function createProgressStore(opts) {
  const o = opts || {};
  const store = o.store || (typeof localStorage !== "undefined" ? localStorage : makeStore());
  const key = o.key || STORAGE_KEY;
  let payload = recover(store, key, loadProgress(store, key));

  return {
    markComplete(sceneId) {
      const r = recordCompletion(payload, sceneId);
      if (!r.ok) return r;
      payload = r.payload;
      const s = saveProgress(store, key, payload);
      return s.ok ? { ok: true } : s;
    },
    lights() { return completionLights(payload); },
    reset() { resetProgress(store, key); payload = emptyPayload(); return { ok: true }; },
    reload() { payload = recover(store, key, loadProgress(store, key)); return payload; },
    explain() { return PRIVACY_NOTE; },
    _payload() { return payload; },
  };
}
