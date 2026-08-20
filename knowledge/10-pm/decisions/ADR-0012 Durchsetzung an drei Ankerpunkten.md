---
title: ADR-0012 Durchsetzung an drei Ankerpunkten
type: decision
tags: [topic/agents, topic/meta]
status: active
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-02-20
related: ["[[ADR-0006 Zwei Klassen von Leitplanken]]", "[[ADR-0002 Prüfbare Vorgaben in Hooks statt in Prosa]]", "[[Durchsetzungsschicht - Ankerpunkte und bekannte Umgehungen]]", "[[T-0035 Durchsetzung am Commit]]"]
---

# ADR-0012 Durchsetzung an drei Ankerpunkten

## Status

angenommen

## Kontext

- Grundsatzprüfung vor dem Startgate (2026-08-20): Alle fünf Schreibprüfungen hängen am
  Write|Edit-Matcher der Hook-Schicht. Über Bash geschriebene Dateien passieren ungeprüft —
  und der Betriebsmodus der Cloud-Umgebung leitet Dateiarbeit ausdrücklich über Bash.
  **Beweis war die Sitzung selbst:** Kein PostToolUse-Hook lief auf den Schreibvorgängen des
  Tages; die Regeln hielten nur, weil die Werkzeuge von Hand liefen. Das ist Prosa-Niveau —
  die Schicht, die dieses Projekt selbst als die schwächste bezeichnet.
- Dazu: CI triggerte nur auf Pull Requests nach main (Solo- und Lokalarbeit ohne jeden
  Rückhalt), niemand prüfte, ob die Hooks überhaupt feuern, und die Hooks versagen offen.
- Externe Belege: Hook-Matcher decken nur das jeweilige Tool ab; permissions.deny schützt
  die Hook-Dateien selbst nachweislich unzuverlässig; als Standard-Gegenmittel dokumentiert
  ist der Git-Hook am Commit mit CI als Rückhalt, als Standard-Umgehung der
  Überspring-Schalter. Quellen in der verlinkten Wissensnotiz.

## Optionen

| Option | Vorteil | Nachteil |
| --- | --- | --- |
| Bash-Kommandos je Aufruf analysieren und Schreibziele erraten | bliebe in der Hook-Schicht | Schreibziele aus beliebigen Kommandos zu erraten ist prinzipiell unzuverlässig; jedes Kommando würde teurer; falsche Sicherheit |
| Nur CI prüfen | ein Ort, einfach | erreicht genau die Zielgruppe nicht, die lokal ohne Pushes arbeitet; Rückmeldung erst Minuten später |
| **Drei Ankerpunkte: Tool-Aufruf, Commit, CI — plus Scharfschaltungs-Nachweis** | jeder Schreibweg passiert mindestens einen Anker; Rückmeldung so früh wie möglich, Rückhalt so spät wie nötig | drei Stellen zu pflegen; lokale Umgehung durch den Menschen bleibt möglich |

## Entscheidung

Drei Ankerpunkte, ein Regelwerk:

1. **Tool-Aufruf** — die bestehenden Hooks; früheste Rückmeldung, deckt Write/Edit.
2. **Commit** — pre-commit-Hook führt `tools/check_all.py --staged` aus; der eine Engpass,
   den jeder Schreibweg passiert. Installiert von `/bootstrap`; git_guard verweigert dem
   Agenten den Überspring-Schalter und das Umbiegen des Hook-Pfads.
3. **CI** — jeder Push führt dasselbe `check_all` über den gepushten Bereich aus; niemand
   kann CI einen Überspring-Schalter mitgeben. Änderungen an Enforcement-Dateien werden laut
   ausgewiesen.

Dazu der **Nachweis statt der Annahme**: `tools/check_armed.py` feuert jede Leitplanke mit
einem Kanarienvogel und erwartet die Ablehnung; `/bootstrap` führt das aus und protokolliert
es im Umgebungs-Manifest.

**Ein Regelwerk an allen drei Punkten.** Commit und CI rufen exakt dieselben Hook-Skripte
über `check_all` auf. Zwei Regelwerke wären auseinandergelaufen, und der Streitfall „lokal
grün, CI rot" wäre eingebaut gewesen.

### Ehrlichkeit als Bestandteil der Entscheidung

Die bekannten Umgehungen stehen in `.claude/rules/guardrails.md`, nicht im Vagen: Der Agent
kann Enforcement-Dateien editieren (sichtbar im Diff und in der CI-Warnung, lokal nicht
verhinderbar); ein Mensch kann den Commit-Hook von Hand entfernen (sein gutes Recht — der
Mensch überstimmt Regeln, der Agent nicht); ein fehlender Interpreter lässt die
Tool-Aufruf-Schicht offen versagen (dafür der Scharfschaltungs-Nachweis). Garantiert ist
nicht perfekte Verhinderung, sondern dass ein Verstoß nicht **leise weit kommt**.

## Konsequenzen

- `check_task` rückte in die blockenden CI-Prüfungen auf; das Startgate wirkt erstmals auch
  außerhalb des Write-Wegs.
- Jeder Commit kostet die Prüfzeit über den Staged-Satz (Sekunden). Bewusst in Kauf
  genommen — das ist der Preis des Engpasses.
- Der Engpass fand am ersten Tag zwei echte Befunde (`cowork/build-skills.sh`), der
  Scharfschaltungs-Nachweis beim ersten Lauf einen falsch gebauten Kanarienvogel. Beide
  Werkzeuge haben sich vor ihrer Fertigstellung bezahlt gemacht.

## Revidieren wenn

- Claude Code einen verlässlichen Mechanismus bekommt, Bash-Schreibziele je Aufruf zu
  prüfen — dann kann der Tool-Aufruf-Anker breiter werden und der Commit-Anker bleibt als
  Netz.
- Die Commit-Prüfzeit bei großen Staged-Sätzen zur echten Bremse wird — dann zuerst die
  Prüfungen beschleunigen, nicht den Anker aufgeben.
