import collections,json,re,sys
from pathlib import Path
root=Path(__file__).parent
sys.path.insert(0,str(root/'vendor'))
import mwparserfromhell as mw
details=json.loads((root/'conversion-details.json').read_bytes())
drafts=json.loads((root/'drafts.json').read_bytes())
foil={
"Anakin's Lightsaber":'Hoth','Brainiac':'A New Hope','Darth Vader':'Premium','Death Star':'Premium',
'Dr. Evazan':'Premiere','Grand Moff Tarkin':'Premiere','Imperial Walker':'Hoth','Leia':'Hoth','Luke Skywalker':'Premiere',
'Obi-Wan Kenobi':'Premiere',"Obi-Wan's Lightsaber":'Premiere','Rebel Snowspeeder':'Hoth','The Circle Is Now Complete':'Premiere',
'Trample':'Hoth',"Vader's Lightsaber":'Premiere','Wedge Antilles':'A New Hope',
}
assets={'Hoth':('Icon-set-Hoth.png','Hoth Limited','Hoth'),'A New Hope':('Icon-set-A-New-Hope.png','A New Hope Limited','A New Hope'),'Premium':('Icon-set-premium.png','Premium (icon)','Premium')}
manifest=[]
for row,detail in zip(drafts,details):
    assert row['title']==detail['title']
    title=row['title'];p=detail['params'];setname=p['set']
    if setname.startswith('Reflections'):
        base=title.split(' (Japanese Reflections',1)[0]
        key=foil[base];basis='Own foil photograph; matched printed badge to existing named icon asset'
    elif not row['is_ja']:
        key='Premium';basis='Own oversized promo face, visible Premium badge beside lore'
    elif 'Empire Strikes Back' in setname:
        if p['gemp_id'].startswith('1404_'):
            key='Premium';basis='Japanese ESB Two-Player premium/exclusive face; Premium sphere, consistent with #276 printed-face evidence'
        else:
            match=re.search(r'\b136([123])_',p['gemp_id']);assert match,(title,p.get('gemp_id'))
            key={'1':'Premiere','2':'A New Hope','3':'Hoth'}[match[1]];basis='Edition printing ID identifies original design set; #287 R7 / #286 D1'
    elif 'Premiere' in setname:key='Premiere';basis='#287 R7: Japanese Premiere-family no-symbol rule'
    elif setname=='Hoth (Japanese)':key='Hoth';basis='#287 R7: Japanese Hoth printed symbol'
    elif setname=='A New Hope (Japanese)':key='A New Hope';basis='#287 R7: Japanese A New Hope printed symbol'
    else:raise ValueError((title,setname))
    if key=='Premiere':value='None ([[Premiere Limited|Premiere]])'
    else:
        file,target,label=assets[key]
        value=f'[[File:{file}|20px|link={target}]] [[{target}|{label}]]'
    p['set_icon']=value
    code=mw.parse(row['text']);template=code.filter_templates(recursive=False)[0]
    template.add('set_icon',value+'\n',showkey=True,preserve_spacing=False)
    row['text']=str(code)
    manifest.append(dict(title=title,symbol=key,display=value,basis=basis))
(root/'drafts.json').write_text(json.dumps(drafts,ensure_ascii=False,indent=2),encoding='utf8')
(root/'conversion-details.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),encoding='utf8')
(root/'set-icon-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
print('Verified icon assignments',dict(collections.Counter(r['symbol'] for r in manifest)))
