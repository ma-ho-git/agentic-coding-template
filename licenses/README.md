# Licence texts of third-party components

Every component listed in `knowledge/05-requirements/fremdkomponenten.md` keeps its licence
text here, as a plain file named after the component:

```
licenses/<component>-LICENSE.txt
```

`tools/check_licenses.py` reports a registered component whose licence text is missing, and
warns about a text here that no entry references.

**Attribution** — where a licence requires naming the authors, that naming goes into the
project's own `README.md`, not only here. A licence text filed away is not attribution.

This directory is empty apart from this file: the template uses no third-party code
(`knowledge/10-pm/decisions/ADR-0010 …`).
