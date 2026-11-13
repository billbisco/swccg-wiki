import json
from pathlib import Path
import requests
root=Path(__file__).parent
titles=["I'm On The Leader","I'm On The Leader (Japanese)",'File:Japanese-ANH-Evader-PSA-156625016-original.jpg']
r=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join(titles),prop='revisions|imageinfo',rvprop='ids|timestamp|content',rvslots='main',iiprop='url|sha1|size'),timeout=60);r.raise_for_status();j=r.json()
(root/'identity-check.json').write_text(json.dumps(j,ensure_ascii=False,indent=2),encoding='utf8')
for p in j['query']['pages']:print(p['title'],p.get('revisions',[{'slots':{'main':{'content':'Missing'}}}])[0]['slots']['main']['content'][:3600])
