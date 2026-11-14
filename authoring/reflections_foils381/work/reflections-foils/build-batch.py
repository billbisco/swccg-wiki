import hashlib,json,re,sys
from pathlib import Path
sys.path.insert(0,'work/japanese-infobox287/vendor');import mwparserfromhell as mw
sys.path.insert(0,'work/wiki-tools');from publication_policy import lint
root=Path(__file__).parent;stage=sys.argv[1]
from source_registry import provenance
from navigation import new_navigation
from publication_identity import publication_id
readings=json.loads((root/(stage+'-readings.json')).read_bytes());files=json.loads((root/(stage+'-files-payload.json')).read_bytes())
heads=json.loads((root/(stage+'-family-heads.json')).read_bytes());families=json.loads((root/(stage+'-families.json')).read_bytes())
check='[https://res.starwarsccg.org/Resources/swccgcardlist4.0.pdf Complete Card List v4.0], pp. 28–32 (collecting compilation). Preserved copy: [https://web.archive.org/web/20261009184033/https://res.starwarsccg.org/Resources/swccgcardlist4.0.pdf Internet Archive].'
encyc='[https://res.starwarsccg.org/Resources/Star_Wars_CCG_Collecting_Encyclopedia_3.2.pdf SWCCG Collecting Encyclopedia 3.2], Reflections product entry (collecting reference). Preserved copy: [https://web.archive.org/web/20261008192828/https://res.starwarsccg.org/Resources/Star_Wars_CCG_Collecting_Encyclopedia_3.2.pdf Internet Archive].'
def card(text):return next(t for t in mw.parse(text).filter_templates(recursive=False) if str(t.name).strip()=='Card')
def expansion_link(name):return '[[Death Star II (expansion)|Death Star II]]' if name=='Death Star II' else '[['+name+']]'
def source(title):return heads[title]['revisions'][0]['slots']['main']['content']
def nav(base):
    t=card(source(base));k='versions' if t.has('versions') else 'printings'
    return str(t.get(k).value).strip()
def entry(r):return "'''Decipher ("+{'Reflections':'Reflections','Reflections II: Expanding the Galaxy':'Reflections II','Reflections III':'Reflections III'}[r['product']]+" foil)''' — [["+r['article']+'|'+r['printed_title']+" (foil)]]"
def insert(value,line):
    bits=re.split(r'<br\s*/?>',value)
    index=next((i for i,b in enumerate(bits) if re.match(r"\s*'''(?:Decipher Errata|PC Errata|Virtual)",b)),len(bits))
    bits.insert(index,line);return '<br />'.join(bits)
