# @contract
# provides:   CLI check of the requirement <-> task chain; exit 1 on error, 0 otherwise
# depends-on: knowledge/05-requirements/ (REQ notes), knowledge/10-pm/tasks/ (task notes),
#             .claude/rules/requirements.md (the rules being enforced)
# consumers:  .github/workflows/rules.yml
# invariants: read-only; never writes to the vault; warnings never fail the run
# updated:    2026-08-19

#!/usr/bin/env python3
"""Validate traceability: every task serves a requirement, and both sides agree.

Run from the repository root: python3 tools/check_traceability.py
Exit code 1 when any error is found. Warnings do not fail the run.
"""
from __future__ import annotations

import os
import re
import sys

TASKS = os.path.join("knowledge", "10-pm", "tasks")
REQUIREMENTS = os.path.join("knowledge", "05-requirements")
LINK = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")


def frontmatter(text):
    """The frontmatter block, empty string when absent."""
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    return text[3:end] if end != -1 else ""


def raw_field(text, name):
    """One frontmatter field with any indented continuation lines."""
    pattern = r"^{0}:(.*(?:\n[ \t]+.*)*)".format(re.escape(name))
    match = re.search(pattern, frontmatter(text), re.M)
    return match.group(1) if match else ""


def scalar(text, name):
    """First-line value of a frontmatter field, stripped."""
    return raw_field(text, name).splitlines()[0].strip() if raw_field(text, name) else ""


def wikilinks(text, name):
    """Every wikilink target inside one frontmatter field."""
    return [match.group(1).strip() for match in LINK.finditer(raw_field(text, name))]


def parse_note(path, text):
    """Traceability record for one task or requirement note."""
    return {
        "name": os.path.splitext(os.path.basename(path))[0],
        "status": scalar(text, "status"),
        "implements": wikilinks(text, "implements"),
        "tasks": wikilinks(text, "tasks"),
        "infra": scalar(text, "infrastruktur"),
    }


def load_notes(folder, wanted=None):
    """Records for every .md note in folder, optionally filtered by `type:`."""
    records = []
    for name in sorted(os.listdir(folder)) if os.path.isdir(folder) else []:
        if not name.endswith(".md"):
            continue
        path = os.path.join(folder, name)
        with open(path, encoding="utf-8", errors="replace") as handle:
            text = handle.read()
        if wanted and scalar(text, "type") != wanted:
            continue
        records.append(parse_note(path, text))
    return records


def check_implements(tasks, known, errors):
    """Every task links an existing requirement, or is justified infrastructure."""
    for task in tasks:
        if task["infra"]:
            continue
        if not task["implements"]:
            errors.append("{0}: no implements: and no infrastruktur: reason"
                          .format(task["name"]))
        for target in task["implements"]:
            if target not in known:
                errors.append("{0}: implements unknown requirement [[{1}]]"
                              .format(task["name"], target))


def link_mismatch(task, requirement):
    """Error text when the two sides disagree about one link, else empty."""
    forward = requirement["name"] in task["implements"]
    back = task["name"] in requirement["tasks"]
    if forward and not back:
        return ("{0}: implements [[{1}]], but that requirement does not list it in tasks:"
                .format(task["name"], requirement["name"]))
    if back and not forward:
        return ("{0}: lists [[{1}]] in tasks:, but that task does not implement it"
                .format(requirement["name"], task["name"]))
    return ""


def check_backlinks(tasks, requirements, errors):
    """A link must exist on both sides or on neither."""
    for requirement in requirements:
        for task in tasks:
            mismatch = link_mismatch(task, requirement)
            if mismatch:
                errors.append(mismatch)


def check_finished(requirements, done, errors):
    """A requirement marked umgesetzt needs every one of its tasks done."""
    for requirement in requirements:
        if requirement["status"] != "umgesetzt":
            continue
        unfinished = [name for name in requirement["tasks"] if name not in done]
        if unfinished:
            errors.append("{0}: marked umgesetzt but these tasks are not done: {1}"
                          .format(requirement["name"], ", ".join(unfinished)))


def check_unimplemented(requirements, warnings):
    """An agreed requirement with no task is not being built yet."""
    for requirement in requirements:
        if requirement["status"] == "vereinbart" and not requirement["tasks"]:
            warnings.append("{0}: agreed but no task implements it yet"
                            .format(requirement["name"]))


def report(errors, warnings):
    for item in warnings:
        print("WARN  " + item)
    for item in errors:
        print("ERROR " + item)
    print("\n{0} error(s), {1} warning(s)".format(len(errors), len(warnings)))
    return 1 if errors else 0


def main():
    tasks = load_notes(TASKS)
    requirements = load_notes(REQUIREMENTS, wanted="requirement")
    known = {item["name"] for item in requirements}
    done = {item["name"] for item in tasks if item["status"] == "done"}
    errors, warnings = [], []
    check_implements(tasks, known, errors)
    check_backlinks(tasks, requirements, errors)
    check_finished(requirements, done, errors)
    check_unimplemented(requirements, warnings)
    sys.exit(report(errors, warnings))


if __name__ == "__main__":
    main()
