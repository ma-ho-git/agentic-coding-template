---
id: T-0038
title: Übergabe von der Vorlage zum Projekt
type: task
implements: ["[[REQ-0026 Anpassbarkeit ohne Umschreiben der Regeln]]"]
status: doing
priority: hoch
agent: claude-code
owner: claude-code
created: 2026-08-20
started: 2026-08-20
finished:
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

- [ ] `tools/handover.py` mit zwei Modi: `--check` (Vorgabe, ändert nichts, meldet jeden
      Rückstand) und `--apply` (führt die Übergabe aus). Die sichere Vorgabe ist die
      prüfende — ein versehentlicher Lauf darf die Vorlage nicht ausräumen.
- [ ] `--apply` setzt `baseline_status` auf `entwurf` und `scan_status` auf `offen`
- [ ] `--apply` **archiviert statt löscht**: Anforderungen, Aufgaben, ADRs, Fortschrittslog
      und Szenario wandern nach `knowledge/90-meta/beispiel/`. Wikilinks lösen in Obsidian
      über den Namen auf, bleiben also intakt, solange die Gruppe zusammen umzieht.
- [ ] Bleiben im Klon: `20-knowledge/` und `30-troubleshooting/` — die beschreiben das
      Werkzeug, das der Klon weiterbenutzt, nicht die Geschichte dieses Projekts
- [ ] `--apply` leert die Board-Lanes, behält das Kanban-Frontmatter
- [ ] `--check` meldet zusätzlich verbliebene Platzhalter (nutzt `check_placeholders`)
- [ ] `/bootstrap` ruft `--apply` **vor** der Erhebung auf, nicht danach, und `--check` als
      letzten Schritt vor der Orientierung
- [ ] In diesem Repository meldet `--check` erwartungsgemäß rot — hier *ist* die Vorlage.
      Wie bei `check_placeholders.py`: eine Prüfung, deren korrektes Ergebnis „rot" ist,
      läuft nicht in CI
- [ ] Tests für beide Modi

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
