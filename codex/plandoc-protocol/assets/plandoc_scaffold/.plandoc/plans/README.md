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
3. `## Outcome`
4. `## Deliverables`
5. `## Goals / Non-Goals`
6. `## Current Behavior`
7. `## Proposed Approach`
8. `## Landing Slice / Stopping Point`
9. `## Deferred / Not In This Slice`
10. `## Implementation Plan`
11. `## Acceptance Criteria`
12. `## Verification & Monitoring`
13. `## Rollback`
14. `## Invariants / Non-Negotiables`
15. `## Risks / Open Questions`
16. `## Resolution`
17. `## Implementation Log`

Local conventions:

- number plandocs sequentially within this workspace
- keep active execution docs out of the root; use the lifecycle folders
- treat `.plandoc/` as the local protocol source of truth over generic memory
- add a `Deep refine:` entry before approval for non-trivial work
- use `.plandoc/comms/` for durable cross-owner handoffs when needed

Control-board note:

- a control board is an official plandoc-protocol coordination artifact, not a
  separate plan type
- use one only when this repo or workspace is actively managing multiple lanes
