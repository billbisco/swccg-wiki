import hashlib,json
import requests
from pathlib import Path
root=Path(__file__).parent
receipts={r['title']:r for r in map(json.loads,(root/'batch3-new-receipts.jsonl').read_text().splitlines())};rows=json.loads((root/'batch3-new-packet.json').read_bytes());out=[]
for row in rows:
    old=row['text'];new=old.replace('Icon-set-Cloud City.png','Icon-set-Cloud-City.png')
    if new!=old:
        response=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles=row['title'],prop='revisions',rvprop='ids|content',rvslots='main'),timeout=60);response.raise_for_status();rev=response.json()['query']['pages'][0]['revisions'][0];actual=rev['slots']['main']['content'];assert actual.rstrip()==old.rstrip(),row['title']
        out.append(dict(title=row['title'],text=actual.replace('Icon-set-Cloud City.png','Icon-set-Cloud-City.png'),before_revid=rev['revid'],before_sha256=hashlib.sha256(actual.encode()).hexdigest(),section=0,summary='Use the existing Cloud City expansion icon file (#381)'))
(root/'batch3-correction-packet.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
