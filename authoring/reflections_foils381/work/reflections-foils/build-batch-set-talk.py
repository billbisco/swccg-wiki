import hashlib,json,re,sys
from pathlib import Path
import requests
from source_registry import provenance
sys.path.insert(0,'work/wiki-tools');from publication_policy import lint
root=Path(__file__).parent;stage=sys.argv[1]
readings=json.loads((root/(stage+'-readings.json')).read_bytes());files=json.loads((root/(stage+'-files-payload.json')).read_bytes())
products=list(dict.fromkeys(r['product'] for r in readings));packets=[];heads={};talk=[]
for product in products:
    response=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles=product,prop='revisions',rvprop='ids|timestamp|content',rvslots='main'),timeout=60);response.raise_for_status()
    page=response.json()['query']['pages'][0];heads[product]=page;rev=page['revisions'][0];old=rev['slots']['main']['content']
    start=old.index('== Possible foils ==');end=old.index('\n== ',start+5);section=old[start:end]
    sys.path.insert(0,'work/japanese-infobox287/vendor');import mwparserfromhell as mw
    manifest=json.loads((root/'manifest.json').read_bytes())
    for r in readings:
        if r['product']!=product:continue
        header=re.search(r'^===.*?'+r['side']+r'(?: Side)?.*?===[ \t]*$',section,re.M)
        assert header,(product,r['side'],'Missing side subsection')
        after=header.end();next_header=re.search(r'^===',section[after:],re.M);limit=after+next_header.start() if next_header else len(section)
        part=section[after:limit];code=mw.parse(part);links=code.filter_wikilinks()
        direct=[link for link in links if str(link.title).strip()==r['article']]
        if direct:
            assert len(direct)==1,(r['article'],'Duplicate direct link');continue
        m=next(row for row in manifest if row['proposed_article']==r['article'])
        options=list(dict.fromkeys([r['title'],m['checklist_target'],r['printed_title']]))
        found=[]
        for target in options:
            found=[link for link in links if str(link.title).strip()==target]
            if found:break
        assert len(found)==1,(r['article'],'Ambiguous or missing side-specific checklist target',len(found))
        found[0].title=r['article'];found[0].text=r['printed_title']
        section=section[:after]+str(code)+section[limit:]
    new=old[:start]+section+old[end:];assert not lint(new,product)[0],lint(new,product)[0]
    packets.append(dict(title=product,text=new,before_revid=rev['revid'],before_sha256=hashlib.sha256(old.encode()).hexdigest(),section=None,summary='Link the next verified original foil articles directly from the checklist (#381)',atomic_reason='Guarded replacement of foil checklist links; all other sections are byte-conserved'))
for r,f in zip(readings,files):
    p=provenance(r)
    text='== Build notes ==\nThe '+r['product']+' foil publication was checked against [[:'+f['title']+'|the original physical foil photograph]] from '+p['credit']+'. The original JPEG and provenance are retained on the File page. Printed wording, symbols and statistics were read from this face independently of earlier printings. Publication identity is separate from any playable mapping.\n\n~~~~\n'
    if r.get('reading_note'):text=text.replace('\n\n~~~~','\n\n'+r['reading_note']+'\n\n~~~~')
    if r.get('printed_extra_stats',{}).get('Hyperdrive'):
        text=text.replace('\n\n~~~~','\n\nThe foil prints “Hyperdrive '+r['printed_extra_stats']['Hyperdrive']+'” as the speed label. That printed label is retained separately in the infobox.\n\n~~~~')
    talk.append(dict(title='Talk:'+r['article'],text=text,new=True,signed_note=True,summary='Record independent physical-foil transcription and source provenance (#381)'))
(root/(stage+'-set-heads.json')).write_text(json.dumps(heads,ensure_ascii=False,indent=2),encoding='utf8')
for kind,rows in [('set',packets),('talk',talk)]:
    (root/(stage+'-'+kind+'-packet.json')).write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print(len(packets),'set checklists;',len(talk),'signed source notes prepared')
