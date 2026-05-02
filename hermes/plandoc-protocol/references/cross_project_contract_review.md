# Cross-Project Contract Review

Use this protocol when a review spans multiple repos, services, libraries, or
boundary owners.

The point is to find producer/consumer drift before it becomes runtime breakage
or permanent architectural residue.

## Audit Focus

Inspect the shared contract from both sides and compare:

- payload shapes
- field naming
- field optionality and requiredness
- serialization behavior
- deserialization behavior
- protocol and transport assumptions
- status vocabularies
- enum values
- identifier formats
- lifecycle and state expectations

Do not stop at one side of the boundary. A producer-only or consumer-only read
is not enough for this mode.

## Required Evidence Sweep

For each boundary under review, identify:

1. producer owner
2. consumer owner
3. payload builder or serializer
4. payload parser or deserializer
5. schema, typespec, or validation owner
6. tests that prove the contract from both sides

Useful evidence sources include:

- API request and response structs
- JSON encoders and decoders
- Phoenix controllers, views, and LiveViews
- Ecto schemas and changesets
- typed maps, structs, and `@spec`
- adapters and client modules
- event payload builders and subscribers
- status or enum declarations
- migrations that define durable enum or column meaning

## Finding Format

Every real finding must include:

- severity
- producer file reference
- consumer file reference
- exact mismatch
- likely runtime or maintenance consequence
- recommended correction

Template:

```md
- Severity: <high|medium|low>
  - Producer: [path](/abs/path/file.ext:line)
  - Consumer: [path](/abs/path/file.ext:line)
  - Mismatch: <exact contract drift>
  - Consequence: <likely runtime breakage, ambiguity, or erosion>
  - Recommended correction: <smallest truthful fix>
```

## Review Ordering

- findings first
- open questions or assumptions second
- change summary last, if there were changes

Do not front-load a summary before the findings list.

## No-Findings Rule

If no mismatches are found, say so explicitly and still record:

- boundaries checked
- evidence inspected
- residual risk
- verification gaps
