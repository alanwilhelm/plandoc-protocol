# GitHub Issues

GitHub issues are front-door work items. Non-trivial issue work must be
classified and prepared before implementation.

Required flow:

1. Read the current issue state.
2. Ignore issues labeled `icebox` unless a human explicitly lifts that exact
   issue out of icebox.
3. Classify the issue as live, stale, superseded, blocked, validation-wait, or
   ready.
4. Create or refine the design anchor when durable meaning is missing.
5. Create or refine the plandoc with the exact issue title and URL.
6. Implement only a bounded approved slice.
7. Post evidence-backed comments only after there is real proof.
8. Do not tag a human validator until the fix is deployed to a testable
   environment.

Issue comments and closeout must stay tied to commits, proof artifacts, and
the governing plandoc.
