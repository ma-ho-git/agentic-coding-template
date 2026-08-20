# @contract
# provides:   pending(root) -> [finding]; apply(root) -> [moved]; reset_field(text, k, v);
#             main() CLI: --check (default, read-only) | --apply
# depends-on: tools/check_placeholders.py#scan, knowledge/05-requirements/,
#             knowledge/10-pm/, knowledge/90-meta/beispiel/ (the archive)
# consumers:  .claude/skills/bootstrap/SKILL.md (handover step and final check)
# invariants: --check never writes; --apply archives, never deletes; idempotent;
#             deliberately NOT in CI - in the template repository red is correct
# updated:    2026-08-20

#!/usr/bin/env python3
"""Turn a clone of the template into a project of its own.

The template's own state travels with every clone. Until this has run, a new
project carries baseline_status: vereinbart and scan_status: gesucht - its
start gate is open before a single requirement exists, and /req-elicit reads
the same field and skips framework elicitation entirely.

Run from the repository root:
  python3 tools/handover.py            # check only, changes nothing
  python3 tools/handover.py --apply    # perform the handover
"""
from __future__ import annotations

import datetime as dt
import os
import re
import shutil
import sys

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLS_DIR)
from check_placeholders import markdown_files, read_documents, scan  # noqa: E402

REQUIREMENTS = os.path.join("knowledge", "05-requirements")
PROJECT_MANAGEMENT = os.path.join("knowledge", "10-pm")
ARCHIVE = os.path.join("knowledge", "90-meta", "beispiel")
BOARD = os.path.join(PROJECT_MANAGEMENT, "board.md")
INDEX = os.path.join("knowledge", "00-index.md")
INDEX_LINK = "- [[Beispielarchiv]] — die Anforderungen, Aufgaben und Entscheidungen der Vorlage"

# Two machine-readable gate conditions; both ship pre-satisfied without this.
GATE_FIELDS = (
    (os.path.join(REQUIREMENTS, "baseline.md"), "baseline_status", "entwurf"),
    (os.path.join(REQUIREMENTS, "fremdloesungen.md"), "scan_status", "offen"),
)
# The project's own history. Knowledge and troubleshooting stay: they describe
# the tooling the clone keeps using, not what this project once decided.
ARCHIVED = (
    (REQUIREMENTS, lambda name: name.startswith("REQ-") or name == "szenario.md"),
    (os.path.join(PROJECT_MANAGEMENT, "tasks"), lambda name: name.startswith("T-")),
    (os.path.join(PROJECT_MANAGEMENT, "decisions"), lambda name: name.startswith("ADR-")),
    (os.path.join(PROJECT_MANAGEMENT, "progress"), lambda name: name.endswith(".md")),
)
ARCHIVE_README = """---
title: Beispielarchiv
aliases: ["Beispielarchiv"]
type: knowledge
tags: [topic/meta]
status: active
created: {today}
updated: {today}
review_after: {review}
related: ["[[00-index]]"]
---

# Beispielarchiv

## Kurz

Hier liegt der Projektstand der **Vorlage**, aus der dieses Projekt geklont wurde:
ihre Anforderungen, Aufgaben, Entscheidungen, ihr Fortschrittslog und ihr Szenario.
Verschoben von `tools/handover.py`, damit sie das eigene Projekt nicht belasten.

## Wozu das gut ist

Ein ausgefülltes Beispiel zeigt mehr als eine leere Vorlage. Wer wissen will, wie eine
brauchbare Anforderung aussieht, was in einen ADR gehört oder wie eine Aufgabe geschnitten
wird, findet hier vier Dutzend echte Fälle — samt der Fehler, die dabei gemacht wurden.

## Was es nicht ist

**Keine Anforderung dieses Projekts.** Die Prüfwerkzeuge sehen dieses Verzeichnis nicht an:
`check_traceability.py` liest nur `05-requirements` und `10-pm/tasks`, und die
Platzhalterprüfung überspringt diesen Pfad. Nichts hier gilt für dich.

Wenn du es nicht brauchst: löschen. Es hängt nichts daran.
"""

