---
name: plandoc-protocol
description: Portable artifact/lifecycle authority for plandocs, design anchors, control boards, durable comms, audit/sweep mode, review gates, cut/slice vocabulary, and proof-backed closure. Use for protocol questions, plan/design structure, state transitions, readiness review, and canonical control-stack meaning; not for live lane routing.
---

# Plandoc Protocol (Optimized)

## Goal
Maximize deterministic delivery correctness, bounded execution, proof-backed closure, and durable coordination/review artifacts.

Administrative convenience is never a valid reason to weaken specificity, explicitness, or evidence.

This protocol is a state machine for work, backed by structured docs:

- Plandocs = execution docs
- Design docs = architectural blueprint docs. This is their literal purpose:
  define the system structure, contracts, boundaries, invariants, vocabulary,
  ownership, accepted options, rejected options, and proof meaning that
  plandocs execute against.
- Control boards = active coordination plandocs for multi-lane work
- Durable comms = protocol-backed handoff threads for cross-owner coordination

## Modes

There are only two supported modes:

- direct mode: use this skill directly through the harness; no local repo files are required
- local mode: install the optional scaffold so a repo gets `.plandoc/` as its local protocol layer

The skill is the product. `.plandoc/` is only the repo-local install of that protocol.

## Use This Skill When

- the user wants a new plan, design doc, or protocol sync
- the user wants a control board, a durable comms protocol, or a plandoc-space governance update
- a repo has legacy docs that need to be refactored into a cleaner plan/design layout
- work is large, risky, multi-step, or needs auditability
- a plan needs review, refinement, activation, implementation, verification, or state movement
- the user asks to audit or sweep resting plandocs, design docs, control boards,
  or plan sets for claims, contradictions, overlap, drift, or missing anchors
- plandocs need to be anchored to canonical design docs so feature intent,
  architecture, vocabulary, invariants, and acceptance meaning stay consistent
- design docs need to become the central, continuously refined source of truth
  for a feature or subsystem instead of passive background references
- review, scoring, smell-sweep, or architecture-health work needs a durable review artifact under `.plandoc/reviews/`
- a cross-project contract audit needs one durable, evidence-backed review artifact with exact producer/consumer mismatches

## Prime Directive

- Prefer provable correctness over speed when risk is real.
- Prefer speed when work is low-risk and reversible.
- Every required section must be filled or explicitly `N/A — reason`.
- Treat design docs as anchors that lock plandoc generation. A plandoc is not
  honest or correct just because it links an anchor; its durable meaning must be
  derived from the anchor.
- Plans and design docs must optimize for structurally deterministic outcomes: if two competent implementers could follow the same approved doc and produce materially different architecture or behavior, the doc is under-specified.
- Design docs are the canonical architectural blueprint for feature meaning,
  system structure, and durable contracts; plandocs execute bounded slices
  against that anchor and must not become the hidden source of product or
  architectural truth.
- Active or locked design docs must be interpretation-intolerant. If a decision
  affects ownership, schema, routes, API shape, deployment, security, privacy,
  lifecycle state, naming, proof, or acceptance, the design doc must state the
  adopted rule exactly or explicitly defer it with an owner, blocker, and
  promotion gate.
- Active design docs are living anchors: every meaningful plandoc transition
  must review whether the anchor remains accurate, too vague, stale, or in need
  of a successor design.
- Briefs, overviews, summaries, or vague narrative notes are never substitutes for required operating sections.

## Execution Standard

- The default intent is to advance each plandoc all the way to finish, not leave it drifting between stages.
- Advancement must be earned with absolute discipline, not optimism or convenience.
- Anchor every plandoc in a single explicit stage so the current position and next valid move are deterministic.
- Apply meticulous attention to detail in structure, wording, style, and technical correctness.
- Use full-spectrum analysis: current state, root problem, constraints, risks, solution shape, verification, rollback, and follow-through.
- One non-trivial plandoc must have one primary outcome. If the document is really coordinating multiple independent outcomes, split it or promote it to a `Milestone` with bounded subplans.
- Every approved or active plandoc must answer one explicit slice question: if we stop immediately after this landing slice, what exact new truth is now true?
- Every non-trivial plandoc must name its design anchor before approval. If no
  canonical design doc exists, create or refine the design doc first; do not
  let a plan invent durable feature semantics.
- Every non-trivial plandoc must include a current design-anchor review record
  before approval, activation, QA, or resolution.
- Drive ambiguity out of plans aggressively enough that implementation shape, boundaries, and critical behavior converge across independent executions.
- Do not blur plan state, implementation state, design intent, or evidence.
- Do not mark a plan as more complete, more certain, or more correct than the underlying evidence supports.

## Audit And Sweep Mode

Use `plandoc-protocol audit` for rigorous deep refinement of a plandoc, design
doc, control board, or related plan set.

Use `plandoc-protocol sweep` for a lighter bounded consistency scan.

There is no separate rest-audit skill. Use `plandoc-protocol audit`.

Audit mode:

- extracts every important claim, assertion, and supposition;
- verifies claims against current code, tests, docs, tickets, checked scripts,
  deployment truth, and read-only live state when available;
- classifies claims as `confirmed`, `contradicted`, `missing`, or `ambiguous`;
- actively hunts for logical contradictions and contract inconsistencies inside
  the document and across neighboring plans, design anchors, scripts, code,
  live readbacks, and issue state;
- detects overlap, drift, stale wording, stale evidence, and hidden
  architecture;
- updates the audited document with evidence-backed corrections when safe and
  in scope;
- records a review finding or follow-up plandoc when correction requires code,
  design, ownership, approval, deploy, or credentialed work;
- leaves one deterministic next legal move.

Do not start implementation, deploy, apply migrations, restart runtimes, run
browser proof, close GitHub issues, or notify testers from audit mode unless a
separate approved execution slice explicitly permits that action.

For recurring watchdog or cron use, audit one document per run. A manual
one-off audit may cover multiple related documents only when the user asks for
that explicitly.

If the item is actively being implemented, switch to live CTRL/workspace lane
control instead of audit mode.

Required audit output:

- `Status`: ready / needs-refine / needs-design-repair / blocked /
  approval-gated / stale / superseded
- `Claim checks`
- `Boundary findings`
- `Contradictions / inconsistencies`
- `Edits made`
- `Next legal move`
- `Verification`

## Cut And Slice Vocabulary

Use `landing slice` as the formal plandoc term for the bounded unit captured by
`## Landing Slice / Stopping Point`.

Use `cut` as operator shorthand for that same bounded unit. A cut is not a
looser bundle, theme, or convenience bucket. If a workspace control board,
handoff, or status note says `active cut`, read it as the current landing
slice.

`Cut`, `slice`, and `landing slice` may be treated as synonyms only under this
protocol boundary:

- one primary outcome;
- one owner or explicitly coordinated owner handoff;
- one stop condition;
- one proof target;
- explicit deferrals for work that is not landing now.

A cut may contain ordered substeps only when those substeps are required to land
the same bounded outcome and share the same proof and stop boundary. If work has
independent outcomes, owners, proofs, rollout paths, or rollback meanings, split
it into separate cuts/slices or promote the coordinating artifact to a
`Milestone` with bounded subplans.

