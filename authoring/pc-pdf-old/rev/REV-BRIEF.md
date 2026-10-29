# Second pass: unidentified lines on the live 2007/2010/2011 decklists — helper brief

Work folder `$W` = /tmp/claude-0/-home-claude/89b0b907-d4b4-53cc-bc54-8fba9b724b03/scratchpad/old
Read-only on the web (GET/POST queries to https://wiki.swccg.com/api.php only). Never edit the wiki, never commit,
never touch `out/` — write only your own `rev/<R>.out.json` and crops in `hi/rev-<R>-*`.

These decks are live; a few lines on each could not be linked and print as written under "Not identified".
Your task file `rev/<R>.json` lists them: per deck `title`, `side` (DS/LS), `source` (the transcription JSON),
`pdf` + `pages` (the scanned sheet), and `lines` = [{n, text, card_tried}] (n = line number in the source JSON's
`lines`; "S<n>" means shield n).

## For each line
1. Look at the sheet: `pdftoppm -r 250 -gray -png -f P -l P $W/<pdf> $W/hi/rev-<R>-<x>` and crop the line's area with
   PIL (the source JSON has the other lines, so you can find the position by neighbouring cards). Budget ~2 reads/line.
   (2010 Dagobah: the PDF is damaged; use `$W/img/2010_Regional_Dagobah_full/p-NN.png`.)
2. Decide the card. Check titles with `python3 $W/wikicheck.py "<start of title>" DS|LS` (lists wiki card pages of that
   side with type/image). The card must exist on the wiki for the deck's side. Common causes: a misread word, a
   nickname ("TRM", "EPP Obi", "HCF" = Han, Chewie And The Falcon), a missing "!" or "?", a combo written as two names.
   Period: 2007 = Decipher + original Virtual Sets; 2010–11 = Decipher + Legacy Virtual Blocks.
3. If still not identifiable, or the only matching card is for the other side, leave it (card "").
   Bill: "if you can't figure it out, print it as written and move on." Never invent.

## Output `rev/<R>.out.json`
```json
[{"source": "out/G5/2010_MPC_D1-p92.json", "fixes": [
   {"n": 33, "shield": false, "text": "Lando w/ Gun", "card": "Lando With Blaster Pistol", "v": false, "why": "sheet reads 'Lando w/ Gun'; only LS Lando with a gun"}]}]
```
- One entry per source file you changed. `n` is the line's `n` in the source (`"shield": true` for S<n>, n = shield n).
- `card` = exact wiki base title (no "(Dark)"/"(V)" suffix; set `v` true if the (V) box is ticked/written).
- Include only lines you resolved. Then `python3 -c "import json;json.load(open('$W/rev/<R>.out.json'))"`.
Report: lines resolved / left, one line per notable call.
