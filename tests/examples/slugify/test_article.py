"""TDD example (T-0009): tests for examples/slugify/article.py."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..", "examples", "slugify")
))

from article import article_url  # noqa: E402


def test_builds_url_from_title(): assert article_url("Hello World") == "/articles/hello-world"
