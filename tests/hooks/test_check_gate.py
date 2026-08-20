"""The start gate as a rigid guardrail (T-0020).

No production code before the framework is agreed - enforced, not announced.
Tooling, tests, examples and everything that is not source stay writable, or
you could not even reach the point of eliciting requirements.

Test names exceed the 3-word naming limit: pytest's mandatory `test_` prefix
already spends one word, and TDD conventions require the name to state the
behaviour in full - shortening further would make it meaningless.
"""
from __future__ import annotations

import json

from hook_runner import run_hook


def make_project(tmp_path, gate=None):
    """Project tree with an optional baseline.md carrying the given gate state."""
    if gate is not None:
        folder = tmp_path / "knowledge" / "05-requirements"
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "baseline.md").write_text(
            "---\ntitle: Rahmen\nbaseline_status: {0}\n---\n".format(gate)
        )
    return tmp_path


def attempt(tmp_path, rel_path):
    """Run the gate hook for a write to rel_path; return (code, decision-or-None)."""
    event = {"tool_input": {"file_path": rel_path, "content": "x = 1\n"}}
    code, out, _err = run_hook("check_gate.py", event, project_dir=tmp_path)
    if not out.strip():
        return code, None
    return code, json.loads(out)["hookSpecificOutput"]


def test_open_gate_allows_source(tmp_path):
    make_project(tmp_path, "vereinbart")
    code, decision = attempt(tmp_path, "src/app.py")
    assert code == 0
    assert decision is None


def test_closed_gate_denies_source(tmp_path):
    make_project(tmp_path, "entwurf")
    code, decision = attempt(tmp_path, "src/app.py")
    assert code == 0
    assert decision["permissionDecision"] == "deny"


def test_missing_baseline_denies(tmp_path):
    make_project(tmp_path)
    _code, decision = attempt(tmp_path, "src/app.py")
    assert decision["permissionDecision"] == "deny"


def test_denial_names_class_and_way(tmp_path):
    make_project(tmp_path, "entwurf")
    _code, decision = attempt(tmp_path, "src/app.py")
    reason = decision["permissionDecisionReason"]
    assert "[RIGID]" in reason
    assert "/req-elicit" in reason


def test_tooling_stays_writable(tmp_path):
    make_project(tmp_path, "entwurf")
    for path in (".claude/hooks/x.py", "tools/x.py", "tests/x.py", "examples/x.py"):
        _code, decision = attempt(tmp_path, path)
        assert decision is None, path


def test_non_source_stays_writable(tmp_path):
    make_project(tmp_path, "entwurf")
    for path in ("README.md", "knowledge/05-requirements/REQ-0001 X.md", "config.json"):
        _code, decision = attempt(tmp_path, path)
        assert decision is None, path


def test_path_outside_project_denied(tmp_path):
    make_project(tmp_path, "entwurf")
    _code, decision = attempt(tmp_path, "/somewhere/else/app.py")
    assert decision["permissionDecision"] == "deny"
