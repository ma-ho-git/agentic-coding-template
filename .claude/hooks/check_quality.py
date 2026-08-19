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


def inspect_python(source, limits):
    """Findings for a Python module."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []
    findings = []
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
    if len(split_words(node.name)) > limits["words"]:
        findings.append("L{0}: name '{1}' has more than {2} words"
                        .format(node.lineno, node.name, limits["words"]))
    return findings


def inspect_generic(source, limits):
    """Naming and parameter findings for non-Python languages, best effort."""
    findings = []
    for number, line in enumerate(source.splitlines(), start=1):
        match = SIGNATURE.search(line)
        if not match:
            continue
        name = match.group("fn") or match.group("cn") or match.group("mn") or ""
        if name and name not in ("if", "for", "while", "switch", "catch") \
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
