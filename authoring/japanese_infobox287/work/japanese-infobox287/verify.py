from concurrent.futures import ThreadPoolExecutor
import hashlib,json,re,sys
from pathlib import Path
from urllib.parse import quote
import requests
from bs4 import BeautifulSoup
root=Path(__file__).parent
sys.path.insert(0,'work/wiki-tools')
from style_lint import lint
drafts=json.loads((root/'drafts.json').read_bytes())
expected={r['title']:r['text'] for r in drafts}
expected.update({r['title']:r['text'] for r in json.loads((root/'cleanup-packet.json').read_bytes())})
expected.update({r['title']:r['text'] for r in json.loads((root/'production-packet.json').read_bytes())})
expected['Template:Card/sandbox']=(root/'template-draft.wiki').read_text(encoding='utf8')
titles=sorted(expected)
def fetch(batch):
    response=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join(batch),prop='revisions|flagged',rvprop='ids|timestamp|content',rvslots='main'),timeout=60)
    response.raise_for_status();j=response.json();assert 'error' not in j,j;return j['query']['pages']
heads={}
with ThreadPoolExecutor(max_workers=3) as pool:
    for batch in pool.map(fetch,[titles[i:i+30] for i in range(0,len(titles),30)]):heads.update({p['title']:p for p in batch})
(root/'checked-heads.json').write_text(json.dumps(heads,ensure_ascii=False,indent=2),encoding='utf8')
source_report=[]
for title,text in expected.items():
    page=heads[title];rev=page['revisions'][0];actual=rev['slots']['main']['content'];flags=lint(actual,title)[0]
    card=not title.startswith('Template:')
    item=dict(title=title,revid=rev['revid'],source_exact=actual.rstrip()==text.rstrip(),lint=flags,reviewed=page.get('flagged',{}).get('stable_revid')==rev['revid'],shared_template=bool(re.search(r'\{\{Card\s*[|\n]',actual)) if card else True,no_manual_infobox='class="wikitable mw-collapsible card-infobox"' not in actual if card else True)
    source_report.append(item)
(root/'source-verification.json').write_text(json.dumps(source_report,ensure_ascii=False,indent=2),encoding='utf8')
fail=[r for r in source_report if not all(r[k] for k in ['source_exact','reviewed','shared_template','no_manual_infobox']) or r['lint']]
assert not fail,fail[:10]
print(len(expected),'live sources exact, reviewed, lint 0;',len(drafts),'shared card transclusions',flush=True)
def public(row):
    title=row['title'];url='https://wiki.swccg.com/wiki/'+quote(title.replace(' ','_'),safe='')
    response=requests.get(url,timeout=60);response.raise_for_status();html=response.text
    soup=BeautifulSoup(html,'html.parser');body=soup.select_one('#mw-content-text > .mw-parser-output');assert body,title
    tables=body.select('table.card-infobox');errors=body.select('.mw-ext-cite-error')
    rev=heads[title]['revisions'][0]['revid'];match=re.search(r'"wgRevisionId":(\d+)',html)
    result=dict(title=title,url=url,revid=rev,public_revid=int(match[1]) if match else None,tables=len(tables),cite_errors=len(errors),set_icon=any(th.get_text(strip=True)=='Set icon' for th in body.select('th')),japanese_sections=bool(body.select('[lang="ja"]')))
    assert len(tables)==1 and not errors and result['public_revid']==rev and result['set_icon'],result
    assert not row['is_ja'] or result['japanese_sections'],result
    return result
results=[]
with ThreadPoolExecutor(max_workers=4) as pool:
    for result in pool.map(public,drafts):
        results.append(result)
        if len(results)%100==0:print('Public pages',len(results),'/',len(drafts),flush=True)
(root/'public-verification.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf8')
print(len(results),'public pages reviewed, current, one infobox, native language markup, set icon, Cite 0',flush=True)
