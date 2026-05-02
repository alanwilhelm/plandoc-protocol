#!/usr/bin/env python3
"""Validate the plandoc skill for Codex and OpenClaw portability."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

MAX_NAME_LENGTH = 64
MAX_DESCRIPTION_LENGTH = 1024
ALLOWED_FRONTMATTER_KEYS = {"name", "description", "license", "allowed-tools", "metadata"}
BOOL_STRINGS = {"true", "false", "yes", "no", "on", "off", "1", "0"}
INSTALL_KINDS = {"brew", "node", "go", "uv", "download"}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_frontmatter(content: str) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    if not content.startswith("---\n"):
        return {}, ["SKILL.md must start with YAML frontmatter delimited by ---"]

    try:
        _, body = content.split("---\n", 1)
        frontmatter_block, _ = body.split("\n---", 1)
    except ValueError:
        return {}, ["SKILL.md frontmatter is missing a closing --- line"]

    data: dict[str, str] = {}
    for lineno, raw_line in enumerate(frontmatter_block.splitlines(), start=2):
        line = raw_line.rstrip()
        if not line.strip():
            continue
        if line.startswith((" ", "\t", "- ")):
            errors.append(
                f"Frontmatter line {lineno} must be single-line key:value for OpenClaw compatibility"
            )
            continue
        if ":" not in line:
            errors.append(f"Frontmatter line {lineno} is not key:value: {line}")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            errors.append(f"Frontmatter line {lineno} has an empty key")
            continue
        data[key] = value

    return data, errors


def validate_name(value: str) -> list[str]:
    errors: list[str] = []
    if not value:
        return ["Missing required frontmatter key: name"]
    if len(value) > MAX_NAME_LENGTH:
        errors.append(f"name is too long ({len(value)} > {MAX_NAME_LENGTH})")
    if not re.fullmatch(r"[a-z0-9-]+", value):
        errors.append("name must be hyphen-case: lowercase letters, digits, and hyphens only")
    if value.startswith("-") or value.endswith("-") or "--" in value:
        errors.append("name cannot start/end with hyphen or contain consecutive hyphens")
    return errors


def validate_description(value: str) -> list[str]:
    errors: list[str] = []
    if not value:
        return ["Missing required frontmatter key: description"]
    if "<" in value or ">" in value:
        errors.append("description cannot contain angle brackets")
    if len(value) > MAX_DESCRIPTION_LENGTH:
        errors.append(
            f"description is too long ({len(value)} > {MAX_DESCRIPTION_LENGTH})"
        )
    return errors


def validate_url(value: str, field: str) -> list[str]:
    try:
        parsed = urlparse(value)
    except Exception:
        return [f"{field} must be a valid URL"]
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return [f"{field} must be an http/https URL"]
    return []


def validate_string_list(value: object, field: str) -> list[str]:
    if not isinstance(value, list) or not all(isinstance(item, str) and item for item in value):
        return [f"{field} must be a non-empty string list when present"]
    return []


def validate_install_spec(spec: object, index: int) -> list[str]:
    prefix = f"metadata.openclaw.install[{index}]"
    if not isinstance(spec, dict):
        return [f"{prefix} must be an object"]

    errors: list[str] = []
    kind = spec.get("kind")
    if kind not in INSTALL_KINDS:
        errors.append(f"{prefix}.kind must be one of {sorted(INSTALL_KINDS)}")
        return errors

    if "label" in spec and not isinstance(spec["label"], str):
        errors.append(f"{prefix}.label must be a string")
    if "bins" in spec:
        errors.extend(validate_string_list(spec["bins"], f"{prefix}.bins"))
    if "os" in spec:
        errors.extend(validate_string_list(spec["os"], f"{prefix}.os"))

    if kind == "brew" and not isinstance(spec.get("formula"), str):
        errors.append(f"{prefix}.formula is required for brew installers")
    if kind == "node" and not isinstance(spec.get("package"), str):
        errors.append(f"{prefix}.package is required for node installers")
    if kind == "go" and not isinstance(spec.get("module"), str):
        errors.append(f"{prefix}.module is required for go installers")
    if kind == "uv" and not isinstance(spec.get("package"), str):
        errors.append(f"{prefix}.package is required for uv installers")
    if kind == "download":
        url = spec.get("url")
        if not isinstance(url, str):
            errors.append(f"{prefix}.url is required for download installers")
        else:
            errors.extend(validate_url(url, f"{prefix}.url"))

    return errors


def validate_metadata(value: str) -> list[str]:
    if not value:
        return []
    errors: list[str] = []
    try:
        metadata = json.loads(value)
    except json.JSONDecodeError as exc:
        return [f"metadata must be single-line JSON for OpenClaw compatibility: {exc}"]

    if not isinstance(metadata, dict):
        return ["metadata must decode to a JSON object"]

    openclaw = metadata.get("openclaw")
    if openclaw is None:
        return []
    if not isinstance(openclaw, dict):
        return ["metadata.openclaw must be an object"]

    if "skillKey" in openclaw and not isinstance(openclaw["skillKey"], str):
        errors.append("metadata.openclaw.skillKey must be a string")
    if "always" in openclaw and not isinstance(openclaw["always"], bool):
        errors.append("metadata.openclaw.always must be a boolean")
    if "homepage" in openclaw:
        if not isinstance(openclaw["homepage"], str):
            errors.append("metadata.openclaw.homepage must be a string")
        else:
            errors.extend(validate_url(openclaw["homepage"], "metadata.openclaw.homepage"))

    requires = openclaw.get("requires")
    if requires is not None:
        if not isinstance(requires, dict):
            errors.append("metadata.openclaw.requires must be an object")
        else:
            for key in ("bins", "anyBins", "env", "config"):
                if key in requires:
                    errors.extend(
                        validate_string_list(requires[key], f"metadata.openclaw.requires.{key}")
                    )

    install = openclaw.get("install")
    if install is not None:
        if not isinstance(install, list):
            errors.append("metadata.openclaw.install must be an array")
        else:
            for index, spec in enumerate(install):
                errors.extend(validate_install_spec(spec, index))

    return errors


def validate_openai_yaml(path: Path, expected_skill_name: str) -> list[str]:
    if not path.exists():
        return []
    content = read_text(path)
    errors: list[str] = []
    required_markers = [
        "interface:",
        "display_name:",
        "short_description:",
        "default_prompt:",
        "policy:",
        "allow_implicit_invocation:",
    ]
    for marker in required_markers:
        if marker not in content:
            errors.append(f"agents/openai.yaml missing required marker: {marker}")
    if f"${expected_skill_name}" not in content:
        errors.append("agents/openai.yaml default_prompt should mention the skill as $<skill-name>")
    return errors


def validate_skill_root(skill_root: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_root / "SKILL.md"
    if not skill_md.exists():
        return ["SKILL.md not found"]

    frontmatter, parse_errors = extract_frontmatter(read_text(skill_md))
    errors.extend(parse_errors)

    unexpected = sorted(set(frontmatter) - ALLOWED_FRONTMATTER_KEYS)
    if unexpected:
        errors.append(
            "Unexpected frontmatter keys for Codex portability: "
            + ", ".join(unexpected)
        )

    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")
    metadata = frontmatter.get("metadata", "")

    errors.extend(validate_name(name))
    errors.extend(validate_description(description))
    errors.extend(validate_metadata(metadata))
    errors.extend(validate_openai_yaml(skill_root / "agents" / "openai.yaml", name))

    return errors


def main(argv: list[str]) -> int:
    if len(argv) > 2:
        print("Usage: validate_skill.py [skill_root]", file=sys.stderr)
        return 2

    skill_root = Path(argv[1]).resolve() if len(argv) == 2 else Path(__file__).resolve().parents[1]
    errors = validate_skill_root(skill_root)
    if errors:
        print(f"Skill validation failed for {skill_root}:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Skill validation passed for {skill_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