## Sprint Definition

A sprint is a bounded set of currently committed landing slices, not a theme bucket, epic label, or loose intention list.

Sprint rules:

- the unit of sprint commitment is the current `## Landing Slice / Stopping Point` of a plandoc, not the whole initiative unless the initiative truly has one bounded slice
- only slices in `Todo + Approved`, `Active + Implementing`, or `QA + Implemented|Reviewed` belong in the sprint
- a slice that lacks one primary outcome, explicit deliverables, explicit deferrals, or mapped verification is not sprint work; it is refinement backlog
- if a plandoc hides multiple independent slices, only one slice may be in the sprint at a time unless a `Milestone` intentionally coordinates bounded subplans
- sprint scope must be small enough that every admitted slice can realistically reach `QA + Reviewed` or `Resolved + Resolved` in the current delivery window

### Sprint Admission

A new slice may enter the sprint only when all of the following are true:

- the plandoc is already `Todo + Approved` or is an explicitly continued in-flight slice already in `Active` or `QA`
- `## Outcome` states one primary outcome sentence
- `## Deliverables` lists explicit `D1`, `D2`, ... items
- `## Landing Slice / Stopping Point` states the exact truth that becomes true if work stops after the slice
- `## Deferred / Not In This Slice` explicitly names what is not landing now
- `## Acceptance Criteria` uses explicit `AC1`, `AC2`, ... items
- the plandoc has a valid design anchor, or an explicit allowed exception, and
  the anchor has been reviewed for consistency with the proposed slice
- `## Design Anchor Review` records the current anchor state and says whether
  anchor maintenance is required before execution
- `## Verification & Monitoring`, `## Rollback`, `## Invariants / Non-Negotiables`, and ownership are present and concrete

If any admission condition is missing, the item is not sprint-ready no matter how urgent or intuitive it feels.

### Sprint Done

A sprint slice is done only when:

- the current slice reaches `QA + Reviewed` or `Resolved + Resolved`
- verification evidence is captured against the slice acceptance criteria
- the design-anchor review has been refreshed against the landed or blocked
  result
- the closing record names what landed for the slice and what remains deferred, if anything

Items sitting in `QA + Implemented` are still in the sprint. They are not done yet.

## Source Of Truth

1. In local mode, repo-local protocol docs if present:
   - `.plandoc/README.md`
   - `.plandoc/plans/README.md`
   - `.plandoc/design/README.md`
   - `.plandoc/reviews/README.md`
   - `.plandoc/comms/README.md` when durable comms are installed
2. In direct mode, or if no local scaffold is installed, use this skill’s defaults.

If repo-local rules conflict with this skill, follow the repo-local rules unless the user asks to change the protocol itself.

## Design Anchor Contract

Hard rule: every non-trivial plandoc must be anchored to one canonical design
doc before it can become `Todo + Approved`, `Active + Implementing`,
`QA`, or `Resolved`.

Harder rule: the design doc is not a one-time prerequisite. It is the central
feature anchor and architectural blueprint. It must be actively reviewed and
improved as execution exposes new facts.

Anchor lock rule: when generating or refining a plandoc, read the intended
design anchor before writing outcome, deliverables, implementation shape,
acceptance criteria, proof semantics, or rollback. The plandoc must be locked
to the anchor's vocabulary, owners, schema, routes, services, state model,
security posture, invariants, and acceptance meaning. If the anchor does not
contain the durable meaning needed by the slice, do not invent that meaning in
the plandoc. Refine or supersede the design doc first, or keep the plandoc in a
seeded/refined state with the exact anchor blocker named.

Design grounding mandate: stay firmly rooted in the governing design docs. If
no design doc governs the area encountered, or if the active design doc is too
thin, stale, inaccurate, or contradicted by current code/proof, create, fix, or
improve the design doc before implementation or in the same bounded slice before
the plan can be approved, activated, closed, or used for worker routing. Do not
bury durable architecture, vocabulary, ownership, schema, route, security,
rollout, or acceptance meaning only in a plandoc, worker prompt, issue comment,
test, or code patch.

Blueprint rule: when a user asks for architecture, system shape, information
architecture, product-object relationships, lifecycle boundaries, route/schema
contracts, deployment topology, proof semantics, or "how this should work",
the expected artifact is a `.plandoc/design/` doc or an update to the governing
design doc. A plandoc may then execute a bounded slice against that blueprint,
but the plandoc must not be the only place the blueprint exists.

The design doc is the canonical source for:

- feature intent and vocabulary
- architecture and boundaries
- contracts and data ownership
- invariants and non-goals
- rollout shape and durable acceptance meaning

Design docs must not merely be plausible narratives. They are contract
surfaces. A locked or active design must leave no material room for an
implementer to choose between competing architectures, owners, names, route
families, data models, lifecycle states, security postures, or acceptance
meanings. Any unresolved choice in those categories keeps the design in
`Draft`, or must be written as an explicit deferred decision with a named owner
and gate.

The plandoc is the execution slice. It may choose scope, sequence, verification,
and rollback for a bounded landing step, but it must not invent or silently
change canonical feature meaning.

Terminology guard:

- `plans/active/` means work currently admitted for execution.
- `design/active/` means adopted architecture truth. It does not mean the
  design is currently being drafted, edited, or implemented.
- Draft or successor designs belong in `design/drafts/` until semantic
  prep/refine and review prove they are safe to adopt as anchors.

Required plandoc header field:

- `Design Anchor: /absolute/path/to/.plandoc/design/active/<doc>.md`

Required plandoc section:

- `## Design Anchor Review`

The section is the anchor-lock record. It must record:

- anchor path and state
- last review date or current review date
- whether the plandoc matches the anchor
- whether the anchor is missing, stale, too vague, contradicted by code, or
  still current
- the specific anchor decisions that constrain this slice
- any durable terms, table names, route names, state names, security rules, or
  proof meanings the plandoc is deriving from the anchor
- the required action: `none`, `clarify active anchor`, `create successor
  design`, `split anchor`, or `archive superseded anchor`

The review must be refreshed before these transitions:

- `Todo + Refined` -> `Todo + Approved`
- `Todo + Approved` -> `Active + Implementing`
- `Active + Implementing` -> `QA + Implemented`
- `QA + Implemented` -> `QA + Reviewed`
- `QA + Reviewed` -> `Resolved + Resolved`

Allowed exceptions:

- `Design Anchor: N/A — trivial mechanical change` for low-risk typo,
  formatting, dependency, or one-file maintenance work that creates no durable
  feature, contract, schema, route, deployment, security, privacy, or
  architecture meaning.
- `Design Anchor: N/A — emergency mitigation` for urgent incident response.
  The plandoc must include a follow-up design-anchor task before it resolves
  if the mitigation changes durable behavior.
- `Design Anchor: draft /absolute/path/to/.plandoc/design/drafts/<doc>.md`
  only while the plandoc remains `Todo + Seeded|Refined`. A draft anchor is not
  sufficient for `Approved`, `Active`, `QA`, or `Resolved`.

Promotion gates:

