# @contract
# provides:   install() -> exit code; writes .git/hooks/pre-commit running
#             check_all --staged; main() CLI entry
# depends-on: tools/check_all.py (the command the hook runs), git rev-parse --git-path
# consumers:  .claude/skills/bootstrap/SKILL.md (setup step)
# invariants: idempotent for our own hook; a foreign pre-commit hook is never
#             overwritten - refused loudly instead (fail closed); no other file touched
# updated:    2026-08-20

#!/usr/bin/env python3
"""Install the commit choke point. Run from the repository root, re-run any time."""
from __future__ import annotations

import os
import stat
import subprocess
import sys

MARKER = "# agentic-coding-template pre-commit"
HOOK_BODY = """#!/bin/sh
{marker}
# Runs every rule check over the staged files (tools/check_all.py).
# Reinstall with: python3 tools/install_hooks.py - replaced only while the
# marker above is present; a hook of your own is left alone.
cd "$(git rev-parse --show-toplevel)" || exit 1
if command -v python3 >/dev/null 2>&1; then
    exec python3 tools/check_all.py --staged
fi
exec python tools/check_all.py --staged
""".format(marker=MARKER)


def hooks_directory():
    """Git's hooks directory for this checkout; empty outside a repository."""
    result = subprocess.run(["git", "rev-parse", "--git-path", "hooks"],
                            capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else ""


def is_ours(path):
    """True when the existing hook carries our marker and may be replaced."""
    try:
        with open(path, encoding="utf-8", errors="replace") as handle:
            return MARKER in handle.read()
    except OSError:
        return False


def install():
    """Write the pre-commit hook; refuse to clobber somebody else's."""
    folder = hooks_directory()
    if not folder:
        print("install_hooks: not inside a git repository.", file=sys.stderr)
        return 1
    target = os.path.join(folder, "pre-commit")
    if os.path.exists(target) and not is_ours(target):
        print("install_hooks: {0} exists and is not ours - left untouched.\n"
              "Merge our line into it yourself: python3 tools/check_all.py --staged"
              .format(target), file=sys.stderr)
        return 1
    os.makedirs(folder, exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(HOOK_BODY)
    os.chmod(target, os.stat(target).st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    print("pre-commit installed: " + target)
    return 0


def main():
    sys.exit(install())


if __name__ == "__main__":
    main()
