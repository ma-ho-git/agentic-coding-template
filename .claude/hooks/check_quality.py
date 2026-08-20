#!/usr/bin/env python3
"""Report size and naming violations after a source file is written. Advisory only."""
from __future__ import annotations

import ast
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import (advise, is_code, load_config, matches_any, read_event,  # noqa: E402
                     relative, target_path)

SIGNATURE = re.compile(
    r"(?:function\s+(?P<fn>\w+)|(?:const|let|var)\s+(?P<cn>\w+)\s*=\s*(?:async\s*)?\("
    r"|(?P<mn>\w+)\s*\([^)]*\)\s*\{)"
)
SKIP_GLOBS = ["**/node_modules/**", "**/dist/**", "**/build/**", "**/vendor/**",
              "**/generated/**", "**/*.min.js"]

# An empty catch body, optionally a stray semicolon. Deliberately narrow: a catch
# that returns a fallback is a visible decision, and one holding a comment carries
# its reason. Only the silent-and-unexplained case is a finding.
EMPTY_CATCH = re.compile(r"catch\s*(?:\([^)]*\))?\s*\{\s*;?\s*\}")
SWALLOW_ADVICE = "handle it, re-raise it, or write in the code why it is ignorable"


# A test name is a sentence about behaviour, not an identifier callers type. The test
# runner owns the prefix (pytest: test_, Go: Test), and .claude/rules/tdd.md requires the
# name to state the behaviour in full - three words plus the prefix by construction. See
# ADR-0013; the word limit would have fired on 139 of this repository's 154 test names.
def is_test_name(name):
    """True for a name the test runner requires to start with its prefix."""
    return name.startswith("test_") or (name.startswith("Test") and name[4:5].isupper())


def split_words(name):
    """Identifier -> word list, for snake_case, kebab-case and camelCase."""
    parts = re.split(r"[_\-]+", name.strip("_"))
    words = []
    for part in parts:
        words.extend(re.findall(r"[A-Z]+(?![a-z])|[A-Z][a-z0-9]*|[a-z0-9]+", part) or [part])
    return [word for word in words if word]


# Explicit binding statements only. Loop and `with` targets bind names too, but
# reading them as "assignments" would surprise anyone counting by hand.
ASSIGNMENTS = (ast.Assign, ast.AugAssign, ast.AnnAssign, ast.NamedExpr)


def count_assignments(node):
    """Assignments in a function - how much state it juggles."""
    return sum(1 for child in ast.walk(node) if isinstance(child, ASSIGNMENTS))


def count_params(node):
    args = node.args
    total = len(args.posonlyargs) + len(args.args) + len(args.kwonlyargs)
    if args.args and args.args[0].arg in ("self", "cls"):
        total -= 1
    return total


def max_depth(node, level=0):
    """Deepest nesting of control-flow statements inside a function."""
    nesting = (ast.If, ast.For, ast.AsyncFor, ast.While, ast.With, ast.AsyncWith, ast.Try)
    deepest = level
    for child in ast.iter_child_nodes(node):
        step = level + 1 if isinstance(child, nesting) else level
        deepest = max(deepest, max_depth(child, step))
    return deepest


def drops_exception(handler):
    """True when the except body only passes or evaluates a bare literal."""
    return all(isinstance(node, ast.Pass)
               or (isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant))
               for node in handler.body)


def carries_reason(lines, handler):
    """True when any line of the except block holds a comment."""
    last = max(getattr(node, "end_lineno", handler.lineno) for node in handler.body)
    return any("#" in line for line in lines[handler.lineno - 1:last])


def find_swallowed(tree, lines):
    """Except blocks that drop the exception and never say why."""
    handlers = [node for node in ast.walk(tree) if isinstance(node, ast.ExceptHandler)]
    silent = [node for node in handlers
              if drops_exception(node) and not carries_reason(lines, node)]
    return ["L{0}: except block drops the exception without a reason - {1}"
            .format(node.lineno, SWALLOW_ADVICE) for node in silent]


