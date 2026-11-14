import collections,csv,json
from pathlib import Path
root=Path(__file__).parent
rows=json.loads((root/'manifest.json').read_bytes())
if not (root/'initial-manifest.json').exists():(root/'initial-manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
if not (root/'initial-inventory.csv').exists():(root/'initial-inventory.csv').write_bytes((root/'inventory.csv').read_bytes())
heads=json.loads((root/'published-heads.json').read_bytes());readings=json.loads((root/'first-readings.json').read_bytes())
for reading in readings:
    matches=[r for r in rows if r['product']=='Reflections' and r['side']==reading['side'] and r['proposed_article']==reading['article']];assert len(matches)==1,reading['article']
    r=matches[0];r.update(status='created',existing_article=reading['article'],existing_revid=heads[reading['article']]['revisions'][0]['revid'],source_photo_sha256=reading['source_sha256'],evidence_status='Full original physical foil inspected; printed fields transcribed; published/reviewed/public/source/nav checks pass; gameplay mapping not asserted')
(root/'manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
with (root/'inventory.csv').open('w',encoding='utf8',newline='') as f:
    keys=['product','checklist_number','side','rarity','label','language','alternate_image','status','existing_article','existing_revid','proposed_article','evidence_status'];w=csv.DictWriter(f,fieldnames=keys,extrasaction='ignore');w.writeheader();w.writerows(rows)
counts=collections.Counter((r['product'],r['status']) for r in rows)
(root/'inventory-status.json').write_text(json.dumps([dict(product=p,status=s,count=n) for (p,s),n in sorted(counts.items())],indent=2),encoding='utf8')
report='''# Story381 — first verified batch

The complete checklist census reconciles 314 regular slots: 114 Reflections I, 100 II and 100 III. It includes fifteen existing Japanese pack foils and the existing English Luke article. The Japanese Vader case topper and four English box toppers are excluded from the regular count. Twelve III slots use alternate images. The source checklist's catalog numbers and occasional misspellings are retained separately from canonical article identity; none are invented GEMP blueprint IDs.

Initial missing count: 298 English articles. Ten have now been created, leaving 288. These ten have independent physical-face transcriptions, unchanged original JPEGs, archived provenance, complete family links and direct Reflections checklist targets. Source differences were preserved, notably 2-1B, Ben Kenobi, Attack Run, Biggs and Black 2. No original/errata text was blindly cloned into the foil articles.

Verification: 85 live source checks exact, style lint zero; all mainspace/File revisions reviewed, Talk review inapplicable; all 85 anonymous public pages current and Cite zero; ten uploaded image SHA1 matches; 54 reciprocal family links and non-navigation content conserved. Seven desktop/mobile/before-after browser captures supplement these checks. Redirect-duplicate links and unlabeled extra family entries were removed from the newly created foil navigators. Other family content remains unchanged apart from intended navigation and explicit source-preservation additions.

Ten original photographs are backed up at https://github.com/billbisco/swccg-wiki-files/commit/7d2b285c2fe655902e6a12ac65604ed822cbb979 . The self-contained original-photo snapshot is byte-verified. Inherited GitHub citation failures were repaired using verified immutable GIF captures, direct verified commit pages, and a byte-verified selected-primary-source snapshot containing public commit fields/diffs/history and the unchanged original Black 2 image. Email metadata was excluded; the snapshot is clearly labeled as source data, not GitHub interface reconstruction. Exact receipts retain the initial failed attempts.

This is a first-batch result, **not** a whole-story PASS. #381 stays In Progress. Further collector photo candidates and SWCA item leads still require physical-face reading before publication. No generic foil effect or non-foil placeholder is used. See `inventory.csv`, `first-readings.json`, `first-source-verification.json`, `first-public-verification.json`, `first-navigation-verification.json`, `first-conservation.json`, `first-visual-verification.json` and `published-pages.md`.
'''
(root/'first-batch-report.md').write_text(report,encoding='utf8')
(root/'progress-note.md').write_text('PROGRESS: (MemoryCoreChatGPT)\n\n[Full inventory](https://github.com/swccg-guild/work/blob/main/evidence/381/inventory.csv): 314 regular foil slots, sixteen existing articles initially and 298 missing English articles. First ten are now published and verified, leaving 288; [first batch report](https://github.com/swccg-guild/work/blob/main/evidence/381/first-batch-report.md) and [all 85 changed live pages](https://github.com/swccg-guild/work/blob/main/evidence/381/published-pages.md). Ten original photographs, 54 reciprocal family links, direct Reflections checklist links, signed Talk notes and inherited citation repairs are included.\n\nContinuing the remaining physical-source inventory and article batches. Draft source PR: https://github.com/billbisco/swccg-wiki/pull/18 . Current scratch: work/reflections-foils; shared evidence: evidence/381. No source gaps are being represented as completed card data.\n',encoding='utf8')
body=(root/'story.md').read_text(encoding='utf8').replace('- [ ] AC1','- [x] AC1')
(root/'story-current.md').write_text(body+'\n## Current delivery\n\n'+report.split('Initial missing count:',1)[1].split('\n\nVerification:',1)[0].join(['Initial missing count:',''])+'\n\n[Inventory and first batch evidence](https://github.com/swccg-guild/work/tree/main/evidence/381). Whole-story work remains In Progress.\n',encoding='utf8')
print(dict(counts))
