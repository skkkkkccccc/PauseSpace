import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { completionView, renderSupport, isSupportApproved, COMPLETION_ACTIONS } from "../src/views/Completion.js";

const support = JSON.parse(readFileSync(new URL("../content/support.json", import.meta.url), "utf8"));
const TITLES = ["Exam room", "Sports field", "Your own room", "Empty classroom"];

test("completion view offers return, replay, find-support, and exit for every scene", () => {
  for (const title of TITLES) {
    const html = completionView({ scene: { title }, support });
    for (const a of ["return", "replay", "find-support", "exit"]) {
      assert.match(html, new RegExp('data-action="' + a + '"'), title + " missing " + a);
    }
  }
});

test("exit/leave is always present (no forced completion)", () => {
  assert.match(completionView({ scene: { title: "X" }, support }), /data-action="exit"/);
});

test("completion actions are independent of tracking (no streak/score/rank)", () => {
  assert.ok(COMPLETION_ACTIONS.includes("return"));
  assert.ok(COMPLETION_ACTIONS.includes("replay"));
  const html = completionView({ scene: { title: "X" }, support });
  assert.doesNotMatch(html, /streak|score|rank/i);
});

test("support content is non-emergency and not yet approved (release blocked)", () => {
  assert.equal(support.reviewStatus, "pending-mentor-review");
  assert.equal(support.releaseBlocked, true);
  assert.equal(isSupportApproved(support), false);
  assert.match(support.boundary, /not emergency/i);
});

test("unapproved support is not shown in full (release blocked until mentor approval)", () => {
  const html = renderSupport(support);
  assert.match(html, /being reviewed/);
  assert.doesNotMatch(html, /mentor-approved-contact/); // placeholder contacts not rendered
});

test("approved support renders boundary + phrases + approved contacts only", () => {
  const approved = {
    reviewStatus: "approved", releaseBlocked: false,
    boundary: "PauseSpace is not emergency support.",
    phrases: [{ text: "You can stop at any time." }],
    contacts: [
      { label: "Counselor", value: "counselor@example.school", approved: true },
      { label: "Unapproved", value: "should-not-appear", approved: false },
    ],
  };
  const html = renderSupport(approved);
  assert.match(html, /not emergency support/);
  assert.match(html, /You can stop at any time/);
  assert.match(html, /counselor@example.school/);
  assert.doesNotMatch(html, /should-not-appear/); // unapproved contact excluded
});

test("missing support renders a safe message (no throw)", () => {
  assert.match(renderSupport(null), /not available/);
});

test("find-support toggles the support panel (aria-expanded)", () => {
  const off = completionView({ scene: { title: "X" }, support, showSupport: false });
  const on = completionView({ scene: { title: "X" }, support, showSupport: true });
  assert.match(off, /aria-expanded="false"/);
  assert.match(on, /aria-expanded="true"/);
  assert.match(on, /class="support/);
});
