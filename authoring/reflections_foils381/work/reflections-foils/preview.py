from concurrent.futures import ThreadPoolExecutor
import gzip,json,sys,re
from pathlib import Path
import requests
from bs4 import BeautifulSoup
root=Path(__file__).parent;stage=sys.argv[1] if len(sys.argv)>1 else 'phase1';rows=json.loads((root/(stage+'-packet.json')).read_bytes())
def render(row):
    text=re.sub(r'\{\{\s*Card(?=\s*[|\n])','{{Card/sandbox',row['text'],count=1) if '--sandbox' in sys.argv else row['text']
    response=requests.post('https://wiki.swccg.com/api.php',data=dict(action='parse',format='json',formatversion=2,title=row['title'],text=text,contentmodel='wikitext',prop='text|links|images|categories'),timeout=90)
    response.raise_for_status();j=response.json();assert 'error' not in j,j
    result=j['parse'];soup=BeautifulSoup(result['text'],'html.parser')
    assert not soup.select('.mw-ext-cite-error'),row['title']
    if row['title'] not in ['Reflections','Reflections II: Expanding the Galaxy','Reflections III'] and not row['title'].startswith(('Talk:','File:','Template:')):assert len(soup.select('.card-infobox'))==1,row['title']
    return row['title'],result
with ThreadPoolExecutor(max_workers=3) as pool:out=dict(pool.map(render,rows))
with gzip.open(root/(stage+('-sandbox' if '--sandbox' in sys.argv else '')+'-previews.json.gz'),'wt',encoding='utf8') as f:json.dump(out,f,ensure_ascii=False)
print(len(out),'previews: Cite 0, infoboxes intact')
