#!/usr/bin/env python3
"""Block writes that look like they carry a credential. Runs on Write/Edit."""
from __future__ import annotations

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import block, read_event, relative, target_path  # noqa: E402

PATTERNS = [
    (r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY-----", "private key block"),
    (r"\bghp_[A-Za-z0-9]{36}\b", "GitHub personal access token"),
    (r"\bgithub_pat_[A-Za-z0-9_]{22,}\b", "GitHub fine-grained token"),
    (r"\bgh[pousr]_[A-Za-z0-9]{36,}\b", "GitHub token"),
    (r"\bAKIA[0-9A-Z]{16}\b", "AWS access key id"),
    (r"\bASIA[0-9A-Z]{16}\b", "AWS temporary access key id"),
    (r"\bxox[abposr]-[A-Za-z0-9-]{10,}\b", "Slack token"),
    (r"\bsk-[A-Za-z0-9]{32,}\b", "provider API key (sk- prefix)"),
    (r"\bAIza[0-9A-Za-z_\-]{35}\b", "Google API key"),
    (r"\bglpat-[A-Za-z0-9_\-]{20,}\b", "GitLab token"),
    (r"(?i)\b(?:api[_-]?key|secret|password|passwd|token|client[_-]?secret)\b"
     r"\s*[:=]\s*[\"'][^\"'\s${}<>]{12,}[\"']", "hardcoded credential literal"),
    (r"(?i)\bpostgres(?:ql)?://[^\s:@/]+:[^\s:@/]+@", "database URL with password"),
    (r"(?i)\bmongodb(?:\+srv)?://[^\s:@/]+:[^\s:@/]+@", "database URL with password"),
]

PLACEHOLDER = re.compile(
    r"(?i)(example|placeholder|changeme|your[_-]?\w*|dummy|sample|xxx+|redacted|"
    r"fake|test[_-]?only|<[^>]+>|\$\{[^}]+\}|process\.env|os\.environ|getenv)"
)


def written_text(event):
    """Text this tool call is about to put on disk."""
    payload = event.get("tool_input") or {}
    parts = [payload.get("content"), payload.get("new_string")]
    edits = payload.get("edits") or []
    parts.extend(entry.get("new_string") for entry in edits if isinstance(entry, dict))
    return "\n".join(part for part in parts if isinstance(part, str))


def scan(text):
    """Return findings as (label, line) pairs; obvious placeholders are ignored."""
    findings = []
    for line in text.splitlines():
        for pattern, label in PATTERNS:
            match = re.search(pattern, line)
            if match and not PLACEHOLDER.search(match.group(0)):
                findings.append((label, line.strip()[:120]))
                break
    return findings


def main():
    event = read_event()
    text = written_text(event)
    if not text:
        sys.exit(0)
    findings = scan(text)
    if not findings:
        sys.exit(0)
    path = target_path(event)
    where = relative(path) if path else "this write"
    detail = "\n".join("  - {0}: {1}".format(label, line) for label, line in findings[:5])
    block(
        "SECURITY BLOCK: possible credential in {0}\n{1}\n\n"
        "Secrets must never enter the repository (.claude/rules/security.md).\n"
        "Read it from an environment variable and document only the variable name.\n"
        "If this is a false positive, make it obviously fake (placeholder or <angle brackets>)."
        .format(where, detail)
    )


if __name__ == "__main__":
    main()
