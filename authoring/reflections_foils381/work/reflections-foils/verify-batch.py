"""Check delivered sources, reciprocal links, conservation and anonymous output."""
import hashlib,json,re,sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import quote,unquote
import requests
from bs4 import BeautifulSoup
sys.path.insert(0,'work/japanese-infobox287/vendor');import mwparserfromhell as mw
sys.path.insert(0,'work/wiki-tools');from style_lint import lint
root=Path(__file__).parent;stage=sys.argv[1];expected={}
for kind in ['new','family-final','shared-nav','set','file-preservation','correction']:
    p=root/(stage+'-'+kind+'-packet.json')
    if p.exists():expected.update({r['title']:r['text'] for r in json.loads(p.read_bytes())})
files=json.loads((root/(stage+'-files-payload.json')).read_bytes())
for f in files:expected.setdefault(f['title'],f['desc'])
receipts={r['title']:r for r in map(json.loads,(root/(stage+'-talk-receipts.jsonl')).read_text().splitlines())}
titles=sorted(set(expected)|set(receipts))
def fetch(batch):
    r=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join(batch),prop='revisions|flagged|imageinfo',rvprop='ids|timestamp|content',rvslots='main',iiprop='url|sha1'),timeout=60);r.raise_for_status();j=r.json();assert 'error' not in j,j;return j['query']['pages']
heads={}
with ThreadPoolExecutor(max_workers=3) as pool:
    for pages in pool.map(fetch,[titles[i:i+25] for i in range(0,len(titles),25)]):heads.update({p['title']:p for p in pages})
report=[]
for title,p in heads.items():
    rev=p['revisions'][0];text=rev['slots']['main']['content'];flags=lint(text,title)[0]
    exact=text.rstrip()==expected[title].rstrip() if title in expected else hashlib.sha256(text.encode()).hexdigest()==receipts[title]['sha256']
    reviewed=p.get('flagged',{}).get('stable_revid')==rev['revid'] if p['ns']%2==0 else None
    row=dict(title=title,revid=rev['revid'],exact=exact,lint=flags,reviewed=reviewed);report.append(row);assert exact and not flags and reviewed is not False,row
for f in files:assert heads[f['title']]['imageinfo'][0]['sha1']==f['sha1'],f['title']
families=json.loads((root/(stage+'-families.json')).read_bytes());readings=json.loads((root/(stage+'-readings.json')).read_bytes());baseline=json.loads((root/(stage+'-family-heads.json')).read_bytes())
archives=json.loads((root/(stage+'-citation-final.json')).read_bytes());corrections=json.loads((root/(stage+'-citation-corrections.json')).read_bytes())
def card(s):return next(t for t in mw.parse(s).filter_templates(recursive=False) if str(t.name).strip()=='Card')
def values(s):
    t=card(s);return '\n'.join(str(t.get(k).value) for k in ['versions','printings'] if t.has(k))
def conserved(s):
    code=mw.parse(s);t=next(t for t in code.filter_templates(recursive=False) if str(t.name).strip()=='Card')
    for k in ['versions','printings']:
        if t.has(k):t.get(k).value='NAVIGATION'
    s=str(code)
    for r in archives.values():s=re.sub(r'\s*Preserved copy:\s*\['+re.escape(r['capture'])+r' [^\]]*\]\.','',s)
    for old,new in corrections.items():s=s.replace(old,new)
    return re.sub(r'\s+','',s)
conservation=[];nav=[]
for r in readings:
    text=heads[r['article']]['revisions'][0]['slots']['main']['content'];t=card(text);assert not t.has('gemp_id') and not t.has('card_uid') and t.has('publication_id')
    value=values(text);shared='{{Card versions/' in value
    for sibling in families[r['title']]:
        old=baseline[sibling]['revisions'][0]['slots']['main']['content']
        if shared and '{{Card versions/' in values(old):continue
        new=heads[sibling]['revisions'][0]['slots']['main']['content'];ok=conserved(old)==conserved(new);assert ok,sibling
        current=card(new)
        for k in ['versions','printings']:
            if current.has(k):assert str(current.get(k).value).count('[['+r['article']+'|')==1,(sibling,k)
        conservation.append(dict(title=sibling,non_navigation_content_conserved=True))
    nav.append(dict(article=r['article'],family_members=len(families[r['title']]),shared_navigator=shared,no_invented_playable_id=True))
