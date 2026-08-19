---
title: Obsidian-Kanban Dateiformat
type: knowledge
tags: [topic/meta, stack/obsidian]
status: active
created: 2026-08-19
updated: 2026-08-19
review_after: 2026-11-19
related: ["[[ADR-0003 Kanban-Board mit Wikilink-Karten]]", "[[Konventionen der Wissensdatenbank]]", "[[00-index]]"]
---

# Obsidian-Kanban Dateiformat

## Kurz

Ein Kanban-Board des obsidian-kanban-Plugins ist eine einzelne Markdown-Datei mit fester
Struktur. Format aus dem Parser-Quellcode verifiziert, nicht aus Blogbeiträgen abgeschrieben.

## Kernpunkte

- Frontmatter-Schlüssel: `kanban-plugin: board` (ältere Versionen: `basic`)
- Lane = Überschrift zweiter Ebene: `## Lane-Name`
- Karte = Listeneintrag mit Checkbox: `- [ ] Inhalt`, erledigt `- [x] Inhalt`
- Erledigt-Lane wird durch einen Absatz `**Complete**` als erste Zeile der Lane markiert
- Archiv: waagerechte Linie `***`, dann `## Archive`
- Einstellungen am Dateiende in einem `%% kanban:settings`-Kommentarblock mit JSON-Codeblock
- Karten dürfen beliebiges Markdown enthalten, also auch `[[Wikilinks]]`

## Beispiel

```markdown
---

kanban-plugin: board

---

## Ready

- [ ] [[T-0042 Token-Refresh]]

## Done

**Complete**

- [x] [[T-0001 Repo-Setup]]

%% kanban:settings
```{"kanban-plugin":"board"}```
%%
```

## Plugin-Name in Obsidian

- Community-Plugin **"Kanban"** von mgmeyers
- Installation: Einstellungen → Community-Plugins → Durchsuchen → "Kanban"
- **Optional.** Kein Code im Repo hängt am Plugin — siehe nächster Abschnitt.

## Was ohne Plugin passiert

- `board.md` ist gültiges Markdown und bleibt voll nutzbar: `## Lane` rendert als
  Überschrift, `- [ ] [[T-XXXX …]]` als klickbare Checkliste
- `%% kanban:settings %%` ist ein Obsidian-Kommentar → in der Leseansicht unsichtbar
- Frontmatter `kanban-plugin: board` ist dann nur eine ungenutzte Property, stört nicht
- `session_brief.py` parst das Board mit eigener Regex (`^##\s+…`, `^\s*-\s*\[[ x]\]`),
  nicht über das Plugin. Auch die Test-Suite braucht weder Obsidian noch Plugin.

## Reibungspunkt mit Plugin

- Karte im Plugin ziehen ändert **nur `board.md`**, nicht das `status:`-Feld der Task-Datei
- Die Wahrheit ist laut [[ADR-0003 Kanban-Board mit Wikilink-Karten]] aber das Frontmatter
- Folge: Board und Task-Datei divergieren still → `/board-sync` repariert das
- Ohne Plugin ist die Divergenzgefahr etwas kleiner, weil Handbearbeitung bewusster passiert

## Wartungslage

- Kanonisches Repo: **`community-archive/obsidian-kanban`**. Die früher hier notierten
  `mgmeyers/obsidian-kanban` und `obsidian-community/obsidian-kanban` leiten beide dorthin
  um — die alte Angabe „Fortführung als `obsidian-community/…`" war falsch.
- Nicht formal archiviert (`archived: false`), aber Organisationsname ist `community-archive`
- Letzter Push **2026-03-06**, 599 offene Issues, 4476 Sterne
- README: „The Kanban plugin is looking for new maintainers"
- Risiko trotzdem gering: das Board bleibt ohne Plugin normales, lesbares Markdown

## Aktivere Alternative (beobachten, nicht umgestellt)

- `xiwcx/obsidian-bases-kanban` — „Kanban Bases View", MIT, letzter Push 2026-06-26
- Baut auf Obsidian *Bases* auf, gruppiert Notizen nach einer Property
- Würde Lanes direkt aus dem `status:`-Feld der Task-Dateien bilden → **keine `board.md`
  mehr nötig**, Divergenzproblem an der Wurzel gelöst
- Dagegen: deutlich kleineres Projekt (139 Sterne), und es wäre ein Umbau von
  [[ADR-0003 Kanban-Board mit Wikilink-Karten]], `session_brief.py` und `/board-sync`

## Quellen

- `src/parsers/formats/list.ts` in https://github.com/community-archive/obsidian-kanban — abgerufen 2026-08-19
- GitHub-Such-API, Query `obsidian-kanban in:name` (Felder `full_name`, `archived`,
  `pushed_at`, `open_issues_count`) — abgerufen 2026-08-19
- https://github.com/xiwcx/obsidian-bases-kanban — abgerufen 2026-08-19
