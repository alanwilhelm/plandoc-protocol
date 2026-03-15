# Design Doc Protocol

Design docs record architecture and decision truth. They do not track execution progress.

States:

- `Draft`
- `Active`
- `Archived`

Every design doc must include:

- Header with `State`, `Owner`, `Last Updated`
- `## Problem Statement`
- `## Constraints / Invariants`
- `## Options Considered`
- `## Decision`
- `## Consequences`
- `## Rollout / Migration`
- `## Security / Privacy Notes`

Local conventions:

- drafts live in `.plandoc/design/drafts/`
- adopted designs move to `.plandoc/design/active/`
- superseded designs move to `.plandoc/design/archived/`
- link each non-trivial plandoc to the design doc that defines its architecture