print(len(heads),'exact sources; lint 0, reviewed; original image hashes match',flush=True)
def public(title):
    url='https://wiki.swccg.com/wiki/'+quote(title.replace(' ','_'),safe='');response=requests.get(url,timeout=60);response.raise_for_status();html=response.text;soup=BeautifulSoup(html,'html.parser');body=soup.select_one('#mw-content-text');assert body,title
    rev=heads[title]['revisions'][0]['revid'];m=re.search(r'"wgRevisionId":(\d+)',html);initial=int(m[1]) if m else None
    if initial!=rev:
        purge=requests.post('https://wiki.swccg.com/api.php',data=dict(action='purge',format='json',formatversion=2,titles=title,forcelinkupdate=1),timeout=60);purge.raise_for_status();assert purge.json()['purge'][0].get('purged'),title
        response=requests.get(url,timeout=60);response.raise_for_status();html=response.text;soup=BeautifulSoup(html,'html.parser');body=soup.select_one('#mw-content-text');m=re.search(r'"wgRevisionId":(\d+)',html)
    row=dict(title=title,url=url,revid=rev,initial_public_revid=initial,public_revid=int(m[1]) if m else None,cite_errors=len(body.select('.mw-ext-cite-error')));assert not row['cite_errors'] and row['public_revid']==rev,row
    reading=next((r for r in readings if r['article']==title),None)
    if reading:
        boxes=body.select('table.card-infobox');assert len(boxes)==1,title
        links={unquote(a.get('href','').split('/wiki/',1)[1].split('#')[0]).replace('_',' ') for a in boxes[0].select('a[href]') if '/wiki/' in a['href']}
        assert set(families[reading['title']])<=links,(title,'Missing family destinations',set(families[reading['title']])-links)
        row['infoboxes']=1;row['family_links_verified']=len(families[reading['title']])
    return row
with ThreadPoolExecutor(max_workers=4) as pool:public_report=list(pool.map(public,titles))
shared_checks=[]
for r in readings:
    if '{{Card versions/' not in values(heads[r['article']]['revisions'][0]['slots']['main']['content']):continue
    needle='/wiki/'+quote(r['article'].replace(' ','_'),safe='(),')
    for sibling in families[r['title']]:
        url='https://wiki.swccg.com/wiki/'+quote(sibling.replace(' ','_'),safe='');response=requests.get(url,timeout=60);response.raise_for_status()
        def linked(html):
            soup=BeautifulSoup(html,'html.parser');box=soup.select_one('.card-infobox')
            return bool(box and any(unquote(a.get('href','').split('/wiki/',1)[-1]).replace('_',' ')==r['article'] for a in box.select('a[href]')))
        was_linked=linked(response.text)
        if not was_linked:
            purge=requests.post('https://wiki.swccg.com/api.php',data=dict(action='purge',format='json',formatversion=2,titles=sibling,forcelinkupdate=1),timeout=60);purge.raise_for_status();response=requests.get(url,timeout=60);response.raise_for_status()
        assert linked(response.text),(sibling,'Shared navigator not propagated')
        shared_checks.append(dict(title=sibling,url=url,foil=r['article'],linked=True,purged=not was_linked,article_source_unchanged=True))
if shared_checks:(root/(stage+'-shared-family-public-verification.json')).write_text(json.dumps(shared_checks,ensure_ascii=False,indent=2),encoding='utf8')
for suffix,data in [('source-verification',report),('public-verification',public_report),('navigation-verification',nav),('conservation',conservation),('published-heads',heads)]:
    (root/(stage+'-'+suffix+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
allheads=json.loads((root/'published-heads.json').read_bytes()) if (root/'published-heads.json').exists() else {};allheads.update(heads);(root/'published-heads.json').write_text(json.dumps(allheads,ensure_ascii=False,indent=2),encoding='utf8')
(root/'published-pages.md').write_text('# Story381 — changed live pages\n\n'+''.join('- ['+t+'](https://wiki.swccg.com/wiki/'+quote(t.replace(' ','_'),safe='')+') — revision '+str(p['revisions'][0]['revid'])+'\n' for t,p in sorted(allheads.items())),encoding='utf8')
print(len(public_report),'anonymous public pages current, Cite 0; reciprocal navigation and existing content conserved',flush=True)
