---
paths:
  - "**/*.{py,pyi,ts,tsx,js,jsx,mjs,cjs,go,rs,java,kt,rb,php,cs,swift,c,h,cpp,hpp,scala,ex,exs,sh}"
---

# Code Quality

Hard limits. The hooks in `.claude/hooks/` check these and will tell you when you cross them.
Thresholds live in `.claude/hooks/config.json` and are meant to be tuned per project.

## Size and shape

The **Source** column matters: some limits come from this project's own brief, others the
template added. The added ones are defaults, not doctrine — change them if they do not fit.

| Limit | Value | Enforcement | Source |
| --- | --- | --- | --- |
| Assignments per function | ≤ 20 | warn | project brief |
| Function parameters | ≤ 3 | warn | project brief |
| Identifier length | ≤ 3 words | warn | project brief |
| Nesting depth | ≤ 3 | warn | template addition |
| File length | ≤ 300 lines | warn | template addition |

**Assignments, not lines.** The measure is how much state a function juggles: `x = …`,
`x += …`, `x: T = …` and walrus, counted anywhere inside the function. A long function that
only branches is not flagged; twenty-one bindings are.

Why the two additions exist:

- **Nesting depth** — each level is one more condition a reader must hold in their head to
  understand the innermost line, and the innermost branch is the least tested. An agent does
  not *feel* a deep `elif` chain the way a person does, so the mechanical limit stands in for
  the missing discomfort.
- **File length** — a crude proxy for "this module has more than one responsibility".
  Genuinely cohesive files (parsers, constant tables) may exceed it; it only warns.

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

Two different decisions, do not mix them:

**Unit level — here.** Before writing a non-trivial unit, check whether a known pattern fits:

- **Creation** — Factory, Builder, Dependency Injection
- **Structure** — Adapter, Facade, Decorator, Composite
- **Behaviour** — Strategy, Observer, State, Command, Template Method
- **Data access** — Repository, Unit of Work, Data Mapper

If one fits: use it, and name it in the `@contract` block (`pattern: Strategy`).
If none fits: write the plain solution. A forced pattern is worse than no pattern.
Record non-obvious pattern choices as an ADR in `knowledge/10-pm/decisions/`.

**System level — not here.** How the components are arranged overall (layered, client-server,
pipe and filter …) follows from the quality requirements, not from taste. That decision runs
through `/architecture`, which names the conflict being resolved and writes the ADR.
Repository appears in both lists because it spans the two levels.

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
