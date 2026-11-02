// Copies the khonnai app prototype (../khonnai-home-mvp) to public/app so the landing page can link to it.
// The prototype stays the single source; public/app is generated and git-ignored.
import { cpSync, existsSync, rmSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const source = resolve(root, "../khonnai-home-mvp");
const target = resolve(root, "public/app");

if (!existsSync(source)) {
  console.error(`sync-app: ${source} not found; the "เริ่มใช้ฟรี" links will 404.`);
  process.exit(1);
}
rmSync(target, { recursive: true, force: true });
cpSync(source, target, {
  recursive: true,
  filter: (path) => !/[\\/](verification|node_modules)([\\/]|$)/.test(path),
});
console.log("sync-app: copied khonnai-home-mvp → public/app");
