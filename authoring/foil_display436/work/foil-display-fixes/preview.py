import json,gzip,re,time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
root=Path(__file__).parent
rows=json.loads((root/'main-packet.json').read_bytes())
rows=[r for r in rows if not r['title'].startswith('Template:')]
def render(row):
    cached=root/'preview-cache'/(str(rows.index(row))+'.json')
    if cached.exists():return row['title'],json.loads(cached.read_bytes())
    text=row['text'].replace('{{Card\n','{{Card/foil-display-436\n',1)
    r=requests.post('https://wiki.swccg.com/api.php',data=dict(action='parse',format='json',formatversion=2,title=row['title'],text=text,contentmodel='wikitext',prop='text|images'),timeout=120);r.raise_for_status();j=r.json();assert 'error' not in j,j
    html=j['parse']['text'];s=BeautifulSoup(html,'html.parser')
    assert not s.select('.mw-ext-cite-error,.mw-ext-cite-error,.error'),(row['title'],s.select('.error'))
    assert '{{{' not in s.get_text(),row['title']
    expected=1 if row['title'] not in ['Reflections','Reflections II: Expanding the Galaxy','Reflections III'] else row['text'].count('{{Card photograph|')
    assert len(s.select('.card-photo'))==expected,(row['title'],expected,len(s.select('.card-photo')))
    for frame in s.select('.card-photo'):
        assert frame.select_one('.card-photo-source img') and frame.find('small').get_text()=='Original photograph',(row['title'],str(frame)[:1800])
    cached.parent.mkdir(exist_ok=True);cached.write_text(json.dumps(j['parse'],ensure_ascii=False),encoding='utf8')
    return row['title'],j['parse']
with ThreadPoolExecutor(max_workers=3) as pool:out=dict(pool.map(render,rows))
with gzip.open(root/'previews.json.gz','wt',encoding='utf8') as f:json.dump(out,f,ensure_ascii=False)
print(len(out),'previews PASS: no parser/Cite errors; card frames and original links present')
