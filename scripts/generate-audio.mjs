// OA01 development-only narration generation CLI. Reads the four scene scripts,
// computes transcript hashes, plans generation (dry-run), and refuses to generate
// from draft/unapproved scripts or without an approved provider. It NEVER prints
// secrets and makes NO network call in dry-run or when unconfigured. No MP3 is
// written unless an approved generation actually succeeds.
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { createHash } from "node:crypto";
import { isProviderConfigured, APPROVED_PROVIDERS, generate } from "./lib/tts-provider.mjs";

const here = dirname(fileURLToPath(import.meta.url));
const root = join(here, "..");
const SCENES = ["exam-room", "sports-field", "own-room", "empty-classroom"];
const APPROVED_STATUS = new Set(["approved"]);

function loadScene(id) {
  return JSON.parse(readFileSync(join(root, "content", id + ".json"), "utf8"));
}
function transcriptHash(text) {
  return createHash("sha256").update(text || "", "utf8").digest("hex");
}
function parseArgs(argv) {
  const a = { dryRun: false, scene: null, preview: false };
  const args = argv.slice(2);
  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--dry-run") a.dryRun = true;
    else if (args[i] === "--preview") a.preview = true;
    else if (args[i].startsWith("--scene=")) a.scene = args[i].slice("--scene=".length);
    else if (args[i] === "--scene" && i + 1 < args.length) a.scene = args[++i];
  }
  return a;
}

async function main() {
  const opts = parseArgs(process.argv);
  const env = process.env;

  if (opts.dryRun) {
    console.log("OA01 dry-run: ZERO provider requests. No secret is read or printed.");
    let planned = 0, blocked = 0;
    for (const id of SCENES) {
      const scene = loadScene(id);
      const status = (scene.review && scene.review.status) || "<none>";
      const hash = transcriptHash(scene.transcript && scene.transcript.text);
      const approved = APPROVED_STATUS.has(status);
      planned += 1;
      console.log("- " + id + ": status=" + status + " approved=" + approved +
        " transcriptSha256=" + hash.slice(0, 12) + "… output=assets/audio/generated/" +
        id + "." + hash.slice(0, 8) + ".ai.mp3 estRequests=1");
      if (!approved) { blocked += 1; console.log("    -> BLOCKED: status '" + status + "'. OA01 refuses draft/unapproved content; will not generate."); }
    }
    console.log("Provider configured: " + isProviderConfigured(env) + " | approved-set size: " + APPROVED_PROVIDERS.size);
    console.log("Planned requests (would run only after preview approval): " + planned + " | blocked scripts: " + blocked);
    if (!isProviderConfigured(env) || APPROVED_PROVIDERS.size === 0)
      console.log("Scripts approved; generation still BLOCKED: no approved provider configured.");
    console.log("No network calls made. No MP3s written.");
    return;
  }

  if (!opts.scene) { console.error("Specify --scene <id> [--preview] or --dry-run"); process.exit(2); }
  const scene = loadScene(opts.scene);
  const result = await generate(scene, env);
  if (!result.ok) { console.error("Generation blocked (" + result.code + "): " + result.message + " No file written."); process.exit(1); }
  console.log("Generated:", JSON.stringify(result));
}

main().catch((e) => { console.error("OA01 error:", e && e.message); process.exit(1); });
