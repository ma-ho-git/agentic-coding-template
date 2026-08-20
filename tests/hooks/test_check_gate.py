"""The start gate as a rigid guardrail (T-0020, extended in T-0028).

No production code before the framework is agreed and the existing-solutions
question is answered - enforced, not announced.
Tooling, tests, examples and everything that is not source stay writable, or
you could not even reach the point of eliciting requirements.
"""
from __future__ import annotations

import json

from hook_runner import run_hook


def make_project(tmp_path, gate=None, scan="gesucht"):
    """Project tree with optional baseline.md and fremdloesungen.md states."""
    folder = tmp_path / "knowledge" / "05-requirements"
    folder.mkdir(parents=True, exist_ok=True)
    if gate is not None:
        (folder / "baseline.md").write_text(
            "---\ntitle: Rahmen\nbaseline_status: {0}\n---\n".format(gate)
        )
    if scan is not None:
        (folder / "fremdloesungen.md").write_text(
            "---\ntitle: Fremdlösungen\nscan_status: {0}\n---\n".format(scan)
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
    for path in (".claude/hooks/x.py", "tools/x.py", "tests/x.py", "examples/x.py",
                 "cowork/build-skills.sh"):
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


# --- the second condition: the existing-solutions decision (T-0028) ---

def test_undecided_scan_denies_source(tmp_path):
    make_project(tmp_path, "vereinbart", scan=None)
    _code, decision = attempt(tmp_path, "src/app.py")
    assert decision["permissionDecision"] == "deny"


def test_open_scan_status_denies_source(tmp_path):
    make_project(tmp_path, "vereinbart", scan="offen")
    _code, decision = attempt(tmp_path, "src/app.py")
    assert decision["permissionDecision"] == "deny"


def test_skipped_scan_allows_source(tmp_path):
    make_project(tmp_path, "vereinbart", scan="uebersprungen")
    _code, decision = attempt(tmp_path, "src/app.py")
    assert decision is None


def test_scan_refusal_names_both_ways(tmp_path):
    make_project(tmp_path, "vereinbart", scan="offen")
    _code, decision = attempt(tmp_path, "src/app.py")
    reason = decision["permissionDecisionReason"]
    assert "[RIGID]" in reason
    assert "/solution-scan" in reason
    assert "uebersprungen" in reason


def test_framework_is_named_first(tmp_path):
    """Both conditions missing: report the framework, which comes first in the process."""
    make_project(tmp_path, "entwurf", scan=None)
    _code, decision = attempt(tmp_path, "src/app.py")
    assert "/req-elicit" in decision["permissionDecisionReason"]


def test_scan_gate_spares_tooling(tmp_path):
    make_project(tmp_path, "vereinbart", scan="offen")
    for path in ("tools/x.py", "tests/x.py", "README.md"):
        _code, decision = attempt(tmp_path, path)
        assert decision is None, path
