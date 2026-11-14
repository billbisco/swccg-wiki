import hashlib,json
from pathlib import Path
import requests
root=Path(__file__).parent;file=root/'batch7-reading-note-packet.json';rows=json.loads(file.read_bytes())
for row in rows:
    response=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles=row['title'],prop='revisions',rvprop='ids|content',rvslots='main'),timeout=60);response.raise_for_status();rev=response.json()['query']['pages'][0]['revisions'][0];old=rev['slots']['main']['content']
    note=row['section_text'];assert '== '+row['sectiontitle']+' ==' not in old
    row.update(text=old.rstrip()+'\n\n== '+row['sectiontitle']+' ==\n\n'+note,before_revid=rev['revid'],before_sha256=hashlib.sha256(old.encode()).hexdigest())
file.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
