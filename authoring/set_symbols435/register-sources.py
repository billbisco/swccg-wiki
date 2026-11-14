"""Restore independent source bytes and register held metadata; no archive client."""
import base64,hashlib,io,json,subprocess,tarfile,datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests
p=Path(__file__).parent;commit=(p/'wiki-commit.txt').read_text().strip();path='authoring/set_symbols435/shared-symbols.tar.xz'
j=json.loads(subprocess.check_output(['gh','api','repos/billbisco/swccg-wiki/contents/'+path+'?ref='+commit]))
if not j.get('content'):j=json.loads(subprocess.check_output(['gh','api','repos/billbisco/swccg-wiki/git/blobs/'+j['sha']]))
raw=base64.b64decode(j['content']);assert raw==(p/'shared-symbols.tar.xz').read_bytes()
sha=lambda b:hashlib.sha256(b).hexdigest();artifact=sha(raw)
with tarfile.open(fileobj=io.BytesIO(raw),mode='r:xz') as t:
    members={m.name:t.extractfile(m).read() for m in t if m.isfile()}
total=sum(map(len,members.values()));now=datetime.datetime.now(datetime.timezone.utc).isoformat();rows=[]
manifest=json.loads((p/'symbols/manifest.json').read_bytes());library=(p/'cardmaker-commit.txt').read_text().strip()
for row in manifest['symbols']:
    rows.append((f'cardmaker/{row["source"]}',manifest['master_commit'],row['source']))
    rows.append(('symbols/'+row['file'],library,'assets/symbols/'+row['file']))
for src in ['assets/icons/SET-ICONS-PROVENANCE.md','assets/icons/SET-ICONS-PROVENANCE.json','tools/set_spheres/sources.json']:
    rows.append(('cardmaker/'+src,manifest['master_commit'],src))
rows.append(('symbols/manifest.json',library,'assets/symbols/manifest.json'))
def checked(row):
    member,rev,src=row;data=members[member];url='https://raw.githubusercontent.com/billbisco/swccg-cardmaker/'+rev+'/'+src
    r=requests.get(url,timeout=60);r.raise_for_status();assert r.content==data,(url,'Source payload differs')
    subject=dict(kind='source_snapshot',title=url,content_sha256=sha(data),bytes=len(data))
    receipt=dict(schema_version=1,subject=subject,storage=dict(kind='git',repository='https://github.com/billbisco/swccg-wiki',commit=commit,path=path,container='tar.xz',member=member,artifact_sha256=artifact,artifact_bytes=len(raw),uncompressed_bytes=total),verification=dict(status='verified',independent=True,restored_sha256=sha(data),restored_bytes=len(data),verified_at=now,restored_container_sha256=artifact,restored_container_bytes=len(raw)))
    return dict(schema_version=1,subject=subject,source=dict(url=url,sha256=sha(data),bytes=len(data)),backup_receipt=receipt,readiness=dict(ready=False,reason='Bill active Archive.org hold; metadata only. Shared-library pilot pending visual/text decision and printing-variant verification.',stage_bytes=0),owner='MemoryCoreChatGPT / swccg-guild/work#435',continuation='Keep all external archive requests paused. After explicit Bill resumption and source/variant acceptance, existing server-wayback-owner alone stages/promotes/submits and verifies exact payloads; no private saver.',approval_scope=dict(story=435,authorization='Bill authorized shared CardMaker-first symbol cleanup and a visual pilot on14 November2026'))
with ThreadPoolExecutor(max_workers=3) as pool:requests_meta=list(pool.map(checked,rows))
(p/'central-registration-requests.json').write_text(json.dumps(requests_meta,ensure_ascii=False,indent=2),encoding='utf8')
code='REQUESTS='+repr(requests_meta)+'\n'+'''import sys,json
from pathlib import Path
sys.path.insert(0,'/opt/swccg-ops/repos/swccg-wiki/ops')
import preservation_registry as registry
d=Path('/root/.local/state/swccg-wayback/registry');assert d.is_dir()
receipts=[registry.register(d,r) for r in REQUESTS]
export=registry.export_records(d);ids={r['object_id'] for r in receipts};export['objects']=[r for r in export['objects'] if r['object_id'] in ids]
print(json.dumps(dict(receipts=receipts,export=export)))
'''
result=json.loads(subprocess.check_output(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode()))
(p/'central-registration-receipts.json').write_text(json.dumps(result['receipts'],indent=2),encoding='utf8');(p/'central-registry-export.json').write_text(json.dumps(result['export'],indent=2),encoding='utf8')
(p/'source-readback.json').write_text(json.dumps([r['backup_receipt'] for r in requests_meta],indent=2),encoding='utf8')
print(len(requests_meta),'exact raw sources independently restored and checked; metadata registered centrally with ready=false; no Archive.org request or submission')
