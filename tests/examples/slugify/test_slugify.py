"""TDD example (T-0009): tests for examples/slugify/slugify.py.

Test names exceed the 3-word naming limit: pytest's mandatory `test_` prefix
already spends one word, and TDD conventions require the name to state the
behaviour in full - shortening further would make it meaningless.

v2 (below the first two tests, added later) demonstrates a real breaking
change and the /contract-sync follow-through - see examples/slugify/README.md.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..", "examples", "slugify")
))

from slugify import slugify  # noqa: E402


def test_lowercases_and_hyphenates():
    assert slugify("Hello World", max_length=60) == "hello-world"


def test_strips_punctuation():
    assert slugify("Wait, what?!", max_length=60) == "wait-what"


def test_truncates_to_max_length():
    assert slugify("one two three four", max_length=7) == "one-two"
