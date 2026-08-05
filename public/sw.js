// PauseSpace service worker (S17). Conservative app-shell cache: serve the shell
// offline, fall back to the network, handle missing assets safely, and never trap
// a new release behind a stale cache (versioned cache + skipWaiting + cleanup).
// Bump VERSION on each release to invalidate the cache.
/* global self, caches, fetch, Response */
const VERSION = "pausespace-v1";
const SHELL = ["/", "/index.html", "/styles.css", "/app.js"];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(VERSION)
      .then((cache) => cache.addAll(SHELL))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  // Delete caches from any previous version; do not trap a new release.
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== VERSION).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return; // only cache GETs

  // Cache-first for the shell; fall back to the network; offline navigation
  // serves the cached shell; other missing assets return a safe 503.
  event.respondWith(
    caches.match(req).then((cached) => {
      if (cached) return cached;
      return fetch(req).catch(() => {
        if (req.mode === "navigate") return caches.match("/index.html");
        return new Response("offline", { status: 503, statusText: "Offline" });
      });
    })
  );
});
