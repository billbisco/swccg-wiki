"""Build exact-publication foil tables, preserving all other set content."""
import collections,hashlib,json,re,sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import requests
from images import rotated
sys.path.insert(0,'work/japanese-infobox287/vendor');import mwparserfromhell as mw
sys.path.insert(0,'work/wiki-tools');from style_lint import lint
root=Path(__file__).parent;manifest=json.loads(Path('work/reflections-foils/manifest.json').read_bytes())
products=list(dict.fromkeys(r['product'] for r in manifest));template='Template:Card scan request'
def fetch(titles,images=False):
    args=dict(action='query',format='json',formatversion=2,titles='|'.join(titles),prop='revisions|flagged'+('|imageinfo' if images else ''),rvprop='ids|timestamp|content',rvslots='main')
    if images:args['iiprop']='url|sha1|timestamp|size|mime'
    r=requests.get('https://wiki.swccg.com/api.php',params=args,timeout=60);r.raise_for_status();j=r.json();assert 'error' not in j,j;return j['query']['pages']
titles=[r['proposed_article'] for r in manifest]+products+[template]+['Talk:'+p for p in products]
heads={}
with ThreadPoolExecutor(max_workers=3) as pool:
    for batch in pool.map(fetch,[titles[i:i+35] for i in range(0,len(titles),35)]):heads.update({h['title']:h for h in batch})
def source(h):return h['revisions'][0]['slots']['main']['content']
def card(title):return next(t for t in mw.parse(source(heads[title])).filter_templates(recursive=False) if str(t.name).strip()=='Card')
cards={r['proposed_article']:card(r['proposed_article']) for r in manifest}
def val(t,key,default=''):return str(t.get(key).value).strip() if t.has(key) else default
filenames=sorted({'File:'+val(t,'image') for t in cards.values() if val(t,'image')})
files={}
with ThreadPoolExecutor(max_workers=3) as pool:
    for batch in pool.map(lambda ts:fetch(ts,True),[filenames[i:i+35] for i in range(0,len(filenames),35)]):files.update({h['title']:h for h in batch})
marker='''<includeonly><span class="card-scan-request" style="display:inline-block;padding:0.4em;border:1px dashed #767676;text-align:center;"><span aria-hidden="true">📷</span> '''+"'''Scan requested'''"+'''<br />[[Special:Upload|Contribute a scan]]<br /><small>[[Talk:{{{card|{{FULLPAGENAME}}}}}|Discuss this card]]</small></span></includeonly><noinclude>
Use <code><nowiki>{{Card scan request|card=Exact card article}}</nowiki></code> in an empty card-image cell. The camera and text invite a scan of the named printing. Keep any existing photograph visible; this marker is for an absent image, not a replacement photograph.

Scans should show the complete card, including its borders, title, text and symbols. Identify the set, language, foil finish and alternate image where applicable. Upload only an image you are entitled to contribute and record its source on the File page.
</noinclude>
'''
packet=[];proof=[];inventory=[]
def add(title,text,summary,signed=False):
    h=heads[title];row=dict(title=title,text=text,summary=summary,section=None,signed_note=signed)
    if 'revisions' in h:
        row.update(before_revid=h['revisions'][0]['revid'],before_sha256=hashlib.sha256(source(h).encode()).hexdigest())
    else:row['new']=True
    flags=lint(text,title)[0]
    if flags:
        baseline=lint(source(h),title)[0]
        assert signed and text.startswith(source(h)) and flags==baseline and all(f.startswith('ARCHIVE') for f in flags),(title,flags)
        row['lint_text']=text[len(source(h)):];row['unchanged_prior_talk_flags']=flags
        assert not lint(row['lint_text'],title)[0]
    packet.append(row)
def clean(value):
    code=mw.parse(value)
    for tag in list(code.filter_tags()):
        if str(tag.tag).lower()=='ref':code.remove(tag)
    return str(code).replace('\n','<br />')
def image_cell(row,t):
    title=row['proposed_article'];filename=val(t,'image');info=files.get('File:'+filename,{}).get('imageinfo',[None])[0]
    if not filename or not info:return '{{Card scan request|card='+title+'}}',False
    alt=row['label']+', '+row['product']+' foil, '+row['language']
    if val(t,'image_rotation')=='left':
        image=rotated(filename,title,alt,info)
    else:image=f'[[File:{filename}|200px|link={title}|alt={alt}]]'
    return image,True
