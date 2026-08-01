// PauseSpace lint (S11). Zero-dependency. Scans the app source for content that
// would breach the static, secret-free, non-diagnostic, tracker-free boundary.
import { readFileSync } from "node:fs";

const FILES = ["../../src/index.html", "../../src/styles.css", "../../src/app.js"];
const FORBIDDEN = [
  { re: /password|api[_-]?key|bearer|authorization\s*:|-----BEGIN|AKIA[0-9A-Z]{16}/i, why: "possible secret/credential" },
  { re: /https?:\/\/(?!localhost|127\.0\.0\.1)(?!example\.)/i, why: "external URL (not allowed in static app)" },
  { re: /google-analytics|gtag\(|googletagmanager|fetch\s*\(\s*['"]https?:\/\//i, why: "tracker / external network call" },
  { re: /treatment of|cures |therapeutic relief|will heal|medicinal use/i, why: "medical / therapeutic claim" },
];

let bad = 0;
for (const f of FILES) {
  const txt = readFileSync(new URL(f, import.meta.url), "utf8");
  for (const { re, why } of FORBIDDEN) {
    const m = txt.match(re);
    if (m) {
      console.error(`LINT FAIL  ${f.replace(/^..\/..\//, "")}: ${why} -> "${m[0]}"`);
      bad++;
    }
  }
}
if (bad) {
  console.error(`\n${bad} lint problem(s) found.`);
  process.exit(1);
}
console.log("lint: clean — no secrets, external URLs, trackers, or medical claims in src.");
