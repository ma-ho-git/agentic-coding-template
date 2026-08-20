# @contract
# provides:   check_file(path) -> int failure count; main() CLI entry, exit 1 on failure
# depends-on: .claude/hooks/check_secrets.py, .claude/hooks/check_contract.py,
#             .claude/hooks/check_task.py,
#             .claude/hooks/check_quality.py
# consumers:  .github/workflows/rules.yml, tools/check_all.py
# invariants: read-only; never writes to the repo; reuses hook scripts via subprocess,
#             no rule logic duplicated here
# updated:    2026-08-20
#!/usr/bin/env python3
"""Run the repo's own hooks against a list of files - for CI, no stdin event.

Interactive hooks read a PostToolUse event from stdin. CI has no such event,
only a list of changed files, so this builds the same event shape per file
and reuses the hooks as subprocesses. Run from the repository root:
  python3 tools/ci_check.py <file> [<file> ...]
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

HOOKS_DIR = os.path.join(os.path.dirname(__file__), "..", ".claude", "hooks")
BLOCKING_HOOKS = ("check_secrets.py", "check_contract.py", "check_task.py")
ADVISORY_HOOKS = ("check_quality.py",)


def event_for(path):
    """PostToolUse-shaped event carrying this file's current content."""
    with open(path, encoding="utf-8", errors="replace") as handle:
        content = handle.read()
    return {"tool_input": {"file_path": path, "content": content}}


def run_hook(name, event):
    """Invoke one hook script with event as stdin JSON; return (code, out, err)."""
    result = subprocess.run(
        [sys.executable, os.path.join(HOOKS_DIR, name)],
        input=json.dumps(event),
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout, result.stderr


def check_file(path):
    """Run blocking + advisory hooks against one file; return failure count."""
    event = event_for(path)
    failures = 0
    for name in BLOCKING_HOOKS:
        code, _out, err = run_hook(name, event)
        if code != 0:
            print(err, file=sys.stderr)
            failures += 1
    for name in ADVISORY_HOOKS:
        _code, out, _err = run_hook(name, event)
        if out.strip():
            print(out)
    return failures


def main():
    paths = [path for path in sys.argv[1:] if os.path.isfile(path)]
    failures = sum(check_file(path) for path in paths)
    if failures:
        print("{0} file(s) failed rule checks.".format(failures), file=sys.stderr)
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
