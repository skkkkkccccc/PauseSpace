import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { sceneCard } from "../src/components/SceneCard.js";
import { homeView } from "../src/views/home.js";
import { sceneDetailView } from "../src/views/scene-detail.js";
import { escapeHtml } from "../src/views/escape-html.js";

const IDS = ["exam-room", "sports-field", "own-room", "empty-classroom"];
const read = (id) => JSON.parse(readFileSync(new URL("../content/" + id + ".json", import.meta.url), "utf8"));
const scenes = IDS.map(read);

test("four cards render from data, each with title + open control", () => {
  for (const s of scenes) {
    const html = sceneCard(s);
    assert.match(html, new RegExp(s.title.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")));
    assert.match(html, /data-scene="/);
    assert.match(html, /<button[^>]*>Open<\/button>/);
  }
});

test("homeView renders all four cards from data (no error state)", () => {
  const html = homeView(scenes);
  for (const s of scenes) assert.match(html, new RegExp(s.title.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")));
  assert.equal((html.match(/class="scene-card"/g) || []).length, 4);
  assert.doesNotMatch(html, /state--error/);
});

test("no scene-specific copy is hard-coded in view/component source", () => {
  const files = ["../src/components/SceneCard.js", "../src/views/home.js", "../src/views/scene-detail.js"];
  const blob = files.map((f) => readFileSync(new URL(f, import.meta.url), "utf8")).join("\n");
  for (const bad of ["Exam room", "exam-room", "Sports field", "sports-field", "Own room", "own-room", "Empty classroom", "empty-classroom"]) {
    assert.equal(blob.includes(bad), false, "view source hard-codes scene copy: " + bad);
  }
});

test("malformed content fails visibly (error state, no throw)", () => {
  const bad = { ...scenes[0], id: "broken", durationSeconds: 9999 };
  const home = homeView([bad]);
  assert.match(home, /state--error/);
  const detail = sceneDetailView(bad);
  assert.match(detail, /could not be shown/);
});

test("empty state when there are no scenes", () => {
  const html = homeView([]);
  assert.match(html, /state--empty/);
  assert.doesNotMatch(html, /scene-card/);
});

test("safe text insertion (escaping)", () => {
  assert.equal(escapeHtml("<b>"), "&lt;b&gt;");
  const html = sceneCard({ id: "x", title: "<script>x</script>", moment: null, durationSeconds: 120 });
  assert.equal(html.includes("<script>"), false);
});

test("detail shows audio metadata but no playback element (no runtime audio/TTS)", () => {
  const html = sceneDetailView(scenes[0]);
  assert.match(html, /Audio:/);
  assert.doesNotMatch(html, /<audio/);
  assert.doesNotMatch(html, /tts/i);
});
