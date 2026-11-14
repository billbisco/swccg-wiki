"""Register known exact bytes with the existing owner, without submitting saves."""
import hashlib,json,subprocess
from pathlib import Path
root=Path(__file__).parent
records=json.loads((root/'uploaded-images.json').read_bytes())+json.loads((root/'psa-originals.json').read_bytes())+[json.loads(s) for s in (root/'swca-originals-results.jsonl').read_text(encoding='utf8').splitlines()]
sizes={}
for row in records:
    if 'local_file' not in row:continue
    data=(root/row['local_file']).read_bytes();sha=hashlib.sha256(data).hexdigest();assert sha==row['sha256'];sizes[sha]=len(data)
queue=json.loads((root/'preservation-queue.json').read_bytes());requests=[];unregistered=[]
for url,row in queue.items():
    image=row.get('wiki_image_version');sha=image['sha256'] if image else row.get('source_sha256')
    if not sha or sha not in sizes:
        unregistered.append(dict(url=url,reason='Exact source response/snapshot payload and independent receipt must be reconciled in task412 before registry registration'));continue
    subject=dict(kind='wiki_file_version' if image else 'source_snapshot',title=image['title'] if image else url,content_sha256=sha,bytes=sizes[sha])
    if image:subject.update(upload_timestamp=image['timestamp'],original_version_url=url)
    requests.append(dict(schema_version=1,subject=subject,source=dict(url=url,sha256=sha,bytes=sizes[sha]),readiness=dict(ready=False,reason='Task412: deferred external preservation; reconcile immutable independent backup/readback receipts before owner promotion',stage_bytes=0),owner='MemoryCoreChatGPT / swccg-guild/work#412',continuation='Reconcile source/image backup receipts, attach checked evidence and increment generation; existing server-wayback-owner alone stages/promotes/submits when its circuit permits; verify exact replay before adding File/citation links.',approval_scope=dict(story=381,follow_up=412,authorization='Bill explicitly requested queuing preservation for later on 2026-11-14',evidence='https://github.com/swccg-guild/work/issues/381#issuecomment-6877145822')))
(root/'central-registration-requests.json').write_text(json.dumps(requests,ensure_ascii=False,indent=2),encoding='utf8')
code='REQUESTS='+repr(requests)+'\n'+'''import json,sys
from pathlib import Path
sys.path.insert(0,'/opt/swccg-ops/repos/swccg-wiki/ops')
import preservation_registry as registry
directory=Path('/root/.local/state/swccg-wayback/registry');assert directory.is_dir()
receipts=[registry.register(directory,r) for r in REQUESTS]
print(json.dumps(dict(receipts=receipts,export=registry.export_records(directory))))
'''
result=subprocess.check_output(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode())
data=json.loads(result)
for receipt,request in zip(data['receipts'],requests):queue[request['source']['url']]['central_registration']=receipt
(root/'central-registration-receipts.json').write_text(json.dumps(data['receipts'],ensure_ascii=False,indent=2),encoding='utf8')
(root/'central-registry-server-export.json').write_text(json.dumps(data['export'],ensure_ascii=False,indent=2),encoding='utf8')
(root/'central-registration-remaining.json').write_text(json.dumps(unregistered,ensure_ascii=False,indent=2),encoding='utf8')
(root/'preservation-queue.json').write_text(json.dumps(queue,ensure_ascii=False,indent=2),encoding='utf8')
print(len(data['receipts']),'exact objects registered centrally; no saves submitted;',len(unregistered),'source/citation entries retained for task412 payload reconciliation')
