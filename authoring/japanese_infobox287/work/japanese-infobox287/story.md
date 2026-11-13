**Type:** Story · **Area:** Wiki · **Labels:** `area:wiki` · **Status:** Ready (all of Bill's questions answered, 12 Nov 2026) · **Agent:** Alpha1
**Blocks:** #286 (printed set icon on every card infobox), for those 794 pages only.
**Related:** #171 (Epic: translate SWCCG cards and localize the wiki), #283 (CardMaker Japanese templates and its `language` parameter), #245, #244.

## Bill's words (verbatim, 12 Nov 2026, 3:49 PM UTC-4)
> Understood. The Japanese pages need to be fixed such that the correct infobox template is used and changes go to it too. I agree. Why do you need Japanese fields? for that. You can make another story for rebuilding, but we aren't going to shy away from doing the right thing

## User story

As a wiki reader, I want every Japanese card page to use the same card infobox template (Template:Card) as every other card, so that it looks and behaves like the rest of the wiki and every future infobox improvement (starting with the set icon in #286) reaches it automatically.

## Background

- **What the pages are:** 794 card articles with hand-made infoboxes. 793 are the Japanese-language printings by Takara (1997–98), and one is the English 5×7 oversized promo [Mara Jade & •Corran Horn & •Talon Karrde](https://wiki.swccg.com/wiki/Mara_Jade_%26_%E2%80%A2Corran_Horn_%26_%E2%80%A2Talon_Karrde), which has the same problem and is fixed the same way:

  | Product | Pages |
  |---|--:|
  | Premiere (Japanese) | 324 |
  | A New Hope (Japanese) | 162 |
  | Hoth (Japanese) | 162 |
  | Premiere Introductory Two-Player Game (Japanese) | 68 |
  | Empire Strikes Back Introductory Two-Player Game (Japanese) | 61 |
  | Japanese Reflections II / III foils | 16 |
| Oversized promo (English) | 1 |

- **The problem:** none of these pages uses Template:Card. Each page has its infobox typed out by hand as an HTML table, one row at a time. So when Template:Card changes, these pages don't. That's why none of them has a Set icon row today.
- **Two layouts today** (live wikitext, 12 Nov 2026):
  - **751 template-look pages** (750 Japanese plus the oversized promo). The hand-made table copies the card template's look: Printing ID, Title, Side, Type, stats, Set, Publisher, Era, Versions. Example: [Admiral Motti (Japanese)](https://wiki.swccg.com/wiki/Admiral_Motti_(Japanese)).
  - **43 simple-table pages.** A shorter table with different rows: Printing ID, Side, Card type, Edition, Printed language, Border / finish, Release. Example: [2-1B (Too-Onebee) (Japanese)](https://wiki.swccg.com/wiki/2-1B_(Too-Onebee)_(Japanese)).
  - Both layouts also have body sections the template has no place for: **Title** (Japanese), **Card Text** (Japanese), **Lore** (Japanese), **Translation of Japanese Text** (English title, card text and lore), and a **Comparison with the English printing** paragraph.

### Why the template needs a few new optional fields (Bill: "Why do you need Japanese fields?")

The fields aren't Japanese-only. They're **printing-language fields** any non-English printing can use, and they're optional, so the 9,276 English pages don't change at all.

They're needed so that no text is lost in the move:
- Template:Card already has places for the English title, game text and lore. On an English page, those hold the printed text.
- On a Japanese page, the printed text *is* Japanese, and the page also carries an English translation and a comparison note. Those are three different pieces of text, and the template has room for one.
- Without new fields, the move would have to do one of two bad things:
  - drop the Japanese text or the translation; or
  - put it in loose wikitext after the template. Template:Card draws the whole page body (lead sentence, Card Text, Lore, Notes, References) inside its own layout, so text left outside it lands below References, outside the page layout.
- With the fields, the template draws these sections in the same place and style on every Japanese page. Later languages (#171) reuse the same fields with no new template work.

**Proposed fields** (names line up with #283's `language` parameter):

| Field | Holds | Today on the page |
|---|---|---|
| `language` | `ja` (default English when empty) | "Printed language" row (simple pages); implied on the rest |
| `printed_title` | Japanese title, wrapped in `<span lang="ja">` by the template | "Title" section |
| `printed_game_text` | Japanese card text | "Card Text" section |
| `printed_lore` | Japanese lore | "Lore" section |
| `translation` | English translation (title, card text, lore), verbatim | "Translation of Japanese Text" |
| `translation_note` | The comparison with the English printing | "Comparison with the English printing" |
| `border_finish` | e.g. black border, foil | "Border / finish" row (simple pages) |
| `edition` / `release` | Edition and release lines | Simple pages' rows |

Existing fields cover the rest: `title`, `side`, `type`, stats, `set`, `publisher`, `era`, `gemp_id` (Printing ID), `versions`, `image`, `notes`, `see_also`.

## Requirements

- **R1. All 794 pages use `{{Card …}}`**, with no hand-made infobox table left. The oversized promo keeps its Size and Year rows (existing `notes` or a new optional `size` field, decided in the sandbox step and recorded).
- **R2. New optional fields** (table above) are added to Template:Card, with no change to how any English page renders.
- **R3. Verbatim content preservation.** Every piece of visible text and every link, file, reference and category on the old page is still on the new page:
  - the Japanese title, text and lore (character-for-character, including full-width punctuation);
  - the translation and comparison text;
  - every reference with its Preserved copy;
  - Versions, image, See Also and Notes.
- **R4. Categories.** Template:Card adds Cards, the set, the side and the type automatically. Those are the same four categories almost every Japanese page has by hand today (793 of 794 have Cards and a side). The hand-written category lines are removed only when the template adds the same one. Any extra category stays as a per-page category. No page loses or gains a category without a recorded reason.
- **R5. Lead sentence.** The template writes "'''X''' is a [[Dark]] [[Character]] from [[Premiere (Japanese)]]." That matches today's hand-written lead on the 751 template-look pages. Any page whose hand-written lead says more keeps the extra words in `notes` or `hatnote`, and the change is listed in the migration report.
- **R6. Sandbox first.** The field changes are built in Template:Card/sandbox, then 10 pages (5 template-look, 5 simple-table, including one foil and one two-player page) are rendered with the sandbox and checked before the template is published or any page is converted.
- **R7. The Set icon row** on each rebuilt page shows the printed symbol from #286's lookup: Premiere-family Japanese cards "None (Premiere)", A New Hope and Hoth Japanese cards those sets' symbols, foils the symbol on their scan.
- **R8. Style-check backlog (Bill's D7 rule).** Before the first edit, the pages in scope that fail `style_lint` are saved to [`evidence/287/lint-backlog.csv`](https://github.com/swccg-guild/work/blob/main/evidence/287/lint-backlog.csv) (12 Nov baseline: 35 pages, already saved). A rebuilt page may be saved with those old flags, but no new ones. A follow-up Task, opened with this Story, fixes every listed page immediately after the rebuild. This Story closes only when that Task has its own PASS-REPORT.
- **R9. Wiki gates:** bot account with `bot=1`, basetimestamp/starttimestamp on every edit, 0 Cite errors, FlaggedRevs reviewed, Wayback Preserved copy for any cited URL.
- **R10. Scripts** (convert, content-diff, audit) are committed to billbisco/swccg-wiki `authoring/` and can be rerun.

## Acceptance criteria

- [ ] **AC1** Given the audit after the work, all 794 pages (793 Japanese, 1 oversized promo) transclude Template:Card, and none has a hand-made `card-infobox` table.
- [ ] **AC2** **No text lost:** for every page, a script extracts the visible text, links, files, references and categories from the old revision and from the new one, and the diff shows nothing missing. Only differences listed in the migration report are allowed (lead-sentence or category changes per R4/R5).
  - Evidence: `content-diff.csv` (one row per page: missing 0, added items listed), `migration-report.md`.
- [ ] **AC3** Given a rebuilt page of each layout and each product (12 pages), it renders the Japanese title, text and lore with `lang="ja"`, then the translation and comparison text, and the infobox rows of its old table.
  - Evidence: before/after screenshots, `samples/*.png` (500 KB or less each).
- [ ] **AC4** Given 50 random English card pages, rendered HTML before and after the template change is identical.
  - Evidence: `render-diff-english.txt`.
- [ ] **AC5** Category membership of every Japanese page is the same before and after, except changes listed in the migration report.
  - Evidence: `categories-before.csv`, `categories-after.csv`.
- [ ] **AC6** Each rebuilt page shows a Set icon row from the #286 lookup (R7), once #286's lookup is live.
- [ ] **AC7** `lint-backlog.csv` exists before the first edit. No rebuilt page has flags beyond its backlog entry. Template:Card, /doc and /sandbox lint 0. The follow-up Task has fixed every backlog page and posted its PASS-REPORT.
- [ ] **AC8** Template:Card/doc documents the new fields, with a Japanese example.

## Out of scope

- Translating or rewording any text. Content moves verbatim.
- New Japanese card pages, or pages for other languages (#171).
- CardMaker Japanese faces (#283).
- The set-icon lookup itself (#286).

## Open questions

None. Bill decided the rebuild on 12 Nov 2026 (quoted above). Field names follow #283's `language` parameter.

## Plan

- **Approach:**
  1. Save baselines: old revisions, text extracts, categories and the lint backlog.
  2. Add the optional fields in Template:Card/sandbox and prove them on 10 sandbox renders, plus the 50-page English render diff.
  3. Publish the template change and review it in FlaggedRevs.
  4. Convert the 751 template-look pages with a script, in batches of 50, running the content diff after each batch and stopping on any missing text.
  5. Convert the 43 simple-table pages the same way (they need their own row mapping).
  6. Rerun the audit and diffs, then hand over to #286 for the Set icon check.
  7. Follow-up Task: fix the lint backlog immediately after.
- **Repos / files touched:**
  - wiki.swccg.com: Template:Card, /doc and /sandbox, and the 794 pages.
  - billbisco/swccg-wiki `authoring/`: convert, diff and audit scripts.
  - swccg-guild/work `evidence/<n>/`.
- **Breakdown (Tasks):** T1 template fields (sandbox) · T2 convert the 751 · T3 convert the 43 · T4 lint backlog fixes (immediately after).
- **Risks:**
  - The biggest risk is lost text. The per-page content diff (AC2) is the guard, and batches stop on any miss.
  - Template:Card changes often, so build in the sandbox and use basetimestamp.
  - About 800 pages re-render, plus FlaggedRevs review.
  - No deletions or server changes.
- **Verification:** AC1 audit · AC2 content diff · AC3 sample screenshots · AC4 English render diff · AC5 category diff · AC6 parse after #286 · AC7 lint before/after plus Task PASS-REPORT · AC8 /doc diff.

The wiki has no Test server, so sandbox renders stand in for Test. Done = live on the wiki with AC1–AC8 met.
