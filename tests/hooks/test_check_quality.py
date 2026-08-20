"""Advisory findings from check_quality.py (PostToolUse Write|Edit, non-blocking)."""
from __future__ import annotations

import json

from hook_runner import run_hook

MANY_ASSIGNMENTS = (
    "def do_things():\n"
    + "\n".join("    value_{0} = {0}".format(i) for i in range(25))
    + "\n    return value_0\n"
)

# Long but state-free: 30 lines, zero assignments. Under the assignment rule this
# is fine, which is exactly the difference from the old line-count rule.
LONG_WITHOUT_STATE = (
    "def describe(mode):\n"
    + "\n".join('    if mode == {0}:\n        return "case {0}"'.format(i)
                for i in range(15))
    + '\n    return "none"\n'
)

CLEAN_FUNCTION = "def add(a, b):\n    return a + b\n"


def write_file(tmp_path, name, text):
    (tmp_path / name).write_text(text)
    return {"tool_input": {"file_path": name}}


def findings(tmp_path, name, text):
    event = write_file(tmp_path, name, text)
    _code, out, _err = run_hook("check_quality.py", event, project_dir=tmp_path)
    return json.loads(out)["hookSpecificOutput"]["additionalContext"] if out.strip() else ""


def test_many_assignments_flagged(tmp_path):
    assert "do_things" in findings(tmp_path, "big.py", MANY_ASSIGNMENTS)


def test_long_without_state_passes(tmp_path):
    assert "describe" not in findings(tmp_path, "branchy.py", LONG_WITHOUT_STATE)


def test_clean_function_is_silent(tmp_path):
    assert findings(tmp_path, "small.py", CLEAN_FUNCTION) == ""


# --- swallowed exceptions (T-0026) ---

SILENT_EXCEPT = (
    "def load(path):\n"
    "    try:\n"
    "        return open(path).read()\n"
    "    except OSError:\n"
    "        pass\n"
)

EXPLAINED_EXCEPT = (
    "def load(path):\n"
    "    try:\n"
    "        return open(path).read()\n"
    "    except OSError:\n"
    "        pass  # optional cache file, absence is normal\n"
)

RERAISING_EXCEPT = (
    "def load(path):\n"
    "    try:\n"
    "        return open(path).read()\n"
    "    except OSError:\n"
    "        raise\n"
)

HANDLING_EXCEPT = (
    "def load(path, log):\n"
    "    try:\n"
    "        return open(path).read()\n"
    "    except OSError as error:\n"
    "        log(error)\n"
)

EMPTY_CATCH = (
    "function load(path) {\n"
    "  try {\n"
    "    return read(path);\n"
    "  } catch (error) {\n"
    "  }\n"
    "}\n"
)

COMMENTED_CATCH = (
    "function load(path) {\n"
    "  try {\n"
    "    return read(path);\n"
    "  } catch (error) {\n"
    "    // optional cache file, absence is normal\n"
    "  }\n"
    "}\n"
)


def test_silent_except_is_flagged(tmp_path):
    assert "drops the exception" in findings(tmp_path, "silent.py", SILENT_EXCEPT)


def test_explained_except_passes(tmp_path):
    assert findings(tmp_path, "explained.py", EXPLAINED_EXCEPT) == ""


def test_reraising_except_passes(tmp_path):
    assert findings(tmp_path, "reraise.py", RERAISING_EXCEPT) == ""


def test_handling_except_passes(tmp_path):
    assert findings(tmp_path, "handled.py", HANDLING_EXCEPT) == ""


def test_empty_catch_is_flagged(tmp_path):
    assert "catch block is empty" in findings(tmp_path, "silent.js", EMPTY_CATCH)


def test_commented_catch_passes(tmp_path):
    assert findings(tmp_path, "explained.js", COMMENTED_CATCH) == ""


def test_swallow_check_can_be_disabled(tmp_path):
    hooks = tmp_path / ".claude" / "hooks"
    hooks.mkdir(parents=True)
    (hooks / "config.json").write_text('{"flag_swallowed_exceptions": false}')
    assert findings(tmp_path, "silent.py", SILENT_EXCEPT) == ""


# --- test names are behaviour sentences, not identifiers (T-0041) ---

LONG_TEST_NAME = "def test_rejects_an_expired_token():\n    assert True\n"
LONG_GO_TEST_NAME = "func TestRejectsAnExpiredToken(t *testing.T) {\n\tt.Fail()\n}\n"
LONG_HELPER_NAME = "def make_a_fake_token():\n    return 1\n"
FAT_TEST_SIGNATURE = "def test_it(one, two, three, four):\n    assert one\n"


def test_long_test_name_passes(tmp_path):
    assert findings(tmp_path, "test_auth.py", LONG_TEST_NAME) == ""


def test_go_test_name_passes(tmp_path):
    assert "more than 3 words" not in findings(tmp_path, "auth_test.go", LONG_GO_TEST_NAME)


def test_helper_in_test_file_flagged(tmp_path):
    """The exemption hangs on the name, not on the directory."""
    assert "make_a_fake_token" in findings(tmp_path, "test_auth.py", LONG_HELPER_NAME)


def test_other_limits_still_apply_to_tests(tmp_path):
    assert "takes 4 parameters" in findings(tmp_path, "test_auth.py", FAT_TEST_SIGNATURE)
