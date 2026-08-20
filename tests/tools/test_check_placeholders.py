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
