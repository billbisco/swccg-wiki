# World Championship hub rebuild — helper brief (Bill 2026-10-30)

Goal: every World Championship hub on wiki.swccg.com (1996–2026) gets ONE standard layout, correct facts, and
every published decklist in finish order. You DRAFT full replacement page text; you do NOT edit the wiki, commit, or post.
Read-only web: GET https://wiki.swccg.com/api.php (live page text, backlinks, file search, card titles).

Folder C = /tmp/claude-0/-home-claude/89b0b907-d4b4-53cc-bc54-8fba9b724b03/scratchpad/champ
- Current hub text: C/hub_<year>_*.wiki (re-fetch live before drafting; live text wins if it changed).
- Facts with sources: C/worlds_facts.json, problems: C/worlds_issues.md (READ BOTH). 2026 extras: C/w26_extra/results.md,
  slack.md, photos.json; 2026 photos uploaded as File:2026 World Championship <subject>.jpg (list in C/w26_extra/photos.json
  picks + "File:2026 World Championship Brian Fred champion.jpg").
- Card pools for 2009–2014: C/pool_map.tsv (event → "Premiere - Virtual Block N.N"). Those pages are being created now; link
  them. 2002–2008 use the existing "Premiere - Original VSn" pages; 1996–2001 the existing "Premiere - <set>" pages; 2015+ [[Open]].
  Never write [[Legacy Open]] for a 2009–2014 event (that is the post-2014 fixed format).
- Hub coverage check: C/hub_coverage.json (deck pages linking each hub). Find ALL deck pages for the year: backlinks of the hub
  + prefixsearch of "<year> World Championship", "<year> Worlds", "<year> Decipher World Championship" + Category:Decklists.

## Layout (exact order)
1. Infobox at top, this markup (omit a row only when truly unknown):
```
{| class="wikitable expansion-infobox" style="float:right; margin:0 0 1em 1em; width:300px;"
! colspan="2" | <Year> World Championship
|-
| colspan="2" style="text-align:center;" | [[File:<champion photo>|280px]]<br/><small>caption</small>
|-
! Edition
| <Nth> (count 1996 as the 1st: 2002 = 7th, 2025 = 30th, 2026 = 31st)
|-
! Organizer
| [[Decipher]] / [[Players Committee]]
|-
! Dates
| <full event dates> (constructed <days>)
|-
! Venue
| <venue>, <city>, <state/country> (<convention> if any)
|-
! Format
| [[<pool page>]]
|-
! Players
| <n> (<which day> if that is what is known)
|-
! Champion
| [[<champion>]]
|-
! Runner-up
| [[<runner-up>]]
|-
! Previous / Next
| [[<prev year hub>|<prev year>]] · [[<next year hub>|<next year>]]
|}
```
2. Lead (2–5 sentences): edition, where/when, field size, champion def. runner-up (and winning decks if known), anything notable
   (Hall of Fame inductees announced there, back-to-back titles). Keep existing sourced narrative — move it into the right
   sections, never delete sourced facts; you may tighten wording.
3. `== Results ==` — ONE table in finish order: `! Place !! Player !! Dark !! Light` with BOTH of a player's decks on the
   same row (deck links `[[deck page|deck name]]`, "—" if none). Top 8 / Day 3 rows first; ties as "5–8". Prize column only if
   sourced. Then, if published, `=== Top 8 bracket ===` (game results as posted; say what was not published).
4. `== Day 2 ==` / `== Day 1 ==` standings tables when published (same columns; deck links for every deck page that exists).
   Any deck page for that year not placed in a table goes into `== Other published decklists ==` (stage, player, Dark, Light),
   sorted by stage then player. EVERY deck page for the year must be linked exactly once on the hub (check!).
5. `== Side events ==` (team tournament, consolation, Hall of Fame inductions, others) — only sourced.
6. `== Photographs ==` `<gallery>` of every relevant File: (event, venue, champion, trophy) with captions.
7. `== See also ==` — [[World Championships]], previous/next Worlds, the format page, convention page if any, [[List of SWCCG tournaments]].
8. `== Sources ==` bullets (keep all existing ones, add new), then the existing references block
   `{{#if:1|<nowiki />\n<h2>References</h2>\n<references />}}`, then categories: [[Category:Tournaments]]
   [[Category:Championships]] [[Category:World Championships]] [[Category:<year>]].

Rules: every fact sourced (inline <ref> or Sources bullet, reuse existing named refs); Bill's correction in worlds_issues.md
wins over old hub text; where sources disagree, state both briefly with refs. Don't invent places, dates or deck names.
Player links must be existing person pages (check; use the page title, e.g. [[Jonny Chu|Johnny Chu]] only if written so).

## Output
`C/hubs_draft/<Year>_World_Championship.wiki` (Decipher years: `<Year>_Decipher_World_Championship.wiki`), plus
`C/hubs_draft/<year>.notes.md`: what changed, facts added (with source), deck pages linked (count = all deck pages for the
year), and anything unresolved. Report a short per-year summary.
