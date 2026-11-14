"""Focused propagation check for an already verified publication batch."""
import json,sys
from pathlib import Path
from urllib.parse import quote,unquote
import requests
from bs4 import BeautifulSoup
sys.path.insert(0,'work/japanese-infobox287/vendor');import mwparserfromhell as mw
root=Path(__file__).parent;stage=sys.argv[1]
heads=json.loads((root/(stage+'-published-heads.json')).read_bytes());families=json.loads((root/(stage+'-families.json')).read_bytes());rows=[]
for r in json.loads((root/(stage+'-readings.json')).read_bytes()):
    source=heads[r['article']]['revisions'][0]['slots']['main']['content']
    if '{{Card versions/' not in source:continue
    for title in families[r['title']]:
        url='https://wiki.swccg.com/wiki/'+quote(title.replace(' ','_'),safe='')
        def check():
            response=requests.get(url,timeout=60);response.raise_for_status();soup=BeautifulSoup(response.text,'html.parser');box=soup.select_one('.card-infobox');assert box,title
            return any(unquote(a.get('href','').split('/wiki/',1)[-1]).replace('_',' ')==r['article'] for a in box.select('a[href]'))
        first=check()
        if not first:
            response=requests.post('https://wiki.swccg.com/api.php',data=dict(action='purge',format='json',formatversion=2,titles=title,forcelinkupdate=1),timeout=60);response.raise_for_status();assert response.json()['purge'][0].get('purged'),title
        assert first or check(),(title,'Shared navigation not propagated')
        rows.append(dict(title=title,url=url,foil=r['article'],linked=True,purged=not first,article_source_unchanged=True))
(root/(stage+'-shared-family-public-verification.json')).write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8');print(len(rows),'existing shared-family pages link to the foil')
