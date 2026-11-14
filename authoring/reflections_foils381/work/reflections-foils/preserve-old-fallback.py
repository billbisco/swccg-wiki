import base64,json,subprocess
from pathlib import Path
root=Path(__file__).parent;body=(root/'old-primary-source.html').read_bytes()
code='BODY='+repr(base64.b64encode(body).decode())+'\n'+'''
import base64,gzip,hashlib,json,re,sys,urllib.request
from pathlib import Path
sys.path.insert(0,'/opt/swccg-ops/repos/swccg-wiki/ops');import wayback_worker as worker
def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':worker.UA}),timeout=60) as r:data=r.read()
    return gzip.decompress(data) if data[:2]==b'\\x1f\\x8b' else data
path=Path('/opt/swccg-res/snapshots/psa/reflections-first-family-primary-sources-381.html')
binary=base64.b64decode(BODY);path.write_bytes(binary);path.chmod(0o644);url='https://swccg.com/snapshots/psa/'+path.name
assert fetch(url)==binary
try:
    capture=worker.latest_capture(url) or worker.save_anon(url)
    replay=fetch(re.sub(r'(/web/\\d{14})/',r'\\1id_/',capture,count=1));assert replay==binary
    path.unlink();print(json.dumps(dict(url=url,capture=capture,verified=True,sha256=hashlib.sha256(replay).hexdigest(),bytes=len(replay),staging_removed=True)),flush=True)
except Exception as e:print(json.dumps(dict(url=url,verified=False,error=str(e),staging_path=str(path))),flush=True)
'''
p=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode(),stdout=subprocess.PIPE,check=True)
(root/'old-primary-preservation.json').write_bytes(p.stdout);print(p.stdout.decode())