- `Seeded`: may name a missing, draft, or active design anchor, but the missing
  anchor must be visible as a refinement blocker.
- `Refined`: must name the intended design anchor and summarize any design
  gaps that block approval in `## Design Anchor Review`.
- `Approved`: must point at an `Active` design doc or carry one of the allowed
  explicit exceptions. The design-anchor review must say the anchor is current
  enough to execute the landing slice without inventing architecture.
- `Active`: implementation must stay inside the design anchor. If execution
  discovers design drift, stop and update or supersede the design doc before
  continuing.
- `QA` and `Resolved`: closure evidence must say whether the design anchor
  remains accurate after the landing slice and what anchor maintenance, if any,
  was completed or deferred.

Conflict rule:

- If a plandoc and its design anchor disagree, the design anchor wins until a
  deliberate design update changes it.
- Do not resolve conflicts by editing the plandoc to match implementation after
  the fact. Record the drift, update or supersede the design doc, then rebind
  the plandoc.

Canonical feature rule:

- A feature must have one active design anchor at a time unless the feature has
  been deliberately split into separately named bounded subsystems.
- Successor designs must name the design they supersede, and the old design
  must be archived or clearly displaced when the successor becomes active.
- Related plandocs should link to the same anchor unless they intentionally
  implement a different bounded feature or subsystem.
- A plandoc may not point at a convenience design doc that duplicates or
  weakens the central anchor. Refine the central anchor instead.

Continuous anchor refinement rule:

- If implementation, QA, review, production evidence, or a blocker changes
  durable feature meaning, update the design anchor first or in the same
  coherent change before closing the plandoc.
- If the needed update is a clarification that preserves adopted meaning, edit
  the active design doc and record the maintenance in its `## Maintenance Log`.
- If the needed update changes adopted meaning, create or refine a successor
  draft design, review it into `Active`, and archive or clearly supersede the
  prior design.
- If several plandocs repeatedly need local explanation that the anchor does not
  contain, the anchor is under-specified. Stop adding explanation to the plans
  and refine the design doc.

## Multi-Agent Boundary

When a manager agent is supervising multiple workers:

- this skill owns plandoc correctness, state movement, plan/design structure,
  control-board rules, and durable-comms rules
- a separate live-operations skill such as `workspace-lane-control` should own:
  - worker assignment
  - progress supervision
  - worker parking, interruption, restart, and re-steering
  - WIP enforcement and completion-ping discipline
  - live chat or external coordination
  - SSH, GitHub, or deployment intervention

Do not turn this skill into a generic fleet or team manager. Use it as the workflow/state machine
that a manager or lead enforces across workers.

### Boundary With Workspace Lane Control

Use `workspace-lane-control` beside this skill when the problem is live
multi-repo or tmux-backed coordination.

This skill defines:

- plandoc lifecycle, stage gates, and required sections
- design-doc structure, design-anchor rules, and maintenance requirements
- control-board artifact contract and required sections
- durable-comm artifact layout and lifecycle
- review, activation, QA, resolution, and archival rules

`workspace-lane-control` applies those rules operationally. It owns:

- live lane discovery and classification
- worker assignment, parking, interruption, restart, and re-steering
- WIP enforcement under the governing board
- routing, parking, and re-steering lanes
- reconciling pane state, board state, indexes, and durable comms
- deciding when to stop routing and run fail-closed realignment

Do not duplicate live routing logic here. Do not let `workspace-lane-control`
define a second plandoc, design-doc, board, or durable-comm protocol. If the two
skills appear to disagree, treat this skill as the artifact/lifecycle authority
and treat `workspace-lane-control` as the live operations authority that must
rebind to the protocol.

Worker agents may recommend next steps, but plandoc protocol does not give them
authority to self-admit follow-up work. Follow-up admission is a control-board
and workspace-lead decision.

### Compound Execution Stack

When plandoc work is running through a live multi-agent workspace, compose the
skills this way:

- `plandoc-protocol` defines the artifact, lifecycle state, design anchor,
  control-board contract, and durable-comm schema.
- `workspace-lane-control` is the top-level live workspace entrypoint. It
  decides what work is admitted, which lane owns it, whether WIP may expand,
  and whether the board must be rebound.
- `tmux-team-lead` is a subroutine for lane sweep and handoff execution after
  `workspace-lane-control` or the governing board has already established the
  legal work.
- `tmux-codex-comms` is transport only: pane discovery, pane capture, prompt
  delivery, queue/send verification, and completion-ping transport.
- `agent-comms` records durable cross-owner handoffs that must survive pane
  churn. It does not choose the owner or invent the comm schema.
- `verification-before-completion` prevents accepting a landed slice without
  fresh evidence.
- `workspace-self-check` is the end-of-turn guardrail. It reconciles board,
  issue, lane, callback, and learning-harvest state before the workspace rests;
  it does not create a second admission loop.
- `plandoc-protocol audit` is the resting-document audit mode. It may refine
  or recommend repair for plans and design anchors, but it does not start
  implementation.
- `fail-closed-realignment` is the emergency brake for drift, contradiction,
  or broken contract state. It stops routing until one owner, one blocker, one
  deliverable, and one next move are explicit.
- `plandocs-github` is the GitHub front desk. It triages issues and escalates
  substantial work into this protocol rather than replacing it.

Do not flatten this stack into one giant skill. Do not expose subordinate
transport or team-sweep skills as competing top-level workflows when a
workspace control board exists. Each layer owns one kind of truth.

Operator entrypoints:

- artifact, lifecycle, design anchor, review, or protocol question:
  `plandoc-protocol`
- live workspace routing, worker ownership, WIP, or next legal move:
  `workspace-lane-control align`
- resting plan/design contradiction, overlap, or drift analysis:
  `plandoc-protocol audit`
- tmux pane discovery or verified prompt transport after ownership is known:
  `tmux-codex-comms`
- durable handoff file creation or update after ownership is known:
  `agent-comms`
- end-of-turn guard:
  `workspace-self-check`

## Coordination Artifacts

Boards and durable comms are official plandoc-protocol concepts.

They are not ad hoc manager notes, and they are not separate shadow systems
owned by a tmux or team-management skill.

### Control Boards

A control board is an official coordination plandoc used when one lane or
workspace is actively managing multiple workers, repos, or bounded slices.

Rules:

- a control board is still a plandoc, not a separate header `Type`, `Status`,
  or `State`
- use normal plandoc lifecycle/state rules for the board itself
- a control board must name a `Design Anchor` and include a current
  `## Design Anchor Review` unless it is a documented emergency mitigation
- use a control board only when multi-lane coordination is real; do not create
  one for ordinary single-repo work
- one workspace should have at most one live active control board at a time
- if a fact is not on the live control board, it is not governing the work

Control-board authority is narrow and operational.

A control board defines:

- current mission and critical path
- admitted WIP and lane states
- owner, slice, stop condition, blockers, and next legal moves
- what work is temporarily illegal while the board is active
- evidence gates needed before a route, deploy, or handoff can proceed

A control board does not define:

- durable architecture
- feature vocabulary or acceptance meaning
- schema, route, service, auth, deployment, security, or privacy contracts
- product intent, non-goals, or long-term rollout strategy

