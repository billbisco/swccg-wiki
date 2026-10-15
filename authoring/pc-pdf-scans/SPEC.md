# PC decklist PDF scans → per-deck JSON (helpers)

Work folder `$P` = `/tmp/claude-0/-home-claude/694b9813-c77f-540d-8dd2-659ab64c4055/scratchpad/pg`.
Read-only on the web: you may query `https://wiki.swccg.com/api.php` (GET only) to confirm card titles. Never edit the wiki.

## Inputs
- Your PDF(s) in `$P/<name>.pdf`; pages already rendered at 110 dpi in `$P/img/<name>/p-NN.png` (or p-NNN.png).
  For hard handwriting render sharper crops yourself: `pdftoppm -r 250 -f N -l N -png $P/<name>.pdf $P/hi/<name>-N`
  then crop with PIL (left column / right column / header) into `$P/hi/`. Read images with the Read tool.
- Your stub list `$P/stubs-<group>.json`: the wiki pages that still need a decklist (title, player, side, event, stage).
  Player names there are the wiki's canonical spellings — use them exactly.
- Card titles: GEMP DB `/home/claude/swccg-gemp/src/gemp-swccg-cards/src/main/resources/card_blueprint_database.json`
  (field `title`, `side` LIGHT/DARK). Use `python3 $P/lookup.py "<fuzzy text>" LIGHT|DARK` to get the best title matches.

## Step 1 — page map
Each sheet is a "DECK LIST" form: header with LIGHT/DARK checkbox, Name, Username; numbered lines 1–60 (Card Title + (V)
checkbox) and Defensive Shields lines. Some decks span 2 pages; some PDFs start with standings/cover pages. Look at the
header of every page (crop the top ~20% to save reads) and write `$P/out/<group>/pagemap.tsv`:
`page<TAB>name as written<TAB>LIGHT|DARK<TAB>matched stub title or "-"`. Match names to the stub list (handwriting is
messy: "Chardy Arlands" = Charlie Arlandson). A deck whose player/side has no stub was already filled — skip it.

## Step 2 — transcribe each stub deck you found
One file per deck: `$P/out/<group>/<slug>.json` (slug = ascii lowercase of player + side), exactly:
```json
{"title": "<stub title>", "player": "...", "side": "DS|LS", "event": "...", "stage": "...",
 "pdf": "<name>.pdf", "page": 12, "pages": [12], "username": "",
 "start": "<objective full 'Front / Back' title, or starting location/interrupt if no objective>",
 "lines": [{"n": 1, "text": "Hoth", "card": "Hoth", "v": false}, ...],
 "shields": [{"n": 1, "text": "Your Insight Serves You Well", "card": "Your Insight Serves You Well", "v": true}, ...],
 "notes": ["UNSURE: line 47 \"Yoda Haz Yer Mouth\" -> Yoda, You Seek Yoda"]}
```
- `lines`: every filled numbered line in sheet order (normally 60). `text` = what is written (best reading); `card` =
  official card title (GEMP/wiki spelling) or "" if you cannot identify it; `v` = the (V) box is checked/marked.
  Ditto marks (″, 〃, ", "same") repeat the previous line's card. A crossed-out line with a replacement written → the
  replacement; crossed out with nothing → keep `text`, `card` "" and note it.
- Sheet slang → official title (e.g. "Qui-Gon w/ Stick" → "Qui-Gon Jinn With Lightsaber"? only if certain;
  "EBO" → "Echo Base Operations / ..."). Combos written as "X Combo" or "X & Y": use the combo card title from the DB.
- The objective: `card` = its full two-sided title from the DB/wiki ("Hidden Base / Systems Will Slip Through Your
  Fingers"). Episode I versions: "Tatooine (Coruscant)"-style titles exist on the wiki; give plain title, the generator
  handles editions.
- Never invent cards or counts. If a name is unreadable after one sharp crop, give your best guess in `card` and add an
  UNSURE note; if no guess, `card` "". Do not stall — finish every deck (Bill: always publish, quality pass later).
- If the sheet's starting objective disagrees with the stub title's archetype, transcribe the sheet and add a note
  `TITLE MISMATCH: wiki says X, sheet starts Y`.
- Budget: about 4–8 image reads per deck. Use 250-dpi column crops; don't re-read the same crop.

## When done
Run `python3 $P/check.py $P/out/<group>` and fix obvious problems. Return a short report: pages mapped, decks written
(count), stubs not found in the PDF (titles), and the number of UNSURE notes. No long prose.
