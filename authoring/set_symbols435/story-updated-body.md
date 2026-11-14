## User story
As a Wiki reader, I want small, transparent, print-faithful set symbols in infoboxes and card text, so I can identify the actual printed expansion without colored background fragments, wrong rings, oversized images or wasteful assets.

## Authorization
Bill,14 November2026, requested fixing five named Reflections orientations, hiding grading holders from Wiki display while retaining original-image links, fixing oversized inline set symbols shown in his screenshot, and creating a general transparent-WebP set-symbol cleanup story. Archive.org/Wayback is fully paused; no request of any kind is allowed until Bill explicitly resumes.

## Requirements
- R1 Inventory every used set-symbol asset and its infobox/card-text/table consumers, including current286 work. Record duplicates, missing glyphs, opaque backgrounds, red/card-background halos, size overrides and genuine printed variants.
- R2 Publish source-verified transparent WebP symbols, with alpha and small dimensions/bytes appropriate for20px display. Preserve originals and provenance; no invented or generatively reconstructed historical symbols. Preserve genuine black/silver/gold rings and printed AI distinctions. Remove only background that is not part of the printed mark.
- R3 Reuse a common sizing/rendering convention for infoboxes, inline card text and set tables. Do not let portrait CSS enlarge symbols. Use the printed symbol, not the pack product, for reprints; Premiere None stays explicit. Link each to the appropriate expansion family.
- R4 Keep print-matched variants separate, preserve historical sources, register new originals centrally and independently back them up. Archive.org remains paused; pending preservation is never reported captured.

## Acceptance criteria
- [ ] AC1 Dated asset/usage/printing-variant audit and relationship to286 are shared.
- [ ] AC2 Approved representative assets, including Jabba’s Palace, match physical printed marks without red background remnants, have true alpha, WebP format, small byte counts and measured thumbnail support.
- [ ] AC3 Infobox and in-text symbols use consistent small sizing on desktop/mobile; table images do not enlarge inline glyphs. Regular/AI ring variants remain correct.
- [ ] AC4 Full migration has a defined printing-aware inventory, guarded changes, public/render/conservation checks, original-file access and an honest remaining-gap ledger; no unsupported mass replacements.
- [ ] AC5 All delivered assets/source/evidence are independently backed up and merged, new image-version registrations retained, Archive hold preserved, and per-AC PASS supports closure only when scope is complete.

## Plan and boundaries
Coordinate with existing Ready story286 (assigned Alpha1; Japanese-template dependency287 is now complete). Prepare an accurate asset inventory and print-verified pilot before broad replacement. Immediate Reflections display defects are a separately linked Bug. Do not take over286 silently, overwrite other agents, modify card scans, change server configuration, create a saver or contact Archive.org. Wider migration remains queued until its full audited batches are executed.

MemoryCoreChatGPT


## 14 November2026 — Bill's shared-source and test direction

Bill: “Before working on that though, check what cardmaker has. We may be doing double work here. We should utilize a common set of symbols.” He also requested a visual test and raised whether card text should use symbols given search difficulty.

The CardMaker-first audit is complete for its existing sphere library. [CardMaker PR12](https://github.com/billbisco/swccg-cardmaker/pull/12) is merged, adding reproducible transparent WebP exports from30 existing masters, a common manifest and ring/variant documentation. Existing source artwork and production rendering are unchanged. This is a shared source/derivative pipeline, not another Wiki artwork collection. Ten old Wiki Icon-set assets are opaque-cornered and have624 usages across610 distinct pages. Original/Legacy/Modern marks and regular/AI rings still require the inventory and physical checks in the gap ledger.

**Live test:** https://swccg.com/snapshots/review/story-435-set-symbols.html . Current versus candidate icons on grey/dark/checkerboard backgrounds,20px actual and64px enlarged; A image-only, B words-only, C image+words card-text examples. Public HTML and native desktop/mobile checks pass. No Wiki card page has been migrated in this test.

**Recommendation:** icon+linked set name in infoboxes; visible bracketed words such as `[Jabba’s Palace icon]` in card text, with the original scan alongside. Symbol+visible words is an alternative if Bill prefers retaining artwork inline. Alt text alone is not a visible symbol descriptor; the pilot tests visible labels, not the live Wiki search index.

**QUESTION @Bill Q1:** Which card-text style do you prefer: B (words only), C (symbols plus words), or A (symbols only)? B is recommended. The requested test is concrete and ready to compare; this is a presentation preference, not a request to reauthorize435.

Full migration remains In Progress. Do not mark this Story Done on the shared export or pilot alone. Shared evidence: evidence/435; source backup PR49. Archive.org/web.archive.org remains completely held;64 exact source payloads plus the review HTML have independent backups and central ready=false metadata only. No capture/submission/preservation-completion claim.
