import hashlib,json,re,sys
from pathlib import Path
sys.path.insert(0,'work/japanese-infobox287/vendor');import mwparserfromhell as mw
sys.path.insert(0,'work/wiki-tools');from style_lint import lint
root=Path(__file__).parent
readings=json.loads((root/'first-readings.json').read_bytes());files=json.loads((root/'first-files-payload.json').read_bytes())
heads=json.loads((root/'first-family-heads.json').read_bytes());families=json.loads((root/'first-families.json').read_bytes())
check='[https://res.starwarsccg.org/Resources/swccgcardlist4.0.pdf Complete Card List v4.0], pp. 28–32 (collecting compilation). Preserved copy: [https://web.archive.org/web/20261009184033/https://res.starwarsccg.org/Resources/swccgcardlist4.0.pdf Internet Archive].'
encyc='[https://res.starwarsccg.org/Resources/Star_Wars_CCG_Collecting_Encyclopedia_3.2.pdf SWCCG Collecting Encyclopedia 3.2], Reflections product entry (collecting reference). Preserved copy: [https://web.archive.org/web/20261008192828/https://res.starwarsccg.org/Resources/Star_Wars_CCG_Collecting_Encyclopedia_3.2.pdf Internet Archive].'
def card(text):return next(t for t in mw.parse(text).filter_templates(recursive=False) if str(t.name).strip()=='Card')
def source(title):return heads[title]['revisions'][0]['slots']['main']['content']
def nav(base):
    t=card(source(base));k='versions' if t.has('versions') else 'printings'
    return str(t.get(k).value).strip()
def entry(r):return "'''Decipher (Reflections foil)''' — [["+r['article']+'|'+r['printed_title']+" (Reflections foil)]]"
def insert(value,line):
    bits=re.split(r'<br\s*/?>',value)
    index=next((i for i,b in enumerate(bits) if re.match(r"\s*'''(?:Decipher Errata|PC Errata|Virtual)",b)),len(bits))
    bits.insert(index,line);return '<br />'.join(bits)
packets=[];old_drafts={};checks=[]
for r,f in zip(readings,files):
    title=r['article'];pid='decipher-reflections-'+re.sub(r'[^a-z0-9]+','-',r['printed_title'].lower()).strip('-')+'-foil-en'
    face='<ref name="foil-face">[[:'+f['title']+'|Original printed Reflections foil face]], PSA certification '+r['physical_cert']+'.</ref>'
    fields=dict(title=r['printed_title'],publication_id=pid,image=f['name'],image_note='Reflections foil, photographed in a grading holder.',side=r['side'],type=r['type'])
    for k in ['subtype','model']:
        if k in r:fields[k]=r[k]
    if 'subtype' in r:fields['subtype_link']=r['subtype']
    fields.update(set='Reflections',language='en',language_display='English',border_finish='Foil',release='January 2000',publisher='[[Decipher]]',era='[[Decipher era]]',rarity=r['rarity'],rarity_link='Rarity',uniqueness=r['uniqueness'])
    if r['set_icon'] is None:fields['set_icon']='None ([[Premiere]])'
    else:
        icon={'A New Hope':'A-New-Hope',"Jabba's Palace":'Jabbas-Palace','Special Edition':'Special-Edition'}.get(r['set_icon'],r['set_icon'])
        fields['set_icon']='[[File:Icon-set-'+icon+'.png|20px|link='+r['original_set']+']] [['+r['original_set']+']]'
    for k in ['destiny','power','ability','armor','maneuver','deploy','forfeit','printed_label']:
        if k in r:fields[k]=r[k]
    fields['icons']=' '.join('[['+x+']]' for x in r['icons'])
    if r['type']=='Character':fields['landspeed']='1'
    fields['extra_info']='<tr><th>Original expansion</th><td>[['+r['original_set']+']]</td></tr><tr><th>Publication ID</th><td><code>'+pid+'</code></td></tr>'
    fields['version_label']='Reflections foil';fields['set_band']='Decipher';fields['navigation']='[[Reflections]] · [['+r['title']+'|Earlier non-foil printing]]'
    fields['lead']="'''"+r['printed_title']+"''' is a [["+r['side']+']] [['+r['type']+']] released as a '+{'VR':'very-rare','SR':'super-rare','UR':'ultra-rare'}[r['rarity']]+' foil in [[Reflections]] in January 2000.<ref name="checklist">'+check+'</ref><ref name="encyc">'+encyc+'</ref> It is a foil printing of the [['+r['original_set']+']] card.'+face
    if r['lore'] is not None:fields['lore']=r['lore']+'<ref name="foil-face" />'
    game=r['game_text']
    if r['type']=='Epic Event':game=game.replace('\n*Your','\n<nowiki>*</nowiki>Your').replace('\n','<br />\n')
    fields['game_text']=game+'<ref name="foil-face" />'
    original_nav=nav(r['title']);thispage=re.compile(r"'''(?:this page|this printing)'''")
    newnav=thispage.sub('[['+r['title']+']]',original_nav)
    newnav=insert(newnav,"'''Decipher (Reflections foil)''' — '''this page'''")
    # Keep every known existing family member reachable from the new article.
    present={str(w.title).strip() for w in mw.parse(newnav).filter_wikilinks()}
    for sibling in families[r['title']]:
        if sibling not in present and sibling!=r['title']:
            newnav+='<br />[['+sibling+']]';present.add(sibling)
    fields['versions']=newnav
    fields['sources']='* Original printed foil face: [[:'+f['title']+'|'+r['printed_title']+', Reflections foil]], Robert John collection, PSA certification '+r['physical_cert']+'.'
    fields['has_refs']='1'
    text='{{Card\n'+''.join('|'+k+'='+v+'\n' for k,v in fields.items())+'}}\n'
    flags=lint(text,title)[0];checks.append(dict(title=title,lint=flags));assert not flags,(title,flags)
    packets.append(dict(title=title,text=text,new=True,section=0,summary='Document the verified original Reflections foil printing and printed fields (#381)'))
    for sibling in families[r['title']]:
        old=old_drafts.get(sibling,source(sibling));code=mw.parse(old);t=next(t for t in code.filter_templates(recursive=False) if str(t.name).strip()=='Card')
        for k in ['versions','printings']:
            if t.has(k):
                value=str(t.get(k).value);assert r['article'] not in value,(sibling,'Foil already present; refresh baseline')
                t.get(k).value=insert(value.strip(),entry(r))+'\n'
        old_drafts[sibling]=str(code)
(root/'first-new-packet.json').write_text(json.dumps(packets,ensure_ascii=False,indent=2),encoding='utf8')
family=[]
for title,text in old_drafts.items():
    rev=heads[title]['revisions'][0];old=rev['slots']['main']['content']
    family.append(dict(title=title,text=text,before_revid=rev['revid'],before_sha256=hashlib.sha256(old.encode()).hexdigest(),section=0,summary='Link the verified Reflections foil in this card family (#381)'))
(root/'first-family-packet.json').write_text(json.dumps(family,ensure_ascii=False,indent=2),encoding='utf8')
(root/'first-new-lint.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf8')
print(len(packets),'new articles, lint 0;',len(family),'family navigation drafts (old citations pending repair)')
