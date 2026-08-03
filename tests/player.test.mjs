import { test } from "node:test";
import assert from "node:assert/strict";
import { createPlayer, transition } from "../src/state/player.mjs";

test("happy path: idle -> ready -> playing -> ended", () => {
  const p = createPlayer();
  assert.equal(p.state, "idle");
  assert.equal(transition(p, "prepare").to, "ready");
  assert.equal(transition(p, "start").to, "playing");
  assert.equal(transition(p, "complete").to, "ended");
});

test("exit is allowed from active states instead of completing (no forced completion)", () => {
  const fromIdle = createPlayer();
  assert.equal(transition(fromIdle, "exit").to, "exited");

  const fromPlaying = createPlayer();
  transition(fromPlaying, "prepare");
  transition(fromPlaying, "start");
  assert.equal(transition(fromPlaying, "exit").to, "exited"); // leave mid-scene
});

test("interrupted playback: playing -> pause -> resume", () => {
  const p = createPlayer();
  transition(p, "prepare");
  transition(p, "start");
  assert.equal(transition(p, "pause").to, "paused");
  assert.equal(transition(p, "resume").to, "playing");
});

test("invalid transition returns a safe error, no throw", () => {
  const p = createPlayer(); // idle
  const r = transition(p, "complete"); // not allowed in idle
  assert.equal(r.ok, false);
  assert.equal(r.code, "invalid_transition");
});

test("reset returns to idle from any state", () => {
  const p = createPlayer();
  transition(p, "prepare");
  transition(p, "start");
  assert.equal(transition(p, "reset").to, "idle");
});
