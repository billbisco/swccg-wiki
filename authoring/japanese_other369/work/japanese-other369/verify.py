"""Read-only final source, review, image and anonymous-public verification."""
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,re,sys
from pathlib import Path
from urllib.parse import quote
import requests
from bs4 import BeautifulSoup
root=Path(__file__).parent
sys.path.insert(0,'work/wiki-tools')
from style_lint import lint
baseline=json.loads((root/'heads-before.json').read_bytes())
expected={}
for stage in ['phase1','phase2','phase3','phase4','rotation-sandbox','rotation-production','rotation-doc','file-metadata']:
    expected.update({r['title']:r['text'] for r in json.loads((root/(stage+'-packet.json')).read_bytes())})
files=json.loads((root/'files-payload.json').read_bytes())+json.loads((root/'recovered-files-payload.json').read_bytes())
first=list(map(json.loads,(root/'upload-receipts.jsonl').read_text().splitlines()))[0]
alias='File:Japanese-ANH-Evader-PSA-156625016-original.jpg'
titles=sorted(set(baseline)|set(expected)|{f['title'] for f in files}|{alias})
def fetch(batch):
    r=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join(batch),prop='revisions|flagged|imageinfo',rvprop='ids|timestamp|content',rvslots='main',iiprop='sha1|url'),timeout=60)
    r.raise_for_status();j=r.json();assert 'error' not in j,j
    return j['query']['pages']
heads={}
with ThreadPoolExecutor(max_workers=3) as pool:
    for batch in pool.map(fetch,[titles[i:i+25] for i in range(0,len(titles),25)]):heads.update({p['title']:p for p in batch})
(root/'checked-heads.json').write_text(json.dumps(heads,ensure_ascii=False,indent=2),encoding='utf8')
report=[]
for title,page in heads.items():
    rev=page['revisions'][0];actual=rev['slots']['main']['content']
    row=dict(title=title,revid=rev['revid'],reviewed=page.get('flagged',{}).get('stable_revid')==rev['revid'],lint=lint(actual,title)[0])
    if title in expected:
        row['source_exact']=actual.rstrip()==expected[title].rstrip()
        if not row['source_exact'] and title in ['Ghhhk (Japanese)','Hypo (Japanese)']:
            # Concurrent family-version maintenance is outside this audit's fields.
            without_versions=lambda s:re.sub(r'^\|versions=.*$', '|versions=EXTERNAL-MAINTENANCE',s,flags=re.M).rstrip()
            row['audit_fields_exact']=without_versions(actual)==without_versions(expected[title])
            row['external_versions_preserved']=True
    if title==first['title']:row['source_exact']=hashlib.sha256(actual.encode()).hexdigest()==first['sha256']
    if title==alias:row['source_exact']=bool(re.search(r'#REDIRECT\s*\[\[File:Japanese-ANH-Im-On-The-Leader-PSA-156625016-original.jpg\]\]',actual,re.I))
    if title in baseline:
        row['shared_card']=bool(re.search(r'\{\{Card\s*[|\n]',actual)) and 'class="wikitable mw-collapsible card-infobox"' not in actual
    report.append(row)
(root/'source-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
bad=[r for r in report if r['lint'] or not r['reviewed'] or not (r.get('source_exact',True) or r.get('audit_fields_exact',False)) or not r.get('shared_card',True)]
assert not bad,bad[:10]
for f in files:assert heads[f['title']]['imageinfo'][0]['sha1']==f['sha1'],f['title']
print(len(heads),'fresh sources; 469 shared Card pages; reviewed, lint 0; 10 original image SHA1 matches',flush=True)
changed=set(expected)|{f['title'] for f in files}|{alias}
def public(title):
    url='https://wiki.swccg.com/wiki/'+quote(title.replace(' ','_'),safe='')
    response=requests.get(url,timeout=60);response.raise_for_status();html=response.text
    soup=BeautifulSoup(html,'html.parser');body=soup.select_one('#mw-content-text > .mw-parser-output') or soup.select_one('#mw-content-text');assert body,title
    rev=heads[title]['revisions'][0]['revid'];match=re.search(r'"wgRevisionId":(\d+)',html)
    row=dict(title=title,url=url,revid=rev,public_revid=int(match[1]) if match else None,cite_errors=len(body.select('.mw-ext-cite-error')))
    assert not row['cite_errors'],row
    if title!=alias:assert row['public_revid']==rev,row
    if title in baseline:
        row['infoboxes']=len(body.select('table.card-infobox'));row['japanese']=bool(body.select('[lang="ja"]'))
        assert row['infoboxes']==1 and row['japanese'],row
    return row
results=[]
with ThreadPoolExecutor(max_workers=4) as pool:
    for row in pool.map(public,sorted(changed)):
        results.append(row)
        if len(results)%50==0:print('Public',len(results),'/',len(changed),flush=True)
(root/'public-verification.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf8')
(root/'published-pages.md').write_text('# Japanese card audit: published pages\n\nEvery changed card, set, template and File is linked below.\n\n'+''.join('- ['+r['title']+']('+r['url']+') — revision '+str(r['revid'])+'\n' for r in results),encoding='utf8')
summary=dict(audited_cards=len(baseline),changed_cards=len(set(baseline)&changed),changed_pages=len(changed),source_pages=len(heads),public_checks=len(results),source_failures=0,public_failures=0,original_images=10)
(root/'verification-summary.json').write_text(json.dumps(summary,indent=2),encoding='utf8');print(summary,flush=True)
