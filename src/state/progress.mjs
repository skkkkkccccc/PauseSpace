// PauseSpace versioned local progress (S12). Versioned payload, forward
// migration of stale versions, reset, and safe error objects. Storage is
// injectable (the app passes localStorage; tests pass an in-memory store).
// No scores, streaks, rankings, names, or identifying data — only per-scene
// "visited" flags. Default key matches config/sample-config.json.
const CURRENT_VERSION = 1;
const DEFAULT_KEY = "pausespace.progress.v1";

function err(code, message) {
  return { ok: false, code, message };
}

export const CURRENT = CURRENT_VERSION;

/** A fresh, empty, versioned payload. */
export function emptyPayload() {
  return { version: CURRENT_VERSION, scenes: {}, updatedAt: null };
}

/** Injectable in-memory store (mirrors the localStorage interface). */
export function makeStore() {
  const m = new Map();
  return {
    getItem: (k) => (m.has(k) ? m.get(k) : null),
    setItem: (k, v) => { m.set(k, v); },
    removeItem: (k) => { m.delete(k); },
  };
}

export function encode(payload) {
  try { return JSON.stringify(payload); } catch (e) { return null; }
}

/** Decode + migrate raw stored JSON. Returns {ok, data?, migrated?} or an error. */
export function decode(raw) {
  if (raw == null) return err("empty", "no stored data");
  let data;
  try { data = JSON.parse(raw); } catch (e) { return err("malformed", "stored data is not valid JSON"); }
  return migrate(data);
}

/** Migrate a parsed payload to the current version (or signal reset). */
export function migrate(data) {
  if (data == null || typeof data !== "object") return err("malformed", "payload is not an object");
  if (typeof data.version !== "number") return err("unknown_version", "no version field -> reset");
  if (data.version === CURRENT_VERSION) return { ok: true, data };
  if (data.version < CURRENT_VERSION) {
    const kept = {};
    const scenes = (data.scenes && typeof data.scenes === "object") ? data.scenes : {};
    for (const [id, v] of Object.entries(scenes)) {
      if (v && typeof v === "object") kept[id] = { visited: !!v.visited }; // keep only versioned fields
    }
    return { ok: true, data: { version: CURRENT_VERSION, scenes: kept, updatedAt: null }, migrated: true };
  }
  return err("future_version", "payload is newer than current -> reset");
}

/** Record that a scene was visited (non-judgmental; no score/streak). */
export function recordVisit(payload, sceneId) {
  const p = payload || emptyPayload();
  p.scenes = p.scenes || {};
  p.scenes[sceneId] = { visited: true };
  p.updatedAt = new Date().toISOString();
  return p;
}

export function saveProgress(store, key, payload) {
  const k = key || DEFAULT_KEY;
  const raw = encode(payload);
  if (raw == null) return err("encode_failed", "could not encode payload");
  try { store.setItem(k, raw); return { ok: true }; } catch (e) { return err("store_failed", "could not write"); }
}

export function loadProgress(store, key) {
  const k = key || DEFAULT_KEY;
  let raw;
  try { raw = store.getItem(k); } catch (e) { return err("store_failed", "could not read"); }
  const r = decode(raw);
  if (!r.ok) return r;
  return { ok: true, data: r.data, migrated: !!r.migrated };
}

export function resetProgress(store, key) {
  const k = key || DEFAULT_KEY;
  try { store.removeItem(k); return { ok: true }; } catch (e) { return err("store_failed", "could not remove"); }
}
