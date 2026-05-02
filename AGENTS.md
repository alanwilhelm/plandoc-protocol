# Plandoc Protocol Agent Guide

Read `README.md` before editing. It defines this repo's boundary and install
policy.

This repo is the canonical source for plandoc artifact and lifecycle meaning.

Rules:

- Keep canonical protocol meaning in `protocol/`.
- Start protocol edits from `protocol/INDEX.md`.
- Keep Codex-specific packaging under `codex/`.
- Keep Hermes-specific packaging under `hermes/`.
- Keep this source repo under `~/projects/skills-workspace/plandoc-protocol`,
  not under a runtime-owned `repos/skills` tree.
- Do not add tmux pane control, worker routing, callback queues, or live
  workspace orchestration here.
- If adapter wording changes protocol meaning, update `protocol/` first.
- There is no separate rest-audit skill. Canonical audit behavior belongs in
  `protocol/audit.md` and the main `plandoc-protocol` adapter.
- Runtime skill directories are install targets, not source of truth.
- Prefer symlink installers for individual adapter skill directories, with a
  copy/sync fallback for runtimes that do not tolerate symlinks.
