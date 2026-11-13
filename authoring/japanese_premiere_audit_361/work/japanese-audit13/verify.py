from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import quote,urljoin

from bs4 import BeautifulSoup
import requests

sys.path.insert(0,'work')
from audit_wiki_card_titles import get
sys.path.insert(0,'work/wiki-tools')
from style_lint import lint

root=Path('work/japanese-audit13')
rows=json.loads((root/'payload.json').read_bytes())['rows']
census=json.loads((root/'census.json').read_bytes())
titles=[row['title'] for row in census]+['Premiere (Japanese)']
titles += [row['title'] for row in rows if row['title'].startswith('File:')]
heads={}
for i in range(0,len(titles),24):
    result=get(action='query',titles='|'.join(titles[i:i+24]),prop='revisions|flagged',rvprop='ids|content|timestamp',rvslots='main')
    heads.update({p['title']:p for p in result['query']['pages']})
(root/'checked-heads.json').write_text(json.dumps(heads,ensure_ascii=False,indent=2),encoding='utf8')
for row in rows:
    page=heads[row['title']]
    rev=page['revisions'][0]
    assert rev['slots']['main']['content']==row['text'],row['title']
    assert not lint(row['text'],row['title'])[0],row['title']
    assert page['flagged']['stable_revid']==rev['revid'],(row['title'],page['flagged'])

def public(row):
    title=row['title']
    url='https://wiki.swccg.com/wiki/'+quote(title.replace(' ','_'),safe="():,'")
    response=requests.get(url,timeout=40)
    response.raise_for_status()
    html=response.text
    rev=heads[title]['revisions'][0]['revid']
    assert re.search(r'"wgRevisionId":'+str(rev)+r'\b',html),(title,'Stale anonymous page')
    assert 'cite-error' not in html,(title,'Citation error')
    soup=BeautifulSoup(html,'html.parser')
    body=soup.select_one('.mw-parser-output')
    assert body is not None
    imgs=body.select('img.mw-file-element') if not title.startswith('File:') else soup.select('.fullImageLink img')
    assert imgs,(title,'Missing thumbnail')
    if title!='Premiere (Japanese)':
        imgurl=urljoin(url,imgs[0]['src'])
        image=requests.get(imgurl,timeout=30)
        image.raise_for_status()
        assert image.headers.get('Content-Type','').startswith('image/'),imgurl
        assert 'Premiere (Japanese)' in body.get_text(' ',strip=True)
        if not title.startswith('File:'):
            assert body.select('span[lang="ja"]'),title
        assert body.select('.references'),title
    return dict(title=title,url=url,revid=rev,stable=True,anonymous=True,cite_errors=0,thumbnail_count=len(imgs),lint=0)

previous={r['title']:r for r in json.loads((root/'verification.json').read_bytes())} if (root/'verification.json').exists() else {}
results=[previous[row['title']] for row in rows if row['title'] in previous and previous[row['title']]['revid']==heads[row['title']]['revisions'][0]['revid']]
pending=[row for row in rows if row['title'] not in {r['title'] for r in results}]
with ThreadPoolExecutor(max_workers=5) as pool:
    for result in pool.map(public,pending):
        results.append(result)
(root/'verification.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf8')
print(len(results),'public reviewed pages match guarded drafts;',len(pending),'new public checks; zero lint/citation errors; thumbnails pass')
