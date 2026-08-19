---
paths:
  - "**/*.{py,pyi,ts,tsx,js,jsx,mjs,cjs,go,rs,java,kt,rb,php,cs,swift,c,h,cpp,hpp,scala,ex,exs,sh}"
---

# Code Quality

Hard limits. The hooks in `.claude/hooks/` check these and will tell you when you cross them.

## Size and shape

| Limit | Value | Enforcement |
| --- | --- | --- |
| Function length | ≤ 20 lines (excluding docstring/comments) | warn |
| Function parameters | ≤ 3 | warn |
| Identifier length | ≤ 3 words | warn |
| File length | ≤ 300 lines | warn |
| Nesting depth | ≤ 3 | warn |

Over a limit, the default answer is **split**. Extract a named helper, introduce a value object,
or move a branch into a polymorphic type. Keep the limit only if splitting would genuinely make
the code harder to read — and then write one line in the code saying why.

**One responsibility per function.** If the name needs an "and", it is two functions.

## Naming

- Maximum three words. `parse_token`, `retry_budget`, `user_repository`.
- Meaningful to a human reading it cold. No `data`, `info`, `helper`, `manager`, `util`,
  `tmp`, `x`, `do_stuff`.
- No abbreviations that are not universal in the domain. `id`, `url`, `http` are fine.
  `usr`, `cfg`, `mgr`, `hndlr` are not.
- Booleans read as predicates: `is_expired`, `has_access`, `can_retry`.
- Functions are verbs, values are nouns. Consistency beats cleverness.

## Design patterns

Before writing a non-trivial unit, check whether a known pattern fits the problem:

- **Creation** — Factory, Builder, Dependency Injection
- **Structure** — Adapter, Facade, Decorator, Composite
- **Behaviour** — Strategy, Observer, State, Command, Template Method
- **Data access** — Repository, Unit of Work, Data Mapper

If one fits: use it, and name it in the `@contract` block (`pattern: Strategy`).
If none fits: write the plain solution. A forced pattern is worse than no pattern.
Record non-obvious pattern choices as an ADR in `knowledge/10-pm/decisions/`.

## Things that get rejected

- Copy-pasted blocks that differ by a constant.
- Boolean parameters that switch behaviour — split into two functions.
- Functions that both compute and print/write. Separate decision from effect.
- Deep chains of `if` on type — that is a missing polymorphism or Strategy.
- Dead code, commented-out code, `TODO` without a task ID.
- Catching an exception and doing nothing with it.
- Magic numbers and magic strings outside a named constant.
- Comments restating the code. Comment *why*, never *what*.

## Documentation

Two layers, both required:

1. The dominant docstring standard of the language, recorded in the active stack profile
   (e.g. Google-style docstrings for Python, TSDoc for TypeScript).
2. The `@contract` block — see `.claude/rules/contracts.md`.

Style for both: telegraphic. Fragments, not sentences. No filler.
Document non-obvious assignments and any computation whose intent is not visible from the code.

Good: `# retry budget shared across all attempts, not per attempt`
Bad: `# This variable stores the retry budget which is used for retrying.`
