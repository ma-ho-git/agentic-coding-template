"""One command for every rule check, at the commit choke point (T-0035).

Bash-written files bypass the Write|Edit hooks; the commit is the one gate
every write path must pass. check_all is what runs there and in CI.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "..", "tools")
))

import check_all  # noqa: E402


# --- the TDD signal ---

def test_hint_fires_for_code_without_tests():
    hint = check_all.missing_tests_hint(["src/app.py"], True)
    assert "[FLEXIBLE]" in hint
    assert "src/app.py" in hint


def test_hint_silent_with_test_change():
    assert check_all.missing_tests_hint(["src/app.py", "tests/test_app.py"], True) == ""


def test_hint_silent_for_prose_and_config():
    assert check_all.missing_tests_hint(["README.md", "config.json"], True) == ""


def test_hint_respects_switch():
    assert check_all.missing_tests_hint(["src/app.py"], False) == ""


def test_test_files_recognised():
    for path in ("tests/x.py", "src/test_app.py", "src/app_test.go",
                 "web/app.spec.ts", "web/app.test.tsx", "spec/thing.rb"):
        assert check_all.is_test_file(path), path
    assert not check_all.is_test_file("src/app.py")
    assert not check_all.is_test_file("src/contest.py")


# --- gate output parsing ---

def test_gate_reason_extracted():
    out = json.dumps({"hookSpecificOutput": {
        "permissionDecision": "deny", "permissionDecisionReason": "[RIGID] closed"}})
    assert check_all.gate_reason(out) == "[RIGID] closed"


def test_gate_reason_empty_when_allowed():
    assert check_all.gate_reason("") == ""
    assert check_all.gate_reason("not json") == ""
    allowed = json.dumps({"hookSpecificOutput": {"permissionDecision": "allow"}})
    assert check_all.gate_reason(allowed) == ""


# --- collecting the file set ---

def test_staged_paths_handle_spaces(tmp_path, monkeypatch):
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    (tmp_path / "a file.py").write_text("x = 1\n")
    subprocess.run(["git", "add", "a file.py"], cwd=tmp_path, check=True)
    monkeypatch.chdir(tmp_path)
    assert check_all.staged_paths() == ["a file.py"]


def test_explicit_paths_pass_through():
    assert check_all.collect(["a.py", "b.md"]) == ["a.py", "b.md"]


def test_range_without_argument_is_rejected():
    assert check_all.collect(["--range"]) is None
