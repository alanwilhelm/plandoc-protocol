# Audit And Sweep

Audit and sweep are first-class plandoc-protocol modes.

There is no separate rest-audit skill. Use `plandoc-protocol audit`.

## Vocabulary

- `audit`: rigorous deep refinement of a plandoc, design doc, control board, or
  related plan set. Extract claims, verify them against current truth, find
  contradictions, contract inconsistencies, drift, and overlap, then repair or
  recommend repair with evidence.
- `sweep`: lighter bounded consistency scan. Use for naming, status, links,
  obvious stale references, queue-shape checks, or candidate drift discovery.
- `resting document`: a plan, design doc, control board, review, or comm that
  is not currently being implemented. Common examples are plans in `todo/`,
  `blocked/`, `qa/`, `resolved/`, or parked/approval-gated board lanes.

If the user asks for deep refinement, correctness, overlap analysis, plan
quality, plan cleanup, logical contradictions, contract inconsistencies, or
"while they are at rest", use `audit`, not `sweep`.

## Audit Contract

An audit:

- extracts every important claim, assertion, and supposition;
- verifies claims against current code, tests, docs, tickets, checked scripts,
  deployment truth, and read-only live state when available;
- detects logical contradictions and contract inconsistencies;
- aligns boundaries with neighboring plans and design docs;
- detects overlap, drift, stale wording, stale evidence, and hidden
  architecture;
- updates the audited document with evidence-backed corrections when the edit
  is safe and in scope;
- records a review finding or follow-up plandoc when correction requires code,
  design, ownership, approval, deploy, or credentialed work;
- leaves one deterministic next legal move.

This is not live execution. Do not start implementation, deploy, apply
migrations, restart runtimes, run browser proof, close GitHub issues, or notify
testers from audit mode unless a separate approved execution slice explicitly
permits that action.

## Claim Ledger

Treat important document assertions as claims and classify each one:

- `confirmed`: current code, checked script output, live read-only state, or
  current issue state supports the claim.
- `contradicted`: current truth disagrees with the claim.
- `missing`: the document asserts or depends on something that current code or
  evidence does not prove.
- `ambiguous`: available evidence is incomplete, wording is too loose, or
  verification is gated.

Do not confirm a claim from old callback text, stale plan status, or
plausibility. Confirm only with evidence.

For every important claim, ask:

- Does this contradict another claim in the same document?
- Does this contradict the active design anchor, repo-local design, control
  board, checked script contract, schema, route, deployment, or live readback?
- Does it use the same word for two different concepts, or two words for one
  concept?
- Does a proposed next step violate a boundary, invariant, approval gate, or
  failure class defined elsewhere?

Classify those as `contradicted` or `ambiguous`; do not smooth them over as
style issues.

## Document Selection

For recurring audit work, choose the next document in this order:

1. active control board or current board/index pointers;
2. active shared design anchors for the current sprint or blocked lane;
3. repo-local design docs linked by the board or candidate plan;
4. repo-local resting plans in `todo/`, `blocked/`, `qa/`, or parked lanes;
5. resolved plans only when they are being reused as anchors or evidence.

For recurring watchdog or cron use, audit one document per run. A manual
one-off audit may cover multiple related documents only when the user asks for
that explicitly.

If the item is actively being implemented, switch to live CTRL/workspace lane
control instead of audit mode.

Do not audit `icebox` issues or their plans unless the user explicitly lifts
the exact issue out of icebox.

## Audit Workflow

1. Bind the audit scope.
   - Name the exact plan, design anchor, repo, issue, or board lane.
   - Classify each item as resting, active, blocked, approval-gated,
     validation-wait, resolved, stale, or orphaned.

2. Read governing protocol and anchors.
   - Read repo/root `AGENTS.md` and local `.plandoc/README.md` when present.
   - Read the plan header, `Design Anchor`, `## Design Anchor Review`,
     `## Outcome`, `## Deliverables`, `## Landing Slice / Stopping Point`,
     `## Acceptance Criteria`, `## Verification`, `## Rollback`, and
     `## Deferred / Not In This Slice`.
   - Read the active design anchor before judging whether the plan is correct.

