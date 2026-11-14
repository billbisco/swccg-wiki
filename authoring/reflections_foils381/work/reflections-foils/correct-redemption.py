import hashlib,json,sys
from pathlib import Path
import requests
sys.path.insert(0,'work/japanese-infobox287/vendor');import mwparserfromhell as mw
sys.path.insert(0,'work/wiki-tools');from style_lint import lint
root=Path(__file__).parent;preserved=json.loads((root/'batch7check-preservation.json').read_bytes());assert preserved['verified']
title='Redemption (Reflections Foil)'
response=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles=title,prop='revisions',rvprop='ids|content',rvslots='main'),timeout=60);response.raise_for_status();rev=response.json()['query']['pages'][0]['revisions'][0];old=rev['slots']['main']['content'];assert 'have been. modified' in old
code=mw.parse(old);card=next(t for t in code.filter_templates(recursive=False) if str(t.name).strip()=='Card');card.get('lore').value=str(card.get('lore').value).replace('have been. modified','have been modified')
source='* Original physical foil photograph, Duncan Jenkins collection, Star Wars Collectors Archive.<ref name="foil-lore-check">[https://theswca.com/index.php?action=disp_item&item_id=45052 Redemption foil], Duncan Jenkins collection. Preserved copy: ['+preserved['capture']+' Internet Archive unchanged original photograph].</ref>'
card.get('sources').value=str(card.get('sources').value).rstrip()+'\n'+source+'\n';text=str(code);assert not lint(text,title)[0],lint(text,title)[0]
row=dict(title=title,text=text,before_revid=rev['revid'],before_sha256=hashlib.sha256(old.encode()).hexdigest(),section=0,summary='Resolve a photographic mark using a second complete foil face; correct lore punctuation (#381)')
(root/'batch7-correction-packet.json').write_text(json.dumps([row],ensure_ascii=False,indent=2),encoding='utf8')
rows=json.loads((root/'batch7-readings.json').read_bytes());r=next(r for r in rows if r['title']=='Redemption');r['lore']=r['lore'].replace('have been. modified','have been modified');r['reading_note']='A second full physical foil, SWCA item 45052, confirms “have been modified”; the punctuation-sized mark in the PSA image is not retained. Original photos are unchanged and both sources preserved.';r['supporting_source']=dict(url='https://theswca.com/index.php?action=disp_item&item_id=45052',capture=preserved['capture'],image_sha256='7c2ec97f3bebc5d2f936f5169fcec44e2082d6322cfbab35b78da149d5c682ac')
(root/'batch7-readings.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
note='A punctuation-sized mark after “been” in the PSA photograph was initially transcribed as a period. A [https://theswca.com/index.php?action=disp_item&item_id=45052 second complete physical foil photograph] confirms “have been modified”; the lore transcription has been corrected. Preserved copy: ['+preserved['capture']+' Internet Archive unchanged original photograph]. Both original photographs remain unchanged. ~~~~'
(root/'batch7-reading-note-packet.json').write_text(json.dumps([dict(title='Talk:'+title,text=note,section='new',sectiontitle='Physical-face reading correction',section_text=note,signed_note=True,summary='Document the targeted second-source punctuation correction (#381)')],ensure_ascii=False,indent=2),encoding='utf8')
print('Guarded lore correction and documented second-source evidence prepared')
