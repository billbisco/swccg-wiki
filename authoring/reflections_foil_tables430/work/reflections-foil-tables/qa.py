"""Verify exact foil row/image targets, conservation, current public output and reviews."""
import collections,gzip,hashlib,json,re,sys
from pathlib import Path
from urllib.parse import unquote,quote
import requests
from bs4 import BeautifulSoup
sys.path.insert(0,'work/wiki-tools');from style_lint import lint
root=Path(__file__).parent;mode=sys.argv[1];inventory=json.loads((root/'inventory.json').read_bytes());packet=json.loads((root/'packet.json').read_bytes())
def check_tables(title,html):
    soup=BeautifulSoup(html,'html.parser');assert not soup.select('.mw-ext-cite-error'),title
    assert soup.select_one('#Foil_cards') and soup.select_one('#Possible_foils'),(title,'Foil heading or old anchor absent')
    tables=[t for t in soup.select('table.card-thumbs') if t.find('caption') and 'Side foils (' in t.find('caption').get_text()]
    assert len(tables)==2,(title,len(tables));actual=[];primary=[]
    for table in tables:
        side='Light' if 'Light Side' in table.find('caption').get_text() else 'Dark'
        for tr in table.select('tr'):
            cells=tr.find_all('td',recursive=False)
            if not cells:continue
            assert len(cells)==7,(title,len(cells),tr.get_text()[:100])
            link=cells[1].find('a');assert link and link.get('href','').startswith('/wiki/')
            target=unquote(link['href'].split('/wiki/',1)[1]).replace('_',' ');row=next(r for r in inventory if r['article']==target)
            assert row['product']==title and row['side']==side
            assert row['language']==cells[2].get_text(strip=True)
            assert cells[6].get_text(strip=True),(target,'Printed text absent from table')
            if row['language']=='Japanese':assert cells[6].find(attrs={'lang':'ja'}) or cells[6].get_text(strip=True)=='The game-text box is blank.',(target,'Native Japanese field or confirmed printed blank lost')
            if row['alternate_image']:assert '(AI)' in cells[1].get_text(),target
            if row['type']=='Location':assert all(label in cells[6].get_text() for label in ['Light Side:','Dark Side:']),(target,'Location halves not labeled')
            img=cells[0].find('img')
            if row['image_available']:
                assert img and row['image'].replace(' ','_') in unquote(img['src']),(target,'Wrong image')
                assert not cells[0].select('.card-scan-request'),target
                primary.append(img['src'])
            else:assert cells[0].select('.card-scan-request'),target
            actual.append(target)
    expected=[r['article'] for r in inventory if r['product']==title]
    assert collections.Counter(actual)==collections.Counter(expected),(title,'Missing/duplicate/extra exact foil rows')
    return dict(title=title,rows=len(actual),side_counts=dict(collections.Counter(r['side'] for r in inventory if r['product']==title)),actual_foil_images=len(primary),cite_errors=0,exact_publication_and_language_targets=True)
if mode=='preview':
    previews=json.loads(gzip.decompress((root/'phase-previews.json.gz').read_bytes()))
    report=[check_tables(t,p['text']) for t,p in previews.items() if t in {r['product'] for r in inventory}]
    (root/'preview-table-verification.json').write_text(json.dumps(report,indent=2),encoding='utf8');print(report);raise SystemExit
titles=[r['title'] for r in packet];heads={}
for i in range(0,len(titles),25):
    response=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join(titles[i:i+25]),prop='revisions|flagged',rvprop='ids|timestamp|content',rvslots='main'),timeout=60);response.raise_for_status();heads.update({h['title']:h for h in response.json()['query']['pages']})
receipts={r['title']:r for r in map(json.loads,(root/'phase-receipts.jsonl').read_text(encoding='utf8').splitlines())};report=[]
if (root/'heading-correction-receipts.jsonl').exists():receipts.update({r['title']:r for r in map(json.loads,(root/'heading-correction-receipts.jsonl').read_text(encoding='utf8').splitlines())})
if (root/'rotation-correction-receipts.jsonl').exists():receipts.update({r['title']:r for r in map(json.loads,(root/'rotation-correction-receipts.jsonl').read_text(encoding='utf8').splitlines())})
for row in packet:
    title=row['title']
    if title not in receipts:continue
    h=heads[title];rev=h['revisions'][0];text=rev['slots']['main']['content'];receipt=receipts[title]
    assert rev['revid']==receipt['revid'] and hashlib.sha256(text.encode()).hexdigest()==receipt['sha256'],title
    if not row.get('signed_note'):assert text.rstrip()==row['text'].rstrip(),title
    flags=lint(text,title)[0];assert flags==row.get('unchanged_prior_talk_flags',[]),(title,flags)
    if h['ns']%2==0:assert h.get('flagged',{}).get('stable_revid')==rev['revid'],title
    url='https://wiki.swccg.com/wiki/'+quote(title.replace(' ','_'),safe=':(),')
    response=requests.get(url,timeout=60);response.raise_for_status();html=response.text;soup=BeautifulSoup(html,'html.parser');m=re.search(r'"wgRevisionId":(\d+)',html)
    assert m and int(m[1])==rev['revid'],(title,'Public cache revision is stale')
    assert not soup.select('.mw-ext-cite-error'),title
    entry=dict(title=title,revid=rev['revid'],exact_saved_source=True,reviewed=h.get('flagged',{}).get('stable_revid')==rev['revid'] if h['ns']%2==0 else None,cite_errors=0,unchanged_prior_talk_flags=flags)
    if title in {r['product'] for r in inventory}:entry.update(check_tables(title,html))
    report.append(entry)
published={t:heads[t] for t in receipts}
(root/'published-heads.json').write_text(json.dumps(published,ensure_ascii=False,indent=2),encoding='utf8')
(root/'public-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
(root/'published-pages.md').write_text('# Changed live pages — story430\n\n'+''.join('- ['+t+'](https://wiki.swccg.com/wiki/'+quote(t.replace(' ','_'),safe=':(),')+')\n' for t in sorted(published)),encoding='utf8')
print(len(report),'exact current reviewed/public pages; foil tables and Cite checks pass; unchanged prior Talk archive flags explicit')
