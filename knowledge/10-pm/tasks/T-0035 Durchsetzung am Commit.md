---
id: T-0035
title: Durchsetzung am Commit
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
related: ["[[T-0036 CI als echter Rückhalt]]", "[[T-0037 Scharfschaltung nachweisen]]", "[[ADR-0006 Zwei Klassen von Leitplanken]]"]
---

# T-0035 Durchsetzung am Commit

## Anforderung

[[REQ-0011 Prüfbare Vorgaben werden durchgesetzt, nicht empfohlen]] — der Befund F1 aus der
Prüfung vom 2026-08-20: Die Hook-Schicht deckt nur den Write/Edit-Weg ab. Dateien, die über
Bash geschrieben werden, passieren alle fünf Schreibprüfungen ungeprüft — nachgewiesen an der
laufenden Sitzung selbst.

## Ziel

Jeder Schreibweg — Write-Tool, Bash, fremder Editor, Mensch — läuft durch denselben
Engpass: den Commit. Dort laufen die Prüfungen, lokal und ohne GitHub.

## Akzeptanzkriterien

- [x] `tools/check_all.py`: ein Kommando für alle Prüfungen — je geänderter Datei die
      Schreib-Hooks (Geheimnisse, Contract, Qualität) **und das Startgate**, dazu repo-weit
      Vault, Rückverfolgbarkeit, Lizenzen. Modi: `--staged`, `--range A..B`, `--all`,
      explizite Pfade. Dateinamen mit Leerzeichen funktionieren.
- [x] TDD-Signal: geänderte Quelldatei ohne Teständerung im selben Satz → `[FLEXIBLE]`-Hinweis,
      nie blockend. Abschaltbar über `flag_missing_tests`. Gilt für das Erstellen und Ändern
      von Code — Doku, Konfiguration und Wissensbasis lösen es nicht aus.
- [x] `tools/install_hooks.py` installiert den pre-commit-Hook (`check_all --staged`),
      idempotent; ein fremder vorhandener Hook wird **nicht** überschrieben, sondern gemeldet.
- [x] `git_guard` verweigert das Überspringen: den Schalter no-verify bei Commits, das
      Kurzzeichen `-n` bei Commits, und das Umbiegen des Hook-Pfads (hooksPath). Ein
      Dry-Run-Push mit `-n` bleibt erlaubt.
- [x] `/bootstrap` installiert den Hook in Schritt 2; `workflow.md` nennt den Engpass.
- [x] Tests für alles Obige; der pre-commit-Hook ist in diesem Repository installiert und
      der nächste Commit läuft nachweislich durch ihn.

## Ergebnis

- `tools/check_all.py`: ein Kommando, vier Modi, NUL-getrennte Dateinamen (die Task-Dateien
  mit Leerzeichen waren der Grund). Je Datei laufen Geheimnis-, Contract-, Task- und
  Qualitätsprüfung **und erstmals das Startgate außerhalb des Write-Wegs**; repo-weit Vault,
  Rückverfolgbarkeit, Lizenzen. `check_task` ist dabei in die blockenden Prüfungen von
  `ci_check` aufgerückt — damit prüft auch CI Task-Dateien.
- TDD-Signal als `[FLEXIBLE]`-Hinweis: geänderter Code ohne Teständerung im selben Satz.
  Ehrlich benannt, was es prüfen kann: **dass** ein Test beiliegt — nicht, dass er zuerst
  kam. Abschaltbar über `flag_missing_tests`.
- `tools/install_hooks.py`: idempotent, verweigert das Überschreiben eines fremden Hooks
  (fail closed) und sagt, welche Zeile man selbst übernehmen kann.
- `git_guard` verweigert die dokumentierte Umgehung: den Überspring-Schalter (no-verify,
  auch als Kurzform) bei Commits und das Umbiegen des Hook-Pfads. Ein Dry-Run-Push bleibt
  erlaubt. Muster und Testliterale zur Laufzeit zusammengesetzt — Gebrauch vs. Erwähnung.
- **Der Engpass fand am ersten Tag zwei echte Befunde:** `cowork/build-skills.sh` hatte
  keinen Contract-Block und galt dem Gate als Produktivcode — die Datei hat nie ein
  Write-Hook gesehen. Contract ergänzt, `cowork/**` als Werkzeug in die Gate-Ausnahmen
  (Test zuerst, dann Fix).
- Hook in diesem Repository installiert; der Abschluss-Commit dieser Aufgabe lief
  nachweislich durch ihn.
- 19 neue Tests, Suite 130 grün. `check_all --all` über das ganze Repository: Exit 0.
- Laufzeitmessung: `--all` braucht ~20 s (jede Datei × vier Subprozesse) — für den
  Normalfall `--staged` mit kleinen Sätzen irrelevant, für CI akzeptabel.

## Kontext

- Recherche 2026-08-20: Hooks feuern nur je Tool-Matcher; Commit-Hook plus CI ist das
  etablierte Gegenmittel, dokumentierte Umgehung ist der no-verify-Schalter — daher die
  git_guard-Sperre. Quellen in der Wissensnotiz zur Durchsetzung.
- Der Betriebsmodus dieser Umgebung leitet Dateiarbeit ausdrücklich über Bash — der
  ungeprüfte Weg ist hier also der Normalweg, nicht die Ausnahme.

## Agent

`claude-code` — Werkzeuge, Hook-Erweiterung, Tests.

## Abhängigkeiten

- keine

## Notizen

- Wortwahl in Prosa und Commit-Botschaften beachten: Die neuen git_guard-Muster greifen
  textbasiert. Die Kombination aus Commit-Kommando und Überspring-Schalter darf in keinem
  Bash-Kommandotext zusammenhängend auftauchen (Verwechslung von Gebrauch und Erwähnung,
  bekannt seit T-0007). Testliterale werden zur Laufzeit zusammengesetzt.
