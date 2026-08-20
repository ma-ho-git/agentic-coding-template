# @contract
# provides:   hook_canaries(root) -> [(hook, armed)]; precommit_installed(dir) -> bool;
#             main() prints ARMED/FAILED per guardrail, exit 1 when any failed
# depends-on: every hook under .claude/hooks/, tools/install_hooks.py#MARKER
# consumers:  .claude/skills/bootstrap/SKILL.md (arming step)
# invariants: read-only outside its own temp directory; canary literals are assembled
#             at runtime so scanners never mistake mention for use; a hook that
#             crashes counts as FAILED, never as armed (fail closed)
# updated:    2026-08-20

#!/usr/bin/env python3
"""Prove the guardrails fire. Run from the repository root after /bootstrap.

The hooks fail open - a crashed script or a missing interpreter lets a write
through silently. This fires every hook with a canary event and expects the
refusal, turning "armed" from an assumption into a checked state.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
HOOKS_DIR = os.path.normpath(os.path.join(TOOLS_DIR, "..", ".claude", "hooks"))
sys.path.insert(0, TOOLS_DIR)
from install_hooks import MARKER, hooks_directory  # noqa: E402

# Assembled at runtime: mention must never look like use to the scanners -
# git_guard reads whole command texts and cannot tell a canary from an attack.
# Not AWS's documented example key: that one contains EXAMPLE, which the
# placeholder exemption in check_secrets deliberately lets through.
FAKE_ACCESS_KEY = "AKIA" + "QZMJ3K7WPBXR2LDV"
DESTRUCTIVE_COMMAND = "git push " + "--for" + "ce origin ma" + "in"
UNCONTRACTED = "\n".join("value_{0} = {0}".format(index) for index in range(12)) + "\n"
BUSY_FUNCTION = ("def busy():\n"
                 + "\n".join("    slot_{0} = {0}".format(index) for index in range(25))
                 + "\n    return slot_0\n")


def run_hook(name, event, root):
    """One hook as a subprocess against a given project root."""
    environment = dict(os.environ, CLAUDE_PROJECT_DIR=root)
    return subprocess.run(
        [sys.executable, os.path.join(HOOKS_DIR, name)],
        input=json.dumps(event), capture_output=True, text=True, env=environment)


def denies(result):
    """True when a PreToolUse hook answered with a deny decision."""
    try:
        payload = json.loads(result.stdout or "{}")
    except json.JSONDecodeError:
        return False
    return (payload.get("hookSpecificOutput") or {}).get("permissionDecision") == "deny"


def advises(result):
    """True when a PostToolUse hook put a finding into the context."""
    try:
        payload = json.loads(result.stdout or "{}")
    except json.JSONDecodeError:
        return False
    return bool((payload.get("hookSpecificOutput") or {}).get("additionalContext"))


def write_canary(root, relative, text):
    """A canary file inside the temp project; returns its absolute path."""
    path = os.path.join(root, relative)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return path


def file_event(path):
    with open(path, encoding="utf-8") as handle:
        return {"tool_input": {"file_path": path, "content": handle.read()}}


def gate_armed(root):
    """A closed framework must refuse product source."""
    write_canary(root, os.path.join("knowledge", "05-requirements", "baseline.md"),
                 "---\nbaseline_status: entwurf\n---\n")
    event = {"tool_input": {"file_path": os.path.join(root, "src", "app.py")}}
    return denies(run_hook("check_gate.py", event, root))


def secrets_armed(root):
    path = write_canary(root, "leak.py", 'aws_access_key_id = "' + FAKE_ACCESS_KEY + '"\n')
    return run_hook("check_secrets.py", file_event(path), root).returncode == 2


def contract_armed(root):
    path = write_canary(root, "bare.py", UNCONTRACTED)
    return run_hook("check_contract.py", file_event(path), root).returncode == 2


def task_armed(root):
    path = write_canary(root, os.path.join("knowledge", "10-pm", "tasks", "T-9999 Probe.md"),
                        "---\nid: T-9999\ntype: task\nstatus: ready\n---\n")
    return run_hook("check_task.py", file_event(path), root).returncode == 2


def quality_armed(root):
    path = write_canary(root, "busy.py", BUSY_FUNCTION)
    return advises(run_hook("check_quality.py", file_event(path), root))


def guard_armed(root):
    event = {"tool_input": {"command": DESTRUCTIVE_COMMAND}}
    return denies(run_hook("git_guard.py", event, root))


def hook_canaries(root):
    """Every guardrail against its canary, inside the given scratch root."""
    return [
        ("check_gate.py", gate_armed(root)),
        ("check_secrets.py", secrets_armed(root)),
        ("check_contract.py", contract_armed(root)),
        ("check_task.py", task_armed(root)),
        ("check_quality.py", quality_armed(root)),
        ("git_guard.py", guard_armed(root)),
    ]


def precommit_installed(folder):
    """True when the commit choke point is in place and ours."""
    path = os.path.join(folder, "pre-commit")
    try:
        with open(path, encoding="utf-8", errors="replace") as handle:
            return MARKER in handle.read()
    except OSError:
        return False


def report(results):
    for name, armed in results:
        print("{0}  {1}".format("ARMED " if armed else "FAILED", name))
    failed = [name for name, armed in results if not armed]
    if failed:
        print("\n{0} guardrail(s) did not refuse their canary. The write path is open;"
              "\nfix this before trusting any rigid rule.".format(len(failed)),
              file=sys.stderr)
    return 1 if failed else 0


def main():
    with tempfile.TemporaryDirectory() as scratch:
        results = hook_canaries(scratch)
    results.append(("pre-commit choke point", precommit_installed(hooks_directory())))
    sys.exit(report(results))


if __name__ == "__main__":
    main()
