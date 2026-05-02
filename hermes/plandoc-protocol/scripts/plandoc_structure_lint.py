#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_HEADINGS = [
    "Context",
    "Outcome",
    "Deliverables",
    "Current Behavior",
    "Proposed Approach",
    "Landing Slice / Stopping Point",
    "Deferred / Not In This Slice",
    "Implementation Plan",
    "Acceptance Criteria",
    "Verification & Monitoring",
    "Rollback",
    "Invariants / Non-Negotiables",
    "Risks / Open Questions",
    "Implementation Log",
]

FORBIDDEN_OPERATING_HEADINGS = {"Brief", "Overview", "Notes"}
SUPPLEMENTAL_HEADINGS = {"Summary"}


def extract_headings(text: str) -> list[str]:
    return re.findall(r"^##\s+(.+?)\s*$", text, re.MULTILINE)


def extract_section_body(text: str, heading: str) -> str | None:
    pattern = re.compile(
        rf"^##\s+{re.escape(heading)}\s*$\n(?P<body>.*?)(?=^##\s+|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    if not match:
        return None
    return match.group("body").strip()


def extract_status(text: str) -> str | None:
    match = re.search(r"^Status:\s*(.+?)\s*$", text, re.MULTILINE)
    return match.group(1).strip() if match else None


def nonempty_lines(body: str | None) -> list[str]:
    if not body:
        return []
    return [line.strip() for line in body.splitlines() if line.strip()]


def has_labeled_items(body: str | None, prefix: str) -> bool:
    if not body:
        return False
    return re.search(rf"(^|\n)\s*(?:[-*]\s+)?{re.escape(prefix)}\d+\b", body) is not None


def lint_file(path: Path, strict_summary: bool) -> tuple[list[str], list[str]]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    warnings: list[str] = []

    headings = extract_headings(text)
    heading_set = set(headings)
    status = extract_status(text)

    for heading in REQUIRED_HEADINGS:
        if heading not in heading_set:
            errors.append(f"missing required heading: ## {heading}")

    for heading in headings:
        if heading in FORBIDDEN_OPERATING_HEADINGS:
            errors.append(
                f"forbidden shorthand heading present: ## {heading} (required operating truth must live in required sections)"
            )
        if strict_summary and heading in SUPPLEMENTAL_HEADINGS:
            errors.append(f"summary heading present under --strict-summary: ## {heading}")

    if "Outcome" in heading_set:
        outcome_lines = nonempty_lines(extract_section_body(text, "Outcome"))
        if not outcome_lines:
            errors.append("## Outcome is empty")
        elif len(outcome_lines) != 1:
            errors.append("## Outcome must contain exactly one non-empty line stating one primary outcome")

    if "Deliverables" in heading_set and not has_labeled_items(
        extract_section_body(text, "Deliverables"), "D"
    ):
        errors.append("## Deliverables must contain explicit D1/D2/... entries")

    if "Acceptance Criteria" in heading_set and not has_labeled_items(
        extract_section_body(text, "Acceptance Criteria"), "AC"
    ):
        errors.append("## Acceptance Criteria must contain explicit AC1/AC2/... entries")

    if "Landing Slice / Stopping Point" in heading_set:
        landing_lines = nonempty_lines(extract_section_body(text, "Landing Slice / Stopping Point"))
        if not landing_lines:
            errors.append("## Landing Slice / Stopping Point is empty")

    if "Deferred / Not In This Slice" in heading_set:
        deferred_lines = nonempty_lines(extract_section_body(text, "Deferred / Not In This Slice"))
        if not deferred_lines:
            errors.append("## Deferred / Not In This Slice is empty")

    if "Verification & Monitoring" in heading_set:
        verification_lines = nonempty_lines(extract_section_body(text, "Verification & Monitoring"))
        if not verification_lines:
            errors.append("## Verification & Monitoring is empty")

    if status and status.lower() == "qa" and "QA Gaps" not in heading_set:
        errors.append("Status: QA requires ## QA Gaps")

    if status and status.lower() == "resolved":
        if "Resolution" not in heading_set and "Solution Summary" not in heading_set:
            errors.append("Status: Resolved requires ## Resolution or ## Solution Summary")

    if "Summary" in heading_set and any(heading not in heading_set for heading in REQUIRED_HEADINGS):
        errors.append("## Summary cannot substitute for missing required operating sections")
    elif "Summary" in heading_set:
        warnings.append("## Summary present; ensure it is supplemental only")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Fail-closed plandoc structure lint")
    parser.add_argument("path", type=Path, help="Path to a plandoc markdown file")
    parser.add_argument(
        "--strict-summary",
        action="store_true",
        help="Treat any ## Summary heading as an error",
    )
    args = parser.parse_args()

    path = args.path
    if not path.exists():
        print(f"ERROR {path}: file not found")
        return 1
    if not path.is_file():
        print(f"ERROR {path}: not a file")
        return 1

    errors, warnings = lint_file(path, strict_summary=args.strict_summary)

    for error in errors:
        print(f"ERROR {path}: {error}")
    for warning in warnings:
        print(f"WARN {path}: {warning}")

    if not errors and not warnings:
        print(f"OK {path}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
