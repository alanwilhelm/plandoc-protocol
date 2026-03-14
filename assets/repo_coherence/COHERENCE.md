# Coherence

This repository uses a repo-local control stack to keep plandoc behavior stable.

The result does not come from one file. It comes from the combined effect of:

- [AGENTS.md](AGENTS.md)
- [docs/plans/README.md](docs/plans/README.md)
- [docs/design/README.md](docs/design/README.md)
- [docs/plans/_index.md](docs/plans/_index.md)
- [docs/design/_index.md](docs/design/_index.md)
- one active umbrella milestone plandoc
- one or more current design docs that state architecture truth
- [VOCABULARY.md](VOCABULARY.md)
- [SURFACE_MATRIX.md](SURFACE_MATRIX.md)

## Required Rules

1. Every non-trivial effort gets a plandoc or design doc before broad implementation churn.
2. Every plandoc is anchored in one explicit `Status` + `State`.
3. Folder placement, header, and `## Implementation Log` must agree.
4. `_index.md` must be updated when plan or design state changes.
5. Design docs define architecture truth; plandocs execute against that truth.
6. Verification is part of closure, not optional cleanup.
7. After green verification, resolve the plan and commit the checkpoint.
8. Seed the next bounded concern before restarting broad churn.

## Control Documents

### [AGENTS.md](AGENTS.md)

Defines the repo identity, writing standard, naming discipline, and local operating rules.

### [docs/plans/README.md](docs/plans/README.md)

Defines the plandoc lifecycle, required sections, and local execution conventions.

### [docs/design/README.md](docs/design/README.md)

Defines the design-doc lifecycle and keeps architecture truth separate from execution state.

### [docs/plans/_index.md](docs/plans/_index.md) and [docs/design/_index.md](docs/design/_index.md)

Provide one current map of active, todo, and resolved work.

### [VOCABULARY.md](VOCABULARY.md)

Keeps terminology stable.

### [SURFACE_MATRIX.md](SURFACE_MATRIX.md)

Keeps ownership and boundary expectations visible.

## Bootstrap Set

Install at least:

- `AGENTS.md`
- `COHERENCE.md`
- `VOCABULARY.md`
- `SURFACE_MATRIX.md`
- `docs/plans/README.md`
- `docs/plans/_index.md`
- `docs/plans/todo/`
- `docs/plans/active/`
- `docs/plans/qa/`
- `docs/plans/resolved/`
- `docs/plans/icebox/`
- `docs/plans/templates/`
- `docs/design/README.md`
- `docs/design/_index.md`
- `docs/design/drafts/`
- `docs/design/active/`
- `docs/design/archived/`
- `docs/design/templates/`

## Recreate Exactly

To recreate this shape in another repo:

1. install the scaffold
2. customize `AGENTS.md` for `{{PROJECT_NAME}}`
3. seed one umbrella milestone plandoc
4. seed at least one design doc that states current architecture truth
5. keep the indices aligned with the actual lifecycle state
6. treat the docs as execution control, not commentary
