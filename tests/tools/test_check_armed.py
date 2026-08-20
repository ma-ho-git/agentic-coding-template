"""Proving the guardrails fire instead of assuming it (T-0037).

The hooks fail open: a crashed script or a missing interpreter lets the
write through. check_armed fires every hook with a canary and expects the
refusal - "armed" becomes a checked state, not an assumption.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "..", "tools")
))

import check_armed  # noqa: E402
import install_hooks  # noqa: E402


def test_every_canary_confirms_armed(tmp_path):
    results = check_armed.hook_canaries(str(tmp_path))
    assert results, "no canaries ran"
    for name, armed in results:
        assert armed, name + " did not refuse its canary"


def test_precommit_detected_when_ours(tmp_path):
    hook = tmp_path / "pre-commit"
    hook.write_text("#!/bin/sh\n" + install_hooks.MARKER + "\n")
    assert check_armed.precommit_installed(str(tmp_path))


def test_precommit_missing_is_reported(tmp_path):
    assert not check_armed.precommit_installed(str(tmp_path))


def test_foreign_precommit_not_counted(tmp_path):
    (tmp_path / "pre-commit").write_text("#!/bin/sh\necho other\n")
    assert not check_armed.precommit_installed(str(tmp_path))
