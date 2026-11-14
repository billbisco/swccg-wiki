"""Discover original photos; captions are leads, never certification."""
import collections,difflib,json,re,unicodedata
from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).parent
manifest=json.loads((root/'manifest.json').read_bytes())
def norm(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]','',s)
rows=[]
for p in (root/'source-html').glob('*.html'):
    if 'store' in p.stem or p.stem in ['master','ri-rank']:continue
    soup=BeautifulSoup(p.read_text(encoding='utf8'),'html.parser');seen=set()
    for a in soup.select('a[rel="lightbox"]'):
        url=a.get('href','');caption=BeautifulSoup(a.get('data-sub-html',''),'html.parser').get_text(' ',strip=True)
        if not re.search('caimages|cloudfront',url):continue
        cert=re.search(r'/cert/(\d+)|/psaimages/\d+/(\d+)',url)
        cert=next(x for x in cert.groups() if x) if cert else url
        if cert in seen:continue
        seen.add(cert)
        product='Reflections III' if 'REFLECTIONS III' in caption.upper() else 'Reflections II: Expanding the Galaxy' if 'REFLECTIONS II' in caption.upper() else 'Reflections'
        title=re.sub(r'^.*?REFLECTIONS(?: III| II)?\s*','',caption,flags=re.I)
        title=re.sub(r'\bFOIL\b.*$','',title,flags=re.I).strip()
        options=[(difflib.SequenceMatcher(None,norm(title),norm(r['label'])).ratio(),r) for r in manifest if r['product']==product]
        best=sorted(options,key=lambda x:x[0],reverse=True)[:3]
        rows.append(dict(source_html=p.name,caption=caption,registry_key=cert,url=url.replace('/medium/','/'),product=product,caption_title=title,matches=[dict(score=round(score,3),label=r['label'],side=r['side'],article=r['proposed_article'],status=r['status']) for score,r in best]))
(root/'photo-candidates.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print('Original candidate photos:',collections.Counter(r['source_html'] for r in rows))
for r in rows[:12]:print(r['caption'],r['matches'][0])
