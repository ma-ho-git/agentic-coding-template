#!/usr/bin/env python3
"""Refuse production code while the start gate is closed. Runs before Write/Edit."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import (deny, is_code, load_config, matches_any,  # noqa: E402
                     project_dir, read_event, relative, target_path)

GATE = os.path.join("knowledge", "05-requirements", "baseline.md")
OPEN_MARKER = "baseline_status: vereinbart"
# Tooling, tests and examples are not the product. Without these you could not
# even build the machinery that lets the framework be agreed in the first place.
DEFAULT_EXEMPT = [".claude/**", "tools/**", "tests/**", "examples/**"]
REFUSAL = (
    "Start gate closed: {0} is production code and the framework is not agreed yet.\n\n"
    "No production code before it is clear what is being built and which technical,\n"
    "functional, organisational, security, legal and quality requirements hold\n"
    "(.claude/rules/requirements.md).\n\n"
    "The way forward:\n"
    "  1. /req-elicit   — clarify the framework with the user\n"
    "  2. /req-validate — check it, then report what is still missing\n"
    "  3. the user sets baseline_status: vereinbart in {1}\n\n"
    "Tooling, tests, documentation and the requirements area itself stay writable."
)


def gate_open():
    """True when the framework is agreed. A missing file counts as closed."""
    try:
        with open(os.path.join(project_dir(), GATE), encoding="utf-8") as handle:
            return OPEN_MARKER in handle.read()
    except OSError:
        return False


def is_product_code(rel_path, path):
    """True when this write is product source rather than tooling or prose."""
    if not is_code(path):
        return False
    exempt = load_config().get("gate_exempt_globs", DEFAULT_EXEMPT)
    return not matches_any(rel_path, exempt)


def main():
    event = read_event()
    path = target_path(event)
    if not path:
        sys.exit(0)
    rel = relative(path).replace(os.sep, "/")
    if not is_product_code(rel, path) or gate_open():
        sys.exit(0)
    deny(REFUSAL.format(rel, GATE.replace(os.sep, "/")))


if __name__ == "__main__":
    main()
