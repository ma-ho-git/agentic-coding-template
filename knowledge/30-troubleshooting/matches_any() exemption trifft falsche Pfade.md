---
title: matches_any() exemption trifft falsche Pfade
type: troubleshooting
tags: [topic/agents, stack/python]
status: active
created: 2026-08-19
updated: 2026-08-19
review_after: 2026-11-19
occurrences: 1
related: ["[[T-0002 Hooks zur Durchsetzung der Vorgaben]]", "[[T-0011 matches_any() Pfadabgleich reparieren]]"]
---

# matches_any() exemption trifft falsche Pfade

## Symptom

Eine Datei, die klar kein Test ist (z. B. `src/best_case_report.py` oder irgendeine Datei
unterhalb eines Ordners, dessen Name mit `test_` beginnt), wird von `check_contract.py`
fälschlich als "Testdatei" behandelt und braucht **keinen** `@contract`-Block, obwohl sie
eigentlich einen bräuchte.

Konkret reproduziert: eine Datei unter einem pytest-`tmp_path`-Ordner wie
`.../test_file_missing_contract_fai0/greet.py` wurde von der Exemption-Prüfung erfasst,
obwohl weder der Dateiname noch ein `tests/`-Verzeichnis beteiligt war.

## Kontext

- `.claude/hooks/_common.py`, Funktion `matches_any(rel_path, globs)`
- Gefunden beim Bau von `tools/ci_check.py` (T-0010), als ein Testfall mit `tmp_path`
  unerwartet als "exempt" durchging

## Ursache

`matches_any()` nutzt Pythons `fnmatch`, das `/` **nicht** als Pfadgrenze behandelt — `*`
matcht dort auch über Verzeichnisgrenzen hinweg, genau wie `**`. Zusätzlich wird der Zweig
`fnmatch.fnmatch("x/" + posix, pattern)` mit dem **unveränderten** Pattern (samt führendem
`**/`) geprüft. Für ein Pattern wie `**/test_*.*` wird daraus effektiv die Regel "irgendwo
im Pfad kommt `/test_` vor, und irgendwo danach im String noch ein `.`" — unabhängig davon,
ob das in ein und demselben Pfadsegment liegt. Ein Verzeichnisname, der zufällig mit
`test_` beginnt (wie pytest ihn aus dem Testfunktionsnamen baut), reicht damit aus, um jede
Datei darunter zu exemptieren.

## Lösung

**Behoben am 2026-08-19** in [[T-0011 matches_any() Pfadabgleich reparieren]].

`fnmatch` durch eine eigene, pfadbewusste Glob-Übersetzung ersetzt
(`glob_regex()` + `next_token()` in `.claude/hooks/_common.py`):

| Glob | Regex | Bedeutung |
| --- | --- | --- |
| `**/` | `(?:[^/]+/)*` | null oder mehr **ganze** Segmente |
| `**` | `.*` | beliebig, auch über `/` |
| `*` | `[^/]*` | beliebig **innerhalb** eines Segments |
| `?` | `[^/]` | ein Zeichen, kein `/` |

Match gegen `regex + \Z`, also gegen den ganzen Pfad. Die Token-Tabelle ist
längster-Treffer-zuerst sortiert, damit `**/` vor `**` vor `*` greift.

Zwei Nebeneffekte, beide gewollt:

- Pfade außerhalb des Projekts (`../../tmp/…`) matchen keine Exemption mehr → sie gelten
  als **nicht** exempt. Fail closed, entspricht `.claude/rules/security.md`.
- Verzeichnisse wie `generated_reports/` werden korrekt **nicht** mehr von `**/generated/**`
  erfasst. Vorher verschluckte `fnmatch` sie still.

Der frühere Workaround (`CLAUDE_PROJECT_DIR` in Tests auf `tmp_path` setzen) ist nicht mehr
nötig. Er bleibt in `tests/tools/test_ci_check.py` trotzdem stehen — hermetische Tests, die
nicht vom Ablageort des Repos abhängen, sind ohnehin die bessere Praxis.

## Sackgassen

- Keine — der Bug wurde beim ersten Testlauf von `tools/ci_check.py` sofort sichtbar
  (Testfall erwartete einen Block, bekam aber 0 Fehler).
- Beim Nachstellen des Fixes lief allerdings eine erste End-to-End-Prüfung in einem
  Temp-Verzeichnis **ohne** `.claude/hooks/config.json`. Dann liefert `load_config()` ein
  leeres Dict, die Exemption-Liste ist leer und *alles* blockt — sah nach einem kaputten
  Fix aus, war aber ein kaputter Testaufbau. Config mitkopieren.

## Vorbeugung

- Exemption-Logik nicht mit rohem `fnmatch` auf ganzen Pfaden testen, wenn Verzeichnisnamen
  aus Testframeworks (wie pytest-`tmp_path`) Substrings enthalten können, die wie
  Glob-Fragmente aussehen (`test_...`).
- Bei neuen Hook-Tests: `CLAUDE_PROJECT_DIR` auf ein sauberes, flaches Testverzeichnis
  zeigen lassen statt auf pytest-generierte, tief verschachtelte Pfade.
