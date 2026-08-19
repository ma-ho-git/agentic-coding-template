"""Shared helpers for the repository hooks.

Hooks are tooling, not project source: they are exempt from the contract rule.
"""
from __future__ import annotations

import json
import os
import re
import sys

CODE_EXTENSIONS = {
    ".py", ".pyi", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs",
    ".go", ".rs", ".java", ".kt", ".rb", ".php", ".cs", ".swift",
    ".c", ".h", ".cpp", ".hpp", ".scala", ".ex", ".exs", ".sh",
}


def read_event():
    """Parse the hook payload from stdin; empty dict when absent or malformed."""
    try:
        return json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError:
        return {}


def project_dir():
    return os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()


def load_config():
    path = os.path.join(project_dir(), ".claude", "hooks", "config.json")
    try:
        with open(path, encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError):
        return {}


def target_path(event):
    """Absolute path of the file the tool touched, or None."""
    raw = (event.get("tool_input") or {}).get("file_path")
    if not raw:
        return None
    return raw if os.path.isabs(raw) else os.path.join(project_dir(), raw)


def relative(path):
    try:
        return os.path.relpath(path, project_dir())
    except ValueError:
        return path


# longest first: '**/' must win over '**', which must win over '*'
GLOB_TOKENS = (
    ("**/", "(?:[^/]+/)*"),   # zero or more whole segments, so '**/a' also matches 'a'
    ("**", ".*"),
    ("*", "[^/]*"),
    ("?", "[^/]"),
)


def next_token(pattern, index):
    """Wildcard at index with its regex, else the literal char there."""
    for token, regex in GLOB_TOKENS:
        if pattern.startswith(token, index):
            return token, regex
    return pattern[index], re.escape(pattern[index])


def glob_regex(pattern):
    """Glob -> regex source. '/' is a real boundary, unlike fnmatch."""
    parts = []
    index = 0
    while index < len(pattern):
        token, regex = next_token(pattern, index)
        parts.append(regex)
        index += len(token)
    return "".join(parts)


def matches_any(rel_path, globs):
    """True when rel_path matches a glob. Paths outside the root never match."""
    posix = rel_path.replace(os.sep, "/")
    return any(re.match(glob_regex(pattern) + r"\Z", posix) for pattern in globs)


def is_code(path):
    return os.path.splitext(path)[1].lower() in CODE_EXTENSIONS


def block(message):
    """Reject the action and hand the reason back to the agent."""
    print(message, file=sys.stderr)
    sys.exit(2)


def advise(message):
    """Let the action stand but put the finding into the agent's context."""
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": message,
        }
    }))
    sys.exit(0)
