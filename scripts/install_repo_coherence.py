#!/usr/bin/env python3
"""Backward-compatible wrapper for the old repo-coherence installer name."""

from __future__ import annotations

from install_plandoc_scaffold import main


if __name__ == "__main__":
    raise SystemExit(main())
