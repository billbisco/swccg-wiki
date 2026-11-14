"""Reuse the existing foil; preserve its text, image and family links."""
import hashlib,json,sys
from pathlib import Path
sys.path.insert(0,'work/japanese-infobox287/vendor');import mwparserfromhell as mw
sys.path.insert(0,'work/wiki-tools');from style_lint import lint
root=Path(__file__).parent
head=json.loads((root/'existing-dont-get-cocky-head.json').read_bytes())
heads=json.loads((root/'existing-dont-get-cocky-audit-heads.json').read_bytes());rows=[]
def patch(h,text,summary,**extra):
    rev=h['revisions'][0];old=rev['slots']['main']['content']
    assert not lint(text,h['title'])[0],lint(text,h['title'])[0]
    rows.append(dict(title=h['title'],text=text,before_revid=rev['revid'],before_sha256=hashlib.sha256(old.encode()).hexdigest(),section=None,summary=summary,**extra))
old=head['revisions'][0]['slots']['main']['content'];code=mw.parse(old);card=code.filter_templates()[0]
for k,v in [('language','en'),('language_display','English'),('border_finish','Foil'),('release','January 2001')]:
    assert not card.has(k);card.add(k,v+'\n',before='publisher')
ref='<ref name="release">[https://res.starwarsccg.org/Resources/Star_Wars_CCG_Collecting_Encyclopedia_3.2.pdf SWCCG Collecting Encyclopedia 3.2], Reflections II product entry (collecting reference). Preserved copy: [https://web.archive.org/web/20261008192828/https://res.starwarsccg.org/Resources/Star_Wars_CCG_Collecting_Encyclopedia_3.2.pdf Internet Archive].</ref>'
card.get('lead').value=str(card.get('lead').value).rstrip()+' It was released in January 2001.'+ref+'\n'
patch(head,str(code),'Complete verified foil language, finish and release metadata without duplicating existing article (#381)')
h=heads['Reflections II: Expanding the Galaxy'];old=h['revisions'][0]['slots']['main']['content'];a=old.index('== Possible foils ==');b=old.index('\n== ',a+5);section=old[a:b]
assert section.count("[[Don't Get Cocky]]")==1
section=section.replace("[[Don't Get Cocky]]","[[Don't Get Cocky (Reflections II Foil)|Don't Get Cocky]]")
patch(h,old[:a]+section+old[b:],'Point the regular foil checklist directly to the existing foil article (#381)')
h=heads['Talk:'+head['title']];old=h['revisions'][0]['slots']['main']['content']
note='\n\n== Reflections inventory integration, 14 November 2026 ==\nThe existing foil is reused for story381 rather than duplicated. Both the current original photograph (PSA certificate 84897751) and the separately collected complete foil photograph show the same printed title, uniqueness, destiny, lore and game text. English language, foil finish and January 2001 release metadata were added; the Reflections II foil checklist now targets [[Don\'t Get Cocky (Reflections II Foil)]] directly. Existing reciprocal family links were retained. The exact public wiki-image version has yet to be captured; the source-photograph replay is not counted as a capture of the wiki-image URL.\n\n~~~~\n'
patch(h,old.rstrip()+note,'Record independent foil inventory reconciliation and wiki-image preservation work (#381)',signed_note=True)
(root/'existing-integration-packet.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
title='File:Reflections-II-L-Dont-Get-Cocky-Foil-PSA.jpg';info=heads[title]['imageinfo'][0];binary=(root/'existing-dont-get-cocky-original.jpg').read_bytes();sha=hashlib.sha256(binary).hexdigest();assert hashlib.sha1(binary).hexdigest()==info['sha1']
record=dict(url=info['url'],title=title,version=info['timestamp'],sha1=info['sha1'],mime=info['mime'],image_sha256=sha,verified=False,error='No Save Page Now request submitted: explicit service throttling already observed; exact version queued for later capture')
(root/'batch12-existing-image-captures.jsonl').write_text(json.dumps(record)+'\n',encoding='utf8')
uploaded=json.loads((root/'uploaded-images.json').read_bytes())
if not any(r['name']==title[5:] for r in uploaded):
    uploaded.append(dict(name=title[5:],local_file='existing-dont-get-cocky-original.jpg',sha256=sha,existing_asset=True))
    (root/'uploaded-images.json').write_text(json.dumps(uploaded,ensure_ascii=False,indent=2),encoding='utf8')
print('3 guarded integration edits; exact existing image hash verified, capture not asserted')
