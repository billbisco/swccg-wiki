"""Read-only reconciliation after other work adds foil articles."""
import json
from pathlib import Path
import requests
root=Path(__file__).parent;manifest=json.loads((root/'manifest.json').read_bytes());heads={}
titles=list(dict.fromkeys(r['proposed_article'] for r in manifest))
for i in range(0,len(titles),40):
    response=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join(titles[i:i+40]),prop='revisions|flagged',rvprop='ids|user|timestamp|content',rvslots='main'),timeout=60);response.raise_for_status();j=response.json();assert 'error' not in j,j;heads.update({p['title']:p for p in j['query']['pages']})
(root/'refreshed-foil-heads.json').write_text(json.dumps(heads,ensure_ascii=False,indent=2),encoding='utf8')
new=json.loads((root/'additional-existing-foils.json').read_bytes()) if (root/'additional-existing-foils.json').exists() else []
known_additional={r['article'] for r in new}
for row in manifest:
    h=heads[row['proposed_article']]
    if row['proposed_article'] not in known_additional and 'revisions' in h and row['status'] in ['missing','draft_prepared_awaiting_preservation']:
        new.append(dict(article=h['title'],revid=h['revisions'][0]['revid'],user=h['revisions'][0]['user'],timestamp=h['revisions'][0]['timestamp'],previous_status='missing',needs_integration_audit=True))
(root/'additional-existing-foils.json').write_text(json.dumps(new,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(new,ensure_ascii=False,indent=2));print(len(new),'additional existing articles discovered; no live changes')
