# Old PC deck-sheet PDFs (2007, 2010, 2011) → new wiki decklist pages

Built 2026-10-25, applied 2026-10-29 (Claude). **Status: LIVE** — 2,091 pages (992 created, 1,099 edited incl. File: pages), 31 PDFs, 899 scans; 0 errors, 0 conflicts, no new red links. Page list: `changed-pages-2026-10-29.md`. Uploads over 1.5 MB must go chunked (single uploads are capped at 2 MB).

These events had no wiki pages at all: 2007 MPC D1/D2, Endor/Kashyyyk Regionals, MA/NJ/ND States, Australian
Championship, US East Nationals D2; 2010 MPC D1/D2, Texas Mini Worlds D1/D2, US West Nationals D1/D2, US East
Nationals, Canadian Nationals, Dagobah/Malastare/Yavin 4 Regionals; 2011 MPC D1/D2, TMW D1/D2, US Nationals,
Yavin 4/Bespin/Tatooine Regionals, Minnesota States, Belgium/Luxembourg Regionals, German Nationals.
899 decks, 26 hubs, ~66 new person pages, ~168 person pages get rows, [[List of SWCCG tournaments]] rows,
new format page [[Premiere - Original VS12]] (2007 pre-August pool).

## Inputs
- PDFs: on Bill's PC `C:\Users\gythe\.grok\claude-agent\old-pdfs\` (res.starwarsccg.org `Resources/tournaments/Decklists/`
  and Wayback `phocadownload/2011…`). Copy each to `pdf/<stem>.pdf` (stems = keys of `events-*.json`, minus `#MN`;
  2011 files are named `ph_2011…` on the PC: drop `ph_`). The 2010 Dagobah PDF is truncated after page 13;
  `scans.py` uses page images from `img/2010_Regional_Dagobah_full/` (extract the 13 JPEGs from the PDF bytes) and
  `pkg.py` uploads a rebuilt 13-page PDF `pdf/2010_Regional_Dagobah_recovered.pdf` (PIL save_all of those images).
- Helper transcriptions: `out/G*/<stem>-p<N>.json` (brief: `BRIEF.md`; groups: `groups.txt`).
- Player names: `names-<year>.tsv` (last column = canonical wiki person; SKIP = left out). Rules: `name_rules.json`.
- Events (hub, stage, dates, sources, era): `events-<year>.json`; `event_overrides.json` moves 12 Bespin-PDF sheets
  headed "MN States" to the Minnesota hub.

## Build (cloud session)
1. `./make_all.sh 2007 2010 2011` → `final-<year>/` (deck pages) and `final-all/` (+ hubs, person edits, tournament
   list; writes `final-all/since.txt` for the edit-conflict guard). Card pages come from `../pc-pdf-scans/resolve_wiki.py`
   with era rules in `build.py`: a ticked (V) in 2010–11 links the Legacy Virtual Block page (image `VB…`/`VSh…`), in
   2007 the original Virtual Set page (`OVS…`); never a post-2014 `V0…/VS…` printing (`era_pick`, `era_fix`).
   "Same as yesterday" sheets apply their swaps to the Day 1 list (Luxembourg uses Belgium's list).
2. `python3 scans.py final-all` → `media/` (one PNG per deck, 130 dpi; ~310 MB).
3. `python3 pkg.py` → `pkg/` (pages incl. File: description pages, `media/`, `pdf/`, `all.tsv`, `ap.py`, `since.txt`).
4. `python3 redcheck.py pkg` → only the PDFs (uploaded in step 5) may be missing.

## Apply (Bill's PC shell, Holocron Claude; see ai-team-skills CLAUDE.md § Wiki publishing)
Copy `pkg/` to `C:\Users\gythe\.grok\claude-agent\old-apply\` (split tar < 25 MB per file), add
`wiki_api_apply.py` (from `../`), then repeat each until it prints DONE (time-boxed, re-runnable):
```
set -a; . ../wiki-bot-password.env; set +a
python3 ap.py files "PC decklist PDFs 2007–2011 (Holocron Claude)" pdf/*
python3 ap.py files "PC deck sheet scans 2007–2011 (Holocron Claude)" media/*
python3 ap.py pages "PC decklists 2007–2011 from the PC PDFs (Holocron Claude)" all.tsv
```
Then purge, re-run the red-link check on the live pages, and report every changed page URL to Bill.

## Open items for Bill
See `issues.md` (left-out sheets, name calls, cards the wiki lacks, unreachable sources).
