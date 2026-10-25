# Old Players Committee deck sheets (2007–2010 PDFs) → per-deck JSON — helper brief

Work folder `$W` = /tmp/claude-0/-home-claude/89b0b907-d4b4-53cc-bc54-8fba9b724b03/scratchpad/old
Read-only on the web: you may GET `https://wiki.swccg.com/api.php` to confirm card titles/sides. Never edit the wiki,
never commit, never write outside `$W/out/<your group>/` and `$W/hi/`.

These are scanned tournament deck sheets that have never been transcribed. Nothing for these events exists on the wiki
yet. Your job is a faithful transcription of every deck in your page range; the page builder does naming and linking.

## Inputs
- Your group line in `$W/groups.txt`: `G<n> <pdf stem> <first page> <last page>`.
- PDF: `$W/pdf/<stem>.pdf`; pages at 110 dpi: `$W/img/<stem>/p-NN.png` (or `p-NNN.png` — check with ls).
- Some PDFs have a typed text layer: `pdftotext -f N -l N -layout $W/pdf/<stem>.pdf -` can help (verify against image).
- Card titles: `python3 $W/lookup.py "<fuzzy text>" LIGHT|DARK` (GEMP DB titles). Wiki API for anything GEMP lacks.

## Page range rules
- A deck may span 2 pages. If your first page is a continuation of a deck that started before your range, skip it
  (the previous group owns it). If your last page starts a deck that continues on the next page, read that next page
  too and finish the deck.
- Non-deck pages (cover, standings, pairings, notes) → record in the page map as `type` "other" with a one-line
  summary; if it holds standings/results (places, records, names), transcribe them into `results.json` (below).

## Step 1 — page map `$W/out/<G>/pagemap.tsv`
`page<TAB>type(deck|cont|other)<TAB>name as written<TAB>username<TAB>LIGHT|DARK|?<TAB>deck name as written<TAB>event as written`
Crop the header (top ~20%) at higher dpi when the name is hard to read.

## Step 2 — one JSON per deck: `$W/out/<G>/<stem>-p<first page>.json`
```json
{"pdf": "<stem>", "pages": [12, 13], "name_written": "J. Chu", "username": "jonnychu", "side": "DS|LS",
 "deck_name": "as written or \"\"", "event_written": "Texas 2010 Day 2", "date_written": "",
 "start": "<objective full 'Front / Back' title, or starting location/interrupt if no objective>",
 "lines": [{"n": 1, "text": "Hoth", "card": "Hoth", "v": false}, ...],
 "shields": [{"n": 1, "text": "Your Insight Serves You Well", "card": "Your Insight Serves You Well", "v": true}],
 "same_as": "", "changes": [],
 "notes": ["UNSURE: line 47 \"Yoda Haz Yer Mouth\" -> Yoda, You Seek Yoda"]}
```
- `lines`: every filled numbered line in sheet order (normally 60). `text` = what is written (best reading). `card` =
  official title (GEMP/wiki spelling) or "" if you cannot identify it. `v` = the (V) box on that line is ticked.
  Ditto marks (″, 〃, ", "same", "n") repeat the previous line's card. Crossed out + replacement → the replacement.
- Combos ("X Combo", "X & Y", "X/Y") → the combo card title from the DB. Objectives → full "Front / Back" title.
- Episode I systems written as such ("Tatooine (EPI)", "Coruscant (Ep1)") → card plain title and `"ep1": true`.
- Never pick a card of the other side; a card that only exists for the other side → `card` "" (printed as written).
- Sheet slang: use the deck's own logic (objective, other cards, side) to choose ("AFA" → "Anger, Fear, Aggression",
  "SRF Combo" → "Short Range Fighters & Watch Your Back!", "Obi's Saber" → "Obi-Wan's Lightsaber", "TTO" →
  "Tatooine Occupation", "K&D" → "Knowledge And Defense", "Sense"/"Alter" plain titles).
- **"Same deck as yesterday" / changes sheets** (Day 2 sheets that only list swaps, e.g. "Short Range Combo →
  Cold Feet V"): set `"same_as": "yesterday"`, put each swap in `changes` as
  `{"out": "<card>", "in": "<card>", "v_in": true|false, "text": "as written", "shield": false}`, and leave `lines` with
  only what is literally written. The builder applies the swaps to that player's Day 1 sheet.
- If after one sharp crop you still cannot name the card: `card` "" and keep `text`. Bill: "if you can't figure it out,
  print it as written and move on." Don't guess wildly; don't stall. Never invent cards or counts.
- Sharp crops: `pdftoppm -r 250 -gray -png -f N -l N $W/pdf/<stem>.pdf $W/hi/<G>-pN` then crop the left column /
  right column / header with PIL into `$W/hi/`. Budget about 4–8 image reads per deck.

## results.json (only if your pages contain standings)
`$W/out/<G>/results.json`: `{"pages":[..], "rows":[{"place":1,"name_written":"...","record":"...","notes":""}]}`

## When done
Run `python3 -c "import json,glob;[json.load(open(f)) for f in glob.glob('$W/out/<G>/*.json')]"`.
Report back (short): pages mapped, decks written, other pages (what they are), UNSURE count, anything odd
(e.g. team event, two names on one sheet, sheet with no name). No long prose.
