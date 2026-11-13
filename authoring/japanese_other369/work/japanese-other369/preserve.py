import base64,hashlib,json,subprocess
from pathlib import Path
root=Path(__file__).parent
source=json.loads((root/'new-source.json').read_bytes());data=(root/source['file']).read_bytes()
html='<!doctype html><html><meta charset="utf-8"><title>Japanese Hoth 2-1B original PSA photograph</title><style>body{font:1rem system-ui;max-width:60rem;margin:2rem auto}img{max-width:100%}header{background:#fff3c2;padding:1rem}</style><header>Preserved source photograph, retrieved 13 November 2026. Original file retained unchanged.</header><h1>Japanese Hoth 2-1B</h1><p>PSA Set Registry gallery: StarWarsCollector_#1. PSA label identifies the 1998 Hoth Japanese Light Side card; certification 108070289.</p><p><a href="'+source['gallery']+'">Source gallery</a> · <a href="'+source['image']+'">Original photograph</a></p><img alt="Japanese Hoth 2-1B in PSA holder" src="data:image/jpeg;base64,'+base64.b64encode(data).decode()+'"></html>'
(root/'2-1b-source.html').write_text(html,encoding='utf8')
code='''
import base64,gzip,hashlib,json,re,sys,urllib.request
from pathlib import Path
sys.path.insert(0,'/opt/swccg-ops/repos/swccg-wiki/ops')
import wayback_worker as worker
def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':worker.UA}),timeout=60) as response:data=response.read()
    return gzip.decompress(data) if data[:2]==b'\\x1f\\x8b' else data
path=Path('/opt/swccg-res/snapshots/psa/japanese-hoth-2-1b-369.html')
path.parent.mkdir(exist_ok=True,parents=True);path.parent.chmod(0o755)
binary=base64.b64decode(BODY);path.write_bytes(binary);path.chmod(0o644)
url='https://swccg.com/snapshots/psa/'+path.name
assert fetch(url)==binary
try:
    capture=worker.latest_capture(url) or worker.save_anon(url)
    replay=fetch(re.sub(r'(/web/\\d{14})/',r'\\1id_/',capture,count=1));assert replay==binary
    image=base64.b64decode(re.search(b'data:image/jpeg;base64,([A-Za-z0-9+/=]+)',replay)[1]);assert hashlib.sha256(image).hexdigest()==IMAGE_SHA
    path.unlink();print(json.dumps(dict(url=url,capture=capture,verified=True,sha256=hashlib.sha256(replay).hexdigest(),image_sha256=IMAGE_SHA,bytes=len(replay),staging_removed=not path.exists())),flush=True)
except Exception as error:print(json.dumps(dict(url=url,verified=False,error=str(error))),flush=True)
'''
code='BODY='+repr(base64.b64encode(html.encode()).decode())+'\nIMAGE_SHA='+repr(hashlib.sha256(data).hexdigest())+'\n'+code
r=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode(),stdout=subprocess.PIPE,check=True)
(root/'preservation.json').write_bytes(r.stdout);print(r.stdout.decode())
