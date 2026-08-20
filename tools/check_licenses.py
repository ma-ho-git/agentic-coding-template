# @contract
# provides:   CLI check of the third-party component register; exit 1 on error
# depends-on: knowledge/05-requirements/fremdkomponenten.md (the register),
#             licenses/ (the licence texts it points at)
# consumers:  .github/workflows/rules.yml
# invariants: read-only; a missing register means no components, not an error;
#             checks completeness only - whether a licence fits is a human decision
# updated:    2026-08-20

#!/usr/bin/env python3
"""Validate that every registered third-party component carries its licence text.

Run from the repository root: python3 tools/check_licenses.py
Exit code 1 when any error is found. Warnings do not fail the run.
"""
from __future__ import annotations

import os
import re
import sys

REGISTER = os.path.join("knowledge", "05-requirements", "fremdkomponenten.md")
LICENSES = "licenses"
COLUMNS = ("komponente", "version", "lizenz", "lizenztext", "pflichten", "quelle")
# Pflichten may legitimately read "keine"; the other five carry no such case.
REQUIRED = ("komponente", "version", "lizenz", "lizenztext", "quelle")
RETRIEVED = re.compile(r"\d{4}-\d{2}-\d{2}")


def table_cells(line):
    """Cells of one markdown table row, without the outer pipes."""
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def data_lines(text):
    """Table lines outside fenced blocks - a fence holds the format, not entries."""
    lines = []
    fenced = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
        elif not fenced and line.lstrip().startswith("|"):
            lines.append(line)
    return lines


def is_heading(cells):
    """True for the header row and for the dashed separator under it."""
    first = cells[0].lower()
    return first.startswith("komponente") or (bool(first) and set(first) <= set("-: "))


def parse_rows(text):
    """One record per registered component."""
    rows = []
    for line in data_lines(text):
        cells = table_cells(line)
        if len(cells) != len(COLUMNS) or is_heading(cells):
            continue
        rows.append(dict(zip(COLUMNS, cells)))
    return rows


def text_path(row):
    """Repository path of the licence text, backticks stripped."""
    return row["lizenztext"].strip("` ").replace(os.sep, "/")


def check_texts(rows, present, errors):
    """A registered component without its licence text cannot fulfil its duties."""
    for row in rows:
        path = text_path(row)
        if path and path not in present:
            errors.append("{0}: licence text '{1}' is not in the repository"
                          .format(row["komponente"], path))


def check_complete(rows, errors):
    """A blank field is an entry nobody can act on."""
    for row in rows:
        missing = [name for name in REQUIRED if not row[name].strip("` ")]
        if missing:
            errors.append("{0}: incomplete entry, missing {1}"
                          .format(row["komponente"] or "(unnamed)", ", ".join(missing)))


def check_sources(rows, errors):
    """Facts about a project go stale; an undated source cannot be re-checked."""
    for row in rows:
        if row["quelle"].strip() and not RETRIEVED.search(row["quelle"]):
            errors.append("{0}: source carries no retrieval date (YYYY-MM-DD)"
                          .format(row["komponente"] or "(unnamed)"))


def check_orphans(rows, present, warnings):
    """A licence text nothing references is either dead weight or a missing entry."""
    referenced = {text_path(row) for row in rows}
    for path in sorted(present - referenced):
        warnings.append("{0}: licence text is in the repository but no entry references it"
                        .format(path))


def is_licence_text(name):
    """True for a file that carries a licence, not the directory's own README."""
    return not name.startswith(".") and name != "README.md"


def read_register():
    """The register's text; a missing file means the project uses no foreign code."""
    try:
        with open(os.path.join(os.getcwd(), REGISTER), encoding="utf-8") as handle:
            return handle.read()
    except OSError:
        return ""


def licence_files():
    """Every file under licenses/, as repository-relative posix paths."""
    found = set()
    for folder, _dirs, files in os.walk(LICENSES):
        for name in files:
            if is_licence_text(name):
                found.add(os.path.join(folder, name).replace(os.sep, "/"))
    return found


def report(errors, warnings):
    for item in warnings:
        print("WARN  " + item)
    for item in errors:
        print("ERROR " + item)
    print("\n{0} error(s), {1} warning(s)".format(len(errors), len(warnings)))
    return 1 if errors else 0


def main():
    rows = parse_rows(read_register())
    present = licence_files()
    errors, warnings = [], []
    check_complete(rows, errors)
    check_texts(rows, present, errors)
    check_sources(rows, errors)
    check_orphans(rows, present, warnings)
    sys.exit(report(errors, warnings))


if __name__ == "__main__":
    main()
