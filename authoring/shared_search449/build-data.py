import json,re,hashlib,html,base64,collections,xml.etree.ElementTree as ET,sys
from pathlib import Path
from urllib.parse import quote
sys.path.insert(0,'work/japanese-infobox287/vendor');import mwparserfromhell as mw
p=Path(__file__).parent;heads=json.loads((p/'source-heads.json').read_bytes());files=json.loads((p/'files.json').read_bytes());filemap={r['title'][5:]:r for r in files}
symbols=[]
symbol_names=[('none','None (Premiere)',['premiere','none'],None),('anh','A New Hope',['anh'], 'A New Hope'),('hoth','Hoth',[],'Hoth (expansion)'),('dagobah','Dagobah',[],'Dagobah (expansion)'),('cloudcity','Cloud City',['cc'],'Cloud City (expansion)'),('jabbaspalace',"Jabba's Palace",['jp','jabbas palace'],"Jabba's Palace"),('premium','Premium',['premium silver','jedi pack'], 'Premium'),('ds2','Death Star II',['ds2'],'Death Star II (expansion)'),('tatooine','Tatooine',['tat'],'Tatooine (expansion)'),('coruscant','Coruscant',['cor'],'Coruscant (expansion)'),('reflections2','Reflections II',['ref2','reflections 2'],'Reflections II: Expanding the Galaxy')]
def url(title):return 'https://wiki.swccg.com/wiki/'+quote(title.replace(' ','_'),safe=':(),')
for key,label,aliases,wiki in symbol_names:
    image=Path('work/set-symbols-435/symbols')/('set-'+key+'-decipher.webp')
    # No unverified Coruscant ring replacement is smuggled into the pilot.
    uri='data:image/webp;base64,'+base64.b64encode(image.read_bytes()).decode() if image.exists() and key!='coruscant' else None
    symbols.append(dict(id=key,label=label,aliases=aliases,image=uri,wiki=url(wiki) if wiki else None))
def field(t,key):return str(t.get(key).value).strip() if t.has(key) else ''
def plain(s):
    code=mw.parse(s)
    for tag in list(code.filter_tags()):
        if str(tag.tag).lower()=='ref':code.remove(tag)
    for link in list(code.filter_wikilinks()):
        name=str(link.title)
        if name.lower().startswith('file:'):
            found=next((x for x in symbols if x['id']!='none' and x['label'].lower().replace("'",'').replace(' ','-') in name.lower().replace("'",'')),None)
            aliases={'Icon-set-Jabbas-Palace.png':'jabbaspalace','Icon-set-Tatooine.png':'tatooine'}
            key=aliases.get(name[5:]) or (found['id'] if found else None);assert key,(name,'Unmapped game-text image')
            label=next(x['label'] for x in symbols if x['id']==key);code.replace(link,'['+label+']')
        else:code.replace(link,str(link.text or link.title))
    return html.unescape(code.strip_code()).strip()
# These observations were read independently from the full original faces,
# not copied from the engine's generated blueprint database.
observed={
 'Seeking An Audience':('premium','unique',['jabbaspalace']),
 'Seeking An Audience (Reflections III Foil)':('premium','unique',['jabbaspalace']),
 'Shmi Skywalker':('tatooine','unique',['tatooine']),
 'You Will Go To The Dagobah System':('hoth','unrestricted',['hoth','dagobah']),
 'Rendezvous Point On Tatooine':('cloudcity','unrestricted',['cloudcity','jabbaspalace']),
 'Presence Of The Force':('none','restricted-2',[]), 'Shistavanen Wolfman':('none','restricted-3',[]),
 'Reserve Pilot':('anh','restricted-2',[]), 'Trade Federation Droid Control Ship':('coruscant','diamond-1',[]),
 'Luke Skywalker':('none','unique',[]), 'Darth Vader':('none','unique',[]),
 'Admiral Ackbar':('ds2','unique',[]), 'Bacta Tank':('hoth','unique',[]),
 'Captain Han Solo':('cloudcity','unique',[]), 'Imperial Artillery':('coruscant','restricted-2',[]),
 'Admiral Ozzel':('hoth','unique',[]), 'The Emperor':('reflections2','unique',[]),
 'Imperial Command':('ds2','unrestricted',[]), "Twi'lek Advisor":('jabbaspalace','unique',[]),
 'Officer Evax':('anh','unique',[]),'Rebel Barrier':('none','unrestricted',[]),
 'Houjix':('anh','unrestricted',[]),'Ghhhk':('anh','unrestricted',[])}
