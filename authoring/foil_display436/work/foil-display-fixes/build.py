import json,re,hashlib,sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests
sys.path.insert(0,'work/japanese-infobox287/vendor');import mwparserfromhell as mw
root=Path(__file__).parent
manifest=json.loads(Path('work/reflections-foils/manifest.json').read_bytes())
products=list(dict.fromkeys(r['product'] for r in manifest))
def fetch(ts):
    r=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join(ts),prop='revisions|flagged',rvprop='ids|timestamp|content',rvslots='main'),timeout=90);r.raise_for_status();j=r.json();assert 'error' not in j,j;return j['query']['pages']
titles=[r['proposed_article'] for r in manifest]+products+['Template:Card','Template:Card/doc','Template:Card photograph','Template:Card/foil-display-436']
heads={}
with ThreadPoolExecutor(max_workers=3) as pool:
    for batch in pool.map(fetch,[titles[i:i+30] for i in range(0,len(titles),30)]):heads.update({h['title']:h for h in batch})
(root/'before-heads.json').write_text(json.dumps(heads,ensure_ascii=False,indent=2),encoding='utf8')
def source(t):return heads[t]['revisions'][0]['slots']['main']['content']
packet=[]
def add(title,text):
    h=heads[title];row=dict(title=title,text=text,section=None,summary='Crop foil photographs for display, preserve originals and correct orientation (#436)')
    if 'revisions' in h:row.update(before_revid=h['revisions'][0]['revid'],before_sha256=hashlib.sha256(source(title).encode()).hexdigest())
    else:row['new']=True
    packet.append(row)
# All dimensions refer to original, EXIF-unrotated source pixels. Only presentation changes.
W='{{{crop_width}}}';H='{{{crop_height}}}';D='{{{width|280}}}'
den='{{#switch:{{{rotation|}}}|left|right='+H+'|#default='+W+'}}'
def scaled(v):return '{{#expr:('+v+')*'+D+'/('+den+')}}'
cw=scaled(W);ch=scaled(H);sw=scaled('{{{source_width}}}')
rot='{{#switch:{{{rotation|}}}|left=-90|right=90|180=180|#default=0}}'
left='{{#switch:{{{rotation|}}}|right='+ch+'|180='+cw+'|#default=0}}'
top='{{#switch:{{{rotation|}}}|left|180='+cw+'|#default=0}}'
# 180 top uses cropped height, unlike left.
top='{{#switch:{{{rotation|}}}|left='+cw+'|180='+ch+'|#default=0}}'
height='{{#switch:{{{rotation|}}}|left|right='+cw+'|#default='+ch+'}}'
helper='<includeonly><div class="card-photo" style="width:'+D+'px;max-width:100%;"><div class="card-photo-viewport" style="position:relative;width:'+D+'px;height:'+height+'px;overflow:hidden;"><div class="card-photo-crop" style="position:absolute;overflow:hidden;width:'+cw+'px;height:'+ch+'px;left:'+left+'px;top:'+top+'px;transform:rotate('+rot+'deg);transform-origin:0 0;{{#if:{{{polygon|}}}|clip-path:polygon({{{polygon}}});}}"><div class="card-photo-source" style="position:absolute;width:'+sw+'px;left:'+scaled('-{{{crop_x|0}}}')+'px;top:'+scaled('-{{{crop_y|0}}}')+'px;line-height:0;">[[File:{{{file}}}|{{#expr:ceil('+sw+')}}px|link={{{link|File:{{{file}}}}}}|alt={{{alt|Card photograph}}}]]</div></div></div><small>[[:File:{{{file}}}|Original photograph]]</small></div></includeonly><noinclude>Display-only framing of an unchanged source photograph. Parameters: file, source_width, crop_x, crop_y, crop_width, crop_height (original pixel coordinates), rotation (left, right, 180 or empty), width (default 280), link, alt, polygon (optional conservative CSS outline). The complete original remains linked. Do not use the frame to hide card borders, text or symbols. [[Category:Templates]]</noinclude>'
add('Template:Card photograph',helper)
old=source('Template:Card')
render='{{#ifeq:{{{image_rotation|}}}|left|<div class="card-image-rotation" style="position:relative;width:280px;height:{{{image_rotated_height|167}}}px;"><div style="position:absolute;left:0;top:{{{image_rotated_height|167}}}px;width:280px;transform:rotate(-90deg) scale({{#expr:{{{image_rotated_height|167}}}/280}});transform-origin:0 0;">[[File:{{{image}}}|280px]]</div></div>|[[File:{{{image}}}|280px]]}}'
new='{{#if:{{{image_crop_width|}}}|{{Card photograph|file={{{image}}}|source_width={{{image_source_width}}}|crop_x={{{image_crop_x|0}}}|crop_y={{{image_crop_y|0}}}|crop_width={{{image_crop_width}}}|crop_height={{{image_crop_height}}}|rotation={{{image_rotation|}}}|polygon={{{image_crop_polygon|}}}|width=280}}|'+render+'}}'
assert old.count(render)==3,old.count(render)
card=old.replace(render,new)
add('Template:Card/foil-display-436',card)
add('Template:Card',card)
doc=source('Template:Card/doc')+'\n\n=== Framing source photographs ===\nFor a photograph containing a grading holder, retain the original <code>image</code> filename and provide <code>image_source_width</code>, <code>image_crop_x</code>, <code>image_crop_y</code>, <code>image_crop_width</code> and <code>image_crop_height</code> in original source pixels. These optional fields frame the complete physical card for display without altering the uploaded source. <code>image_rotation</code> accepts <code>left</code>, <code>right</code> or <code>180</code> in this mode. An optional <code>image_crop_polygon</code> removes only background around a perspective photograph; preserve every card edge. The display includes an explicit link to the original photograph. Unframed photographs and secondary-image trim parameters keep their existing behavior.\n'
add('Template:Card/doc',doc)
measure={r['file']:r for r in json.loads((root/'framing-measurements.json').read_bytes())}
affected={};proof=[]
for r in manifest:
    title=r['proposed_article'];old=source(title);code=mw.parse(old);t=next(t for t in code.filter_templates(recursive=False) if str(t.name).strip()=='Card')
    file=str(t.get('image').value).strip();m=measure.get(file)
    if title=='Rebel Leadership (Reflections III Foil)':m=dict(source_width=640,source_height=480,x=0,y=0,w=640,h=480,file=file)
    if not m:continue
    rotation=str(t.get('image_rotation').value).strip() if t.has('image_rotation') else ''
    if title in ['Rebel Leadership (Reflections III Foil)','Coruscant: Jedi Council Chamber (Reflections III Foil)','Cloud City: Guest Quarters (Reflections Foil)',"Dagobah: Yoda's Hut (Reflections Foil)",'Death Star: Trench (Reflections Foil)']:rotation='right'
    if title=='Rendezvous Point (Reflections Foil)':rotation=''
    fields={'image_source_width':m['source_width'],'image_crop_x':m['x'],'image_crop_y':m['y'],'image_crop_width':m['w'],'image_crop_height':m['h']}
    if m.get('polygon'):fields['image_crop_polygon']=m['polygon']
    for key,value in fields.items():t.add(key,str(value)+'\n',before='image',preserve_spacing=False)
    for key in ['image_rotation','image_rotated_height']:
        if t.has(key):t.remove(key)
    if rotation:t.add('image_rotation',rotation+'\n',before='image',preserve_spacing=False)
    text=str(code);add(title,text);affected[title]=(file,m,rotation)
    # Round-trip proof: only allowlisted image fields change.
    restored=mw.parse(text);rt=next(t for t in restored.filter_templates(recursive=False) if str(t.name).strip()=='Card')
    original=mw.parse(old);ot=next(t for t in original.filter_templates(recursive=False) if str(t.name).strip()=='Card')
    allowed=set(fields)|{'image_rotation','image_rotated_height'}
    for tt in [rt,ot]:
        for key in allowed:
            if tt.has(key):tt.remove(key)
    assert str(restored)==str(original),title
    proof.append(dict(title=title,file=file,rotation=rotation,measurement=m))
