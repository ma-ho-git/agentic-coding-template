---
paths:
  - "**/*.{py,pyi,ts,tsx,js,jsx,mjs,cjs,go,rs,java,kt,rb,php,cs,swift,c,h,cpp,hpp,scala,ex,exs,sh}"
---

# Security

No known or obvious vulnerability ships. "Obvious" means: it appears on the OWASP Top 10,
or a reviewer with a security habit would catch it in one read.

## Always

- **Secrets never enter the repo.** Not in code, tests, fixtures, comments, commit messages,
  or the knowledge base. Use environment variables and document the variable name only.
  A secrets hook blocks commits and writes that look like credentials.
- **Validate at the boundary.** Everything from outside the process is untrusted:
  HTTP, CLI arguments, files, environment, database rows, other services.
  Validate type, range, length, and format on entry — not at the point of use.
- **Parameterize queries.** No string concatenation into SQL, shell, LDAP, or XPath.
- **Encode on output** for the target context (HTML, attribute, URL, JS, SQL).
- **Fail closed.** On error, deny. Never fall through to a permissive default.
- **Least privilege** for credentials, file permissions, container users, tokens, and scopes.
- **Pin and audit dependencies.** Lockfile committed. Run the stack profile's audit command
  before adding a dependency, and record the decision if it has known advisories.

## Never

- Roll your own crypto, password hashing, or token format. Use the vetted library
  named in the active stack profile.
- Log secrets, tokens, full payment data, or personal data. Redact before logging.
- Disable TLS verification, even "temporarily", even in tests.
- `eval`, `exec`, deserialization of untrusted data, or shelling out with interpolated input.
- Swallow an authentication or authorization error.
- Commit a `.env` with real values.

## Review checklist

Before a task leaves `Review`, walk this list against the diff:

1. Where does untrusted input enter, and where is it validated?
2. What identity is this code running as, and does it need that much?
3. What does it log, and could any of it be sensitive?
4. Any new dependency? Audited? Actually needed?
5. Any new endpoint, file path, or query built from input?
6. What happens on the error path — does it deny, or does it leak?

Record anything non-obvious you decided as an ADR in `knowledge/10-pm/decisions/`.
