# @contract
# provides:   pending(root) -> [finding]; unfilled(root) -> [path]; apply(root) -> [moved];
#             is_done(root) -> bool;
#             main() CLI: --check (default, read-only) | --apply
# depends-on: tools/check_placeholders.py#scan and #CORE, tools/handover_texts.py#SKELETONS,
#             knowledge/05-requirements/, knowledge/10-pm/, knowledge/90-meta/beispiel/
# consumers:  .claude/skills/bootstrap/SKILL.md (handover step and final check)
# invariants: --check never writes; --apply archives, never deletes; a second --apply is a
#             no-op, so it never overwrites the project's own answers with a blank form;
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
import json
import os
import re
import shutil
import sys

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLS_DIR)
from check_placeholders import CORE, markdown_files, read_documents, scan  # noqa: E402
from handover_texts import ARCHIVE_README, EMPTY_BOARD, SKELETONS  # noqa: E402

REQUIREMENTS = os.path.join("knowledge", "05-requirements")
PROJECT_MANAGEMENT = os.path.join("knowledge", "10-pm")
ARCHIVE = os.path.join("knowledge", "90-meta", "beispiel")
BOARD = os.path.join(PROJECT_MANAGEMENT, "board.md")
CONFIG = os.path.join(".claude", "hooks", "config.json")
DONE_KEY = "handover_done"
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
def read_text(path):
    """File contents, empty when unreadable - a missing file is not a crash."""
    try:
        with open(path, encoding="utf-8", errors="replace") as handle:
            return handle.read()
    except OSError:
        return ""


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


def is_done(root):
    """True once the handover ran here - recorded, not guessed from the tree.

    Without this the check cannot tell the template's leftovers from the
    project's own requirements, and would flag every new REQ file forever.
    """
    try:
        with open(os.path.join(root, CONFIG), encoding="utf-8") as handle:
            return bool(json.load(handle).get(DONE_KEY))
    except (OSError, json.JSONDecodeError):
        return False


def mark_done(root):
    """Record that this clone has become a project of its own."""
    path = os.path.join(root, CONFIG)
    try:
        with open(path, encoding="utf-8") as handle:
            config = json.load(handle)
    except (OSError, json.JSONDecodeError):
        return
    config[DONE_KEY] = True
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(config, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def unfilled(root):
    """Forms still awaiting the project's own answers - a to-do list, not a defect.

    Kept apart from pending() on purpose: after the handover an empty skeleton is
    the project's homework, and only the project can do it. Only the core
    documents block, because a project cannot ship with the template's vision.
    """
    return scan(read_documents(root, markdown_files(root)))


def pending(root):
    """Everything still marking this clone as the template itself.

    Empty once the handover has run: gate markers, REQ files and placeholder
    forms then belong to the project, not to the template.
    """
    if is_done(root):
        return []
    findings = gate_findings(root)
    for source, _destination in archive_plan(root):
        findings.append("{0}: template history, not this project's"
                        .format(os.path.relpath(source, root).replace(os.sep, "/")))
    return findings + ["{0}: template placeholder".format(path)
                       for path in unfilled(root)]


GROUPS = (("Anforderungen", "REQ-"), ("Aufgaben", "T-"), ("Entscheidungen", "ADR-"))


def archive_contents(names):
    """Grouped wikilinks to everything archived.

    Every archived note must be linked from here: some were only ever reachable
    through the index, and the project rewrites that.
    """
    remaining = sorted(names)
    lines = []
    for heading, prefix in GROUPS:
        group = [name for name in remaining if name.startswith(prefix)]
        if group:
            lines.append("**{0}**\n".format(heading))
            lines.extend("- [[{0}]]".format(name) for name in group)
            lines.append("")
        remaining = [name for name in remaining if not name.startswith(prefix)]
    if remaining:
        lines.append("**Weiteres**\n")
        lines.extend("- [[{0}]]".format(name) for name in remaining)
    return "\n".join(lines)


def write_archive_readme(root, names):
    """Explain the archive, link its contents, and link it from the index."""
    today = dt.date.today()
    review = today.replace(year=today.year + 1)
    path = os.path.join(root, ARCHIVE, "README.md")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ARCHIVE_README.format(today=today.isoformat(),
                                           review=review.isoformat(),
                                           inhalt=archive_contents(names)))
    index = os.path.join(root, INDEX)
    text = read_text(index)
    if not text or INDEX_LINK in text:
        return
    with open(index, "a", encoding="utf-8") as handle:
        handle.write("\n## Beispielarchiv\n\n" + INDEX_LINK + "\n")


def write_skeletons(root):
    """Replace the framework documents with empty forms carrying fill-in prompts.

    Replaced, not archived: baseline.md and vision.md keep their names in the
    archive, and Obsidian resolves a wikilink by name - two files called
    "Rahmen und Startgate" would make every link to it ambiguous.
    """
    today = dt.date.today()
    review = today.replace(year=today.year + 1)
    os.makedirs(os.path.join(root, REQUIREMENTS), exist_ok=True)
    for name, skeleton in SKELETONS.items():
        with open(os.path.join(root, REQUIREMENTS, name), "w", encoding="utf-8") as handle:
            handle.write(skeleton.format(today=today.isoformat(), review=review.isoformat()))


def apply(root):
    """Reset the gate markers, archive the history, empty the board, leave blank forms.

    A no-op once it has run: a second call must never overwrite the answers the
    project has since written with an empty skeleton again.
    """
    if is_done(root):
        return []
    plan = archive_plan(root)
    if plan:
        os.makedirs(os.path.join(root, ARCHIVE), exist_ok=True)
    for source, destination in plan:
        shutil.move(source, destination)
    if os.path.isdir(os.path.join(root, ARCHIVE)):
        write_archive_readme(root, [os.path.splitext(os.path.basename(target))[0]
                                    for _source, target in plan])
    board = os.path.join(root, BOARD)
    if os.path.exists(board):
        with open(board, "w", encoding="utf-8") as handle:
            handle.write(EMPTY_BOARD)
    write_skeletons(root)
    mark_done(root)
    return [destination for _source, destination in plan]


def report(findings, forms):
    """Print both lists; fail on template leftovers and on unfilled core documents.

    A blank form is not a defect - it is work only the project can do. The four
    core documents are the exception: shipping the template's vision is.
    """
    for item in findings:
        print("PENDING  " + item)
    core = [path for path in forms if path in CORE]
    for path in core:
        print("TO FILL  " + path + "  (core - required before starting)")
    for path in forms:
        if path not in core:
            print("to fill  " + path)
    if not findings and not core:
        print("Handover complete - this is a project of its own.")
        return 0
    if findings:
        print("\n{0} item(s) still belong to the template. Run:\n"
              "  python3 tools/handover.py --apply".format(len(findings)), file=sys.stderr)
    if core:
        print("\n{0} core document(s) still hold the template's text. Fill them via "
              "/req-elicit before writing code.".format(len(core)), file=sys.stderr)
    return 1


def main():
    root = os.getcwd()
    if sys.argv[1:] == ["--apply"]:
        moved = apply(root)
        print("Archived {0} document(s) to {1}/.".format(len(moved),
                                                         ARCHIVE.replace(os.sep, "/")))
        sys.exit(report(pending(root), unfilled(root)))
    if sys.argv[1:] not in ([], ["--check"]):
        print("usage: handover.py [--check | --apply]", file=sys.stderr)
        sys.exit(2)
    sys.exit(report(pending(root), unfilled(root)))


if __name__ == "__main__":
    main()
