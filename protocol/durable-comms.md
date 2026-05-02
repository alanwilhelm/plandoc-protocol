# Durable Comms

Durable comms are protocol-backed handoff threads for cross-owner work.

They record:

- sender
- owner
- requested action
- state
- acceptance
- blocker or completion
- evidence
- closeout

Durable comms are not a live routing substitute. Live routing belongs to
`ctrl-protocol`; durable comms preserve the auditable handoff trail.
