"""Guarded static frontend deployments; no engine, database or service reconfiguration."""
import base64,hashlib,json,subprocess,sys
from pathlib import Path
p=Path(__file__).parent;phase=sys.argv[1];assert phase in ['shared','test','play'];m=json.loads((p/'build-manifest.json').read_bytes());items=[]
sha=lambda b:hashlib.sha256(b).hexdigest()
def add(target,source,old=None,bind=False):
    raw=(p/'product'/source).read_bytes();prior=[]
    receipt=p/(phase+'-deployment.json')
    if receipt.exists():prior=[r.get('after_sha256') or r.get('sha256') for r in json.loads(receipt.read_bytes())['receipts'] if r['path']==target]
    items.append(dict(path=target,data=base64.b64encode(raw).decode(),sha256=sha(raw),expected_sha256=sha(old) if old is not None else None,prior_own_sha256=prior,bind_file=bind))
if phase=='shared':
    for name in [m['js'],m['css']]:add('/opt/swccg-wiki/chrome/'+name,name)
    add('/opt/swccg-wiki/SwccgChrome.php','SwccgChrome.php',(p/'SwccgChrome.live-before.php').read_bytes(),True)
    add('/opt/swccg-res/snapshots/review/shared-search-449/scomp.html','scomp.html')
else:
    root='/opt/swccg-gemp-test' if phase=='test' else '/opt/gemp-swccg'
    prefix=root+'/src/gemp-swccg-async/src/main/web/'
    for name in ['js/gemp-016/cards/CardFilter.js','deckBuild.html']:
        original=subprocess.check_output(['git','-C','work/search-gemp-source','show',m['gempSourceCommit']+':src/gemp-swccg-async/src/main/web/'+name])
        add(prefix+name,Path(name).name,original)
    add(prefix+'searchPilot.html','searchPilot.html')
code='ITEMS='+repr(items)+'\nPHASE='+repr(phase)+'\n'+'''import pathlib,hashlib,base64,json,os,subprocess,time
backup=pathlib.Path('/mnt/HC_Volume_107153504/work/memorycore-shared-search-449-20261114');backup.mkdir(exist_ok=True)
(backup/'README.txt').write_text('MemoryCoreChatGPT / Story449: guarded static frontend rollback copies and deployment receipts; keep for pilot review. No engine/database/configuration changes.\\n')
(backup/'KEEP').touch()
assert pathlib.Path('/opt/swccg-res/snapshots').is_dir()
if PHASE=='shared':
    mount=subprocess.check_output(['findmnt','-n','-o','TARGET','/opt/swccg-res/snapshots']).decode().strip();assert mount=='/opt/swccg-res/snapshots'
for item in ITEMS:
    target=pathlib.Path(item['path']);raw=base64.b64decode(item['data']);assert hashlib.sha256(raw).hexdigest()==item['sha256']
    if target.exists():
        old=target.read_bytes();oldsha=hashlib.sha256(old).hexdigest()
        assert oldsha in [item['sha256'],item['expected_sha256']]+item['prior_own_sha256'],(str(target),'Concurrent or pre-existing different file; stop')
    else:assert item['expected_sha256'] is None,(str(target),'Expected old file missing')
    if item['path'].endswith('.php'):
        check=subprocess.run(['docker','exec','-i','swccg_wiki','php','-l','/dev/stdin'],input=raw,stdout=subprocess.PIPE,stderr=subprocess.STDOUT);assert check.returncode==0,check.stdout.decode()
receipts=[]
for item in ITEMS:
    target=pathlib.Path(item['path']);raw=base64.b64decode(item['data']);before=target.read_bytes() if target.exists() else None
    if before==raw:receipts.append(dict(path=str(target),sha256=item['sha256'],already_applied=True));continue
    target.parent.mkdir(parents=True,exist_ok=True)
    saved=backup/(PHASE+'-'+hashlib.sha256(str(target).encode()).hexdigest()[:12]+'-'+(hashlib.sha256(before).hexdigest()[:12] if before else 'new')+'.before')
    if before is not None:
        assert not saved.exists() or saved.read_bytes()==before;saved.write_bytes(before)
    oldstat=target.stat() if target.exists() else None
    if item['bind_file']:
        with target.open('wb') as f:f.write(raw);f.flush();os.fsync(f.fileno())
    else:
        tmp=target.with_name(target.name+'.memorycore449.tmp');assert not tmp.exists();tmp.write_bytes(raw);tmp.chmod(oldstat.st_mode&0o777 if oldstat else 0o644)
        if oldstat:os.chown(tmp,oldstat.st_uid,oldstat.st_gid)
        os.replace(tmp,target)
    assert target.read_bytes()==raw
    receipts.append(dict(path=str(target),before_sha256=hashlib.sha256(before).hexdigest() if before is not None else None,after_sha256=item['sha256'],bytes=len(raw),backup=str(saved) if before is not None else None))
if PHASE=='shared':subprocess.run(['docker','exec','swccg_wiki','apachectl','graceful'],check=True)
(backup/(PHASE+'-deployment.json')).write_text(json.dumps(receipts,indent=2))
print(json.dumps(dict(phase=PHASE,receipts=receipts,static_only=True,engine_database_unchanged=True)))
'''
r=subprocess.check_output(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode());(p/(phase+'-deployment.json')).write_bytes(r);print(phase,len(items),'guarded frontend files deployed with rollback copies')
