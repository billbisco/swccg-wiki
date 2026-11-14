"""Metadata only. No Archive.org calls or worker activation."""
import datetime,hashlib,json,subprocess
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests
p=Path(__file__).parent;proof=json.loads((p/'source-readback.json').read_bytes());manifest=json.loads((p/'build-manifest.json').read_bytes())
members={r['member']:r for r in proof['members']};now=datetime.datetime.now(datetime.timezone.utc).isoformat();rows=[]
for f in json.loads((p/'files.json').read_bytes()):
    rows.append(dict(subject=dict(kind='wiki_file_version',title=f['title'],upload_timestamp=f['timestamp'],original_version_url=f['url'],content_sha256=f['sha256'],bytes=f['bytes']),url=f['url'],member=f['local_file']))
for r in json.loads((p/'revision-ledger.json').read_bytes()):
    rows.append(dict(subject=dict(kind='wiki_revision',title=r['title'],revision_id=r['revision_id'],content_sha256=r['sha256'],bytes=r['bytes']),url=r['url'],member=r['member']))
for member,url in [('product/'+manifest['js'],'https://wiki.swccg.com/chrome/'+manifest['js']),('product/'+manifest['css'],'https://wiki.swccg.com/chrome/'+manifest['css']),('product/scomp.html','https://swccg.com/snapshots/review/shared-search-449/scomp.html'),('product/searchPilot.html','https://test.swccg.com/gemp-swccg/searchPilot.html'),('product/searchPilot.html','https://play.swccg.com/gemp-swccg/searchPilot.html')]:
    r=members[member];rows.append(dict(subject=dict(kind='source_snapshot',title=url,content_sha256=r['sha256'],bytes=r['bytes']),url=url,member=member))
def checked(row):
    subject=row['subject'];member=members[row['member']]
    assert (subject['content_sha256'],subject['bytes'])==(member['sha256'],member['bytes'])
    r=requests.get(row['url'],timeout=60);r.raise_for_status();assert (hashlib.sha256(r.content).hexdigest(),len(r.content))==(member['sha256'],member['bytes']),row['url']
    backup=dict(schema_version=1,subject=subject,storage=dict(kind='git',repository=proof['repository'],commit=proof['commit'],path=proof['path'],container='tar.xz',member=row['member'],artifact_sha256=proof['artifact_sha256'],artifact_bytes=proof['artifact_bytes'],uncompressed_bytes=proof['uncompressed_bytes']),verification=dict(status='verified',independent=True,restored_sha256=member['sha256'],restored_bytes=member['bytes'],verified_at=now,restored_container_sha256=proof['artifact_sha256'],restored_container_bytes=proof['artifact_bytes']))
    return dict(schema_version=1,subject=subject,source=dict(url=row['url'],sha256=member['sha256'],bytes=member['bytes']),backup_receipt=backup,readiness=dict(ready=False,reason='Bill active absolute Archive.org hold. Exact source/version independently backed up; not submitted or archived.',stage_bytes=0),owner='MemoryCoreChatGPT / swccg-guild/work#449',continuation='Keep every Archive.org request paused. After Bill explicitly resumes, existing server-wayback-owner alone may stage/promote/submit/check exact payloads and complete version/File mappings; no private saver.',approval_scope=dict(story=449,authorization='Bill authorized source-backed Wiki/GEMP/own SCOMPLINK search pilot on14 November2026'))
with ThreadPoolExecutor(max_workers=3) as pool:meta=list(pool.map(checked,rows))
(p/'central-registration-requests.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf8')
code='REQUESTS='+repr(meta)+'\n'+'''import sys,json
from pathlib import Path
sys.path.insert(0,'/opt/swccg-ops/repos/swccg-wiki/ops');import preservation_registry as r
d=Path('/root/.local/state/swccg-wayback/registry');assert d.is_dir()
known={o['object_id']:o for o in r.export_records(d)['objects']};receipts=[]
for q in REQUESTS:
    key=r.registration_object_id(q['subject'],q['source']);old=known.get(key)
    if old:
        # Retain a peer's exact-version mapping/owner and immutable history.
        previous=json.loads((d/old['record']).read_text());entry=r.register(d,previous);entry['reused_existing_mapping']=True
    else:
        entry=r.register(d,q);entry['reused_existing_mapping']=False
    receipts.append(entry)
ids={q['object_id'] for q in receipts};export=r.export_records(d);export['objects']=[o for o in export['objects'] if o['object_id'] in ids]
assert len(export['objects'])==len(ids)
assert all(not q['submitted'] and (q['reused_existing_mapping'] or q['state']=='awaiting_stage') for q in receipts),receipts
print(json.dumps(dict(receipts=receipts,export=export)))
'''
result=json.loads(subprocess.check_output(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode()))
(p/'central-registration-receipts.json').write_text(json.dumps(result['receipts'],indent=2),encoding='utf8');(p/'central-registry-export.json').write_text(json.dumps(result['export'],ensure_ascii=False,indent=2),encoding='utf8')
print(len(meta),'exact source/version objects independently restored, live bytes checked, centrally registered ready=false; no Archive.org request')
