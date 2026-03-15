---
name: plandoc-protocol
description: State-machine protocol for reliable LLM planning, execution, review, and closure.
---

# Plandoc Protocol (Optimized)

## Goal
Maximize delivery correctness and coordination with minimal bureaucracy.

This protocol is a state machine for work, backed by structured docs:

- Plandocs = execution docs
- Design docs = architecture / strategy / decision docs

## Modes

There are only two supported modes:

- direct mode: use this skill directly through the harness; no local repo files are required
- local mode: install the optional scaffold so a repo gets `.plandoc/` as its local protocol layer

The skill is the product. `.plandoc/` is only the repo-local install of that protocol.

## Use This Skill When

- the user wants a new plan, design doc, or protocol sync
- a repo has legacy docs that need to be refactored into a cleaner plan/design layout
- work is large, risky, multi-step, or needs auditability
- a plan needs review, refinement, activation, implementation, verification, or state movement

## Prime Directive

- Prefer provable correctness over speed when risk is real.
- Prefer speed when work is low-risk and reversible.
- Every required section must be filled or explicitly `N/A — reason`.
- Plans and design docs must optimize for structurally deterministic outcomes: if two competent implementers could follow the same approved doc and produce materially different architecture or behavior, the doc is under-specified.

## Execution Standard

- The default intent is to advance each plandoc all the way to finish, not leave it drifting between stages.
- Advancement must be earned with absolute discipline, not optimism or convenience.
- Anchor every plandoc in a single explicit stage so the current position and next valid move are deterministic.
- Apply meticulous attention to detail in structure, wording, style, and technical correctness.
- Use full-spectrum analysis: current state, root problem, constraints, risks, solution shape, verification, rollback, and follow-through.
- Drive ambiguity out of plans aggressively enough that implementation shape, boundaries, and critical behavior converge across independent executions.
- Do not blur plan state, implementation state, design intent, or evidence.
- Do not mark a plan as more complete, more certain, or more correct than the underlying evidence supports.

## Source Of Truth

1. In local mode, repo-local protocol docs if present:
   - `.plandoc/README.md`
   - `.plandoc/plans/README.md`
   - `.plandoc/design/README.md`
2. In direct mode, or if no local scaffold is installed, use this skill’s defaults.

If repo-local rules conflict with this skill, follow the repo-local rules unless the user asks to change the protocol itself.

## Multi-Agent Boundary

When a manager agent is supervising multiple workers:

- this skill owns plandoc correctness, state movement, and plan/design structure
- a separate team-management skill should own:
  - worker assignment
  - progress supervision
  - Discord or chat coordination
  - SSH, GitHub, or deployment intervention

Do not turn this skill into a generic fleet or team manager. Use it as the workflow/state machine
that a manager or lead enforces across workers.

## Classify First

Before editing or moving docs, classify each artifact:

- Put it in `.plandoc/plans/` if it is primarily about execution state, verification, sequencing, and delivery.
- Put it in `.plandoc/design/` if it is primarily about architecture, strategy, constraints, or decisions.
- If the intake is primarily an unresolved goal, initiative, epic, or architecture/tradeoff question, establish the design truth first, then create linked plandocs for execution work.

Do not leave active plandocs directly in `.plandoc/plans/` root unless repo-local protocol explicitly says so.

## Intake Patterns

When new work lands, choose the smallest artifact that truthfully matches the request.

Allowed plandoc `Type` values:

- `Bug` - broken behavior, regression, incorrect output, failed workflow, or reliability issue.
- `Case` - support, customer, operator, or one-off fulfillment/investigation request. If the case reveals systemic product or infra work, create linked `Bug`, `Task`, or `Feature` plandocs.
- `Feature` - new capability or material behavior change with a clear user-facing or operator-facing outcome.
- `Task` - bounded maintenance, cleanup, migration, upgrade, documentation, or operational work without a major product-surface change.
- `Research` - the problem is real, but the solution or scope is not yet known. Use it to discover the next executable work.
- `Runbook` - repeatable operational procedure, incident-response flow, migration execution guide, or support playbook.
- `Decision` - the primary output is a durable policy, ruling, or choice that needs to be recorded.
- `Milestone` - umbrella execution plan that coordinates a bounded set of linked subplans.

Rules of thumb:

- One support request can produce multiple linked artifacts: a `Case` for fulfillment plus a `Bug` or `Feature` for systemic follow-up.
- One goal should not become a fuzzy omnibus plandoc. Split design or strategy from execution.
- Use one primary plandoc per bounded unit of delivery.
- Use `Research` only when the real next executable work is still unknown.

## Folder Layout (Canonical)

### Plandocs

