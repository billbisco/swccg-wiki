import json,re,hashlib,xml.etree.ElementTree as ET
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests
p=Path(__file__).parent;heads=json.loads((p/'source-heads.json').read_bytes());names=set()
for h in heads.values():
    if not h.get('revisions'):continue
    text=h['revisions'][0]['slots']['main']['content'];m=re.search(r'^\|\s*image\s*=([^\n]+)',text,re.M)
    if m:names.add('File:'+m.group(1).strip())
    for name in re.findall(r'(?:Media:|File:)([^\]|]+\.txt)',text):names.add('File:'+name.strip())
r=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join(sorted(names)),prop='imageinfo|revisions',iiprop='url|sha1|timestamp|size|mime',rvprop='ids|content',rvslots='main'),timeout=60);r.raise_for_status();files={h['title']:h for h in r.json()['query']['pages']};out=[]
def fetch(item):
    title,h=item;info=h['imageinfo'][0];name=title[5:];folder='decks' if name.endswith('.txt') else 'faces';f=p/folder/name;f.parent.mkdir(exist_ok=True)
    if f.exists() and hashlib.sha1(f.read_bytes()).hexdigest()==info['sha1']:raw=f.read_bytes()
    else:
        r=requests.get(info['url'],timeout=60);r.raise_for_status();raw=r.content;assert hashlib.sha1(raw).hexdigest()==info['sha1'],title;f.write_bytes(raw)
    rec=dict(title=title,local_file=f.relative_to(p).as_posix(),url=info['url'],timestamp=info['timestamp'],sha1=info['sha1'],sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw),mime=info['mime'])
    if folder=='decks':
        xml=ET.fromstring(raw);print('XML',name,ET.tostring(xml,encoding='unicode')[:620].replace('\n',' '),flush=True)
    return rec
with ThreadPoolExecutor(max_workers=3) as pool:out=list(pool.map(fetch,files.items()))
(p/'files.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8');print('Saved',len(out),'exact original card faces and deck XML files')
