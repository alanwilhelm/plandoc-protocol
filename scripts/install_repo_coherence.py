#!/usr/bin/env python3
"""Install the repo-local plandoc coherence scaffold into a target repository."""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
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
        help="Overwrite existing managed files.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned writes without changing files.",
    )
    return parser.parse_args()


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


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).expanduser().resolve()
    project_name = args.project_name or repo_root.name
    skill_root = Path(__file__).resolve().parents[1]
    template_root = skill_root / "assets" / "repo_coherence"

    directories = [
        repo_root / "docs" / "plans" / "todo",
        repo_root / "docs" / "plans" / "active",
        repo_root / "docs" / "plans" / "qa",
        repo_root / "docs" / "plans" / "resolved",
        repo_root / "docs" / "plans" / "icebox",
        repo_root / "docs" / "plans" / "templates",
        repo_root / "docs" / "design" / "drafts",
        repo_root / "docs" / "design" / "active",
        repo_root / "docs" / "design" / "archived",
        repo_root / "docs" / "design" / "templates",
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

    if not args.dry_run:
        print("")
        print("Scaffold installed.")
        print("Next steps:")
        print("1. Customize AGENTS.md for the repo identity and local boundaries.")
        print("2. Seed an umbrella milestone plandoc.")
        print("3. Seed the first design doc that states current architecture truth.")
        print("4. Keep the index files aligned with actual plan/design state.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
