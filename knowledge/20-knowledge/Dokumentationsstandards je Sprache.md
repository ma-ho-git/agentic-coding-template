---
title: Dokumentationsstandards je Sprache
type: knowledge
tags: [topic/meta, stack/python, stack/typescript]
status: active
created: 2026-08-19
updated: 2026-08-19
review_after: 2026-11-19
related: ["[[Konventionen der Wissensdatenbank]]", "[[T-0004 Stack-Profile und Doku-Schema]]", "[[00-index]]"]
---

# Dokumentationsstandards je Sprache

## Kurz

Vorgabe des Templates: pro Sprache den verbreitetsten Standard suchen, im Projekt festschreiben
und anwenden. Diese Notiz hält den Stand fest — samt der Einschränkung, wie belastbar er ist.

## Wichtige Einschränkung

- Es gibt **keine belastbare, aktuelle Erhebung** darüber, welcher Docstring-Stil in Python
  tatsächlich am häufigsten ist. Verfügbar sind nur Ratgeberartikel ohne Datenbasis.
- Die Tabelle unten ist deshalb eine **begründete Vorauswahl**, keine gemessene Wahrheit.
- **Beim Projektstart gilt:** Was im Zielprojekt oder in seinem Ökosystem bereits verwendet wird,
  schlägt jede allgemeine Empfehlung. Erst wenn nichts vorhanden ist, greift die Vorauswahl.

## Vorauswahl je Sprache

| Sprache | Standard | Warum | Werkzeug |
| --- | --- | --- | --- |
| Python | Google-Style-Docstrings | am besten lesbar ohne Rendering, breit unterstützt | Sphinx + napoleon, pydocstyle |
| TypeScript | TSDoc | von Microsoft spezifiziert, TypeScript-spezifisch statt JSDoc-Erbe | TypeDoc, `eslint-plugin-tsdoc` |
| JavaScript | JSDoc | de facto Standard, Typinformation im Kommentar | JSDoc, TypeDoc |
| Go | Doc Comments nach `go doc` | von der Toolchain vorgegeben, keine echte Alternative | `go doc`, pkg.go.dev |
| Rust | `///` Doc-Comments mit Markdown | von `rustdoc` vorgegeben, Beispiele werden getestet | `cargo doc` |
| Java | Javadoc | seit jeher Standard | `javadoc` |
| C# | XML-Dokumentationskommentare | vom Compiler unterstützt | DocFX |

## Python: die drei Kandidaten

- **Google** — flache Abschnitte (`Args:`, `Returns:`, `Raises:`), kompakt, ohne Rendering lesbar
- **NumPy** — Abschnitte mit Unterstreichung, ausführlicher, verbreitet im wissenschaftlichen Umfeld
- **reST / Sphinx** — `:param x:`-Felder, nativ für Sphinx, schlecht direkt lesbar

Vorauswahl **Google**, weil Doku im Template primär für Menschen und Agenten **im Code** gedacht
ist, nicht für gerenderte Webseiten.

## Zusätzlich immer: der Contract-Block

Unabhängig von der Sprache steht am Anfang jeder Quelldatei und über jedem öffentlichen Symbol
der `@contract`-Block. Er ersetzt den Sprachstandard nicht, er ergänzt ihn.
Schema: `.claude/rules/contracts.md`.

## Quellen

- https://tsdoc.org/ — abgerufen 2026-08-19
- https://typedoc.org/documents/Doc_Comments.TSDoc_Support.html — abgerufen 2026-08-19
- Vergleichsartikel zu Python-Docstring-Stilen (Real Python u. a.) — abgerufen 2026-08-19, ohne Datenbasis
