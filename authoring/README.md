Authoring helpers used to generate and apply pages on the live wiki (generators, Xerox transcribe apply scripts, QA).

The public backup of encyclopedia text is `../pages/`. Refresh that from production with `python ../tools/dump_live.py`.

## Running in the cloud (no Windows worktree needed)

`generate_decktech.py`, `generate_gpn_decks.py` and their inputs (`scomp-*.json`, `pc-cardlists/`, `card_title_map.json`, `decktech-inventory.json`, `decktech-posts/`, `gpn-decks/`, `gemp-import-gpn/`) live here. Verified 2026-10-10: running `python generate_decktech.py` from this folder reproduces the live 22701 pages byte-for-byte. Outputs go to `pages/` (the backup copy of live pages is `../pages/`). Apply on the VPS with `apply-tsv.sh` (scp the TSV + pages first). Keep this folder in sync with the Windows worktree `code-swccg1/wiki` when either side changes a generator.

## Style lint (run before saving any article)

`authoring/style_lint.py` checks wikitext against [[SWCCG Wiki:Style guide]]. Prose checks read the body only (refs, templates, files, galleries, categories, See also/References are stripped; External links is checked, minus its link titles). Citation checks read the whole page.

```
python3 authoring/style_lint.py "Page title"                 # live page vs its previous revision
python3 authoring/style_lint.py draft.wiki --title "Page"     # local draft vs live page
```

Flags: banned hedge/meta words (note, research, pending, inferred, reportedly, appears to, probably, unclear, …), headings named Gaps/Notes/Research/Open questions/Sources, captions over 12 words or describing the image (shows, visible, left, right, pictured, …), sentences over 30 words. Prints body word count vs previous revision. Exits 1 on any flag; fix all flags before saving. No login needed.

Exemptions (2026-10-14): `{| |}` tables are stripped before sentence and word checks; each line or list item is checked separately, and `."`/`.”` end a sentence; quoted speech is not scanned for banned words; sentences with 6+ commas (name lists) are not length-checked; list/sub-pages (title contains `/` or body starts "This page lists") may say "this page"/"we" and skip the length check; `== Sources ==` is allowed on decklist and event pages only.

Citation checks (Bill, 2026-10-20):
- `ARCHIVE`: every external URL on the page (`<ref>`, list items, body, tables, External links) needs a Preserved copy, a `https://web.archive.org/web/<14 digits>/<url>` or `https://archive.org/details/...` link. A URL inside a `<ref>` needs the copy inside that same `<ref>`. A URL elsewhere passes if its own line has a copy or the same URL has a Wayback copy anywhere on the page. Skipped: `wiki.swccg.com`, `swccg.com/images/` and archive links.
- `EMAIL`: personal email addresses anywhere in the page text, including `mailto:`. Passes: `@decipher.com`, Players Committee role addresses (`rules@starwarsccg.org`, …), and a line carrying an `<!-- email-ok: reason -->` comment for a defunct address Bill wants kept.
- `REF`: a `<ref>` with no URL and fewer than two words of source text (e.g. `<ref>None</ref>`).
- `HEADING 'Sources'`: deck/event pages are detected by category, from the wikitext plus the live page's categories when linting by title: Decklists, Dark Side decks, Light Side decks, GEMP importable decklists, Tournaments, Championships, World Championships, Events, Retro League. Every other page cites in References.

Tests: `python3 -m unittest discover -s authoring/tests` (fixtures are saved revisions of live pages).
