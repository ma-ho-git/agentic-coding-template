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

Dabei wird dir angeboten, dein Vorhaben zunächst in eigenen Worten zu **erzählen** —
`/szenario`. Kein Formular: du schreibst drauflos, der Agent ordnet es und fragt nach, wo
etwas fehlt. Daraus werden anschließend die Anforderungen abgeleitet. Optional; wenn du
lieber direkt loslegst, entfällt der Schritt und lässt sich jederzeit nachholen.

Sobald der Rahmen steht und **bevor** die erste Zeile Code entsteht, wird dir noch eine Frage
gestellt: `/solution-scan` — gibt es das vielleicht schon fertig? Der Agent misst gefundene
Projekte an deinen Anforderungen, prüft Lizenz und Wartungsstand und empfiehlt; entscheiden
tust du. „Nichts davon passt" ist ein vollwertiges Ergebnis und wird mit Begründung
festgehalten.

Danach ist der Arbeitszyklus immer derselbe:

```
/task-next  →  Test schreiben  →  Code schreiben  →  /contract-sync  →  /task-done
```

## Projektzuschnitt — wie viel Zeremonie?

Ein Wegwerfskript und ein gepflegtes Produkt brauchen dieselben Leitplanken, aber nicht
dieselbe Menge an Dokumentation. `/bootstrap` fragt deshalb, was du baust, und hält die
Antwort als `project_scope` in `.claude/hooks/config.json` fest — die **Begründung** dazu
kommt nach `knowledge/05-requirements/baseline.md`.

| Zuschnitt | Wofür | Anforderungserhebung | Dokumentation |
| --- | --- | --- | --- |
| `skript` | einmalig, nur für dich | alle sechs Kategorien werden gefragt, „trifft hier nicht zu, weil …" reicht als Antwort | Vision in drei Zeilen, ADR nur bei schwer umkehrbaren Entscheidungen, Fortschritt einzeilig |
| `werkzeug` | du gibst es weiter, überschaubarer Umfang | echte Antworten für Funktion, Technik, Sicherheit, Recht | zusätzlich Glossar und Risiken, ADR bei echten Alternativen |
| `produkt` | wird länger gepflegt, mehrere Beteiligte | jede Kategorie mit vereinbarter Anforderung | vollständig, ohne Abstriche |

Was der Zuschnitt **nicht** ändert: Das Startgate gilt immer, alle sechs Kategorien werden
immer gefragt, TDD gilt immer, und jede starre Leitplanke bleibt in jedem Zuschnitt scharf.
Kleiner werden nur die Antworten und die Schreibarbeit — nie die Prüfungen.

Ohne Angabe gilt `produkt`. Der Rückfall kostet Schreibarbeit, nie Sicherheit.

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

- **Schwellenwerte** — `.claude/hooks/config.json` (Zuweisungen je Funktion, Parameterzahl, Namenslänge …)
- **Projektzuschnitt** — `project_scope` in `.claude/hooks/config.json`; die Begründung gehört
  in `knowledge/05-requirements/baseline.md`, die alte bleibt stehen
- **Blockieren vs. warnen** — welche Prüfung wie hart ist, steht in
  `knowledge/10-pm/decisions/ADR-0002 …`; geändert wird es in `.claude/settings.json`
- **Sprache der Dokumentation** — `CLAUDE.md` §7
- **Stack** — `stacks/` erweitern, beim Bootstrap auswählen

## Lizenz

[MIT](LICENSE).

Die Lizenz gilt für das Template. Code, den du damit erzeugst, gehört dir und steht nicht
unter dieser Lizenz.
