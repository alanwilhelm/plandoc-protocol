# Plandoc Protocol

Canonical source repo for the plandoc document protocol.

## Purpose

This repo defines the artifact and lifecycle rules for deterministic,
proof-backed work:

- design docs as architectural blueprint anchors
- plandocs as bounded execution docs
- audits and sweeps
- control-board artifact shape
- durable comm artifact shape
- GitHub issue intake and closeout rules
- cut, slice, and landing-slice vocabulary
- plan state transitions and review gates

## Repository Layout

- `protocol/` contains canonical protocol text that is independent of any
  agent harness. Start with `protocol/INDEX.md`.
- `codex/` contains Codex skill adapters.
- `hermes/` contains Hermes skill adapters.
- `templates/` contains reusable plandoc, design, review, and comm templates.
- `scripts/` contains repo-owned helper scripts.
- `tests/` contains checks for protocol packaging and sync behavior.

## Dependency Rule

This repo owns document protocol meaning. It must not depend on live workspace
orchestration, tmux panes, Codex worker lanes, Hermes worker lanes, or callback
queues. Those belong in `ctrl-protocol`.

If a question is about artifact shape, design anchors, plan sections, audit
behavior, durable comms, GitHub issue closeout, or proof-backed closure, answer
it here.

If a question is about live worker routing, tmux delivery, WIP, callback intake,
lane parking, or next legal move operation, answer it in `ctrl-protocol`.

## Runtime Install Policy

This repo is source of truth. Runtime installed copies are deploy targets.

Clean layout:

- source repo: `~/projects/skills-workspace/plandoc-protocol`
- Codex install target: `~/.codex/skills/<skill-name>`
- Hermes install target: `~/.hermes/skills/<category>/<skill-name>`

Do not make `~/.codex/repos/...` or `~/.hermes/...` the canonical source path
for this repo.

Preferred local-development install:

- symlink `codex/<skill-name>` into the Codex skill path
- symlink `hermes/<skill-name>` into the Hermes skill path
- link individual skill directories only
- do not symlink this whole repo into either runtime
- do not create nested source paths such as `~/.codex/repos/<repo>/skills/...`

Fallback install:

- use a checked sync script to copy adapter directories into runtime skill paths
  when symlinks are not appropriate

Any installer must preserve the canonical boundary: protocol meaning lives in
`protocol/`; Codex and Hermes directories are adapters.

Checked local linkers:

- `scripts/link-codex-adapters.sh`
- `scripts/link-hermes-adapters.sh`

Run linkers in `--mode plan` before `--mode apply`. The Hermes linker targets
`~/.hermes/skills/software-development`. Existing non-symlink Hermes skill
directories are not replaced unless `--replace-existing` is passed; replacement
moves the old directory aside with a timestamped backup name.

## Current Included Skills

Codex adapters:

- `plandoc-protocol`
- `plandocs-github`

Hermes adapters:

- `plandoc-protocol`
- `plandocs-github`
