---
id: T-0032
title: Artefakttyp bestimmt die Beispiele
type: task
implements: ["[[REQ-0020 Für unerfahrene Anwender nutzbar]]"]
status: done
priority: mittel
agent: claude-code
owner: claude-code
created: 2026-08-20
started: 2026-08-20
finished: 2026-08-20
tags: [topic/requirements, topic/meta]
related: ["[[T-0031 Qualitätsmerkmale vollständig abfragen]]", "[[REQ-0017 Anforderungserhebung vor der Entwicklung]]", "[[Qualitätsmerkmale je Artefakttyp]]"]
---

# T-0032 Artefakttyp bestimmt die Beispiele

## Anforderung

[[REQ-0020 Für unerfahrene Anwender nutzbar]] — Präzisierung vom 2026-08-20.

## Ziel

`/req-elicit` fragt als Erstes nach dem Artefakttyp — und benutzt danach für alle
dieselbe Beispielspalte „Kommandozeilenwerkzeug". Ein Anfänger kann ein CLI-Beispiel
nicht auf seinen Dienst übertragen; genau das ist ja seine Lücke.

## Akzeptanzkriterien

- [x] Wissensnotiz mit einem Profil je Artefakttyp: Bibliothek, Kommandozeilenwerkzeug,
      Dienst/API, Datenstrecke, Anwendung mit Oberfläche, Wegwerfskript
- [x] Je Profil: die drei bis fünf Qualitätsmerkmale, die dort tatsächlich entscheiden,
      je mit einer messbaren Beispielanforderung
- [x] `/req-elicit` wählt seine Beispiele nach dem genannten Artefakttyp
- [x] **Die Fragenliste bleibt in jedem Fall gleich** — artefaktabhängig sind Beispiele,
      Messgrößen und die Tiefe, nie der Umfang der Prüfung
- [x] Unbekannter oder gemischter Typ: alle Profile anbieten statt raten

## Ergebnis

- Wissensnotiz [[Qualitätsmerkmale je Artefakttyp]] mit sechs Profilen: Bibliothek,
  Kommandozeilenwerkzeug, Dienst/API, Datenstrecke, Anwendung mit Oberfläche, Wegwerfskript.
  Je Merkmal eine **messbare** Beispielanforderung, keine Schlagworte.
- `/req-elicit` schlägt die Profildatei nach, sobald der Artefakttyp genannt ist, und nimmt
  seine Beispiele von dort statt aus der CLI-Spalte. Die Spaltenüberschrift sagt das jetzt
  auch — vorher war sie stillschweigend für alle zuständig.
- **Warum das Nachschlagen der eigentliche Punkt ist:** Ein Anfänger kann ein CLI-Beispiel
  nicht auf seinen Dienst übertragen. Genau diese Übertragung ist das Wissen, das ihm fehlt —
  sie ihm abzuverlangen, macht den Artefakttyp zur Zierfrage.
- Gemischter oder unklarer Typ: **beide Profile anbieten, nicht raten.** Ein Werkzeug mit
  Weboberfläche ist beides.
- Grenze wie überall: Das Profil ändert **Beispiele, Messgrößen und erwartete Tiefe. Nie die
  Fragenliste.** Steht in der Notiz und im Skill.
- Der Sweep weiß jetzt auch, **wo er hartnäckig sein muss**: bei einer Bibliothek auf
  Kompatibilität, bei einer Datenstrecke auf Wiederholbarkeit, bei einem CLI darauf, wie es
  sich in einer Pipe verhält.

### Abweichung von einem eigenen Akzeptanzkriterium

Das Kriterium verlangt „drei bis fünf Merkmale je Profil". Das **Wegwerfskript-Profil hat
zwei** — Zuverlässigkeit und, falls echte Daten im Spiel sind, Sicherheit. Das ist Absicht:
Für ein Skript, das einmal läuft und dann gelöscht wird, ist die ehrliche Antwort, dass fast
nichts zutrifft. Drei weitere zu erfinden, um eine selbst gesetzte Zahl zu treffen, wäre genau
die Platzhalter-Erfüllung, gegen die dieses Template gebaut ist. Kriterium als erfüllt
gewertet, Abweichung hier benannt statt kaschiert.

### Belastbarkeit

Handwerkswissen, keine Norm — so steht es auch in der Notiz. Nur die Versionierungsregel für
Bibliotheken hat eine zitierbare Quelle (SemVer 2.0.0), und selbst deren Seite war wegen des
Egress-Proxys nicht abrufbar. Die Profile sind eine Vorauswahl zum Widersprechen, kein Katalog
zum Abhaken.

Suite 106 grün (unverändert — Notiz und Skill), `check_vault.py` und
`check_traceability.py` ohne Befund.

## Kontext

- ISO 25010 ist ausdrücklich zum Zuschneiden gedacht; welche Merkmale zählen, hängt vom
  System ab
- Gleiche Bauform wie der Projektzuschnitt: die Prüfung skaliert nie, nur die Antwort

## Agent

`claude-code` für den Einbau. Die Recherche je Artefakttyp gehört zu `researcher` oder
Cowork — in dieser Sitzung blockierte der Egress-Proxy jeden Seitenabruf.

## Abhängigkeiten

- [[T-0031 Qualitätsmerkmale vollständig abfragen]]

## Notizen

- Die Profile sind eine Vorauswahl, kein Gesetz. Sie sollen dem Nutzer das Übertragen
  abnehmen, nicht ihm vorschreiben, was ihm wichtig zu sein hat.
