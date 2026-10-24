# Brief: finish tournament-report data files (SWCCG wiki)

Bill 2026-10-24: every tournament report gets its own wiki article (with the report text verbatim and uncensored), and its results feed the tournament (hub) pages and player pages. You finish the data file; I build, apply and edit hubs. You do NOT build, apply, commit or push, and you only touch the `tournament-reports/<source>/<id>.json` files you are assigned.

Working dir: `/home/claude/swccg-wiki/authoring`. Python 3. Live page check: `python3 -c "import decktech_batch as b; print(b.live_text('Page Title') is not None)"` (prints the wikitext with `print(b.live_text(...))`).

## Input
`tournament-reports/decktech/<id>.json` already holds the fetched report: `posted_title` (the archive only keeps a URL slug), `byline`, `date` (posted), `body` (verbatim text). Read the whole body.

## Never change
`body`, `byline`, `posted_title`, `url`, `mirror`, `date`. The body is published verbatim: no censoring, no typo fixes, no trimming (Bill 2026-10-24).

## Fields you add (exact keys)
- `title`: readable report title. The archive URL slug lost punctuation ("rochester-ny-7-31-99"); rebuild it from the slug words only, restoring obvious capitals, apostrophes and dates ("Rochester NY 7-31-99", "Sokol's DCon 2000 Report"). Don't add words. No `# < > [ ] { } |` and no "/" (write dates with "-"). If the slug words are crude, still use them here but set `withhold_title: true` (see below).
- `withhold_title`: true only when the title is crude (swearing or euphemisms for it such as "Mofo", sexual or drug jokes, slurs, jokes about real tragedies). The page is then titled by author + event. The text inside the article stays uncensored.
- `author`: real name "First Last" (title case) from the byline; a prank or handle-only byline is credited by the handle. `author_page`: "existing" | "new" | "none" (none only when there is no name or handle). `author_link`: set only when the person page has a different title (e.g. accents); never a redirect.
- `event`: the wiki hub title for the event the report covers, e.g. "2000 Milford Grand Slam", "2001 New York State Championship", "1999 Decipher World Championship". Check [[List of SWCCG tournaments]] (`b.live_text("List of SWCCG tournaments")`) and the live hub. If no hub exists, propose a name in the house style `<year> <Place> <Event type>` and set `event_status: "new"`; existing hub → "existing"; an unnamed local / store event with no clear name → `event: null`, `event_status: "unnamed"` and describe it in `event_desc` (e.g. "a sanctioned tournament in Rochester, New York").
- `event_date`: ISO date (or "2000-04" / "2000") of the event, from the report (not the posting date). `event_site`: city/state/country as stated, or null. `event_type`: "Grand Slam" | "State Championship" | "Regional" | "DPC" | "World Championship" | "Local" | … as stated. `players`: number of players if stated, else null.
- `author_finish`: "1st" / "2nd" / "Top 8" / "13th" … as stated, else null. `author_record`: e.g. "4–2" (en dash) from the games, else null. `author_points`: the final tournament points / differential line if stated, e.g. "10 (+55)", else null.
- `games`: one entry per game, in order: `{"round": "1", "opponent": "Matt Quirk", "opponent_page": true|false, "author_side": "Dark"|"Light"|null, "author_deck": "Imperial Occupation" (short, as the report describes it) or null, "opponent_deck": "Throne Room mains" or null, "result": "Win"|"Loss"|"Tie"|null, "margin": "+4" / "−34" / "FW 15" as stated or null, "note": short or null}`. Round labels as the report has them ("1", "2", "Top 8 G1", "Final G2"). Opponent names as the report spells them, but use the real person page title when it clearly exists (check `b.live_text`), and then `opponent_page: true`. Don't guess full names that the report doesn't give.
- `decks`: the author's own decks as described: `[{"side": "Dark", "description": "Imperial Occupation", "deck_page": "<live deck page title>" or null}]`. Set `deck_page` only if a live DeckTech deck page is this exact deck (same author, same event/time). If the report includes a full decklist, say so in `notes` (don't dest it).
- `other_results`: placings for OTHER players that the report states (`[{"player": "Jason Stewart", "finish": "1st", "player_page": true|false}]`). Only what the report says.
- `summary`: one or two neutral sentences of fact: who, where, finish, record ("Kurycki finished 2nd of 14 with Imperial Occupation and a Revolution deck, going 5–1 and losing only to Jason Stewart.").
- `notes`: short factual list of judgment calls (event identification, uncertain names, mismatches with the hub, a deck list included, etc.).
- `multi_event`: true if the report covers more than one tournament; put the others in `side_events` (below).

## Every named player, every event (Bill 2026-10-24)
- **Small-world rule:** a named person is the same person as the wiki page of that name. Obvious misspellings of an existing page's name ("Dan Mailoux" / [[Dan Mailloux]], "Akessson") map to that page; note it. Use the page title as `opponent` / `player` and set `opponent_page` / `player_page` true.
- **Every player with a full name gets an article.** Give every opponent's full name whenever the report gives one (first name only → keep it, it gets no page). For each game also give `opponent_side` ("Dark"/"Light", the side opposite the author's) so the opponent's page can show what they played.
- **Every tournament gets a page.** Mentioned tournaments with no hub get `event_status: "new"` plus `event_format`, and end up on [[List of SWCCG tournaments]]. `event_format`: the GEMP format name the List uses for other events in the same month and region (e.g. "Premiere - Endor", "Premiere - Reflections II"); a sealed event uses the sealed format name the List uses. Also give `event_winner` if the report says who won.
- **Side events:** another tournament covered in the same report (a sealed event at Worlds, a Saturday-night open) goes in `side_events`: a list of objects with the same keys as the main event (`event`, `event_status`, `event_date`, `event_site`, `event_type`, `event_format`, `event_winner`, `players`, `author_finish`, `author_record`, `games`, `other_results`, `summary`), plus `parent`: the main event's hub title. Name it in house style, e.g. "1999 Decipher World Championship ECC Sealed".
- **New facts for existing hubs:** `hub_updates`: `[{"event": "<hub>", "field": "players"|"date"|"site", "value": "66"}]` for facts the live hub doesn't state yet.
- **Discrepancies:** `discrepancies`: `[{"event": "<hub>", "text": "Lush describes six Swiss rounds, but the hub and Brian Hunter's page say Hunter went 5–0."}]`. They are shown in the report article and on the hub.

## Discrepancies
If the report conflicts with what the live hub says (winner, date, place, player count), keep both: the hub/Decipher record stays the reference, and you add a `discrepancies` entry (Bill 2026-10-24: trust Decipher's records over a player's post until there is more evidence, and note the discrepancy).

## Report back (your final message)
For each id: title, author (+page status), event (+status), event date, author finish/record, number of games, decks, other results, and every judgment call / discrepancy. Compact.
