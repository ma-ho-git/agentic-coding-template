"""Positive/negative cases for check_task.py (PostToolUse Write|Edit guard)."""
from __future__ import annotations

from hook_runner import run_hook

WITH_REQUIREMENT = (
    "---\n"
    "id: T-0042\n"
    "type: task\n"
    "status: ready\n"
    'implements: ["[[REQ-0001 Beispiel]]"]\n'
    "---\n\nText\n"
)

INFRASTRUCTURE = (
    "---\n"
    "id: T-0043\n"
    "type: task\n"
    "status: ready\n"
    "implements: []\n"
    "infrastruktur: Werkzeugpflege ohne fachlichen Bezug\n"
    "---\n\nText\n"
)

BARE = (
    "---\n"
    "id: T-0044\n"
    "type: task\n"
    "status: ready\n"
    "---\n\nText\n"
)

EMPTY_WITHOUT_REASON = (
    "---\n"
    "id: T-0045\n"
    "type: task\n"
    "status: ready\n"
    "implements: []\n"
    "---\n\nText\n"
)


def write_task(tmp_path, name, text):
    folder = tmp_path / "knowledge" / "10-pm" / "tasks"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / name).write_text(text)
    return {"tool_input": {"file_path": "knowledge/10-pm/tasks/" + name}}


def test_task_with_requirement_passes(tmp_path):
    event = write_task(tmp_path, "T-0042 Gut.md", WITH_REQUIREMENT)
    code, _out, _err = run_hook("check_task.py", event, project_dir=tmp_path)
    assert code == 0


def test_infrastructure_task_passes(tmp_path):
    event = write_task(tmp_path, "T-0043 Werkzeug.md", INFRASTRUCTURE)
    code, _out, _err = run_hook("check_task.py", event, project_dir=tmp_path)
    assert code == 0


def test_task_without_field_blocks(tmp_path):
    event = write_task(tmp_path, "T-0044 Nackt.md", BARE)
    code, _out, err = run_hook("check_task.py", event, project_dir=tmp_path)
    assert code == 2
    assert "implements" in err


def test_empty_without_reason_blocks(tmp_path):
    event = write_task(tmp_path, "T-0045 Leer.md", EMPTY_WITHOUT_REASON)
    code, _out, err = run_hook("check_task.py", event, project_dir=tmp_path)
    assert code == 2
    assert "infrastruktur" in err


def test_non_task_file_ignored(tmp_path):
    path = tmp_path / "notes.md"
    path.write_text(BARE)
    event = {"tool_input": {"file_path": "notes.md"}}
    code, _out, _err = run_hook("check_task.py", event, project_dir=tmp_path)
    assert code == 0


def test_board_file_ignored(tmp_path):
    folder = tmp_path / "knowledge" / "10-pm"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "board.md").write_text("## Ready\n\n- [ ] [[T-0042 Gut]]\n")
    event = {"tool_input": {"file_path": "knowledge/10-pm/board.md"}}
    code, _out, _err = run_hook("check_task.py", event, project_dir=tmp_path)
    assert code == 0
