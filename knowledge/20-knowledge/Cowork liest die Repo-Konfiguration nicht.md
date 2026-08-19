---
title: Cowork liest die Repo-Konfiguration nicht
type: knowledge
tags: [topic/agents, stack/cowork, stack/claude-code]
status: active
created: 2026-08-19
updated: 2026-08-19
review_after: 2026-11-19
related: ["[[Konfigurationsebenen von Claude Code]]", "[[ADR-0004 Cowork über ein leichtes Paket anbinden]]", "[[00-index]]"]
---

# Cowork liest die Repo-Konfiguration nicht

## Kurz

Zentrale Einschränkung für jedes Template, das beide Agenten steuern will:
Cowork lädt **keine** `.claude/`-Konfiguration aus einem geklonten Repository.

## Kernpunkte

| | Claude Code lokal | Claude Code Cloud-Session | Cowork (Desktop) |
| --- | --- | --- | --- |
| `CLAUDE.md` aus dem Repo | ja | ja | nicht dokumentiert |
| `.claude/rules/` | ja | ja | nein |
| `.claude/skills/` | ja | ja (aus dem geklonten Repo) | **nein** |
| `.claude/agents/` | ja | ja | nein |
| Hooks aus `.claude/settings.json` | ja | ja | nein |
| Skills aus dem claude.ai-Konto | nein | nein | **ja**, beim Sessionstart synchronisiert |

- Cowork-Sessions laden ausschließlich die Skills, die im **claude.ai-Konto** aktiviert sind
  (Verwaltung: Desktop-Seitenleiste → Customize, oder Skill-Einstellungen auf claude.ai)
- Cowork organisiert Kontext über **Projekte**: Instructions, verknüpfter Ordner, Memory
- Cowork-Projekte sind **desktop-lokal**, ohne Cloud-Sync, und existieren in Claude Code nicht

## Folgen für dieses Template

- Regeln, Hooks und Subagenten im Repo wirken **nur** in Claude Code
- Codearbeit gehört deshalb nach Claude Code — dort greifen die Prüfungen
- Cowork übernimmt Recherche, Dokumente und Material von außerhalb des Repos
- Für Cowork existiert `cowork/` mit Instructions-Text und hochladbaren Skills

## Quellen

- https://code.claude.com/docs/en/skills — Abschnitt "Skills in Cowork and cloud sessions", abgerufen 2026-08-19
- https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork — abgerufen 2026-08-19
