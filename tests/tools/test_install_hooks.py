"""Installing the pre-commit choke point (T-0035)."""
from __future__ import annotations

import os
import subprocess
import sys

sys.path.insert(0, os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "..", "tools")
))

import install_hooks  # noqa: E402


def fresh_repo(tmp_path):
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    return tmp_path / ".git" / "hooks" / "pre-commit"


def test_installs_marked_executable_hook(tmp_path, monkeypatch):
    target = fresh_repo(tmp_path)
    monkeypatch.chdir(tmp_path)
    assert install_hooks.install() == 0
    text = target.read_text()
    assert install_hooks.MARKER in text
    assert "check_all.py --staged" in text
    assert os.access(target, os.X_OK)


def test_reinstall_is_idempotent(tmp_path, monkeypatch):
    fresh_repo(tmp_path)
    monkeypatch.chdir(tmp_path)
    assert install_hooks.install() == 0
    assert install_hooks.install() == 0


def test_foreign_hook_is_preserved(tmp_path, monkeypatch):
    target = fresh_repo(tmp_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("#!/bin/sh\necho somebody else\n")
    monkeypatch.chdir(tmp_path)
    assert install_hooks.install() == 1
    assert target.read_text() == "#!/bin/sh\necho somebody else\n"
