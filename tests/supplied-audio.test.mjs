// OA01 focused tests (after S17): verify the four supplied placeholder MP3s,
// the deterministic scene mapping, the placeholder manifest schema + hashes, that
// transcripts remain available, and that NO track is selected for release.
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, existsSync } from "node:fs";
import { createHash } from "node:crypto";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const here = dirname(fileURLToPath(import.meta.url));
const root = join(here, "..");
const IDS = ["exam-room", "sports-field", "own-room", "empty-classroom"];
const readJson = (p) => JSON.parse(readFileSync(join(root, p), "utf8"));
const sha256 = (rel) => createHash("sha256").update(readFileSync(join(root, rel))).digest("hex");

test("exactly the four expected supplied MP3s exist at assets/audio/", () => {
  for (const id of IDS) assert.ok(existsSync(join(root, "assets/audio", id + ".mp3")), "exists: " + id);
});

test("each scene JSON maps deterministically to assets/audio/<id>.mp3 and the file exists", () => {
  for (const id of IDS) {
    const scene = readJson("content/" + id + ".json");
    assert.equal(scene.audio.src, "assets/audio/" + id + ".mp3", "audio.src mapping: " + id);
    assert.ok(existsSync(join(root, scene.audio.src)), "file present: " + scene.audio.src);
  }
});

test("manifest placeholder validates: 4 tracks, valid roles, hashes match files", () => {
  const m = readJson("assets/audio/audio-manifest.placeholder.json");
  assert.equal(m.tracks.length, 4);
  const validRoles = new Set(["narration", "ambient", "mixed"]);
  const seen = new Set();
  for (const t of m.tracks) {
    assert.ok(validRoles.has(t.role), "valid role: " + t.sceneId);
    assert.equal(t.sourceLabel, "user-supplied-placeholder");
    assert.equal(t.sha256, sha256(t.sourcePath), "hash matches file: " + t.sceneId);
    assert.equal(t.reviewStatus, "pending-human-listening");
    seen.add(t.sceneId);
  }
  assert.deepEqual([...seen].sort(), [...IDS].sort(), "all four scenes covered");
});

test("transcripts remain available for every scene (independent of audio)", () => {
  for (const id of IDS) {
    const scene = readJson("content/" + id + ".json");
    assert.ok(scene.transcript && scene.transcript.sameOrigin === true && (scene.transcript.text || "").length > 0, "transcript present: " + id);
  }
});

test("no track is selected for release (all pending human listening)", () => {
  const m = readJson("assets/audio/audio-manifest.placeholder.json");
  for (const t of m.tracks) assert.notEqual(t.reviewStatus, "approved", "not released: " + t.sceneId);
});
