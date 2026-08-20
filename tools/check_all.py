# @contract
# provides:   one command running every rule check over a set of changed files;
#             modes --staged | --range A..B | --all | explicit paths; exit 1 on failure
# depends-on: tools/ci_check.py#check_file, .claude/hooks/check_gate.py,
#             .claude/hooks/_common.py#is_code, .claude/hooks/_common.py#load_config,
#             tools/check_vault.py, tools/check_traceability.py, tools/check_licenses.py
# consumers:  .git/hooks/pre-commit (written by tools/install_hooks.py),
#             .github/workflows/rules.yml
# invariants: read-only; blocking failures come only from rigid checks and the gate;
#             the missing-tests hint never fails the run; a git error yields an empty
#             file set, never a crash
# updated:    2026-08-20

#!/usr/bin/env python3
"""Every rule check in one run - the commit choke point and CI both call this.

The Write|Edit hooks cover only tool-mediated writes; files written via Bash or
any other editor bypass them. The commit is the one gate every write path must
pass, so this command exists to run there. Run from the repository root:
  python3 tools/check_all.py --staged | --range A..B | --all | <file> ...
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
HOOKS_DIR = os.path.normpath(os.path.join(TOOLS_DIR, "..", ".claude", "hooks"))
sys.path.insert(0, TOOLS_DIR)
sys.path.insert(0, HOOKS_DIR)
import ci_check  # noqa: E402
from _common import FLEXIBLE, is_code, load_config  # noqa: E402

REPO_CHECKS = ("check_vault.py", "check_traceability.py", "check_licenses.py")
TEST_DIRS = ("tests", "__tests__", "spec")
TEST_MARKERS = ("test_", "_test.", ".test.", ".spec.")
USAGE = "usage: check_all.py --staged | --range A..B | --all | <file> ..."


def run_git(arguments):
    """Stdout of a git command; empty on failure - a missing ref is not a crash."""
    result = subprocess.run(["git"] + arguments, capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else ""


def null_separated(raw):
    """Filenames from -z output; the NUL separator keeps spaces in names intact."""
    return [item for item in raw.split("\0") if item]


def staged_paths():
    """Files the pending commit would introduce or change."""
    return null_separated(run_git(
        ["diff", "--cached", "--name-only", "-z", "--diff-filter=ACMR"]))


def range_paths(range_spec):
    """Files changed inside a commit range, e.g. what one push moved."""
    return null_separated(run_git(
        ["diff", "--name-only", "-z", "--diff-filter=ACMR", range_spec]))


def collect(arguments):
    """File set for the chosen mode; None when the arguments make no sense."""
    if arguments == ["--staged"]:
        return staged_paths()
    if arguments[:1] == ["--range"] and len(arguments) == 2:
        return range_paths(arguments[1])
    if arguments == ["--all"]:
        return null_separated(run_git(["ls-files", "-z"]))
    if arguments and not arguments[0].startswith("--"):
        return list(arguments)
    return None


def is_test_file(path):
    """True for anything the test suite owns - by directory or naming convention."""
    name = os.path.basename(path).lower()
    inside = any(part in TEST_DIRS for part in path.replace(os.sep, "/").split("/"))
    return inside or any(marker in name for marker in TEST_MARKERS)


def missing_tests_hint(paths, enabled):
    """Changed code without a test change - TDD's machine-visible shadow.

    Only the presence of a test change is checkable; that the test came first
    is not. Hence a hint, never a block (.claude/rules/guardrails.md).
    """
    code = [path for path in paths if is_code(path) and not is_test_file(path)]
    if not enabled or not code or any(is_test_file(path) for path in paths):
        return ""
    return (FLEXIBLE + " changed code without a test change: " + ", ".join(code[:8])
            + "\nTDD wants the failing test first (.claude/rules/tdd.md). If none of "
            "these needs one - refactor under existing tests, scaffolding, generated "
            "code - say why in the commit message.")


def gate_reason(stdout_text):
    """Deny reason from a PreToolUse hook's stdout, empty when the write may pass."""
    try:
        payload = json.loads(stdout_text or "{}")
    except json.JSONDecodeError:
        return ""
    output = payload.get("hookSpecificOutput") or {}
    if output.get("permissionDecision") != "deny":
        return ""
    return output.get("permissionDecisionReason") or "denied"


def gate_failures(paths):
    """Start-gate refusals per file - the gate finally guards non-tool writes too."""
    failures = []
    for path in paths:
        _code, out, _err = ci_check.run_hook(
            "check_gate.py", {"tool_input": {"file_path": path}})
        reason = gate_reason(out)
        if reason:
            failures.append("GATE  {0}: {1}".format(path, reason.splitlines()[0]))
    return failures


def repo_failures():
    """Repo-wide checks; their output appears only when they fail."""
    failures = 0
    for name in REPO_CHECKS:
        result = subprocess.run([sys.executable, os.path.join(TOOLS_DIR, name)],
                                capture_output=True, text=True)
        if result.returncode != 0:
            print(result.stdout + result.stderr, file=sys.stderr)
            failures += 1
    return failures


def main():
    collected = collect(sys.argv[1:])
    if collected is None:
        print(USAGE, file=sys.stderr)
        sys.exit(2)
    paths = [path for path in collected if os.path.isfile(path)]
    failures = sum(ci_check.check_file(path) for path in paths)
    gate = gate_failures(paths)
    for line in gate:
        print(line, file=sys.stderr)
    hint = missing_tests_hint(paths, load_config().get("flag_missing_tests", True))
    if hint:
        print(hint)
    failures += len(gate) + repo_failures()
    if failures:
        print("\ncheck_all: {0} blocking finding(s).".format(failures), file=sys.stderr)
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
