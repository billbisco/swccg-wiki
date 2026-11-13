import json,subprocess
from pathlib import Path
root=Path(__file__).parent
code='''
import gzip,hashlib,json,re,sys,urllib.request
from pathlib import Path
sys.path.insert(0,'/opt/swccg-ops/repos/swccg-wiki/ops')
import wayback_worker as worker
path=Path('/opt/swccg-res/snapshots/psa/japanese-nine-faces-369-v2.html');url='https://swccg.com/snapshots/psa/'+path.name
try:
    binary=path.read_bytes();capture=worker.latest_capture(url)
    if not capture:capture=worker.save_anon(url)
    with urllib.request.urlopen(urllib.request.Request(re.sub(r'(/web/\\d{14})/',r'\\1id_/',capture,count=1),headers={'User-Agent':worker.UA}),timeout=180) as response:data=response.read()
    if data[:2]==b'\\x1f\\x8b':data=gzip.decompress(data)
    assert data==binary
    path.unlink();print(json.dumps(dict(url=url,capture=capture,verified=True,sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),staging_removed=not path.exists())),flush=True)
except Exception as error:print(json.dumps(dict(url=url,verified=False,error=str(error))),flush=True)
'''
r=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode(),stdout=subprocess.PIPE,check=True)
(root/'recovered-preservation-v2.json').write_bytes(r.stdout);print(r.stdout.decode())
