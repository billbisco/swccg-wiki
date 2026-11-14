"""Attach actual independent readback receipts to existing registered objects."""
import hashlib,json,subprocess
from datetime import datetime,timezone
from pathlib import Path
root=Path(__file__).parent;file=root/'central-registration-backed-requests.json'
proof=json.loads((root/'images-independent-readback.json').read_bytes());assert proof['passed']
byhash={r['sha256']:r for r in proof['paths']}
if file.exists():requests=json.loads(file.read_bytes())
else:
    requests=json.loads((root/'central-registration-requests.json').read_bytes())
    for request in requests:
        subject=request['subject'];row=byhash[subject['content_sha256']];assert row['bytes']==subject['bytes'] and row['independently_restored']
        receipt=dict(schema_version=1,subject=subject,storage=dict(kind='git',repository=row['repository'],commit=row['commit'],path=row['path']),verification=dict(status='verified',independent=True,restored_sha256=row['sha256'],restored_bytes=row['bytes'],verified_at=datetime.now(timezone.utc).isoformat()))
        request.update(generation=1,backup_receipt=receipt)
        request['source']['checked_evidence']=dict(path='images-independent-readback.json',sha256=hashlib.sha256((root/'images-independent-readback.json').read_bytes()).hexdigest())
        request['readiness']=dict(ready=True,reason='Exact checked original bytes independently restored from immutable Git backup; existing server owner may preserve later under task412 and its durable circuit; no client submission',stage_bytes=0)
        request['continuation']='Existing server-wayback-owner alone promotes/submits when its durable circuit permits; verify exact raw replay bytes before adding File/citation capture links. Publication is already complete; task412 owns preservation follow-up.'
    file.write_text(json.dumps(requests,ensure_ascii=False,indent=2),encoding='utf8')
code='REQUESTS='+repr(requests)+'\n'+'''import json,sys
from pathlib import Path
sys.path.insert(0,'/opt/swccg-ops/repos/swccg-wiki/ops')
import preservation_registry as registry
directory=Path('/root/.local/state/swccg-wayback/registry');assert directory.is_dir()
receipts=[registry.register(directory,r) for r in REQUESTS]
print(json.dumps(dict(receipts=receipts,export=registry.export_records(directory))))
'''
result=json.loads(subprocess.check_output(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode()))
assert all(r['state']=='ready' and not r['submitted'] for r in result['receipts'])
original=root/'central-initial-registration-receipts.json'
if not original.exists():original.write_bytes((root/'central-registration-receipts.json').read_bytes())
queue=json.loads((root/'preservation-queue.json').read_bytes())
for request,receipt in zip(requests,result['receipts']):queue[request['source']['url']]['central_registration']=receipt
for name,data in [('central-registration-receipts.json',result['receipts']),('central-registry-server-export.json',result['export']),('preservation-queue.json',queue)]:
    (root/name).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
print(len(result['receipts']),'central objects now have independently verified backup receipts; ready for existing owner, not submitted or captured')
