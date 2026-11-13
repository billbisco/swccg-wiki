import hashlib,json
from pathlib import Path
import requests
root=Path(__file__).parent
r=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='Template:Card|Template:Card/sandbox|Template:Card/doc',prop='revisions',rvprop='ids|timestamp|content',rvslots='main'),timeout=60);r.raise_for_status();heads={p['title']:p for p in r.json()['query']['pages']}
if (root/'rotation-heads.json').exists() and not (root/'rotation-heads-first.json').exists():(root/'rotation-heads-first.json').write_bytes((root/'rotation-heads.json').read_bytes())
(root/'rotation-heads.json').write_text(json.dumps(heads,ensure_ascii=False,indent=2),encoding='utf8')
old=heads['Template:Card']['revisions'][0]['slots']['main']['content']
needle='[[File:{{{image}}}|280px]]';assert old.count(needle)==3,old.count(needle)
height='{{{image_rotated_height|167}}}'
rotated='<div class="card-image-rotation" style="position:relative;width:280px;height:'+height+'px;"><div style="position:absolute;left:0;top:'+height+'px;width:280px;transform:rotate(-90deg) scale({{#expr:'+height+'/280}});transform-origin:0 0;">[[File:{{{image}}}|280px]]</div></div>'
new=old.replace(needle,'{{#ifeq:{{{image_rotation|}}}|left|'+rotated+'|'+needle+'}}')
(root/'template-rotation.wiki').write_text(new,encoding='utf8')
rows=[]
for title in ['Template:Card/sandbox','Template:Card']:
    rev=heads[title]['revisions'][0]
    rows.append(dict(title=title,text=new,before_revid=rev['revid'],before_sha256=hashlib.sha256(rev['slots']['main']['content'].encode()).hexdigest(),section=0,summary='Support display-only upright orientation for original sideways card photos (#369)'))
(root/'rotation-sandbox-packet.json').write_text(json.dumps(rows[:1],ensure_ascii=False,indent=2),encoding='utf8')
(root/'rotation-production-packet.json').write_text(json.dumps(rows[1:],ensure_ascii=False,indent=2),encoding='utf8')
doc="Optional '''image_rotation''' — <code>left</code> displays the first portrait a quarter turn counterclockwise. Use it for an original source photograph whose card is sideways. The original File and downloaded photograph stay unchanged. Omit it for an upright photo. '''image_rotated_height''' is the displayed height in pixels after rotation; use the nearest integer to <code>280 × original image width / original image height</code> (default 167). The template scales the standard thumbnail inside its 280px rail. Works with the first portrait in stacked and two-column layouts. Do not use rotation to infer a different printing or to hide a cropped card edge."
page=heads['Template:Card/doc'];rev=page['revisions'][0];old_doc=rev['slots']['main']['content']
docrow=dict(title=page['title'],text=old_doc.rstrip()+'\n\n== Source-photo orientation ==\n\n'+doc,before_revid=rev['revid'],before_sha256=hashlib.sha256(old_doc.encode()).hexdigest(),section='new',sectiontitle='Source-photo orientation',section_text=doc,summary='Document display-only orientation for unaltered source photographs (#369)')
(root/'rotation-doc-packet.json').write_text(json.dumps([docrow],ensure_ascii=False,indent=2),encoding='utf8')
print('Optional display-only left rotation; all three default image branches retained verbatim')
