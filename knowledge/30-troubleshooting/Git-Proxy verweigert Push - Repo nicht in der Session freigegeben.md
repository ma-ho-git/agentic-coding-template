---
title: Git-Proxy verweigert Push - Repo nicht in der Session freigegeben
type: troubleshooting
tags: [topic/meta, stack/github, stack/claude-code]
status: active
created: 2026-08-19
updated: 2026-08-19
review_after: 2026-11-19
occurrences: 1
related: ["[[T-0008 Schreibzugriff auf das GitHub-Repo]]", "[[00-index]]"]
---

# Git-Proxy verweigert Push - Repo nicht in der Session freigegeben

## Symptom

```
remote: access denied by the git proxy: <owner>/<repo> is not in this session's authorized
repository set, so the proxy will not inject a credential for it. To fix, add the repository
to the session's sources.
fatal: unable to access 'https://github.com/<owner>/<repo>.git/': The requested URL returned error: 403
```

Bei einem Zugriff auf die GitHub-API zusätzlich:

```
GitHub access to this repository is not enabled for this session. Use add_repo to request access.
```

## Kontext

- Umgebung: Cloud-Session (Cowork bzw. Claude Code in der Cloud), August 2026
- `git clone` und `git ls-remote` funktionieren — das Repo ist öffentlich, Lesen braucht kein Credential
- `git push` schlägt fehl
- `env` zeigt `GITHUB_TOKEN=proxy-injected`, `https_proxy=http://127.0.0.1:<port>`

## Ursache

Nicht fehlende Anmeldedaten, sondern **fehlende Autorisierung**.

Die Session enthält kein echtes GitHub-Token. Ein vorgeschalteter Proxy injiziert Credentials
zur Laufzeit, aber nur für Repositories, die der Session ausdrücklich zugeordnet sind.
Öffentliches Lesen umgeht den Proxy-Check, Schreiben nicht.

## Lösung

1. GitHub-Konto mit dem Claude-Konto verbinden — einer der beiden Wege reicht:
   - Claude GitHub App unter https://github.com/apps/claude installieren und für das Repo freigeben
   - oder in der Claude Code CLI `/web-setup` ausführen (synchronisiert den lokalen `gh`-Token)
2. Das Repository der Session bzw. dem Projekt als **Source** hinzufügen
   (Oberfläche: „+" → GitHub → Repo wählen oder URL einfügen)
3. Push erneut versuchen

Rückfallweg ohne Freigabe: Dateien aus der Session herunterladen und lokal pushen.

## Sackgassen

- `git -c credential.helper=…` mit Platzhalter-Anmeldedaten — der Proxy prüft die
  Repo-Zuordnung, nicht das mitgeschickte Credential
- `curl https://api.github.com/repos/…` — dieselbe Sperre, andere Fehlermeldung
- Ein Personal Access Token in den Chat schreiben: **nicht tun**. Er steht dann dauerhaft
  im Sitzungsverlauf. Die Freigabe über die Oberfläche ist der vorgesehene Weg.

## Vorbeugung

- Vor Arbeitsbeginn einmal `git ls-remote` **und** einen Push auf einen Wegwerf-Branch testen
- Freigabe des Repos als erste Aufgabe einplanen, nicht erst wenn Ergebnisse anfallen

## Quellen

- https://code.claude.com/docs/en/claude-code-on-the-web — Abschnitt "GitHub authentication options", abgerufen 2026-08-19
