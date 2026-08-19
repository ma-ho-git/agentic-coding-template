"""Positive/negative cases for git_guard.py (PreToolUse Bash guard).

Test names exceed the 3-word naming limit: pytest's mandatory `test_` prefix
already spends one word, and TDD conventions require the name to state the
behaviour in full - shortening further would make it meaningless.
"""
from __future__ import annotations

import json

from hook_runner import run_hook


def bash_event(command):
    return {"tool_input": {"command": command}}


def test_allows_safe_command():
    code, out, _ = run_hook("git_guard.py", bash_event("git status"))
    assert code == 0
    assert out.strip() == ""


def test_denies_force_push():
    code, out, _ = run_hook("git_guard.py", bash_event("git push --force origin main"))
    decision = json.loads(out)["hookSpecificOutput"]["permissionDecision"]
    assert code == 0
    assert decision == "deny"


def test_denies_reset_hard():
    code, out, _ = run_hook("git_guard.py", bash_event("git reset --hard HEAD~1"))
    decision = json.loads(out)["hookSpecificOutput"]["permissionDecision"]
    assert code == 0
    assert decision == "deny"


def test_denies_push_to_main():
    code, out, _ = run_hook("git_guard.py", bash_event("git push origin main"))
    decision = json.loads(out)["hookSpecificOutput"]["permissionDecision"]
    assert code == 0
    assert decision == "deny"


def test_allows_push_to_feature_branch():
    code, out, _ = run_hook("git_guard.py", bash_event("git push origin task/T-0007-x"))
    assert code == 0
    assert out.strip() == ""


def test_denies_recursive_delete_outside_project():
    code, out, _ = run_hook("git_guard.py", bash_event("rm -rf ~"))
    decision = json.loads(out)["hookSpecificOutput"]["permissionDecision"]
    assert code == 0
    assert decision == "deny"
