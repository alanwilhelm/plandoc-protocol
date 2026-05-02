# Local Plandoc Protocol

`{{PROJECT_NAME}}` uses `.plandoc/` as the local source of truth for planning and design state.

Use this as the first local reference before generic defaults.

## Layout

- `.plandoc/plans/` - execution plans
- `.plandoc/design/` - architecture and decision docs
- `.plandoc/reviews/` - durable review artifacts and score-backed review evidence
- `.plandoc/comms/` - durable cross-owner handoffs when a message must survive
  chat or tmux churn

## Operating Rules

- keep each plandoc anchored in one explicit `Status` + `State`
- keep each design doc anchored in one explicit `State`
- write review and scoring artifacts to `.plandoc/reviews/`, not chat alone
- use `.plandoc/comms/` for durable cross-owner handoffs; do not treat tmux or
  chat as the only source of truth when a handoff must survive
- use findings-first review artifacts; for contract audits, compare producer and consumer sides explicitly
- keep `_index.md` aligned with actual lifecycle state
- treat design docs as architecture truth and plandocs as execution truth
- treat review artifacts as durable review evidence, not execution plans
- treat a control board as an official plandoc role only when this repo or
  workspace is actively coordinating multiple lanes
- verify outcomes before claiming closure
