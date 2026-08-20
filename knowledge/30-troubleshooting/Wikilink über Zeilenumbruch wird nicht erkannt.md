---
title: Wikilink über Zeilenumbruch wird nicht erkannt
type: troubleshooting
tags: [topic/meta, stack/obsidian]
status: active
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[Konventionen der Wissensdatenbank]]", "[[00-index]]"]
---

# Wikilink über Zeilenumbruch wird nicht erkannt

## Kurz

`check_vault.py` meldet einen kaputten Wikilink, obwohl die Zielnotiz existiert und der Name
stimmt. Ursache ist fast immer ein Zeilenumbruch **innerhalb** der Klammern.

## Symptom

```
ERROR 2026-08.md: broken wikilink [[REQ-0007 Grenzen für Funktionsgröße und
```

Die Fehlermeldung bricht mitten im Namen ab — das ist der Hinweis.

## Kontext

- Beim Schreiben von Fortschritts- und Aufgabennotizen, wenn eine Zeile die übliche
  Zeilenbreite überschreitet und der Umbruch mitten in den Linktext fällt.
- Zweimal aufgetreten am 2026-08-20, beide Male beim Anhängen an
  `knowledge/10-pm/progress/2026-08.md`.

## Ursache

Die Linkerkennung arbeitet zeilenweise. Ein über zwei Zeilen verteilter `[[…]]`-Ausdruck ist
für sie ein geöffneter, nie geschlossener Link — der Rest des Namens steht in der nächsten
Zeile und wird nie gelesen. Obsidian selbst verhält sich genauso.

## Lösung

Den Link geschlossen auf eine Zeile setzen, notfalls den Satz davor umbrechen:

```markdown
… drückt gegen die flexiblen Größengrenzen
  ([[REQ-0007 Grenzen für Funktionsgröße und Benennung]]); und …
```

## Sackgassen

- Nach einem Tippfehler im Dateinamen suchen. Der Name war beide Male korrekt.

## Vorbeugung

- **Wikilinks nie umbrechen.** Lieber eine zu lange Zeile als ein toter Link — oder den
  Umbruch vor die öffnende Klammer legen.
- `check_vault.py` nach jedem Anhängen an eine Vault-Datei laufen lassen; der Fehler ist
  sofort sichtbar und in einer Zeile behoben.
