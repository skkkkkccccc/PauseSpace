import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { validateScene, loadScenes } from "../src/data/scene-loader.mjs";

const valid = JSON.parse(readFileSync(new URL("../content/exam-room.json", import.meta.url), "utf8"));

test("valid scene passes", () => {
  assert.equal(validateScene(valid).ok, true);
});

test("missing required field fails safely (no throw)", () => {
  const noExit = { ...valid };
  delete noExit.exit;
  const r = validateScene(noExit);
  assert.equal(r.ok, false);
  assert.ok(r.code);
});

test("malformed duration fails safely", () => {
  assert.equal(validateScene({ ...valid, durationSeconds: 9999 }).ok, false);
});

test("malformed non-object input fails safely (no throw)", () => {
  assert.equal(validateScene(null).ok, false);
  assert.equal(validateScene("nope").ok, false);
  assert.equal(validateScene(undefined).ok, false);
});

test("missing exit language fails safely", () => {
  assert.equal(validateScene({ ...valid, exit: { language: "" } }).ok, false);
});

test("loadScenes aggregates valid + failed", () => {
  const res = loadScenes([valid, { ...valid, id: "bad", durationSeconds: "x" }]);
  assert.equal(res.ok, false);
  assert.equal(res.valid.length, 1);
  assert.ok(res.failed["bad"]);
});
