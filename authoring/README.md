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

Flags: banned hedge/meta words (note, research, pending, inferred, reportedly, appears to, probably, unclear, …), headings named Gaps/Notes/Research/Open questions/Sources, captions over 12 words or describing the image (shows, visible, left, right, pictured, …). No sentence- or quote-length limit (Bill, 2026-10-26): clarity and full understanding come first. Prints body word count vs previous revision. Exits 1 on any flag; fix all flags before saving. No login needed.

Exemptions (2026-10-14): `{| |}` tables are stripped before the banned-word and word-count checks; quoted speech is not scanned for banned words; list/sub-pages (title contains `/` or body starts "This page lists") may say "this page"/"we"; `== Sources ==` is allowed on decklist, event, card and set-table pages only.

Citation checks (Bill, 2026-10-20):
- `ARCHIVE`: every external URL on the page (`<ref>`, list items, body, tables, External links) needs a Preserved copy, a `https://web.archive.org/web/<14 digits>/<url>` or `https://archive.org/details/...` link. A URL inside a `<ref>` needs the copy inside that same `<ref>`. A URL elsewhere passes if its own line has a copy or the same URL has a Wayback copy anywhere on the page. Skipped: `wiki.swccg.com`, `swccg.com/images/` and archive links. **Exempt: the Main Page** (Chief, 2026-10-20): its body links are navigation to live resources, not citations, and Preserved copies stay out of body text. Lint it by title (`style_lint.py "Main Page"` or `--title "Main Page"`); a draft file without `--title` is still checked. Its URLs are still queued in `ops/wayback/queue.txt` (Cloudflare hosts via an existing capture or route C) so copies exist.
- `EMAIL`: personal email addresses anywhere in the page text, including `mailto:`. Passes: `@decipher.com`, Players Committee role addresses (`rules@starwarsccg.org`, …), and a line carrying an `<!-- email-ok: reason -->` comment for a defunct address Bill wants kept.
- `REF`: a `<ref>` with no URL and fewer than two words of source text (e.g. `<ref>None</ref>`).
- `HEADING 'Sources'`: deck/event pages are detected by category, from the wikitext plus the live page's categories when linting by title: Decklists, Dark Side decks, Light Side decks, GEMP importable decklists, Tournaments, Championships, World Championships, Events, Retro League. Card pages (pages using `{{Card}}`, or in Category:Cards) and set-table pages (Category:Sets or any `… sets` category such as Decipher sets, Virtual Legacy sets, Current Virtual sets) may also keep Sources (Bill, 2026-10-20: a Sources list is only for pages that transcribe a single source; References are for specific claims on every page, and a source already cited as a reference is not repeated in Sources unless it is the source for the whole page). Every other page cites in References. Only a heading written in the page's own wikitext fails (Chief, 2026-10-20): a heading inside a template's `<includeonly>` (e.g. `== Sources ==` in [[Template:Card]]) is template output, so it is exempt on the template page, and card pages that only pass `|sources=` to the template pass.

Banned words skip names (Chief, 2026-10-20): `[[link text]]`, `[url link titles]`, templates such as `{{CardLink|...}}` and printed card titles from `authoring/card_title_map.json` (each half of a combo or Objective, with `(V)`/`(Dark)`-style qualifiers dropped) are not scanned, so a card like *We Have A Prisoner* is not read as "we". The editor's own prose around them is still checked. The page's own bold name is skipped too (Chief, 2026-10-20): the bold name opening the lead (two or more words, or equal to the page title), any bold span equal to the page title, and the title on a decklist title line (`'''Deck title:''' ...`, `deck title '''...'''`), so `'''2007 Worlds Day 1 Adam Howland LS We'll Handle This'''` is not read as "we"; a lone bold word and ordinary prose are still checked.

Transcript pages skip quoted speech (Chief, 2026-10-20): a page whose title ends in `(transcript)` (or a `/Transcript` subpage), or that is in Category:Transcripts, is a transcript. Each speaker turn there (a line opening with a bold label such as `'''[00:10] Henry Dunn:'''` or `'''Interviewer:'''`) is left out of the banned-word check. The page's own prose (lead, transcription note, section intros) and editorial labels such as `'''Note:'''` are still checked, and ARCHIVE still applies.

Tests: `python3 -m unittest discover -s authoring/tests` (fixtures are saved revisions of live pages).

## Snapshots (`make_snapshot.py`)
`python3 authoring/make_snapshot.py page.html --url LIVE_URL -o out.html [--flaresolverr http://localhost:8191/v1]` builds a self-contained HTML snapshot for Wayback.
With `--flaresolverr`, each run now uses its **own** FlareSolverr session, named `snap-<pid>-<UTC timestamp>` by default or set with `--fs-session NAME`. That session is destroyed when the run ends, even if the run fails.
Before this change every run shared one hard-coded `snap` session, which parallel jobs reused and which stayed open afterwards. Callers that pass nothing still work unchanged.
`--keep-fs-session` leaves a named session open for reuse. The script then won't close it, so you must call `sessions.destroy` yourself when done.
From Python, `Fetcher(..., fs_session=..., keep_fs_session=...)` is also a context manager (`with Fetcher(...) as f:`) that destroys the session on exit.
