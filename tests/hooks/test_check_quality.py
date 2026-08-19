"""Advisory findings from check_quality.py (PostToolUse Write|Edit, non-blocking).

Test names exceed the 3-word naming limit: pytest's mandatory `test_` prefix
already spends one word, and TDD conventions require the name to state the
behaviour in full - shortening further would make it meaningless.
"""
from __future__ import annotations

import json

from hook_runner import run_hook

LONG_FUNCTION = (
    "def do_things():\n"
    + "\n".join("    x = {0}".format(i) for i in range(25))
    + "\n    return x\n"
)

CLEAN_FUNCTION = "def add(a, b):\n    return a + b\n"


def write_file(tmp_path, name, text):
    (tmp_path / name).write_text(text)
    return {"tool_input": {"file_path": name}}


def test_long_function_is_flagged(tmp_path):
    event = write_file(tmp_path, "big.py", LONG_FUNCTION)
    code, out, _err = run_hook("check_quality.py", event, project_dir=tmp_path)
    context = json.loads(out)["hookSpecificOutput"]["additionalContext"]
    assert code == 0
    assert "do_things" in context


def test_clean_function_is_silent(tmp_path):
    event = write_file(tmp_path, "small.py", CLEAN_FUNCTION)
    code, out, _err = run_hook("check_quality.py", event, project_dir=tmp_path)
    assert code == 0
    assert out.strip() == ""
