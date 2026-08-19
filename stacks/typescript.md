# Stack profile: TypeScript

Verify every version and command during `/bootstrap` before copying this to `stacks/active.md`.
The values below were plausible on 2026-08-19 and were **not** re-checked since.

## Identity

| Field | Value |
| --- | --- |
| Language | TypeScript 5.x, strict mode on |
| Package manager | pnpm |
| Verified on | — (fill in at bootstrap) |

## Commands

| Purpose | Command |
| --- | --- |
| Install dependencies | `pnpm install --frozen-lockfile` |
| Run all tests | `pnpm vitest run` |
| Run one test file | `pnpm vitest run src/token.test.ts` |
| Coverage | `pnpm vitest run --coverage` |
| Lint | `pnpm eslint .` |
| Auto-fix | `pnpm eslint . --fix && pnpm prettier --write .` |
| Type check | `pnpm tsc --noEmit` |
| Dependency audit | `pnpm audit --audit-level=moderate` |
| Build | `pnpm build` |

## Layout

| What | Where |
| --- | --- |
| Source | `src/` |
| Tests | next to the source file, or `tests/` — pick one and keep it |
| Test file naming | `<module>.test.ts` |
| Test function naming | `it("rejects an expired token", ...)` |

## Documentation standard

- Docstring style: **TSDoc** (`@param`, `@returns`, `@throws`, `@remarks`)
- Rendering tool: TypeDoc
- Enforced by: `eslint-plugin-tsdoc`

## Contract comment syntax

```typescript
/**
 * @contract
 * provides:   parseToken(raw: string): Token; throws TokenError on malformed input
 * depends-on: src/crypto/verify.ts#verifySignature
 * consumers:  src/api/auth.ts#requireUser
 * invariants: pure; never logs the raw token
 * updated:    2026-08-19
 */
```

## Security defaults

| Concern | Vetted choice |
| --- | --- |
| Password hashing | `argon2` or `bcrypt`, never a hand-rolled hash |
| Tokens / JWT | `jose` with an explicit algorithm allowlist |
| HTTP client | native `fetch` with an `AbortSignal` timeout on every call |
| Input validation | `zod` at the process boundary |
| Secrets from environment | validate `process.env` once at startup, then never read it again |

## Notes

- `strict: true` plus `noUncheckedIndexedAccess: true`. Without the second, indexing lies to you.
- Never `any`. Use `unknown` and narrow it.
- Runtime validation is not optional just because the types look right — types vanish at runtime.
