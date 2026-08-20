"""Handing the template over to a real project (T-0038).

The template's own state ships with every clone. Until the handover runs, a
new project starts with an open start gate and /req-elicit skips framework
elicitation - the single most important guardrail, disabled by cloning.
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
    hooks = tmp_path / ".claude" / "hooks"
    hooks.mkdir(parents=True)
    (hooks / "config.json").write_text('{"handover_done": false}', encoding="utf-8")
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


# The gate markers used to be patched in place; since T-0040 they arrive with the
# skeletons instead. test_apply_resets_both_gate_markers still guards the outcome.

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


def test_archive_is_findable(tmp_path):
    """Archived, not deleted, only helps if someone can find it (T-0038)."""
    make_template(tmp_path)
    index = tmp_path / "knowledge" / "00-index.md"
    index.write_text("---\ntitle: Index\n---\n\n# Index\n\n## Meta\n\n- [[Konventionen]]\n",
                     encoding="utf-8")
    handover.apply(str(tmp_path))
    readme = tmp_path / "knowledge" / "90-meta" / "beispiel" / "README.md"
    assert readme.exists()
    assert "[[00-index]]" in readme.read_text(encoding="utf-8")
    assert "Beispielarchiv" in index.read_text(encoding="utf-8")


def test_index_link_added_once(tmp_path):
    make_template(tmp_path)
    index = tmp_path / "knowledge" / "00-index.md"
    index.write_text("---\ntitle: Index\n---\n\n## Meta\n\n- [[Konventionen]]\n",
                     encoding="utf-8")
    handover.apply(str(tmp_path))
    handover.apply(str(tmp_path))
    # Count the link line itself: "Beispielarchiv" also appears in the heading.
    assert index.read_text(encoding="utf-8").count(handover.INDEX_LINK) == 1


def test_own_requirements_are_not_flagged(tmp_path):
    """After the handover, new requirements belong to the project (T-0034).

    Found by the real walkthrough: --check reported the project's own freshly
    written REQ files as template history, so bootstrap's final check could
    never come back clean.
    """
    make_template(tmp_path)
    handover.apply(str(tmp_path))
    own = tmp_path / "knowledge" / "05-requirements" / "REQ-0001 Eigene Anforderung.md"
    own.write_text("---\ntype: requirement\n---\n", encoding="utf-8")
    assert handover.pending(str(tmp_path)) == []


def test_own_open_gate_is_not_flagged(tmp_path):
    """A project that opens its own gate later must not be called unfinished."""
    make_template(tmp_path)
    handover.apply(str(tmp_path))
    baseline = tmp_path / "knowledge" / "05-requirements" / "baseline.md"
    baseline.write_text("---\nbaseline_status: vereinbart\n---\n", encoding="utf-8")
    assert handover.pending(str(tmp_path)) == []


def test_apply_records_completion(tmp_path):
    make_template(tmp_path)
    assert not handover.is_done(str(tmp_path))
    handover.apply(str(tmp_path))
    assert handover.is_done(str(tmp_path))


def test_archive_readme_links_everything(tmp_path):
    """Nothing archived may become an orphan (T-0034).

    Found by the real walkthrough: the progress log was linked only from the
    index; once the project rewrote its index, check_vault called it an orphan.
    """
    make_template(tmp_path)
    handover.apply(str(tmp_path))
    text = (tmp_path / "knowledge" / "90-meta" / "beispiel" / "README.md").read_text(
        encoding="utf-8")
    for name in ("REQ-0001 Beispiel", "T-0001 Etwas", "ADR-0001 Wahl", "2026-08", "szenario"):
        assert "[[" + name + "]]" in text, name


# --- empty forms instead of a foreign project's filled ones (T-0040) ---

FRAMEWORK = ("baseline.md", "vision.md", "constraints.md", "glossary.md",
             "risks.md", "stakeholders.md", "fremdloesungen.md", "fremdkomponenten.md")


def make_framework(tmp_path):
    """The template's own filled framework documents, as a clone inherits them."""
    requirements = tmp_path / "knowledge" / "05-requirements"
    for name in FRAMEWORK:
        (requirements / name).write_text(
            "---\ntitle: Alt\n---\n\n# Vorlage\n\nZielartefakt der Vorlage, 36 REQ-Verweise.\n",
            encoding="utf-8")


def test_framework_loses_foreign_content(tmp_path):
    make_template(tmp_path)
    make_framework(tmp_path)
    handover.apply(str(tmp_path))
    requirements = tmp_path / "knowledge" / "05-requirements"
    for name in FRAMEWORK:
        text = (requirements / name).read_text(encoding="utf-8")
        assert "Vorlage" not in text, name
        assert "36 REQ" not in text, name


def test_skeletons_keep_frontmatter_and_marker(tmp_path):
    make_template(tmp_path)
    make_framework(tmp_path)
    handover.apply(str(tmp_path))
    requirements = tmp_path / "knowledge" / "05-requirements"
    for name in FRAMEWORK:
        text = (requirements / name).read_text(encoding="utf-8")
        assert text.startswith("---\ntitle: "), name
        assert "type: knowledge" in text, name
        assert "<!-- template-placeholder -->" in text, name
        assert "[[" in text, name + " has no outgoing wikilink"


def test_baseline_skeleton_keeps_its_alias(tmp_path):
    """Everything links to [[Rahmen und Startgate]] - the alias must survive."""
    make_template(tmp_path)
    make_framework(tmp_path)
    handover.apply(str(tmp_path))
    text = (tmp_path / "knowledge" / "05-requirements" / "baseline.md").read_text(
        encoding="utf-8")
    assert "Rahmen und Startgate" in text
    assert "baseline_status: entwurf" in text


def test_scan_skeleton_closes_the_second_gate(tmp_path):
    make_template(tmp_path)
    make_framework(tmp_path)
    handover.apply(str(tmp_path))
    text = (tmp_path / "knowledge" / "05-requirements" / "fremdloesungen.md").read_text(
        encoding="utf-8")
    assert "scan_status: offen" in text


def test_skeletons_survive_a_second_apply(tmp_path):
    make_template(tmp_path)
    make_framework(tmp_path)
    handover.apply(str(tmp_path))
    (tmp_path / "knowledge" / "05-requirements" / "vision.md").write_text(
        "---\ntitle: Projektvision\n---\n\nEchter Inhalt des Projekts.\n", encoding="utf-8")
    handover.apply(str(tmp_path))
    text = (tmp_path / "knowledge" / "05-requirements" / "vision.md").read_text(
        encoding="utf-8")
    assert "Echter Inhalt" in text, "a second apply must not wipe the project's own work"
