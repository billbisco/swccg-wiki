# World Championships / Tournaments cleanup (Bill 2026-10-30)

Applied as Holocron Claude on 2026-10-30:
- [[Championships]] moved to [[World Championships]] (redirect kept); new table built by `gen_wc.py` + `page.py` from the hub infoboxes.
- All 31 Worlds hubs rebuilt to `HUB-BRIEF.md` (drafts in `hubs/`, per-year notes `*.notes.md`, build scripts in `hub-scripts/`).
- [[Hall of Fame]] created (`Hall_of_Fame.wiki`, notes file has open points).
- Dated Virtual Block pools: 11 pages [[Premiere - Virtual Block 6.1]]–[[9.1]] (drafts in `../formats/drafts/`), `pool_map.tsv` (42 events → pool),
  `relink/` replaced [[Legacy Open]] with the dated pool on 2,802 pages; [[Legacy Open]] = fixed post-2014 pool only.
- [[List of SWCCG tournaments]] split: 1996–2001 → [[List of SWCCG tournaments in YYYY]] (`listsplit/split.py`); formats tools read all 7 pages.
- [[Tournaments]]: Worlds-specific sections moved to the 1998/2000 hubs.
