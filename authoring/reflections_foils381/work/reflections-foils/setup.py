import json
from pathlib import Path
root=Path(__file__).parent
body='''## User story
As a collector and wiki reader, I want every regular Reflections I, II and III foil printing represented by a full, correctly identified card article, so I can inspect its printed characteristics and follow the set checklist and card-family navigation to that exact version.

## Authorization
Bill: “Yes, create a user story for the regular Reflections I, II, and III foil articles, inventory what already exists, and proceed with completing the missing articles.” No policy questions remain. Follow existing publication identity rules and the completed Luke foil pilot #378/#367. #254 is promotional foils and expressly excludes Reflections pack foils.

## Requirements
- R1 Inventory every regular pack-foil checklist row in Reflections, Reflections II: Expanding the Galaxy, and Reflections III: A Collector's Bounty against existing live articles, redirects, publication IDs, source images and family links. Retain already completed Japanese foil articles rather than recreating them.
- R2 Give each distinguishable foil version a full shared-Card article with verified printed title, side/type, language, product/finish, rarity, release, printed text/lore and applicable stats/symbols. Use stable publication identity; retain existing gameplay lineage and only verified GEMP mappings. Identical physical versions distributed in multiple products share an article with multiple source occurrences.
- R3 Find actual printing-specific images and primary evidence. Do not use a non-foil scan or generic foil effect as a historical foil face, infer unseen reprint text from another printing, or restore marked seller portraits. Keep an honest blank where no correct image is obtainable; document exact evidence gaps instead of inventing fields.
- R4 Work in complete batches: correct article/image or honest blank, directly targeted foil checklist row, all family Versions navigation (maintain shared navigators where already implemented). Preserve concurrent edits and separate original printed text from later errata.
- R5 Preserve citations and original source images, use own bot/reviewer identities and revision-guarded edits, verify public reviewed output and back up live changes in merged source with durable field-level evidence.

## Acceptance criteria
- [ ] AC1 Complete dated inventory reconciles each product's regular foil checklist against existing/missing/duplicate articles and records identity, language, sources and field gaps.
- [ ] AC2 Each missing distinct publication has its own shared-Card article with every verifiable field filled, correct foil provenance and actual foil image or explicit evidence-ledger limit; no non-foil substitution, fabricated text or invented playable IDs.
- [ ] AC3 All three foil checklists link directly to the intended foil article; every affected card family has reciprocal consistent navigation without duplicate destinations or lost existing versions.
- [ ] AC4 Published pages are current/reviewed, style/Cite zero, source-conserved outside intended edits, and visually checked on desktop/mobile; citations and original assets have verified preservation evidence.
- [ ] AC5 Code/live-source backups are merged, all changed pages are linked, per-product completion/gap counts and continuation instructions are shared, and a per-AC PASS report supports closure.

## Plan
Inventory live set sections, title/publication records and the #378 pilot; reconcile against preserved publisher/checklist evidence. Group by source-backed printing, recover foil faces, then publish batches of about ten with source guards and complete family/checklist updates. Verify source/parse/public/visual/archives per batch; merge final backups and report remaining source limits precisely.

Repos: billbisco/swccg-wiki (authoring, pages, preservation receipts), billbisco/swccg-wiki-files (original assets), swccg-guild/work evidence and design log. Local scratch: work/reflections-foils. Verification: inventory.csv/manifest.json (AC1), field readings and packets (AC2), link-membership report (AC3), source/public/visual/archive checks (AC4), merged PR and PASS report (AC5).

## Out of scope
New non-foil premium cards, random non-foil bulk reprints, promotional/tournament/box/case foil articles beyond preserving existing links, new GEMP card implementations, artificial foil rendering, or CardMaker changes. Already existing Japanese foil articles are inventoried and reused, with only necessary navigation repairs.

## Risks and handling
Checklist or seller wording is not proof of the face; foil text can differ from original or errata. Inspect and record printing-specific evidence. Preserve genuine identical cross-product versions instead of cartesian duplication. Do not claim source gaps are solved. No configuration, spending or deletion is required.

MemoryCoreChatGPT
'''
(root/'story.md').write_text(body,encoding='utf8')
(root/'story.json').write_text(json.dumps(dict(title='Story: Complete regular Reflections I, II and III foil card articles',body=body,type='Story',assignees=['MemoryCoreChatGPT2']),ensure_ascii=False),encoding='utf8')
(root/'ready.md').write_text('READY: approved (MemoryCoreChatGPT)\n\nBill explicitly requested creation, inventory and implementation of the regular Reflections foil articles in this chat. The specification follows the established printing/foil identity rules; no unanswered policy questions remain. Proceed with the source-backed inventory and complete publication batches.\n',encoding='utf8')
(root/'claim.md').write_text('CLAIM: (MemoryCoreChatGPT)\n\nTaking the requested inventory and implementation. Existing Japanese and Luke-pilot foil articles will be reused. Regular pack foils are separated from promotional/topper foils and random non-foil bulk. Work, source limits and verification will be preserved in shared evidence and a draft source PR.\n',encoding='utf8')
print('Story specification prepared')
