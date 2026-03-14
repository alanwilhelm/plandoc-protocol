# AGENTS.md

This repository is the active working codebase and planning workspace for `{{PROJECT_NAME}}`.

## Current Working Location

- Planning, design docs, vocabulary work, and code changes happen here.
- If there is a source snapshot or reference tree elsewhere, name it explicitly.
- Do not split active work across multiple repos without stating that boundary plainly.

## Project Identity

- `{{PROJECT_NAME}}` is a real technical project, not a branding exercise.
- Use precise technical naming with high naming fidelity.
- Do not use architecture language as marketing copy.

## Writing Standard

- default to clinical candor
- prefer academic precision over sales language
- prefer terse effectiveness over expansive explanation
- remove fluff, hype, and posture
- do not present aspirations as current fact

## Rust Style

Use Rust like intelligent adults:

- prefer concrete structs, enums, modules, and functions
- add a trait only at a real seam
- favor explicit state over stringly typed control flow
- favor typed errors at service and port boundaries
- keep modules small and responsibility-aligned
- write direct behavior tests instead of mock choreography

## Naming Discipline

- names must describe what the thing actually is
- distinguish durable objects from runtime actions
- use `VOCABULARY.md` and `SURFACE_MATRIX.md` to keep terms and ownership coherent

## Documentation Standard

- explain the current system before proposing a better one
- separate current behavior, intended behavior, and deferred work explicitly
- keep examples accurate to the actual runtime surface
- state internal/public naming differences plainly instead of smoothing them over

## Reference Inputs

- list the working codebase here
- list any read-only source snapshot here
- list any architecture or vocabulary reference repos here

Borrow selectively. Do not cargo-cult another repo's complexity.
