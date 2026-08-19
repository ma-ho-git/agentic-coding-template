# Stack profile: Python

Verify every version and command during `/bootstrap` before copying this to `stacks/active.md`.
The values below were plausible on 2026-08-19 and were **not** re-checked since.

## Identity

| Field | Value |
| --- | --- |
| Language | Python 3.12+ |
| Package manager | uv (fallback: pip + venv) |
| Verified on | — (fill in at bootstrap) |

## Commands

| Purpose | Command |
| --- | --- |
| Install dependencies | `uv sync` |
| Run all tests | `uv run pytest` |
| Run one test file | `uv run pytest tests/test_token.py -x` |
| Coverage | `uv run pytest --cov=src --cov-report=term-missing` |
| Lint | `uv run ruff check .` |
| Auto-fix | `uv run ruff check --fix . && uv run ruff format .` |
| Type check | `uv run mypy src` |
| Dependency audit | `uv run pip-audit` |
| Build | `uv build` |

## Layout

| What | Where |
| --- | --- |
| Source | `src/<package>/` |
| Tests | `tests/`, mirroring the source tree |
| Test file naming | `test_<module>.py` |
| Test function naming | `test_<behaviour>` — behaviour, not method name |

## Documentation standard

- Docstring style: **Google** (`Args:`, `Returns:`, `Raises:`)
- Rendering tool: Sphinx with the `napoleon` extension
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

## Security defaults

| Concern | Vetted choice |
| --- | --- |
| Password hashing | `argon2-cffi`, never `hashlib` directly |
| Tokens / JWT | `pyjwt` with an explicit algorithm allowlist |
| HTTP client | `httpx` with a timeout on every call |
| Input validation | `pydantic` at the process boundary |
| Secrets from environment | `os.environ["NAME"]` — fail loudly if missing |

## Notes

- `ruff` replaces flake8, isort, pyupgrade and black in one tool — do not add those separately.
- Set `pytest` to `--strict-markers` and `-W error` so warnings cannot rot unnoticed.
- Mutable default arguments are the classic Python trap. `None` plus an in-body default.