Those sticky meanings belong in active design docs. If the board and its design
anchor disagree, the design anchor wins and the board is stale until it is
rebound. If a board repeats the same architectural explanation across slices or
uses an observation to decide future work, promote or refine that meaning in the
design anchor instead of letting the board become a hidden design doc.

Required control-board sections:

- `## Design Anchor Review`
- `## Active Mission`
- `## Current Critical Path`
- `## WIP Cap`
- `## Active Lanes`
- `## Parked Lanes`
- `## Blocked Lanes`
- `## Support-Only Lanes`
- `## Next Three Legal Moves`
- `## Illegal Moves While This Board Is Active`

Minimum control-board discipline:

- name exactly one current critical path unless a parallel evidence lane is
  explicitly admitted
- keep every managed lane in one explicit state
- update the board when a landed or blocked reply changes owner, slice, or stop
  truth
- do not leave an old sprint or owner active on the board once the evidence has
  moved on

Canonical lane states for a control board:

- `active`
- `research-only`
- `parked`
- `blocked`
- `drifted`
- `stale`
- `support-only`

Use `research-only` only for explicitly admitted no-code, no-QA evidence work
that can run without becoming a second implementation critical path.

### Durable Comms

Durable comms are the official protocol artifact for cross-owner handoffs that
must survive pane churn, delayed pickup, or local plandoc-only state changes.

Use durable comms when:

- ownership changes across repos or lanes
- a blocker crosses repo boundaries
- a bounded next step must survive tmux churn
- a worker must be able to recover the exact ask later

Do not use durable comms for:

- ordinary repo-local implementation notes
- transient tmux chatter that can be safely lost
- plandoc state changes by themselves

Canonical comm layout:

- `.plandoc/comms/open/`
- `.plandoc/comms/acked/`
- `.plandoc/comms/closed/`
- `.plandoc/comms/templates/`
- `.plandoc/comms/README.md`

Canonical filename shape:

- `YYYY-MM-DDTHHMMSSZ--from--to--slug.md`

Required comm fields:

- `From`
- `To`
- `Created`
- `Status`
- `Subject`
- `Related Plans`
- `Reason`
- `Current Truth`
- `Requested Action`
- `Evidence`
- `Blockers`
- `Next Expected Reply`
- `Updates`

Allowed comm `Status` values:

- `Open`
- `Acked`
- `Closed`

Durable-comm lifecycle:

1. create the thread in `open/`
2. nudge the live lane only after the durable thread exists, when live tmux is
   in use
3. move the thread to `acked/` when the receiver accepts ownership or starts
   work
4. move the thread to `closed/` when the request is resolved, superseded, or no
   longer actionable

When the handoff is for active execution rather than background reference, the
comm must also require an explicit completion reply:

- landed or blocked phrase
- `changed: ...`
- `commit: ...` or `blocker: ...`
- `tests: ...`
- `next recommended: ...`

Tmux or other live transport may point a worker at a durable comm. It does not
replace the durable comm as source of truth.

Completion replies are idempotent inputs, not commands to repeat work.

Before moving any plan, board, comm, or design state from a landed or blocked
reply, classify the reply as:

- `new`
- `duplicate`
- `conflicting`
- `orphaned`

Use the durable comm path, repo/lane, governing plandoc, commit or blocker,
changed summary, tests summary, and next recommended step as the callback key.

If the key is already represented in a closed comm and the governing
plandoc/board already integrated it, the reply is `duplicate`. Do not close the
same slice again, rerun design-anchor maintenance, rerun wiki maintenance, or
admit follow-up work from that duplicate.

If the same slice has different evidence or next-step meaning, the reply is
`conflicting`; stop and reconcile before any transition.

If no governing comm or plandoc can be found, the reply is `orphaned`; create
or recover the missing durable record before accepting it.

## Classify First

Before editing or moving docs, classify each artifact:

- Put it in `.plandoc/plans/` if it is primarily about execution state, verification, sequencing, and delivery.
- Put it in `.plandoc/design/` if it is primarily about architecture, strategy, constraints, or decisions.
- Put it in `.plandoc/reviews/` if it is a durable code review, scoring artifact, smell report, or architecture-health review.
- If the intake is primarily an unresolved goal, initiative, epic, or architecture/tradeoff question, establish the design truth first, then create linked plandocs for execution work.

Do not leave active plandocs directly in `.plandoc/plans/` root unless repo-local protocol explicitly says so.

## Intake Patterns

When new work lands, choose the narrowest truthful artifact that can fully specify one outcome without hiding ambiguity.

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

## Forbidden Shorthand

The following are forbidden as substitutes for a fully specified plandoc:

- `brief`
- `overview`
- `high-level plan`
- `quick plan`
- `notes`
- `follow-up summary`

Rules:

- these may exist only as supplemental navigation aids if repo-local protocol requires them
- they must never replace `## Outcome`, `## Deliverables`, `## Landing Slice / Stopping Point`, `## Acceptance Criteria`, or `## Verification & Monitoring`
- if a repo-local template requires `## Summary`, keep it short and factual, but do not treat it as the plan

## Folder Layout (Canonical)

### Plandocs

- `.plandoc/plans/todo/NNNN-...md`
- `.plandoc/plans/active/NNNN-...md`
- `.plandoc/plans/qa/NNNN-...md`
- `.plandoc/plans/resolved/NNNN-...md`
- `.plandoc/plans/icebox/NNNN-...md`
- `.plandoc/plans/templates/`
- `.plandoc/plans/_index.md`

`icebox` means manual hold. A plandoc in `plans/icebox/` or a GitHub/Jira
issue labeled `icebox` is not a candidate for prep, routing, blocker
accounting, self-check rest conditions, comments, or closeout. It re-enters the
state machine only after the human manually lifts the exact item out of
icebox, and that lift is recorded in the governing index, issue-control, or
board before assignment.

### Design docs

- `.plandoc/design/drafts/NNNN-...md`
- `.plandoc/design/active/NNNN-...md`
- `.plandoc/design/archived/NNNN-...md`
- `.plandoc/design/templates/`
- `.plandoc/design/_index.md`

### Review artifacts

- `.plandoc/reviews/YYYY-MM-DD-<scope-slug>-code-review.md`
- `.plandoc/reviews/README.md`

### Durable comms

- `.plandoc/comms/open/YYYY-MM-DDTHHMMSSZ--from--to--slug.md`
- `.plandoc/comms/acked/YYYY-MM-DDTHHMMSSZ--from--to--slug.md`
- `.plandoc/comms/closed/YYYY-MM-DDTHHMMSSZ--from--to--slug.md`
- `.plandoc/comms/templates/message.md`
- `.plandoc/comms/README.md`

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

### Icebox Discipline

`Icebox` is for intentionally deferred work, not forgotten work.

Every plandoc in `Icebox` must carry explicit move-out criteria in a dedicated `## Icebox Exit Criteria`
section.

Minimum standard:

- name the exact gates or prerequisites that would justify moving the plandoc out of `Icebox`
- state the concrete signal or evidence to check for each gate
- name the target next `Status` + `State` once those gates open
- avoid vague language like "later", "eventually", or "when time permits"

