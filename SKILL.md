---
name: plandoc-protocol
description: High-effectiveness Plandoc + Design Doc protocol for planning, deep-refining, refiling legacy doc spaces, and executing plan state transitions with approval gates.
---

# Plandoc Protocol (Optimized)

## Goal
Maximize delivery correctness and coordination with minimal bureaucracy.

This protocol is a state machine for work, backed by structured docs:

- Plandocs = execution docs
- Design docs = architecture / strategy / decision docs

## Use This Skill When

- the user wants a new plan, design doc, or protocol sync
- a repo has legacy docs that need to be refactored into a cleaner plan/design layout
- work is large, risky, multi-step, or needs auditability
- a plan needs review, refinement, activation, implementation, verification, or state movement

## Prime Directive

- Prefer provable correctness over speed when risk is real.
- Prefer speed when work is low-risk and reversible.
- Every required section must be filled or explicitly `N/A — reason`.

## Execution Standard

- The default intent is to advance each plandoc all the way to finish, not leave it drifting between stages.
- Advancement must be earned with absolute discipline, not optimism or convenience.
- Anchor every plandoc in a single explicit stage so the current position and next valid move are deterministic.
- Apply meticulous attention to detail in structure, wording, style, and technical correctness.
- Use full-spectrum analysis: current state, root problem, constraints, risks, solution shape, verification, rollback, and follow-through.
- Do not blur plan state, implementation state, design intent, or evidence.
- Do not mark a plan as more complete, more certain, or more correct than the underlying evidence supports.

## Source Of Truth

1. Repo-local protocol docs if present:
   - `docs/plans/README.md`
   - `docs/design/README.md`
2. Otherwise use this skill’s defaults.

If repo-local rules conflict with this skill, follow the repo-local rules unless the user asks to change the protocol itself.

## Classify First

Before editing or moving docs, classify each artifact:

- Put it in `docs/plans/` if it is primarily about execution state, verification, sequencing, and delivery.
- Put it in `docs/design/` if it is primarily about architecture, strategy, constraints, or decisions.

Do not leave active plandocs directly in `docs/plans/` root unless repo-local protocol explicitly says so.

## Folder Layout (Canonical)

### Plandocs

- `docs/plans/todo/NNNN-...md`
- `docs/plans/active/NNNN-...md`
- `docs/plans/qa/NNNN-...md`
- `docs/plans/resolved/NNNN-...md`
- `docs/plans/icebox/NNNN-...md`
- `docs/plans/templates/`
- `docs/plans/_index.md`

### Design docs

- `docs/design/drafts/NNNN-...md`
- `docs/design/active/NNNN-...md`
- `docs/design/archived/NNNN-...md`
- `docs/design/templates/`
- `docs/design/_index.md`

## States + Transitions

### Use Both `Status` And `State`

`Status` answers where the doc lives in the lifecycle.

Allowed plandoc `Status` values:

- `Todo`
- `Active`
- `QA`
- `Resolved`
- `Blocked`
- `Icebox`

`State` answers the exact workflow stage.

Allowed plandoc `State` values:

- `Seeded`
- `Refined`
- `Approved`
- `Implementing`
- `Implemented`
- `Reviewed`
- `Resolved`

### Allowed `Status` + `State` Combinations

- `Todo` + `Seeded|Refined|Approved`
- `Active` + `Implementing`
- `QA` + `Implemented|Reviewed`
- `Resolved` + `Resolved`
- `Blocked` + `Seeded|Refined|Approved|Implementing|Implemented|Reviewed`
- `Icebox` + `Seeded|Refined|Approved`

Do not invent custom values.

### Stage Anchoring (Required)

Every plandoc must be anchored in exactly one current stage.

- Do not leave a plandoc "between stages" or implied by prose alone.
- The header `Status` + `State`, folder placement, and `## Implementation Log` must agree.
- A stage transition is not complete until the doc itself records it.
- If the evidence does not support the next stage, keep the plandoc where it is.

Stage definitions and minimum requirements:

