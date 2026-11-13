from concurrent.futures import ThreadPoolExecutor
import collections,hashlib,json,re,sys
from pathlib import Path
import requests
root=Path(__file__).parent
sys.path[:0]=[str(root.parent/'japanese-infobox287'/'vendor'),'work/wiki-tools',str(root)]
import mwparserfromhell as mw
from style_lint import lint
import runpy
readings=runpy.run_path(str(root/'icon-readings.py'))['readings']
assert set(readings)==set(range(1,125))
uniques=json.loads((root/'uniqueness-manifest.json').read_bytes());icons=json.loads((root/'icon-inspection-manifest.json').read_bytes())
changes={};ledger=[]
for row in uniques:
    value='Restricted (3)' if row['number'] in [1,20] else 'Unrestricted'
    changes.setdefault(row['title'],{})['uniqueness']=value
    ledger.append(dict(title=row['title'],field='uniqueness',value=value,source_file=row['source_file'],photo_sha256=row['sha256'],inspection='All ten full-face sheets; complete title bar visible',source_number=row['number']))
legend={'P':'Pilot','W':'Warrior','N':'Nav Computer','S':'Scomp Link','D':'Droid'}
for row in icons:
    code=readings[row['icon_number']]
    value=' '.join('[['+legend[c]+']]' for c in code)
    if value:changes.setdefault(row['title'],{})['icons']=value
    ledger.append(dict(title=row['title'],field='icons',value=value or 'No lower-box gameplay icons',source_file=row['source_file'],photo_sha256=row['sha256'],inspection='Full face/type icon and enlarged lower corners, compared with established icon assets; ordinary faction symbols remain in Type',source_number=row['icon_number'],counts=dict(collections.Counter(legend[c] for c in code))))
for row in json.loads((root/'face-manifest.json').read_bytes()):
    if row['title'] in ['Death Star (Japanese)','Death Star (Japanese Reflections II Foil)']:
        changes.setdefault(row['title'],{})['icons']='[[Mobile]]'
        ledger.append(dict(title=row['title'],field='icons',value='[[Mobile]]',source_file=row['source_file'],photo_sha256=row['sha256'],inspection='Blue Mobile symbol matches Icon-mobile.png'))
photo=json.loads((root/'preservation.json').read_bytes())
changes.setdefault('2-1B (Too-Onebee) (Japanese)',{})['icons']='[[Droid]]'
ledger.append(dict(title='2-1B (Too-Onebee) (Japanese)',field='icons',value='[[Droid]]',source_file='File:Japanese-Hoth-2-1B-PSA-175224368.jpg',photo_sha256=photo['image_sha256'],inspection='Printed gold Droid type symbol matches the established icon'))
for title,label,native,value in [('Dianoga (Japanese)','Slither','粘り','5'),('Wampa (Japanese)','Vicious howl','血も凍る叫び声','3')]:
    changes.setdefault(title,{})['_creature_defense']=(label,native,value)
    row=next(r for r in uniques if r['title']==title)
    ledger.append(dict(title=title,field='creature statistics',value='Ferocity *; '+label+' '+value,source_file=row['source_file'],photo_sha256=row['sha256'],inspection='Japanese printed labels and numbers; English original face used only for established label naming'))
titles=sorted(changes)
def fetch(batch):
    response=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join(batch),prop='revisions',rvprop='ids|timestamp|content',rvslots='main'),timeout=60)
    response.raise_for_status();j=response.json();assert 'error' not in j,j;return j['query']['pages']
heads={}
with ThreadPoolExecutor(max_workers=3) as pool:
    for batch in pool.map(fetch,[titles[i:i+30] for i in range(0,len(titles),30)]):heads.update({p['title']:p for p in batch})
(root/'phase2-heads.json').write_text(json.dumps(heads,ensure_ascii=False,indent=2),encoding='utf8')
rows=[];skipped=[]
for title,fields in changes.items():
    rev=heads[title]['revisions'][0];old=rev['slots']['main']['content'];code=mw.parse(old)
    template=next(t for t in code.filter_templates(recursive=False) if str(t.name).strip()=='Card')
    source=next(r['source_file'] for r in ledger if r['title']==title)
    # Reuse the page's existing named photo reference where possible.
    refs=re.findall(r'<ref\s+name="([^"]+)"[^>]*>(.*?)</ref>',old,re.S)
    refname=next((name for name,body in refs if source[5:] in body),None)
    ref='<ref name="'+refname+'" />' if refname else '<ref name="printed-fields-369">[[:'+source+'|Original Japanese printed face]].</ref>'
    for field,value in fields.items():
        if field.startswith('_'):continue
        if template.has(field) and str(template.get(field).value).strip():
            skipped.append(dict(title=title,field=field,reason='Concurrent/editor value already present; preserved'))
            continue
        template.add(field,value+ref+'\n',preserve_spacing=False)
        if not refname:ref='<ref name="printed-fields-369" />'
    if '_creature_defense' in fields:
        label,native,value=fields['_creature_defense']
        assert str(template.get('power').value).strip()=='*' and str(template.get('ferocity').value).strip()=='*',title
        template.remove('power')
        extra=str(template.get('extra_info').value).strip() if template.has('extra_info') else ''
        template.add('extra_info',extra+'\n<tr><th>'+label+' (<span lang="ja">'+native+'</span>)</th><td>'+value+ref+'</td></tr>\n',preserve_spacing=False)
    new=str(code)
    if new==old:continue
    assert not lint(new,title)[0],(title,lint(new,title))
    rows.append(dict(title=title,text=new,before_revid=rev['revid'],before_sha256=hashlib.sha256(old.encode()).hexdigest(),section=0,summary='Fill verified printed uniqueness/gameplay icons; retain Japanese printing differences (#369)'))
(root/'phase2-packet.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
(root/'field-readings.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2),encoding='utf8')
(root/'phase2-skipped.json').write_text(json.dumps(skipped,ensure_ascii=False,indent=2),encoding='utf8')
print(len(rows),'lint-clean guarded drafts;',len(uniques),'uniqueness readings;',sum(bool(x) for x in readings.values()),'printed gameplay-icon readings;',sum(not x for x in readings.values()),'confirmed no gameplay icon; concurrent fields preserved:',len(skipped))
