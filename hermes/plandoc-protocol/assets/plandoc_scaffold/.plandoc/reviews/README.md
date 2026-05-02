# Review Artifacts

Use `.plandoc/reviews/` for durable review outputs:

- code review
- scoring
- smell sweeps
- architecture-health checks
- cross-project contract audits

Do not treat chat replies as a substitute for these artifacts.

## File Rule

- filename: `YYYY-MM-DD-<scope-slug>-code-review.md`

## Required Sections

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

`## Actions Taken` is required every time. For read-only review, write
`none; review-only`.

## Findings Rule

Lead with findings and order them by severity.

Each real finding should include:

- producer file reference
- consumer file reference when a boundary is involved
- exact mismatch or defect
- likely consequence
- recommended correction
