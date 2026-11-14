"""Current evidence summary; partial work never counts as full delivery."""
import json,re
from pathlib import Path
root=Path(__file__).parent
p=json.loads((root/'completion-progress.json').read_bytes());heads=json.loads((root/'published-heads.json').read_bytes())
summary='Inventory: 314 regular foil slots (114 Reflections I, 100 II, 100 III). Sixteen articles existed initially. Of the 298 initial gaps: 70 new articles passed full verification; ten additional new articles are live with preservation/family completion outstanding; 217 new drafts are prepared; one additional existing article was discovered and reused. No faces remain unread or undrafted. The story remains unfinished; AC2–AC5 are open.\n'
table='\n| Product | Initial existing | Fully verified new | Additional new live | Unsaved drafts | Additional existing reused |\n|---|---:|---:|---:|---:|---:|\n'
for product,c in p['per_product'].items():table+='| '+product+' | '+' | '.join(str(c.get(k,0)) for k in ['existing','created','published_pending_batch_verification','draft_prepared_awaiting_preservation','existing_pending_preservation'])+' |\n'
text='''# Story381 — current delivery, 14 November 2026

SUMMARY
TABLE
## Delivered and checked

The first seven batches passed exact source, style, supported review, public current revision/Cite, reciprocal family/checklist links, source conservation, source preservation, exact wiki-original binary captures and representative desktop/mobile checks. All70 File pages have byte-verified replay links. Subsequent independent navigation additions on Conquest/Red5 families were retained in the backup, with foil text/stat fields unchanged (post-delivery-current-heads.json).

Batch8 has ten new articles, ten original images/File descriptions, ten signed Talk notes and direct Reflections checklist links live. Its published subset passed a separate31-page source/public/review/image-hash check. Its45 family drafts and ten wiki-original captures/File Preservation links remain unfinished. The partial check is not a full-batch PASS.

The existing Don't Get Cocky Reflections II foil was independently checked against two complete photographs. Missing language, finish and release metadata and the direct Reflections II checklist target were completed (revisions304301–304303), retaining its four reciprocal family links, image and printed text. Public/review/style/Cite and desktop/mobile checks passed. Its source photo has a replay; the exact wiki-image URL still needs its own capture. This is not an81st new card or a fully preserved delivery.

Current backup: PAGECOUNT distinct live pages, all linked in published-pages.md. No article deletion is required.

## Prepared work

All298 initially missing English physical faces were independently read:113/95/90 by product. Every original hash is checked. Batches9–11 contain33 unsaved Reflections I drafts;12–21 contain94 Reflections II drafts;22–31 contain90 Reflections III drafts. All217 new drafts have zero style flags, shared-Card previews, exact field/reading agreement and unique publication IDs. See prepared-work-verification.json and draft-index.md. Draft-only image identities are not uploads. The12 Reflections III alternate-image faces were manually compared against regular and alternate references and matched (artwork-verification.json).

Printed differences, symbolic/named statistics, side-specific location text and copyright evidence are retained; no playable mappings are invented. Existing Japanese foils and Luke's completed English foil are reused. Ric Olié's source-name mismatch was fixed by explicitly reading the UTF8 discovery ledger, without renaming or losing its original photograph.

Inherited family citations are separately inventoried:211 distinct URLs,27 reusable verified receipts,184 still needing archival verification. This is not a physical-face gap. No unverified family packet was published. Refresh all family/set guards before applying these historical drafts.

## External preservation blocker

Wayback anonymous GET saves on both VPS and Bill's PC returned HTTP520 / “Job failed”. The public POST route returned HTTP429 explicitly identifying automated-traffic throttling, so submissions stopped. The documented authenticated VPS route returned HTTP401. One ordinary retry after an extended cooldown still returned520. No credentials were exposed, no requests were rotated to bypass throttling, and no failed capture was certified.

Core rules require “Never save with open flags.” Unpreserved File descriptions and inherited citations fail ARCHIVE lint; exact public image versions also need their own byte-verified replay. The general access fallback does not authorize weakening the explicit lint/image rules. No further permission question is outstanding. Service recovery or maintenance of the existing authenticated credential is required for complete publication.

Original photographs are backed up in swccg-wiki-files. Exact image versions and retained staging URLs are queued in the source repository. Keep /opt/swccg-res/snapshots/psa/reflections381-batch8-primary-sources.html and reflections381-batch8-wiki-originals.html until captures are checked. A gallery capture does not replace each binary comparison.

## Continuation

Finish batch8's primary snapshot,45 family edits, ten exact wiki-original captures and File links, then full verification. Capture the reused Don't Get Cocky wiki image too. Continue prepared batches9–31 with fresh family/set guards and complete upload packets regenerated only after verified source snapshots. See RESUME.md. Source backup PR18 is a checkpoint, not closure of the story.

[Story381](https://github.com/swccg-guild/work/issues/381); [source backup PR18](https://github.com/billbisco/swccg-wiki/pull/18); [shared evidence](https://github.com/swccg-guild/work/tree/main/evidence/381).
'''.replace('SUMMARY',summary).replace('TABLE',table).replace('PAGECOUNT',str(len(heads)))
(root/'current-batch-report.md').write_text(text,encoding='utf8')
links='[Detailed report](https://github.com/swccg-guild/work/blob/main/evidence/381/current-batch-report.md), [all changed pages](https://github.com/swccg-guild/work/blob/main/evidence/381/published-pages.md), [draft index](https://github.com/swccg-guild/work/blob/main/evidence/381/draft-index.md), [source backup PR18](https://github.com/billbisco/swccg-wiki/pull/18).'
live=(root/'story-live.md').read_text(encoding='utf-8-sig');assert live.count('## Current delivery')==1
delivery='## Current delivery\n\n'+summary+table+'\nAll298 initial-gap faces were independently read and original hashes checked;12 AI artwork comparisons verified. All217 unsaved drafts pass style/field/infobox-preview checks. Existing Don’t Get Cocky metadata and direct checklist integration are complete; its wiki-image capture remains.\n\nPublication is externally blocked: anonymous archive saves520, explicit public POST throttling429, documented authenticated route401. No captures were invented or failed results marked verified. Next: complete batch8 preservation/family work, then publish9–31 with fresh guards. No further authorization is needed and no articles need deletion.\n\n'+links+'\n'
(root/'story-current.md').write_text(re.sub(r'## Current delivery\n.*',lambda m:delivery,live,flags=re.S),encoding='utf8')
(root/'README.md').write_text('# Regular Reflections foil publications — story381\n\n'+summary+table+'\nRead current-batch-report.md, RESUME.md, draft-index.md and published-pages.md. Never count drafts, queues or partial checks as whole-story completion.\n',encoding='utf8')
print(len(heads),'live backup pages;217 drafts;298 initial-gap faces read; whole story unfinished')
