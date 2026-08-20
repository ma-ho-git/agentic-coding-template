#!/usr/bin/env python3
"""Refuse production code while the start gate is closed. Runs before Write/Edit.

Two conditions open it: the framework is agreed, and the existing-solutions
question is answered. Both are decisions reserved for the human.
"""
from __future__ import annotations

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import (deny, is_code, load_config, matches_any,  # noqa: E402
                     project_dir, read_event, relative, target_path)

GATE = os.path.join("knowledge", "05-requirements", "baseline.md")
OPEN_MARKER = "baseline_status: vereinbart"
SCAN = os.path.join("knowledge", "05-requirements", "fremdloesungen.md")
# Searching is optional, answering is not. A deliberate skip opens the gate too.
SCAN_ANSWERED = ("gesucht", "uebersprungen")
# Tooling, tests and examples are not the product. Without these you could not
# even build the machinery that lets the framework be agreed in the first place.
DEFAULT_EXEMPT = [".claude/**", "tools/**", "tests/**", "examples/**"]
FRAMEWORK_REFUSAL = (
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
SCAN_REFUSAL = (
    "Start gate closed: {0} is production code and nobody has answered whether this\n"
    "already exists.\n\n"
    "The cheapest line of code is the one somebody else already wrote and maintains.\n"
    "The question is asked now because earlier there was nothing to measure a candidate\n"
    "against, and later the home-made version wins by being there (.claude/rules/workflow.md).\n\n"
    "Either of these opens the gate:\n"
    "  1. /solution-scan — compare candidates against the agreed REQ-IDs, then decide\n"
    "  2. set scan_status: uebersprungen in {1}, with the reason\n\n"
    "Searching is not compulsory. Answering is.\n\n"
    "Tooling, tests, documentation and the requirements area itself stay writable."
)


def gate_open():
    """True when the framework is agreed. A missing file counts as closed."""
    try:
        with open(os.path.join(project_dir(), GATE), encoding="utf-8") as handle:
            return OPEN_MARKER in handle.read()
    except OSError:
        return False


def scan_answered():
    """True when the existing-solutions question was decided either way."""
    try:
        with open(os.path.join(project_dir(), SCAN), encoding="utf-8") as handle:
            match = re.search(r"^scan_status:\s*(\w+)", handle.read(), re.M)
    except OSError:
        return False
    return bool(match) and match.group(1) in SCAN_ANSWERED


def refusal(rel_path):
    """Text for whichever condition is unmet, empty when the gate is open.

    Framework first: without agreed requirements a solution scan has no yardstick.
    """
    if not gate_open():
        return FRAMEWORK_REFUSAL.format(rel_path, GATE.replace(os.sep, "/"))
    if not scan_answered():
        return SCAN_REFUSAL.format(rel_path, SCAN.replace(os.sep, "/"))
    return ""


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
    if not is_product_code(rel, path):
        sys.exit(0)
    text = refusal(rel)
    if text:
        deny(text)
    sys.exit(0)


if __name__ == "__main__":
    main()
