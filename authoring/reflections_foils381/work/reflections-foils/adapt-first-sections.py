import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import requests
root=Path(__file__).parent;rows=json.loads((root/'first-family-final-packet.json').read_bytes());baseline=json.loads((root/'first-family-heads.json').read_bytes())
def fetch(batch):
    r=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join(batch),prop='revisions',rvprop='ids|content',rvslots='main',rvsection=0),timeout=60);r.raise_for_status();return r.json()['query']['pages']
leads={};titles=[r['title'] for r in rows]
with ThreadPoolExecutor(max_workers=3) as pool:
    for batch in pool.map(fetch,[titles[i:i+25] for i in range(0,len(titles),25)]):leads.update({p['title']:p for p in batch})
changed=[]
for row in rows:
    title=row['title'];lead=leads[title]['revisions'][0]['slots']['main']['content'];old=baseline[title]['revisions'][0]['slots']['main']['content']
    if lead.rstrip() not in [old.rstrip(),row['text'].rstrip()]:
        assert old.startswith(lead.rstrip()),title
        row['section']=None
        row['atomic_reason']='Existing article has real sections outside Card. Navigation and inherited citation repairs span sections; one exact full-source revision/hash guard protects all unchanged content.'
        changed.append(title)
(root/'first-family-final-packet.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
(root/'first-section-scope.json').write_text(json.dumps(dict(atomic_multi_section=changed,guard='exact old revision + source SHA256 + both timestamps'),ensure_ascii=False,indent=2),encoding='utf8')
print('Explicit guarded multi-section packets:',changed)
