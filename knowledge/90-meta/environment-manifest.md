---
title: Umgebungs-Manifest
aliases: ["Umgebungs-Manifest"]
type: knowledge
tags: [topic/meta, stack/claude-code]
status: active
created: 2026-08-19
updated: 2026-08-19
review_after: 2026-09-18
related: ["[[00-index]]", "[[SessionStart meldet BOOTSTRAP REQUIRED trotz aktuellem Manifest]]"]
---

# Umgebungs-Manifest

## Kurz

Alle externen Annahmen, auf denen dieses Template beruht — mit Prüfdatum und Quelle.
`/bootstrap` arbeitet diese Liste ab. Einträge älter als 30 Tage gelten als ungeprüft.

Feldbedeutung: `verified` = Datum der letzten Prüfung gegen die Quelle.
`state` = `ok` (unverändert), `changed` (angepasst), `unknown` (nicht prüfbar).

---

## Claude Code — Konfigurationsebenen

- **assumption:** `CLAUDE.md` im Repo-Root oder `.claude/CLAUDE.md`; Regeln in `.claude/rules/*.md`
  mit optionalem `paths:`-Frontmatter; Skills in `.claude/skills/<name>/SKILL.md`;
  Subagenten in `.claude/agents/*.md`
- **verified:** 2026-08-19
- **state:** ok
- **source:** https://code.claude.com/docs/en/memory , https://code.claude.com/docs/en/skills
- **action:** —

## Claude Code — CLAUDE.md ist keine harte Durchsetzung

- **assumption:** Anweisungen in `CLAUDE.md` beeinflussen das Verhalten, garantieren es nicht.
  Verbindliche Regeln gehören in Hooks.
- **verified:** 2026-08-19
- **state:** ok
- **source:** https://code.claude.com/docs/en/memory
- **action:** Prüfbare Vorgaben liegen in `.claude/hooks/`

## Claude Code — Hook-Events und Payload

- **assumption:** Events `SessionStart`, `PreToolUse`, `PostToolUse` existieren;
  Konfiguration in `.claude/settings.json` unter `hooks`; Payload auf stdin mit
  `tool_input.file_path` bzw. `tool_input.command`; Exit-Code 2 blockiert;
  JSON-Antwort mit `hookSpecificOutput.permissionDecision` bzw. `.additionalContext`
- **verified:** 2026-08-19
- **state:** ok
- **source:** https://code.claude.com/docs/en/hooks
- **action:** —

## Cowork — liest die Repo-Konfiguration nicht

- **assumption:** Cowork-Sessions laden nur die im claude.ai-Konto aktivierten Skills,
  nicht `.claude/skills/` aus einem geklonten Repo. Cloud-Sessions von Claude Code laden
  Projekt-Skills aus dem geklonten Repo sehr wohl.
- **verified:** 2026-08-19
- **state:** ok
- **source:** https://code.claude.com/docs/en/skills (Abschnitt "Skills in Cowork and cloud sessions")
- **action:** Deshalb existiert `cowork/`. Fällt diese Annahme, wird `cowork/` überflüssig.

## Obsidian — Kanban-Dateiformat

- **assumption:** Frontmatter-Schlüssel `kanban-plugin: board`; Lanes als `## Überschrift`;
  Karten als `- [ ] …`; `**Complete**` markiert die Erledigt-Lane; Einstellungsblock
  `%% kanban:settings` am Dateiende
- **verified:** 2026-08-19
- **state:** ok
- **source:** Parser-Quellcode `src/parsers/formats/list.ts` im Repo `obsidian-community/obsidian-kanban`
- **action:** —

## Obsidian — Kanban-Plugin sucht Maintainer

- **assumption:** Original `mgmeyers/obsidian-kanban` ist archiviert; Fortführung als
  `obsidian-community/obsidian-kanban`; Autor sucht seit Januar 2026 Nachfolger
- **verified:** 2026-08-19
- **state:** ok
- **source:** https://github.com/obsidian-community/obsidian-kanban/blob/main/MAINTAINERS.md
- **action:** Risiko akzeptiert — das Board ist reines Markdown und bleibt ohne Plugin lesbar

## GitHub — Schreibzugriff aus Cloud-Sessions

- **assumption:** Cloud-Sessions authentifizieren sich über einen Proxy; das Repo muss der
  Session ausdrücklich zugeordnet sein. Verbindung über die Claude GitHub App oder `/web-setup`.
- **verified:** 2026-08-19
- **state:** ok
- **source:** https://code.claude.com/docs/en/claude-code-on-the-web
- **action:** siehe [[Git-Proxy verweigert Push - Repo nicht in der Session freigegeben]]

## Aktiver Stack

- **assumption:** Python-Profil (`stacks/python.md`) passt, da alles Code in diesem Repo
  (`.claude/hooks/`, `tools/`) Python ist. Layout und Commands mussten an die Realität
  angepasst werden (kein `src/<package>/`, kein `pyproject.toml`, keine Runtime-Deps).
- **verified:** 2026-08-19
- **state:** changed
- **source:** `stacks/python.md` gegen `find .claude/hooks tools -type f` und installierte
  Toolchain (`which uv pytest ruff mypy`, `python3 --version`) geprüft
- **action:** `stacks/active.md` angelegt, Python-Version auf 3.11+ korrigiert (installiert:
  3.11.15, Vorlage sagte 3.12+), Layout/Commands auf `.claude/hooks/`+`tools/` umgestellt.
  Fehlendes `pyproject.toml` für Test-Setup an T-0007 verwiesen, nicht hier erledigt.