add(template,marker,'Add an accessible missing-card-scan invitation (#430)')
for product in products:
    old=source(heads[product]);match=re.search(r'^== (?:Possible foils|Foil cards) ==\n.*?(?=^== [^=]|\Z)',old,re.M|re.S);assert match,product
    oldfoil=match.group();intro=re.split(r'^=== ',oldfoil,maxsplit=1,flags=re.M)[0].split('\n',1)[1].strip()
    intro=re.sub(r'^<span id="Possible_foils"></span>\n','',intro).split('\n\nClick a card image',1)[0].strip()
    foil='== Foil cards ==\n<span id="Possible_foils"></span>\n'+intro+'\n\nClick a card image or title to open that foil printing. Have a clearer scan? [[Special:Upload|Contribute a scan]] of the complete card, including its borders, title, text and symbols. Identify the set, language and foil finish on the File page. <span aria-hidden="true">📷</span> '''+"'''Scan requested'''"+' marks a missing image; existing photographs remain visible.\n\n'
    rows=[r for r in manifest if r['product']==product]
    for side in ['Light','Dark']:
        selected=[r for r in rows if r['side']==side]
        foil+='=== [['+side+'|'+side+' Side]] ===\n<div style="overflow-x:auto;">\n{| class="wikitable card-thumbs sortable"\n|+ '+side+' Side foils ('+str(len(selected))+')\n! Image !! Card !! Language !! Type !! Rarity !! Destiny !! Game text\n'
        for r in selected:
            title=r['proposed_article'];t=cards[title];image,available=image_cell(r,t)
            label=val(t,'title',r['label'])+(' (AI)' if r.get('alternate_image') else '')
            kind='[['+val(t,'type')+']]'
            if val(t,'subtype'):kind+=' — [['+val(t,'subtype_link',val(t,'subtype'))+'|'+val(t,'subtype')+']]'
            card_label='[['+title+'|'+label+']]'
            if r['language']=='Japanese' and val(t,'printed_title'):card_label+='<br />'+clean(val(t,'printed_title'))
            game=val(t,'printed_game_text') or val(t,'game_text')
            assert game,(title,'No verified printed game text available')
            if val(t,'type')=='Location':
                if "'''Light Side:'''" not in game and "'''Dark Side:'''" not in game:
                    assert title=='Death Star (Japanese Reflections II Foil)'
                    game="'''Light Side:''' <br />'''Dark Side:''' "+game
                else:
                    if "'''Light Side:'''" not in game:game="'''Light Side:''' <br />"+game
                    if "'''Dark Side:'''" not in game:game+="<br />'''Dark Side:'''"
            fields=[image,card_label,r['language'],kind,val(t,'rarity'),val(t,'destiny'),clean(game)]
            foil+='|-\n'+('| '+' || '.join(fields)).rstrip()+'\n'
            inventory.append(dict(product=product,side=side,type=val(t,'type'),article=title,publication_id=val(t,'publication_id'),language=r['language'],alternate_image=r.get('alternate_image',False),image=val(t,'image'),image_available=available,source_revid=heads[title]['revisions'][0]['revid'],destiny=val(t,'destiny'),game_text_present=bool(game)))
        foil+='|}\n</div>\n\n'
    # Existing exclusive tables are whole-section moved, with only the heading changed.
    other=old[:match.start()]+old[match.end():];exclusive=''
    exclusive_match=re.search(r'^== (?:Card list|Exclusive cards) ==\n.*?(?=^== [^=]|\Z)',other,re.M|re.S)
    if exclusive_match:
        original=exclusive_match.group();exclusive=original.replace('== Card list ==','== Exclusive cards ==',1).rstrip()+'\n\n'
        other=other[:exclusive_match.start()]+other[exclusive_match.end():]
    insertion=match.start()-(len(original) if exclusive_match and exclusive_match.start()<match.start() else 0)
    new=other[:insertion]+exclusive+foil+other[insertion:]
    # Conservation proof removes only the specifically replaced/moved sections.
    new_other=new.replace(exclusive,'',1) if exclusive else new
    new_other=new_other.replace(foil,'',1)
    old_other=old.replace(oldfoil,'',1)
    if exclusive_match:old_other=old_other.replace(original,'',1)
    assert new_other==old_other,product
    assert len(rows)=={'Reflections':114,'Reflections II: Expanding the Galaxy':100,'Reflections III':100}[product]
    proof.append(dict(title=product,all_unrelated_content_exactly_conserved=True,exclusive_rows_preserved=True,exclusive_section_moved=bool(exclusive),foil_entries=len(rows),per_side=dict(collections.Counter(r['side'] for r in rows))))
    add(product,new,'Show actual Light/Dark foil cards below exclusive cards and invite scans (#430)')
    talk='Talk:'+product;oldtalk=source(heads[talk]) if 'revisions' in heads[talk] else ''
    note='\n\n== Foil tables and scan contributions ==\nRegular foil rows use their exact publication articles and existing images. Exclusive-card rows are retained above the foil lists. Missing images use the camera/text scan-request marker; existing photographs are not treated as absent scans. Printed card data and original image files are unchanged. ~~~~\n'
    if '== Foil tables and scan contributions ==' not in oldtalk:add(talk,oldtalk+note,'Record foil-table placement, source mappings and scan requests (#430)',True)
if '--check-idempotent' in sys.argv:
    for row in packet:assert row['text'].rstrip()==source(heads[row['title']]).rstrip(),(row['title'],'Rebuild would change current published data')
    (root/'idempotence-verification.json').write_text(json.dumps(dict(passed=True,rebuilt_current_pages=[r['title'] for r in packet],exact_rows=len(inventory),duplicate_talk_notes_prevented=True),indent=2),encoding='utf8')
    print('Fresh rebuild matches current set/template bytes;314 rows, no duplicated notes');raise SystemExit
for name,data in [('packet.json',packet),('inventory.json',inventory),('conservation.json',proof),('article-heads.json',heads),('image-heads.json',files)]:
    (root/name).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
for row in packet:(root/('draft-'+row['title'].replace(':','-').replace('/','-')+'.wiki')).write_text(row['text'],encoding='utf8')
print(len(inventory),'exact foil rows;',sum(not r['image_available'] for r in inventory),'missing images;',len(packet),'guarded pages; changed-content strict lint 0; prior Talk archive flags recorded')
