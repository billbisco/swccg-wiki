from b2common import *
pr=gh('repos/billbisco/swccg-wiki/pulls/58');assert pr['merged'];revision=pr['merge_commit_sha'];info=gh('repos/billbisco/swccg-wiki/contents/chrome/card-image-pilot.json?ref='+revision);data=base64.b64decode(info['content']);assert data==(ROOT/'source/chrome/card-image-pilot.json').read_bytes();titles=list(json.loads(data)['pages'])
code="""from pathlib import Path
import base64,hashlib,json,subprocess,urllib.parse,datetime
root=Path('/mnt/HC_Volume_107153504/work/memorycore-443-ovs1-batch2-20261114');root.mkdir(parents=True,exist_ok=True);target=Path('/opt/swccg-wiki/chrome/card-image-pilot.json');new=base64.b64decode(DATA);old=target.read_bytes();backup=root/'before-batch2-manifest.json'
assert hashlib.sha256(old).hexdigest()in['4f2ed39a2d45fcda9bdb0844fc2bd403a11787d549d49269a8e3ef15167e0f36',hashlib.sha256(new).hexdigest()]
if not backup.exists():backup.write_bytes(old)
target.write_bytes(new);assert target.read_bytes()==new
print(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_revision':REVISION,'sha256':hashlib.sha256(new).hexdigest(),'titles':TITLES,'rollback_manifest':str(backup),'server_configuration_changes':0}))
""".replace('DATA',repr(base64.b64encode(data).decode())).replace('REVISION',repr(revision)).replace('TITLES',repr(titles))
r=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3 -'],input=code.encode(),capture_output=True);assert r.returncode==0,r.stderr.decode(errors='replace')[-1000:];save('deploy.json',json.loads(r.stdout));print(r.stdout.decode())
