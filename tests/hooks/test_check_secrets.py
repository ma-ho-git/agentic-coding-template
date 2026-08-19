"""Positive/negative cases for check_secrets.py (PostToolUse Write|Edit guard).

Test names exceed the 3-word naming limit: pytest's mandatory `test_` prefix
already spends one word, and TDD conventions require the name to state the
behaviour in full - shortening further would make it meaningless.

Fake secrets below are built by concatenation, not as bare literals: a
contiguous literal would trip this very hook when this test file itself is
written, since the hook scans line by line regardless of intent.
"""
from __future__ import annotations

from hook_runner import run_hook


def write_event(content, path="app.py"):
    return {"tool_input": {"file_path": path, "content": content}}


def test_allows_clean_content():
    code, _out, _err = run_hook("check_secrets.py", write_event("print('hello')\n"))
    assert code == 0


def test_blocks_aws_access_key():
    fake_key = "AKIA" + "ABCDEFGHIJKLMNOP"
    event = write_event("KEY = '{0}'\n".format(fake_key))
    code, _out, err = run_hook("check_secrets.py", event)
    assert code == 2
    assert "SECURITY BLOCK" in err


def test_blocks_private_key_block():
    marker = "-----BEGIN" + " RSA PRIVATE KEY-----"
    text = marker + "\nMIIBogIBAAKCAQ==\n-----END RSA PRIVATE KEY-----\n"
    code, _out, err = run_hook("check_secrets.py", write_event(text))
    assert code == 2
    assert "SECURITY BLOCK" in err


def test_allows_obvious_placeholder_token():
    event = write_event("token = 'your_token_here_xxxxxxxxx'\n")
    code, _out, _err = run_hook("check_secrets.py", event)
    assert code == 0
