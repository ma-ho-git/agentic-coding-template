# Agentic Coding Template

Vorlage für strukturiertes Vibe-Coding mit **Claude Code** und **Claude Cowork**.
Klonen, `/bootstrap` aufrufen, loslegen.

Das Template gibt den Agenten verbindliche Regeln, eine Obsidian-Wissensdatenbank mit
Kanban-Aufgabenverwaltung und automatische Prüfungen, die die Regeln durchsetzen statt sie
nur zu empfehlen.

## Was es macht

| Bereich | Inhalt |
| --- | --- |
| **Regeln** | TDD verpflichtend, harte Größen- und Namensgrenzen, Design-Pattern-Prüfung vor dem Schreiben, Sicherheitsvorgaben |
| **Contract-Kommentare** | Jede Quelldatei nennt ihre Abhängigkeiten und ihre bekannten Aufrufer — der Wirkungsradius einer Änderung ist am Code ablesbar, ohne die Codebasis zu durchsuchen |
| **Wissensdatenbank** | Obsidian-Vault: Projektmanagement, Kanban-Board, Recherchewissen, Troubleshooting, ADRs — inklusive Deprecation-Workflow für veraltetes Wissen |
| **Durchsetzung** | Hooks blockieren Geheimnisse, fehlende Contract-Kommentare und zerstörerische Kommandos; Größen- und Namensverstöße erzeugen Hinweise. Läuft zusätzlich als GitHub-Actions-Check auf jedem Pull Request — gilt auch für Beiträge ohne die lokalen Hooks |
| **Agenten-Routing** | Für jede Aufgabe wird entschieden, ob Claude Code oder Cowork besser passt |

## Voraussetzungen

- **Claude Code** — lädt die Konfiguration im Repo automatisch
- **Python 3** — für die Hook-Skripte
- **Obsidian** *(optional)* — für die Wissensdatenbank. Alles bleibt auch ohne Obsidian
  normales, lesbares Markdown.
- **Kanban-Plugin** *(optional)* — nur für die Drag-and-Drop-Ansicht des Boards. In Obsidian
  unter Community-Plugins als **„Kanban"** zu finden
  ([Repo](https://github.com/community-archive/obsidian-kanban)). Kein Code des Templates
  hängt daran: `board.md` ist ohne Plugin eine klickbare Checkliste, die Prüfskripte lesen
  das Board selbst. Beachte, dass das Plugin derzeit keine aktive Wartung hat —
  Details in `knowledge/20-knowledge/Obsidian-Kanban Dateiformat.md`.
- **Claude Cowork** *(optional)* — siehe `cowork/README.md`; Cowork liest die Repo-Konfiguration
  **nicht** und braucht einen einmaligen Einrichtungsschritt

## Erste Schritte

```bash
git clone https://github.com/ma-ho-git/agentic-coding-template.git mein-projekt
cd mein-projekt
rm -rf .git && git init
claude
```

Dann in Claude Code:

```
/bootstrap
```

`/bootstrap` prüft, ob die Annahmen des Templates noch stimmen (Claude Code, Cowork, GitHub,
Stack), passt das Repo an, richtet das Projekt ein und erklärt dir kurz, wie es weitergeht.

Danach ist der Arbeitszyklus immer derselbe:

```
/task-next  →  Test schreiben  →  Code schreiben  →  /contract-sync  →  /task-done
```

## Deine Aufgaben als Verwender

Die Agenten arbeiten, entscheiden aber nicht. Das bleibt bei dir:

- **Umfang und Prioritäten festlegen** — das Board genehmigen, nicht jeden Vorschlag durchwinken
- **Zugänge bereitstellen** — Credentials über Umgebungsvariablen, niemals in den Chat
- **Reviewen und mergen** — Agenten mergen nicht selbst
- **Rückfragen beantworten** — eine beantwortete Frage ist billiger als eine geratene Annahme
- **Bei `/bootstrap` dabei sein** — Projektname, Zweck und Stack legst du fest

## Struktur

| Pfad | Inhalt |
| --- | --- |
| `CLAUDE.md` | Einstiegspunkt für Agenten, unter 100 Zeilen |
| `.claude/rules/` | Regeln nach Thema; code-nahe Regeln laden nur bei Quelldateien |
| `.claude/skills/` | Abläufe: `/bootstrap`, `/task-next`, `/task-done`, `/kb-capture`, … |
| `.claude/agents/` | Subagenten: Recherche, Testautor, Review, Wissenspflege |
| `.claude/hooks/` | Prüfskripte; Schwellenwerte in `config.json` |
| `knowledge/` | Obsidian-Vault, deutschsprachig |
| `stacks/` | Stack-Profile (Python, TypeScript, Vorlage) |
| `cowork/` | Einrichtung für Claude Cowork |
| `tools/` | Prüfskripte, z. B. `check_vault.py`, `ci_check.py` |
| `tests/` | Tests für die Hooks und Tools selbst |
| `.github/workflows/` | CI: prüft Pull Requests mit denselben Skripten wie die Hooks |
| `examples/` | Kleines Beispielfeature, zeigt den Zyklus TDD → Contract → `/contract-sync`; beim eigenen Projektstart löschen |

## Anpassen

- **Schwellenwerte** — `.claude/hooks/config.json` (Funktionslänge, Parameterzahl, Namenslänge …)
- **Blockieren vs. warnen** — welche Prüfung wie hart ist, steht in
  `knowledge/10-pm/decisions/ADR-0002 …`; geändert wird es in `.claude/settings.json`
- **Sprache der Dokumentation** — `CLAUDE.md` §7
- **Stack** — `stacks/` erweitern, beim Bootstrap auswählen

## Lizenz

[MIT](LICENSE).

Die Lizenz gilt für das Template. Code, den du damit erzeugst, gehört dir und steht nicht
unter dieser Lizenz.
