# Review Artifact Protocol

This is the canonical review-artifact contract for `$plandoc-protocol`.

Use it whenever the work product is primarily a durable review rather than an
execution plan or design decision.

## What Counts As A Review Artifact

Use `.plandoc/reviews/` for:

- code review
- module or subsystem scoring
- smell sweeps
- architecture-health reviews
- quality-rating evidence that should survive chat history

Do not use a review artifact to track implementation state. That is what
plandocs are for.

Do not use a review artifact to hold architectural truth or strategic
decisions. That is what design docs are for.

## Path Rules

- canonical location: `.plandoc/reviews/`
- canonical filename: `YYYY-MM-DD-<scope-slug>-code-review.md`

If `.plandoc/` does not exist and repo writes are allowed, create
`.plandoc/reviews/` and write the artifact there.

If repo writes are not allowed, the review is blocked unless the user
explicitly approves a different durable location.

## Non-Negotiable Review Rules

- A chat reply is not a substitute for the artifact.
- Do not give a final review or final score until the artifact exists on disk.
- `## Actions Taken` is required every time, including read-only review.
- For read-only review, set `## Actions Taken` to `none; review-only`.
- Findings must lead the review result and be ordered by severity.
- Every real finding must include exact file references, the exact mismatch or defect,
  the likely runtime or maintenance consequence, and the recommended correction.
- Keep summary material, open questions, and change notes after findings rather than
  before them.

## Required Sections

Write sections in this exact order:

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

Allowed `## Decision` values:

- `review-only`
- `changes requested`
- `changes applied`
- `blocked`

Every required section must be filled or explicitly `N/A - reason`.

## Section Semantics

### `## Scope`

State the exact module, directory, subsystem, or repo surface reviewed.

### `## Review Mode`

State the mode explicitly, for example:

- `review-only`
- `review plus fixes`
- `smell sweep`
- `architecture-health check`
- `cross-project contract audit`

### `## Profile`

State the primary evaluation profile when one applies, for example:

- `phoenix-web`
- `domain-context`
- `otp-runtime`
- `adapter-integration`
- `ecto-data`
- `library-core`
- `cross-project-contract`

### `## Evidence`

Record the evidence gathered:

- files or directories inspected
- exact search commands
- exact verification commands
- relevant test, lint, or static-analysis signals

For `cross-project contract audit` mode, also record the boundary map:

- producer surface
- consumer surface
- payload or schema owner
- serializer and deserializer owners
- status, enum, and identifier conventions inspected

### `## Findings`

List findings in severity order when there are real issues.

If there are no findings, state that explicitly.

For each real finding, include:

- severity
- producer file reference
- consumer file reference
- exact mismatch
- likely runtime or maintenance consequence
- recommended correction

### `## Actions Taken`

Record the exact outcome:

- `none; review-only`
- files changed
- tests added
- behavior tightened
- blockers encountered

### `## Verification`

List exact commands run and the result of each command.

### `## Score`

If the review includes scoring, record the score and whether it is `final` or
`provisional`.

If the review does not include scoring, write `N/A - review did not request a
score`.

### `## Next Actions`

State the smallest credible next step, or `none`.

## Minimal Skeleton

```md
# Code Review: <scope>

## Scope

## Review Mode

## Profile

## Evidence

## Findings

## Actions Taken

## Verification

## Score

## Decision

## Next Actions
```

## Final Reply Contract

The final reply for review-mode work must include:

- the artifact path
- the top findings or the no-findings result
- the exact actions taken
- the verification status
- the score if scoring was requested

## Cross-Project Contract Audit Addendum

When the scope spans multiple repos or boundary owners, audit the contract from
both sides.

Focus on:

- payload shapes
- field naming and optionality
- serialization and deserialization behavior
- protocol assumptions
- status vocabularies
- identifier formats
- enum values
- lifecycle and state expectations

Prioritize findings that threaten:

- clean boundaries
- truthful contracts
- long-term architectural consistency

Use [cross_project_contract_review.md](cross_project_contract_review.md) for the
contract-audit checklist and finding template.
