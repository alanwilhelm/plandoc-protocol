# Repository Guidelines

This is the real upstream skill repo for `plandoc-protocol`.

## Source Of Truth
- Upstream repo: `git@github.com:alanwilhelm/plandoc-protocol.git`
- Publish changes from a remote-backed checkout of this repo.
- Do not treat an ad hoc local tree with no remote as authoritative for publish work.

## Working Rules
- Use SSH git auth for clone/fetch/push. `gh` CLI auth may be broken and is not required.
- When changing the protocol itself, update `SKILL.md` first. Update `agents/openai.yaml` only if the invocation surface or wording must change.
- Keep the repo centered on the skill itself. Treat the optional local scaffold as support, not the primary product.
- Keep the repo portable for Codex/OpenClaw installs. Do not add dependencies to the validation path unless required.

## Validation
- Run `python3 scripts/validate_skill.py`
- Run `python3 scripts/test_validate_skill.py`

## Publish Flow
1. Pull the real upstream repo.
2. Apply protocol/skill changes here.
3. Run validation.
4. Commit with a focused message.
5. Push back to `origin/main` unless a feature branch is required.

## Protocol Guidance
- For intake clarity, the skill should distinguish `Bug`, `Case`, `Feature`, `Task`, `Research`, `Runbook`, and `Decision`.
- Goals, initiatives, epics, and architecture choices should start as design docs before they become execution plandocs.
