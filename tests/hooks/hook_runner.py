"""Run a repo hook script as a subprocess and capture exit code, stdout, stderr."""
from __future__ import annotations

import json
import os
import subprocess
import sys

HOOKS_DIR = os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "..", ".claude", "hooks")
)
REPO_ROOT = os.path.normpath(os.path.join(HOOKS_DIR, "..", ".."))


def run_hook(name, event=None, project_dir=None):
    """Invoke .claude/hooks/<name> with event as stdin JSON; return (code, out, err)."""
    env = dict(os.environ)
    env["CLAUDE_PROJECT_DIR"] = str(project_dir) if project_dir else REPO_ROOT
    result = subprocess.run(
        [sys.executable, os.path.join(HOOKS_DIR, name)],
        input=json.dumps(event or {}),
        capture_output=True,
        text=True,
        env=env,
    )
    return result.returncode, result.stdout, result.stderr
