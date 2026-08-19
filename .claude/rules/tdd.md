---
paths:
  - "**/*.{py,pyi,ts,tsx,js,jsx,mjs,cjs,go,rs,java,kt,rb,php,cs,swift,c,h,cpp,hpp,scala,ex,exs,sh}"
---

# Test-Driven Development

Mandatory. Not a style preference.

## The loop

1. **Red** — write the smallest test that expresses the next missing behaviour. Run it.
   Watch it fail for the reason you expect. A test that passes immediately is not a test yet.
2. **Green** — write the least code that makes it pass. Ugly is acceptable here.
3. **Refactor** — clean up with the test as your safety net. Re-run after every step.

Commit at green, refactor, commit again. Never commit at red.

## Rules

- No production code without a failing test that demanded it.
- One behaviour per test. A test name states the behaviour, not the method name:
  `rejects_expired_token`, not `test_validate`.
- Test the contract, not the implementation. If a refactor breaks a test without changing
  behaviour, the test was reaching into internals.
- Boundaries get their own tests: empty, zero, one, maximum, malformed, unauthorized.
- Bug found in existing code? Write the reproducing test first. Then fix it. The test stays.
- Mock only what you do not own (network, clock, filesystem, third-party APIs).
  Mocking your own code is a signal the design is wrong.

## Exceptions

Only three, and each must be stated in the commit message:

- Pure scaffolding with no behaviour (empty module, config file, generated code).
- Throwaway spikes — which are deleted, not merged.
- Code the language makes untestable in isolation (rare; explain why).

"It was faster without a test" is not an exception.
