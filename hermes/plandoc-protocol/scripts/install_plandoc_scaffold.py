#!/usr/bin/env python3
"""Install the optional local plandoc scaffold into a target repository."""

from __future__ import annotations

import argparse
from pathlib import Path

MANAGED_BLOCK_START = "<!-- BEGIN PLANDOC-PROTOCOL -->"
MANAGED_BLOCK_END = "<!-- END PLANDOC-PROTOCOL -->"
ENTRYPOINT_FILES = ("AGENTS.md", "CLAUDE.md")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root",
        required=True,
        help="Target repository root.",
    )
    parser.add_argument(
        "--project-name",
        help="Project name for template substitution. Defaults to the repo directory name.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing managed scaffold files under .plandoc.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned writes without changing files.",
    )
    return parser.parse_args(argv)


def render_template(text: str, project_name: str) -> str:
    return text.replace("{{PROJECT_NAME}}", project_name)


def write_file(
    destination: Path,
    content: str,
    *,
    force: bool,
    dry_run: bool,
) -> str:
    if destination.exists() and not force:
        return f"skip  {destination}"
    if dry_run:
        return f"write {destination}"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(content, encoding="utf-8")
    return f"write {destination}"


def entrypoint_block() -> str:
    return (
        f"{MANAGED_BLOCK_START}\n"
        "## Local Plandoc Protocol\n\n"
        "Use `.plandoc/README.md` as the local protocol source of truth.\n\n"
        "- Execution plans live in `.plandoc/plans/`\n"
        "- Design docs live in `.plandoc/design/`\n"
        "- Review artifacts live in `.plandoc/reviews/`\n"
        "- Durable cross-owner handoffs live in `.plandoc/comms/`\n"
        "- If local protocol docs exist, follow them over generic defaults\n"
        f"{MANAGED_BLOCK_END}\n"
    )


def upsert_entrypoint(path: Path, *, dry_run: bool) -> str:
    block = entrypoint_block()
    if not path.exists():
        if dry_run:
            return f"write {path}"
        path.write_text(block, encoding="utf-8")
        return f"write {path}"

    original = path.read_text(encoding="utf-8")
    start = original.find(MANAGED_BLOCK_START)
    end = original.find(MANAGED_BLOCK_END)

    if start != -1 and end != -1 and end >= start:
        end += len(MANAGED_BLOCK_END)
        if end < len(original) and original[end:end + 1] == "\n":
            end += 1
        updated = original[:start] + block + original[end:]
    else:
        stripped = original.rstrip()
        if stripped:
            updated = stripped + "\n\n" + block
        else:
            updated = block

    if updated == original:
        return f"skip  {path}"
    if dry_run:
        return f"patch {path}"
    path.write_text(updated, encoding="utf-8")
    return f"patch {path}"


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    repo_root = Path(args.repo_root).expanduser().resolve()
    project_name = args.project_name or repo_root.name
    skill_root = Path(__file__).resolve().parents[1]
    template_root = skill_root / "assets" / "plandoc_scaffold"

    directories = [
        repo_root / ".plandoc" / "plans" / "todo",
        repo_root / ".plandoc" / "plans" / "active",
        repo_root / ".plandoc" / "plans" / "qa",
        repo_root / ".plandoc" / "plans" / "resolved",
        repo_root / ".plandoc" / "plans" / "icebox",
        repo_root / ".plandoc" / "plans" / "templates",
        repo_root / ".plandoc" / "design" / "drafts",
        repo_root / ".plandoc" / "design" / "active",
        repo_root / ".plandoc" / "design" / "archived",
        repo_root / ".plandoc" / "design" / "templates",
        repo_root / ".plandoc" / "reviews",
        repo_root / ".plandoc" / "comms" / "open",
        repo_root / ".plandoc" / "comms" / "acked",
        repo_root / ".plandoc" / "comms" / "closed",
        repo_root / ".plandoc" / "comms" / "templates",
    ]

    for directory in directories:
        if args.dry_run:
            print(f"mkdir {directory}")
        else:
            directory.mkdir(parents=True, exist_ok=True)

    for template_path in sorted(template_root.rglob("*")):
        if template_path.is_dir():
            continue
        relative = template_path.relative_to(template_root)
        destination = repo_root / relative
        content = render_template(template_path.read_text(encoding="utf-8"), project_name)
        print(write_file(destination, content, force=args.force, dry_run=args.dry_run))

    for filename in ENTRYPOINT_FILES:
        print(upsert_entrypoint(repo_root / filename, dry_run=args.dry_run))

    if not args.dry_run:
        print("")
        print("Local plandoc scaffold installed.")
        print("Next steps:")
        print("1. Adjust .plandoc/README.md if local rules differ.")
        print("2. Seed the first plandoc in .plandoc/plans/todo/.")
        print("3. Seed the first design doc in .plandoc/design/drafts/.")
        print("4. Write durable review artifacts in .plandoc/reviews/ when review mode is used.")
        print("5. Use .plandoc/comms/ for durable cross-owner handoffs when coordination must survive chat or tmux churn.")
        print("6. Keep .plandoc/plans/_index.md and .plandoc/design/_index.md aligned.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
