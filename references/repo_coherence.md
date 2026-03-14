# Repo Coherence Bootstrap

Use this when a repository needs the same kind of plandoc discipline that `ironfang` achieved:

- repo-local protocol docs
- explicit lifecycle folders and indices
- a root `COHERENCE.md`
- root control docs that reinforce naming, ownership, and vocabulary

Run:

```bash
python3 scripts/install_repo_coherence.py --repo-root /path/to/repo --project-name MyProject
```

Add `--force` to overwrite the managed scaffold files.

The installer writes:

- `COHERENCE.md`
- `AGENTS.md`
- `VOCABULARY.md`
- `SURFACE_MATRIX.md`
- `docs/plans/README.md`
- `docs/plans/_index.md`
- `docs/design/README.md`
- `docs/design/_index.md`
- canonical `docs/plans/*` lifecycle folders
- canonical `docs/design/*` lifecycle folders

After install, do not stop at the scaffold. To get real coherence:

1. customize `AGENTS.md` for the repo identity, codebase boundary, and style rules
2. seed an umbrella milestone plandoc
3. seed the first design doc that states current architectural truth
4. keep the index files aligned with actual plan/design state
5. treat the docs as execution control, not narration

Do not present the scaffold alone as sufficient. The result depends on the operating behavior as
much as the files.
