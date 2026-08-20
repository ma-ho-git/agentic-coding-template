# Agentic Coding Template

Vorlage für strukturiertes Vibe-Coding mit **Claude Code** und **Claude Cowork**.
Klonen, `/bootstrap` aufrufen, loslegen.

Das Template gibt den Agenten verbindliche Regeln, eine Obsidian-Wissensdatenbank mit
Kanban-Aufgabenverwaltung und automatische Prüfungen, die die Regeln durchsetzen statt sie
nur zu empfehlen.

<!-- template-placeholder -->
> **Für ein eigenes Projekt:** Diese README beschreibt die *Vorlage*. Ersetze sie durch die
> deines Projekts — `/bootstrap` erinnert daran, und `tools/check_placeholders.py` findet,
> was noch übrig ist.

## Was es macht

| Bereich | Inhalt |
| --- | --- |
| **Anforderungen zuerst** | Bevor die erste Zeile Produktivcode entsteht, ist geklärt, *was* gebaut wird — und welche funktionalen, technischen, organisatorischen, Sicherheits-, Rechts- und Qualitätsanforderungen dabei gelten. Ein **Startgate** setzt das durch: Solange der Rahmen nicht freigegeben ist, werden Schreibzugriffe auf Produktivcode abgelehnt. Freigeben darf nur ein Mensch |
| **Regeln** | TDD verpflichtend, harte Größen- und Namensgrenzen, Design-Pattern-Prüfung vor dem Schreiben, Sicherheitsvorgaben |
| **Fehler- und Ausfallverhalten** | Der Agent handelt als erfahrener Entwickler: Für jede Eingabe, jede Ausnahme und jedes angebundene System wird entschieden, was im Fehlerfall passiert — und zwar für alle drei Arten von Ausfall getrennt: *nicht erreichbar*, *zu langsam*, *falsche Antwort*. Jeder behandelte Fehlerpfad braucht einen Test, der ihn auslöst |
| **Contract-Kommentare** | Jede Quelldatei nennt ihre Abhängigkeiten und ihre bekannten Aufrufer — der Wirkungsradius einer Änderung ist am Code ablesbar, ohne die Codebasis zu durchsuchen |
| **Wissensdatenbank** | Obsidian-Vault: Projektmanagement, Kanban-Board, Recherchewissen, Troubleshooting, ADRs — inklusive Deprecation-Workflow für veraltetes Wissen |
| **Leitplanken in zwei Klassen** | **Starre** Leitplanken sind maschinell durchgesetzt und für den Agenten nicht übersteuerbar: Geheimnisse, fehlende Contract-Blöcke, Aufgaben ohne Anforderung, zerstörerische Git-Kommandos, das Startgate. **Flexible** blockieren nie, sondern verlangen bei bewusster Abweichung eine Begründung im Code. Jede Meldung nennt ihre Klasse — sonst kann man eine Wand nicht von einem Hinweis unterscheiden |
| **Durchsetzung an drei Stellen** | Beim **Werkzeugaufruf** (Hooks), beim **Commit** (`pre-commit`, von `/bootstrap` installiert) und in der **CI** (jeder Push) — überall dieselben Prüfungen. Der Commit ist der Punkt, den jeder Schreibweg passiert, auch einer, den kein Hook gesehen hat |
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

