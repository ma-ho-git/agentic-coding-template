"""Advisory findings from check_quality.py (PostToolUse Write|Edit, non-blocking).

Test names exceed the 3-word naming limit: pytest's mandatory `test_` prefix
already spends one word, and TDD conventions require the name to state the
behaviour in full - shortening further would make it meaningless.
"""
from __future__ import annotations

import json

from hook_runner import run_hook

MANY_ASSIGNMENTS = (
    "def do_things():\n"
    + "\n".join("    value_{0} = {0}".format(i) for i in range(25))
    + "\n    return value_0\n"
)

# Long but state-free: 30 lines, zero assignments. Under the assignment rule this
# is fine, which is exactly the difference from the old line-count rule.
LONG_WITHOUT_STATE = (
    "def describe(mode):\n"
    + "\n".join('    if mode == {0}:\n        return "case {0}"'.format(i)
                for i in range(15))
    + '\n    return "none"\n'
)

CLEAN_FUNCTION = "def add(a, b):\n    return a + b\n"


def write_file(tmp_path, name, text):
    (tmp_path / name).write_text(text)
    return {"tool_input": {"file_path": name}}


def findings(tmp_path, name, text):
    event = write_file(tmp_path, name, text)
    _code, out, _err = run_hook("check_quality.py", event, project_dir=tmp_path)
    return json.loads(out)["hookSpecificOutput"]["additionalContext"] if out.strip() else ""


def test_many_assignments_flagged(tmp_path):
    assert "do_things" in findings(tmp_path, "big.py", MANY_ASSIGNMENTS)


def test_long_without_state_passes(tmp_path):
    assert "describe" not in findings(tmp_path, "branchy.py", LONG_WITHOUT_STATE)


def test_clean_function_is_silent(tmp_path):
    assert findings(tmp_path, "small.py", CLEAN_FUNCTION) == ""
