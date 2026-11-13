import json,re,time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests
root=Path(__file__).parent
API='https://wiki.swccg.com/api.php'
def call(**params):
    r=requests.get(API,params=dict(action='query',format='json',formatversion=2,**params),timeout=90);r.raise_for_status();j=r.json();assert 'error' not in j,j;return j
def fetch(titles):return call(titles='|'.join(titles),prop='revisions|flagged|imageinfo',rvprop='ids|timestamp|content',rvslots='main',iiprop='url|sha1')['query']['pages']
sets=['Reflections','Reflections II: Expanding the Galaxy',"Reflections III: A Collector's Bounty"]
first=fetch(sets+['Luke Skywalker (Reflections Foil)','Template:Card versions/Luke Skywalker (Premiere)','SWCCG Wiki:Style guide'])
(root/'bootstrap-heads.json').write_text(json.dumps({p['title']:p for p in first},ensure_ascii=False,indent=2),encoding='utf8')
print('Saved set sources and existing Luke foil pilot',flush=True)
path=root/'all-article-titles.json'
if path.exists():titles=json.loads(path.read_bytes())
else:
    titles=[];cont={}
    while True:
        j=call(list='allpages',aplimit=500,apnamespace=0,apfilterredir='nonredirects',**cont)
        titles.extend(p['title'] for p in j['query']['allpages'])
        if 'continue' not in j:break
        cont=j['continue']
        if len(titles)%5000==0:print('Titles',len(titles),flush=True)
    path.write_text(json.dumps(titles,ensure_ascii=False,indent=2),encoding='utf8')
foil_titles=[t for t in titles if re.search(r'foil|reflections',t,re.I)]
heads={}
with ThreadPoolExecutor(max_workers=3) as pool:
    for batch in pool.map(fetch,[foil_titles[i:i+25] for i in range(0,len(foil_titles),25)]):heads.update({p['title']:p for p in batch})
(root/'existing-foil-heads.json').write_text(json.dumps(heads,ensure_ascii=False,indent=2),encoding='utf8')
print(len(titles),'article titles;',len(heads),'foil/reflections articles saved',flush=True)
for title in sorted(heads):
    text=heads[title]['revisions'][0]['slots']['main']['content']
    print(title,'; '+'; '.join(re.findall(r'^\|(?:publication_id|gemp_id|set|image|border_finish)\s*=.*$',text,re.M)),flush=True)