- `Seeded`
  - Purpose: capture the work item correctly enough to exist in the system.
  - Minimum: required header present, problem/context stated, initial goals/non-goals stated, next refinement needs visible.
  - Not yet true: execution readiness.

- `Refined`
  - Purpose: make the plandoc materially more trustworthy than the initial seed.
  - Minimum: relevant source-of-truth docs reviewed, current behavior separated from intended behavior, touch points identified, risks/verification/rollback drafted.
  - Not yet true: approved for activation.

- `Approved`
  - Purpose: mark the plandoc as ready for activation.
  - Minimum: plan review completed, implementation shape coherent, acceptance criteria clear, major open questions either resolved or explicitly bounded.
  - Not yet true: substantial code edits. If code changes are non-trivial, the separate implementation approval gate still applies.

- `Implementing`
  - Purpose: active execution against an approved plan.
  - Minimum: plandoc moved to `Active`, execution scope is explicit, intended touch points/tests/verification path are known, implementation work is being carried out or is ready to begin immediately.
  - Requirement while in stage: log meaningful execution progress; do not claim implementation completion early.

- `Implemented`
  - Purpose: implementation is complete enough to enter verification.
  - Minimum: planned code/docs/test changes landed, no known required implementation work remains for the scoped acceptance criteria, verification can now judge the result.
  - Not yet true: accepted and resolved.

- `Reviewed`
  - Purpose: implementation and evidence have been reviewed against the plan.
  - Minimum: verification results captured, acceptance criteria assessed explicitly, remaining issues either absent or severe enough to return the plan to `Active + Implementing`.
  - Not yet true: resolved historical record.

- `Resolved`
  - Purpose: close the plan as complete or conclusively finished.
  - Minimum: final state is supported by evidence, the plandoc has a stable historical record, and no further action is implied unless reopened.

Required transition mechanics:

- update `Status` and `State`
- move the file to the correct lifecycle folder when required
- add an `## Implementation Log` entry naming the transition
- keep `_index.md` aligned if the repo uses an index
- do not skip stage requirements just because the intended next step is obvious

### Canonical Next-Step Rules

When the user says "do the next thing", use this table:

- `Todo + Seeded` -> `refine-plan`
- `Todo + Refined` -> `review-plan`
- `Todo + Approved` -> `activate-plan`
- `Active + Implementing` -> `implement-plan`
- `QA + Implemented` -> `review-implementation`
- `QA + Reviewed` -> `resolve-plan`
- `Blocked + <any>` -> unblock first; do not guess
- `Resolved + Resolved` -> no further action unless the plan is reopened

### Canonical Transition Rules

- `seed-plan` -> `Todo + Seeded`
- `refine-plan` -> `Todo + Refined`
- `review-plan` -> either stay `Todo + Refined` with findings or move to `Todo + Approved`
- `activate-plan` -> `Active + Implementing`
- `implement-plan`
  - stays `Active + Implementing` while work remains
  - moves to `QA + Implemented` when implementation is ready for verification
- `review-implementation`
  - stays or returns to `Active + Implementing` if fixes are required
  - moves to `QA + Reviewed` when evidence supports acceptance
- `resolve-plan` -> `Resolved + Resolved`

### Doc-Only Exception

For research, protocol sync, or docs-only work with no implementation phase:

- allowed flow: `Seeded -> Refined -> Approved -> Resolved`
- `resolve-plan` may move `Todo + Approved` directly to `Resolved + Resolved` if verification is captured inline
- record clearly in `## Verification & Monitoring` why no implementation/QA phase exists

### Design doc states

- `Draft` -> proposed or exploratory
- `Active` -> current adopted design
- `Archived` -> historical or superseded

## Evidence Minimum

For any change beyond trivial:

- verification steps: exact commands + expected results
- rollback: safe revert path
- risks: what can break and blast radius

## Deep Refine (Required For Non-Trivial Work)

Run a deep refine before:

- cross-cutting plan/design space refiles
- large or risky implementation plans
- architecture changes
- compatibility or packaging work
- any task where stale docs may mislead execution

Deep refine minimum:

