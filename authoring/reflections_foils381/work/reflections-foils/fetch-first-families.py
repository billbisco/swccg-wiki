import json,re,sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import requests
sys.path.insert(0,'work/japanese-infobox287/vendor');import mwparserfromhell as mw
root=Path(__file__).parent
def template(text):return next((t for t in mw.parse(text).filter_templates(recursive=False) if str(t.name).strip()=='Card'),None)
def links(text):
    t=template(text)
    if t is None:return []
    value='\n'.join(str(t.get(k).value) for k in ['versions','printings'] if t.has(k))
    return list(dict.fromkeys(str(w.title).strip() for w in mw.parse(value).filter_wikilinks() if ':' not in str(w.title) or not re.match(r'^(File|Template|Category):',str(w.title))))
def fetch(batch):
    r=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join(batch),prop='revisions|flagged',rvprop='ids|timestamp|content',rvslots='main'),timeout=60);r.raise_for_status();j=r.json();assert 'error' not in j,j;return j['query']['pages']
roots=[r['title'] for r in json.loads((root/'first-readings.json').read_bytes())]
heads={};wanted=set(roots);families={}
for depth in range(5):
    missing=sorted(wanted-set(heads))
    if not missing:break
    with ThreadPoolExecutor(max_workers=3) as pool:
        for batch in pool.map(fetch,[missing[i:i+30] for i in range(0,len(missing),30)]):heads.update({p['title']:p for p in batch})
    for title,p in list(heads.items()):
        if 'revisions' not in p:continue
        text=p['revisions'][0]['slots']['main']['content']
        wanted.update(links(text))
        m=re.match(r'#REDIRECT\s*\[\[([^\]]+)\]\]',text,re.I)
        if m:wanted.add(m[1])
for start in roots:
    family={start};queue=[start]
    while queue:
        t=queue.pop();p=heads.get(t)
        if not p or 'revisions' not in p:continue
        text=p['revisions'][0]['slots']['main']['content'];nexts=links(text)
        m=re.match(r'#REDIRECT\s*\[\[([^\]]+)\]\]',text,re.I)
        if m:nexts.append(m[1])
        for n in nexts:
            if n not in family:family.add(n);queue.append(n)
    families[start]=sorted(t for t in family if t in heads and 'revisions' in heads[t] and template(heads[t]['revisions'][0]['slots']['main']['content']) is not None)
(root/'first-family-heads.json').write_text(json.dumps(heads,ensure_ascii=False,indent=2),encoding='utf8')
(root/'first-families.json').write_text(json.dumps(families,ensure_ascii=False,indent=2),encoding='utf8')
print({t:len(f) for t,f in families.items()});print(len(heads),'heads including old redirects/missing links')
