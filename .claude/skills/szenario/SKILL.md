---
description: Capture the user's project as a scenario, in their own words, before requirements are elicited. Offers short beginner guidance on what a scenario should contain, lets the user narrate freely, and sorts it into knowledge/05-requirements/szenario.md. Use at the very start of a project, when /bootstrap offers it, or whenever a scenario is added later.
allowed-tools: Read, Glob, Grep, Write, Edit
---

# Capture the scenario

**Optional. Offer it once, take no for an answer.**

A scenario is the user's own account of what they want. It is not a requirement and not a
vision — it is the raw material both are derived from. Its whole value is that it is in
*their* words: everything a later step derives has to point back here.

Rules: `.claude/rules/requirements.md`. Stance: same as `/req-elicit` — explain before
asking, propose instead of interrogating, and never fill a gap yourself.

## 1. Offer it

Ask once, plainly, and make the cheap path visible:

> Bevor wir Anforderungen sortieren: Magst du in eigenen Worten erzählen, was du vorhast?
> Kein Formular — schreib drauflos, ich ordne das anschließend und frage nach, wo etwas
> fehlt. Wenn du lieber direkt loslegst, ist das auch in Ordnung.

**No means no.** Go straight to `/req-elicit` and say that the scenario can be added later
at any time. Do not ask twice, do not reframe the offer as a warning.

If the user has already described the project in this conversation, do not make them repeat
it. Say that you will use what they wrote, sort it, and read it back.

## 2. The help — show it once, keep it short

Only when the user wants guidance, or writes two lines and stalls. This is a checklist to
notice gaps, **not a form to fill in**. Show it as one block:

> **Das gehört rein:**
> - **Wer und wann** — wer benutzt das, und was löst es aus?
>   „Ich selbst, immer montags, wenn der Export aus dem Shop kommt."
> - **Ablauf** — was passiert im Normalfall, Schritt für Schritt?
>   „Datei einlesen, Dubletten raus, nach Region sortieren, als Tabelle speichern."
> - **Ergebnis** — woran merkst du, dass es geklappt hat?
>   „Eine Datei, die ich ohne Nacharbeit in Excel öffnen kann."
>
> **Das hilft zusätzlich sehr:**
> - **Was schiefgehen kann** — „Manchmal ist die Datei leer, manchmal doppelt so groß."
> - **Mengen und Häufigkeit** — „5.000 Zeilen, einmal pro Woche."
> - **Bestehende Systeme** — „Kommt aus Shopware, muss nach DATEV."
> - **Was nicht passieren darf** — „Kundennamen dürfen das Haus nicht verlassen."

Then stop explaining and let them write.

The last four look optional and are not: *was schiefgehen kann* is the only place a beginner
ever mentions failure, and *was nicht passieren darf* is usually the only hint at security
and legal duties. If they are missing, ask for them by name — one at a time.

## 3. Sort it, read it back

Write what the user said into `knowledge/05-requirements/szenario.md`, using
`knowledge/90-meta/templates/szenario.md`. Then read the result back in three or four lines
and ask whether you understood it correctly.

**Keep their wording.** Reorder, group, remove repetition — but do not upgrade their words
into technical terms. „Die Liste ist manchmal kaputt" stays that; it does not become
„inkonsistente Eingabedaten". The precise term belongs in the requirement derived from it,
not here.

## 4. Gaps stay gaps

You will notice missing pieces. Ask about them — once, in the user's language, with a
proposal to react to:

> Was soll denn passieren, wenn die Datei mal gar nicht ankommt? Häufig will man dann eine
> Meldung und keinen stillen Abbruch. Passt das, oder ist das bei dir anders?

„Weiß ich nicht" is a complete answer. It goes under **Offene Punkte** — never into the body
as an assumption. A scenario that contains sentences the user never said is worse than a
short one, because everything downstream will be derived from those sentences.

## 5. Hand over

Say what happens next, in one sentence: the scenario is now the basis for `/req-elicit`,
each requirement derived from it will quote the passage it came from, and the user confirms
every requirement before it counts as agreed.

Then run `/req-elicit`.

## Never

- Make the scenario mandatory, or ask a second time after a no.
- Write a sentence into the scenario that the user did not say.
- Turn the help into an interrogation — it is a checklist for you, not a questionnaire.
- Replace the user's words with technical vocabulary.
- Derive requirements here. This skill captures; `/req-elicit` derives.
