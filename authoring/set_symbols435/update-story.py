import json,subprocess
from pathlib import Path
p=Path(__file__).parent
current=json.loads(subprocess.check_output(['gh','issue','view','435','-R','swccg-guild/work','--json','body']))['body']
section='''

## 14 November2026 — Bill's shared-source and test direction

Bill: “Before working on that though, check what cardmaker has. We may be doing double work here. We should utilize a common set of symbols.” He also requested a visual test and raised whether card text should use symbols given search difficulty.

The CardMaker-first audit is complete for its existing sphere library. [CardMaker PR12](https://github.com/billbisco/swccg-cardmaker/pull/12) is merged, adding reproducible transparent WebP exports from30 existing masters, a common manifest and ring/variant documentation. Existing source artwork and production rendering are unchanged. This is a shared source/derivative pipeline, not another Wiki artwork collection. Ten old Wiki Icon-set assets are opaque-cornered and have624 usages across610 distinct pages. Original/Legacy/Modern marks and regular/AI rings still require the inventory and physical checks in the gap ledger.

**Live test:** https://swccg.com/snapshots/review/story-435-set-symbols.html . Current versus candidate icons on grey/dark/checkerboard backgrounds,20px actual and64px enlarged; A image-only, B words-only, C image+words card-text examples. Public HTML and native desktop/mobile checks pass. No Wiki card page has been migrated in this test.

**Recommendation:** icon+linked set name in infoboxes; visible bracketed words such as `[Jabba’s Palace icon]` in card text, with the original scan alongside. Symbol+visible words is an alternative if Bill prefers retaining artwork inline. Alt text alone is not a visible symbol descriptor; the pilot tests visible labels, not the live Wiki search index.

**QUESTION @Bill Q1:** Which card-text style do you prefer: B (words only), C (symbols plus words), or A (symbols only)? B is recommended. The requested test is concrete and ready to compare; this is a presentation preference, not a request to reauthorize435.

Full migration remains In Progress. Do not mark this Story Done on the shared export or pilot alone. Shared evidence: evidence/435; source backup PR49. Archive.org/web.archive.org remains completely held;64 exact source payloads plus the review HTML have independent backups and central ready=false metadata only. No capture/submission/preservation-completion claim.
'''
assert '## 14 November2026 — Bill\'s shared-source and test direction' not in current
(p/'story-updated-body.md').write_text(current+section,encoding='utf8')
(p/'progress-comment.md').write_text('''PROGRESS: (MemoryCoreChatGPT) Shared-source audit and visual test ready.
- Done: reused CardMaker masters; [PR12 merged](https://github.com/billbisco/swccg-cardmaker/pull/12),30 transparent WebP exports with unchanged source artwork, alpha/lossless checks and shared manifest. Ten legacy Wiki icon assets audited:624 usages across610 pages.
- Test: [public visual comparison](https://swccg.com/snapshots/review/story-435-set-symbols.html), desktop/mobile image/sizing/visible-label checks pass. Compare current icons with candidates on light/dark/checkerboard backgrounds and A/B/C card text. No Wiki card migrated yet.
- Stopped at: the requested visual-test checkpoint, before broad Wiki replacement or choosing a new card-text convention.
- Next: Bill chooses Q1, then implement the selected card-text convention and guarded infobox/file replacements; continue regular/AI ring and numbered-era verification without substituting unverified variants.
- QUESTION @Bill Q1: Which card-text style do you prefer: B (words only), C (symbols plus words), or A (symbols only)? B is recommended; infoboxes retain icon+name.
- Work: [evidence/435](https://github.com/swccg-guild/work/tree/main/evidence/435), design log, gap ledger, exact source backup PR49. Story remains In Progress;286 retains wider infobox-population scope. Archive.org hold intact;65 exact sources/review HTML centrally registered ready=false, not submitted or captured.
''',encoding='utf8')
(p/'PROGRESS-REPORT.md').write_text('''Story435 — MemoryCoreChatGPT — 14 November2026 — pilot checkpoint

| AC | Current result | Evidence |
|---|---|---|
| AC1 Asset/usage/printing audit | PARTIAL | CardMaker existing sphere library identified;30 masters exported. Ten legacy Icon-set assets,624 usages,610 distinct pages in wiki-symbol-audit.json. Numbered Virtual and physical AI-ring inventory remain in remaining-gaps.json. |
| AC2 Print-faithful transparent WebP assets | PILOT READY | Existing masters reused with30 alpha-checked96px WebP derivatives and exact lossless RGBA derivative round trips. Source PNGs unchanged; shared manifest pins hashes and provenance. Five representative symbols and original Seeking An Audience face shown. Coruscant regular silver/AI gold not guessed; broader variant acceptance remains. |
| AC3 Consistent readable/searchable presentation | PILOT READY | Public preview at1280/390px,24 symbol bounds, no broken images, explicit searchable symbol-label checks for B/C. Infobox icon+name remains; Q1 card-text choice pending. Not a claim of Wiki search-index validation or completed rollout. |
| AC4 Guarded migration and gap ledger | NOT STARTED | No Wiki card changes in this pilot. remaining-gaps.json and Q1 recorded on435; source masters/originals retained; story286 coverage remains separate. |
| AC5 Independent backups/merged source/preservation | PILOT DELIVERED | CardMaker PR12 merged. Exact masters/derivatives/provenance independently restored from approved Wiki backup bundle;64 source objects plus hosted HTML centrally registered ready=false. Wiki backup PR49 and shared evidence preserve the test and continuation. Archive.org requests0; not externally preserved. |

Overall: IN PROGRESS — requested visual-test checkpoint ready; Q1 needed before broad card-text convention rollout. Do not close435 or claim a full symbol migration. Source/asset reuse and pilot delivery are complete; per-variant checks and Wiki replacements remain.
''',encoding='utf8')
print('Story direction, Q1 and honest per-AC progress prepared')
