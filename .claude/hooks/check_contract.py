#!/usr/bin/env python3
"""Enforce the file-level @contract block on source files. Runs on Write/Edit."""
from __future__ import annotations

import datetime as dt
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import (advise, block, is_code, load_config, matches_any,  # noqa: E402
                     read_event, relative, target_path)

REQUIRED_KEYS = ("provides", "depends-on", "consumers", "invariants", "updated")
HEADER_WINDOW = 60
KEY_PATTERN = re.compile(r"^[^A-Za-z0-9]*\s*({0})\s*:".format("|".join(REQUIRED_KEYS)))
DATE_PATTERN = re.compile(r"updated\s*:\s*(\d{4}-\d{2}-\d{2})")


def head_lines(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as handle:
            return handle.read().splitlines()
    except OSError:
        return []


def missing_keys(lines):
    """Keys of the schema absent from the header window."""
    window = "\n".join(lines[:HEADER_WINDOW])
    found = {match.group(1) for match in
             (KEY_PATTERN.match(line) for line in lines[:HEADER_WINDOW]) if match}
    if "@contract" not in window:
        return list(REQUIRED_KEYS)
    return [key for key in REQUIRED_KEYS if key not in found]


def stale_date(lines):
    """Contract date if it is not today, else None."""
    match = DATE_PATTERN.search("\n".join(lines[:HEADER_WINDOW]))
    if not match:
        return None
    return match.group(1) if match.group(1) != dt.date.today().isoformat() else None


def exempt(rel_path, config, lines):
    globs = config.get("contract_exempt_globs", [])
    minimum = config.get("min_lines_for_contract", 10)
    return matches_any(rel_path, globs) or len(lines) < minimum


def main():
    event = read_event()
    path = target_path(event)
    if not path or not is_code(path) or not os.path.exists(path):
        sys.exit(0)
    config = load_config()
    lines = head_lines(path)
    if not config.get("contract_required", True) or exempt(relative(path), config, lines):
        sys.exit(0)
    absent = missing_keys(lines)
    if absent:
        block(
            "CONTRACT BLOCK: {0} has no valid @contract header.\n"
            "Missing: {1}\n\n"
            "Add it at the very top of the file, in the language's comment syntax:\n"
            "  @contract\n  provides:   ...\n  depends-on: ...\n  consumers:  ...\n"
            "  invariants: ...\n  updated:    {2}\n\n"
            "Use 'none' for empty values. Schema: .claude/rules/contracts.md"
            .format(relative(path), ", ".join(absent), dt.date.today().isoformat())
        )
    old = stale_date(lines)
    if old:
        advise(
            "Contract note: {0} was edited but its @contract still says updated: {1}. "
            "Re-verify provides/consumers/depends-on against the code, then set today's date. "
            "If the public surface changed, run /contract-sync.".format(relative(path), old)
        )
    sys.exit(0)


if __name__ == "__main__":
    main()
