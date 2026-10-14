Authoring helpers used to generate and apply pages on the live wiki (generators, Xerox transcribe apply scripts, QA).

The public backup of encyclopedia text is `../pages/`. Refresh that from production with `python ../tools/dump_live.py`.

## Running in the cloud (no Windows worktree needed)

`generate_decktech.py`, `generate_gpn_decks.py` and their inputs (`scomp-*.json`, `pc-cardlists/`, `card_title_map.json`, `decktech-inventory.json`, `decktech-posts/`, `gpn-decks/`, `gemp-import-gpn/`) live here. Verified 2026-10-10: running `python generate_decktech.py` from this folder reproduces the live 22701 pages byte-for-byte. Outputs go to `pages/` (the backup copy of live pages is `../pages/`). Apply on the VPS with `apply-tsv.sh` (scp the TSV + pages first). Keep this folder in sync with the Windows worktree `code-swccg1/wiki` when either side changes a generator.

## Style lint (run before saving any article)

`authoring/style_lint.py` checks wikitext against [[SWCCG Wiki:Style guide]]. Body prose only (refs, templates, files, galleries, categories, See also/References are stripped).

```
python3 authoring/style_lint.py "Page title"                 # live page vs its previous revision
python3 authoring/style_lint.py draft.wiki --title "Page"     # local draft vs live page
```

Flags: banned hedge/meta words (note, research, pending, inferred, reportedly, appears to, probably, unclear, …), headings named Gaps/Notes/Research/Open questions/Sources, captions over 12 words or describing the image (shows, visible, left, right, pictured, …), sentences over 30 words. Prints body word count vs previous revision. Exits 1 on any flag; fix all flags before saving. No login needed.
