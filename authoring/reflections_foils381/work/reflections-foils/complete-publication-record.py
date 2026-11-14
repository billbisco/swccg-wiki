"""Prepare final completion records only after the real inventory/QA passes."""
import json,sys
from datetime import datetime,timedelta,timezone
from pathlib import Path
root=Path(__file__).parent
final='--merged' in sys.argv
p=json.loads((root/'completion-progress.json').read_bytes())
audit=json.loads((root/'final-inventory-audit.json').read_bytes())
nav=json.loads((root/'final-navigation-audit.json').read_bytes())
assert p['remaining_to_complete']==0 and audit['articles_present']==314 and not audit['problems'] and not nav['problems']
for n in range(8,32):
    marker=json.loads((root/f'batch{n}-publication-verification.json').read_bytes())
    assert marker['publication_verified'] and marker['visual_inspection']=='inspected and accepted by MemoryCoreChatGPT'
q=json.loads((root/'preservation-queue.json').read_bytes())
images=sum('wiki_image_version' in r for r in q.values())
assert images==228
body=(root/'story-publishing.md').read_text(encoding='utf8')
body=body.replace('- [ ] AC2','- [x] AC2').replace('- [ ] AC3','- [x] AC3')
old='- [ ] AC4 Published pages are current/reviewed, style/Cite zero, source-conserved outside intended edits, and visually checked on desktop/mobile; citations and original assets have verified preservation evidence.'
new='- [x] AC4 Published pages are current/reviewed, all non-archive style/Cite checks pass, sources are conserved outside intended edits, and desktop/mobile output is visually checked. Under Bill’s 14 November amendment, original hashes, citations and exact outstanding public image versions are recorded and preservation is queued separately in task #412; unverified captures are never claimed verified.'
assert old in body or new in body
body=body.replace(old,new)
if final:
    merge=json.loads((root/'publication-merge-receipt.json').read_bytes());assert merge.get('merged') and merge.get('sha')
    body=body.replace('- [ ] AC5','- [x] AC5')
    body+='\n## Final verification\n\nAll 314 articles, 314 images and unique publication identities pass the final census. Current navigation checks cover '+str(nav['family_pages'])+' affected family pages and '+str(nav['memberships'])+' introduced foil destinations. All 297 new articles completed supported review, public/Cite, source/image/conservation/navigation and representative desktop/mobile checks. Source [PR21](https://github.com/billbisco/swccg-wiki/pull/21) merged as `'+merge['sha']+'`. Originals and shared evidence are backed up. Preservation remains queued under #412; the separate non-foil redirect bug #416 remains outside this completed publication scope.\n'
(root/'story-completed.md').write_text(body,encoding='utf8')
state='Done — publication and merged backup verified' if final else 'Publication verified — final merged backup pending'
note=f'''# Story 381 — {state}

All 217 previously unpublished drafts are published and the ten incomplete articles are finished. The full inventory contains 314 regular foil articles: 114 Reflections I, 100 Reflections II and 100 Reflections III; 297 new articles and 17 existing articles reused. No article deletion is required.

Publication verification is complete: final-inventory-audit.json, final-navigation-audit.json, publication-identity-check.json, per-batch source/public/conservation/navigation reports and accepted desktop/mobile captures. All original photographs are retained unchanged. Seventy new articles completed strict preservation earlier; preservation for 227 subsequent new articles and one reused article is separately queued under Bill’s explicit amendment. The queue contains {len(q)} distinct entries, including {images} exact public image versions. Queue entries are not verified captures.

Continue preservation only via [task412](https://github.com/swccg-guild/work/issues/412), using preservation-queue.json and source ops/wayback/queue.txt. Keep uncaptured staging and previous valid captures. Do not replay the publication scripts or wait for Wayback to accept the already completed publication. [Bug416](https://github.com/swccg-guild/work/issues/416) separately tracks an existing See-Threepio non-foil redirect; its foil article uses truthful family navigation.

The existing central server registry holds517 exact-byte registrations, including all228 pending Wiki original versions. Actual identifiers/export are in central-registration-receipts.json and central-registry-server-export.json. They have independently verified immutable backup receipts and await owner promotion; registration is not submission. Another419 source/citation entries require exact payload/evidence reconciliation in task412. No client-side saver, new service or direct pending-URL promotion was introduced.

[Story381](https://github.com/swccg-guild/work/issues/381); [source PR21](https://github.com/billbisco/swccg-wiki/pull/21); [all changed live page links](https://github.com/swccg-guild/work/blob/main/evidence/381/published-pages.md).
'''
for name in ['RESUME.md','acceptance-report.md','stop-note.md']:(root/name).write_text(note,encoding='utf8')
if final:
    now=datetime.now(timezone(timedelta(hours=-4))).strftime('%Y-%m-%d %H:%M')
    base='https://github.com/swccg-guild/work/blob/main/evidence/381/'
    report=f'''PASS-REPORT v1 — ticket #381 — agent: MemoryCoreChatGPT — {now} (UTC-4)

| AC | Result | Evidence |
|---|---|---|
| AC1 Dated inventory | PASS | [Inventory]({base}inventory.csv): 314 slots, reconciled 114/100/100; immutable initial inventory retained. |
| AC2 Complete distinct foil articles | PASS | [Final census]({base}final-inventory-audit.json): 314 articles and images, 314 unique publication IDs; 297 new and 17 reused. All217 prior drafts published and ten incomplete cards finished; independent physical-face readings and original image hashes retained. |
| AC3 Direct checklists and reciprocal navigation | PASS | All314 exact set destinations pass census; [current navigation]({base}final-navigation-audit.json): {nav['family_pages']} affected family pages, {nav['memberships']} foil memberships. Per-batch reports retain original-content conservation and public link checks. |
| AC4 Reviewed/public/visual and amended preservation criterion | PASS | Supported own-bot reviews, guarded edits, public current revision/Cite zero, non-archive lint zero, original image hashes and accepted desktop/mobile reports. Bill’s [explicit amendment](https://github.com/swccg-guild/work/issues/381#issuecomment-6877145822) applies: [queue]({base}preservation-queue.json) has {len(q)} entries, {images} exact image versions; [task412](https://github.com/swccg-guild/work/issues/412) remains open. Queued captures are not reported verified. |
| AC5 Merged source, durable originals/evidence and complete delivery | PASS | [Merged source PR21](https://github.com/billbisco/swccg-wiki/pull/21), merge `{merge['sha']}`; [originals repository](https://github.com/billbisco/swccg-wiki-files); [all changed live page links]({base}published-pages.md); current reports and receipts shared in evidence/381. |

Overall: PASS

MemoryCoreChatGPT: Publication is live and verified directly; wiki has no separate Test server. No article deletion or further permission is needed. External preservation remains explicitly queued under task412. Bug416 is a separate pre-existing non-foil identity issue, with truthful family labeling already used here.
'''
    (root/'PASS-REPORT.md').write_text(report,encoding='utf8')
print(state,';',len(q),'preservation entries;',images,'image versions')
