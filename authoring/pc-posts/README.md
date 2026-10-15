# PC deck posts → wiki decklist pages

Fills existing empty decklist stubs (2015–2017 PC events) from the Players Committee's per-deck posts
(`starwarsccg.org/wp/<slug>/`, raw Wayback captures). No OCR. Built 2026-10-15 (Claude).

1. **Fetch** (on Bill's PC; the cloud can't reach archive.org): CDX prefix query per event →
   `curl https://web.archive.org/web/<ts>id_/<url>` into `claude-agent\pc-posts-*\html\`.
2. `parse_posts.py <html_dir> <cdx_dir> parsed.json` — headings `X:`, `[X]`, `{X]`, bare `Starting (6)`;
   quantities `xN`, `(xN)`, `(Nx)`, `N x`; `(V)` and trailing ` v`; notes `(+3 effects)`, `(12 card start)`,
   `+15 Defensive Shields`, Record and comment sections skipped; headless posts read whole body (shields capped at 16).
3. `match.py parsed.json stubs.json decks.json` — existing stub title by player+side+stage; exact first, then fuzzy;
   `ALIAS` for known misspellings; side inferred from card sides when the post omits DS/LS.
4. `canon.py decks.json decks-canon.json` — keeps any name with a wiki page; Ep I tags → `X (Coruscant)` /
   `X (Dark) (Coruscant)`; `EXPLICIT` typo map; objective back-side variants resolved by wiki prefix (originals unless V);
   fuzzy ≥0.88 vs GEMP titles of that side. Logs `Posted X dested Y` per deck (stays off pages).
5. `gen_pc_decks.py` (run in the Windows worktree's Linux shell with `WIKI_WT`, `BP_PATH`; absolute paths) — EC 2015
   machinery, Open lookups, grouped by type.
6. `finalize_pc.py gen_dir decks-canon.json final` — Player/Event/Side, deck post + Wayback copy, stub's PC-list source,
   no Scan section, missing card pages printed as text.
7. `gemp_build.py decks-canon.json final_copy` — GEMP import file only when every main-deck card resolves (full pool;
   retired 2015 shields GEMP lacks are left out and listed in `gemp-report.txt`); adds the `GEMP Importable deck` line.
8. Apply on the PC as Holocron Claude (see ai-team-skills CLAUDE.md § Wiki publishing): chunked `apply_resilient.py`.
