# Durable Comms Protocol

Use `.plandoc/comms/` for cross-owner handoffs that must survive pane churn,
prompt loss, delayed pickup, or local plandoc-only state changes.

## Layout

- `open/` - active requests waiting for acknowledgement or action
- `acked/` - requests whose receiver has accepted ownership or started work
- `closed/` - finished or superseded requests kept for history
- `templates/message.md` - canonical starting template for new threads

## Rules

- one bounded ask per message file
- keep local plandoc and `_index.md` truth updated separately from the comm
- do not create a duplicate thread when an open or acked thread already covers
  the same next owner and same bounded ask
- if the handoff depends on a live worker, include current tmux location and
  repo path under `Current Truth` or `Evidence`
- live transport such as tmux may point a worker at the comm, but does not
  replace the comm as source of truth

## Required Fields

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

## Filename Shape

Use:

`YYYY-MM-DDTHHMMSSZ--from--to--slug.md`

Keep the basename unchanged when moving a thread between `open/`, `acked/`,
and `closed/`.
