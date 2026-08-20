---
title: ADR-0007 Projektzuschnitt skaliert nur die Dokumentation
type: decision
tags: [topic/meta, topic/requirements]
status: active
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-02-20
related: ["[[ADR-0006 Zwei Klassen von Leitplanken]]", "[[ADR-0005 Anforderungen als Pflicht vor dem Code]]", "[[Rahmen und Startgate]]", "[[T-0022 Projektzuschnitt bestimmt die Zeremonie]]"]
---

# ADR-0007 Projektzuschnitt skaliert nur die Dokumentation

## Status

angenommen

## Kontext

- Das Template verlangt in jedem Projekt dasselbe: sechs Anforderungskategorien, Vision,
  Stakeholder, Glossar, ADRs, Fortschrittslog, Contract-Kommentare, TDD.
- Für ein gepflegtes Produkt ist das angemessen. Für ein Wegwerfskript von 80 Zeilen ist es
  ein Vielfaches des eigentlichen Aufwands.
- Der reale Ausgang eines solchen Missverhältnisses ist nicht sorgfältige Arbeit, sondern
  Umgehung: Der Nutzer schreibt Platzhalter in die Pflichtfelder, und danach ist die
  Rückverfolgbarkeit nur noch formal vorhanden. Genau dieses Risiko steht in [[Risiken]]
  („Regeln werden formal erfüllt, aber sinnentleert").
- Ein Zuschnitt ist also nötig. Die Gefahr dabei liegt auf der Hand: Er kann zum Schlupfloch
  werden — „ist doch nur ein kleines Skript" ist genau das Argument, unter dem ein Geheimnis
  in die Historie gerät.

## Optionen

| Option | Vorteil | Nachteil |
| --- | --- | --- |
| Kein Zuschnitt, eine Zeremonie für alle | einfach, keine Schlupflöcher | erzeugt Platzhalter-Erfüllung bei kleinen Projekten |
| Zuschnitt schaltet auch Prüfungen ab | maximale Erleichterung | hebt die Klasse der starren Leitplanken auf; unheilbare Verstöße würden möglich |
| **Zuschnitt skaliert nur Dokumentationspflicht und Erhebungstiefe** | kleine Projekte werden benutzbar, die kritischen Grenzen bleiben | zwei Begriffe mehr, die erklärt werden müssen |

## Entscheidung

Drei Zuschnitte — `skript`, `werkzeug`, `produkt` — als `project_scope` in
`.claude/hooks/config.json`. Sie skalieren **ausschließlich**:

- wie ausführlich Anforderungen erhoben werden (nicht: welche Kategorien gefragt werden),
- wie viel Dokumentation entsteht — Vision, Glossar, ADR-Pflicht, Fortschrittsdetails.

Sie skalieren **nicht**: die Anforderungen selbst, das Startgate, TDD, und keine einzige
starre Leitplanke. Alle acht Prüfungen aus [[ADR-0006 Zwei Klassen von Leitplanken]]
verhalten sich in jedem Zuschnitt identisch.

### Warum die Konfigurationsdatei

`config.json` ist die einzige Stelle, die Hooks und Skills gleichermaßen lesen — ein Wert im
Vault wäre für die Hooks nicht erreichbar, ohne Markdown zu parsen.

### Warum die Begründung trotzdem in den Vault gehört

Ein nackter Konfigurationswert sagt *was*, nicht *warum*. Ohne die Begründung kann der
nächste Agent nicht unterscheiden, ob der Zuschnitt überlegt gewählt oder durchgereicht
wurde — und ein unbegründeter Zuschnitt ist eine Ausrede, keine Entscheidung. Deshalb steht
sie im Abschnitt „Projektzuschnitt" von [[Rahmen und Startgate]], neben dem Startgate, das
ebenfalls dem Menschen vorbehalten ist. Bei einer Änderung kommt die neue Begründung dazu,
die alte bleibt stehen.

### Warum der Rückfall `produkt` heißt

Ein fehlender oder unbekannter Wert bedeutet **mehr** Zeremonie, nicht weniger. Das ist
dieselbe Regel wie beim Startgate: fail closed (`.claude/rules/security.md`). Ein Tippfehler
darf keine Erleichterung erkaufen.

## Konsequenzen

- `/bootstrap` fragt den Zuschnitt in Schritt 2a und schreibt beides — Wert und Begründung.
- `/req-elicit` liest den Wert und passt die Tiefe an, nicht die Fragenliste.
- Der SessionStart-Hook nennt den Zuschnitt in jeder Sitzung samt dem Satz, dass starre
  Leitplanken davon unberührt bleiben. Ein stiller Konfigurationswert wäre genau das
  Schlupfloch, das diese Entscheidung vermeiden will.
- Dieses Repository steht auf `produkt` — es wird öffentlich geklont und ist zugleich sein
  eigenes Vorbild.

## Revidieren wenn

- Sich zeigt, dass `skript` in der Praxis trotzdem zu schwer ist. Dann fehlt ein vierter,
  noch kleinerer Zuschnitt — nicht eine Aufweichung der Prüfungen.
- Nutzer den Zuschnitt als Schalter für Prüfungen missverstehen. Dann ist die Erklärung im
  Bootstrap zu schwach, nicht die Trennung falsch.
