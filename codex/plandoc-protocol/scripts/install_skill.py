#!/usr/bin/env python3
"""Install the skill into Codex, OpenClaw, Claude Code, or OpenCode."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

from validate_skill import validate_skill_root

SUPPORTED_TARGETS = ("codex", "openclaw", "claude", "opencode")
SUPPORTED_SCOPES = ("global", "project")
SUPPORTED_MODES = ("copy", "link")


def expand_home(path: str) -> Path:
    return Path(os.path.expanduser(path)).resolve()


def resolve_destination(
    target: str,
    scope: str,
    skill_name: str,
    project_root: Path | None,
) -> Path:
    if scope == "global":
        if target == "codex":
            return expand_home(f"~/.codex/skills/{skill_name}")
        if target == "openclaw":
            return expand_home(f"~/.openclaw/skills/{skill_name}")
        if target == "claude":
            return expand_home(f"~/.claude/skills/{skill_name}")
        if target == "opencode":
            return expand_home(f"~/.config/opencode/skills/{skill_name}")
    if scope == "project":
        if project_root is None:
            raise ValueError("project scope requires --project-root")
        if target == "codex":
            raise ValueError(
                "project-scope Codex install is not supported here; only the verified global path "
                "~/.codex/skills/<name> is implemented"
            )
        if target == "openclaw":
            return (project_root / "skills" / skill_name).resolve()
        if target == "claude":
            return (project_root / ".claude" / "skills" / skill_name).resolve()
        if target == "opencode":
            return (project_root / ".opencode" / "skills" / skill_name).resolve()
    raise ValueError(f"unsupported target/scope combination: {target}/{scope}")


def remove_existing(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
        return
    if path.is_dir():
        shutil.rmtree(path)
        return
    raise ValueError(f"unsupported existing path type: {path}")


def install_copy(source_root: Path, destination: Path) -> None:
    shutil.copytree(
        source_root,
        destination,
        ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"),
    )


def install_link(source_root: Path, destination: Path) -> None:
    destination.symlink_to(source_root, target_is_directory=True)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--target",
        action="append",
        choices=SUPPORTED_TARGETS + ("all",),
        help="Install target. Repeatable. Defaults to codex if omitted.",
    )
    parser.add_argument(
        "--scope",
        choices=SUPPORTED_SCOPES,
        default="global",
        help="Install globally or into a project-specific skill directory.",
    )
    parser.add_argument(
        "--project-root",
        help="Project root for project-scope installs.",
    )
    parser.add_argument(
        "--mode",
        choices=SUPPORTED_MODES,
        default="copy",
        help="Install by copying files or creating a symlink.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing installed skill at the destination path.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned actions without writing anything.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    skill_root = Path(__file__).resolve().parents[1]
    errors = validate_skill_root(skill_root)
    if errors:
        print("Refusing to install an invalid skill:")
        for error in errors:
            print(f"- {error}")
        return 1

    frontmatter_name = None
    for line in (skill_root / "SKILL.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("name:"):
            frontmatter_name = line.split(":", 1)[1].strip()
            break
    if not frontmatter_name:
        print("Could not determine skill name from SKILL.md", file=sys.stderr)
        return 1

    targets = args.target or ["codex"]
    if "all" in targets:
        targets = list(SUPPORTED_TARGETS)

    seen: set[str] = set()
    ordered_targets: list[str] = []
    for target in targets:
        if target in seen:
            continue
        seen.add(target)
        ordered_targets.append(target)

    project_root = Path(args.project_root).resolve() if args.project_root else None

    install_fn = install_copy if args.mode == "copy" else install_link

    for target in ordered_targets:
        try:
            destination = resolve_destination(target, args.scope, frontmatter_name, project_root)
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 2

        action = f"{args.mode} {skill_root} -> {destination}"
        if args.dry_run:
            print(f"[dry-run] {target}: {action}")
            continue

        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists() or destination.is_symlink():
            if not args.force:
                print(
                    f"Destination exists for {target}: {destination}. Use --force to replace it.",
                    file=sys.stderr,
                )
                return 1
            remove_existing(destination)

        install_fn(skill_root, destination)
        print(f"Installed for {target}: {destination}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
