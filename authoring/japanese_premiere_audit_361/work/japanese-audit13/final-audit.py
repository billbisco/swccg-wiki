import collections
import csv
import html
import json
from pathlib import Path
import re
from urllib.parse import quote

from bs4 import BeautifulSoup

root=Path('work/japanese-audit13')
heads=json.loads((root/'checked-heads.json').read_bytes())
old=json.loads((root/'census.json').read_bytes())
images={r['number']:r for r in json.loads((root/'images.json').read_bytes())}
payload={r['title']:r for r in json.loads((root/'payload.json').read_bytes())['rows']}
readings={r['number'] for r in json.loads((root/'readings.json').read_bytes())}
observed={r['number']:r for r in json.loads((root/'observations.json').read_bytes())}
def plain(text):
    text=re.sub(r'<ref\b(?![^>]*?/\s*>)[^>]*>.*?</ref>|<ref[^>]*/>','',text,flags=re.S)
    return BeautifulSoup(text,'html.parser').get_text(' ',strip=True).replace("'''",'').strip()
def split(text):
    text=re.sub(r'<h2>(.*?)</h2>',r'== \1 ==',text)
    parts=re.split(r'(?m)^==\s*(.*?)\s*==\s*\n',text)
    return dict(zip(parts[1::2],parts[2::2]))
manifest=[]
for card in old:
    n,title=card['number'],card['title']
    rev=heads[title]['revisions'][0]
    text=rev['slots']['main']['content']
    sections=split(text)
    stats={name:plain(value) for name,value in re.findall(r'<tr><th>(.*?)</th><td>(.*?)</td></tr>',text,re.S)}
    kind=stats.get('Type',stats.get('Card type',''))
    primary=re.search(r'\[\[([^]|]+)',kind)
    primary=primary[1] if primary else kind.split(' (',1)[0]
    applicable=['Destiny']
    if primary=='Location':
        applicable=['Dark icons','Light icons','Icons']
        if 'System' in kind:applicable.append('Parsec')
    elif primary in ['Character','Starship','Vehicle']:
        applicable+=['Power','Deploy','Forfeit','Icons']
        if 'Character' in kind and 'Droid' not in kind:applicable+=['Ability']
        if 'Starship' in kind and 'Capital' in kind:applicable+=['Armor','Hyperspeed']
        if 'Starship' in kind and 'Starfighter' in kind:applicable+=['Maneuver','Hyperspeed']
        if 'Vehicle' in kind:applicable+=['Landspeed']
    fields={}
    for name in ['Title','Card Text','Lore','Translation of Japanese Text']:
        value=plain(sections.get(name,''))
        absent=not value or bool(re.search(r'not yet|not been transcribed|awaits verification|untranscribed',value,re.I))
        status='missing' if absent else 'present; existing transcription not independently rechecked'
        if name=='Lore' and 'Location' in kind:status='intentionally unprinted'
        elif n in readings:status='face-verified in #361'
        elif n==49 and name=='Card Text':status='face-verified completed truncation in #361'
        elif n in [122,127,298] and name in ['Card Text','Translation of Japanese Text']:status='previous text retained; omitted opposite-side block face-verified in #361'
        fields[name]=status
    translation=plain(sections.get('Translation of Japanese Text',''))
    translation_parts={label:bool(re.search(pattern,translation,re.I)) for label,pattern in [('title',r'(title|name)[:：]'),('game_text',r'(card text|game text|light side|dark side)[:：]'),('lore',r'lore[:：]')]}
    if primary=='Location':translation_parts['lore']='intentionally unprinted'
    missing=[name for name in applicable if not stats.get(name)]
    file=re.search(r'\[\[File:([^|\]]+)',text)[1]
    edge='not independently assessed across the entire face'
    if n in readings or n in [49,53,63,69,86] or n in [25,185]:edge='full printed area visually inspected in #361'
    elif observed[n]['location_observation']:edge='both side bars and symbols visually inspected in #361'
    elif observed[n]['icons_observed']:edge='visible printed symbols inspected; full edge completeness not certified'
    if n==165:edge='lower edge cropped; Imperial/Pilot visible; any additional lower symbol remains unresolved'
    current_image=images[n]
    if n in [25,185]:
        receipt=next(r for r in map(json.loads,(root/'upload-receipts.jsonl').read_text().splitlines()) if f'-{n}o-' in r['title'])
        current_image=dict(file=file,url=receipt['image_url'],sha256=receipt['image_sha256'],size=[480,640])
    manifest.append(dict(number=n,title=title,url='https://wiki.swccg.com/wiki/'+quote(title.replace(' ','_'),safe="():,'"),printing_id=f'1301_{n}o',revid=rev['revid'],source_file=file,initial_image=images[n],current_image=current_image,current_stats=stats,applicable_fields=applicable,missing_applicable_stats=missing,text_coverage=fields,translation_components=translation_parts,scan_presence='verified existing wiki file bytes downloaded',edge_status=edge,video_image_candidate='video' in file.lower(),template='manual card-infobox',type_subtype_verification='existing type/subtype retained unless listed as a #361 correction; no comprehensive subtype rereading claimed',changed_in_361=title in payload))
assert len(manifest)==324 and len({r['printing_id'] for r in manifest})==324
(root/'final-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
gaps=[dict(number=r['number'],title=r['title'],missing_stats=r['missing_applicable_stats'],missing_text=[name for name,state in r['text_coverage'].items() if state=='missing'],missing_translation_components=[key for key,state in r['translation_components'].items() if state is False]) for r in manifest if r['missing_applicable_stats'] or 'missing' in r['text_coverage'].values() or False in r['translation_components'].values()]
(root/'remaining-field-gaps.json').write_text(json.dumps(gaps,ensure_ascii=False,indent=2),encoding='utf8')
with (root/'coverage.csv').open('w',encoding='utf8',newline='') as f:
    columns=['number','title','printing_id','revid','source_file','scan_presence','edge_status','video_image_candidate','changed_in_361']
    writer=csv.DictWriter(f,fieldnames=columns,extrasaction='ignore');writer.writeheader();writer.writerows(manifest)
rows=['# Remaining evidence limits','#361 audits field coverage and repairs verified omissions; it does not certify a new full linguistic proofreading of all 324 existing transcriptions.','',f"{sum(r['video_image_candidate'] for r in manifest)} current images have video-derived filenames. This is a candidate list, not a count of proven incomplete faces. Original crops remain preserved when a better photo replaces them.",'','## Exact field gaps',json.dumps(gaps,ensure_ascii=False,indent=2),'','## Specifically unresolved edge','- [Chief Bast](https://wiki.swccg.com/wiki/Chief_Bast_(Japanese)): Imperial and Pilot are visible; the lower edge is cropped. No absent additional symbol is inferred.','','## Video-image candidates for full-face inspection or replacement','']
rows.extend(f"- [{r['title']}]({r['url']}) — {r['edge_status']}" for r in manifest if r['video_image_candidate'])
(root/'remaining-evidence.md').write_text('\n'.join(rows)+'\n',encoding='utf8')
print('324 printing records;',len(gaps),'remaining presence/applicable-stat gaps;',sum(r['video_image_candidate'] for r in manifest),'video-image candidates;',sum(r['changed_in_361'] for r in manifest),'card articles changed')
for gap in gaps:print(gap)
