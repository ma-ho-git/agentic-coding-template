"""TDD example (T-0009): tests for examples/slugify/article.py.

Test names exceed the 3-word naming limit: pytest's mandatory `test_` prefix
already spends one word, and TDD conventions require the name to state the
behaviour in full - shortening further would make it meaningless.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..", "examples", "slugify")
))

from article import article_url  # noqa: E402


def test_builds_url_from_title(): assert article_url("Hello World") == "/articles/hello-world"
