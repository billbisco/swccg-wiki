import json,hashlib
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlencode
import requests
p=Path(__file__).parent;folder=p/'product/revisions';folder.mkdir(exist_ok=True)
heads=json.loads((p/'source-heads.json').read_bytes())
for kind in ['wiki','talk']:
    title='SWCCG Wiki'+(' talk' if kind=='talk' else '')+':Samples/Shared search pilot'
    j=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles=title,prop='revisions|flagged',rvprop='ids|timestamp|content',rvslots='main'),timeout=60).json()
    h=j['query']['pages'][0];assert h.get('revisions'),h
    if kind=='wiki':assert h['revisions'][0]['revid']==307273 and h['flagged']['stable_revid']==307273
    (p/(kind+'-published.json')).write_text(json.dumps({'page':h},ensure_ascii=False,indent=2),encoding='utf8');heads[title]=h
def checked(h):
    rev=h['revisions'][0];raw=rev['slots']['main']['content'].encode();url='https://wiki.swccg.com/index.php?'+urlencode(dict(title=h['title'],oldid=rev['revid'],action='raw'))
    r=requests.get(url,timeout=60);r.raise_for_status();assert r.content==raw,(h['title'],'Exact raw revision differs')
    member='product/revisions/'+str(rev['revid'])+'.wiki';(p/member).write_bytes(raw)
    return dict(kind='wiki_revision',title=h['title'],revision_id=rev['revid'],url=url,member=member,sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw))
with ThreadPoolExecutor(max_workers=3) as pool:rows=list(pool.map(checked,heads.values()))
(p/'revision-ledger.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8');print(len(rows),'exact raw source/sample/Talk revisions verified and staged for independent backup')