**Der einfache Weg:** oben auf [**Use this template**](https://github.com/ma-ho-git/agentic-coding-template/generate)
klicken. GitHub legt dir daraus ein eigenes Repository an — mit einem einzigen frischen
Commit, ohne die Historie dieser Vorlage und ohne Verbindung zu ihr. Danach klonen und
starten:

```bash
git clone https://github.com/DEIN-KONTO/mein-projekt.git
cd mein-projekt
claude
```

**Ohne GitHub-Konto** geht es genauso, nur von Hand:

```bash
git clone https://github.com/ma-ho-git/agentic-coding-template.git mein-projekt
cd mein-projekt
rm -rf .git && git init    # trennt die Historie der Vorlage ab, macht daraus dein Projekt
claude
```

Das `rm -rf .git` löscht die Versionsgeschichte **der frisch geklonten Vorlage** — deine
Dateien bleiben, und ein anderes Repository ist nicht betroffen, solange du im richtigen
Verzeichnis stehst. Wenn du unsicher bist, nimm den Weg über den Knopf.

Dann in beiden Fällen, in Claude Code:

```
/bootstrap
```

`/bootstrap` prüft, ob die Annahmen des Templates noch stimmen (Claude Code, Cowork, GitHub,
Stack), passt das Repo an, richtet das Projekt ein und erklärt dir kurz, wie es weitergeht.

**Dabei hört das Repository auf, eine Vorlage zu sein.** Das ist ein eigener Schritt, und du
solltest wissen, was er tut:

- Die Anforderungen, Aufgaben und Entscheidungen der Vorlage wandern nach
  `knowledge/90-meta/beispiel/` — **archiviert, nicht gelöscht**. Ein ausgefülltes Beispiel
  zeigt mehr als ein leeres Formular; wer es nicht braucht, löscht den Ordner.
- Die Rahmendokumente (Vision, Rahmen, Stakeholder, Glossar, Risiken …) werden durch **leere
  Formulare mit Ausfüllhinweisen** ersetzt. Sie sagen dir, was hineingehört — das ist genau
  das, wonach `/req-elicit` gleich fragt.
- Das Startgate wird **geschlossen**. Die Vorlage selbst hat ein offenes; ohne diesen Schritt
  erbte dein Projekt eine Freigabe, die nie jemand für dein Vorhaben erteilt hat.
- Der `pre-commit`-Haken wird installiert. Ein frischer Klon bringt ihn nicht mit — Git-Haken
  liegen in `.git/hooks/` und werden nicht mitgeklont.

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
| `tools/` | Prüfskripte: `check_all.py` (führt alle aus), `check_vault.py`, `check_traceability.py`, `check_licenses.py`, `check_placeholders.py`, `check_armed.py`, `handover.py`, `install_hooks.py` |
| `licenses/` | Lizenztexte übernommener Fremdkomponenten (hier leer, siehe unten) |
| `tests/` | Tests für die Hooks und Tools selbst |
| `.github/workflows/` | CI: prüft Pull Requests mit denselben Skripten wie die Hooks |
| `examples/` | Kleines Beispielfeature, zeigt den Zyklus TDD → Contract → `/contract-sync`; beim eigenen Projektstart löschen |

## Anpassen

- **Schwellenwerte** — `.claude/hooks/config.json` (Zuweisungen je Funktion, Parameterzahl, Namenslänge …)
- **Projektzuschnitt** — `project_scope` in `.claude/hooks/config.json`; die Begründung gehört
  in `knowledge/05-requirements/baseline.md`, die alte bleibt stehen
- **Blockieren vs. warnen** — welche Prüfung starr und welche flexibel ist, steht in
  `.claude/rules/guardrails.md` samt Zuordnungstest für neue Regeln
  (`knowledge/10-pm/decisions/ADR-0006 …`); verdrahtet wird es in `.claude/settings.json`
- **Sprache der Dokumentation** — `CLAUDE.md` §7
- **Stack** — `stacks/` erweitern, beim Bootstrap auswählen

## Lizenz

[MIT](LICENSE).

Die Lizenz gilt für das Template. Code, den du damit erzeugst, gehört dir und steht nicht
unter dieser Lizenz.

**Fremdcode:** keiner. Das Template setzt auf keiner fremden Codebasis auf
(`knowledge/10-pm/decisions/ADR-0010 …`), das Register unter
`knowledge/05-requirements/fremdkomponenten.md` ist entsprechend leer.

Übernimmst du in deinem Projekt eine fremde Komponente, gehören ihre Pflichten dorthin: der
Lizenztext nach `licenses/`, die Namensnennung in **dein** README, und der Eintrag ins
Register. `tools/check_licenses.py` prüft das in CI — Vollständigkeit, nicht Rechtmäßigkeit.
