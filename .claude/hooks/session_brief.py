#!/usr/bin/env python3
"""Put the project's current state into context at session start."""
from __future__ import annotations

import datetime as dt
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import project_dir  # noqa: E402

BOARD = "knowledge/10-pm/board.md"
MANIFEST = "knowledge/90-meta/environment-manifest.md"
TASKS = "knowledge/10-pm/tasks"
BOOTSTRAP_MAX_AGE = 30


def read_text(relative_path):
    try:
        with open(os.path.join(project_dir(), relative_path), encoding="utf-8") as handle:
            return handle.read()
    except OSError:
        return ""


def bootstrap_line():
    """Whether the environment assumptions were verified recently enough."""
    dates = re.findall(r"verified:\s*(\d{4}-\d{2}-\d{2})", read_text(MANIFEST))
    if not dates:
        return "BOOTSTRAP REQUIRED: no verified entry in the environment manifest. Run /bootstrap first."
    newest = max(dates)
    age = (dt.date.today() - dt.date.fromisoformat(newest)).days
    if age > BOOTSTRAP_MAX_AGE:
        return "BOOTSTRAP REQUIRED: last verified {0} ({1} days ago). Run /bootstrap first.".format(newest, age)
    return "Environment last verified {0} ({1} days ago).".format(newest, age)


def board_summary():
    """Lane name -> card titles, from the kanban board."""
    lanes = {}
    current = None
    for line in read_text(BOARD).splitlines():
        heading = re.match(r"^##\s+(.*\S)\s*$", line)
        if heading:
            current = heading.group(1)
            lanes[current] = []
        elif current and re.match(r"^\s*-\s*\[[ x]\]", line):
            lanes[current].append(re.sub(r"^\s*-\s*\[[ x]\]\s*", "", line).strip())
    return lanes


def stale_notes():
    """Count of knowledge notes whose review date has passed."""
    root = os.path.join(project_dir(), "knowledge")
    today = dt.date.today().isoformat()
    count = 0
    for folder, _dirs, files in os.walk(root):
        for name in files:
            if not name.endswith(".md"):
                continue
            with open(os.path.join(folder, name), encoding="utf-8", errors="replace") as handle:
                head = handle.read(1200)
            match = re.search(r"review_after:\s*(\d{4}-\d{2}-\d{2})", head)
            if match and match.group(1) < today and "status: deprecated" not in head:
                count += 1
    return count


def render(lanes, stale):
    """Assemble the briefing text."""
    parts = ["Project state (from .claude/hooks/session_brief.py):", bootstrap_line()]
    if lanes:
        counts = ", ".join("{0} {1}".format(len(cards), lane) for lane, cards in lanes.items())
        parts.append("Board: " + counts)
        for lane in ("Doing", "Review", "Ready"):
            if lanes.get(lane):
                parts.append("  {0}: {1}".format(lane, "; ".join(lanes[lane][:5])))
    else:
        parts.append("Board: empty or missing - run /bootstrap.")
    if stale:
        parts.append("Knowledge base: {0} note(s) past review_after. Run /kb-review.".format(stale))
    parts.append("Start work with /task-next. Do not work outside a board task.")
    return "\n".join(parts)


def main():
    text = render(board_summary(), stale_notes())
    print(json.dumps({
        "hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": text}
    }))


if __name__ == "__main__":
    main()
