#!/usr/bin/env python3
"""Stdlib tests for validate_skill.py."""

from __future__ import annotations

import tempfile
import textwrap
import unittest
from pathlib import Path

from validate_skill import validate_skill_root


class ValidateSkillTests(unittest.TestCase):
    def test_current_skill_passes(self) -> None:
        skill_root = Path(__file__).resolve().parents[1]
        self.assertEqual(validate_skill_root(skill_root), [])

    def test_rejects_unexpected_frontmatter_key(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "SKILL.md").write_text(
                textwrap.dedent(
                    """\
                    ---
                    name: example-skill
                    description: Example skill
                    homepage: https://example.com
                    ---

                    # Example
                    """
                ),
                encoding="utf-8",
            )
            errors = validate_skill_root(root)
            self.assertTrue(any("Unexpected frontmatter keys" in error for error in errors))

    def test_rejects_missing_skill_reference_in_openai_yaml(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "agents").mkdir(parents=True)
            (root / "SKILL.md").write_text(
                textwrap.dedent(
                    """\
                    ---
                    name: example-skill
                    description: Example skill
                    ---

                    # Example
                    """
                ),
                encoding="utf-8",
            )
            (root / "agents" / "openai.yaml").write_text(
                textwrap.dedent(
                    """\
                    interface:
                      display_name: "Example"
                      short_description: "Example skill"
                      default_prompt: "Use this skill."

                    policy:
                      allow_implicit_invocation: true
                    """
                ),
                encoding="utf-8",
            )
            errors = validate_skill_root(root)
            self.assertTrue(any("default_prompt should mention the skill" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
