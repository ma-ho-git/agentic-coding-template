#!/usr/bin/env python3
"""Deny shell commands that could destroy work or history. Runs before Bash."""
from __future__ import annotations

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import deny, read_event  # noqa: E402

DENIED = [
    (r"\bgit\s+push\b[^|;&]*\s(?:--force\b|-f\b)",
     "force-push rewrites published history"),
    (r"\bgit\s+push\b[^|;&]*\s--mirror\b",
     "mirror-push can delete remote branches"),
    (r"\bgit\s+push\b[^|;&]*\s+\S+\s+(?:HEAD:)?(?:main|master)\b",
     "direct push to the default branch"),
    (r"\bgit\s+reset\s+--hard\b",
     "discards uncommitted work irreversibly"),
    (r"\bgit\s+clean\b[^|;&]*-\w*[fx]",
     "deletes untracked and ignored files irreversibly"),
    (r"\bgit\s+filter-branch\b|\bgit\s+filter-repo\b",
     "rewrites history"),
    (r"\bgit\s+branch\s+(?:-D|--delete\s+--force)\b",
     "force-deletes a branch with unmerged work"),
    (r"\brm\s+-[a-zA-Z]*r[a-zA-Z]*f?\s+(?:/|~|\$HOME|\.\.)",
     "recursive delete outside the project"),
    (r"\bgit\s+checkout\s+--\s+\.$|\bgit\s+restore\s+\.$",
     "discards all uncommitted changes in the tree"),
]


def find_violation(command):
    for pattern, reason in DENIED:
        if re.search(pattern, command):
            return reason
    return None


def main():
    event = read_event()
    command = (event.get("tool_input") or {}).get("command") or ""
    reason = find_violation(command)
    if reason:
        deny("Blocked by .claude/rules/agent-conduct.md: {0}.\n"
             "Command: {1}\n"
             "If this really is needed, explain why and let the user run it."
             .format(reason, command.strip()[:200]))
    sys.exit(0)


if __name__ == "__main__":
    main()