packets=[];old_drafts={};checks=[]
for r,f in zip(readings,files):
    title=r['article'];product=r['product'];product_label={'Reflections':'Reflections','Reflections II: Expanding the Galaxy':'Reflections II','Reflections III':'Reflections III'}[product];release={'Reflections':'January 2000','Reflections II: Expanding the Galaxy':'January 2001','Reflections III':'October 2001'}[product];pid='decipher-'+re.sub(r'[^a-z0-9]+','-',product_label.lower())+'-'+re.sub(r'[^a-z0-9]+','-',r['printed_title'].lower()).strip('-')+'-foil-en'
    pid=publication_id(r['article'],product)
    p=provenance(r)
    face='<ref name="foil-face">[[:'+f['title']+'|Original printed '+product_label+' foil face]], '+p['credit']+'.</ref>'
    caption=product_label+' foil, photographed in a grading holder.' if p['kind']=='PSA' else product_label+' foil.'
    fields=dict(title=r['printed_title'],publication_id=pid,image=f['name'],image_note=caption,side=r['side'],type=r['type'])
    if r.get('alternate_image'):
        assert r.get('artwork_verification',{}).get('verified'),title
        fields['ai_mark']='1'
    for k in ['image_rotation','image_rotated_height']:
        if k in r:fields[k]=r[k]
    for k in ['subtype','type_display','model']:
        if k in r:fields[k]=r[k]
    if 'subtype' in r:fields['subtype_link']=r['subtype']
    fields.update(set=product,language='en',language_display='English',border_finish='Foil',release=release,publisher='[[Decipher]]',era='[[Decipher era]]',rarity=r['rarity'],rarity_link='Rarity',uniqueness=r['uniqueness'])
    if r['set_icon'] is None:fields['set_icon']='None ('+expansion_link(r['original_set'])+')'
    else:
        icon={'A New Hope':'A-New-Hope','Cloud City':'Cloud-City',"Jabba's Palace":'Jabbas-Palace','Special Edition':'Special-Edition','Death Star II':'Death-Star-II','Premium':'premium'}.get(r['set_icon'],r['set_icon'])
        target='Death Star II (expansion)' if r['original_set']=='Death Star II' else r['original_set']
        fields['set_icon']='[[File:Icon-set-'+icon+'.png|20px|link='+target+']] '+('Premium — ' if r['set_icon']=='Premium' else '')+expansion_link(r['original_set'])
        if r['set_icon'] in ['Coruscant','Reflections II','Theed Palace']:
            fields['set_icon']=expansion_link(r['original_set'])
    for k in ['destiny','power','ability','armor','maneuver','hyperspeed','landspeed','deploy','forfeit','printed_label','parsec','light_icons','dark_icons']:
        if k in r:fields[k]=r[k]
    fields['icons']=' '.join('[['+x+']]' for x in r['icons'])
    if r['type']=='Character':fields.setdefault('landspeed','1')
    fields['extra_info']='<tr><th>Original expansion</th><td>'+expansion_link(r['original_set'])+'</td></tr><tr><th>Publication ID</th><td><code>'+pid+'</code></td></tr>'
    if r.get('printed_extra_stats'):fields['extra_info']=''.join('<tr><th>'+k+'</th><td>'+v+'</td></tr>' for k,v in r['printed_extra_stats'].items())+fields['extra_info']
    fields['version_label']=product_label+' foil';fields['set_band']='Decipher';fields['navigation']='[['+product+']] · [['+r['title']+'|Earlier non-foil printing]]'
    fields['lead']="'''"+r['printed_title']+"''' is a [["+r['side']+']] [['+r['type']+']] released as a '+{'VR':'very-rare','SR':'super-rare','UR':'ultra-rare'}[r['rarity']]+' foil in [['+product+']] in '+release+'.<ref name="checklist">'+check+'</ref><ref name="encyc">'+encyc+'</ref> It is a foil printing of the '+expansion_link(r['original_set'])+' card.'+face
    if r['lore'] is not None:fields['lore']=r['lore']+'<ref name="foil-face" />'
    game=r['game_text']
    if r['type']=='Epic Event':game=game.replace('\n*Your','\n<nowiki>*</nowiki>Your').replace('\n','<br />\n')
    fields['game_text']=game+'<ref name="foil-face" />'
    fields['versions']=new_navigation(r,heads,families,readings)
    fields['sources']='* Original printed foil face: [[:'+f['title']+'|'+r['printed_title']+', '+product_label+' foil]], '+p['credit']+'.'
    fields['has_refs']='1'
    text='{{Card\n'+''.join('|'+k+'='+v+'\n' for k,v in fields.items())+'}}\n'
    flags=lint(text,title)[0];checks.append(dict(title=title,lint=flags));assert not flags,(title,flags)
    packets.append(dict(title=title,text=text,new=True,section=0,summary='Document the verified original Reflections foil printing and printed fields (#381)'))
    for sibling in families[r['title']]:
        if sibling in {row['article'] for row in readings}:continue
        old=old_drafts.get(sibling,source(sibling));code=mw.parse(old);t=next(t for t in code.filter_templates(recursive=False) if str(t.name).strip()=='Card')
        if any(t.has(k) and '{{Card versions/' in str(t.get(k).value) for k in ['versions','printings']):continue
        for k in ['versions','printings']:
            if t.has(k):
                value=str(t.get(k).value);
                if r['article'] not in value:t.get(k).value=insert(value.strip(),entry(r))+'\n'
                else:assert value.count(r['article'])==1,(sibling,'Duplicate foil link')
        old_drafts[sibling]=str(code)
(root/(stage+'-new-packet.json')).write_text(json.dumps(packets,ensure_ascii=False,indent=2),encoding='utf8')
family=[]
for title,text in old_drafts.items():
    rev=heads[title]['revisions'][0];old=rev['slots']['main']['content']
    family.append(dict(title=title,text=text,before_revid=rev['revid'],before_sha256=hashlib.sha256(old.encode()).hexdigest(),section=0,summary='Link the verified Reflections foil in this card family (#381)'))
(root/(stage+'-family-packet.json')).write_text(json.dumps(family,ensure_ascii=False,indent=2),encoding='utf8')
(root/(stage+'-new-lint.json')).write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf8')
print(len(packets),'new articles, lint 0;',len(family),'family navigation drafts (old citations pending repair)')
