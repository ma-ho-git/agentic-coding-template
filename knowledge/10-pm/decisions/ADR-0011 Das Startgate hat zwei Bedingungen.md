---
title: ADR-0011 Das Startgate hat zwei Bedingungen
type: decision
tags: [topic/meta, topic/agents]
status: active
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-02-20
related: ["[[ADR-0006 Zwei Klassen von Leitplanken]]", "[[REQ-0024 Vorhandene Lösungen werden vor dem Codieren geprüft]]", "[[Fremdlösungen]]", "[[T-0028 Startgate verlangt die Fremdlösungs-Entscheidung]]"]
---

# ADR-0011 Das Startgate hat zwei Bedingungen

## Status

angenommen

## Kontext

- [[REQ-0024 Vorhandene Lösungen werden vor dem Codieren geprüft]] sagt: Die Suche nach einer
  bestehenden Lösung **muss angeboten werden**.
- Ein Schritt, der nur in Prosa steht, ist nach
  [[ADR-0006 Zwei Klassen von Leitplanken]] eine flexible Leitplanke, egal wie er sich
  nennt. Dieses Projekt hat das schon einmal am eigenen Bestand gefunden: Das Startgate war
  die weichste aller Leitplanken, bis T-0020 es durchgesetzt hat.
- Entscheidung des Auftraggebers vom 2026-08-20, auf Nachfrage: Startgate erweitern statt
  bloßem Prozessschritt.

## Optionen

| Option | Vorteil | Nachteil |
| --- | --- | --- |
| Nur Prozessschritt in Zyklus und Skills | keine zusätzliche Reibung beim Projektstart | der Schritt lässt sich überspringen, ohne dass es auffällt — genau der Zustand, den die Anforderung beheben soll |
| Eigene Prüfung, eigene Meldung | klare Trennung | zwei Sperren, die dasselbe schützen; der Nutzer sieht zwei Wände statt einer Tür mit zwei Schlössern |
| **Zweite Bedingung am bestehenden Startgate** | ein Ort, an dem „darf jetzt gebaut werden?" beantwortet wird | die Meldung muss sagen, *welche* Bedingung fehlt, sonst verwirrt sie |

## Entscheidung

`check_gate.py` prüft zwei Bedingungen, in dieser Reihenfolge:

1. **Rahmen vereinbart** — `baseline_status: vereinbart`
2. **Fremdlösungs-Frage beantwortet** — `scan_status` in `fremdloesungen.md` ist `gesucht`
   oder `uebersprungen`

Die Reihenfolge ist keine Geschmacksfrage: Ohne vereinbarte Anforderungen fehlt der Maßstab,
an dem ein Kandidat gemessen würde. Zuerst nach Fremdlösungen zu fragen hieße, nach etwas zu
suchen, das noch niemand beschrieben hat.

Die Meldung nennt immer nur die **eine** fehlende Bedingung und den einen Schritt, der sie
erfüllt. Zwei Wände auf einmal zu zeigen, hilft niemandem.

### Warum starr, obwohl nicht unheilbar

Der Zuordnungstest aus [[ADR-0006 Zwei Klassen von Leitplanken]] trifft hier über Kriterium 4:
Die Entscheidung, ob auf fremdem Code aufgesetzt wird, ist dem Menschen vorbehalten. Ein
Agent, der sie durch Losbauen faktisch vorwegnimmt, umgeht sie.

Kriterium 1 — unheilbar — trifft **nicht im strengen Sinn**: Man kann später noch eine
Bibliothek übernehmen, anders als bei einem Geheimnis in der Historie. Praktisch aber gewinnt
der Eigenbau, sobald er dasteht, und zwar nicht durch Argumente, sondern durch Trägheit. Das
reicht als Verstärkung, nicht als eigene Begründung — und es gehört hier hingeschrieben,
damit niemand später einen strengeren Grund unterstellt, als tatsächlich vorliegt.

### Warum das kein Zwang zur Suche ist

`uebersprungen` **öffnet das Gate**. Verlangt wird eine Antwort, keine Suche. Ein
Wegwerfskript, bei dem der Nutzer sagt „ich will das selbst schreiben, darum geht es mir
gerade", ist eine vollständige Antwort — sie kostet eine Zeile und bleibt nachlesbar.

## Konsequenzen

- Ein neu geklontes Projekt trifft zwei Sperren statt einer. Beide sind mit je einer Zeile im
  Repository erfüllbar, beide gehören dem Menschen.
- Die Prüfung kann nur die **Antwort** sehen, nicht ihre Ernsthaftigkeit — dieselbe Grenze
  wie beim Projektzuschnitt. Wer `uebersprungen` ohne echten Grund einträgt, betrügt sich
  selbst; sichtbar bleibt es trotzdem.
- Ausnahmen unverändert: Werkzeug, Tests, Beispiele, Dokumentation und der
  Anforderungsbereich bleiben schreibbar. Sonst käme man nicht einmal zum Antworten.

## Revidieren wenn

- Nutzer die zweite Bedingung reflexhaft mit `uebersprungen` abräumen, ohne die Frage gelesen
  zu haben. Dann ist nicht die Sperre falsch, sondern der Text, der sie erklärt.
