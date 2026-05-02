# Plandoc Protocol Canon Index

This directory is the canonical, tool-agnostic protocol source.

Codex and Hermes adapters must derive protocol meaning from this directory. If
adapter wording changes the meaning of plandocs, design anchors, audits,
control-board artifact shape, durable comms, issue intake, state transitions,
or proof-backed closure, update this canon first.

## Authority Boundary

Plandoc protocol owns artifact and lifecycle semantics:

- what a design doc is;
- what a plandoc is;
- what a control-board document must contain;
- what a durable comm artifact must contain;
- how audit and sweep work;
- how GitHub issues enter and leave plandoc-governed work;
- what cut, slice, and landing slice mean;
- what proof-backed closure means.

Plandoc protocol does not own live orchestration:

- no tmux pane discovery;
- no worker prompt delivery;
- no live callback intake;
- no WIP enforcement;
- no lane parking or rebinding;
- no "who works now" decision.

Those live operations belong in `ctrl-protocol`, which consumes this protocol.

## Canon Documents

- `design-docs.md`
  - Design docs are architectural blueprint anchors.
  - They own durable architecture, vocabulary, ownership, invariants,
    accepted/rejected options, and proof meaning.

- `plandocs.md`
  - Plandocs are bounded execution documents.
  - They execute slices against design anchors and must not invent durable
    architecture.

- `audit.md`
  - Audit and sweep are first-class plandoc-protocol modes.
  - Audit deeply verifies document claims, contradictions, drift, overlap, and
    missing anchors.
  - There is no separate rest-audit skill; use `plandoc-protocol audit`.

- `control-boards.md`
  - Defines the control-board artifact shape.
  - Does not define live routing behavior.

- `durable-comms.md`
  - Defines durable handoff artifact shape.
  - Does not choose live owner, priority, or transport.

- `github-issues.md`
  - Defines GitHub issue intake, preparation, proof, comments, and closeout
    discipline.

## Adapter Rule

Adapters under `../codex/` and `../hermes/` are packaging surfaces. They may
summarize and route to this canon, but they must not become hidden sources of
protocol truth.

When changing behavior:

1. Update the canon document in this directory.
2. Update affected Codex and Hermes adapters.
3. Validate adapters.
4. Commit the canon and adapter change together.
