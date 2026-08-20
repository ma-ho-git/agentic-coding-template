---
id: T-0042
title: README auf den gebauten Stand bringen
type: task
implements: ["[[REQ-0001 Einsatzbereites Gerüst für strukturiertes Vibe-Coding]]"]
status: done
priority: hoch
agent: claude-code
owner: claude-code
created: 2026-08-20
started: 2026-08-20
finished: 2026-08-20
tags: [topic/meta, topic/docs]
related: ["[[REQ-0020 Für unerfahrene Anwender nutzbar]]", "[[T-0040 Übergabe hinterlässt leere Formulare]]"]
---

# T-0042 README auf den gebauten Stand bringen

## Anforderung

[[REQ-0001 Einsatzbereites Gerüst für strukturiertes Vibe-Coding]] — „ohne dass der Nutzer
Regeln, Ablage oder Abläufe selbst erfinden muss". Die README ist die einzige Stelle, an der
jemand vor dem Klonen erfährt, welche Abläufe es gibt.

## Ziel

Die README ist nicht falsch, sie ist **unvollständig**: Sie beschreibt die Vorlage, wie sie
vor vier Ausbaustufen aussah. Gezählt im Text — „flexibel" 0 Treffer, „Übergabe" 0,
„pre-commit" 0, „Ausfall" 0.

Was fehlt:

1. **Anforderungen und Startgate** als Merkmal. Der Kern des Verfahrens taucht in der
   Merkmalstabelle gar nicht auf, obwohl er entscheidet, wann überhaupt codiert werden darf.
2. **Die zwei Klassen von Leitplanken** ([[ADR-0006 Zwei Klassen von Leitplanken]]). Ohne sie
   kann ein Leser eine Wand nicht von einem Hinweis unterscheiden.
3. **Die drei Ankerpunkte** ([[ADR-0012 Durchsetzung an drei Ankerpunkten]]). Genannt sind
   Hooks und CI, nicht aber der Commit — laut ADR der einzige Punkt, den jeder Schreibweg passiert.
4. **Die Übergabe** ([[T-0040 Übergabe hinterlässt leere Formulare]]). Wer klont, erfährt
   nicht, dass `/bootstrap` das Beispielprojekt archiviert und leere Formulare hinterlässt.
5. **Fehler- und Ausfallverhalten** (`.claude/rules/robustness.md`) — ausdrücklich gewünscht,
   nirgends beworben.
6. Die Tabelle `tools/` nennt vier von zehn Skripten.
7. „Blockieren vs. warnen" verweist auf ADR-0002; die Frage beantwortet inzwischen ADR-0006.

## Akzeptanzkriterien

- [x] Die Merkmalstabelle nennt Anforderungen/Startgate, die zwei Leitplankenklassen, die drei
      Ankerpunkte und das Ausfallverhalten
- [x] „Erste Schritte" sagt, was `/bootstrap` mit dem geklonten Repository macht — Übergabe,
      Archiv, leere Formulare, installierter Commit-Haken
- [x] Die Struktur-Tabelle stimmt mit `ls tools/` überein
- [x] Der Verweis unter „Anpassen" zeigt auf die Entscheidung, die die Frage beantwortet
- [x] Keine Behauptung ohne Deckung: jede genannte Datei existiert, jeder genannte Ablauf läuft
- [x] Platzhalter-Marker und Lizenzabschnitt bleiben unangetastet
- [x] `check_vault.py` und `check_placeholders.py` verhalten sich unverändert

## Kontext

- Die README ist deutsch (`CLAUDE.md` §7) und richtet sich an einen Menschen, der noch nicht
  geklont hat. Kein Fachbegriff ohne Erklärung im selben Satz.
- Nicht länger werden um jeden Preis: Was schon dasteht und stimmt, bleibt stehen.

## Agent

`claude-code`.

## Abhängigkeiten

- keine

## Ergebnis

- Merkmalstabelle um drei Zeilen ergänzt: **Anforderungen zuerst** (mit dem Startgate),
  **Fehler- und Ausfallverhalten**, **Leitplanken in zwei Klassen**. Die Zeile „Durchsetzung"
  heißt jetzt „Durchsetzung an drei Stellen" und nennt den Commit-Haken.
- „Erste Schritte" erklärt in vier Punkten, was `/bootstrap` mit dem geklonten Repository
  macht — Archiv statt Löschen, leere Formulare, geschlossenes Startgate, installierter
  `pre-commit`-Haken. Das war vorher eine Überraschung beim ersten Lauf.
- `tools/`-Zeile stimmt wieder mit dem Verzeichnis überein (vier von zehn Skripten waren
  genannt).
- „Blockieren vs. warnen" zeigt jetzt auf `guardrails.md` und ADR-0006 statt auf ADR-0002 —
  die Frage beantwortet inzwischen die Klassenzuordnung, nicht die ältere Hook-Entscheidung.
- Jede Behauptung geprüft: `install_hooks.py` wird in Bootstrap-Schritt 5 aufgerufen, alle
  genannten Dateien existieren, `check_placeholders.py` meldet unverändert 14 Dokumente
  (davon 4 Kern) und der Marker in der README ist unangetastet.
- Suite 158 grün.