If the move-out criteria cannot be stated concretely, the plandoc is under-refined and should not be
treated as a trustworthy deferred plan.

### Stage Anchoring (Required)

Every plandoc must be anchored in exactly one current stage.

- Do not leave a plandoc "between stages" or implied by prose alone.
- The header `Status` + `State`, folder placement, and `## Implementation Log` must agree.
- A stage transition is not complete until the doc itself records it.
- If the evidence does not support the next stage, keep the plandoc where it is.

Stage definitions and minimum requirements:

- `Seeded`
  - Purpose: capture the work item correctly enough to exist in the system.
  - Minimum: required header present, design anchor named or explicitly missing
    as a refinement blocker, problem/context stated, initial goals/non-goals
    stated, initial `## Design Anchor Review` created, next refinement needs
    visible.
  - Not yet true: execution readiness.

- `Refined`
  - Purpose: make the plandoc materially more trustworthy than the initial seed.
  - Minimum: relevant source-of-truth docs and the design anchor reviewed,
    current behavior separated from intended behavior, touch points identified,
    design gaps named in `## Design Anchor Review`, risks/verification/rollback
    drafted, and semantic prep completed: every durable architecture,
    ownership, vocabulary, route, schema, lifecycle, rollout, security,
    privacy, and acceptance meaning needed by the current slice is either
    already present in the design anchor or explicitly blocked/deferred there.
  - Not yet true: approved for activation.

- `Approved`
  - Purpose: mark the plandoc as ready for activation.
  - Minimum: plan review completed, active design anchor or explicit allowed
    exception present, current design-anchor review says no anchor refinement
    blocks the slice, implementation shape coherent, primary outcome explicit,
    deliverables explicit, first landing slice explicit, acceptance criteria
    clear, major open questions either resolved or explicitly bounded.
  - Gate: if unresolved ambiguity can still materially change architecture, contracts, rollout shape, or acceptance criteria, the plandoc is not `Approved`.
  - Gate: if approval requires architectural, vocabulary, contract, schema,
    route, rollout, security, or privacy meaning that is not in the design
    anchor, the plandoc is not `Approved`.
  - Gate: if the plandoc cannot say what lands in the current slice and what remains deferred, it is not `Approved`.
  - Not yet true: substantial code edits. If code changes are non-trivial, the separate implementation approval gate still applies.

- `Implementing`
  - Purpose: active execution against an approved plan.
  - Minimum: plandoc moved to `Active`, execution scope is explicit, intended touch points/tests/verification path are known, the current landing slice and stopping point are explicit, implementation work is being carried out or is ready to begin immediately.
  - Requirement while in stage: log meaningful execution progress; keep work
    inside the design anchor; stop for design rebind if execution exposes
    anchor drift; refresh `## Design Anchor Review` before moving to QA; do not
    claim implementation completion early.

- `Implemented`
  - Purpose: implementation is complete enough to enter verification.
  - Minimum: all deliverables for the current landing slice have landed, no known required implementation work remains for that slice, and verification can now judge the result.
  - Not yet true: accepted and resolved.

- `Reviewed`
  - Purpose: implementation and evidence have been reviewed against the plan.
  - Minimum: verification results captured, acceptance criteria assessed
    explicitly, deliverables assessed explicitly, design anchor accuracy
    checked and recorded in `## Design Anchor Review`, remaining issues either
    absent or severe enough to return the plan to `Active + Implementing`.
  - Not yet true: resolved historical record.

- `Resolved`
  - Purpose: close the plan as complete or conclusively finished.
  - Minimum: final state is supported by evidence, the design anchor remains
    accurate or a follow-up design update is named, the plandoc has a stable
    historical record, the landed outcome and deliverables are named explicitly,
    `## Design Anchor Review` records the closing anchor decision, and any
    deferred or follow-up work is named explicitly unless there is none.

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
- `Active` -> current adopted design; canonical anchor, not active execution
- `Archived` -> historical or superseded

### Design Stage Anchoring (Required)

Every design doc must be anchored in exactly one current state.

- Do not leave a design doc "between states" or implied by prose alone.
- The header `State`, folder placement, and `.plandoc/design/_index.md` entries must agree if the repo uses an index.
- A design transition is not complete until the doc itself records the current state and any linked replacement or adoption result is clear.

### Design Doc Protocol

Design docs are architectural blueprints. They record architectural truth,
system structure, boundaries, contracts, and acceptance meaning. They do not
track execution progress and they are not substitutes for plandocs.

Each non-trivial feature or subsystem should have one active design doc that
serves as the canonical blueprint and anchor for its linked plandocs. Treat the
design doc as the stable source for meaning and structure, not as a post-hoc
explanation of whatever a landing slice happened to implement.

Central anchor rule:

- The active design doc is the canonical feature anchor. Linked plandocs are
  slices against it, not alternate sources of truth.
- If multiple active design docs seem to govern the same feature, stop and
  reconcile them before approving more plandocs.
- If a plan needs a local architecture explanation that is absent from the
  design doc, the correct default is to improve the design doc, not to bury the
  explanation in the plan.
- Every active design doc should name the plandocs it currently anchors or the
  index that tracks them.

Create or update a design doc when work changes or establishes:

- architecture
- information architecture
- contracts
- invariants
- vocabulary
- product object relationships
- module boundaries
- lifecycle boundaries
- route, schema, service, deployment, or storage topology
- security or privacy posture
- long-lived decisions that plandocs will implement against

Do not create a design doc just to narrate implementation work already covered by a plandoc.

Design docs must be specific enough that linked plandocs can produce structurally deterministic
implementations. If an active design still allows materially different architectures or behavioral
models, it is under-specified and should remain `Draft`.

Design docs must also be maintainable anchors. They should say what they cover,
what they do not cover, which active or recent plandocs rely on them, and what
drift signals should trigger a follow-up refinement.

### Watertight Design Standard

An active or locked design doc is ready only when it can serve as a fixed source
of truth for implementation without requiring hallway interpretation.

It must answer, where relevant:

- who owns the behavior, data, route, service, deploy surface, or lifecycle
  state;
- what is in scope and what is explicitly out of scope;
- which names, identifiers, routes, tables, namespaces, env vars, statuses, and
  state transitions are canonical;
- which operations are allowed, forbidden, or deferred;
- which invariants must not be broken by implementation plandocs;
- what proof or acceptance meaning demonstrates that the design was followed;
- what successor decision is required before deferred behavior can move into
  scope.

Open questions may exist in a design doc, but they must not overlap with the
behavior being locked. If an open question can change implementation shape,
schema, routing, security, rollout, or acceptance meaning, the design is not
lockable until the question is answered or explicitly moved out of scope.

Plandocs may add execution order, todo sequencing, file touch points,
verification commands, rollback steps, and tactical details. They must not add
new architecture, vocabulary, ownership, or acceptance meaning that the design
doc does not already contain.

### Design Doc Information Architecture

Design docs are not free-form essays. They must use a consistent information
architecture so repo-local and cross-repo anchors can be compared, audited, and
implemented without guessing.

