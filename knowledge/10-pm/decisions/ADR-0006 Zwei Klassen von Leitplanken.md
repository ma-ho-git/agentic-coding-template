---
title: ADR-0006 Zwei Klassen von Leitplanken
type: decision
tags: [topic/agents, topic/meta]
status: active
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-02-20
related: ["[[ADR-0002 Prüfbare Vorgaben in Hooks statt in Prosa]]", "[[Spec-Driven-Development - was andere Projekte machen]]", "[[T-0019 Leitplanken benennen und klassifizieren]]"]
---

# ADR-0006 Zwei Klassen von Leitplanken

## Status

angenommen

## Kontext

- Zielbild: ein Software-Engineering-Ansatz mit KI-Agenten, der auch für unerfahrene
  Anwender tragfähig ist — Vorteile der Agenten nutzen, Nachteile durch Leitplanken begrenzen.
- Vorgabe des Auftraggebers: es muss **mindestens zwei Arten** von Leitplanken geben —
  **starre** für kritische Entscheidungen, **flexible** für Optimierungsentscheidungen.
- [[ADR-0002 Prüfbare Vorgaben in Hooks statt in Prosa]] trifft diese Unterscheidung bereits
  faktisch, benennt sie aber nicht als Konzept. Wer eine neue Regel hinzufügt, hat keinen
  Maßstab, in welche Klasse sie gehört.
- Die Marktumschau ([[Spec-Driven-Development - was andere Projekte machen]]) zeigt: die
  großen Projekte (Spec Kit, BMAD) führen ihre „Constitution" als reine Prosa. Die
  Guardrails-Literatur nennt das die schwächste Schicht, weil sie umgehbar ist.
- **Befund bei der Prüfung des eigenen Codes:** die Zuordnung war verkehrt herum. Ein
  fehlender `@contract`-Kommentar blockiert den Schreibvorgang — „Code schreiben, obwohl gar
  keine Anforderung vereinbart ist" blockiert **nichts**. `baseline_status` kam an sechs
  Stellen vor, fünf davon in Skills (Prosa) und eine in einem Hook, der nur *berichtet*.
  Die wichtigste kritische Entscheidung war die weichste Leitplanke.

## Optionen

| Option | Vorteil | Nachteil |
| --- | --- | --- |
| Alles blockieren | maximale Verbindlichkeit | Rauschen, Abbruch; Optimierungsfragen haben selten eine richtige Antwort |
| Alles nur empfehlen | keine Reibung | genau der Zustand, den die Vorgabe beheben soll |
| **Zwei benannte Klassen mit Zuordnungstest** | kritische Entscheidungen halten, weiche bleiben verhandelbar | jede neue Regel braucht eine Einordnung |

## Entscheidung

Zwei Klassen, benannt und für den Nutzer sichtbar.

### Starre Leitplanke

Für Entscheidungen, deren Verletzung **nicht durch späteres Nachbessern heilbar** ist oder
die das Projekt, sein Umfeld oder die Nachvollziehbarkeit grundsätzlich beschädigt.

- Wird **maschinell durchgesetzt** — Exit-Code 2 oder `permissionDecision: deny`.
- **Eine starre Leitplanke, die nicht maschinell durchgesetzt wird, ist keine.** Steht sie
  nur in Prosa, ist sie eine flexible.
- Der Agent kann sie nicht überstimmen. Der Mensch ändert sie, indem er die Regel ändert.

Heute: Geheimnisse im Repo, fehlender Contract-Block, zerstörerische Git-Kommandos, Aufgabe
ohne Anforderungsbezug — und **neu** das Startgate vor Produktivcode.

### Flexible Leitplanke

Für **Optimierungsentscheidungen**: Es gibt eine bessere und eine schlechtere Antwort, aber
der Einzelfall kann die schlechtere rechtfertigen.

- Erzeugt einen Hinweis, blockiert nicht.
- Wer sie überschreitet, **begründet das im Code** — die Abweichung wird sichtbar, nicht
  verboten.

Heute: Funktionsgröße, Parameterzahl, Namenslänge, Verschachtelungstiefe, Dateilänge,
veraltetes Contract-Datum.

### Zuordnungstest

Eine Regel ist **starr**, wenn mindestens eines zutrifft:

1. Die Verletzung ist nicht rückgängig zu machen (Geheimnis in der Historie).
2. Sie gefährdet Projekt, Umfeld oder Daten (zerstörerische Kommandos).
3. Sie zerstört die Nachvollziehbarkeit dauerhaft (Arbeit ohne Anforderung, ohne Contract).
4. Sie umgeht eine Entscheidung, die dem Menschen vorbehalten ist (Startgate).

Sonst ist sie **flexibel**. Im Zweifel flexibel: eine falsch gesetzte starre Leitplanke
kostet mehr Vertrauen, als eine falsch gesetzte flexible kostet.

### Sichtbarkeit

Jede Meldung nennt ihre Klasse. Der Nutzer muss erkennen können, ob er gerade an einer
Wand steht oder an einem Hinweis — sonst behandelt er beides gleich, und das heißt:
irgendwann beides als Rauschen.

## Konsequenzen

- Das Startgate wird durch einen `PreToolUse`-Hook durchgesetzt: keine Schreibzugriffe auf
  Produktivcode, solange `baseline_status: entwurf`. Werkzeug, Konfiguration, Dokumentation,
  Tests und der Anforderungsbereich selbst bleiben frei — sonst käme man nicht einmal zum
  Erheben.
- Jede bestehende Prüfung bekommt ihre Klasse zugewiesen und in der Meldung ausgewiesen.
- Neue Regeln müssen den Zuordnungstest durchlaufen; das Ergebnis gehört in die Regeldatei.
- Mehr Reibung beim Projektstart. Bewusst in Kauf genommen — das ist der Punkt.

## Revidieren wenn

- Die Gate-Sperre in der Praxis zu Abbrüchen führt, statt zur Anforderungserhebung.
  Dann braucht es einen ausdrücklichen Spike-Modus mit Verfallsdatum.
- Sich zeigt, dass Nutzer flexible Leitplanken pauschal ignorieren — dann ist nicht die
  Klasse falsch, sondern der Schwellwert.
