import json,re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
root=Path(__file__).parent;folder=root/'source-html';folder.mkdir(exist_ok=True)
urls={
'ri-adam':'https://www.psacard.com/psasetregistry/tcg/other-tcg-sets/2000-decipher-star-wars-ccg-reflections-foil/publishedset/570322',
'ri-rank':'https://www.psacard.com/psasetregistry/tcg/company-sets/2000-decipher-star-wars-ccg-reflections-foil/compositerankings/23563',
'master':'https://www.psacard.com/psasetregistry/tcg/pokemon-sets-key-card-sets-company-subsets/decipher-star-wars-ccg-foils-master-set-1999-2001/composition/23836',
'rii-gallery':'https://www.psacard.com/psasetregistry/showcase/modern-1981-present/star-wars-ccg-reflections-ii/imagegallery/17997',
'ri-store':'https://www.swccgstore.com/category-s/343.htm'}
def one(item):
    name,url=item
    try:
        r=requests.get(url,timeout=90);r.raise_for_status();(folder/(name+'.html')).write_bytes(r.content)
        soup=BeautifulSoup(r.text,'html.parser')
        links=[dict(text=a.get_text(' ',strip=True),href=a['href']) for a in soup.select('a[href]') if re.search(r'publishedset|imagegallery|compositerankings|\.jpg|\.png',a['href'],re.I)]
        return dict(name=name,url=url,status=r.status_code,title=soup.title.get_text() if soup.title else '',links=links,images=[x.get('src') for x in soup.select('img[src]')],bytes=len(r.content))
    except Exception as e:return dict(name=name,url=url,error=str(e))
with ThreadPoolExecutor(max_workers=3) as pool:rows=list(pool.map(one,urls.items()))
(root/'source-probe.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
for r in rows:print(r['name'],r.get('title',r.get('error')),r.get('bytes'),len(r.get('links',[])))
