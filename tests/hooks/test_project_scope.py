"""The project scope is recorded and visible at session start (T-0022).

Scope scales documentation duty and elicitation depth. It never switches a
rigid guardrail off - so it has to be visible, not a silent config value.

Test names exceed the 3-word naming limit: pytest's mandatory `test_` prefix
already spends one word, and TDD conventions require the name to state the
behaviour in full - shortening further would make it meaningless.
"""
from __future__ import annotations

import json

from hook_runner import run_hook

BOARD = "## Doing\n\n## Ready\n\n## Review\n\n## Done\n\n"


def make_project(tmp_path, scope=None):
    """Minimal project tree, optionally carrying a project_scope in the hook config."""
    (tmp_path / "knowledge" / "10-pm").mkdir(parents=True, exist_ok=True)
    (tmp_path / "knowledge" / "10-pm" / "board.md").write_text(BOARD)
    meta = tmp_path / "knowledge" / "90-meta"
    meta.mkdir(parents=True, exist_ok=True)
    (meta / "environment-manifest.md").write_text("- **verified:** 2026-08-20\n")
    hooks = tmp_path / ".claude" / "hooks"
    hooks.mkdir(parents=True, exist_ok=True)
    config = {} if scope is None else {"project_scope": scope}
    (hooks / "config.json").write_text(json.dumps(config))
    return tmp_path


def brief(tmp_path):
    _code, out, _err = run_hook("session_brief.py", project_dir=tmp_path)
    return json.loads(out)["hookSpecificOutput"]["additionalContext"]


def test_scope_appears_in_brief(tmp_path):
    make_project(tmp_path, "skript")
    assert "skript" in brief(tmp_path)


def test_scope_defaults_to_produkt(tmp_path):
    make_project(tmp_path)
    assert "produkt" in brief(tmp_path)


def test_unknown_scope_falls_back_to_produkt(tmp_path):
    """An unrecognised value must not silently buy less ceremony."""
    make_project(tmp_path, "winzig")
    text = brief(tmp_path)
    assert "produkt" in text
    assert "winzig" in text