The required top-level sections remain the strict template sections below. For
subsystem, API, infra, auth, data, lifecycle, or UI architecture docs, structure
`## Decision` with the following typed blocks in this order when relevant. If a
block does not apply, either omit it when clearly irrelevant or write
`N/A — reason` when omission could be ambiguous.

1. `### Ownership And System Boundary`
   - owner repo/module/service/team;
   - consumer and producer boundaries;
   - adjacent systems explicitly not owned here.
2. `### Domain / Object Model`
   - canonical nouns and product objects;
   - one-to-one, one-to-many, and ownership relationships;
   - identifiers, public ids, private ids, and display names.
3. `### Route And Endpoint Contract`
   - exact route families, methods, paths, auth mode, principal, payload
     shape, response shape, side effects, error classes, CORS/preflight meaning,
     and proof surface.
4. `### Data / Schema Contract`
   - stores, schemas, tables, collections, files, buckets, prefixes, primary
     keys, foreign keys, indexes, uniqueness, migration owner, and source of
     truth.
5. `### Auth / Authorization Contract`
   - identity principal, token/session type, credential owner, authorization
     boundary, cross-tenant/cross-org leak prevention, and secret handling.
6. `### Lifecycle / State Machine`
   - states, allowed transitions, terminal states, retries, interrupts,
     cleanup, and invalid transition behavior.
7. `### Runtime / Integration Contract`
   - external services, internal service calls, queues, background jobs,
     event streams, polling, timeouts, idempotency, and failure normalization.
8. `### Deployment / Infrastructure Contract`
   - environments, hostnames, branches, image repositories, Kubernetes
     resources, namespaces, Helm/config paths, required env vars, secrets,
     healthchecks, and checked deploy scripts.
9. `### Observability / Proof Contract`
   - logs, metrics, traces, screenshots, browser proof, API proof, DB
     readbacks, artifact locations, and what acceptance evidence means.
10. `### Forbidden And Deferred Operations`
    - operations this design explicitly rejects;
    - decisions intentionally deferred;
    - the gate required before deferred behavior can move into scope.

Use typed tables when a block defines a contract surface. Do not describe
routes, schemas, env vars, or states only in prose when a table would remove
ambiguity.

Route and endpoint tables should use this shape unless a repo-local protocol
defines a stricter one:

| Family | Method | Path | Auth / Principal | Request | Response | Side Effects | Errors | CORS / Preflight | Owner | Proof |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Rules for route tables:

- use exact path strings, including prefixes such as `/v1` or `/v1/flora`;
- list every current route family instead of saying `etc.`;
- state whether a route is browser public, browser authenticated,
  server-to-server, admin-only, healthcheck, or internal;
- state the principal used for authorization;
- state the source of payload truth and whether the route mutates data;
- state the expected error classes, not only success behavior;
- state CORS/preflight behavior for browser-callable routes;
- map each route family to a proof surface.

Data/schema tables should use this shape:

| Store / Schema / Table | Owner | IDs | Key Fields | Relationships | Invariants | Migration Authority | Proof |
| --- | --- | --- | --- | --- | --- | --- | --- |

Deployment/env tables should use this shape:

| Resource / Env Var | Environment | Required | Default | Secret | Owner | Source | Proof |
| --- | --- | --- | --- | --- | --- | --- | --- |

Lifecycle/state tables should use this shape:

| State | Meaning | Entered By | Allowed Next States | Forbidden Next States | Cleanup / Timeout | Proof |
| --- | --- | --- | --- | --- | --- | --- |

Design docs may have additional typed tables for UI information architecture,
background jobs, events, files, buckets, queues, plugins, tools, or permissions
when those surfaces are part of the adopted architecture. The rule is the same:
canonical names, owners, source of truth, allowed operations, forbidden
operations, and proof must be explicit.

Blueprint consistency rules:

- Use the same nouns across related design docs. If a term changes, record the
  rename and the old term's status.
- Prefer one narrow active design anchor per subsystem area over one giant doc
  that hides unrelated decisions.
- A central entrypoint design may link narrower anchors, but it must not
  duplicate their detailed contracts unless it is intentionally summarizing
  them.
- If a plandoc needs a new route, table, env var, lifecycle state, namespace,
  permission, or proof meaning that is missing from the active design, update
  the design first or in the same coherent doc-first slice.
- If two active design docs describe the same route, schema, state, or deploy
  surface differently, that is a blocking contradiction. Audit and repair the
  anchors before admitting implementation.

State meanings and minimum requirements:

- `Draft`
  - Purpose: propose or refine an architectural position.
  - Minimum: problem is stated, constraints are visible, options are considered, a concrete decision is proposed, and major open questions are either listed or explicitly bounded.
  - Not yet true: this is safe to treat as architectural truth for implementation.

- `Active`
  - Purpose: define the currently adopted architectural truth.
  - Minimum: key decisions are resolved, consequences are explicit, scope and
    non-scope are clear, linked plandocs can implement against it without major
    interpretive drift, no lock-critical open question remains inside the
    adopted behavior, and any superseded design is archived or clearly
    displaced.
  - Requirement while in state: keep it aligned with implementation and linked plandocs; do not let code silently outrun it.

- `Archived`
  - Purpose: preserve superseded or historical architectural context.
  - Minimum: replacement or reason for archival is clear, and the doc is no longer presented as current truth.

Design doc review standard:

- does the doc constrain important structural choices tightly enough?
- are invariants and non-goals explicit?
- are tradeoffs and rejected options visible?
- are owners, canonical names, identifiers, states, allowed operations,
  forbidden operations, and proof meanings explicit enough to prevent
  incompatible implementations?
- are open questions limited to genuinely deferred behavior, instead of
  overlapping with the behavior being adopted or locked?
- can a plandoc implement against it without inventing architecture?
- are linked plandocs pointing at this same central anchor instead of forking
  local design truth?
- does the maintenance log show whether recent landed or blocked work changed
  the design meaning?

If the answer to any of those is no, keep the doc in `Draft`.

Relationship to plandocs:

- plandocs execute against design docs
- non-trivial plandocs must name their design anchor explicitly
- non-trivial plandocs must include a `## Design Anchor Review`
- every non-trivial change still needs a plandoc
- if implementation changes architecture, update the design doc first or in the same change
- if a plandoc and design doc disagree, resolve that conflict explicitly rather than letting implementation choose silently
- when a plandoc lands or blocks on a semantic contradiction, record the design
  callback result in the plan and either update the active design, start a
  successor design, or explicitly decide that no anchor change is needed

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

## Native Review Authority

Review is a native phase of this protocol. It is not owned by a separate skill.
Use the native review / readiness gate below for plandoc and design-doc review.

## Native Review / Readiness Gate

Use this gate before moving any non-trivial plandoc to `Approved`, `QA`, or
`Resolved`, and before adopting a design doc as an active anchor.

Required plandoc review checks:

- Outcome: one primary outcome is identifiable, valuable at the landing point,
  and stated as new truth rather than activity.
- Deliverables: every deliverable is concrete, checkable, and mapped to a
  consumer, route, command, artifact, or state change.
- Landing slice: `## Landing Slice / Stopping Point` states exactly what lands
  now and what remains deferred.
