# @contract
# provides:   slugify(text: str, max_length: int) -> str
# depends-on: none
# consumers:  examples/slugify/article.py#article_url
# invariants: pure; lowercase; words joined by '-'; punctuation dropped;
#             result never longer than max_length
# updated:    2026-08-19
#!/usr/bin/env python3
"""Turn free text into a URL-safe slug."""
from __future__ import annotations

import re

WORD = re.compile(r"[a-z0-9]+")


def slugify(text, max_length):
    """Lowercase words joined by '-', punctuation dropped, capped to max_length."""
    slug = "-".join(WORD.findall(text.lower()))
    return slug[:max_length]
