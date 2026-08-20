---
id: T-0037
title: Scharfschaltung nachweisen
type: task
implements: ["[[REQ-0011 Prüfbare Vorgaben werden durchgesetzt, nicht empfohlen]]"]
status: done
priority: hoch
agent: claude-code
owner: claude-code
created: 2026-08-20
started: 2026-08-20
finished: 2026-08-20
tags: [topic/agents, topic/meta]
related: ["[[T-0035 Durchsetzung am Commit]]", "[[T-0036 CI als echter Rückhalt]]", "[[ADR-0006 Zwei Klassen von Leitplanken]]"]
---

# T-0037 Scharfschaltung nachweisen

## Anforderung

[[REQ-0011 Prüfbare Vorgaben werden durchgesetzt, nicht empfohlen]] — Befund F3: Nichts
prüft, ob die Leitplanken überhaupt feuern. Die Hooks versagen offen (Skript crasht,
`python3` fehlt → Schreibvorgang läuft durch), und der Agent kann die Hook-Dateien selbst
editieren, ohne dass es auffällt.

## Ziel

„Scharf" ist ein geprüfter Zustand, keine Annahme — und die bekannten Umgehungen stehen
schwarz auf weiß in der Leitplanken-Regel, statt verschwiegen zu werden.

## Akzeptanzkriterien

- [x] `tools/check_armed.py` feuert jeden Hook mit einem Kanarienvogel-Ereignis und erwartet
      die Ablehnung: git_guard verweigert ein zerstörerisches Kommando, das Gate verweigert
      Produktivcode bei geschlossenem Rahmen, Geheimnis-, Contract- und Task-Prüfung blocken
      ihre Negativfälle, die Qualitätsprüfung meldet ihren Hinweis
- [x] Zusätzlich geprüft: pre-commit-Hook installiert und von uns
- [x] Kanarien-Literale werden zur Laufzeit zusammengesetzt (Gebrauch-vs.-Erwähnung)
- [x] `/bootstrap` führt den Selbsttest aus und trägt das Ergebnis ins Umgebungs-Manifest
- [x] `guardrails.md` bekommt den Abschnitt **„Drei Ankerpunkte, und was sie nicht halten"**:
      die Abdeckungstabelle (Tool-Aufruf / Commit / CI) und die bekannten Umgehungen —
      Hook-Datei editieren, Hook-Verzeichnis löschen, Ausfall bei fehlendem Python. Ehrlich:
      lokal ist Verhinderung best effort, garantiert ist Sichtbarkeit im Diff und in CI
- [x] ADR hält die Entscheidung fest: Durchsetzung an drei Ankerpunkten, samt verworfener
      Alternativen (Bash-Kommando-Analyse je Schreibvorgang, nur CI)
- [x] Wissensnotiz mit der Recherche vom 2026-08-20 und allen Quellen

## Ergebnis

- `tools/check_armed.py`: sieben Kanarienvögel, sieben Ablehnungen erwartet — Gate,
  Geheimnisse, Contract, Task, Qualität, git_guard und der installierte pre-commit-Engpass.
  Ein crashender Hook zählt als FAILED, nie als scharf. Live-Lauf: sieben von sieben ARMED.
- **Der Selbsttest fand beim allerersten Lauf einen Fehler — meinen:** Der
  Geheimnis-Kanarienvogel war AWSs dokumentierter Beispielschlüssel, und der enthält
  „EXAMPLE" — genau das Wort, das die Platzhalter-Ausnahme absichtlich durchlässt. Der
  Kanarienvogel prüfte die Ausnahme statt der Regel. Ersetzt durch einen unauffälligen
  Fake-Schlüssel; die Falle steht in der Wissensnotiz.
- **Und git_guard verweigerte beim Schreiben des Selbsttests mein eigenes Kommando:**
  `--force` war zerlegt, „origin main" nicht — das Push-auf-main-Muster griff im
  Heredoc-Text. Zweiter Vorfall dieser Klasse, jetzt als Troubleshooting-Notiz
  [[git_guard verwechselt Erwähnung mit Gebrauch]] mit occurrences: 2.
- `/bootstrap` führt den Selbsttest nach der Hook-Installation aus; das Umgebungs-Manifest
  trägt den Eintrag „Leitplanken — Scharfschaltung" mit Datum und Ergebnis.
- `guardrails.md`: Abschnitt „Three anchor points - and what they do not hold" —
  Abdeckungstabelle plus die bekannten Umgehungen, ausgeschrieben statt gewünscht:
  Enforcement-Dateien editierbar (Diff und CI-Warnung sind die Antwort), Mensch kann den
  Hook entfernen (sein Recht — der Mensch überstimmt Regeln, der Agent nicht), fehlender
  Interpreter versagt offen (dafür der Selbsttest), das TDD-Signal prüft Beilage, nicht
  Reihenfolge. Garantie der drei Anker: Ein Verstoß kommt nicht leise weit. Nicht mehr.
- [[ADR-0012 Durchsetzung an drei Ankerpunkten]] hält die Entscheidung samt verworfener
  Alternativen fest (Bash-Analyse je Aufruf: unzuverlässiges Raten; nur CI: erreicht die
  Zielgruppe nicht). Wissensnotiz mit allen Quellen:
  [[Durchsetzungsschicht - Ankerpunkte und bekannte Umgehungen]].

Vier neue Tests, Suite 134 grün. Vault- und Rückverfolgbarkeitsprüfung ohne Befund.

## Kontext

- Externe Belege: Hook-Matcher decken nur das jeweilige Tool ab; permissions.deny schützt
  Hook-Dateien nachweislich unzuverlässig (Issue #11226); dokumentierter
  Überspring-Vorfall über sechs Commits in Folge
- Fail-open verletzt unsere eigene Regel aus `security.md` — mindestens muss der Zustand
  prüfbar sein, wenn er schon nicht erzwingbar ist

## Agent

`claude-code` — Werkzeug, Tests, Regeln, ADR, Notiz.

## Abhängigkeiten

- [[T-0035 Durchsetzung am Commit]]

## Notizen

- Der Selbsttest gehört nicht in CI: Dort ist der pre-commit-Hook naturgemäß nicht
  installiert, und das ist dort auch richtig so. Er gehört zu `/bootstrap` — an den Moment,
  in dem ein Klon scharfgestellt wird.
