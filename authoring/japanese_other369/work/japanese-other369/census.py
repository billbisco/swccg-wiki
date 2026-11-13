import collections,csv,json,re,sys
from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).parent;root.mkdir(exist_ok=True)
base=root.parent/'japanese-infobox287'
sys.path.insert(0,str(base/'vendor'))
import mwparserfromhell as mw
heads=json.loads((root/'heads-before.json').read_bytes());targets=set(heads)
if (root/'checked-heads.json').exists():heads.update(json.loads((root/'checked-heads.json').read_bytes()))
records=[]
def plain(value):
    value=re.sub(r'<ref\b(?![^>]*?/\s*>)[^>]*>.*?</ref>|<ref[^>]*/>','',value,flags=re.S)
    return BeautifulSoup(mw.parse(value).strip_code(),'html.parser').get_text(' ',strip=True)
def missing(value):
    without_refs=re.sub(r'<ref\b(?![^>]*?/\s*>)[^>]*>.*?</ref>|<ref[^>]*/>','',value,flags=re.S).strip()
    return without_refs!='*' and (not plain(value).strip() or bool(re.search(r'not yet (?:transcribed|added|verified)|await(?:s|ing)? verification|not transcribed|untranscribed',plain(value),re.I)))
for title,page in heads.items():
    if title not in targets:continue
    text=page['revisions'][0]['slots']['main']['content'];template=next(t for t in mw.parse(text).filter_templates(recursive=False) if str(t.name).strip()=='Card')
    params={str(p.name).strip():str(p.value).strip() for p in template.params}
    images=[x for x in re.findall(r'\[\[File:([^|\]]+)',text) if not x.startswith('Icon-')]
    if params.get('image'):images.insert(0,params['image'])
    typ=params['type'];display=plain(params.get('type_display',''))
    fields=['printed_title','printed_game_text','translation']
    if typ not in ['Location','Epic Event']:fields.append('printed_lore')
    required=['dark_icons','light_icons'] if typ=='Location' else ['destiny']
    if typ=='Location' and 'System' in display:required+=['parsec']
    if typ in ['Character','Starship','Vehicle']:required+=['power','deploy','forfeit']
    if typ=='Creature':required+=['ferocity','deploy','forfeit']
    droid='Droid' in display or bool(re.search(r'<th>Subtype</th><td>.*?Droid',params.get('extra_info',''))) or bool(re.search(r'^(R[235]-|RA-7|FX-|EG-4|M-HYD|WED15|2-1B)',title))
    if typ=='Character' and not droid:required+=['ability']
    if typ=='Starship' and not re.search(r'^(Black 4|TIE )',title):required+=['hyperspeed']
    # Armor/maneuver applicability and printed icons need a face-level judgment.
    gaps=[k for k in fields+required if missing(params.get(k,''))]
    if not images:gaps.insert(0,'scan')
    records.append(dict(title=title,revid=page['revisions'][0]['revid'],set=params['set'],type=typ,images=list(dict.fromkeys(images)),gaps=gaps,uniqueness=params.get('uniqueness',''),icons=params.get('icons',''),params=params))
assert len(records)==469,len(records)
# Keep the input baseline immutable; updated output goes in census.json.
(root/'census.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf8')
with (root/'coverage.csv').open('w',encoding='utf8',newline='') as f:
    writer=csv.writer(f);writer.writerow(['title','set','type','image_count','gaps','uniqueness','icons'])
    writer.writerows([r['title'],r['set'],r['type'],len(r['images']),'; '.join(r['gaps']),r['uniqueness'],plain(r['icons'])] for r in records)
print('469 printings;',sum('scan' in r['gaps'] for r in records),'missing faces;',sum(bool(set(r['gaps'])-{'scan'}) for r in records),'pages with possible applicable-field gaps')
print('Gaps',dict(collections.Counter(k for r in records for k in r['gaps'])))
for row in records:
    if any(k in row['gaps'] for k in ['translation','printed_title','printed_game_text']):print(row['title'],row['gaps'],row['images'])