- `.plandoc/plans/todo/NNNN-...md`
- `.plandoc/plans/active/NNNN-...md`
- `.plandoc/plans/qa/NNNN-...md`
- `.plandoc/plans/resolved/NNNN-...md`
- `.plandoc/plans/icebox/NNNN-...md`
- `.plandoc/plans/templates/`
- `.plandoc/plans/_index.md`

### Design docs

- `.plandoc/design/drafts/NNNN-...md`
- `.plandoc/design/active/NNNN-...md`
- `.plandoc/design/archived/NNNN-...md`
- `.plandoc/design/templates/`
- `.plandoc/design/_index.md`

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

- `Todo + Seeded` -> `refine`
- `Todo + Refined` -> `review`
- `Todo + Approved` -> `activate`
- `Active + Implementing` -> `implement`
- `QA + Implemented` -> `verify`
- `QA + Reviewed` -> `resolve`
- `Blocked + <any>` -> unblock first; do not guess
- `Resolved + Resolved` -> no further action unless the plan is reopened

### Canonical Transition Rules

- `seed`
  - for plandocs -> `Todo + Seeded`
  - for design docs -> `Draft`
- `refine`
  - for plandocs -> `Todo + Refined`
  - for design docs -> stays `Draft` for proposed or successor designs until the design is reviewable
  - for active design docs -> may stay `Active` only for non-substantive clarifications that do not change adopted meaning
- `review`
  - for plandocs -> either stay `Todo + Refined` with findings or move to `Todo + Approved`
  - for design docs -> either stay `Draft` with findings or move to `Active`
- `activate` -> `Active + Implementing`
- `implement`
  - stays `Active + Implementing` while work remains
  - moves to `QA + Implemented` when implementation is ready for verification
- `verify`
  - stays or returns to `Active + Implementing` if fixes are required
  - moves to `QA + Reviewed` when evidence supports acceptance
- `resolve` -> `Resolved + Resolved`

### Doc-Only Exception

For research, protocol sync, or docs-only work with no implementation phase:

- allowed flow: `Seeded -> Refined -> Approved -> Resolved`
- `resolve` may move `Todo + Approved` directly to `Resolved + Resolved` if verification is captured inline
- record clearly in `## Verification & Monitoring` why no implementation/QA phase exists

### Design doc states

- `Draft` -> proposed or exploratory
- `Active` -> current adopted design
- `Archived` -> historical or superseded

### Design Stage Anchoring (Required)

Every design doc must be anchored in exactly one current state.

- Do not leave a design doc "between states" or implied by prose alone.
- The header `State`, folder placement, and `.plandoc/design/_index.md` entries must agree if the repo uses an index.
- A design transition is not complete until the doc itself records the current state and any linked replacement or adoption result is clear.

### Design Doc Protocol

Design docs record architectural truth. They do not track execution progress and they are not
substitutes for plandocs.

Create or update a design doc when work changes or establishes:

- architecture
- contracts
- invariants
- vocabulary
- module boundaries
- security or privacy posture
- long-lived decisions that plandocs will implement against

Do not create a design doc just to narrate implementation work already covered by a plandoc.

Design docs must be specific enough that linked plandocs can produce structurally deterministic
implementations. If an active design still allows materially different architectures or behavioral
models, it is under-specified and should remain `Draft`.

State meanings and minimum requirements:

- `Draft`
  - Purpose: propose or refine an architectural position.
  - Minimum: problem is stated, constraints are visible, options are considered, a concrete decision is proposed, and major open questions are either listed or explicitly bounded.
  - Not yet true: this is safe to treat as architectural truth for implementation.

- `Active`
  - Purpose: define the currently adopted architectural truth.
  - Minimum: key decisions are resolved, consequences are explicit, linked plandocs can implement against it without major interpretive drift, and any superseded design is archived or clearly displaced.
  - Requirement while in state: keep it aligned with implementation and linked plandocs; do not let code silently outrun it.

- `Archived`
  - Purpose: preserve superseded or historical architectural context.
  - Minimum: replacement or reason for archival is clear, and the doc is no longer presented as current truth.

Design doc review standard:

- does the doc constrain important structural choices tightly enough?
- are invariants and non-goals explicit?
- are tradeoffs and rejected options visible?
- can a plandoc implement against it without inventing architecture?

If the answer to any of those is no, keep the doc in `Draft`.

Relationship to plandocs:

- plandocs execute against design docs
- every non-trivial change still needs a plandoc
- if implementation changes architecture, update the design doc first or in the same change
- if a plandoc and design doc disagree, resolve that conflict explicitly rather than letting implementation choose silently

Canonical design next-step rules:

- `Draft` -> `review` if the proposed decision is coherent enough for adoption review; otherwise `refine`
- `Active` -> no next step unless a material architecture change is required; if it is, create or refine a successor `Draft`
- `Archived` -> no further action unless reopened for correction or historical reference maintenance

