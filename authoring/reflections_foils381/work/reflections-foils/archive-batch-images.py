"""Archive exact original wiki-image versions; verify binary payload and identity."""
import json,subprocess,sys
from pathlib import Path
import requests
root=Path(__file__).parent;stage=sys.argv[1]
files=json.loads((root/(stage+'-files-payload.json')).read_bytes());bytitle={f['title']:f for f in files}
r=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join(bytitle),prop='imageinfo',iiprop='url|timestamp|sha1|size|mime'),timeout=60);r.raise_for_status()
rows=[]
for p in r.json()['query']['pages']:
    f=bytitle[p['title']];info=p['imageinfo'][0];assert info['sha1']==f['sha1']
    rows.append(dict(title=p['title'],url=info['url'],image_sha256=f['sha256'],version=info['timestamp'],size=info['size'],mime=info['mime'],sha1=info['sha1']))
(root/(stage+'-image-versions.json')).write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
prior={r['title']:r for r in map(json.loads,(root/(stage+'-image-captures.jsonl')).read_text().splitlines())} if (root/(stage+'-image-captures.jsonl')).exists() else {}
rows=[r for r in rows if not prior.get(r['title'],{}).get('verified')]
code='ROWS='+repr(rows)+'\n'+'''
import hashlib,json,re,sys,urllib.request
sys.path.insert(0,'/opt/swccg-ops/repos/swccg-wiki/ops');import wayback_worker as worker
for row in ROWS:
    try:
        capture=worker.latest_capture(row['url']) or worker.save_anon(row['url'])
        with urllib.request.urlopen(worker.id_url(capture),timeout=60) as r:data=r.read();mime=r.headers.get('Content-Type','')
        digest=hashlib.sha256(data).hexdigest()
        assert data.startswith(b'\\xff\\xd8') and len(data)==row['size'] and digest==row['image_sha256'],('Image payload mismatch',mime,len(data))
        print(json.dumps(dict(row,capture=capture,verified=True,sha256=digest,bytes=len(data),capture_mime=mime)),flush=True)
    except Exception as e:print(json.dumps(dict(row,verified=False,error=str(e))),flush=True)
'''
p=subprocess.Popen(['ssh','-o','BatchMode=yes','gemp','python3','-'],stdin=subprocess.PIPE,stdout=subprocess.PIPE);p.stdin.write(code.encode());p.stdin.close()
with (root/(stage+'-image-captures.jsonl')).open('ab') as log:
    for line in p.stdout:log.write(line);log.flush();r=json.loads(line);print(r['title'],r['verified'],r.get('capture',r.get('error')),flush=True)
raise SystemExit(p.wait())
