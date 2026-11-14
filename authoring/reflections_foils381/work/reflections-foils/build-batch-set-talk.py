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
    for r in readings:
        if r['product']!=product:continue
        options=list(dict.fromkeys([r['title'],r['printed_title']]))
        found=[t for t in options if '[['+t+']]' in section]
        assert len(found)==1,(r['article'],found)
        needle='[['+found[0]+']]';assert section.count(needle)==1,(r['article'],section.count(needle))
        section=section.replace(needle,'[['+r['article']+'|'+r['printed_title']+']]')
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
