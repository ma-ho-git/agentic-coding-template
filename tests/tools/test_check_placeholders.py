"""Template placeholders in tools/check_placeholders.py (T-0033).

A cloned project must not ship the template's own placeholder text. The check
runs after /bootstrap, never in CI - in the template repository itself the
placeholders are supposed to be there.

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

import check_placeholders as placeholders  # noqa: E402

MARKED = "# Titel\n\n> Für ein eigenes Projekt: ersetzen.\n<!-- template-placeholder -->\n"
CLEAN = "# Titel\n\nEchter Projektinhalt ohne Platzhalter.\n"


def test_marked_text_is_found():
    assert placeholders.has_marker(MARKED)


def test_clean_text_is_not_found():
    assert not placeholders.has_marker(CLEAN)


def test_scan_reports_only_marked_files():
    found = placeholders.scan([("README.md", MARKED), ("vision.md", CLEAN)])
    assert found == ["README.md"]


def test_scan_of_clean_project_is_empty():
    assert placeholders.scan([("README.md", CLEAN)]) == []


def test_marker_survives_surrounding_text():
    """The marker sits inside a rendered blockquote; it must still be found."""
    text = "vor\n> Hinweis <!-- template-placeholder --> mehr Text\nnach\n"
    assert placeholders.has_marker(text)


def test_archive_is_skipped(tmp_path):
    """The example archive keeps template content on purpose (T-0038).

    handover.py moves the template's own history there. Reporting it forever
    would mean the handover could never come back clean.
    """
    archive = tmp_path / "knowledge" / "90-meta" / "beispiel"
    archive.mkdir(parents=True)
    (archive / "REQ-0001 Alt.md").write_text(MARKED, encoding="utf-8")
    (tmp_path / "README.md").write_text(CLEAN, encoding="utf-8")
    assert placeholders.markdown_files(str(tmp_path)) == ["README.md"]