Canonical design-doc transition rules:

- `seed` -> `Draft`
- `refine`
  - stays `Draft` for proposed or successor designs until the design is reviewable
  - may stay `Active` only for non-substantive clarifications that do not change adopted meaning
- `review`
  - stays `Draft` with findings if the design is not yet adoption-ready
  - moves to `Active` when the design is sufficiently resolved to serve as architectural truth
- archiving a superseded design is a maintenance action, not a primary public verb; move the design doc to `Archived` when its successor becomes authoritative

## Evidence Minimum

For any change beyond trivial:

- verification steps: exact commands + expected results
- rollback: safe revert path
- risks: what can break and blast radius

## Priority And Severity

- `Priority` applies to every plandoc.
- Allowed `Priority` values:
  - `P0` - requires immediate active handling because the business, user, or operational impact is severe right now.
  - `P1` - important and should be scheduled soon; materially affects delivery, users, or operators.
  - `P2` - worthwhile backlog work; useful, but not urgent.
- `Severity` is optional and applies only to `Bug` or incident-like work.
- Allowed `Severity` values:
  - `S1` - outage, security issue, data loss or corruption, billing failure, or a core workflow broken with no acceptable workaround.
  - `S2` - serious degradation or incorrect behavior with limited workaround or reduced trust.
  - `S3` - minor bug, edge case, cosmetic issue, or low-blast-radius defect with acceptable workaround.

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
5. Identify any choices that are still vague enough to produce materially different implementations.
6. Reclassify artifacts as plan vs design where needed.
7. Record a canonical `Deep refine:` entry in the relevant plan `## Implementation Log`.

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

Header (minimum):

- `State`
- `Owner`
- `Last Updated`

1. `## Problem Statement`
2. `## Constraints / Invariants`
3. `## Options Considered`
4. `## Decision`
5. `## Consequences`
6. `## Rollout / Migration`
7. `## Security / Privacy Notes`

Every required section must be filled or explicitly `N/A — reason`.

## Legacy Refile Workflow

When refiling an existing docs space:

1. Inventory all current docs under `.plandoc/plans/`, `.plandoc/design/`, and any legacy `docs/plans/` or `docs/design/`.
2. Classify each file as plandoc vs design doc.
3. Preserve numbering when it helps trace history.
4. Move files into state folders, not root, unless repo-local rules say otherwise.
5. Rewrite docs to current protocol shape instead of only adding headers when the old structure is misleading.
6. Add or update repo-local `README.md` protocol docs if the repo has none.
7. Add or update `_index.md` files so the resulting layout is navigable.
8. Keep historical intent, but align wording with current architecture and current evidence.

## Staged Workflow

Default staged flow:

`seed -> refine -> review -> activate -> implement -> verify -> resolve`

- `seed` = create the first correct plan or design doc in the right folder and state
- `refine` = deepen or clean up an existing plan/design doc after reading the relevant sources
- first `review` = review the plan/design for readiness
- `activate` = preflight + move `Todo + Approved -> Active + Implementing`
- `implement` = execute the approved plan
- `verify` = review implementation and evidence against acceptance criteria
- `resolve` = move the plan to `Resolved + Resolved`

Use `sync-protocol` when the task is about the protocol itself, templates, indexes, or refiling the doc space.

## Operational Verbs

Use these verbs exactly in prompts:

- classify the target first: plandoc, design doc, or protocol/doc-space work
- `seed` = create a new plandoc or design doc in the correct folder and initial state
- `refine` = enrich or restructure an existing plandoc or design doc without implementation
- `review` = review a plandoc or design doc for readiness, gaps, and protocol compliance
- `activate` = preflight + move `Todo + Approved -> Active + Implementing`
- `implement` = execute approved plan work
- `verify` = review implementation against acceptance criteria and evidence
- `resolve` = move an accepted plan to `Resolved + Resolved`
- `sync-protocol` = update repo-local protocol docs, templates, indexes, or doc-space structure

Do not expose plan-specific and design-specific verb variants unless a harness absolutely requires them. The point of the public verb surface is to stay small while the stage model stays explicit.

If the user asks to refile, normalize, or restructure a plan/design space, treat it as `sync-protocol` work and perform a deep refine first.

## GitHub Bridge

Treat GitHub Issues as intake/public surface; plandocs remain the execution source of truth.

- Every non-trivial plandoc should link `GH#N` when applicable.
- Large, risky, or multi-PR issues should have plandocs.

## Optional Local Scaffold

Use this only when a repo explicitly wants local plandoc protocol docs installed as an operating layer.

Read `references/plandoc_scaffold.md` and use:

```bash
python3 scripts/install_plandoc_scaffold.py --repo-root /path/to/repo --project-name ProjectName
```

Use `--force` only when replacing an existing scaffold intentionally.

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
