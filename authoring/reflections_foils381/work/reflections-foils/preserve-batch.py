import base64,hashlib,html,json,subprocess,sys
from pathlib import Path
from source_registry import provenance
root=Path(__file__).parent;stage=sys.argv[1];assert stage.isalnum()
rows=json.loads((root/(stage+'-readings.json')).read_bytes())
body='<!doctype html><html><meta charset="utf-8"><title>Original physical SWCCG foil photographs — '+stage+'</title><style>body{font:1rem system-ui;max-width:60rem;margin:2rem auto}img{max-width:100%}header{background:#fff3c2;padding:1rem}</style><header>Original source photographs retained unchanged for wiki story 381. Source collection credits and original image URLs are recorded individually.</header>'
hashes=[]
for r in rows:
    data=(root/r['source_photo']).read_bytes();digest=hashlib.sha256(data).hexdigest();assert digest==r['source_sha256'];hashes.append(digest);p=provenance(r)
    body+='<section><h2>'+html.escape(r['article'])+'</h2><p>'+html.escape(r['product']+', '+r['side']+' Side foil. Source: '+p['credit'])+'. <a href="'+html.escape(p['url'],quote=True)+'">Source collection entry</a> · <a href="'+html.escape(r['source_url'],quote=True)+'">Original photograph</a>. SHA256 '+digest+'</p><img alt="'+html.escape(r['printed_title'],quote=True)+'" src="data:image/jpeg;base64,'+base64.b64encode(data).decode()+'"></section>'
body+='</html>';(root/(stage+'-source.html')).write_text(body,encoding='utf8')
code='BODY='+repr(base64.b64encode(body.encode()).decode())+'\nHASHES='+repr(hashes)+'\nSTAGE='+repr(stage)+'\n'+'''
import base64,gzip,hashlib,json,re,sys,urllib.request
from pathlib import Path
sys.path.insert(0,'/opt/swccg-ops/repos/swccg-wiki/ops');import wayback_worker as worker
def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':worker.UA}),timeout=60) as r:data=r.read()
    return gzip.decompress(data) if data[:2]==b'\\x1f\\x8b' else data
path=Path('/opt/swccg-res/snapshots/psa/reflections381-'+STAGE+'-originals.html');binary=base64.b64decode(BODY);path.write_bytes(binary);path.chmod(0o644)
url='https://swccg.com/snapshots/psa/'+path.name;assert fetch(url)==binary
try:
    capture=worker.latest_capture(url) or worker.save_anon(url);replay=fetch(worker.id_url(capture));assert replay==binary
    hashes=[hashlib.sha256(base64.b64decode(x)).hexdigest() for x in re.findall(b'data:image/jpeg;base64,([A-Za-z0-9+/=]+)',replay)];assert hashes==HASHES
    path.unlink();print(json.dumps(dict(url=url,capture=capture,verified=True,sha256=hashlib.sha256(replay).hexdigest(),image_hashes=hashes,bytes=len(replay),staging_removed=True)),flush=True)
except Exception as e:print(json.dumps(dict(url=url,verified=False,error=str(e),staging_path=str(path))),flush=True)
'''
p=subprocess.run(['ssh','-o','BatchMode=yes','gemp','python3','-'],input=code.encode(),stdout=subprocess.PIPE,check=True)
(root/(stage+'-preservation.json')).write_bytes(p.stdout);print(p.stdout.decode())
