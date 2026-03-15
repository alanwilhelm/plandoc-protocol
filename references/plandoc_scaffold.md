# Optional Local Plandoc Scaffold

Use this when a repository wants a local `.plandoc/` operating layer instead of relying only on the global skill.

This does not create a second protocol. It installs a repo-local copy of the same protocol shape.

Run:

```bash
python3 scripts/install_plandoc_scaffold.py --repo-root /path/to/repo --project-name MyProject
```

Add `--force` to overwrite existing managed files under `.plandoc/`.

The installer writes:

- `.plandoc/README.md`
- `.plandoc/plans/README.md`
- `.plandoc/plans/_index.md`
- `.plandoc/design/README.md`
- `.plandoc/design/_index.md`
- canonical `.plandoc/plans/*` lifecycle folders
- canonical `.plandoc/design/*` lifecycle folders

It also patches:

- `AGENTS.md`
- `CLAUDE.md`

with short managed blocks that point those entrypoints to `.plandoc/README.md`.

The scaffold is optional. Use it only when a repo actually wants local planning state and local protocol docs.