EMPTY_BOARD = """---

kanban-plugin: board

---

## Backlog

## Ready

## Doing

## Review

## Done

%% kanban:settings
```
{"kanban-plugin":"board","show-checkboxes":true,"lane-width":320}
```
%%
"""


def read_text(path):
    """File contents, empty when unreadable - a missing file is not a crash."""
    try:
        with open(path, encoding="utf-8", errors="replace") as handle:
            return handle.read()
    except OSError:
        return ""


def reset_field(text, field, value):
    """Frontmatter field set to value; text unchanged when the field is absent."""
    pattern = re.compile(r"^{0}:.*$".format(re.escape(field)), re.M)
    if not pattern.search(text):
        return text
    return pattern.sub("{0}: {1}".format(field, value), text, count=1)


def archive_plan(root):
    """(source, destination) for every file that belongs in the example archive."""
    plan = []
    for folder, belongs in ARCHIVED:
        directory = os.path.join(root, folder)
        for name in sorted(os.listdir(directory)) if os.path.isdir(directory) else []:
            if name.endswith(".md") and belongs(name):
                plan.append((os.path.join(directory, name),
                             os.path.join(root, ARCHIVE, name)))
    return plan


def gate_findings(root):
    """Gate markers still carrying the template's answers."""
    findings = []
    for relative, field, wanted in GATE_FIELDS:
        text = read_text(os.path.join(root, relative))
        match = re.search(r"^{0}:\s*(\S+)".format(re.escape(field)), text, re.M)
        if match and match.group(1) != wanted:
            findings.append("{0}: {1} is '{2}', a new project needs '{3}'"
                            .format(relative.replace(os.sep, "/"), field,
                                    match.group(1), wanted))
    return findings


def pending(root):
    """Everything still marking this clone as the template itself."""
    findings = gate_findings(root)
    for source, _destination in archive_plan(root):
        findings.append("{0}: template history, not this project's"
                        .format(os.path.relpath(source, root).replace(os.sep, "/")))
    documents = read_documents(root, markdown_files(root))
    findings.extend("{0}: template placeholder".format(path) for path in scan(documents))
    return findings


def write_archive_readme(root):
    """Explain the archive, and link it from the index so it can be found."""
    today = dt.date.today()
    review = today.replace(year=today.year + 1)
    path = os.path.join(root, ARCHIVE, "README.md")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ARCHIVE_README.format(today=today.isoformat(),
                                           review=review.isoformat()))
    index = os.path.join(root, INDEX)
    text = read_text(index)
    if not text or INDEX_LINK in text:
        return
    with open(index, "a", encoding="utf-8") as handle:
        handle.write("\n## Beispielarchiv\n\n" + INDEX_LINK + "\n")


def apply(root):
    """Reset the gate markers, archive the history, empty the board."""
    for relative, field, wanted in GATE_FIELDS:
        path = os.path.join(root, relative)
        text = read_text(path)
        if text:
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(reset_field(text, field, wanted))
    plan = archive_plan(root)
    if plan:
        os.makedirs(os.path.join(root, ARCHIVE), exist_ok=True)
    for source, destination in plan:
        shutil.move(source, destination)
    if os.path.isdir(os.path.join(root, ARCHIVE)):
        write_archive_readme(root)
    board = os.path.join(root, BOARD)
    if os.path.exists(board):
        with open(board, "w", encoding="utf-8") as handle:
            handle.write(EMPTY_BOARD)
    return [destination for _source, destination in plan]


def report(findings):
    for item in findings:
        print("PENDING  " + item)
    if not findings:
        print("Handover complete - this is a project of its own.")
        return 0
    print("\n{0} item(s) still belong to the template. Run:\n"
          "  python3 tools/handover.py --apply".format(len(findings)), file=sys.stderr)
    return 1


def main():
    root = os.getcwd()
    if sys.argv[1:] == ["--apply"]:
        moved = apply(root)
        print("Archived {0} document(s) to {1}/.".format(len(moved),
                                                         ARCHIVE.replace(os.sep, "/")))
        sys.exit(report(pending(root)))
    if sys.argv[1:] not in ([], ["--check"]):
        print("usage: handover.py [--check | --apply]", file=sys.stderr)
        sys.exit(2)
    sys.exit(report(pending(root)))


if __name__ == "__main__":
    main()
