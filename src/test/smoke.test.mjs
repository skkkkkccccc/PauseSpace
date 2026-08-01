import { test } from "node:test";
import assert from "node:assert/strict";
import { sceneCount, isKnownScene, SCENE_IDS } from "../app.js";

test("four launch scenes are defined", () => {
  assert.equal(sceneCount(), 4);
});

test("known and unknown scene ids", () => {
  assert.equal(isKnownScene("exam-room"), true);
  assert.equal(isKnownScene("nope"), false);
});

test("scene ids match the four launch scenes", () => {
  assert.deepEqual(
    [...SCENE_IDS].sort(),
    ["empty-classroom", "exam-room", "own-room", "sports-field"]
  );
});