1. Read the current source of truth docs first.
2. Audit the relevant code/docs/tests, not just the existing plan text.
3. Separate current behavior from intended behavior.
4. Identify actual touch points and stale assumptions.
5. Reclassify artifacts as plan vs design where needed.
6. Record a canonical `Deep refine:` entry in the relevant plan `## Implementation Log`.

For legacy doc-space refiles, the deep refine should answer:

- which files are execution plans
- which files are design docs
- which files are current vs historical
- which states are supported by the evidence on disk

Do not invent completion state or certainty that the docs do not support.

## Approval Gates

Before any substantial code edits under a plandoc:

- produce an Implementation Overview covering:
  - what / why
  - touch points
  - tests to add or modify
  - verification plan
  - rollout / flags / migrations
  - risks + rollback
- wait for explicit approval

Docs-only refactors do not require a code-implementation approval gate, but they still require a deep refine when cross-cutting.

## Minimal Templates

### Plandoc required sections

1. Header (`Status`, `State`, `Type`, `Priority`, `Owner`, `Links`, `Created`)
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

### Design doc required sections

1. `## Problem Statement`
2. `## Constraints / Invariants`
3. `## Options Considered`
4. `## Decision`
5. `## Consequences`
6. `## Rollout / Migration`
7. `## Security / Privacy Notes`

## Legacy Refile Workflow

When refiling an existing docs space:

1. Inventory all current docs under `docs/plans/` and `docs/design/`.
2. Classify each file as plandoc vs design doc.
3. Preserve numbering when it helps trace history.
4. Move files into state folders, not root, unless repo-local rules say otherwise.
5. Rewrite docs to current protocol shape instead of only adding headers when the old structure is misleading.
6. Add or update repo-local `README.md` protocol docs if the repo has none.
7. Add or update `_index.md` files so the resulting layout is navigable.
8. Keep historical intent, but align wording with current architecture and current evidence.

## Staged Workflow

Default staged flow:

`seed -> refine -> review -> activate -> implement -> review -> resolve`

- `seed` = create the first correct plan or design doc in the right folder and state
- `refine` = deepen or clean up an existing plan/design doc after reading the relevant sources
- first `review` = review the plan/design for readiness
- `activate` = preflight + move `Todo + Approved -> Active + Implementing`
- `implement` = execute the approved plan
- second `review` = review implementation and evidence
- `resolve` = move the plan to `Resolved + Resolved`

Use `sync-protocol` when the task is about the protocol itself, templates, indexes, or refiling the doc space.

## Operational Verbs

Use these verbs exactly in prompts:

- `seed-plan` = create a new plandoc in the correct state folder with the minimum correct structure
- `seed-design` = create a new design doc in the correct design folder with the minimum correct structure
- `refine-plan` = enrich or restructure an existing plandoc without implementation
- `refine-design` = enrich or restructure an existing design doc without implementation
- `review-plan` = review a plandoc for readiness, gaps, and protocol compliance
- `activate-plan` = preflight + move `Todo + Approved -> Active + Implementing`
- `implement-plan` = execute approved plan work
- `review-implementation` = review implementation against acceptance criteria and evidence
- `resolve-plan` = move an accepted plan to `Resolved + Resolved`
- `sync-protocol` = update repo-local protocol docs, templates, indexes, or doc-space structure

If the user asks to refile, normalize, or restructure a plan/design space, treat it as `sync-protocol` work and perform a deep refine first.

## GitHub Bridge

Treat GitHub Issues as intake/public surface; plandocs remain the execution source of truth.

- Every non-trivial plandoc should link `GH#N` when applicable.
- Large, risky, or multi-PR issues should have plandocs.

## Escalation Triggers

Create or require a plandoc if any apply:

- cross-repo or 9+ files
- schema changes / migrations
- auth / security / integration work
- non-obvious rollback
- multi-week effort

## Automation Hooks

If the repo supports it, prefer:

- `tools/plans/new`
- `tools/plans/validate`
- `tools/plans/index --write`

Keep automation strict, informative, and aligned with the written protocol.
