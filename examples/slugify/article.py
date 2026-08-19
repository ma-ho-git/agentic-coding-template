# @contract
# provides:   article_url(title: str) -> str
# depends-on: examples/slugify/slugify.py#slugify
# consumers:  none
# invariants: pure; always starts with '/articles/'; slug capped at 60 chars
# updated:    2026-08-19
#!/usr/bin/env python3
"""Build a canonical article URL from its title."""
from __future__ import annotations

from slugify import slugify

SLUG_MAX_LENGTH = 60


def article_url(title):
    """'/articles/<slug>' for this title, slug capped at SLUG_MAX_LENGTH."""
    return "/articles/" + slugify(title, SLUG_MAX_LENGTH)
