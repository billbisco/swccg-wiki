import base64,hashlib,html,json,subprocess
from pathlib import Path
root=Path(__file__).parent;rows=json.loads((root/'recovered-face-manifest.json').read_bytes())
body='<!doctype html><html><meta charset="utf-8"><title>Nine original Japanese SWCCG photographs</title><style>body{font:1rem system-ui;max-width:60rem;margin:2rem auto}img{max-width:100%}header{background:#fff3c2;padding:1rem}</style><header>Preserved original source photographs, retrieved 13 November 2026. PSA Set Registry. Each original JPEG is retained unchanged.</header><h1>Nine Japanese card faces</h1>'
hashes=[]
for row in rows:
    data=(root/row['file']).read_bytes();assert hashlib.sha256(data).hexdigest()==row['sha256'];hashes.append(row['sha256'])
    body+='<section><h2>'+html.escape(row['title'])+'</h2><p>Printing '+row['uid']+'. <a href="'+html.escape(row['gallery'],quote=True)+'">PSA Set Registry source gallery</a> · <a href="'+row['url']+'">Original photograph</a></p><img alt="'+html.escape(row['title'],quote=True)+'" src="data:image/jpeg;base64,'+base64.b64encode(data).decode()+'"></section>'
body+='</html>';(root/'recovered-source.html').write_text(body,encoding='utf8')
code='''
import base64,gzip,hashlib,json,re,sys,urllib.request
from pathlib import Path
sys.path.insert(0,'/opt/swccg-ops/repos/swccg-wiki/ops')
import wayback_worker as worker
def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':worker.UA}),timeout=60) as response:data=response.read()
    return gzip.decompress(data) if data[:2]==b'\\x1f\\x8b' else data
path=Path('/opt/swccg-res/snapshots/psa/japanese-nine-faces-369-v2.html');path.parent.mkdir(exist_ok=True,parents=True);path.parent.chmod(0o755)
binary=base64.b64decode(BODY);path.write_bytes(binary);path.chmod(0o644);url='https://swccg.com/snapshots/psa/'+path.name
assert fetch(url)==binary
try:
    capture=worker.latest_capture(url) or worker.save_anon(url);replay=fetch(re.sub(r'(/web/\\d{14})/',r'\\1id_/',capture,count=1));assert replay==binary
    hashes=[hashlib.sha256(base64.b64decode(x)).hexdigest() for x in re.findall(b'data:image/jpeg;base64,([A-Za-z0-9+/=]+)',replay)]
    assert hashes==HASHES
    path.unlink();print(json.dumps(dict(url=url,capture=capture,verified=True,sha256=hashlib.sha256(replay).hexdigest(),image_hashes=hashes,bytes=len(replay),staging_removed=not path.exists())),flush=True)
except Exception as error:print(json.dumps(dict(url=url,verified=False,error=str(error))),flush=True)
'''
code='BODY='+repr(base64.b64encode(body.encode()).decode())+'\nHASHES='+repr(hashes)+'\n'+code
r=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode(),stdout=subprocess.PIPE,check=True)
(root/'recovered-preservation.json').write_bytes(r.stdout);print(r.stdout.decode())
