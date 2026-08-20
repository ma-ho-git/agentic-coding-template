# @contract
# provides:   CLI check for leftover template placeholders; exit 1 when any remain
# depends-on: the marker <!-- template-placeholder --> in the template's own documents;
#             tools/handover.py parks archived template history under the skipped path
# consumers:  .claude/skills/bootstrap/SKILL.md (final step)
# invariants: read-only; deliberately NOT wired into CI - in the template repository the
#             placeholders are supposed to be present, so CI would always be red
# updated:    2026-08-20

#!/usr/bin/env python3
"""Report documents that still carry the template's placeholder marker.

Run from the repository root after /bootstrap: python3 tools/check_placeholders.py
Exit code 1 while any placeholder remains. In this template repository that is the
expected result - the check is meant for a clone that has been adapted.
"""
from __future__ import annotations

import os
import sys

MARKER = "<!-- template-placeholder -->"
SKIP_DIRS = (".git", "node_modules", "__pycache__")
# handover.py parks the template's own history here on purpose; reporting it
# forever would mean the handover could never come back clean.
SKIP_PATHS = (os.path.join("knowledge", "90-meta", "beispiel"),)
# The four documents a project cannot ship unadapted. Others may keep their notes.
CORE = ("README.md", "knowledge/00-index.md",
        "knowledge/05-requirements/vision.md",
        "knowledge/05-requirements/baseline.md")


def has_marker(text):
    """True when the text still carries the template placeholder marker."""
    return MARKER in text


def scan(documents):
    """(path, text) pairs -> paths that still carry the marker, order preserved."""
    return [path for path, text in documents if has_marker(text)]


def markdown_files(root):
    """Repository-relative posix paths of every markdown file worth checking."""
    found = []
    skipped = tuple(os.path.join(root, path) for path in SKIP_PATHS)
    for folder, dirs, files in os.walk(root):
        dirs[:] = [name for name in dirs if name not in SKIP_DIRS]
        if folder.startswith(skipped):
            continue
        for name in sorted(files):
            if name.endswith(".md"):
                path = os.path.relpath(os.path.join(folder, name), root)
                found.append(path.replace(os.sep, "/"))
    return found


def read_documents(root, paths):
    """(path, text) pairs; unreadable files count as empty rather than crashing."""
    documents = []
    for path in paths:
        try:
            with open(os.path.join(root, path), encoding="utf-8", errors="replace") as handle:
                documents.append((path, handle.read()))
        except OSError:
            documents.append((path, ""))
    return documents


def report(remaining):
    """Print the finding; core documents first, because those block a handover."""
    if not remaining:
        print("No template placeholders left.")
        return 0
    core = [path for path in remaining if path in CORE]
    rest = [path for path in remaining if path not in CORE]
    for path in core:
        print("CORE  " + path)
    for path in rest:
        print("      " + path)
    print("\n{0} document(s) still carry template placeholders, {1} of them core."
          .format(len(remaining), len(core)))
    return 1


def main():
    root = os.getcwd()
    remaining = scan(read_documents(root, markdown_files(root)))
    sys.exit(report(remaining))


if __name__ == "__main__":
    main()
