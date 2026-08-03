import { test } from "node:test";
import assert from "node:assert/strict";
import {
  makeStore, emptyPayload, recordVisit, saveProgress, loadProgress,
  resetProgress, decode, migrate, CURRENT,
} from "../src/state/progress.mjs";

test("versioned round-trip (save -> load)", () => {
  const store = makeStore();
  const p = recordVisit(emptyPayload(), "exam-room");
  assert.equal(saveProgress(store, "k", p).ok, true);
  const r = loadProgress(store, "k");
  assert.equal(r.ok, true);
  assert.equal(r.data.version, CURRENT);
  assert.equal(r.data.scenes["exam-room"].visited, true);
});

test("stale-version payload migrates forward (drops non-versioned fields)", () => {
  const r = migrate({ version: 0, scenes: { "exam-room": { visited: true, streak: 5 } } });
  assert.equal(r.ok, true);
  assert.equal(r.migrated, true);
  assert.equal(r.data.version, CURRENT);
  assert.equal(r.data.scenes["exam-room"].visited, true);
  assert.equal(r.data.scenes["exam-room"].streak, undefined);
});

test("malformed stored JSON fails safely", () => {
  const r = decode("{not valid json");
  assert.equal(r.ok, false);
  assert.equal(r.code, "malformed");
});

test("future-version payload signals reset", () => {
  const r = migrate({ version: CURRENT + 1, scenes: {} });
  assert.equal(r.ok, false);
  assert.equal(r.code, "future_version");
});

test("reset clears stored progress", () => {
  const store = makeStore();
  saveProgress(store, "k", recordVisit(emptyPayload(), "exam-room"));
  assert.equal(resetProgress(store, "k").ok, true);
  const r = loadProgress(store, "k");
  assert.equal(r.ok, false); // empty -> error (nothing stored)
});