assert len(affected)==216,len(affected)
for product in products:
    old=source(product);lines=old.splitlines(keepends=True);n=0
    for i,line in enumerate(lines):
        if not line.startswith('| '):continue
        for title,(file,m,rotation) in affected.items():
            if ' || [['+title+'|' not in line:continue
            assert line.count(' || ')>=6
            args=dict(file=file,source_width=m['source_width'],crop_x=m['x'],crop_y=m['y'],crop_width=m['w'],crop_height=m['h'],rotation=rotation,width=200,link=title,alt=title)
            if m.get('polygon'):args['polygon']=m['polygon']
            cell='{{Card photograph'+''.join('|'+k+'='+str(v) for k,v in args.items())+'}}'
            lines[i]='| '+cell+' || '+line.split(' || ',1)[1];n+=1;break
    assert n>0;new=''.join(lines)
    assert [x.split(' || ',1)[1] for x in old.splitlines() if ' || ' in x]==[x.split(' || ',1)[1] for x in new.splitlines() if ' || ' in x]
    add(product,new)
(root/'all-packet.json').write_text(json.dumps(packet,ensure_ascii=False,indent=2),encoding='utf8')
(root/'framing-proof.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2),encoding='utf8')
for stage,selected in [('helper',[r for r in packet if r['title'] in ['Template:Card photograph','Template:Card/foil-display-436']]),('main',[r for r in packet if r['title'] not in ['Template:Card photograph','Template:Card/foil-display-436']])]:
    (root/(stage+'-packet.json')).write_text(json.dumps(selected,ensure_ascii=False,indent=2),encoding='utf8')
print(len(packet),'pages;',len(affected),'display-only framed photographs; all other card/set fields conserved')
