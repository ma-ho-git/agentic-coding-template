---
id: T-0038
title: Übergabe von der Vorlage zum Projekt
type: task
implements: ["[[REQ-0026 Anpassbarkeit ohne Umschreiben der Regeln]]"]
status: done
priority: hoch
agent: claude-code
owner: claude-code
created: 2026-08-20
started: 2026-08-20
finished: 2026-08-20
tags: [topic/meta, topic/requirements]
related: ["[[T-0034 Erstlauf im frischen Klon durchspielen]]", "[[REQ-0017 Anforderungserhebung vor der Entwicklung]]", "[[ADR-0012 Durchsetzung an drei Ankerpunkten]]"]
---

# T-0038 Übergabe von der Vorlage zum Projekt

## Anforderung

[[REQ-0026 Anpassbarkeit ohne Umschreiben der Regeln]] — der vierte Abnahmepunkt, „keine
Rückstände nach `/bootstrap`", in seiner scharfen Lesart. Betrifft zugleich
[[REQ-0017 Anforderungserhebung vor der Entwicklung]]: Ohne diese Reparatur überspringt ein
Klon die Rahmenerhebung.

## Ziel

Der Zustand der Vorlage wird mitgeklont. Solange `baseline_status: vereinbart` und
`scan_status: gesucht` ausgeliefert werden, startet **jedes** neue Projekt mit offenem
Startgate — und `/req-elicit` geht in den Stufenmodus, statt den Rahmen zu erheben. Die
einzige Absicherung ist heute ein Satz Prosa in `baseline.md`; `/bootstrap` setzt nichts
zurück.

## Akzeptanzkriterien

- [x] `tools/handover.py` mit zwei Modi: `--check` (Vorgabe, ändert nichts, meldet jeden
      Rückstand) und `--apply` (führt die Übergabe aus). Die sichere Vorgabe ist die
      prüfende — ein versehentlicher Lauf darf die Vorlage nicht ausräumen.
- [x] `--apply` setzt `baseline_status` auf `entwurf` und `scan_status` auf `offen`
- [x] `--apply` **archiviert statt löscht**: Anforderungen, Aufgaben, ADRs, Fortschrittslog
      und Szenario wandern nach `knowledge/90-meta/beispiel/`. Wikilinks lösen in Obsidian
      über den Namen auf, bleiben also intakt, solange die Gruppe zusammen umzieht.
- [x] Bleiben im Klon: `20-knowledge/` und `30-troubleshooting/` — die beschreiben das
      Werkzeug, das der Klon weiterbenutzt, nicht die Geschichte dieses Projekts
- [x] `--apply` leert die Board-Lanes, behält das Kanban-Frontmatter
- [x] `--check` meldet zusätzlich verbliebene Platzhalter (nutzt `check_placeholders`)
- [x] `/bootstrap` ruft `--apply` **vor** der Erhebung auf, nicht danach, und `--check` als
      letzten Schritt vor der Orientierung
- [x] In diesem Repository meldet `--check` erwartungsgemäß rot — hier *ist* die Vorlage.
      Wie bei `check_placeholders.py`: eine Prüfung, deren korrektes Ergebnis „rot" ist,
      läuft nicht in CI
- [x] Tests für beide Modi

## Ergebnis

- `tools/handover.py` mit `--check` als **sicherer Vorgabe** und `--apply` für die Übergabe.
  Setzt beide Gate-Marker zurück, leert das Board, archiviert 78 Dokumente nach
  `knowledge/90-meta/beispiel/` und legt dort eine README an, die aus dem Index verlinkt ist
  — archiviert, nicht gelöscht, und **auffindbar**, sonst wäre die Entscheidung folgenlos.
- Geblieben sind `20-knowledge/` und `30-troubleshooting/`: Sie beschreiben das Werkzeug,
  das der Klon weiterbenutzt, nicht die Geschichte dieses Projekts.
