# @contract
# provides:   CLI check of the knowledge vault; exit 1 on error, 0 otherwise
# depends-on: knowledge/90-meta/conventions.md (frontmatter and linking rules)
# consumers:  none (invoked manually and from CI)
# invariants: read-only; never writes to the vault; warnings never fail the run
# updated:    2026-08-19

#!/usr/bin/env python3
"""Validate the knowledge vault: frontmatter, wikilinks, orphans, reachability.

Run from the repository root: python3 tools/check_vault.py
Exit code 1 when any error is found. Warnings do not fail the run.
"""
from __future__ import annotations

import os
import re
import sys

VAULT = "knowledge"
INDEX = "00-index.md"
REQUIRED = ("title", "type", "tags", "status", "created")
DATED_TYPES = ("knowledge", "troubleshooting", "decision", "progress", "requirement")
LINK = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
FENCE = re.compile(r"```.*?```|`[^`\n]+`", re.S)
SKIP_DIRS = {".obsidian", "templates", "attachments"}
PLUGIN_OWNED = {"board.md"}   # own frontmatter schema; linted for links only


def collect_notes():
    """Relative paths of every note in the vault, templates excluded."""
    found = []
    for folder, dirs, files in os.walk(VAULT):
        dirs[:] = [name for name in dirs if name not in SKIP_DIRS]
        found.extend(os.path.join(folder, name) for name in files if name.endswith(".md"))
    return sorted(found)


def frontmatter(text):
    """Top-level frontmatter keys, empty when the block is absent."""
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end]
    return {match.group(1) for match in re.finditer(r"^([a-z_]+):", block, re.M)}


def note_names(path, text):
    """Every name this note can be linked by: its filename stem plus any aliases."""
    names = {os.path.splitext(os.path.basename(path))[0]}
    block = re.search(r"^aliases:\s*\[(.*?)\]", text, re.M)
    if block:
        names |= {item.strip().strip("\"'") for item in block.group(1).split(",") if item.strip()}
    return names


def prose(text):
    """Text with fenced and inline code removed, so examples are not linted."""
    return FENCE.sub("", text)


def check_frontmatter(path, text, errors):
    stem = os.path.basename(path)
    if stem in PLUGIN_OWNED:
        return
    keys = frontmatter(text)
    if not keys:
        errors.append("{0}: no frontmatter".format(stem))
        return
    missing = [key for key in REQUIRED if key not in keys]
    if missing:
        errors.append("{0}: missing frontmatter keys: {1}".format(stem, ", ".join(missing)))
    kind = re.search(r"^type:\s*(\w+)", text, re.M)
    if not kind or kind.group(1) not in DATED_TYPES:
        return
    for key in ("updated", "review_after"):
        if key not in keys:
            errors.append("{0}: type '{1}' requires {2}".format(stem, kind.group(1), key))


def check_links(path, text, titles):
    """Return (targets, errors, warnings) for one note's outgoing wikilinks."""
    stem = os.path.basename(path)
    targets = {match.group(1).strip() for match in LINK.finditer(prose(text))}
    errors = ["{0}: broken wikilink [[{1}]]".format(stem, target)
              for target in sorted(targets) if target not in titles]
    # The index and the board carry no prose links: the index is the hub, the
    # board carries cards, and an empty board is a new project's normal start.
    exempt = stem == INDEX or stem in PLUGIN_OWNED
    warnings = [] if targets or exempt else \
        ["{0}: no outgoing wikilink (orphan)".format(stem)]
    return targets, errors, warnings


def check_reachable(names, linked, errors):
    """Every note must be linked from somewhere, under any of its names."""
    for path, aliases in names.items():
        if os.path.basename(path) in (INDEX,) or os.path.basename(path) in PLUGIN_OWNED:
            continue
        if not aliases & linked:
            errors.append("{0}: not linked from any other note".format(os.path.basename(path)))


def check_claude_md(warnings):
    """Warn when CLAUDE.md outgrows the length Anthropic recommends for memory files."""
    # 200 comes from Anthropic's CLAUDE.md guidance, not from this project's brief.
    # Every session loads the file in full, and adherence drops as it grows.
    for path, limit in (("CLAUDE.md", 200),):
        if not os.path.exists(path):
            warnings.append("{0} is missing".format(path))
            continue
        length = len(open(path, encoding="utf-8").read().splitlines())
        if length > limit:
            warnings.append("{0} is {1} lines (recommended limit {2})".format(path, length, limit))


def report(errors, warnings):
    for item in warnings:
        print("WARN  " + item)
    for item in errors:
        print("ERROR " + item)
    print("\n{0} error(s), {1} warning(s)".format(len(errors), len(warnings)))
    return 1 if errors else 0


def main():
    notes = collect_notes()
    sources = {path: open(path, encoding="utf-8").read() for path in notes}
    names = {path: note_names(path, text) for path, text in sources.items()}
    titles = set().union(*names.values()) if names else set()
    errors, warnings, linked = [], [], set()
    for path, text in sources.items():
        check_frontmatter(path, text, errors)
        targets, link_errors, link_warnings = check_links(path, text, titles)
        linked |= targets
        errors.extend(link_errors)
        warnings.extend(link_warnings)
    check_reachable(names, linked, errors)
    check_claude_md(warnings)
    sys.exit(report(errors, warnings))


if __name__ == "__main__":
    main()
