"""Current publication status under Bill's explicit archive deferral."""
import json,re
from pathlib import Path
root=Path(__file__).parent;p=json.loads((root/'completion-progress.json').read_bytes());c=p['counts'];heads=json.loads((root/'published-heads.json').read_bytes());queue=json.loads((root/'preservation-queue.json').read_bytes())
complete=c.get('created',0)+c.get('created_preservation_queued',0);live=complete+c.get('published_pending_batch_verification',0)
table='| Product | New publication complete | New live/checks underway | New drafts | Existing reused |\n|---|---:|---:|---:|---:|\n'
for product,count in p['per_product'].items():table+='| '+product+' | '+str(count.get('created',0)+count.get('created_preservation_queued',0))+' | '+str(count.get('published_pending_batch_verification',0))+' | '+str(count.get('draft_prepared_awaiting_preservation',0))+' | '+str(count.get('existing',0)+count.get('existing_preservation_queued',0))+' |\n'
summary=f'''The314 regular foil slots reconcile as114 Reflections I,100 II and100 III. Seventeen existing articles are reused (sixteen at the initial census, plus Don't Get Cocky discovered afterwards). {live} new articles are live; {complete} have completed publication checks, including {c.get('created_preservation_queued',0)} accepted with preservation queued. {c.get('published_pending_batch_verification',0)} live new articles are still being checked. {c.get('draft_prepared_awaiting_preservation',0)} new articles remain drafted. No physical faces remain unread; all298 initial-gap original photographs were checked independently and hashed.\n'''
text='# Story381 — publication with preservation queued\n\n'+summary+'\n'+table+f'''\n## Authorization and checks

On14 November2026 Bill explicitly instructed us not to let Wayback block publication, to queue preservation for later and publish the remaining217 drafts/finish the ten incomplete cards. This supersedes the prior archive gate for this story. The standard linter is unchanged; a task-scoped wrapper records ARCHIVE findings as deferred while rejecting every other finding. Exact original image hashes, supported reviews, guarded current revisions, source conservation, direct checklist/family links, public current revision/Cite and representative desktop/mobile checks remain required.

All217 original drafts passed physical field/style/template checks;12 Reflections III AI images matched their alternate-art references. Existing family templates and independent Conquest/Red5 navigation changes are retained. Current live-source backup includes {len(heads)} pages, listed in published-pages.md. No article deletion is required.

## Preservation follow-up

Task412 retains the separate archival work: {len(queue)} distinct source/citation/image queue entries, including {sum('wiki_image_version' in row for row in queue.values())} exact wiki-image versions recorded so far. Queue entries are not capture receipts. Existing verified captures remain usable; no failed/unchecked replay is labeled verified. Live forum/www.starwarsccg.org URLs are routed to staged snapshots, not submitted directly. No new Save Page Now requests are made by the publication pipeline.

The first70 new cards completed strict preservation before the exception. Subsequent publication markers explicitly say archive_deferred:true. Original photographs are backed up unchanged. The exact outstanding public image timestamps/SHA1/SHA256 and source URLs are in preservation-queue.json, also carried into source ops/wayback/queue.txt where supported.

## Continuation

Finish current batch checks and inspect its representative desktop/mobile captures, then continue batches9–31 through run-publication-batch.py with fresh family/set heads. Never replay obsolete revision guards or duplicate the existing Don't Get Cocky article. Current source PR21 is the publication checkpoint; PR18 was the earlier merged backup. After all articles/checklists/family links pass, merge current backup and close story381 under the amended acceptance criteria. Task412 remains open for external preservation.

[Story381](https://github.com/swccg-guild/work/issues/381); [preservation task412](https://github.com/swccg-guild/work/issues/412); [publication source PR21](https://github.com/billbisco/swccg-wiki/pull/21); [all changed pages](published-pages.md).
'''
draft_titles={r['proposed_article'] for r in json.loads((root/'manifest.json').read_bytes()) if r['status']=='draft_prepared_awaiting_preservation'}
index='# Remaining unpublished foil drafts — story381\n\n'+str(len(draft_titles))+' new articles remain unpublished. Printed/source evidence is retained in the corresponding stage readings. Preservation is queued separately under Bill’s authorization.\n\n| Article | Stage | Reading | Draft |\n|---|---|---|---|\n'
for stage in ['batch'+str(n) for n in range(9,32)]:
    for row in json.loads((root/(stage+'-new-packet.json')).read_bytes()):
        if row['title'] in draft_titles:index+='| '+row['title']+' | '+stage+' | ['+stage+'-readings.json]('+stage+'-readings.json) | ['+stage+'-new-packet.json]('+stage+'-new-packet.json) |\n'
(root/'draft-index.md').write_text(index,encoding='utf8')
(root/'current-batch-report.md').write_text(text,encoding='utf8');(root/'README.md').write_text(text,encoding='utf8')
body=(root/'story-authorized.md').read_text(encoding='utf-8-sig');start=body.index('## Current delivery');end=body.find('\n## User amendment',start);assert end>=0
delivery='## Current delivery\n\n'+summary+'\n'+table+'\nPublication continues under Bill’s explicit archive deferral. Preservation is tracked in [task412](https://github.com/swccg-guild/work/issues/412); queued captures are never reported verified. All other checks remain mandatory. [Publication source PR21](https://github.com/billbisco/swccg-wiki/pull/21), [current evidence/report](https://github.com/swccg-guild/work/blob/main/evidence/381/current-batch-report.md), [all changed pages](https://github.com/swccg-guild/work/blob/main/evidence/381/published-pages.md). No article deletion is needed.\n'
(root/'story-publishing.md').write_text(body[:start]+delivery+body[end:],encoding='utf8');print('New publication complete',complete,';new live',live,';new drafts',c.get('draft_prepared_awaiting_preservation',0),';source pages',len(heads))
