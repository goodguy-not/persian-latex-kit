#!/usr/bin/env python3
"""Cross-platform entry point for Persian LaTeX Kit project creation."""

import sys

sys.dont_write_bytecode = True  # Generating a project must not write in the kit.

from project_generator import main


if __name__ == "__main__":
    raise SystemExit(main())
