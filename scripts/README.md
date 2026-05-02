# Scripts

Repo-owned plandoc-protocol helper scripts live here.

- `link-codex-adapters.sh` links `codex/<skill-name>` adapters into
  `${CODEX_HOME:-$HOME/.codex}/skills`.
- `link-hermes-adapters.sh` links `hermes/<skill-name>` adapters into
  `${HERMES_HOME:-$HOME/.hermes}/skills/software-development`.

Run scripts with `--mode plan` before `--mode apply`.

Hermes linking refuses to replace existing non-symlink skill directories unless
`--replace-existing` is passed. Replacement moves the old directory aside before
creating the symlink.
