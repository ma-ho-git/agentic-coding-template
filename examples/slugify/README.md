# slugify — die Kette Anforderung → Test → Code an einem Fall

Winziges, echtes Feature: aus einem Artikeltitel eine URL-Kennung machen. Zeigt den vollen
Zyklus aus `CLAUDE.md` §3 — nicht erst ab dem Test, sondern ab der Anforderung.

> Die Anforderungen liegen hier unter `requirements/`, damit das Beispiel für sich steht und
> löschbar bleibt. In einem echten Projekt gehören sie nach `knowledge/05-requirements/` und
> werden dort von `tools/check_traceability.py` mitgeprüft.

## Die Kette

```
REQ-0001 Titel wird zu URL-Slug          (funktional, Rahmen)
   ↓
   test_slugify.py:test_lowercases_and_hyphenates      ← rot
   ↓
   slugify.py#slugify                                  ← grün
   ↓
   article.py#article_url    @contract: depends-on slugify
```

## Ablauf, wie er passiert ist

**Stufe 1 — die Anforderung existiert vor dem Code.**
`REQ-0001` sagt, *was* gelten muss, und nennt eine prüfbare Abnahme: `slugify("Hello World", 60)`
liefert `"hello-world"`, Satzzeichen entfallen, nur `a-z0-9-` im Ergebnis. Genau daraus
lassen sich die Tests ableiten — das ist der Zweck der Prüfbarkeitsregel.

1. **TDD:** `tests/examples/slugify/test_slugify.py` (rot) → `slugify.py` (grün).
2. **Zweite Datei:** `test_article.py` (rot) → `article.py`, das `slugify()` aufruft (grün).
   Die `@contract`-Blöcke verlinken beide Dateien: `slugify.py#consumers` ↔
   `article.py#depends-on`.

**Stufe 2 — eine neue Anforderung kommt dazu.**
`REQ-0002` (Slug-Länge begrenzt) entsteht später, aus dem Betrieb: zu lange Pfadsegmente
werden von nachgelagerten Systemen stillschweigend gekürzt, wodurch zwei Artikel auf
derselben URL landen können.

3. **`/req-change`:** Die neue Anforderung ändert den Vertrag von `slugify()` — der Parameter
   `max_length` wird Pflicht. Betroffen ist alles in der `tasks:`-Liste der Anforderung.
4. **TDD für die Änderung:** neuer Test `test_truncates_to_max_length` (rot) →
   `slugify(text, max_length)` (grün). Der alte Aufruf in `article.py` bricht dadurch.
5. **`/contract-sync`:** Die `consumers:`-Liste in `slugify.py` nennt `article.py` — der
   Wirkungsradius ist ablesbar, ohne den Repo zu durchsuchen. Zur Sicherheit gegengeprüft
   per `grep`: keine undokumentierte Aufrufstelle. Fix: `SLUG_MAX_LENGTH = 60` eingeführt
   und übergeben, beide `@contract`-Blöcke aktualisiert.
6. Volle Suite wieder grün (`pytest tests/examples`).

## Was der Fall zeigt

- Eine **prüfbar formulierte** Anforderung liefert die Tests fast von selbst. Stünde in
  REQ-0002 „der Slug soll nicht zu lang sein", gäbe es nichts zu testen.
- Ein Vertragsbruch ist über die `consumers:`-Liste **sofort auffindbar** statt durch Suche.
- Der Unterschied zwischen den beiden Sync-Skills: `/req-change` arbeitet auf der Ebene
  Anforderung → Aufgabe, `/contract-sync` auf der Ebene Funktion → Aufrufstelle. Dieselbe
  Mechanik, zwei Höhen.
