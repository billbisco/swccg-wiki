import hashlib,json
from pathlib import Path
import requests
root=Path(__file__).parent;files=json.loads((root/'recovered-files-payload.json').read_bytes());titles='|'.join(r['title'] for r in files)
def get(**kwargs):
    response=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles=titles,prop='revisions',rvprop='ids|timestamp|content',rvslots='main',**kwargs),timeout=60)
    response.raise_for_status();return {p['title']:p for p in response.json()['query']['pages']}
heads=get();leads=get(rvsection=0);rows=[]
for f in files:
    page=heads[f['title']]
    if page.get('missing'):continue
    rev=page['revisions'][0];old=rev['slots']['main']['content'];lead=leads[f['title']]['revisions'][0]['slots']['main']['content']
    if old==f['desc']:continue
    assert old.split('== References ==',1)[1]==f['desc'].split('== References ==',1)[1],f['title']
    rows.append(dict(title=f['title'],text=f['desc'],section=0,section_text=f['desc'].split('== References ==',1)[0].rstrip(),before_revid=rev['revid'],before_sha256=hashlib.sha256(old.encode()).hexdigest(),before_section_sha256=hashlib.sha256(lead.encode()).hexdigest(),summary='Verify actual printed identity and link corrected preserved source photographs (#369)'))
(root/'file-metadata-packet.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print(len(rows),'guarded File lead-section corrections')
