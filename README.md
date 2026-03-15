# plandoc-protocol

`plandoc-protocol` is a skill that turns an LLM into a state machine to get more reliable results.

It does that with explicit stages, strict transitions, approval gates, and evidence-backed closure.

## Why It Works

LLMs get sloppy when work has implicit state. This skill makes state explicit.

Core plandoc flow:

```text
Seeded -> Refined -> Approved -> Implementing -> Implemented -> Reviewed -> Resolved
```

Core design-doc flow:

```text
Draft -> Active -> Archived
```

That improves reliability because it forces the model to:

- separate design truth from execution state
- choose one current stage instead of hand-waving progress
- follow allowed transitions instead of improvising workflow
- verify outcomes before claiming closure

## Install

```bash
python3 scripts/install_skill.py --target codex --force
```

The installer also supports OpenClaw, Claude Code, and OpenCode.

## Use

Invoke the skill and use it as a strict workflow engine for:

- `seed`
- `refine`
- `review`
- `activate`
- `implement`
- `verify`
- `resolve`

The public verb surface is intentionally small. The stage model stays rich underneath.

The product is [SKILL.md](SKILL.md).

## Repo Layout

- `SKILL.md` - the protocol itself
- `agents/openai.yaml` - OpenAI/Codex shim
- `scripts/install_skill.py` - skill installer
- `scripts/validate_skill.py` - package validator
- `scripts/test_validate_skill.py` - validator self-tests
- `AGENTS.md` - upstream repo working rules

## Optional Extras

This repo also contains an optional local plandoc scaffold:

- `scripts/install_plandoc_scaffold.py`
- `assets/plandoc_scaffold/`
- `references/plandoc_scaffold.md`

That installer:

- writes `.plandoc/`
- creates `.plandoc/plans/` and `.plandoc/design/`
- patches `AGENTS.md` and `CLAUDE.md` with short entrypoint blocks that point to `.plandoc/README.md`

Ignore it if you only want the skill.

Optional scaffold install:

```bash
python3 scripts/install_plandoc_scaffold.py --repo-root /path/to/repo --project-name MyProject
```

## Validation

```bash
python3 scripts/validate_skill.py
python3 scripts/test_validate_skill.py
```

## Bottom Line

This repo should be read skill-first.

The main claim is simple: `plandoc-protocol` makes LLM work more reliable by turning planning and execution into an explicit state machine.
