"""Traceability checks in tools/check_traceability.py (T-0014).

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

import check_traceability as trace  # noqa: E402

TASK = (
    "---\n"
    "id: T-0042\n"
    "type: task\n"
    "status: done\n"
    'implements: ["[[REQ-0001 Beispiel]]"]\n'
    "---\n\nText\n"
)

TASK_BLOCK_LIST = (
    "---\n"
    "id: T-0042\n"
    "type: task\n"
    "status: doing\n"
    "implements:\n"
    '  - "[[REQ-0001 Beispiel]]"\n'
    '  - "[[REQ-0002 Zweitens]]"\n'
    "---\n\nText\n"
)

TASK_INFRA = (
    "---\n"
    "id: T-0043\n"
    "type: task\n"
    "status: done\n"
    "implements: []\n"
    "infrastruktur: Werkzeugpflege ohne fachlichen Bezug\n"
    "---\n\nText\n"
)

TASK_BARE = (
    "---\n"
    "id: T-0044\n"
    "type: task\n"
    "status: ready\n"
    "---\n\nText\n"
)


def note(name, **fields):
    """Record shaped like parse_note output; serves tasks and requirements alike."""
    record = {"name": name, "status": "ready", "implements": [], "tasks": [],
              "infra": "", "sources": []}
    record.update(fields)
    return record


# --- parsing ---

def test_parses_inline_link_list():
    parsed = trace.parse_note("T-0042 Beispiel.md", TASK)
    assert parsed["name"] == "T-0042 Beispiel"
    assert parsed["status"] == "done"
    assert parsed["implements"] == ["REQ-0001 Beispiel"]
    assert parsed["infra"] == ""


def test_parses_indented_block_list():
    parsed = trace.parse_note("T-0042 Beispiel.md", TASK_BLOCK_LIST)
    assert parsed["implements"] == ["REQ-0001 Beispiel", "REQ-0002 Zweitens"]


def test_parses_infrastructure_reason():
    parsed = trace.parse_note("T-0043 Werkzeug.md", TASK_INFRA)
    assert parsed["implements"] == []
    assert parsed["infra"] == "Werkzeugpflege ohne fachlichen Bezug"


def test_missing_field_is_empty():
    parsed = trace.parse_note("T-0044 Nackt.md", TASK_BARE)
    assert parsed["implements"] == []
    assert parsed["infra"] == ""


# --- implements ---

def test_task_with_known_requirement_passes():
    errors = []
    trace.check_implements([note("T-1 A", implements=["REQ-0001 X"])], {"REQ-0001 X"}, errors)
    assert errors == []


def test_task_without_requirement_fails():
    errors = []
    trace.check_implements([note("T-1 A")], set(), errors)
    assert len(errors) == 1
    assert "T-1 A" in errors[0]


def test_infrastructure_task_is_allowed():
    errors = []
    trace.check_implements([note("T-1 A", infra="Werkzeugpflege")], set(), errors)
    assert errors == []


def test_unknown_requirement_fails():
    errors = []
    trace.check_implements([note("T-1 A", implements=["REQ-9999 Weg"])], {"REQ-0001 X"}, errors)
    assert len(errors) == 1
    assert "REQ-9999 Weg" in errors[0]


# --- backlinks ---

def test_matching_backlinks_pass():
    errors = []
    tasks = [note("T-1 A", implements=["REQ-1 X"])]
    reqs = [note("REQ-1 X", tasks=["T-1 A"])]
    trace.check_backlinks(tasks, reqs, errors)
    assert errors == []


def test_requirement_missing_backlink_fails():
    errors = []
    tasks = [note("T-1 A", implements=["REQ-1 X"])]
    reqs = [note("REQ-1 X")]
    trace.check_backlinks(tasks, reqs, errors)
    assert len(errors) == 1


def test_task_missing_forward_link_fails():
    errors = []
    tasks = [note("T-1 A")]
    reqs = [note("REQ-1 X", tasks=["T-1 A"])]
    trace.check_backlinks(tasks, reqs, errors)
    assert len(errors) == 1


# --- status consistency ---

def test_implemented_requirement_needs_done_tasks():
    errors = []
    reqs = [note("REQ-1 X", status="umgesetzt", tasks=["T-1 A", "T-2 B"])]
    trace.check_finished(reqs, {"T-1 A"}, errors)
    assert len(errors) == 1
    assert "T-2 B" in errors[0]


def test_implemented_requirement_all_done_passes():
    errors = []
    reqs = [note("REQ-1 X", status="umgesetzt", tasks=["T-1 A"])]
    trace.check_finished(reqs, {"T-1 A"}, errors)
    assert errors == []


def test_agreed_requirement_without_task_warns():
    warnings = []
    trace.check_unimplemented([note("REQ-1 X", status="vereinbart")], warnings)
    assert len(warnings) == 1


def test_draft_requirement_without_task_silent():
    warnings = []
    trace.check_unimplemented([note("REQ-1 X", status="entwurf")], warnings)
    assert warnings == []


# --- scenario (T-0024) ---

REQUIREMENT_FROM_SCENARIO = (
    "---\n"
    "type: requirement\n"
    "status: entwurf\n"
    'quelle: Marcus (Auftraggeber) — "[[Szenario]]", Abschnitt Ablauf\n'
    "---\n\nText\n"
)


def test_parses_scenario_reference_in_quelle():
    parsed = trace.parse_note("REQ-0001 Beispiel.md", REQUIREMENT_FROM_SCENARIO)
    assert parsed["sources"] == ["Szenario"]


def test_scenario_without_derived_requirement_fails():
    errors = []
    trace.check_scenario(True, [note("REQ-1 X")], errors)
    assert len(errors) == 1
    assert "szenario" in errors[0].lower()


def test_scenario_with_derived_requirement_passes():
    errors = []
    trace.check_scenario(True, [note("REQ-1 X", sources=["Szenario"])], errors)
    assert errors == []


def test_missing_scenario_needs_no_reference():
    errors = []
    trace.check_scenario(False, [note("REQ-1 X")], errors)
    assert errors == []