3. Extract claims.
   - List important assertions about code, schema, routes, services,
     Kubernetes resources, scripts, tests, issue status, deployment, ownership,
     acceptance, or user-visible behavior.
   - Separate durable design claims from execution claims and volatile
     evidence.
   - Classify each claim as `confirmed`, `contradicted`, `missing`, or
     `ambiguous`.

4. Verify current truth.
   - Prefer current code, tests, checked scripts, live read-only probes, and
     current GitHub issue state over old callback text.
   - Use `rg`, `git show`, checked readback/plan commands, and read-only
     inspection commands first.
   - If live verification would mutate or need credentials, mark that exact
     verification as gated instead of guessing.

5. Check boundary alignment.
   - Compare neighboring plans and design docs for duplicate ownership,
     contradictory vocabulary, stale path/status, hidden architecture, missing
     deferrals, or overlapping acceptance criteria.
   - Confirm the plan does not claim work outside its owner/repo/lane.
   - Confirm design docs define the architectural contract and plans only
     execute bounded slices against it.
   - Explicitly identify internal contradictions, cross-document
     contradictions, code-vs-doc contradictions, stale evidence treated as
     current truth, and next-step actions that violate the claimed contract.

6. Refine from evidence.
   - Tighten vague claims into testable invariants when evidence supports them.
   - Add explicit caveats where the document overstates certainty.
   - Add safer implementation ideas only when they follow directly from current
     code or checked readback.
   - Do not invent new architecture or bury product meaning in a plan.

7. Repair or record findings.
   - For safe doc-only corrections, update the plandoc/design doc directly.
   - For higher-risk architectural disagreement, create or update a review
     artifact under `.plandoc/reviews/` and name the required repair slice.
   - For implementation fallout, create or update a plandoc that plans the code
     edits; do not start code from audit mode.

8. Leave a deterministic result.
   - State whether the audited item is ready, blocked, stale, superseded,
     needs design repair, needs issue refresh, or needs explicit approval.
   - Name the next legal move as one bounded transition.

## Required Output Shape

For each audited item, produce:

- `Status`: ready / needs-refine / needs-design-repair / blocked /
  approval-gated / stale / superseded.
- `Claim checks`: key claims verified or contradicted.
- `Boundary findings`: overlap, drift, missing anchor, or neighboring-plan
  conflicts.
- `Contradictions / inconsistencies`: internal contradictions, cross-anchor
  conflicts, code-vs-doc mismatches, or `none found`.
- `Edits made`: exact files changed, or `none`.
- `Next legal move`: one bounded next step.
- `Verification`: commands/readbacks run, and what could not be verified.

For recurring watchdog/cron output, keep the report short:

- `Document reviewed`
- `Claims confirmed / contradicted / missing / ambiguous`
- `Bounded update made`
- `Next document to audit`

If nothing materially changed and the caller requested quiet recurring mode,
return `[SILENT]`.

## Cron Prompt Shape

Use this shape for recurring plan consistency jobs:

```text
Use $plandoc-protocol audit. Audit one resting workspace design or plan document
at a time. First identify the next resting document from the workspace indexes,
active control board, and resting plandocs. Validate each concrete claim
against current code truth, repo status, checked readback/plan output, or live
read-only workspace state. Actively search for internal logical contradictions,
cross-document contract inconsistencies, stale evidence being treated as
current truth, and next-step actions that violate the governing anchor. Confirm
claims only when evidence supports them.
Refine the document only when the evidence justifies a tighter boundary,
clearer invariant, safer implementation idea, or explicit caveat. Do not batch
multiple documents in one run. Do not start implementation, deploy, close
issues, notify testers, or schedule another cron job. Report the document
reviewed, claims confirmed/contradicted/missing/ambiguous, any bounded update
made, and the next document to audit. If nothing materially changed, return
[SILENT].
```
