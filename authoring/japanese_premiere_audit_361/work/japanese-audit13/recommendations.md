# Japanese card integration recommendations — #361 / #287

Use the shared **Template:Card** for Japanese printings. The existing migration story [#287](https://github.com/swccg-guild/work/issues/287) is the right implementation home. It already has Bill's authorization, generic field names, sandbox trials, content conservation checks and English regression checks. Keep this content repair separate from the migration so its owner can rebase from the corrected live revisions.

## What this audit established

- All 324 regular Japanese Premiere printing IDs resolve to individual articles and retrievable image files. None currently transcludes Template:Card; all use hand-written infoboxes. A working image is not evidence that its full printed area is visible.
- Sixteen articles had not yet received Japanese game text, lore and translations even though their existing collector photographs made those fields readable. These are now completed from their faces. Four further Translation sections contained only a title (Ponda Baba, Overload, Physical Choke and Precise Attack); their game/lore translations are now filled. Ellorrs Madak's game text was truncated despite a complete photograph and complete set-list row.
- Ellorrs Madak, K'lor'slug, Rycar Ryjerd and Yerka Mig were typed as characters/creatures. Their Japanese faces and the set list classify them as Effects. Deriving type from a title would reproduce those errors.
- System parsec values had been put in Destiny fields. Several locations also carried imported destiny/deploy zero defaults and mixed Force icons with shared location symbols. The 37 location pages now separate counted Light/Dark Force icons, shared symbols and the ten printed parsec values.
- The Japanese Black 2 and Black 3 faces expressly say they have no hyperdrive. A missing number must not become an invented numeric zero. Droids do not print an ability value; the absent character ability is not a transcription gap.
- Recovered complete R4-E1 and Lieutenant Tanbris photographs verify their lower edges. Many other video-derived images remain candidates for edge inspection or replacement. Chief Bast's visible Imperial/Pilot symbols are now recorded with a precise lower-edge limitation.
- Historical text needs its own identity. Dutch's Japanese game text repeats a phrase; Owen Lars's lore calls him Obi-Wan's younger brother. Preserve these printed statements and explain them separately rather than silently rewriting them to match English text or later continuity.

## Recommended template contract

Use #287's proposed `language`, `printed_title`, `printed_game_text`, `printed_lore`, `translation`, `translation_note`, `border_finish`, `edition` and `release`. Default existing English pages without changing their render. `language=ja` describes the **physical printing**, while the article and its translation remain English. Do not reuse `original_title` (a virtual-card host-title concept) or `printed_label` (small print) for the Japanese title.

Place the native title first, followed by printed game text and lore with `lang="ja"`, then a clearly labeled editorial English translation and any comparison note. Keep the familiar English catalog title for navigation and cross-language discovery. A translation is not the English printing's rules text. Do not fill it by substituting an English counterpart.

For the migration, one verbatim `translation` block is the safest initial field because it preserves the varied existing sections. Later, separately typed translation-title/game/lore fields could improve reuse; introduce them only with a conservation report for the existing block.

Locations need two separately labeled side text blocks. For a first migration these can stay inside `printed_game_text`; a later generic pair of `light_game_text` / `dark_game_text` fields would enable consistent rendering and set-table reuse. A blank side of a location must stay blank. Preserve the distinction between **control** and **occupy** in both transcription and translation.

Keep `dark_icons` and `light_icons` numeric; put Interior Site, Exterior Site, Planet, Mobile and Scomp Link in the shared `icons` field. Preserve repeated symbols: Tonnika Sisters prints two Warrior icons. Support `*` in numeric-looking fields, including Jawa's deploy value. Do not classify a missing optional stat as zero. Clearly separate printed values from rule-derived attributes, and retain a specific uncertainty note where the source edge is hidden.

## Further integrations, in order

1. **One printing record, multiple views.** Drive the card article, set-list type/stats/text and printing-family navigation from the same verified printing data. The article/set drift found here shows why independent hand entry is fragile. Start with a read-only reconciliation report before generating set rows. Never derive identity or rules equivalence from English title alone.
2. **Printed set symbol versus product.** Tie #286's lookup to printing identity and the actual symbol. Japanese Premiere needs `None (Premiere)`; the current template fallback recognizes `Japanese Premiere` rather than the canonical `Premiere (Japanese)`. Do not infer the foil's printed symbol from the retail product name.
3. **Evidence status per field.** Store source File/revision and verification status in an audit manifest: verified, present but not independently rechecked, intentionally unprinted, or unresolved. Scan presence and full-face completeness are different checks. Replace blanket “incomplete article” warnings with specific evidence gaps.
4. **Cross-language navigation and search.** Keep reciprocal English/Japanese printing links and searchable native titles, tied to printing IDs. Use existing family navigation; add native-title redirects only after collision checks, particularly for same-title opposite-side cards. No article deletion or title move is required for these content repairs.
5. **A preservation trail readers can follow.** Let the File description hold photographer, original source record, exact original-byte hash and verified archival replay; articles cite that File. Keep source originals and display derivatives distinct. The two new files demonstrate this without overwriting old frames.
6. **CardMaker and exports.** Reuse language codes and verified printed fields with #283, but label recreated faces separately from original scans. A translation must not silently become gameplay text in GEMP or an “official English” export. Preserve original Japanese text-state differences.
7. **Language-aware characteristics and display.** Do not run English keyword/persona extraction over Japanese native text or infer characteristics from a translation without a face-based check. Preserve underlined keywords and source markers. Test Japanese glyphs and wrapping on a browser with CJK font support, including a narrow viewport; keep any language-specific style changes scoped so English cards retain their existing render.

## Add these migration fixtures to #287

- A freshly completed native-text article (2X-3KPR), a rich comparison page (BoShek), and Mantellian Savrip, which previously had no text sections.
- Both Alderaan printings: no destiny/deploy number, parsec 2, different Force-icon counts and different side text.
- Dantooine and Tatooine: both side text blocks, printed parsec, and no location lore.
- A droid with no printed ability, Jawa's `*` deploy, a no-hyperdrive TIE, Talz's three uniqueness asterisks and Tonnika Sisters' two Warrior symbols.
- Chief Bast's specific unresolved edge note, source references and preserved crop; full new photos and original-video provenance for R4-E1/Tanbris.
- The four Effect type corrections and Ellorrs Madak's inline Pilot icon.
- Reactor Terminal's formerly malformed Versions row; it now closes correctly without losing a printing link. Also account for the legacy raw HTML headings: their display anchors have no editable section indices, and API `rvsection=0` returns the whole card. Preserve their entire source when rebasing the migration.

Rebase #287's saved content/category baselines against #361's final revision manifest. Its old 35-page lint backlog must be reconciled: this audit fixes all 34 Premiere watch-page citation failures. Keep #287's sandbox-first, 10-page trials, 12-product/layout checks and 50 unchanged-English-render checks. This audit does not claim the template migration is complete.

MemoryCoreChatGPT
