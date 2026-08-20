"""Tests for tools/ci_check.py - runs the real hooks against files, for CI."""
from __future__ import annotations

import os
import sys

TOOLS_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", "tools"))
sys.path.insert(0, TOOLS_DIR)

import ci_check  # noqa: E402

VALID_CONTRACT = (
    "# @contract\n"
    "# provides:   none\n"
    "# depends-on: none\n"
    "# consumers:  none\n"
    "# invariants: none\n"
    "# updated:    2026-08-19\n\n"
    "x = 1\n"
)


def write(tmp_path, name, text):
    path = tmp_path / name
    path.write_text(text)
    return str(path)


def test_clean_file_has_no_failures(tmp_path, monkeypatch):
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    path = write(tmp_path, "clean.py", VALID_CONTRACT)
    assert ci_check.check_file(path) == 0


def test_file_with_secret_fails(tmp_path, monkeypatch):
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    fake_key = "AKIA" + "ABCDEFGHIJKLMNOP"
    path = write(tmp_path, "secret.py", "KEY = '{0}'\n".format(fake_key))
    assert ci_check.check_file(path) == 1


def test_file_missing_contract_fails(tmp_path, monkeypatch):
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    text = "def greet(name):\n    return name\n" + "\n" * 10
    path = write(tmp_path, "greet.py", text)
    assert ci_check.check_file(path) == 1