- Acceptance: acceptance criteria are falsifiable and prove the outcome rather
  than restating implementation tasks.
- Implementation shape: touch points are concrete and do not rely on hidden
  assumptions about current behavior.
- Verification: verification maps back to deliverables and acceptance criteria;
  unresolved proof gaps are named as QA gaps or blockers.
- Anchor lock: `## Design Anchor Review` records the active anchor decisions
  that constrain the slice, not only the anchor path.
- Semantic prep: durable architecture, vocabulary, ownership, route, schema,
  lifecycle, rollout, security, privacy, and acceptance meaning needed by the
  slice is present in the design anchor or explicitly blocked/deferred there.

Required design-doc review checks:

- the design states exactly one adopted architecture for the scope it governs
- scope and non-scope are explicit enough for adjacent teams
- owners are named for behavior, data, routes, services, deployments,
  lifecycle state, and proof surfaces where relevant
- canonical names are explicit: routes, tables, schemas, env vars, namespaces,
  statuses, identifiers, events, and state transitions
- allowed, forbidden, and deferred operations are distinguished
- invariants are written as non-negotiable rules, not preferences
- open questions do not overlap with locked behavior
- linked plandocs can derive proof meaning from the design without inventing
  local acceptance semantics

Blocking findings:

- no single primary outcome is identifiable
- deliverables are missing or only describe file edits
- the stopping point is implicit
- acceptance criteria are not independently testable or reviewable
- verification does not prove the claimed outcome
- deferred work is implicit
- required operating truth is hidden in `Summary`, `Brief`, `Overview`, or
  `Notes`
- a design doc is marked `Active` or locked while still allowing materially
  different implementations
- a plandoc contains architecture, vocabulary, ownership, route, schema,
  rollout, security, or acceptance meaning absent from its design anchor
- a generated plandoc is only loosely related to its design anchor instead of
  locked to anchor decisions and vocabulary
- a non-trivial plandoc is moved toward approval, activation, QA, or resolution
  without semantic prep ending in `clear`, `blocked`, or `deferred`

Review output should lead with findings and end with the allowed next state:

- `Verdict:` `Pass`, `Fail`, or `Blocked`
- `Allowed Next State:`
- `Blocking Findings:`
- `Required Rewrites:`
- `Missing Evidence:`

When a durable review artifact is required, write it under `.plandoc/reviews/`
using the review artifact protocol below.

## Review Artifact Protocol

Review artifacts are durable evidence docs. They are not plandocs, and they are not design docs.

Use a review artifact when the work product is primarily:

- code review
- module or subsystem scoring
- smell-sweep findings
- architecture-health review
- quality-rating evidence that should survive chat history

Non-negotiable rules:

- If review or scoring work happens in a repo and repo writes are allowed, you MUST write the artifact under `.plandoc/reviews/`.
- Do not treat the chat reply as a substitute for the artifact.
- Do not give a final review or final score until the artifact exists on disk.
- If repo writes are blocked, the review is blocked unless the user explicitly approves a different durable location.
- Findings must lead the review result. Order them by severity.
- Every real finding must include exact file references, the exact mismatch, the likely runtime or maintenance consequence, and the recommended correction.
- Keep summaries, open questions, or change notes after the findings, not before them.

File contract:

- filename: `YYYY-MM-DD-<scope-slug>-code-review.md`
- location: `.plandoc/reviews/`

Required sections, in order:

1. `# Code Review: <scope>`
2. `## Scope`
3. `## Review Mode`
4. `## Profile`
5. `## Evidence`
6. `## Findings`
7. `## Actions Taken`
8. `## Verification`
9. `## Score`
10. `## Decision`
11. `## Next Actions`

`## Actions Taken` is mandatory every time. For read-only work, write `none; review-only`.

Allowed `## Decision` values:

- `review-only`
- `changes requested`
- `changes applied`
- `blocked`

Use [references/review_artifact_protocol.md](references/review_artifact_protocol.md) for the canonical filename rule, section semantics, and reply contract.
Use [references/cross_project_contract_review.md](references/cross_project_contract_review.md) when the scope crosses repo or boundary-owner lines.

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

## Deep Refine / Semantic Prep (Required For Non-Trivial Work)

`Prep` is not a separate lifecycle state. Treat `prep` as a user-facing alias
for deep `refine`.

The purpose of deep refine / semantic prep is to lock in semantic clarity
before execution. It is not administrative cleanup. It must prove that durable
meaning lives in the design anchor and that the plandoc only executes a bounded
slice against that meaning.

Run a deep refine / semantic prep before:

- cross-cutting plan/design space refiles
- large or risky implementation plans
- architecture changes
- compatibility or packaging work
- any task where stale docs may mislead execution
- any attempt to move a plandoc from `Todo + Refined` to `Todo + Approved`
- any MVP, milestone, design-lock, or acceptance-lock checkpoint

Deep refine / semantic prep minimum:

1. Read the current source of truth docs and design anchor first.
2. Audit the relevant code/docs/tests, not just the existing plan text.
3. Separate current behavior from intended behavior.
4. Identify actual touch points and stale assumptions.
5. Identify any choices that are still vague enough to produce materially
   different implementations, and decide whether that ambiguity belongs in the
   design anchor instead of the plandoc.
6. Move durable meaning out of the plandoc and into the design anchor:
   owners, names, routes, schemas, lifecycle states, allowed/forbidden
   operations, security/privacy posture, rollout meaning, and proof/acceptance
   semantics.
7. Refresh the plandoc `## Design Anchor Review` and record whether the anchor
   needs no action, clarification, a successor design, a split, or archival of a
   superseded anchor.
8. If the anchor is stale or under-specified, refine the design doc before
   approving the plandoc.
9. Name the primary outcome, deliverables, and first truthful landing slice.
10. Reclassify artifacts as plan vs design where needed.
11. Record a canonical `Semantic prep:` entry in the relevant plan
    `## Implementation Log`.

A semantic prep pass must end in one of three truthful outcomes:

- `clear`: the design anchor is watertight enough for the current slice
- `blocked`: one exact design ambiguity blocks approval or activation
- `deferred`: the ambiguity is explicitly out of scope for the current slice
  and has an owner/gate before it can enter scope

For legacy doc-space refiles, the deep refine should answer:

- which files are execution plans
- which files are design docs
- which files are current vs historical
- which states are supported by the evidence on disk

Do not invent completion state or certainty that the docs do not support.

## Approval Gates

Before any substantial code edits under a plandoc:

- produce an Implementation Contract covering:
  - what / why
  - outcome
  - deliverables
  - landing slice / stopping point
  - invariants / non-negotiables
  - touch points
  - tests to add or modify
  - verification plan
  - rollout / flags / migrations
- risks + rollback
- wait for explicit approval

Docs-only refactors do not require a code-implementation approval gate, but they still require a deep refine when cross-cutting.

Sprint admission normally happens after this gate. A plandoc that still cannot satisfy the sprint admission rules is not ready to be pulled into the current window.

## Enforcement

Before moving a non-trivial plandoc into `Approved`, `QA`, or `Resolved`:

