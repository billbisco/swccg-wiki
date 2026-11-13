import subprocess
from pathlib import Path
root=Path(__file__).parent
code='''
import gzip,hashlib,json,re,sys,urllib.request
from pathlib import Path
sys.path.insert(0,'/opt/swccg-ops/repos/swccg-wiki/ops')
import wayback_worker as worker
source=Path('/mnt/HC_Volume_107153504/work/memorycorechatgpt-infobox287-20261113/bgg-snapshot.html')
path=Path('/opt/swccg-res/snapshots/bgg/swccg-card-list-33565-287.html')
path.parent.mkdir(parents=True,exist_ok=True);path.parent.chmod(0o755)
binary=source.read_bytes();path.write_bytes(binary);path.chmod(0o644)
url='https://swccg.com/snapshots/bgg/'+path.name
def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':worker.UA}),timeout=60) as response:data=response.read()
    return gzip.decompress(data) if data[:2]==b'\\x1f\\x8b' else data
assert fetch(url)==binary
try:
    capture=worker.latest_capture(url) or worker.save_anon(url)
    replay=fetch(re.sub(r'(/web/\\d{14})/',r'\\1id_/',capture,count=1))
    assert replay==binary and b'swccgcardlist4.2' in replay and b'Whaleyland' in replay
    path.unlink()
    print(json.dumps(dict(url=url,capture=capture,verified=True,sha256=hashlib.sha256(replay).hexdigest(),bytes=len(replay),staging_removed=not path.exists())),flush=True)
except Exception as error:print(json.dumps(dict(url=url,verified=False,error=str(error))),flush=True)
'''
result=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode(),stdout=subprocess.PIPE,check=True)
(root/'bgg-preservation.json').write_bytes(result.stdout)
print(result.stdout.decode())
