import hashlib,json,re,sys
from pathlib import Path
import requests
sys.path.insert(0,'work/wiki-tools');from style_lint import lint
root=Path(__file__).parent
response=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='Reflections',prop='revisions',rvprop='ids|timestamp|content',rvslots='main'),timeout=60);response.raise_for_status()
page=response.json()['query']['pages'][0];rev=page['revisions'][0];old=rev['slots']['main']['content']
start=old.index('== Possible foils ==');end=old.index('\n== ',start+5);section=old[start:end]
for r in json.loads((root/'first-readings.json').read_bytes()):
    needle='[['+r['printed_title']+']]';assert section.count(needle)==1,(r['title'],section.count(needle))
    section=section.replace(needle,'[['+r['article']+'|'+r['printed_title']+']]')
new=old[:start]+section+old[end:]
encyc='https://res.starwarsccg.org/Resources/Star_Wars_CCG_Collecting_Encyclopedia_3.2.pdf'
needle='<ref name="encyc">['+encyc+' SWCCG Collecting Encyclopedia 3.2]</ref>';assert new.count(needle)==1
new=new.replace(needle,'<ref name="encyc">['+encyc+' SWCCG Collecting Encyclopedia 3.2]. Preserved copy: [https://web.archive.org/web/20261008192828/'+encyc+' Internet Archive].</ref>')
needle='* [https://www.starwarsccg.org/collecting/ SWCCG Collecting Encyclopedia] at starwarsccg.org';assert new.count(needle)==1
new=new.replace(needle,needle+'. Preserved copy: [https://web.archive.org/web/20261027044807/https://swccg.com/snapshots/pc/collecting.html Internet Archive].')
assert not lint(new,'Reflections')[0],lint(new,'Reflections')[0]
(root/'first-set-heads.json').write_text(json.dumps({'Reflections':page},ensure_ascii=False,indent=2),encoding='utf8')
packet=[dict(title='Reflections',text=new,before_revid=rev['revid'],before_sha256=hashlib.sha256(old.encode()).hexdigest(),section=None,summary='Link ten verified foil articles directly and preserve existing source citations (#381)',atomic_reason='Coordinated checklist and two inherited citation repairs in separate sections; exact whole-source revision/hash guard protects all other text')]
(root/'first-set-packet.json').write_text(json.dumps(packet,ensure_ascii=False,indent=2),encoding='utf8')
print('Ten direct foil links; all other checklist entries conserved; set source lint 0')
