// PauseSpace player state machine (S12). Deterministic. Exit is always allowed
// from every active state (no forced completion). Invalid transitions return a
// safe error object {ok:false, code, message} and never throw.
const STATES = ["idle", "ready", "playing", "paused", "ended", "exited"];

// action -> next state, per current state
const NEXT = {
  idle: { prepare: "ready", exit: "exited", reset: "idle" },
  ready: { start: "playing", exit: "exited", reset: "idle" },
  playing: { pause: "paused", complete: "ended", exit: "exited", reset: "idle" },
  paused: { resume: "playing", complete: "ended", exit: "exited", reset: "idle" },
  ended: { replay: "ready", exit: "exited", reset: "idle" },
  exited: { reset: "idle" },
};

function err(code, message) {
  return { ok: false, code, message };
}

/** Create a fresh player in the idle state. */
export function createPlayer() {
  return { state: "idle", sceneId: null, segment: 0 };
}

/** True if `action` is allowed from `state`. */
export function canTransition(state, action) {
  return !!(NEXT[state] && action in NEXT[state]);
}

/** Apply an action to a player (mutates + returns a result object). Safe. */
export function transition(player, action) {
  if (!player || typeof player !== "object") return err("invalid_player", "player object required");
  if (!(player.state in NEXT)) return err("invalid_state", "unknown state: " + player.state);
  const map = NEXT[player.state];
  if (!(action in map)) return err("invalid_transition", "'" + action + "' not allowed in '" + player.state + "'");
  const from = player.state;
  player.state = map[action];
  if (action === "prepare" || action === "replay") player.segment = 0;
  return { ok: true, from, to: player.state };
}

export const PLAYER_STATES = STATES.slice();
