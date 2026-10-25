# PC decklist PDF scans → wiki decklist pages (2016 Worlds/EC/TMW/EGP, 2017 EGP)

Built 2026-10-15 (Claude). For stubs whose only source is the Players Committee's scanned deck-sheet PDFs.

1. PDFs fetched on Bill's PC (Wayback `id_` / res.starwarsccg.org), uploaded to the wiki as
   `File:<Event> Day N Decklists[ <places>].pdf` (chunked upload). Pages rendered at 110 dpi.
2. Helpers follow `SPEC.md`: page map, then one JSON per stub deck with every numbered sheet line
   (`text` as written, `card` official title, `v`), shields, start, notes (`UNSURE: line N …`, `TITLE MISMATCH`, …).
   `lookup.py` (GEMP fuzzy title), `check.py` (counts, blanks, other-side, not-in-GEMP).
3. `assemble.py out decks.json` — aggregates cards; Goldenrod text → card "Goldenrod" (plain text on the wiki);
   drops (V) ticks on cards with no (V) version (`hasVirtualSuffix`); `verified` = no blank and no UNSURE/INCOMPLETE.
4. `../pc-posts/canon.py` → `gen_pc_decks.py` on the PC (grouped layout) → `finalize_pdf.py gen decks-canon.json final`:
   verified decks keep the grouped list (phase 4); others get the sheet's numbered list (phases 1–3) where UNSURE lines
   print as written, unlinked; Scan section (`File:<Event> <Stage> <Player> <DS|LS>.png`, page ref to the PDF);
   Sources = PDF original URL + Wayback.
5. `make_scans.py final/scans.tsv <pdf dir> final/media` — 130 dpi grayscale, multi-page stacked, upside-down scans
   turned (logo-corner darkness, else tesseract OSD).
6. `../pc-posts/gemp_build.py` on verified decks only, with `GEMP_TAKEN`.

## 2026-10-25 — second pass: numbered lists → grouped lists (all 123 done)

The 123 decks that went live as "numbered lines, not every card verified" were re-checked against the scans by 20
helpers (`REVIEW-BRIEF.md`; reviewed JSONs in `reviewed-2026-10-25/`), then rebuilt as grouped lists:
- `render_grouped.py <reviewed_dir> <final_dir>` fetches each live page and replaces only the Decklist section (plus
  the Starting Card CardLink). Card pages are resolved **side-aware** by `resolve_wiki.py` (DeckTech lesson: the old
  numbered pages linked `Endor (expansion)`, Light `Endor: Bunker` in Dark decks, etc.). (V) only where a (V) page
  exists; Episode I printings via `"ep1": true`; shields must land on a Defensive Shield page of that side (2015–16
  "Yavin Sentry", "Weapons Display"… are the (V) shields, Ultimatum/Ounee Ta the Reflections III shields).
- Not identified lines print as written under **Not identified** (134 lines; 30 are Light "Goldenrod" /
  "Jabba's Prize" shields, which have no Light Defensive Shield page on the wiki).
- GEMP files: `../pc-posts/gemp_build.py` (113 files; 10 decks skipped because a main-deck card is not in GEMP,
  e.g. Obi-Wan In Radiant VII). All 113 import cleanly (gemp_import_test.py --formats Open).
