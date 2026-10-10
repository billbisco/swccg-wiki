Authoring helpers used to generate and apply pages on the live wiki (generators, Xerox transcribe apply scripts, QA).

The public backup of encyclopedia text is `../pages/`. Refresh that from production with `python ../tools/dump_live.py`.

## Running in the cloud (no Windows worktree needed)

`generate_decktech.py`, `generate_gpn_decks.py` and their inputs (`scomp-*.json`, `pc-cardlists/`, `card_title_map.json`, `decktech-inventory.json`, `decktech-posts/`, `gpn-decks/`, `gemp-import-gpn/`) live here. Verified 2026-10-10: running `python generate_decktech.py` from this folder reproduces the live 22701 pages byte-for-byte. Outputs go to `pages/` (the backup copy of live pages is `../pages/`). Apply on the VPS with `apply-tsv.sh` (scp the TSV + pages first). Keep this folder in sync with the Windows worktree `code-swccg1/wiki` when either side changes a generator.
