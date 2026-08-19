"""Positive/negative cases for session_brief.py (SessionStart briefing).

Test names exceed the 3-word naming limit: pytest's mandatory `test_` prefix
already spends one word, and TDD conventions require the name to state the
behaviour in full - shortening further would make it meaningless.
"""
from __future__ import annotations

import json

from hook_runner import run_hook

BOARD = "## Doing\n\n- [ ] [[T-1 Example]]\n\n## Ready\n\n## Review\n\n## Done\n\n"


def make_project(tmp_path, verified_date):
    pm_dir = tmp_path / "knowledge" / "90-meta"
    pm_dir.mkdir(parents=True)
    (tmp_path / "knowledge" / "10-pm").mkdir(parents=True)
    (tmp_path / "knowledge" / "10-pm" / "board.md").write_text(BOARD)
    (pm_dir / "environment-manifest.md").write_text(
        "## Entry\n\n- **verified:** {0}\n- **state:** ok\n".format(verified_date)
    )
    return tmp_path


def test_fresh_manifest_has_no_bootstrap_flag(tmp_path):
    make_project(tmp_path, "2026-08-19")
    code, out, _err = run_hook("session_brief.py", project_dir=tmp_path)
    context = json.loads(out)["hookSpecificOutput"]["additionalContext"]
    assert code == 0
    assert "BOOTSTRAP REQUIRED" not in context


def test_stale_manifest_flags_bootstrap(tmp_path):
    make_project(tmp_path, "2026-01-01")
    code, out, _err = run_hook("session_brief.py", project_dir=tmp_path)
    context = json.loads(out)["hookSpecificOutput"]["additionalContext"]
    assert code == 0
    assert "BOOTSTRAP REQUIRED" in context
