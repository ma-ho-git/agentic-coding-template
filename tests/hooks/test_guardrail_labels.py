"""Every guardrail names its class in its own message (T-0019).

A user who cannot tell a wall from a hint ends up treating both as noise,
so the class has to travel with the message, not sit only in the rules.
"""
from __future__ import annotations

import json

from hook_runner import run_hook

MANY_ASSIGNMENTS = (
    "def do_things():\n"
    + "\n".join("    value_{0} = {0}".format(i) for i in range(25))
    + "\n    return value_0\n"
)


def write_file(tmp_path, name, text):
    (tmp_path / name).write_text(text)
    return {"tool_input": {"file_path": name}}


def test_secret_block_is_labelled_rigid(tmp_path):
    fake_key = "AKIA" + "ABCDEFGHIJKLMNOP"
    event = {"tool_input": {"file_path": "app.py", "content": "K = '{0}'\n".format(fake_key)}}
    code, _out, err = run_hook("check_secrets.py", event, project_dir=tmp_path)
    assert code == 2
    assert "[RIGID]" in err


def test_contract_block_is_labelled_rigid(tmp_path):
    text = "def greet(name):\n    return name\n" + "\n" * 12
    event = write_file(tmp_path, "greet.py", text)
    code, _out, err = run_hook("check_contract.py", event, project_dir=tmp_path)
    assert code == 2
    assert "[RIGID]" in err


def test_quality_hint_is_labelled_flexible(tmp_path):
    event = write_file(tmp_path, "big.py", MANY_ASSIGNMENTS)
    code, out, _err = run_hook("check_quality.py", event, project_dir=tmp_path)
    context = json.loads(out)["hookSpecificOutput"]["additionalContext"]
    assert code == 0
    assert "[FLEXIBLE]" in context


def test_flexible_message_demands_reason(tmp_path):
    event = write_file(tmp_path, "big.py", MANY_ASSIGNMENTS)
    _code, out, _err = run_hook("check_quality.py", event, project_dir=tmp_path)
    context = json.loads(out)["hookSpecificOutput"]["additionalContext"]
    assert "justif" in context.lower() or "reason" in context.lower()


def test_git_denial_is_labelled_rigid():
    event = {"tool_input": {"command": "git push --force origin main"}}
    code, out, _err = run_hook("git_guard.py", event)
    reason = json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"]
    assert code == 0
    assert "[RIGID]" in reason
