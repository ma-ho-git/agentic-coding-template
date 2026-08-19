---
title: Konfigurationsebenen von Claude Code
type: knowledge
tags: [topic/agents, stack/claude-code]
status: active
created: 2026-08-19
updated: 2026-08-19
review_after: 2026-11-19
related: ["[[ADR-0001 Regeln aufteilen statt eine große CLAUDE.md]]", "[[ADR-0002 Prüfbare Vorgaben in Hooks statt in Prosa]]", "[[Cowork liest die Repo-Konfiguration nicht]]", "[[00-index]]"]
---

# Konfigurationsebenen von Claude Code

## Kurz

Claude Code kennt fünf Ebenen, ein Projekt zu steuern. Sie unterscheiden sich vor allem im
**Ladeverhalten** — das ist das Kriterium, nach dem man wählt, nicht der Inhalt.

## Kernpunkte

| Ebene | Ort | lädt | Kosten |
| --- | --- | --- | --- |
| Memory | `CLAUDE.md` bzw. `.claude/CLAUDE.md` | jede Session, vollständig | dauerhaft |
| Rules | `.claude/rules/*.md` | immer, oder pfad-gebunden über `paths:` | dauerhaft bzw. bedarfsweise |
| Skills | `.claude/skills/<name>/SKILL.md` | nur bei Aufruf oder Modellentscheidung | nur bei Nutzung |
| Subagents | `.claude/agents/*.md` | bei Aufruf, eigener Kontext | nur bei Nutzung |
| Hooks | `.claude/settings.json` | deterministisch bei Events | keine Kontextkosten |

- **Wichtigster Satz der Dokumentation:** *"CLAUDE.md instructions shape Claude's behavior
  but are not a hard enforcement layer."* Verbindliches gehört in Hooks.
- Empfehlung: unter **200 Zeilen** je `CLAUDE.md`. Längere Dateien senken die Befolgung.
- `@pfad`-Importe sparen **keinen** Kontext — die importierte Datei wird beim Start mitgeladen.
- Pfad-gebundene Regeln (`paths:` im Frontmatter) laden erst, wenn Claude eine passende
  Datei liest. Nach `/compact` werden sie **nicht** automatisch neu eingespielt.
- `.claude/commands/*.md` und Skills erzeugen beide `/name`; bei Namensgleichheit gewinnt der Skill.
- Reihenfolge bei Namenskonflikten: Enterprise > persönlich > Projekt; Plugin-Skills sind
  über `plugin:skill` eigenständig benannt.
- Skills werden zur Laufzeit neu eingelesen; neue Skill-Verzeichnisse brauchen einen Neustart.

## Hooks

- Events u. a. `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `Stop`
- Payload kommt als JSON auf stdin (`tool_name`, `tool_input`, `cwd`)
- **Exit-Code 2** blockiert; stderr geht an den Agenten
- **Exit 0 mit JSON** steuert strukturiert:
  `hookSpecificOutput.permissionDecision` (`allow`/`deny`, nur `PreToolUse`) und
  `hookSpecificOutput.additionalContext` (Hinweis in den Kontext)
- `${CLAUDE_PROJECT_DIR}` zeigt auf die Projektwurzel — in Kommandos verwenden,
  nicht auf das Arbeitsverzeichnis verlassen

## Quellen

- https://code.claude.com/docs/en/memory — abgerufen 2026-08-19
- https://code.claude.com/docs/en/skills — abgerufen 2026-08-19
- https://code.claude.com/docs/en/hooks — abgerufen 2026-08-19
- https://code.claude.com/docs/en/sub-agents — abgerufen 2026-08-19
