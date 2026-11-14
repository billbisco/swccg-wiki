# Story435 — shared-symbol source and visual test

## 14 November2026 — CardMaker-first shared source

**Decision:** reuse CardMaker's existing master sphere PNGs and current renderer ring recipe; export reproducible transparent96px WebP display derivatives in the CardMaker repository. Pin per-file master/derivative hashes and source commit. Do not create another hand-cut Wiki artwork family.

**Why:** CardMaker already has30 relevant sphere masters, source lists and newer print-derived cuts. Its Rev80 provenance supersedes older Wiki-inner-disc and Game Aid sources. A symbol may consist of sphere artwork plus a ring supplied by the renderer; raw transparent PNG and complete rendered symbol are distinct. The visual test uses the existing classic inline black-ring recipe and clips transparent corners.

**Alternatives:** recutting the same spheres for Wiki duplicates work and risks drift; blindly copying older assets carries obsolete artwork/backgrounds. Existing CardMaker Coruscant assets are not proof of regular silver versus AI gold, so keep those variants unresolved until verified from physical printings. Preserve genuine printed rings.

**Who/status:** Bill requested435, CardMaker-first reuse, a common source and a visual test on14 November2026. MemoryCoreChatGPT implements the source audit/export/pilot. No production CardMaker renderer or Wiki card has changed in this pilot.

**Evidence:** cardmaker-tree.json, cardmaker-import.json, symbols/manifest.json, shared-symbols.tar.xz, export-symbols.py; wiki-symbol-audit.json inventories ten opaque-corner Icon-set files,624 file-usage references across610 distinct pages. This is the legacy Icon-set asset inventory, not an assertion that every Virtual mark is inventoried. Remaining gaps are explicit in remaining-gaps.json.

## 14 November2026 — searchable card-text presentation test

**Proposal:** keep icon+linked set name in infoboxes. Prefer explicit bracketed words such as `[Jabba’s Palace icon]` in the reading copy of card text, with the original scan visible beside it. A symbol+visible-word alternative preserves the artwork inline, with additional visual density. Alt text remains for accessibility; visible labels make the symbol references explicit in ordinary reading, copying and find-in-page.

**Test:** preview.html is self-contained and displays current versus candidate icons on grey/dark/checkerboard backgrounds,20px actual size and64px enlarged. It includes three exact presentation candidates for Seeking An Audience and the original face as a reference. check-preview.py verifies unbroken images, round bounds and explicit visible labels at1280px/390px. The search check proves presence of visible symbol descriptors, not a live MediaWiki search-index result. Existing sentence words about Jabba’s Palace sites occur in all three examples; the descriptor distinguishes the symbol reference itself.

**Open Q1 (Bill):** for card-text symbol references, choose B words only (recommended), C symbol plus visible words, or A symbols only. The visual test is ready; broad card-text replacement remains pending this choice. This is a display preference, not a request to reauthorize435. Asset/source audit and shared-library work proceed independently. Story286 retains wider infobox-population ownership.

**Hold:** no Archive.org/web.archive.org requests of any kind; no saver/service/timer started. New shared objects retain independent GitHub backup/readback and central pending metadata before any later Wiki publication. No preservation-completion claim.
