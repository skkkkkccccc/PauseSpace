import { test } from "node:test";
import assert from "node:assert/strict";
import { createPlayer, transition } from "../src/state/player.mjs";
import { MODES, DEFAULT_MODE, isValidMode, normalizeMode, toggleMode, modePicker } from "../src/components/ModePicker.js";
import { hasAudio, primaryAction, onBackground, onResume, audioPlayer } from "../src/components/AudioPlayer.js";

const scene = { durationSeconds: 180, audio: { sameOrigin: true, src: "assets/audio/exam-room.mp3" }, transcript: { text: "You might rest your attention." } };
const noAudio = { durationSeconds: 180, audio: { sameOrigin: false, src: "" }, transcript: { text: "x" } };

// --- viewing modes (reversible; never changes safety claims) ---
test("both viewing modes are valid, default eyes-open, and reversible", () => {
  assert.deepEqual(MODES, ["eyes-open", "eyes-closed"]);
  assert.equal(DEFAULT_MODE, "eyes-open");
  assert.equal(toggleMode("eyes-open"), "eyes-closed");
  assert.equal(toggleMode("eyes-closed"), "eyes-open");
  assert.equal(isValidMode("nope"), false);
  assert.equal(normalizeMode("nope"), "eyes-open");
});

test("mode picker renders both options, carries reduced-motion, and keeps the safety note in every mode", () => {
  for (const m of MODES) {
    const html = modePicker({ mode: m, reducedMotion: true });
    assert.match(html, /data-mode="eyes-open"/);
    assert.match(html, /data-mode="eyes-closed"/);
    assert.match(html, /data-reduced-motion="true"/);
    assert.match(html, /not diagnosis, treatment, counselling/); // safety claim unchanged by mode
  }
});

// --- player controls per state (no autoplay) ---
test("primary control is Play in idle/ready — user-initiated, no autoplay", () => {
  assert.equal(primaryAction("idle").action, "start");
  assert.equal(primaryAction("idle").label, "Play");
  assert.equal(primaryAction("ready").label, "Play");
});

test("primary control reflects each FSM state", () => {
  assert.equal(primaryAction("playing").action, "pause");
  assert.equal(primaryAction("paused").action, "resume");
  assert.equal(primaryAction("ended").action, "replay");
});

// --- rapid input keeps the control surface consistent ---
test("rapid transition sequence keeps controls consistent", () => {
  const p = createPlayer();
  const steps = [["prepare", "Play"], ["start", "Pause"], ["pause", "Resume"], ["resume", "Pause"], ["complete", "Replay"]];
  for (const [action, label] of steps) {
    transition(p, action);
    assert.equal(primaryAction(p.state).label, label);
  }
});

// --- missing audio -> error state, no play control ---
test("missing audio renders an error state with no start/play control", () => {
  const html = audioPlayer({ scene: noAudio, player: createPlayer() });
  assert.match(html, /audio-player--error/);
  assert.doesNotMatch(html, /data-action="start"/);
});

test("valid audio renders a Play (start) control — no autoplay", () => {
  const html = audioPlayer({ scene, player: createPlayer() });
  assert.match(html, /data-action="start"/);
  assert.match(html, /data-mode="eyes-open"/); // default mode
});

// --- keyboard path: every control is a real <button type="button"> with action/aria ---
test("every control is a keyboard-operable button", () => {
  const html = audioPlayer({ scene, player: createPlayer() });
  const buttons = html.match(/<button[^>]*>/g) || [];
  assert.ok(buttons.length >= 3);
  for (const b of buttons) {
    assert.match(b, /type="button"/);
    assert.match(b, /data-action=/);
    assert.match(b, /aria-label=/);
  }
});

// --- reset, background/resume ---
test("reset returns the FSM to idle", () => {
  const p = createPlayer(); transition(p, "prepare"); transition(p, "start");
  assert.equal(transition(p, "reset").to, "idle");
});

test("background pauses a playing scene; resume does NOT auto-resume", () => {
  const p = createPlayer(); transition(p, "prepare"); transition(p, "start");
  assert.equal(onBackground(p).to, "paused");
  const r = onResume(p);
  assert.equal(r.autoResumed, false);
  assert.equal(p.state, "paused"); // still paused — user must resume
});

// --- reduced-motion + exit ---
test("reduced-motion is carried on the player surface", () => {
  assert.match(audioPlayer({ scene, player: createPlayer(), reducedMotion: true }), /data-reduced-motion="true"/);
});

test("exit control is always rendered (no forced completion)", () => {
  assert.match(audioPlayer({ scene, player: createPlayer() }), /data-action="exit"/);
});

// --- no runtime TTS / no autoplay attribute ---
test("no autoplay attribute and no TTS call in the rendered player", () => {
  const html = audioPlayer({ scene, player: createPlayer() });
  assert.doesNotMatch(html, /autoplay/i);
  assert.doesNotMatch(html, /speechSynthesis|TextToSpeech|new Audio\(/);
});
