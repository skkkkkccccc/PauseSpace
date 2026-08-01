// PauseSpace build (S11). Zero-dependency. Copies the app files to dist/.
import { cpSync, mkdirSync, rmSync, existsSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const here = dirname(fileURLToPath(import.meta.url));
const root = join(here, "..", "..");
const src = join(root, "src");
const dist = join(root, "dist");
const APP_FILES = ["index.html", "styles.css", "app.js"];

if (existsSync(dist)) rmSync(dist, { recursive: true, force: true });
mkdirSync(dist, { recursive: true });
for (const f of APP_FILES) cpSync(join(src, f), join(dist, f));

console.log(`build: copied src/{${APP_FILES.join(",")}} -> dist/ (${APP_FILES.length} files)`);
