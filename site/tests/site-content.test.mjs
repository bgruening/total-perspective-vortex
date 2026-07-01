import assert from "node:assert/strict";
import { existsSync, readFileSync } from "node:fs";
import { join } from "node:path";

const siteRoot = new URL("..", import.meta.url).pathname;
const pagePath = join(siteRoot, "src", "pages", "index.astro");
const cnamePath = join(siteRoot, "public", "CNAME");

assert.ok(existsSync(pagePath), "homepage source should exist");
assert.ok(existsSync(cnamePath), "CNAME should exist for the custom domain");

const page = readFileSync(pagePath, "utf8");
const cname = readFileSync(cnamePath, "utf8").trim();

assert.equal(cname, "tpv.galaxyproject.org");

[
  "Total Perspective Vortex",
  "right-sizing",
  "meta-scheduling",
  "usegalaxy",
  "Shared resource database",
  "Read the Docs",
  "GitHub",
  "Galaxy Training Network",
  "doi.org/10.1007/s42979-026-04947-0",
  "/tpv-logo-wide.png",
  "/job-dispatch-process.svg"
].forEach((text) => {
  assert.ok(page.includes(text), `homepage should include ${text}`);
});

