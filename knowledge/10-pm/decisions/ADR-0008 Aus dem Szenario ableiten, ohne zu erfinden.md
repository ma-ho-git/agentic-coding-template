---
title: ADR-0008 Aus dem Szenario ableiten, ohne zu erfinden
type: decision
tags: [topic/requirements, topic/agents]
status: active
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-02-20
related: ["[[ADR-0005 Anforderungen als Pflicht vor dem Code]]", "[[Szenario]]", "[[T-0024 Szenario trägt die Anforderungserhebung]]", "[[REQ-0022 Das Szenario trägt die weitere Entwicklung]]"]
---

# ADR-0008 Aus dem Szenario ableiten, ohne zu erfinden

## Status

angenommen

## Kontext

- [[REQ-0022 Das Szenario trägt die weitere Entwicklung]] verlangt, dass die Erhebung ihre
  Vorschläge aus dem Szenario **ableitet**.
- Die härteste Regel in `/req-elicit` verbietet dem Agenten, eine Anforderung zu **erfinden**:
  „Eine erfundene Anforderung, die aussieht wie vereinbart, ist das schlimmstmögliche
  Ergebnis dieses Skills."
- Beides gleichzeitig ist nur scheinbar widersprüchlich — aber die Grenze verläuft nicht dort,
  wo man sie vermutet. **Jede** Ableitung fügt etwas hinzu: einen Schwellwert, ein Merkmal,
  eine Abgrenzung. Ein Szenario sagt „Dubletten raus", eine Anforderung muss sagen, woran
  eine Dublette erkannt wird. Das Hinzugefügte ist der Zweck der Erhebung, nicht ihr Fehler.
- Gefährlich ist nicht das Hinzufügen, sondern das **unsichtbare** Hinzufügen. Wenn hinterher
  niemand mehr unterscheiden kann, welcher Satz vom Nutzer stammt und welcher vom Agenten,
  ist die Rückverfolgbarkeit zwar formal vorhanden und inhaltlich wertlos.

## Optionen

| Option | Vorteil | Nachteil |
| --- | --- | --- |
| Frei ableiten, Szenario als Kontext | schnell, wenig Rückfragen | genau der unsichtbare Zusatz; der Agent ersetzt unbemerkt die Absicht des Nutzers |
| Nicht ableiten, Szenario nur als Hintergrundlektüre | keine Vermischung möglich | macht das Szenario zur Dekoration — der Aufwand des Nutzers verpufft |
| **Ableiten mit Zitatpflicht, benanntem Zusatz und Bestätigung** | Herkunft bleibt prüfbar, der Zusatz wird zur Frage statt zur Behauptung | eine Rückfrage mehr je Anforderung |

## Entscheidung

Ableiten ist erlaubt und erwünscht, in drei Schritten: **vorschlagen, zitieren, bestätigen.**

1. **Zitatpflicht.** Jede aus dem Szenario abgeleitete Anforderung nennt `[[Szenario]]` in
   `quelle` und zitiert die Stelle wörtlich unter `## Herkunft`, mit Abschnittsnamen.
2. **Zusatz benennen.** Der Agent sagt im selben Atemzug, welcher Teil vom Nutzer stammt und
   welchen er ergänzt hat — und stellt den Zusatz als Frage, nicht als Feststellung.
3. **Bestätigung vor `vereinbart`.** Unverändert: Der Agent bescheinigt sich nichts selbst.

Was das Szenario nicht beantwortet, wird normal erfragt. Eine Lücke wird nie mit etwas
gefüllt, das bloß zum Szenario passt.

## Konsequenzen

- Vorlage und Regeln bekommen den Abschnitt `## Herkunft`; `.claude/rules/requirements.md`
  führt die Kette ab dem Szenario.
- `tools/check_traceability.py` meldet ein Szenario, aus dem keine einzige Anforderung
  abgeleitet wurde — die Verbindung ist maschinell prüfbar.
- `/req-validate` prüft die Gegenrichtung: ein `## Herkunft`-Zitat, das im Szenario **nicht
  steht**, ist eine erfundene Ableitung und der schwerwiegendste Befund überhaupt — sie sieht
  vereinbart aus und ist es nicht.
- Die inhaltliche Abdeckung bleibt beim Menschen. Prosa lässt sich nicht maschinell
  abgleichen; wer das behauptet, verkauft ein falsches Sicherheitsgefühl.
- Eine Rückfrage mehr je Anforderung. Bewusst in Kauf genommen: Sie ist billiger als eine
  Anforderung, die niemand gestellt hat.

## Revidieren wenn

- Die Zitatpflicht bei langen Szenarien zur Formalie wird (immer derselbe Absatz zitiert).
  Dann fehlt eine feinere Gliederung des Szenarios, nicht die Pflicht.
- Sich zeigt, dass Nutzer die Rückfragen als Verhör empfinden. Dann ist die Bündelung der
  Fragen falsch, nicht die Bestätigung.
