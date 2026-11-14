"""Try SPN resource capture, then verify every original binary independently."""
import base64,html,json,subprocess,sys
from pathlib import Path
import requests
root=Path(__file__).parent;stage=sys.argv[1];assert stage.isalnum()
files=json.loads((root/(stage+'-files-payload.json')).read_bytes());bytitle={r['title']:r for r in files}
response=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join(bytitle),prop='imageinfo',iiprop='url|timestamp|sha1|size|mime'),timeout=60);response.raise_for_status();rows=[]
for page in response.json()['query']['pages']:
    f=bytitle[page['title']];i=page['imageinfo'][0];assert i['sha1']==f['sha1'];rows.append(dict(title=page['title'],url=i['url'],image_sha256=f['sha256'],version=i['timestamp'],size=i['size'],mime=i['mime'],sha1=i['sha1']))
body='<!doctype html><html><meta charset="utf-8"><title>Reflections foil original-image preservation '+stage+'</title><style>body{font:1rem system-ui;max-width:60rem;margin:2rem auto}img{max-width:100%;height:auto}</style><h1>Original uploaded foil photographs</h1><p>Preservation gallery for story 381. Each image source is the full-resolution wiki original, not a thumbnail. Every binary must be checked independently before its version is marked preserved.</p>'
for r in rows:body+='<section><h2>'+html.escape(r['title'])+'</h2><p>Version '+r['version']+'; original SHA256 '+r['image_sha256']+'</p><img src="'+html.escape(r['url'],quote=True)+'" alt="'+html.escape(r['title'],quote=True)+'"></section>'
body+='</html>';binary=body.encode();(root/(stage+'-image-gallery.html')).write_bytes(binary)
code='BODY='+repr(base64.b64encode(binary).decode())+'\nROWS='+repr(rows)+'\nSTAGE='+repr(stage)+'\n'+'''
import base64,gzip,hashlib,json,re,sys,time,urllib.request
from pathlib import Path
sys.path.insert(0,'/opt/swccg-ops/repos/swccg-wiki/ops');import wayback_worker as worker
def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':worker.UA}),timeout=90) as r:data=r.read();final=r.geturl();mime=r.headers.get('Content-Type','')
    return (gzip.decompress(data) if data[:2]==b'\\x1f\\x8b' else data),final,mime
path=Path('/opt/swccg-res/snapshots/psa/reflections381-'+STAGE+'-wiki-originals.html');binary=base64.b64decode(BODY);path.write_bytes(binary);path.chmod(0o644);url='https://swccg.com/snapshots/psa/'+path.name
assert fetch(url)[0]==binary
try:
    capture=worker.latest_capture(url) or worker.save_anon(url);replay=fetch(worker.id_url(capture))[0];assert replay==binary
    print(json.dumps(dict(kind='gallery',url=url,capture=capture,verified=True,sha256=hashlib.sha256(replay).hexdigest(),bytes=len(replay),staging_removed=False,staging_path=str(path))),flush=True)
except Exception as e:
    print(json.dumps(dict(kind='gallery',url=url,verified=False,error=str(e),staging_path=str(path))),flush=True);raise SystemExit(0)
timestamp=re.search(r'/web/(\\d{14})',capture)[1]
verified_images=0
for row in ROWS:
    try:
        candidate='https://web.archive.org/web/'+timestamp+'id_/'+row['url'];data,final,mime=fetch(candidate);digest=hashlib.sha256(data).hexdigest()
        assert data.startswith(b'\\xff\\xd8') and len(data)==row['size'] and digest==row['image_sha256'],('Binary mismatch',mime,len(data))
        assert re.search(r'/web/\\d{14}',final),final
        final=re.sub(r'(/web/\\d{14})id_/',r'\\1/',final)
        print(json.dumps(dict(row,kind='image',capture=final,verified=True,sha256=digest,bytes=len(data),capture_mime=mime,method='Gallery resource capture; exact full-resolution binary comparison')),flush=True)
        verified_images+=1
    except Exception as e:print(json.dumps(dict(row,kind='image',verified=False,error=str(e))),flush=True)
    time.sleep(5)
if verified_images==len(ROWS):path.unlink()
print(json.dumps(dict(kind='gallery-summary',url=url,verified=verified_images==len(ROWS),verified_images=verified_images,total_images=len(ROWS),staging_removed=not path.exists(),staging_path=str(path))),flush=True)
'''
p=subprocess.Popen(['ssh','-o','BatchMode=yes','gemp','python3','-'],stdin=subprocess.PIPE,stdout=subprocess.PIPE);p.stdin.write(code.encode());p.stdin.close();report=[]
prior={r['title']:r for r in map(json.loads,(root/(stage+'-image-captures.jsonl')).read_text().splitlines()) if r.get('verified')} if (root/(stage+'-image-captures.jsonl')).exists() else {}
with (root/(stage+'-image-captures.jsonl')).open('ab') as log:
    for line in p.stdout:
        r=json.loads(line);report.append(r)
        if r['kind']=='image':
            if r['verified'] or not (prior.get(r['title'],{}).get('verified') and prior[r['title']]['version']==r['version']):log.write(line);log.flush()
            print(r['title'],r['verified'],r.get('error',''),flush=True)
        else:print('gallery',r['verified'],r.get('capture',r.get('error')),flush=True)
(root/(stage+'-image-gallery-results.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');raise SystemExit(p.wait())