- `/bootstrap` ruft die Übergabe als **Schritt 2a** auf — vor der Erhebung. Beim Verdrahten
  fiel auf, dass die Schrittnummern nicht der Laufreihenfolge entsprachen und die
  Restprüfung **nach** der Orientierung stand, obwohl sie davor gehört. Beides umgestellt:
  2 → 2a Übergabe → 2b Zuschnitt → 3 Erhebung → 3a Restprüfung → 4 Orientierung.

### Am echten Klon nachgewiesen, nicht am Testdoppel

Vier Durchläufe mit `git clone`. Der erste lief ins Leere, weil das Werkzeug noch nicht
committet war — danach mit echtem Inhalt. Ergebnis des vollständigen Ablaufs:

| Schritt | Ergebnis |
| --- | --- |
| Klon vor der Übergabe | `scan_status: gesucht` — die zweite Gate-Bedingung war vorbeantwortet |
| `--apply` | 78 Dokumente archiviert, beide Marker zurückgesetzt |
| `install_hooks.py` | Engpass installiert |
| `check_armed.py` | sieben von sieben ARMED |
| `check_vault`, `check_traceability`, `check_licenses` | je 0 Fehler, 0 Warnungen |
| Probe-Commit mit Produktivcode | **vom Gate verweigert** — der eigentliche Beweis |

### Drei Funde, die nur der echte Klon liefern konnte

1. **Archivierte Dateien meldeten sich ewig als Platzhalter.** Drei der 78 tragen den
   Platzhalter-Marker; die Übergabe wäre nie „vollständig" geworden. `check_placeholders`
   überspringt den Archivpfad jetzt — mit Test.
2. **Das geleerte Board galt als Waise.** Ein frisches Projekt hätte mit einer Warnung
   begonnen. Das Board ist plugin-eigen und trägt Karten, keine Prosa-Links; leer ist sein
   normaler Startzustand. Ausnahme ergänzt — mit Test.
3. **Git-Hooks werden nicht mitgeklont.** `check_armed` meldete im frischen Klon sechs von
   sieben — der Commit-Anker fehlte. Das ist **korrektes Verhalten**, kein Defekt: `.git/hooks/`
   gehört nicht zum Repository-Inhalt. Genau deshalb installiert `/bootstrap` ihn und prüft
   **danach**. In `guardrails.md` und der Wissensnotiz festgehalten.

Eine Selbstkorrektur: Ein Idempotenz-Test schlug fehl, weil meine Zusicherung „Beispielarchiv"
zählte — das Wort steht pro Einfügung zweimal drin (Überschrift und Link). Die Probe war
falsch, nicht die Implementierung; geschärft auf die Linkzeile selbst.

13 neue Tests, Suite 147 grün.

## Kontext

- Befund vom 2026-08-20, aufgefallen erst bei der Frage, ob das Gate oder T-0034 zuerst
  kommt: Das Gate zu öffnen heißt bei einer Vorlage, einen Defekt auszuliefern
- Vierter Fall desselben Musters — starre Leitplanke, von Prosa gehalten (nach T-0020,
  T-0028, T-0035)
- Entscheidung des Auftraggebers: archivieren statt löschen, damit das ausgefüllte Beispiel
  einem Anfänger erhalten bleibt ([[REQ-0020 Für unerfahrene Anwender nutzbar]])

## Agent

`claude-code` — Werkzeug, Tests, Bootstrap-Verdrahtung.

## Abhängigkeiten

- keine

## Notizen

- `--apply` in diesem Repository auszuführen wäre ein Datenverlust-Unfall. Deshalb ist die
  Vorgabe `--check`, und `--apply` verlangt den Schalter ausdrücklich.
- Nach dem Umzug dürfen `check_vault.py` und `check_traceability.py` nicht rot werden: Die
  Rückverfolgbarkeitsprüfung sucht in `05-requirements` und `10-pm/tasks` — nach dem Umzug
  ist dort nichts mehr, also auch kein Widerspruch. Im Testfall nachweisen, nicht annehmen.
