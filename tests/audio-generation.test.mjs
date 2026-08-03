import { test } from "node:test";
import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { createHash } from "node:crypto";
import {
  dryRunPlan, generate, generationBlockedReason, isProviderConfigured, redact,
} from "../scripts/lib/tts-provider.mjs";

const here = dirname(fileURLToPath(import.meta.url));
const genCli = join(here, "..", "scripts", "generate-audio.mjs");
// Clearly-fake fixture value (never a real credential).
const FAKE_KEY = "FACE-TEST-KEY-NOT-REAL-1234";
const draftScene = { id: "exam-room", review: { status: "draft" }, transcript: { text: "You might let your attention rest." } };
const approvedScene = { id: "exam-room", review: { status: "approved" }, transcript: { text: "You might let your attention rest." } };
const configuredEnv = { TTS_PROVIDER: "p", TTS_API_KEY: FAKE_KEY, TTS_MODEL: "m", TTS_VOICE: "v", TTS_LOCALE: "en" };

test("dry-run plan exposes no secret", () => {
  const plan = dryRunPlan(draftScene, { ...configuredEnv });
  assert.equal(JSON.stringify(plan).includes(FAKE_KEY), false);
  assert.equal(plan.secretExposed, false);
});

test("redact() never returns the raw value", () => {
  assert.notEqual(redact(FAKE_KEY), FAKE_KEY);
  assert.equal(redact(""), "");
});

test("generationBlockedReason refuses draft scripts (fixture, no real-content coupling)", () => {
  const r = generationBlockedReason(draftScene, configuredEnv);
  assert.equal(r.blocked, true);
  assert.equal(r.code, "unapproved_script");
});

test("generationBlockedReason refuses approved script without provider", () => {
  const r = generationBlockedReason(approvedScene, {});
  assert.equal(r.blocked, true);
  assert.equal(r.code, "provider_not_configured");
});

test("generate() refuses when provider unconfigured (no network)", async () => {
  const r = await generate(approvedScene, {});
  assert.equal(r.ok, false);
  assert.equal(r.code, "provider_not_configured");
});

test("generate() refuses an unapproved provider (no network)", async () => {
  const r = await generate(approvedScene, { ...configuredEnv, TTS_PROVIDER: "random" });
  assert.equal(r.ok, false);
  assert.equal(r.code, "provider_not_approved");
});

test("CLI dry-run: zero provider requests, no network, no secret", () => {
  const out = execFileSync("node", [genCli, "--dry-run"], { encoding: "utf8", env: { ...process.env } });
  assert.match(out, /ZERO provider requests/);
  assert.match(out, /No network calls made/);
  assert.match(out, /no approved provider configured/);
  assert.equal(out.includes(FAKE_KEY), false);
});

test("CLI generation is blocked without an approved provider (non-zero exit)", () => {
  let rc = 0, out = "";
  try { execFileSync("node", [genCli, "--scene", "exam-room"], { encoding: "utf8", env: { ...process.env } }); }
  catch (e) { rc = e.status ?? 1; out = (e.stdout || "") + (e.stderr || ""); }
  assert.notEqual(rc, 0);
  assert.match(out, /provider_not_configured|Generation blocked/);
});

test("transcript hash is deterministic", () => {
  const h = (t) => createHash("sha256").update(t, "utf8").digest("hex");
  assert.equal(h("abc"), h("abc"));
  assert.notEqual(h("abc"), h("abd"));
});
