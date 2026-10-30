import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { test } from "node:test";

test("Windows CLI reports a missing Java executable and removes its scratch folders", { skip: process.platform !== "win32" }, () => {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), "statechart-win-"));
  const cli = path.resolve(import.meta.dirname, "../statechart.ts");
  const spec = path.join(root, "Check.tla");
  fs.writeFileSync(spec, "---- MODULE Check ----\n====\n");
  fs.writeFileSync(path.join(root, "Check.cfg"), "INIT Init\nNEXT Next\n");
  try {
    const r = spawnSync(process.execPath, [cli, spec, "--out", path.join(root, "out")], {
      encoding: "utf8", windowsHide: true, timeout: 15000,
      env: { ...process.env, TEMP: root, TMP: root, TLA2TOOLS: path.join(root, "missing.jar"), JAVA: path.join(root, "missing-java.exe") },
    });
    assert.equal(r.error, undefined);
    assert.equal(r.status, 2, r.stderr);
    assert.match(r.stderr, /missing-java\.exe ENOENT/);
    assert.doesNotMatch(r.stderr, /\/bin\/sh|Unhandled/);
    assert.deepEqual(fs.readdirSync(root).sort(), ["Check.cfg", "Check.tla"]);
  } finally {
    fs.rmSync(root, { recursive: true, force: true });
  }
});
