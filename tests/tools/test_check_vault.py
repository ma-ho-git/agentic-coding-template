"""Frontmatter checks in tools/check_vault.py (T-0012).

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

import check_vault  # noqa: E402

COMPLETE = (
    "---\n"
    "title: Beispiel\n"
    "type: requirement\n"
    "tags: [topic/requirements]\n"
    "status: entwurf\n"
    "created: 2026-08-19\n"
    "updated: 2026-08-19\n"
    "review_after: 2026-11-19\n"
    "---\n\nText\n"
)

WITHOUT_REVIEW = (
    "---\n"
    "title: Beispiel\n"
    "type: requirement\n"
    "tags: [topic/requirements]\n"
    "status: entwurf\n"
    "created: 2026-08-19\n"
    "updated: 2026-08-19\n"
    "---\n\nText\n"
)


def check(text):
    errors = []
    check_vault.check_frontmatter("REQ-0001 Beispiel.md", text, errors)
    return errors


def test_complete_requirement_passes():
    assert check(COMPLETE) == []


def test_requirement_without_review_date_fails():
    errors = check(WITHOUT_REVIEW)
    assert len(errors) == 1
    assert "review_after" in errors[0]


def test_empty_board_is_not_an_orphan():
    """A freshly handed-over project starts with an empty board (T-0038).

    The board is plugin-owned and carries cards, not prose links. Empty is its
    legitimate starting state and must not greet a new project with a warning.
    """
    _targets, errors, warnings = check_vault.check_links(
        "knowledge/10-pm/board.md", "---\n\nkanban-plugin: board\n\n---\n\n## Ready\n", set())
    assert errors == []
    assert warnings == []
