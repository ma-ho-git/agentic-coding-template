"""Positive/negative cases for check_contract.py (PostToolUse Write|Edit guard)."""
from __future__ import annotations

from hook_runner import run_hook

VALID_CONTRACT = (
    "# @contract\n"
    "# provides:   greet(name: str) -> str\n"
    "# depends-on: none\n"
    "# consumers:  none\n"
    "# invariants: pure\n"
    "# updated:    2026-08-19\n\n"
    "def greet(name):\n"
    "    return 'hi ' + name\n"
)

NO_CONTRACT = (
    "def greet(name):\n"
    "    return 'hi ' + name\n"
    "\n\n\n\n\n\n\n\n\n\n"
)


def write_file(tmp_path, name, text):
    (tmp_path / name).write_text(text)
    return {"tool_input": {"file_path": name}}


def test_file_with_valid_contract_passes(tmp_path):
    event = write_file(tmp_path, "greet.py", VALID_CONTRACT)
    code, out, _err = run_hook("check_contract.py", event, project_dir=tmp_path)
    assert code == 0
    assert out.strip() == ""


def test_file_missing_contract_blocks(tmp_path):
    event = write_file(tmp_path, "greet.py", NO_CONTRACT)
    code, _out, err = run_hook("check_contract.py", event, project_dir=tmp_path)
    assert code == 2
    assert "CONTRACT BLOCK" in err


def test_short_file_is_exempt(tmp_path):
    event = write_file(tmp_path, "tiny.py", "x = 1\n")
    code, out, _err = run_hook("check_contract.py", event, project_dir=tmp_path)
    assert code == 0
    assert out.strip() == ""
