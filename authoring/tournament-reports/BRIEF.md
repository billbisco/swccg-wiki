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
- `event`: the wiki hub title for the event the report covers, e.g. "2000 Milford Grand Slam", "2001 New York State Championship", "1999 Decipher World Championship". Check [[List of SWCCG tournaments]] (`b.live_text("List of SWCCG tournaments")`) and the live hub. If no hub exists, propose a name in the house style `<year> <Place> <Event type>` and set `event_status: "new"`; existing hub → "existing"; an unnamed local / store event still gets a name (see "Every event is named" below) and its description in `event_desc` (e.g. "a sanctioned tournament in Rochester, New York").
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

## Every event is named; Objectives are linked (Bill 2026-10-24)
- **No unnamed events.** A local or store tournament without a proper name still gets an article: name it like the List's precedents, `<Month YYYY> <City> tournament` (e.g. "July 1999 Rochester tournament", "October 1998 Portsmouth tournament"), `event_status: "new"`, with `event_desc` kept as the description. Two same-month events in one city: add the store or day ("July 1999 Rochester tournament (Game Shop)"). Check the List first: the event may already exist under another name.
- **Objectives:** when a deck description names or clearly implies an Objective (HDADTJ, Hunt Down, Ralltiir Ops, Profit, Hidden Base, Throne Room mains is NOT an objective), give its exact two-sided Decipher page title: `author_objective` / `opponent_objective` on each game, and `objective` on each `decks` entry, e.g. "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe". Pick the version by context: the original and the (V) are different cards. Use the objective that existed and fits the event's date and format and the report's wording (e.g. Hunt Down And Destroy The Jedi (V) is Virtual Set 13, 2007, so a 1999–2002 report means the original). Check the page exists (`b.live_text`). The description text stays as the report has it; the link is added around it.

## Discrepancies
If the report conflicts with what the live hub says (winner, date, place, player count), keep both: the hub/Decipher record stays the reference, and you add a `discrepancies` entry (Bill 2026-10-24: trust Decipher's records over a player's post until there is more evidence, and note the discrepancy).

## Report back (your final message)
For each id: title, author (+page status), event (+status), event date, author finish/record, number of games, decks, other results, and every judgment call / discrepancy. Compact.

## Added 2026-10-25 (from batches 2–3)
- `author_played: false` when the author didn't play the main event (judge, staff, spectator); put their decks on the side events they did play.
- `event_parent`: the parent page of the main event when the report is mainly about a side event (e.g. "DecipherCon 2000").
- A side event's `parent` may be null (an earlier event the report mentions is not a side event).
- `hub_updates` may use `field: "winner"` (fills an Unknown winner), besides players / date / site.
- Names: a person known only by first name plus an initial ("Kevin W.") gets no page; write it as the report has it.
- Before inventing an event name, search the List for the same date and city; for repeated convention events use one hub per session, `<year> <Convention> <Decipher's event name> (<day> <Month>)`.
- Opponents: give `opponent_side`, and use the person page's exact title (check redirects: "Michael Kessling" → "Mike Kessling").
- Don't infer: no places from list order, no full names or winners taken from another report, no objective guessed from a vague deck name ("Speeder Ops", "Lightside OPS"). Keep the report's own words and put the inference in `notes`.
- Handles, team names and censored names get a parenthesis so they get no person page: "Bobbo Feet (DeckTech handle)", "Charlie's Angels (team: [[A]], [[B]])", "Rich Glass@#$% (surname censored in the archive)".
- Objective sets for reference: ISB Operations, Hunt Down And Destroy The Jedi, Hidden Base, Ralltiir Operations, Local Uprising, Imperial Occupation are Special Edition (1998); Quiet Mining Colony and This Deal Is Getting Worse All The Time are Enhanced Cloud City (Dec 1999); Court Of The Vile Gangster is Enhanced Jabba's Palace (Jan 2000). Check the objective page's `set=` when unsure.

## Added 2026-10-25 (batches 10–11)
- A place the report gives as "X or Y" ("4th, Kevin Wan or Alan Sagan") is recorded for neither player; put it in notes. A range the report states ("4th–6th") or a hedge on one player ("4th (I think)") is kept as written.
- A team ("Team Albany") is never `player_page` true.
- An author who did not play a side event: `author_played: false` on that side event.
- Before filling, check `tournament-reports/built.txt`: a key listed there is already published; only update it to match the live wiki.
- Several events in one city and month: every new one gets its day in the name; one already built keeps its live name (renaming a built event breaks links), so don't ask for a rename.
- Two reports with the same author and title (a weekly "Mirkwood Deadbody Style"): set `page_title` to "<Author> <Title> (<day month year>)" on each.
- A report that tells a sexual or degrading story about a real, named person, or is mostly abuse aimed at named people: don't fill it; tell me (I hold it for Bill).
- An unnamed opponent is `null` (put the report's words, e.g. "some guy", in the game note), never a name string; lowercase phrases are not names. (Batch 16 created a "Some guy" page by mistake.)
- A minor (a report says the player is a child) gets no person page: opponent `null`, the report's words in the game note.
- A name that the wiki has as a disambiguation page ("Paul Feldman"): map it to the right person or leave player_page false; never link the disambiguation page.
- Hearsay ("he won, I heard") and hedged finishes ("5th or 6th (I think)") are not recorded as results or hub winners; put them in notes.
- A sexual claim about a named real person ("X is a connoisseur of porn", "X and Y contracted STDs") or an insult aimed at one (suicide jokes, "bisexual midget") counts as degrading: hold the report.
