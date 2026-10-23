# Brief: finish DeckTech deck data files (SWCCG wiki)

You finish the card "dest" (destination) for DeckTech posts so a wiki page can be built. You do NOT build, apply, commit or push anything, and you do not touch any file other than the `decktech-decks/<id>.json` files you are assigned.

Working dir: `/home/claude/swccg-wiki/authoring`. Python 3.

## Inputs per deck id
- Post: `python3 -c "import generate_decktech as gd; p=gd.split_dt_post(ID); print(p['author'],'|',p['title']); print(p['cards']); print(p['strategy'][:1500])"` and `grep -h '^Description\|^Tags' decktech-posts/ID.txt`
- Draft JSON (already exists): `decktech-decks/ID.json`
- Card lookup: `python3 -c "import decktech_batch as b; print(b.suggest('NAME','Dark'))"` → ('exact'|'nickname'|'fuzzy'|'?', title). Only an `exact` title is acceptable in the final file. Search the GEMP card DB for candidates: `gemp-data/card_blueprint_database.json` (list of dicts: title, side DARK/LIGHT, expansionSet, cardCategory; sets with cardId prefix ≥ 200 are later virtual sets — not legal in 2002 decks).
- Player page check: `python3 -c "import decktech_batch as b; print(b.live_text('First Last') is not None)"`

## Write the finished file with the helper
```python
import sys; sys.path.insert(0,'/home/claude'); from finish import finish
finish(ID, [(qty, "Exact Card Title", "posted text"), ...], **fields)
```
It overwrites `decktech-decks/ID.json`, prints `ID qty N not-exact [...]`. Every card must come back exact (the not-exact list must be empty, except cards you deliberately mark UNKNOWN).

Fields (see finished examples `decktech-decks/22243.json`, `22048.json`, `21986.json`, `22119.json`):
- `player`: real name "First Last" (title-case). `byline`: the post's author string as posted. `player_page`: "existing" if the page exists, else "new". If the name the user posts under is a film/celebrity/character name (e.g. 'Silent "Silent Bob" Bob'), that is still his name: `player` = that name, normal person page (Bill 2026-10-22). Every deck gets a player page (Bill 2026-10-22: "we have to have player pages"). A joke/prank byline is credited by the DeckTech handle (`player` = handle, page "new"/"existing"); report it. `player_page: "none"` only when the post carries no name or handle at all.
- `side`: "Dark" or "Light" (trust the cards over the DeckTech tag).
- `player_intro`: e.g. `"(DeckTech handle '''tk424''') posted a [[Light]] [[Objective Title|Short]] list on DeckTech in March 2002."` (only for new pages; for existing pages `"posted a [[Dark]] list on DeckTech."`).
- `starting`: {"card": objective (or starting location/card) or null, "interrupt": e.g. "Prepared Defenses"/"Podrace Prep" or null, "effect": e.g. "Fear Is My Ally"/"An Unusual Amount Of Fear" or null}. Heading For The Medical Frigate and Prepared Defenses are Interrupts → `starting.interrupt`. When several Effects start, leave `starting.effect` null}. Use exact titles.
- `shields`: Defensive Shields posted OUTSIDE the 60, as `[[1,"Exact Title","DEFENSIVE_SHIELD"], ...]` — only shields actually named. `shields_note`: say what the post said (e.g. "10 shields of your choice; none named").
- `types`: {"Title": "UNKNOWN"} for a posted name that matches no real card (shown as posted, left out of GEMP); {"Title": "DEVICE"} etc. only when the helper's type is wrong.
- `notes`: short factual list: qty if not 60 ("Qty 59 as published: …"), every non-obvious dest ("Posted X dested Y"), original-era (V) slips, duplicates, author edits not applied ("dested as posted").
- Do NOT set use_published_title unless the title is controversial (profanity, sexual or drug jokes, slurs, violence against people): then set `"use_published_title": false` and add a note "TITLE WITHHELD: <why>" so the lead can log it.

