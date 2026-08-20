"""Unit tests for .claude/hooks/_common.py#matches_any (T-0011)."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "..", ".claude", "hooks")
))

from _common import matches_any  # noqa: E402

# The real exemption list from .claude/hooks/config.json.
EXEMPT = [
    "**/test_*.*", "**/*_test.*", "**/*.test.*", "**/*.spec.*",
    "**/tests/**", "**/__tests__/**", "**/spec/**",
    "**/__init__.py", "**/conftest.py",
    "**/migrations/**", "**/generated/**", "**/*.generated.*",
    "**/node_modules/**", "**/dist/**", "**/build/**", "**/vendor/**",
    ".claude/**",
]


# --- the bug: a directory whose name merely starts with test_ must not exempt ---

def test_test_prefixed_directory_not_exempt():
    assert matches_any("test_run_0/greet.py", EXEMPT) is False


def test_nested_test_directory_not_exempt():
    assert matches_any("tmp/test_case_1/module.py", EXEMPT) is False


def test_substring_tests_not_exempt():
    assert matches_any("contests/scoring.py", EXEMPT) is False


def test_star_does_not_cross_segments():
    assert matches_any("src/spec_helper/main.py", EXEMPT) is False


# --- regressions: the exemptions that must keep working ---

def test_root_test_file_exempt():
    assert matches_any("test_thing.py", EXEMPT) is True


def test_nested_test_file_exempt():
    assert matches_any("tests/hooks/test_git_guard.py", EXEMPT) is True


def test_tests_directory_exempt():
    assert matches_any("tests/tools/helper.py", EXEMPT) is True


def test_claude_directory_exempt():
    assert matches_any(".claude/hooks/_common.py", EXEMPT) is True


def test_node_modules_exempt():
    assert matches_any("node_modules/left-pad/index.js", EXEMPT) is True


def test_dunder_init_exempt():
    assert matches_any("src/package/__init__.py", EXEMPT) is True


def test_spec_suffix_exempt():
    assert matches_any("src/user.spec.ts", EXEMPT) is True


def test_plain_source_not_exempt():
    assert matches_any("src/service/token.py", EXEMPT) is False
