"""Positive/negative cases for git_guard.py (PreToolUse Bash guard)."""
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


# --- skipping the commit choke point (T-0035); literals assembled at runtime ---

SKIP_FLAG = "--no-" + "verify"
SHORT_SKIP = "-" + "n"
HOOKS_KEY = "core." + "hooksPath"


def decision_for(command):
    _code, out, _err = run_hook("git_guard.py", bash_event(command))
    if not out.strip():
        return "allow"
    return json.loads(out)["hookSpecificOutput"]["permissionDecision"]


def test_denies_commit_skipping_hooks():
    assert decision_for("git commit -m 'x' " + SKIP_FLAG) == "deny"


def test_denies_commit_short_skip_flag():
    assert decision_for("git commit " + SHORT_SKIP + " -m 'x'") == "deny"


def test_allows_plain_commit():
    assert decision_for("git commit -m 'feat: add parser'") == "allow"


def test_allows_dry_run_push():
    assert decision_for("git push " + SHORT_SKIP + " origin feature") == "allow"


def test_denies_hookspath_via_config():
    assert decision_for("git config " + HOOKS_KEY + " /tmp/empty") == "deny"


def test_denies_hookspath_inline():
    assert decision_for("git -c " + HOOKS_KEY + "=/dev/null commit -m 'x'") == "deny"