## Dest rules
- Dest every line to the card the player meant, in the 2002 card pool (Decipher sets through Theed Palace + Reflections III, plus Players Committee Virtual Set 1/2 "original (V) slips" when the post marks a card virtual: keys like "Luke Skywalker (V)", "Gold 1 (V)", "Sai'torr Kal Fas (V)", "Fusion Generator Supply Tanks (V) (Light|Dark)").
- Common shorthand: "w/stick" = With Lightsaber; "in ship" = pilot-in-ship cards (Zuckuss In Mist Hunter, Dengar In Punishing One, Bossk In Hound's Tooth, IG-88 In IG-2000, Boba Fett In Slave I); "EPP X" = X With Lightsaber/With Blaster…; "DB" = docking bay site; "Mob Points/YCHF" = You Cannot Hide Forever & Mobilization Points; "IAO/SP" = Imperial Arrest Order & Secret Plans; "Prep Def" = Prepared Defenses; "FIMA" = Fear Is My Ally; "AUAOF" = An Unusual Amount Of Fear; "HFTMF" = Heading For The Medical Frigate; combo cards use " & " (e.g. "Sense & Uncertain Is The Future"); objectives use their two-sided title "Front / Back".
- A Dark card on a Light list (or the reverse) is a dest error — find the side's real card (e.g. "Rebel Barrier" in a Dark deck → Imperial Barrier) and note it.
- Quantities: "x3", "(x3)", "3x", "3-Name" prefixes. Section headers are not cards. When the header counts disagree with the list, dest the list as posted and note the total.
- Never invent a card. If a name can't be matched with confidence, mark it UNKNOWN and note it.
- Keep posted text in the third tuple element verbatim (it becomes "posted: …").

## Report back (your final message)
For each id: the `finish` output line, total qty, side, player + page status, and every judgment call you made (dests you were unsure of, UNKNOWNs, withheld titles, prank names). Keep it compact.

## 2001 additions (batches 37–53; these override anything above)
- **Card pool by date.** These posts are Feb–Mar 2001: the pool is Decipher Premiere through Reflections II (Dec 2000). Tatooine came out 30 May 2001, Coruscant Aug 2001, Theed Palace Dec 2001; Defensive Shields (Reflections III) came later still. So in these lists there are **no Defensive Shields and no starting "shield" phase**: Secret Plans, Wise Advice, No Escape, Allegations Of Corruption, Battle Order, Resistance, Do Or Do Not, etc. are the older **Effects / Interrupts** of the same name — dest the Effect (the bare title / `(Dark)` page the helper gives), never the Reflections III shield. Leave `shields` empty and `shields_note` "The post names no Defensive Shields." Don't dest Players Committee virtual cards (none existed yet). If a list has Tatooine-set cards (pre-release lists), keep them; I set the format afterwards with era_format.py — leave `format` as drafted.
- **Never add cards not in the posted list** (exception: the poster says in the text that he left one off and names it — then add it and note it). Don't "fix" a 59/61 count; note "Qty N as published".
- "X or Y" lines (either card) are one row marked UNKNOWN with the posted text; note it.
- `starting.effect` / `starting.interrupt` only when the post itself names them as starting cards. (Prepared Defenses was in use by early 2001 — see 14510 — but only set it when the post lists it.)
- **Starting location** goes in `starting.card` when there is no objective.
- A deck posted for someone else is credited to the builder (player = builder, note who posted it).
- **Posted text is never edited** (descriptions and strategy stay as published, typos included). Only crude page TITLES change: titles like "WTF", "BICH", "@#$%", a swear word, sexual/drug jokes, slurs, jokes about a real person's race → `"use_published_title": false` + note "TITLE WITHHELD: <why>"; the page becomes `{Player} LS/DS`. A bare "@$$"/"A$$" in a title stays (precedent Bad@$$).
- **Title clashes:** if the same author already has a live deck with the same title (check `python3 -c "import decktech_batch as b; print(b.live_text('Player Name Title') is not None)"` with the page title the build would make) or two posts in your set share author+title, set `"dest_title": "{Player} {Title} LS"` / `DS` (or with the objective's short name). Mojibake titles get a clean `dest_title`.
- **Reposts and joke posts:** if a post is an exact/near repost of another post by the same author (same list), or has no real list (joke), DON'T finish it: report the id and reason ("repost of NNNNN" / "joke, no list") and I will skip it.
- **Tournament decks:** if the post says the list was played at a named event (won, placed, went X–Y at "Ohio State Championship", "Meriden", a DPC, Regionals…), set `"kind": "tournament"`, `"event"`: your best hub name in the form `2001 <Event Name>` (e.g. "2001 Meriden Tournament", "2001 Texas State Championship"), `"finish"`: "1st"/"2nd"/"Top 8"/"3–1" as stated or null, and a `player_note` quoting what the post says (date, place, record). A reworked/"improved" version of an event deck stays tournament with a player_note saying it may differ. Report every tournament deck with event + date + the post's exact words so I can create/extend the hub. Otherwise `"kind": "general"`, event/finish null.
- **Player names:** "First Last" from the byline; keep diacritics as posted when clearly the person's name. Check the player page (`live_text`) for `player_page`. A same-name existing page with no 2001 link is fine to use; mention it in your report.
- Look at a finished example from the last batch before you start: `decktech-decks/14510.json` (general) and `decktech-decks/14524.json` (tournament).
- Only edit your assigned `decktech-decks/<id>.json` files. Don't run build/apply/git.

## 2026-10-22 additions
- **Event hubs:** before naming an event, search the wiki for it (`python3 -c "import decktech_batch as b; print(b.live_text('2001 X'))"` and try the city name, e.g. "Brugge" found [[2001 Brugge Belgian Open]]). Use the existing hub title and the existing player page spelling (Juliën Riviëre). If Decipher's Deck Designs already published the player's list for that event and the post is the same deck, file the post as general with a note pointing to that page.
- A list reworked months after the event ("V2.0", "rebuilt since") stays general with a player_note quoting the result.
- Wrong-side generic sites/systems (bare "Tatooine: Docking Bay 94" on a Dark list) are fixed afterwards by fix_card_pages.py — fine to leave the bare title the helper returns.
- Before you start, check each id is not already live: `python3 -c "import decktech_batch as b; print(b.live_text('<Player> <Title>'))"`. If a live page already cites this post id, don't finish it; report "already live".

## 2026-10-22 (evening) additions
- `finish()` now keeps the posted name for rows you pass as `types={"Name": "UNKNOWN"}` — no need to patch them afterwards. (Copy of the helper: `authoring/dt_finish_helper.py`.)
- "Grabber"/"Grabbler" in early-2001 lists: UNKNOWN (Allegations Of Corruption is a Coruscant card, Aug 2001).
- Plain "Boba Fett" is a disambiguation page: use "Boba Fett (Special Edition)" or "Boba Fett (Cloud City)" when the post says which (SE / CC); otherwise use "Boba Fett (Cloud City)" (Bill 2026-10-22: most likely the CC card, and GEMP already maps plain Boba Fett to Cloud City 5_91).
- `player_intro` on existing pages may use the full 14510 form (handle + objective link + month); that's fine.
- Byline with initials only (`M "ISBOPS" C`, "R. Smith"): `player` = the initials as posted ("M C", "R. Smith"), normal player page (Bill 2026-10-22).
- GEMP-only titles with no wiki page: "Tarkin" → Grand Moff Tarkin; "Han" (Jedi Pack) → Han (Jedi Pack); "Threepio" (Endor) → Threepio (Endor); "Artoo" (Jabba's Palace) → Artoo (Jabba's Palace).
- Bare "Luke"/"Leia"/"Vader" in 2001 lists: Luke Skywalker / Leia Organa / Darth Vader (the GEMP titles "Luke", "Leia", "Vader" have no wiki pages).
