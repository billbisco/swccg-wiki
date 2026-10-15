# 2015 European Championship Day 2 — Xerox batch

Batch: 70 deck pages (35 players, DS + LS) from the two PC Day 2 PDFs
(`SW-EC-2015-Day-2-Deck-Lists-Place-01-17.pdf`, `-18-35.pdf`).

- Transcriptions: `encyclopedia/pc-2015-events/transcribe_2015_ec_*.py` (Grok's Olson format).
- Generate (Windows worktree, Linux shell): `generate_2015_ec.py --xerox` through a wrapper that sets
  `update_gempc_start_fields.BP_PATH` to the local GEMP `card_blueprint_database.json` and adds
  `generate_2014_mpc.TYPE_OVERRIDE`: `combined attack`→Interrupt, `tatooine (coruscant)` and
  `tatooine (dark) (coruscant)`→Location.
- `finalize.py`: keeps existing stub titles (hub/player links), adds Player/Event/Side, keeps the stub's PC list
  Source + Preserved copy, cites the PDF with its Wayback capture, prints card links with no wiki page as plain text.
  `report.txt` lists the 20 decks whose sheet objective differs from the stub title, and the plain-text cards.
- Generated pages are gitignored; the ready-to-apply copy (pages + scans + PDFs) is in `C:\Users\gythe\.grok\claude-agent\y2015-ec-xerox\`.
- Apply: `python3 authoring/wiki_api_apply.py <batch>/titles.tsv --files <media>/* --summary "2015 EC Day 2 Xerox dest"`
  where `<media>` holds the 70 scan PNGs (`2015 European Championship <Player> DS|LS.png`, full-page 180 dpi
  grayscale) and the two PDFs as `2015 European Championship Day 2 Place 01-17.pdf` / `18-35.pdf`. Scans are not in git.
