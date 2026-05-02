# Optional Local Plandoc Scaffold

Use this when a repository wants a local `.plandoc/` operating layer instead of relying only on the global skill.

This does not create a second protocol. It installs a repo-local copy of the same protocol shape.

Run:

```bash
python3 scripts/install_plandoc_scaffold.py --repo-root /path/to/repo --project-name MyProject
```

Add `--force` to overwrite existing managed files under `.plandoc/`.

Operational checklist:

1. Verify whether `.plandoc/` already exists before installing.
2. Check `git status --short` so scaffold changes are not confused with pre-existing dirty work.
3. Read local schema/entrypoint files such as `README.md`, `AGENTS.md`, and `CLAUDE.md` when they exist so the first design docs match the project’s current conventions.
4. Run the installer with `--dry-run` first and inspect the planned writes/patches.
5. Run the installer without `--dry-run` only after the planned scaffold scope is understood.
6. Read back `.plandoc/README.md`, `.plandoc/design/_index.md`, and any patched entrypoint files to verify the scaffold landed.
7. If seeding design docs for architecture that is already adopted on disk, place them in `.plandoc/design/active/` with `State: Active`; use `drafts/` only for unresolved proposals.
8. Update `.plandoc/design/_index.md` immediately after adding design docs.
9. Run a simple structural verification: required scaffold directories exist, every active design doc has the required design sections, and every active design doc is indexed.

The installer writes:

- `.plandoc/README.md`
- `.plandoc/plans/README.md`
- `.plandoc/plans/_index.md`
- `.plandoc/design/README.md`
- `.plandoc/design/_index.md`
- `.plandoc/reviews/README.md`
- `.plandoc/comms/README.md`
- `.plandoc/comms/templates/message.md`
- canonical `.plandoc/plans/*` lifecycle folders
- canonical `.plandoc/design/*` lifecycle folders
- canonical `.plandoc/reviews/` review-artifact folder
- canonical `.plandoc/comms/open|acked|closed|templates/` coordination folders

It also patches:

- `AGENTS.md`
- `CLAUDE.md`

with short managed blocks that point those entrypoints to `.plandoc/README.md`.

The scaffold is optional. Use it only when a repo actually wants local planning state and local protocol docs.
