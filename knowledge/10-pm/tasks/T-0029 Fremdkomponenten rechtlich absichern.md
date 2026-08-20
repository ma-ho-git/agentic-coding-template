---
id: T-0029
title: Fremdkomponenten rechtlich absichern
type: task
implements: ["[[REQ-0025 Übernommene Fremdkomponenten sind rechtlich geklärt]]"]
status: done
priority: mittel
agent: claude-code
owner: claude-code
created: 2026-08-20
started: 2026-08-20
finished: 2026-08-20
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

- [x] Register `knowledge/05-requirements/fremdkomponenten.md` mit Vorlage: Komponente,
      Version, Lizenz, Pflichten, Quelle mit Abrufdatum
- [x] Die Lizenzprüfung läuft gegen die Weitergabeabsicht aus der `recht`-Kategorie des
      Rahmens; das Ergebnis steht als ADR fest, bei Unvereinbarkeit mit Ablehnungsgrund
- [x] Beiliegende Lizenztexte an einem festen Ort, Namensnennung dort, wo sie verlangt wird
- [x] `tools/check_licenses.py` meldet jede registrierte Komponente ohne Lizenztext im Repo
- [x] Prüfung läuft in CI; Tests in `tests/tools/`
- [x] `/solution-scan` verweist beim ausgewählten Kandidaten auf diese Pflichten

## Ergebnis

- Register `knowledge/05-requirements/fremdkomponenten.md`: Ablauf vor jeder Übernahme,
  Lizenzfamilien-Tabelle als Orientierung, und die Tabelle selbst — **leer**, weil das
  Template keinen Fremdcode übernimmt. Ein leeres Register ist ein gültiger Zustand.
- Der Ablauf beginnt bei der **eigenen** Weitergabeabsicht aus der `recht`-Kategorie, nicht
  bei der fremden Lizenz. Ohne zu wissen, was man selbst vorhat, lässt sich Verträglichkeit
  nicht beurteilen.
- **Zwei Punkte, die in der Praxis Geld kosten**, stehen ausdrücklich drin: die Lizenzdatei
  im Repository der Komponente lesen, nicht das Etikett auf der Paketseite — die beiden
  weichen häufiger ab als gedacht. Und: **keine genannte Lizenz heißt keine eingeräumten
  Rechte**, egal wie öffentlich der Code liegt.
- `tools/check_licenses.py` prüft Vollständigkeit: Eintrag vollständig, Lizenztext in
  `licenses/` vorhanden, Quelle mit Abrufdatum. Warnt zusätzlich bei einem Lizenztext, den
  kein Eintrag referenziert.
- **Grenze ausgeschrieben:** Das Werkzeug prüft Vollständigkeit, **nicht Rechtmäßigkeit**.
  Wer daraus ein Gefühl von Rechtssicherheit ableitet, hat es missverstanden — das steht so
  im Register und im README.
- Einordnung als **CI-Prüfung**, nicht als Schreibsperre, jetzt auch in `guardrails.md`
  begründet: Der Schaden entsteht bei der Weitergabe; ein Schreib-Hook würde den falschen
  Moment blockieren — man bekäme eine Quelldatei verweigert wegen einer Komponente, mit der
  sie nichts zu tun hat.
- `/solution-scan` verweist beim ausgewählten Kandidaten auf den Ablauf.

Elf Tests. **Zwei echte Funde beim ersten Lauf gegen die Wirklichkeit:** Das eigene
`licenses/README.md` löste die Waisen-Warnung aus (Fehlalarm, mit Reproduktionstest behoben),
und der Register-Eintrag fehlte im Index. Suite 106 grün.

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
