"""Verify live changes without certifying a preservation-blocked whole batch."""
import hashlib,json,re,sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import quote
import requests
from bs4 import BeautifulSoup
sys.path.insert(0,'work/wiki-tools');from publication_policy import lint
root=Path(__file__).parent;stage=sys.argv[1];expected={};talk={}
for kind in ['new','set']:
    expected.update({r['title']:r['text'] for r in json.loads((root/(stage+'-'+kind+'-packet.json')).read_bytes())})
files=json.loads((root/(stage+'-files-payload.json')).read_bytes());expected.update({r['title']:r['desc'] for r in files})
talk={r['title']:r['sha256'] for r in map(json.loads,(root/(stage+'-talk-receipts.jsonl')).read_text().splitlines())}
titles=sorted(set(expected)|set(talk));heads={};report=[]
for i in range(0,len(titles),25):
    response=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join(titles[i:i+25]),prop='revisions|flagged|imageinfo',rvprop='ids|timestamp|content',rvslots='main',iiprop='sha1|url'),timeout=60);response.raise_for_status();heads.update({p['title']:p for p in response.json()['query']['pages']})
for title,p in heads.items():
    rev=p['revisions'][0];text=rev['slots']['main']['content'];assert not lint(text,title)[0],title
    assert text.rstrip()==expected[title].rstrip() if title in expected else hashlib.sha256(text.encode()).hexdigest()==talk[title],title
    if p['ns']%2==0:assert p.get('flagged',{}).get('stable_revid')==rev['revid'],title
for f in files:assert heads[f['title']]['imageinfo'][0]['sha1']==f['sha1']
def public(title):
    url='https://wiki.swccg.com/wiki/'+quote(title.replace(' ','_'),safe='');response=requests.get(url,timeout=60);response.raise_for_status();soup=BeautifulSoup(response.text,'html.parser');body=soup.select_one('#mw-content-text');rid=heads[title]['revisions'][0]['revid'];m=re.search(r'"wgRevisionId":(\d+)',response.text);assert m and int(m[1])==rid,title;assert body and not body.select('.mw-ext-cite-error'),title
    return dict(title=title,url=url,revid=rid,exact_source=True,lint=[],cite_errors=0,public_revision_current=True)
with ThreadPoolExecutor(max_workers=3) as pool:report=list(pool.map(public,titles))
(root/(stage+'-partial-public-verification.json')).write_text(json.dumps(dict(scope='Published new articles, File descriptions and binaries, checklist and signed Talk notes only. Does not certify pending family edits or exact wiki-image Wayback captures.',pages=report),ensure_ascii=False,indent=2),encoding='utf8')
published=json.loads((root/'published-heads.json').read_bytes());published.update(heads);(root/'published-heads.json').write_text(json.dumps(published,ensure_ascii=False,indent=2),encoding='utf8')
(root/'published-pages.md').write_text('# Changed live pages — story 381\n\n'+''.join('* ['+t+'](https://wiki.swccg.com/wiki/'+quote(t.replace(' ','_'),safe='')+')\n' for t in sorted(published)),encoding='utf8')
print(len(report),'published pages verified; preservation and family work remain explicitly pending')
