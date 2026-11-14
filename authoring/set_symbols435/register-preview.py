import base64,hashlib,json,subprocess,datetime
from pathlib import Path
p=Path(__file__).parent;deployment=json.loads((p/'preview-deployment.json').read_bytes());url=deployment['url'];path=deployment['source_backup_path'];commit=deployment['source_backup_commit']
j=json.loads(subprocess.check_output(['gh','api','repos/billbisco/swccg-wiki/contents/'+path+'?ref='+commit]));raw=base64.b64decode(j['content']);assert raw==(p/'preview.html').read_bytes();sha=hashlib.sha256(raw).hexdigest();assert sha==deployment['sha256']
subject=dict(kind='source_snapshot',title=url,content_sha256=sha,bytes=len(raw));receipt=dict(schema_version=1,subject=subject,storage=dict(kind='git',repository='https://github.com/billbisco/swccg-wiki',commit=commit,path=path),verification=dict(status='verified',independent=True,restored_sha256=sha,restored_bytes=len(raw),verified_at=datetime.datetime.now(datetime.timezone.utc).isoformat()))
request=dict(schema_version=1,subject=subject,source=dict(url=url,sha256=sha,bytes=len(raw)),backup_receipt=receipt,readiness=dict(ready=False,reason='Bill active absolute Archive.org hold; visual review page is independently backed up, not submitted or archived.',stage_bytes=0),owner='MemoryCoreChatGPT / swccg-guild/work#435',continuation='Keep all archive requests paused. Only after explicit Bill resumption may the existing server-wayback-owner stage/promote/submit and verify the exact HTML.',approval_scope=dict(story=435,authorization='Bill requested shared symbols and a visual test on14 November2026'))
code='REQUEST='+repr(request)+'\n'+'''import sys,json
from pathlib import Path
sys.path.insert(0,'/opt/swccg-ops/repos/swccg-wiki/ops');import preservation_registry as r
d=Path('/root/.local/state/swccg-wayback/registry');receipt=r.register(d,REQUEST);export=r.export_records(d);export['objects']=[o for o in export['objects'] if o['object_id']==receipt['object_id']]
print(json.dumps(dict(receipt=receipt,export=export)))
'''
result=json.loads(subprocess.check_output(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode()));result.update(backup_receipt=receipt,request=request);(p/'preview-preservation.json').write_text(json.dumps(result,indent=2),encoding='utf8');print('Public review HTML independently restored and registered with ready=false; no Archive.org request')
