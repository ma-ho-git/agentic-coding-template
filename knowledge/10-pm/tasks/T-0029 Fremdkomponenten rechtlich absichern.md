---
id: T-0029
title: Fremdkomponenten rechtlich absichern
type: task
implements: ["[[REQ-0025 Übernommene Fremdkomponenten sind rechtlich geklärt]]"]
status: ready
priority: mittel
agent: claude-code
owner:
created: 2026-08-20
started:
finished:
tags: [topic/meta, topic/requirements]
related: ["[[T-0027 Bestehende Lösungen vor dem Codieren prüfen]]", "[[REQ-0015 Öffentliche Bereitstellung mit geklärten Nutzungsrechten]]"]
---

# T-0029 Fremdkomponenten rechtlich absichern

## Anforderung

[[REQ-0025 Übernommene Fremdkomponenten sind rechtlich geklärt]]

## Ziel

Wer auf fremdem Code aufsetzt, erbt dessen Pflichten. Sie werden geprüft, bevor gebaut wird,
und im Repository erfüllt — nicht nur notiert.

## Akzeptanzkriterien

- [ ] Register `knowledge/05-requirements/fremdkomponenten.md` mit Vorlage: Komponente,
      Version, Lizenz, Pflichten, Quelle mit Abrufdatum
- [ ] Die Lizenzprüfung läuft gegen die Weitergabeabsicht aus der `recht`-Kategorie des
      Rahmens; das Ergebnis steht als ADR fest, bei Unvereinbarkeit mit Ablehnungsgrund
- [ ] Beiliegende Lizenztexte an einem festen Ort, Namensnennung dort, wo sie verlangt wird
- [ ] `tools/check_licenses.py` meldet jede registrierte Komponente ohne Lizenztext im Repo
- [ ] Prüfung läuft in CI; Tests in `tests/tools/`
- [ ] `/solution-scan` verweist beim ausgewählten Kandidaten auf diese Pflichten

## Kontext

- Klassenzuordnung: **CI-Prüfung, keine Schreibsperre.** Der Schaden entsteht bei der
  Weitergabe, nicht beim Schreiben — CI vor dem Merge sitzt am Schadensmoment, eine
  Schreibsperre am falschen Moment
- Abgrenzung zu [[REQ-0015 Öffentliche Bereitstellung mit geklärten Nutzungsrechten]]:
  dort die eigene Lizenz, hier die geerbten Pflichten

## Agent

`claude-code` — Prüfwerkzeug, CI, Vorlage. Lizenzrecherche über `researcher`.

## Abhängigkeiten

- [[T-0027 Bestehende Lösungen vor dem Codieren prüfen]]

## Notizen

- Das Werkzeug prüft Vollständigkeit, nicht Rechtmäßigkeit. Ob eine Lizenz zum Vorhaben
  passt, entscheidet der Mensch — das Werkzeug stellt nur sicher, dass niemand die Frage
  überspringt. Die Grenze gehört in die Dokumentation, sonst entsteht ein falsches
  Sicherheitsgefühl.
