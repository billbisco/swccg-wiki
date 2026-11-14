from b3common import *
pr=gh('repos/billbisco/swccg-wiki/pulls/62');assert pr['merged'];revision=pr['merge_commit_sha'];names=['card-image-viewer.js','card-image-viewer.css','card-image-preferences.php','card-image-pilot.json']+['i18n/'+x+'.json'for x in['en','fr','de','es','ja']];packet=[]
for n in names:
 f='chrome/'+n;info=gh('repos/billbisco/swccg-wiki/contents/'+f+'?ref='+revision);new=base64.b64decode(info['content']);assert new==(ROOT/'source'/f).read_bytes();old=subprocess.check_output(['git','-C',str(ROOT/'source'),'show','HEAD^:'+f]);packet.append({'path':n,'old_sha256':sha(old),'new_sha256':sha(new),'payload':base64.b64encode(new).decode()})
code="""from pathlib import Path
import json,hashlib,base64,datetime
root=Path('/mnt/HC_Volume_107153504/work/memorycore-443-settings-correction-20261114');root.mkdir(parents=True,exist_ok=True);chrome=Path('/opt/swccg-wiki/chrome');result=[]
for item in PACKET:
 target=chrome/item['path'];assert target.resolve().is_relative_to(chrome.resolve());old=target.read_bytes();new=base64.b64decode(item['payload']);assert hashlib.sha256(old).hexdigest()in[item['old_sha256'],item['new_sha256']],item['path'];assert hashlib.sha256(new).hexdigest()==item['new_sha256']
 backup=root/'before'/item['path'];backup.parent.mkdir(parents=True,exist_ok=True)
 if not backup.exists():backup.write_bytes(old)
 target.write_bytes(new);assert target.read_bytes()==new;result.append({'path':item['path'],'sha256':item['new_sha256'],'rollback':str(backup)})
print(json.dumps({'source_revision':REVISION,'files':result,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'server_configuration_changes':0}))
""".replace('PACKET',repr(packet)).replace('REVISION',repr(revision))
r=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3 -'],input=code.encode(),capture_output=True);assert r.returncode==0,r.stderr.decode(errors='replace')[-1500:];save('deploy.json',json.loads(r.stdout));print(json.dumps({'deployed_assets':len(packet),'revision':revision}))
