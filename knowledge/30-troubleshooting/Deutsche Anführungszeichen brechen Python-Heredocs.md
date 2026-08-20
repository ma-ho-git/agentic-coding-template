---
title: Deutsche Anführungszeichen brechen Python-Heredocs
type: troubleshooting
tags: [topic/meta, stack/python]
status: active
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[git_guard verwechselt Erwähnung mit Gebrauch]]", "[[00-index]]"]
---

# Deutsche Anführungszeichen brechen Python-Heredocs

## Kurz

Wer deutschsprachige Vault-Texte über ein Python-Heredoc bearbeitet, stolpert früher oder
später über die typografischen Anführungszeichen. Python sieht darin ein String-Ende.

## Symptom

```
SyntaxError: unterminated string literal (detected at line 4)
SyntaxError: '(' was never closed
```

Die gemeldete Zeile sieht völlig unauffällig aus — sie enthält lediglich ein Zitat in
deutscher Typografie.

## Kontext

Beim Bearbeiten von Dateien unter `knowledge/` und `.claude/skills/` per
`python3 - <<'PY' … PY`. **occurrences: 2** am 2026-08-20 — einmal beim Ergänzen eines
Skills, einmal beim Fortschrittslog.

## Ursache

Der Vault ist deutschsprachig und benutzt konsequent die typografischen Anführungszeichen.
Das schließende davon ist kein ASCII-Zeichen, sieht aber in vielen Schriften einem
geraden Anführungszeichen zum Verwechseln ähnlich. Beim Tippen des Suchmusters gerät leicht
ein gerades hinein — und das beendet den Python-String an Ort und Stelle.

## Lösung

Das Suchmuster so wählen, dass **kein** Anführungszeichen darin vorkommt. Meist genügt ein
kürzerer, eindeutiger Ausschnitt:

```python
s = s.replace("[[REQ-0009 Eine Datei]]", "**REQ-0009 Eine Datei**")
```

Wenn das Zitat unvermeidlich ist: Datei mit `pathlib` lesen, in Python zusammensetzen und
die Sonderzeichen über `\u201e` und `\u201c` schreiben.

## Sackgassen

- Auf einfache Anführungszeichen im Python-Code ausweichen: hilft nicht, wenn im Text auch
  Apostrophe vorkommen — und die kommen vor.
- Dreifach-Anführungszeichen: verschiebt das Problem nur auf längere Textblöcke.

## Vorbeugung

- **Suchmuster ohne Anführungszeichen wählen.** Der kürzeste eindeutige Ausschnitt ist
  ohnehin der robustere.
- Verwandt und aus derselben Familie: [[git_guard verwechselt Erwähnung mit Gebrauch]] —
  auch dort beißt der Inhalt einer Datei, während man sie schreibt.
