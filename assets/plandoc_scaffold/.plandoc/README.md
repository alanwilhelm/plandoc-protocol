# Local Plandoc Protocol

`{{PROJECT_NAME}}` uses `.plandoc/` as the local source of truth for planning and design state.

Use this as the first local reference before generic defaults.

## Layout

- `.plandoc/plans/` - execution plans
- `.plandoc/design/` - architecture and decision docs

## Operating Rules

- keep each plandoc anchored in one explicit `Status` + `State`
- keep each design doc anchored in one explicit `State`
- keep `_index.md` aligned with actual lifecycle state
- treat design docs as architecture truth and plandocs as execution truth
- verify outcomes before claiming closure