- perform the native review / readiness gate in this skill
- treat any missing primary outcome, missing deliverables, missing landing slice, vague deferral, or unmapped verification as a blocking defect
- treat a missing or stale `## Design Anchor Review` as a blocking defect
- treat missing semantic prep as a blocking defect when the plan is non-trivial:
  the review must be able to say whether the design anchor is `clear`,
  `blocked`, or `deferred` for the current slice
- reject the transition if the plan contains durable design meaning that is not
  present in the central design anchor
- when the filesystem is available, run the native structure lint:
  `python3 plandoc-protocol/scripts/plandoc_structure_lint.py <plandoc.md>`
- do not advance the plandoc while the lint still reports structural errors
- lint passing is necessary but not sufficient; human review must still reject
  missing design anchors, underspecified scope, hidden second outcomes, or weak
  acceptance criteria
- if a repo-local template still uses older headings, rewrite the template or rework the plandoc rather than silently exempting it

## Plan Smells (Reject Or Rework)

Keep a plandoc in `refine` or return it from `review` if any of these are true:

- the title says `cleanup`, `hardening`, `follow-up`, `parity`, or `refactor`, but the primary outcome is not explicit
- the plandoc cannot answer what exact new truth is true if the current slice lands and work stops there
- `## Acceptance Criteria` mostly restates implementation steps rather than outcomes
- there are multiple independent deliverables with different consumers, rollout shapes, or proof paths in one plandoc
- the plan names many files but does not state the one user-visible, operator-visible, or system-visible result
- the sprint is being framed as a theme, initiative, or bucket of tasks instead of named landing slices with explicit stop truth
- the plandoc has no design anchor, or the plan is carrying architecture,
  vocabulary, contract, route, schema, rollout, security, or privacy truth that
  belongs in a design doc
- `## Design Anchor Review` is missing, stale, vague, or says the anchor needs
  action before the plan can safely proceed
- the design anchor is still `Draft` but the plandoc is being moved to
  `Approved`, `Active`, `QA`, or `Resolved`
- multiple plandocs for the same feature point at different active design docs
  without an explicit supersession story
- several plandocs repeat the same architecture explanation because the central
  anchor is under-specified
- `QA` is being used as a parking state without exact proof gaps and exit checks
- `Resolved` does not name what landed and what, if anything, remains deferred
- the plan was silently rewritten after implementation to match what happened instead of recording drift and re-baselining honestly
- the document relies on a `summary`, `overview`, `brief`, or `notes` section to communicate key intent that should instead live in required operating sections

If a plandoc smells wrong, do not advance it just because the next work feels obvious.

## Strict Templates

### Plandoc required sections

1. Header (`Status`, `State`, `Type`, `Priority`, `Owner`, `Design Anchor`, `Links`, `Created`)
2. `## Context`
3. `## Design Anchor Review`
4. `## Outcome`
5. `## Deliverables`
6. `## Goals / Non-Goals`
7. `## Current Behavior`
8. `## Proposed Approach`
9. `## Landing Slice / Stopping Point`
10. `## Deferred / Not In This Slice`
11. `## Implementation Plan`
12. `## Acceptance Criteria`
13. `## Verification & Monitoring`
14. `## Rollback`
15. `## Invariants / Non-Negotiables`
16. `## Risks / Open Questions`
17. `## Resolution` or repo-local resolved equivalent
18. `## Implementation Log`

Template notes:

- `## Acceptance Criteria` should use stable IDs (`AC1`, `AC2`, ...)
- `## Verification & Monitoring` should map evidence back to those criteria
- `## Deliverables` should use stable IDs (`D1`, `D2`, ...)
- `## Outcome` must be exactly one primary outcome sentence for the plandoc
- `Design Anchor` must point to an active design doc before approval unless an
  allowed `N/A` exception is stated with a reason
- `## Design Anchor Review` must record the current anchor state, consistency
  decision, and required anchor-maintenance action
- `## Landing Slice / Stopping Point` must state the exact truth that becomes true if execution stops after the current slice
- any plandoc with `Status: Icebox` must include `## Icebox Exit Criteria` immediately before `## Implementation Log`
- `## Icebox Exit Criteria` must name the gates, the signals to watch, and the target next `Status` + `State` once the gates open
- any plandoc with `Status: QA` must include `## QA Gaps` immediately before `## Implementation Log`
- any plandoc with `Status: Resolved` must include `## Resolution` or repo-local equivalent immediately before `## Implementation Log` or in the local protocol-approved closing position
- no section named `Summary`, `Overview`, `Brief`, or `Notes` may carry required operating truth that is missing from the required sections

### Design doc required sections

Header (minimum):

- `State`
- `Owner`
- `Last Updated`

1. `## Problem Statement`
2. `## Scope / Anchor Boundary`
3. `## Linked Plandocs`
4. `## Constraints / Invariants`
5. `## Options Considered`
6. `## Decision`
7. `## Consequences`
8. `## Rollout / Migration`
9. `## Security / Privacy Notes`
10. `## Drift Watch / Open Questions`
11. `## Maintenance Log`

Every required section must be filled or explicitly `N/A — reason`.

For active or locked design docs, the section standard is stricter than
presence:

- `## Scope / Anchor Boundary` must make the interpretation boundary explicit,
  including what this design does not decide.
- `## Constraints / Invariants` must name non-negotiable rules, not preferences.
- `## Decision` must contain the adopted contract, including canonical owners,
  names, identifiers, states, allowed operations, forbidden operations, and
  deferred gates where relevant.
- `## Drift Watch / Open Questions` must not contain questions that can change
  the locked behavior. Such questions keep the doc in `Draft` unless they are
  explicitly out of scope for the current lock.

`## Maintenance Log` should capture design-anchor reviews from landed,
blocked, or superseding plandocs. It is not an execution log; it records how
the canonical design truth changed or why it intentionally did not change.

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
- `refine` / `prep` = deepen an existing plan/design doc after reading the
  relevant sources, move durable meaning into the design anchor, and classify
  the design-anchor state as `clear`, `blocked`, or `deferred` for the current
  slice
- first `review` = review the plan/design for readiness
- `activate` = preflight + move `Todo + Approved -> Active + Implementing`
- `implement` = execute the approved plan
- `verify` = review implementation and evidence against acceptance criteria
- `resolve` = move the plan to `Resolved + Resolved`

Use `sync-protocol` when the task is about the protocol itself, templates,
indexes, control boards, durable comms, or refiling the doc space.

## Operational Verbs

Use these verbs exactly in prompts:

- classify the target first: plandoc, design doc, or protocol/doc-space work
- `seed` = create a new plandoc or design doc in the correct folder and initial state
- `refine` = enrich or restructure an existing plandoc or design doc without implementation; `prep` is an alias and must perform the same semantic-clarity work
- `review` = review a plandoc or design doc for readiness, gaps, and protocol compliance
- `activate` = preflight + move `Todo + Approved -> Active + Implementing`
- `implement` = execute approved plan work
- `verify` = review implementation against acceptance criteria and evidence
- `resolve` = move an accepted plan to `Resolved + Resolved`
- `sync-protocol` = update repo-local protocol docs, templates, indexes,
  control-board/comms docs, or doc-space structure

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