def find_empty_catch(source):
    """Empty catch blocks. Text-based, so only the plainly empty case is found."""
    findings = []
    for match in EMPTY_CATCH.finditer(source):
        line = source.count("\n", 0, match.start()) + 1
        findings.append("L{0}: catch block is empty - {1}".format(line, SWALLOW_ADVICE))
    return findings


def inspect_python(source, limits):
    """Findings for a Python module."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []
    findings = find_swallowed(tree, source.splitlines()) if limits["swallowed"] else []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            findings.extend(check_function(node, limits))
        elif isinstance(node, ast.ClassDef) and len(split_words(node.name)) > limits["words"]:
            findings.append("L{0}: class name '{1}' has more than {2} words"
                            .format(node.lineno, node.name, limits["words"]))
    return findings


def check_function(node, limits):
    """Size, parameter, nesting and naming findings for one function node."""
    findings = []
    assignments = count_assignments(node)
    if assignments > limits["assignments"]:
        findings.append("L{0}: {1}() makes {2} assignments (limit {3}) - split it"
                        .format(node.lineno, node.name, assignments, limits["assignments"]))
    params = count_params(node)
    if params > limits["params"]:
        findings.append("L{0}: {1}() takes {2} parameters (limit {3}) - group them into an object"
                        .format(node.lineno, node.name, params, limits["params"]))
    depth = max_depth(node)
    if depth > limits["depth"]:
        findings.append("L{0}: {1}() nests {2} levels deep (limit {3}) - extract or invert"
                        .format(node.lineno, node.name, depth, limits["depth"]))
    if not is_test_name(node.name) and len(split_words(node.name)) > limits["words"]:
        findings.append("L{0}: name '{1}' has more than {2} words"
                        .format(node.lineno, node.name, limits["words"]))
    return findings


def inspect_generic(source, limits):
    """Naming, parameter and empty-catch findings for other languages, best effort."""
    findings = find_empty_catch(source) if limits["swallowed"] else []
    for number, line in enumerate(source.splitlines(), start=1):
        match = SIGNATURE.search(line)
        if not match:
            continue
        name = match.group("fn") or match.group("cn") or match.group("mn") or ""
        if name and name not in ("if", "for", "while", "switch", "catch") \
                and not is_test_name(name) \
                and len(split_words(name)) > limits["words"]:
            findings.append("L{0}: name '{1}' has more than {2} words"
                            .format(number, name, limits["words"]))
        params = line[line.find("(") + 1:line.rfind(")")]
        if params.strip() and len(params.split(",")) > limits["params"]:
            findings.append("L{0}: {1}(...) takes more than {2} parameters"
                            .format(number, name or "function", limits["params"]))
    return findings


def read_limits():
    config = load_config()
    return {
        "assignments": config.get("max_assignments", 20),
        "params": config.get("max_parameters", 3),
        "words": config.get("max_name_words", 3),
        "file": config.get("max_file_lines", 300),
        "depth": config.get("max_nesting_depth", 3),
        # not a threshold but a switch; it rides along because every check reads this bundle
        "swallowed": config.get("flag_swallowed_exceptions", True),
    }


def main():
    event = read_event()
    path = target_path(event)
    if not path or not is_code(path) or not os.path.exists(path):
        sys.exit(0)
    rel = relative(path)
    if matches_any(rel, SKIP_GLOBS):
        sys.exit(0)
    source = open(path, encoding="utf-8", errors="replace").read()
    limits = read_limits()
    findings = inspect_python(source, limits) if path.endswith(".py") \
        else inspect_generic(source, limits)
    total = len(source.splitlines())
    if total > limits["file"]:
        findings.insert(0, "file is {0} lines (limit {1}) - split the module"
                        .format(total, limits["file"]))
    if not findings:
        sys.exit(0)
    advise("Code quality findings in {0}:\n{1}\n\nRules: .claude/rules/code-quality.md. "
           "Fix them now unless splitting would genuinely hurt readability - "
           "in that case leave one line in the code explaining why."
           .format(rel, "\n".join("  - " + item for item in findings[:12])))


if __name__ == "__main__":
    main()
