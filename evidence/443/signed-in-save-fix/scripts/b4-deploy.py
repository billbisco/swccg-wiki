from b4common import *
pr=gh('repos/billbisco/swccg-wiki/pulls/64');assert pr['merged'];revision=pr['merge_commit_sha'];info=gh('repos/billbisco/swccg-wiki/contents/chrome/card-image-viewer.js?ref='+revision);data=base64.b64decode(info['content']);assert data==(ROOT/'source/chrome/card-image-viewer.js').read_bytes();before=subprocess.check_output(['git','-C',str(ROOT/'source'),'show','HEAD^:chrome/card-image-viewer.js']);save('source-manifest.json',json.loads((ROOT/'source/chrome/card-image-pilot.json').read_bytes()))
code="""from pathlib import Path
import json,base64,hashlib,datetime
root=Path('/mnt/HC_Volume_107153504/work/memorycore-443-signed-in-save-fix-20261114');root.mkdir(parents=True,exist_ok=True);target=Path('/opt/swccg-wiki/chrome/card-image-viewer.js');old=target.read_bytes();new=base64.b64decode(DATA);assert hashlib.sha256(old).hexdigest()in[OLD,hashlib.sha256(new).hexdigest()];backup=root/'before-base-dependency-fix.js'
if not backup.exists():backup.write_bytes(old)
target.write_bytes(new);assert target.read_bytes()==new
print(json.dumps({'source_revision':REVISION,'sha256':hashlib.sha256(new).hexdigest(),'old_sha256':OLD,'rollback':str(backup),'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'server_configuration_changes':0,'wiki_content_edits':0}))
""".replace('DATA',repr(base64.b64encode(data).decode())).replace('OLD',repr(sha(before))).replace('REVISION',repr(revision))
r=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3 -'],input=code.encode(),capture_output=True);assert r.returncode==0,r.stderr.decode(errors='replace')[-1200:];save('deploy.json',json.loads(r.stdout));print(r.stdout.decode())
s=(ROOT/'batch2-purge.py').read_text(encoding='utf-8').replace('from b2common import *','from b4common import *').replace("titles=[r['title']for r in read('plan.json')]","titles=list(read('source-manifest.json')['pages'])")
(ROOT/'b4-purge.py').write_bytes(s.encode())
