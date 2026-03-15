# Plandoc Protocol

This repo uses the canonical plandoc lifecycle:

- `Todo + Seeded|Refined|Approved`
- `Active + Implementing`
- `QA + Implemented|Reviewed`
- `Resolved + Resolved`
- `Blocked + Seeded|Refined|Approved|Implementing|Implemented|Reviewed`
- `Icebox + Seeded|Refined|Approved`

Every plandoc must include:

1. Header with `Status`, `State`, `Type`, `Priority`, `Owner`, `Links`, `Created`
2. `## Context`
3. `## Goals / Non-Goals`
4. `## Current Behavior`
5. `## Proposed Approach`
6. `## Implementation Plan`
7. `## Acceptance Criteria`
8. `## Verification & Monitoring`
9. `## Rollback`
10. `## Risks / Open Questions`
11. `## Implementation Log`

Local conventions:

- number plandocs sequentially within this workspace
- keep active execution docs out of the root; use the lifecycle folders
- treat `.plandoc/` as the local protocol source of truth over generic memory
- add a `Deep refine:` entry before approval for non-trivial work
