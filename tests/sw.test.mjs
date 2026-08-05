// S17 service-worker tests. Runs public/sw.js in a mocked service-worker
// environment (via node:vm) and simulates install/activate/fetch events.
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import vm from "node:vm";

const SW_SOURCE = readFileSync(fileURLToPath(new URL("../public/sw.js", import.meta.url)), "utf8");

function loadSW(opts = {}) {
  const stores = opts.stores || new Map(); // cacheName -> Map(url -> res)
  let offline = !!opts.offline;
  const listeners = {};
  const toUrl = (r) => (typeof r === "string" ? r : r && r.url);
  const makeRes = (url, status) => ({ url, status, ok: (status || 200) < 400, statusText: (status || 200) === 200 ? "OK" : "Offline", text: () => Promise.resolve("body:" + url) });
  const Caches = {
    open(name) {
      if (!stores.has(name)) stores.set(name, new Map());
      const m = stores.get(name);
      return Promise.resolve({
        addAll(urls) { return Promise.all(urls.map((u) => { m.set(toUrl(u), makeRes(toUrl(u), 200)); })); },
        put(req, res) { m.set(toUrl(req), res); return Promise.resolve(); },
        match(req) { return Promise.resolve(m.get(toUrl(req))); },
      });
    },
    keys() { return Promise.resolve([...stores.keys()]); },
    delete(name) { stores.delete(name); return Promise.resolve(true); },
    match(req) { const u = toUrl(req); for (const m of stores.values()) if (m.has(u)) return Promise.resolve(m.get(u)); return Promise.resolve(undefined); },
  };
  const fetchImpl = (req) => (offline ? Promise.reject(new Error("offline")) : Promise.resolve(makeRes(toUrl(req), 200)));
  const self = {
    addEventListener(type, fn) { listeners[type] = fn; },
    skipWaiting() { self._skipped = true; return Promise.resolve(); },
    clients: { claim() { self._claimed = true; return Promise.resolve(); } },
  };
  const ResponseCtor = function (body, init) { init = init || {}; return { status: init.status || 200, statusText: init.statusText || "OK", ok: (init.status || 200) < 400, text: () => Promise.resolve(String(body)) }; };
  const ctx = { self, caches: Caches, fetch: fetchImpl, Response: ResponseCtor, console };
  vm.createContext(ctx);
  let src = SW_SOURCE;
  if (opts.versionOverride) src = src.replace(/const VERSION = "[^"]*"/, 'const VERSION = "' + opts.versionOverride + '"');
  vm.runInContext(src, ctx);
  function fire(type, request) {
    const req = typeof request === "string" ? { url: request, method: "GET", mode: "navigate" } : request;
    const ev = { request: req };
    let waited = null, responded = null;
    ev.waitUntil = (p) => { waited = p; };
    ev.respondWith = (p) => { responded = p; };
    if (listeners[type]) listeners[type](ev);
    return { waited, responded };
  }
  return { stores, fire, setOffline: (v) => { offline = !!v; }, self };
}

test("first load / install caches the app shell + skipWaiting", async () => {
  const sw = loadSW();
  await sw.fire("install").waited;
  const cache = [...sw.stores.values()][0];
  assert.ok(cache, "a cache was created");
  for (const url of ["/", "/index.html", "/styles.css", "/app.js"]) assert.ok(cache.has(url), "cached " + url);
  assert.equal(sw.self._skipped, true);
});

test("second load: install keeps the cache (idempotent)", async () => {
  const sw = loadSW();
  await sw.fire("install").waited;
  await sw.fire("install").waited;
  assert.ok([...sw.stores.values()][0].has("/index.html"));
});

test("offline: previously-loaded shell is served", async () => {
  const sw = loadSW();
  await sw.fire("install").waited; // online: cache the shell
  sw.setOffline(true);
  const res = await sw.fire("fetch", { url: "/", method: "GET", mode: "navigate" }).responded;
  assert.ok(res && res.status === 200, "served cached shell offline");
});

test("missing asset offline returns a safe 503 (no throw)", async () => {
  const sw = loadSW();
  await sw.fire("install").waited;
  sw.setOffline(true);
  const res = await sw.fire("fetch", { url: "/missing-asset.png", method: "GET", mode: "no-cors" }).responded;
  assert.equal(res.status, 503);
});

test("update: a new release is not trapped — old cache cleared, new present, clients.claim", async () => {
  const shared = new Map();
  const sw1 = loadSW({ stores: shared });
  await sw1.fire("install").waited;
  assert.ok(shared.has("pausespace-v1"));
  const sw2 = loadSW({ stores: shared, versionOverride: "pausespace-v2" });
  await sw2.fire("install").waited;
  await sw2.fire("activate").waited;
  assert.equal(shared.has("pausespace-v1"), false, "old version cache cleared");
  assert.ok(shared.has("pausespace-v2"), "new version cache present");
  assert.equal(sw2.self._claimed, true);
});

test("non-GET requests are ignored by the fetch handler", async () => {
  const sw = loadSW();
  await sw.fire("install").waited;
  const r = sw.fire("fetch", { url: "/x", method: "POST", mode: "navigate" });
  assert.equal(r.responded, null); // handler returned early
});