cards=[];ledger=[]
for title,(symbol,unique,refs) in observed.items():
    h=heads[title];source=h['revisions'][0]['slots']['main']['content'];t=next(x for x in mw.parse(source).filter_templates(recursive=False) if str(x.name).strip()=='Card')
    card_id=field(t,'publication_id') or field(t,'card_uid');assert card_id,title
    family='112_7' if title.endswith('(Reflections III Foil)') else re.sub(r'(?:o\d*|d)$','',field(t,'card_uid'))
    assert re.fullmatch(r'\d+_\d+',family),family
    recorded=None if field(t,'publication_id') else field(t,'card_uid')
    text=plain(field(t,'game_text'));assert text and 'File:' not in text,title
    tokens=[]
    for token in re.findall(r'\[([^\]]+)\]',text):
        sym=next((x for x in symbols if any(token.casefold()==v.casefold() for v in [x['label']]+x['aliases'])),None)
        if sym:tokens.append(sym['id'])
    assert set(tokens)==set(refs),(title,tokens,refs)
    face=filemap[field(t,'image')]
    card=dict(id=card_id,title=title,gameTitle=field(t,'display_title') or field(t,'title') or title,familyId=family,recordedId=recorded,product=field(t,'set'),printedSymbol=symbol,uniqueness=unique,referencedSymbols=refs,text=text,wiki=url(title),sourceRevision=h['revisions'][0]['revid'],sourceFace=face['url'])
    cards.append(card);ledger.append(dict(title=title,id=card_id,source_revision=card['sourceRevision'],face=face,printed_symbol=symbol,uniqueness_observed=unique,reference_symbols_observed=refs,verified_by='MemoryCoreChatGPT inspected full source faces/contact sheets and Seeking printed-versus-inline close-up; foil face separately inspected',scope='printed fields only; no inferred gameplay changes'))
decks=[];deckproof=[]
for title,h in heads.items():
    if title in observed:continue
    source=h['revisions'][0]['slots']['main']['content'];name=re.search(r'Media:([^\]|]+\.txt)',source).group(1).strip();f=filemap[name];tree=ET.fromstring((p/f['local_file']).read_bytes())
    counts=collections.Counter((n.attrib['blueprintId'],'main' if n.tag=='card' else 'outside',n.attrib.get('title','')) for n in tree if n.tag in ['card','cardOutsideDeck'])
    entries=[dict(recordedId=id,familyId=re.sub(r'(?:o\d*|d)(?=_BACK$|$)','',id.removesuffix('_BACK')),zone=zone,title=name,count=count) for (id,zone,name),count in counts.items()]
    main=sum(x['count'] for x in entries if x['zone']=='main');outside=sum(x['count'] for x in entries if x['zone']=='outside');assert main==60,(title,main)
    # Independent text-list quantities must reconcile with the original XML.
    deckpart=source.split('== Decklist ==',1)[1].split('== Sources ==',1)[0]
    text_counts=[int(n) for n in re.findall(r'^\*\s*(\d+)x?\s',deckpart,re.M)]
    assert sum(text_counts)==main+outside,(title,sum(text_counts),main,outside)
    def info(label):
        m=re.search(r"\* '''"+label+r":'''\s*\[\[([^\]|]+)",source);return m.group(1) if m else ''
    d=dict(id='wiki:'+str(h['pageid']),title=title,player=info('Player'),event=info('Event'),format=info('Format'),year=2026,wiki=url(title),download=f['url'],sourceRevision=h['revisions'][0]['revid'],mainCount=main,outsideCount=outside,complete=True,entries=entries)
    decks.append(d);deckproof.append(dict(title=title,id=d['id'],xml=f,main=main,outside=outside,wiki_quantity_total=sum(text_counts),source_revision=d['sourceRevision'],starting_cards_not_counted_twice=True,pilot_membership=[dict(card=c['id'],family=c['familyId'],count=sum(e['count'] for e in entries if e['familyId']==c['familyId'] and e['zone']=='main')) for c in cards]))
data=dict(schemaVersion=1,snapshotId='449-'+hashlib.sha256(json.dumps([cards,decks],sort_keys=True).encode()).hexdigest()[:12],title='Shared search pilot',cards=cards,decks=decks,symbols=symbols,coverage=str(len(cards))+' card printings and four complete published decklists. Set-symbol roles and printed uniqueness only; this is not the full catalog or a legality checker.',sourcesCheckedOn='2026-11-14',interfaces=dict(wiki=url('SWCCG Wiki:Samples/Shared search pilot'),gemp='https://play.swccg.com/gemp-swccg/searchPilot.html',scomp='https://swccg.com/snapshots/review/shared-search-449/scomp.html'))
(p/'product/data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
(p/'printed-field-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2),encoding='utf8');(p/'deck-membership-proof.json').write_text(json.dumps(deckproof,ensure_ascii=False,indent=2),encoding='utf8')
print(data['snapshotId'],len(cards),'printings;',len(decks),'complete decks; independent Wiki/XML counts agree')
for d in deckproof:print(d['title'],[(x['card'],x['count']) for x in d['pilot_membership'] if x['count']])
