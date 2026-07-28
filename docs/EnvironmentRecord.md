# Environment Record

Recorded as part of the PauseSpace workspace kickoff audit. Only tools actually
detected on the machine are listed; missing tools are noted as "Not available"
rather than estimated.

- **Collected:** 2026-07-28
- **Method:** direct version checks run in this session (`uname`, `sw_vers`,
  `--version` flags, `defaults read` on installed app bundles, env inspection).

## Detected versions

| Component       | Version                                  | Source / notes |
|-----------------|------------------------------------------|----------------|
| Operating system| macOS 26.2 (Build 25C56)                 | `sw_vers`. Darwin kernel 25.2.0, `arm64` (Apple Silicon). Shell `zsh` 5.9. |
| Editor          | Cursor 3.13.10 (VS Code-based)           | App bundle `defaults read`; session env `TERM_PROGRAM=vscode`, `TERM_PROGRAM_VERSION=3.13.10`. Visual Studio Code.app is **not** installed. |
| Git             | 2.50.1 (Apple Git-155)                   | `git --version`. Repo on branch `main`, clean, tracking `origin/main`. |
| Node.js         | v24.18.0                                 | `node --version`. |
| npm             | 11.16.0                                  | `npm --version`. |
| Browser         | Safari 26.2; Google Chrome 150.0.7871.187| App bundle `defaults read`. |
| Coding agent    | Claude Code 2.1.220                      | `claude --version`. |

## Checked and not available

- **Editor CLIs:** neither `code` nor `cursor` is on the `PATH` (only the app
  bundles are installed). Shell-out editor commands may need the CLI enabled.
- **Browsers:** Microsoft Edge and Firefox are **not** installed. The mobile-first
  test plan will need additional device/browser coverage before release.
- **No application runtime yet:** there is no `package.json`, `node_modules/`,
  `dist/`, or `index.html` in the tree. This is expected at kickoff — the
  static HTML/CSS/JS repository is introduced in a later session, and S01 has not
  started.

## Privacy note

A scan of all tracked and untracked text files (excluding `.git` and
`node_modules`) found **no** real secrets, API keys, tokens, credentials, or
identifying participant data. All pattern matches were policy wording inside
project and prompt files (for example "No secrets, credentials…").
