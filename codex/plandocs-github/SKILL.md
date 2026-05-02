---
name: plandocs-github
description: GitHub front desk for plandoc-governed work. Use to triage GitHub issues or PRs, keep comments/status scoped and evidence-backed, and escalate substantial or design-bearing work into plandoc-protocol; not for bypassing design anchors, approval gates, or implementation planning.
---

# Plandocs GitHub

## Intent
Use GitHub Issues/PRs as the primary interface **without** losing rigor.

This skill is the "front desk". For complex work, it escalates into the "engine room" (Plandocs/Design Docs).

## Prime directive
- Make the next action obvious.
- Prefer short, testable acceptance criteria.
- Never start substantial code without an approval gate.

## Icebox Exclusion

Issues or tickets labeled `icebox` are not active intake.

- Do not assess, refine, propose, implement, check, comment on, close, route,
  or count an `icebox` item as remaining work.
- Do not create a prep plandoc for an `icebox` item.
- The item re-enters the workflow only when the human manually removes the
  label or explicitly names the exact issue to lift out of icebox.
- Record the manual lift in the governing issue-control or board before
  routing work.

## Rigid verbs (lifecycle)
Use these verb names exactly.

### `assess`
Doc-only triage.
- Classify: bug | enhancement | design | infra | question
- Scope: small (1–2 files) | medium (3–8) | large (9+ or cross-repo)
- Identify likely touch points (paths), risks, and the fastest safe path.
- Output: a single issue comment with classification/scope, suspected root cause/surface, and recommendation.

### `refine`
Doc-only: convert issue into implementation-ready spec.
Must include:
- Ordered steps (each step has file paths)
- Acceptance criteria (testable)
- Verification commands
- Rollback notes (even if trivial: “revert commit”)

### `propose` (approval gate)
Doc-only: Implementation Overview.
Required fields:
- What / Why
- Touch points (every file)
- Tests
- Verification plan
- Rollout/migration
- Risks + rollback
Then wait for explicit approval.

### `implement`
Make changes + open PR.
Rules:
- PR must reference the issue (`Closes #N`).
- Keep commits reviewable.
- If scope expands: stop and re-propose.

### `check`
Post-implementation verification.
Must include:
- Commands run + results
- Manual checks performed
- Evidence links/screenshots if UI
- Verdict: pass | partial | fail

## Escalation to Plandocs/Design Docs (hard triggers)
Escalate when ANY:
- large scope (9+ files) or multi-PR
- cross-repo
- schema changes
- auth/security/privacy
- non-obvious rollback
- new protocol/architecture decisions

Design-anchor rule:
- When escalation creates or refines a plandoc, the plandoc must be locked to
  an active design anchor before implementation approval.
- Design docs are the architecture blueprints for ticket work. If an issue
  needs system structure, product-object relationships, lifecycle boundaries,
  route/schema/service contracts, deployment topology, information
  architecture, or proof semantics, update or create the `.plandoc/design/`
  anchor first.
- If no active design anchor contains the needed durable meaning, create or
  refine the design doc first and keep the plandoc in a seeded/refined state.
- Do not let a GitHub issue title or issue comment become the hidden source of
  architecture, schema, route, security, rollout, or acceptance meaning.

Escalation output:
- Create plandoc at the repo's canonical plandoc path, usually
  `.plandoc/plans/todo/NNNN-...md`
- Link bidirectionally (issue ↔ plandoc)
- Record the exact GitHub issue title in the plandoc in a visible
  `## GitHub Ticket Names` section. For multi-issue plandocs, list every
  source issue as `#<number>: <exact GitHub issue title>`.
- Keep GitHub issue as the public wrapper

## Related Use

- Use `$plandoc-protocol` when the issue is large, cross-repo, design-bearing,
  migration-bearing, or needs durable state transitions.
- Use the native `$plandoc-protocol` review / readiness gate before approving
  or activating a non-trivial plandoc.
- Use `$verification-before-completion` before claiming the GitHub issue or PR
  is complete.

## Comment template (use every time)
```md
## [verb] — [title]

**Classification**: ...
**Scope**: small|medium|large

### Summary
...

### Touch points
- `path/to/file` — what changes

### Acceptance criteria
- [ ] ...

### Verification
- `command` → expected

### Rollback
...

---
*`plandocs-github` · [verb] · YYYY-MM-DD*
```
