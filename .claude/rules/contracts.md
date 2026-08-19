---
paths:
  - "**/*.{py,pyi,ts,tsx,js,jsx,mjs,cjs,go,rs,java,kt,rb,php,cs,swift,c,h,cpp,hpp,scala,ex,exs,sh}"
---

# Contract Comments (the "vibe-coding comment")

## Why

When you change a function, something elsewhere breaks. Finding it normally means searching the
whole codebase. The contract block records those links **at the code**, so the blast radius of a
change is readable in seconds without a repo-wide search.

This only works if it is always current. A stale contract block is worse than none —
it makes you trust a wrong answer.

## Where

- **Every source file**: one file-level block, at the very top, before imports.
- **Every public / exported symbol**: one block directly above it.
  Private helpers do not need one unless their contract is surprising.

Use the language's normal comment syntax (`#` for Python, `/** */` for TS/JS, `//` for Go/Rust).

## Schema

```
@contract
provides:   what this unit offers — signature and, when not obvious, behaviour
depends-on: contracts this unit relies on — path#symbol, or an external package name
consumers:  known call sites outside this file — path#symbol
invariants: promises callers rely on; error behaviour; thread/IO/mutation guarantees
pattern:    design pattern in use, or omit the line
updated:    YYYY-MM-DD
```

- Every key ends with `:` and starts a line. Multi-line values indent by two spaces.
- Empty value → write `none`. Never leave a key blank.
- Paths are relative to the repository root.
- `updated` is the date this block was last verified against the code — not the file's last edit.

## Example (Python)

```python
# @contract
# provides:   parse_token(raw: str) -> Token; raises TokenError on malformed input
# depends-on: src/crypto/verify.py#verify_signature
#             PyJWT >= 2.8
# consumers:  src/api/auth.py#require_user
#             src/cli/inspect.py#show_token
# invariants: pure; never logs the raw token; expired tokens parse but flag is_expired
# pattern:    none
# updated:    2026-08-19
```

## Keeping it current — the actual discipline

When you change a unit's public surface:

1. Read its `consumers:` list. That is your blast radius. Do not search the repo first.
2. Update every consumer you can update **now**.
3. For any consumer you cannot update now — because it is another agent's task, out of scope,
   or would grow the change beyond review size — create a task in `knowledge/10-pm/tasks/`,
   put it in the **Ready** lane (never Backlog), and link it from both task files.
   Contract debt is urgent debt.
4. Update the `consumers:` and `depends-on:` lists on both sides of every link you changed.
5. Set `updated:` to today.

Run `/contract-sync` to do steps 1–5 with assistance and to catch links you missed.

## When you add a new call site

Adding a call to `foo()` from a new file means editing **two** contract blocks: the new caller's
`depends-on:` and the callee's `consumers:`. Both, in the same commit. This is the only way the
lists stay trustworthy.

## What not to put in it

- Anything the signature already says.
- Implementation detail. The contract is the promise, not the method.
- Call sites inside the same file — those are visible already.
