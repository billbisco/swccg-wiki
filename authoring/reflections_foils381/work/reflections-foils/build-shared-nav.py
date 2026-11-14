import hashlib,json,sys
from pathlib import Path
sys.path.insert(0,'work/japanese-infobox287/vendor');import mwparserfromhell as mw
from navigation import canonical
root=Path(__file__).parent;stage=sys.argv[1]
heads=json.loads((root/(stage+'-family-heads.json')).read_bytes());readings=json.loads((root/(stage+'-readings.json')).read_bytes());drafts={}
for r in readings:
    source=heads[canonical(r['title'],heads)]['revisions'][0]['slots']['main']['content'];card=next(t for t in mw.parse(source).filter_templates(recursive=False) if str(t.name).strip()=='Card')
    for k in ['versions','printings']:
        if not card.has(k):continue
        for nav in mw.parse(str(card.get(k).value)).filter_templates():
            if not str(nav.name).strip().startswith('Card versions/'):continue
            title='Template:'+str(nav.name).strip();old=drafts.get(title,heads[title]['revisions'][0]['slots']['main']['content'])
            assert r['article'] not in old
            label={'Reflections':'Reflections','Reflections II: Expanding the Galaxy':'Reflections II','Reflections III':'Reflections III'}[r['product']]
            entry='<br /><strong class="card-family-edition" style="font-size:95%;"><u>[['+r['product']+'|'+label+']]</u></strong><br /><!--\n-->{{Card version link|page='+r['article']+'|label=Foil|current={{{current|{{FULLPAGENAME}}}}}}}'
            index=old.index('</div>');new=old[:index]+entry+old[index:]
            # Retire the pilot's now-resolved gap sentence without changing membership policy.
            new=new.replace('The English Reflections foil is a known follow-up publication-inventory gap; it is not represented by an ordinary black-border image or an invented playable ID.','The English Reflections foil is included with its independently verified physical foil face and publication identity.')
            drafts[title]=new
rows=[]
for title,text in drafts.items():
    rev=heads[title]['revisions'][0];old=rev['slots']['main']['content']
    rows.append(dict(title=title,text=text,before_revid=rev['revid'],before_sha256=hashlib.sha256(old.encode()).hexdigest(),section=None,atomic_reason='Add one verified publication to existing shared navigator and retire its resolved pilot gap sentence; exact source guards preserve all other entries',summary='Add the verified Reflections foil to the existing shared family navigator (#381)'))
(root/(stage+'-shared-nav-packet.json')).write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print(len(rows),'shared navigator updates')
