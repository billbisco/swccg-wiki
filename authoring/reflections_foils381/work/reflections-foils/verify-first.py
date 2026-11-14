import collections,hashlib,json,re,sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import quote
import requests
from bs4 import BeautifulSoup
sys.path.insert(0,'work/japanese-infobox287/vendor');import mwparserfromhell as mw
sys.path.insert(0,'work/wiki-tools');from style_lint import lint
root=Path(__file__).parent
expected={}
for stage in ['first-new','first-family-final','first-set','first-nav']:
    expected.update({r['title']:r['text'] for r in json.loads((root/(stage+'-packet.json')).read_bytes())})
files=json.loads((root/'first-files-payload.json').read_bytes());expected.update({f['title']:f['desc'] for f in files})
talk_receipts={r['title']:r for r in map(json.loads,(root/'first-talk-receipts.jsonl').read_text().splitlines())}
titles=sorted(set(expected)|set(talk_receipts))
def fetch(batch):
    r=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join(batch),prop='revisions|flagged|imageinfo',rvprop='ids|timestamp|content',rvslots='main',iiprop='url|sha1'),timeout=60);r.raise_for_status();j=r.json();assert 'error' not in j,j;return j['query']['pages']
heads={}
with ThreadPoolExecutor(max_workers=3) as pool:
    for batch in pool.map(fetch,[titles[i:i+25] for i in range(0,len(titles),25)]):heads.update({p['title']:p for p in batch})
(root/'published-heads.json').write_text(json.dumps(heads,ensure_ascii=False,indent=2),encoding='utf8')
report=[]
for title,p in heads.items():
    rev=p['revisions'][0];text=rev['slots']['main']['content'];flags=lint(text,title)[0]
    exact=text.rstrip()==expected[title].rstrip() if title in expected else hashlib.sha256(text.encode()).hexdigest()==talk_receipts[title]['sha256']
    reviewed=p.get('flagged',{}).get('stable_revid')==rev['revid'] if p['ns']%2==0 else None
    row=dict(title=title,revid=rev['revid'],exact=exact,lint=flags,reviewed=reviewed);report.append(row)
    assert exact and not flags and reviewed is not False,row
for f in files:assert heads[f['title']]['imageinfo'][0]['sha1']==f['sha1'],f['title']
def card(text):return next(t for t in mw.parse(text).filter_templates(recursive=False) if str(t.name).strip()=='Card')
def values(text):
    t=card(text)
    return '\n'.join(str(t.get(k).value) for k in ['versions','printings'] if t.has(k))
families=json.loads((root/'first-families.json').read_bytes());readings=json.loads((root/'first-readings.json').read_bytes());nav=[]
for r in readings:
    ftext=heads[r['article']]['revisions'][0]['slots']['main']['content'];links=[str(w.title).strip() for w in mw.parse(values(ftext)).filter_wikilinks()]
    assert all(t in links for t in families[r['title']]),r['article']
    t=card(ftext);assert not t.has('gemp_id') and not t.has('card_uid') and t.has('publication_id')
    for sibling in families[r['title']]:
        t=card(heads[sibling]['revisions'][0]['slots']['main']['content'])
        for k in ['versions','printings']:
            if t.has(k):assert str(t.get(k).value).count('[['+r['article']+'|')==1,(sibling,k)
    nav.append(dict(article=r['article'],reciprocal_members=len(families[r['title']]),no_invented_playable_id=True))
old_heads=json.loads((root/'first-family-heads.json').read_bytes());archives=json.loads((root/'old-citation-final.json').read_bytes())
def conserved(text):
    code=mw.parse(text);t=next(t for t in code.filter_templates(recursive=False) if str(t.name).strip()=='Card')
    for k in ['versions','printings']:
        if t.has(k):t.get(k).value='NAVIGATION'
    text=str(code)
    for r in archives.values():text=re.sub(r'\s*Preserved copy:\s*\['+re.escape(r['capture'])+r' [^\]]*\]\.','',text)
    return re.sub(r'\s+','',text)
conservation=[]
for family in families.values():
    for t in family:
        old=old_heads[t]['revisions'][0]['slots']['main']['content'];new=heads[t]['revisions'][0]['slots']['main']['content'];ok=conserved(old)==conserved(new);assert ok,t
        conservation.append(dict(title=t,non_navigation_content_conserved=True))
(root/'first-source-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
(root/'first-navigation-verification.json').write_text(json.dumps(nav,ensure_ascii=False,indent=2),encoding='utf8')
(root/'first-conservation.json').write_text(json.dumps(conservation,ensure_ascii=False,indent=2),encoding='utf8')
print(len(heads),'sources exact/lint 0; main/File pages reviewed; Talk review inapplicable; 10 original image hashes; 54 reciprocal links/content conserved',flush=True)
def public(title):
    url='https://wiki.swccg.com/wiki/'+quote(title.replace(' ','_'),safe='')
    response=requests.get(url,timeout=60);response.raise_for_status();html=response.text;soup=BeautifulSoup(html,'html.parser');body=soup.select_one('#mw-content-text');assert body,title
    errors=len(body.select('.mw-ext-cite-error'));rev=heads[title]['revisions'][0]['revid'];match=re.search(r'"wgRevisionId":(\d+)',html)
    row=dict(title=title,url=url,revid=rev,public_revid=int(match[1]) if match else None,cite_errors=errors)
    assert not errors and row['public_revid']==rev,row
    if title in [r['article'] for r in readings]:
        row['infoboxes']=len(body.select('table.card-infobox'));assert row['infoboxes']==1,row
    return row
with ThreadPoolExecutor(max_workers=4) as pool:public_report=list(pool.map(public,titles))
(root/'first-public-verification.json').write_text(json.dumps(public_report,ensure_ascii=False,indent=2),encoding='utf8')
(root/'published-pages.md').write_text('# Story381 — changed live pages\n\n'+''.join('- ['+r['title']+']('+r['url']+') — revision '+str(r['revid'])+'\n' for r in public_report),encoding='utf8')
print(len(public_report),'anonymous public pages current, Cite 0',flush=True)
