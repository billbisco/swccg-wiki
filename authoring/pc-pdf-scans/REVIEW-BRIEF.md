# PDF deck-sheet review (Players Committee scans) — helper brief

Work folder `$W` = /tmp/claude-0/-home-claude/89b0b907-d4b4-53cc-bc54-8fba9b724b03/scratchpad/pdfres
Read-only on the web: you may GET `https://wiki.swccg.com/api.php` to confirm card titles/sides. Never edit the wiki,
never commit, never touch files other than your own outputs.

These decks are ALREADY transcribed (an earlier pass) and live on the wiki as "numbered lists, not every card verified".
Your job: finish the identification so each deck can become a normal grouped decklist.

## Input (one per deck): `$W/tasks/<slug>.json`
Fields: title, player, side (DS|LS), event, stage, start, `lines` [{n, text, card, v}], `shield_lines`, notes
(UNSURE / other), `image` (full sheet PNG at 160 dpi), `pdf_path`, `pages`.

## Do, for each deck
1. Read `image` with the Read tool. For hard handwriting render a sharper crop yourself:
   `pdftoppm -r 300 -gray -png -f P -l P <pdf_path> $W/hi/<slug>-pP` then crop columns with PIL (python3) into `$W/hi/`.
   Budget about 3–6 image reads per deck.
2. Check EVERY line against the sheet, with extra care on lines named in UNSURE notes and lines with empty `card`.
   - `card` = the official card title as in the GEMP DB (`python3 $W/lookup.py "<text>" LIGHT|DARK`), e.g.
     "Jerjerrod" → "Moff Jerjerrod", "TTO" → "Tatooine Occupation", "K & D" → "Knowledge And Defense",
     "SRF Combo" → "Short Range Fighters & Watch Your Back!". Use the deck's own logic (objective, other cards,
     the side) to choose between versions. Never pick a card of the other side; if the sheet names a card that only
     exists for the other side, keep `card` "" (printed as written).
   - Episode I Tatooine/Naboo/Coruscant systems: write "Tatooine (EPI)" → card "Tatooine" and add "ep1": true on the
     line (the page builder picks the Episode I printing).
   - `v` = the (V) box on that line is ticked/marked. Re-check ticks on lines you change.
   - Ditto marks (″, 〃, ", "n", "same") repeat the line above. Crossed out + replacement → the replacement.
   - Combos written "X Combo"/"X & Y"/"X/Y": the combo card title from the DB.
   - If after a sharp crop you still cannot name the card: `card` "" and keep `text` as written. Bill: "if you can't
     figure it out, print it as written and move on." Don't guess wildly; don't stall.
3. Counts are as on the sheet. Never add or remove lines. Never invent cards.
4. Starting card `start`: the objective's full "Front / Back" title (or starting location if no objective).
5. Player/title stay as given (the wiki's canonical names). If the header shows something important (a different
   player, a different deck than the title), add a note only.

## Output: `$W/out/<slug>.json`
Same shape as the task file, with corrected `lines` / `shield_lines` / `start`, plus:
- `"reviewed": true`
- `"unresolved": [n, ...]` (line numbers still with card "", shields as "S<n>")
- `notes`: replace each old UNSURE note you settled with nothing (drop it); keep or add a short note for anything still
  doubtful ("UNSURE: line 52 'Fel' -> Baron Soontir Fel (only Fel card on Dark)" is fine when you are fairly sure).
Then run `python3 -c "import json;json.load(open('$W/out/<slug>.json'))"` to check it parses.

## Report back (short)
Per deck: slug, how many lines you changed, unresolved count, and any line you were unsure about. No long prose.
