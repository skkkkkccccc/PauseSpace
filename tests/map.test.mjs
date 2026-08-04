import { test } from "node:test";
import assert from "node:assert/strict";
import {
  recordCompletion, completionLights, hasNoSensitiveData, createProgressStore,
  PRIVACY_NOTE, SCENE_IDS,
} from "../src/state/progressStore.js";
import { makeStore } from "../src/state/progress.mjs";
import { mapView } from "../src/views/Map.js";

// --- refresh persistence ---
test("completion survives a fresh store re-read (refresh)", () => {
  const store = makeStore();
  createProgressStore({ store }).markComplete("exam-room");
  const after = createProgressStore({ store }); // simulate refresh
  assert.equal(after.lights()["exam-room"], true);
});

// --- duplicate completion is idempotent (no count/streak) ---
test("duplicate completion is idempotent — one light, no count field", () => {
  const ps = createProgressStore({ store: makeStore() });
  ps.markComplete("exam-room");
  ps.markComplete("exam-room");
  assert.equal(ps.lights()["exam-room"], true);
  assert.deepEqual(ps._payload().scenes["exam-room"], { visited: true });
});

// --- corrupt / partial payload recovery ---
test("corrupt stored JSON recovers to empty (no throw)", () => {
  const store = makeStore();
  store.setItem("k", "{not valid json");
  const ps = createProgressStore({ store, key: "k" });
  for (const id of SCENE_IDS) assert.equal(ps.lights()[id], false);
});

test("partial payload without a version recovers to empty (drops any junk)", () => {
  const store = makeStore();
  store.setItem("k2", JSON.stringify({ scenes: { "exam-room": { visited: true, diary: "secret" } } }));
  const ps = createProgressStore({ store, key: "k2" });
  assert.equal(ps.lights()["exam-room"], false);
});

// --- old version migration ---
test("old version (v0) migrates and keeps the visited light", () => {
  const store = makeStore();
  store.setItem("k3", JSON.stringify({ version: 0, scenes: { "exam-room": { visited: true, streak: 5 } } }));
  const ps = createProgressStore({ store, key: "k3" });
  assert.equal(ps.lights()["exam-room"], true); // migrated; non-versioned fields dropped
});

// --- complete reset ---
test("complete reset clears all lights and persists", () => {
  const store = makeStore();
  const ps = createProgressStore({ store });
  ps.markComplete("exam-room");
  ps.markComplete("sports-field");
  ps.reset();
  for (const id of SCENE_IDS) assert.equal(ps.lights()[id], false);
  const fresh = createProgressStore({ store });
  for (const id of SCENE_IDS) assert.equal(fresh.lights()[id], false);
});

// --- stores no sensitive text / mood score ---
test("payload stores only a visited flag — no free text, no mood score", () => {
  const ps = createProgressStore({ store: makeStore() });
  ps.markComplete("exam-room");
  assert.equal(hasNoSensitiveData(ps._payload()), true);
  assert.equal(ps._payload().scenes["exam-room"].moodScore, undefined);
  assert.equal(ps._payload().scenes["exam-room"].notes, undefined);
});

// --- unknown scene refused (schema-validated) ---
test("unknown scene id is refused", () => {
  const r = recordCompletion({ version: 1, scenes: {} }, "nope");
  assert.equal(r.ok, false);
  assert.equal(r.code, "unknown_scene");
});

// --- map view ---
test("map view renders 4 scenes with lights, the privacy note, and reset", () => {
  const scenes = SCENE_IDS.map((id) => ({ id, title: id }));
  const lights = { "exam-room": true, "sports-field": false, "own-room": true, "empty-classroom": false };
  const html = mapView({ scenes, lights });
  for (const id of SCENE_IDS) assert.match(html, new RegExp('data-scene="' + id + '"'));
  assert.match(html, /data-complete="true"/);
  assert.match(html, /data-complete="false"/);
  assert.match(html, /Reset local progress/);
  assert.match(html, /no scores, streaks/); // non-judgmental lede
  assert.match(PRIVACY_NOTE, /only on this device/);
  assert.match(html, /no names, no notes, no mood scores/); // privacy note rendered
});
