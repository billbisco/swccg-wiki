"""Back up current live heads, retaining any post-delivery concurrent edits."""
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import quote
import requests
root=Path(__file__).parent;before=json.loads((root/'published-heads.json').read_bytes());titles=sorted(before)
def fetch(batch):
    response=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join(batch),prop='revisions|flagged',rvprop='ids|timestamp|user|content',rvslots='main'),timeout=60);response.raise_for_status();data=response.json();assert 'error' not in data,data;return data['query']['pages']
heads={}
with ThreadPoolExecutor(max_workers=3) as pool:
    for batch in pool.map(fetch,[titles[i:i+30] for i in range(0,len(titles),30)]):heads.update({r['title']:r for r in batch})
assert set(heads)==set(before) and all('revisions' in h for h in heads.values())
changes=[dict(title=t,before_revid=before[t]['revisions'][0]['revid'],current_revid=h['revisions'][0]['revid'],user=h['revisions'][0]['user']) for t,h in heads.items() if before[t]['revisions'][0]['revid']!=h['revisions'][0]['revid']]
(root/'post-delivery-current-heads.json').write_text(json.dumps(dict(scope='Read-only backup refresh; any later edits retained, not attributed to this story or certified by earlier batch checks',changes=changes),ensure_ascii=False,indent=2),encoding='utf8')
(root/'published-heads.json').write_text(json.dumps(heads,ensure_ascii=False,indent=2),encoding='utf8')
(root/'published-pages.md').write_text('# Changed live pages — story381\n\n'+''.join('* ['+t+'](https://wiki.swccg.com/wiki/'+quote(t.replace(' ','_'),safe='')+')\n' for t in sorted(heads)),encoding='utf8')
print(len(heads),'current live sources backed up;',len(changes),'post-delivery revisions retained')
