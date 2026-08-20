"""Third-party licence obligations in tools/check_licenses.py (T-0029).

The tool checks completeness, not lawfulness: whether every registered
component carries its licence text in the repository. Whether a licence fits
the project is a human decision and is recorded as an ADR.

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

import check_licenses as licences  # noqa: E402

HEADER = (
    "| Komponente | Version | Lizenz | Lizenztext | Pflichten | Quelle (abgerufen) |\n"
    "| --- | --- | --- | --- | --- | --- |\n"
)

ENTRY = HEADER + (
    "| example-lib | 2.3.1 | MIT | `licenses/example-lib.txt` | Namensnennung | "
    "https://example.org/lib (2026-08-20) |\n"
)

INCOMPLETE = HEADER + (
    "| example-lib | | MIT | `licenses/example-lib.txt` | Namensnennung | "
    "https://example.org/lib (2026-08-20) |\n"
)

UNDATED = HEADER + (
    "| example-lib | 2.3.1 | MIT | `licenses/example-lib.txt` | Namensnennung | "
    "https://example.org/lib |\n"
)

FENCED_EXAMPLE = (
    "Format:\n\n```\n"
    "| Komponente | Version | Lizenz | Lizenztext | Pflichten | Quelle (abgerufen) |\n"
    "| beispiel | 1.0 | MIT | `licenses/beispiel.txt` | keine | https://x (2026-08-20) |\n"
    "```\n\n" + HEADER
)


def test_parses_one_entry():
    rows = licences.parse_rows(ENTRY)
    assert len(rows) == 1
    assert rows[0]["komponente"] == "example-lib"
    assert rows[0]["lizenz"] == "MIT"


def test_header_and_separator_ignored():
    assert licences.parse_rows(HEADER) == []


def test_example_inside_fence_ignored():
    """A fenced block shows the format; it must not register a component."""
    assert licences.parse_rows(FENCED_EXAMPLE) == []


def test_empty_register_is_clean():
    errors = []
    licences.check_texts([], set(), errors)
    licences.check_complete([], errors)
    assert errors == []


def test_missing_licence_text_fails():
    errors = []
    licences.check_texts(licences.parse_rows(ENTRY), set(), errors)
    assert len(errors) == 1
    assert "example-lib" in errors[0]


def test_present_licence_text_passes():
    errors = []
    licences.check_texts(licences.parse_rows(ENTRY), {"licenses/example-lib.txt"}, errors)
    assert errors == []


def test_incomplete_entry_fails():
    errors = []
    licences.check_complete(licences.parse_rows(INCOMPLETE), errors)
    assert len(errors) == 1
    assert "version" in errors[0]


def test_source_without_date_fails():
    errors = []
    licences.check_sources(licences.parse_rows(UNDATED), errors)
    assert len(errors) == 1


def test_dated_source_passes():
    errors = []
    licences.check_sources(licences.parse_rows(ENTRY), errors)
    assert errors == []


def test_unreferenced_licence_text_warns():
    warnings = []
    licences.check_orphans(licences.parse_rows(ENTRY), {"licenses/other.txt"}, warnings)
    assert len(warnings) == 1
    assert "other.txt" in warnings[0]


def test_readme_is_not_a_licence_text():
    """The directory's own README explains the convention; it registers nothing."""
    assert not licences.is_licence_text("README.md")
    assert licences.is_licence_text("example-lib-LICENSE.txt")
    assert licences.is_licence_text("example-lib-LICENSE.md")
