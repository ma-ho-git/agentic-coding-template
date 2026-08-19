# slugify — Smoke-Test für den Template-Zyklus

Winziges, echtes Feature: Text zu einem URL-Slug machen. Zeigt den vollen Zyklus aus
`CLAUDE.md` §3 an zwei verknüpften Dateien.

## Ablauf, wie er passiert ist

1. **TDD, v1:** `tests/examples/slugify/test_slugify.py` (rot) →
   `examples/slugify/slugify.py` mit `slugify(text)` (grün).
2. **TDD, zweite Datei:** `test_article.py` (rot) → `article.py` mit `article_url(title)`,
   das `slugify()` aufruft (grün). `@contract`-Blöcke verlinken beide Dateien
   (`slugify.py#consumers` ↔ `article.py#depends-on`).
3. **Echte Vertragsänderung:** `slugify()` bekommt einen Pflichtparameter `max_length`
   (neuer Test zuerst, rot; Implementierung danach, grün) — bricht `article.py`, weil der
   alte Aufruf `slugify(title)` jetzt ein Argument fehlt.
4. **`/contract-sync`:** `consumers:`-Liste in `slugify.py` gelesen → `article.py` als
   einzig betroffene Stelle bestätigt (per `grep` gegen den ganzen Repo verifiziert, keine
   undokumentierte Aufrufstelle gefunden) → kleiner Fix (`SLUG_MAX_LENGTH = 60`
   eingeführt, an `slugify()` übergeben) → beide `@contract`-Blöcke aktuell.
5. Vollständige Test-Suite wieder grün (`pytest tests/examples`).

Damit ist gezeigt: ein Vertragsbruch wird durch die `consumers:`-Liste sofort auffindbar,
ohne den Repo zu durchsuchen — und `/contract-sync` führt den Fix nach, statt ihn nur zu
behaupten.
