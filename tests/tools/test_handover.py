"""Handing the template over to a real project (T-0038).

The template's own state ships with every clone. Until the handover runs, a
new project starts with an open start gate and /req-elicit skips framework
elicitation - the single most important guardrail, disabled by cloning.

Test names exceed the 3-word naming limit: pytest's mandatory `test_` prefix
already spends one word, and TDD conventions require the name to state the
behaviour in full - shortening further would make it meaningless.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "..", "tools")
))

import handover  # noqa: E402

BASELINE = "---\ntitle: Rahmen\nbaseline_status: vereinbart\n---\n\nText\n"
SCAN = "---\ntitle: Fremdlösungen\nscan_status: gesucht\n---\n\nText\n"
BOARD = ("---\n\nkanban-plugin: board\n\n---\n\n## Backlog\n\n## Ready\n\n"
         "- [ ] [[T-0001 Etwas]]\n\n## Doing\n\n## Review\n\n## Done\n\n"
         "- [x] [[T-0002 Anderes]]\n\n%% kanban:settings\n```\n{}\n```\n%%\n")


def make_template(tmp_path):
    """A clone that has not been handed over yet - the template's own state."""
    requirements = tmp_path / "knowledge" / "05-requirements"
    requirements.mkdir(parents=True)
    (requirements / "baseline.md").write_text(BASELINE, encoding="utf-8")
    (requirements / "fremdloesungen.md").write_text(SCAN, encoding="utf-8")
    (requirements / "REQ-0001 Beispiel.md").write_text("---\ntype: requirement\n---\n")
    (requirements / "szenario.md").write_text("---\ntype: knowledge\n---\n")
    pm = tmp_path / "knowledge" / "10-pm"
    (pm / "tasks").mkdir(parents=True)
    (pm / "tasks" / "T-0001 Etwas.md").write_text("---\ntype: task\n---\n")
    (pm / "decisions").mkdir()
    (pm / "decisions" / "ADR-0001 Wahl.md").write_text("---\ntype: decision\n---\n")
    (pm / "progress").mkdir()
    (pm / "progress" / "2026-08.md").write_text("---\ntype: progress\n---\n")
    (pm / "board.md").write_text(BOARD, encoding="utf-8")
    keep = tmp_path / "knowledge" / "20-knowledge"
    keep.mkdir()
    (keep / "Werkzeugwissen.md").write_text("---\ntype: knowledge\n---\n")
    return tmp_path


# --- resetting the two gate markers ---

def test_field_is_reset_in_place():
    result = handover.reset_field(BASELINE, "baseline_status", "entwurf")
    assert "baseline_status: entwurf" in result
    assert "vereinbart" not in result
    assert "title: Rahmen" in result


def test_absent_field_leaves_text_alone():
    assert handover.reset_field("---\ntitle: X\n---\n", "baseline_status", "entwurf") == \
        "---\ntitle: X\n---\n"


# --- what still marks this as the template ---

def test_untouched_clone_reports_findings(tmp_path):
    make_template(tmp_path)
    findings = handover.pending(str(tmp_path))
    joined = " ".join(findings)
    assert "baseline_status" in joined
    assert "scan_status" in joined
    assert "REQ-0001 Beispiel.md" in joined


def test_handed_over_clone_is_clean(tmp_path):
    make_template(tmp_path)
    handover.apply(str(tmp_path))
    assert handover.pending(str(tmp_path)) == []


# --- archiving, not deleting ---

def test_apply_archives_project_history(tmp_path):
    make_template(tmp_path)
    handover.apply(str(tmp_path))
    archive = tmp_path / "knowledge" / "90-meta" / "beispiel"
    for name in ("REQ-0001 Beispiel.md", "T-0001 Etwas.md",
                 "ADR-0001 Wahl.md", "2026-08.md", "szenario.md"):
        assert (archive / name).exists(), name


def test_apply_keeps_reusable_knowledge(tmp_path):
    make_template(tmp_path)
    handover.apply(str(tmp_path))
    assert (tmp_path / "knowledge" / "20-knowledge" / "Werkzeugwissen.md").exists()


def test_apply_empties_board_keeping_frontmatter(tmp_path):
    make_template(tmp_path)
    handover.apply(str(tmp_path))
    text = (tmp_path / "knowledge" / "10-pm" / "board.md").read_text(encoding="utf-8")
    assert "kanban-plugin: board" in text
    assert "## Ready" in text
    assert "T-0001" not in text


def test_apply_resets_both_gate_markers(tmp_path):
    make_template(tmp_path)
    handover.apply(str(tmp_path))
    requirements = tmp_path / "knowledge" / "05-requirements"
    assert "baseline_status: entwurf" in (requirements / "baseline.md").read_text(encoding="utf-8")
    assert "scan_status: offen" in (requirements / "fremdloesungen.md").read_text(encoding="utf-8")


def test_second_apply_changes_nothing(tmp_path):
    make_template(tmp_path)
    handover.apply(str(tmp_path))
    handover.apply(str(tmp_path))
    assert handover.pending(str(tmp_path)) == []
