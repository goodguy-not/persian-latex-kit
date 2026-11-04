#!/usr/bin/env python3
"""Compatibility entry point for the OS single-question generator."""

import sys

sys.dont_write_bytecode = True  # Keep the source toolkit untouched.

from project_generator import main


if __name__ == "__main__":
    raise SystemExit(main(["--template", "os-single-question", *sys.argv[1:]]))
