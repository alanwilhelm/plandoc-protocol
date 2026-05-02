# Control Boards

Control boards are plandoc artifacts used for live coordination.

This protocol defines the required artifact shape:

- active mission
- current critical path
- WIP cap
- active, parked, blocked, and support-only lanes
- next legal moves
- illegal moves
- implementation log
- design-anchor review

Live lane routing, tmux execution, callback dedupe, and worker control belong
to `ctrl-protocol`.
