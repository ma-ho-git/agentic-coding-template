#!/usr/bin/env python3
"""Block a task file that serves no requirement. Runs on Write/Edit."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import block, matches_any, read_event, relative, target_path  # noqa: E402

TASK_GLOBS = ["knowledge/10-pm/tasks/*.md"]
HINT = (
    "TRACEABILITY BLOCK: {0} names no requirement.\n\n"
    "Every task must serve an agreed requirement (.claude/rules/requirements.md).\n"
    "Add one of these to the frontmatter:\n\n"
    '  implements: ["[[REQ-0001 Titel]]"]\n\n'
    "or, for pure infrastructure and maintenance work, state why:\n\n"
    "  implements: []\n"
    "  infrastruktur: <reason this serves no product requirement>\n\n"
    "No agreed requirement fits yet? Run /req-elicit first."
)


def frontmatter(path):
    """Frontmatter block of the file, empty string when absent."""
    try:
        with open(path, encoding="utf-8", errors="replace") as handle:
            text = handle.read()
    except OSError:
        return ""
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    return text[3:end] if end != -1 else ""


def serves_requirement(block_text):
    """True when the task links a requirement or justifies being infrastructure."""
    if "[[REQ-" in block_text:
        return True
    for line in block_text.splitlines():
        if line.startswith("infrastruktur:") and line[len("infrastruktur:"):].strip():
            return True
    return False


def main():
    event = read_event()
    path = target_path(event)
    if not path or not os.path.exists(path):
        sys.exit(0)
    rel = relative(path).replace(os.sep, "/")
    if not matches_any(rel, TASK_GLOBS):
        sys.exit(0)
    if not serves_requirement(frontmatter(path)):
        block(HINT.format(rel))
    sys.exit(0)


if __name__ == "__main__":
    main()
