# Stack profile: Python (active)

Verified during `/bootstrap` on 2026-08-19. Copied from `stacks/python.md` and adjusted to
match this repo's actual layout: there is no application package here, only tooling
(`.claude/hooks/`, `tools/`). Runtime deps: none — everything is stdlib. Dev deps
(`pytest`, `ruff`, `mypy`) are installed globally in this environment; a `pyproject.toml`
pinning them is still missing (tracked in T-0007, not created here to avoid bootstrap scope
creep).

## Identity

| Field | Value |
| --- | --- |
| Language | Python 3.11+ (installed: 3.11.15; template doc said 3.12+ — corrected) |
| Package manager | uv (fallback: pip + venv) — no `pyproject.toml` yet, see note above |
| Verified on | 2026-08-19 |

## Commands

| Purpose | Command |
| --- | --- |
| Install dependencies | none yet (stdlib only); once `pyproject.toml` exists: `uv sync` |
| Run all tests | `uv run pytest` (or plain `pytest` until `pyproject.toml` exists) |
| Run one test file | `pytest tests/test_check_secrets.py -x` |
| Coverage | `pytest --cov=.claude/hooks --cov=tools --cov-report=term-missing` |
| Lint | `ruff check .` |
| Auto-fix | `ruff check --fix . && ruff format .` |
| Type check | `mypy .claude/hooks tools` |
| Dependency audit | `pip-audit` (no third-party deps currently, so low-value until any are added) |
| Build | n/a — this repo ships as a template, not a package |

## Layout

| What | Where |
| --- | --- |
| Source | `.claude/hooks/`, `tools/` |
| Tests | `tests/` (to be created — no tests exist yet), mirroring source tree |
| Test file naming | `test_<module>.py` |
| Test function naming | `test_<behaviour>` — behaviour, not method name |

## Documentation standard

- Docstring style: **Google** (`Args:`, `Returns:`, `Raises:`)
- Rendering tool: none set up (no Sphinx) — not needed for internal tooling scripts
- Enforced by: `ruff` rule set `D` (pydocstyle), convention `google`

## Contract comment syntax

```python
# @contract
# provides:   parse_token(raw: str) -> Token; raises TokenError on malformed input
# depends-on: src/crypto/verify.py#verify_signature
# consumers:  src/api/auth.py#require_user
# invariants: pure; never logs the raw token
# updated:    2026-08-19
```

Note: `.claude/hooks/_common.py` is explicitly exempt from `@contract` (tooling, not
project source) per its own header — this is intentional, not a gap.

## Security defaults

| Concern | Vetted choice |
| --- | --- |
| Password hashing | `argon2-cffi`, never `hashlib` directly |
| Tokens / JWT | `pyjwt` with an explicit algorithm allowlist |
| HTTP client | `httpx` with a timeout on every call |
| Input validation | `pydantic` at the process boundary |
| Secrets from environment | `os.environ["NAME"]` — fail loudly if missing |

None of these currently apply — the repo has no auth, network, or password code. Kept for
when a downstream project (or `T-0009` example project) needs them.

## Notes

- `ruff` replaces flake8, isort, pyupgrade and black in one tool — do not add those separately.
- Set `pytest` to `--strict-markers` and `-W error` so warnings cannot rot unnoticed, once a
  `pyproject.toml`/`pytest.ini` exists.
- Mutable default arguments are the classic Python trap. `None` plus an in-body default.
- Installed toolchain in this environment verified present: `uv`, `pytest`, `ruff`, `mypy`
  (checked via `which` on 2026-08-19).
