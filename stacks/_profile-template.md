# Stack profile: <language / framework>

Copy this file to `stacks/active.md` during `/bootstrap` and fill in every field.
An unfilled field is a bug — `/task-done` reads this file to run the checks.

## Identity

| Field | Value |
| --- | --- |
| Language | <e.g. Python 3.13> |
| Package manager | <e.g. uv> |
| Verified on | <YYYY-MM-DD> |

## Commands

| Purpose | Command |
| --- | --- |
| Install dependencies | `<...>` |
| Run all tests | `<...>` |
| Run one test file | `<...>` |
| Coverage | `<...>` |
| Lint | `<...>` |
| Auto-fix | `<...>` |
| Type check | `<...>` |
| Dependency audit | `<...>` |
| Build | `<...>` |

## Layout

| What | Where |
| --- | --- |
| Source | `<...>` |
| Tests | `<...>` |
| Test file naming | `<...>` |
| Test function naming | `<...>` |

## Documentation standard

- Docstring style: `<...>`
- Rendering tool: `<...>`
- Enforced by: `<...>`

## Contract comment syntax

```
<the @contract block in this language's comment syntax>
```

## Security defaults

| Concern | Vetted choice |
| --- | --- |
| Password hashing | `<...>` |
| Tokens / JWT | `<...>` |
| HTTP client | `<...>` |
| Input validation | `<...>` |
| Secrets from environment | `<...>` |

## Notes

- <anything about this stack that surprised someone once>
