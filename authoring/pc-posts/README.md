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

## Wave 3 (2017–2020, 2026-10-15)

- Posts fetched per event folder (`claude-agent\pc-posts-wave3\<event>\html`); event pages' deck links, or a site-wide CDX
  search where the event page capture had none (2017 MPC/Worlds/EGP). `SLUG_EVENT=slug-event-wave3.json` maps slug → event.
- 2018+ posts use the Beaver Builder theme (`fl-module-fl-post-content`); `parse_posts.py` handles it, typo headings,
  `(N total)`, `(Ref N)`, inner `(xN)`, site footer lines.
- `gemp_build.py`: set `GEMP_TAKEN=<file of names already on the wiki>` so a new batch never reuses (overwrites) another
  batch's GEMP file name. Dedupe now compares the final cleaned name (wave 2 had one shared name; fixed and republished).
- 681 of the 800 unmatched wave-3 posts belong to decks that already had full pages (Grok's earlier work); the other 119
  have no page yet (quality pass).

## Wave 4 (live PC site via Chrome, 2026-10-15)

- The 2017–2020 per-deck pages that Wayback never captured (e.g. 2017 Worlds Day 2) are live on starwarsccg.org behind
  Cloudflare. Read them through Claude in Chrome (Bill's real browser): in-page `fetch()` of each event page's deck
  links, body = `.fl-module-fl-post-content .fl-module-content` (or `.entry-content`), saved as one JSON download
  (`pc-deck-posts-2017-2020.json`, Bill-approved) → wrapped as `<title>…</title><div class="entry-content">…` HTML.
- `match.py` aliases: jonas-hagen→Nørregaard, gyorgy-bill→Póra, kent-l→Larsen, pete-the-welsh→Rowlands,
  casper-jorgenson→Jørgensen; "Drops" stubs accept any posted stage.
- `finalize_pc.py` now also resolves front-only objective names on the Starting Card line (and case variants).

## Wave 5 (live PC site via FlareSolverr, 2026-10-29) — LIVE

- 43 empty 2015–2018 stubs whose only source was a per-deck PC post. Posts fetched with FlareSolverr on the gemp
  server (loopback `127.0.0.1:8191`, reached over SSH) — `/wp/` URLs redirect to a landing page, so fetch without `/wp/`.
- `wave5/fill.py`: `parse_posts.parse` + `canon.fix` + the era-aware resolver from `../pc-pdf-old/build.py` (modern era:
  shortest title, Legacy VB/VSh/OVS printings only when nothing else), title-case retry, a few typo fixes (`EXTRA`),
  unheaded opening lines taken as the starting cards. Inserts `== Decklist ==` before See also and the deck post as the
  first Source. Unmatched shields print as text under Defensive Shield (Goldenrod, as on earlier pages); other unmatched
  lines under "Not identified". `report.txt` = card counts and calls. Starting Card red links were swapped for the
  objective's CardLink (11 pages). Page list: `wave5/changed-pages-2026-10-29.md`.

## Wave 6 (audit + live PC site, 2026-11-04) — LIVE

- Inventory: Wayback CDX (4,257 deck posts) + the live site's Yoast post sitemaps via FlareSolverr (8,936 posts, ~7,600 deck posts).
  1,246 candidates (uncited or ambiguous) were fetched through the WordPress REST API (`/wp-json/wp/v2/posts?slug=…`, 15 per call).
- `wave6/compare.py` renders each post (`render.py`, wave-5 resolver) and compares its card multiset with the player's
  decklist pages of that year; `classify.py` = COVERED only when a page of the same event + same player has ≥85% of
  the cards (≥70% at the same stage). Event aliases: Seattle = EGP, Boston Winter Classic = BWC, PC20, 23OCS/T8, Outrider eur/usa/III/IV.
- Result: 970 covered, 256 missing, 20 no longer on the site. `build.py` → `split.py` → batch A (139, named from the
  player's own page at the event, `hubrows.py` adds hub + player rows, `publish.py`) and batch B (finished by four
  agents: 2022 / retro / 2023-26 / early, `publish_merge.py` 3-way merges hub/player edits against live).
- Live: 223 new deck pages, 22 retro (2021 Worlds Throwback) lists corrected from the posts, 8 existing pages got the
  deck post as a source, new hub [[2026 Retro World Championship]], Tatooine section on [[2026 Regional Championships]],
  222 GEMP files (built from the rendered card list; `gemp_importable` now escapes quotes in titles).
- Lessons: `parse_wiki_cards` needs an `Nx` quantity on every line (do not use it on pages with single copies);
  GEMP titles carry subtitles the wiki drops ("BB-8 (Beebee-Ate)") → `build.gemp_xml` BASE: fallback.
