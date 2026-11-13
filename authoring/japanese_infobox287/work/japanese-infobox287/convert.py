import collections
import csv
import hashlib
import html
import json
from pathlib import Path
import re
import sys

root=Path(__file__).parent
sys.path[:0]=[str(root/'vendor'),'work/wiki-tools']
import mwparserfromhell as mw
from mwparserfromhell.nodes import Template
from style_lint import lint
heads=json.loads((root/'heads-before.json').read_bytes())
titles=json.loads((root/'targets.json').read_bytes())
summary=json.loads((root/'baseline-summary.json').read_bytes())
backlog={r['title']:r['flags'] for r in summary['lint']}

def plain(value):
    value=re.sub(r'<ref\b(?![^>]*?/\s*>)[^>]*>.*?</ref>|<ref[^>]*/>','',value,flags=re.S)
    return html.unescape(mw.parse(value).strip_code()).strip()
def classed(tag,klass):
    return str(tag.tag)=='div' and tag.has('class') and klass in str(tag.get('class').value).strip('"\'').split()
def firstlink(value):
    links=mw.parse(value).filter_wikilinks()
    return str(links[0].title).strip() if links else plain(value)
def split_sections(body):
    pat=r'<h2>\s*(.*?)\s*</h2>|(?m:^==\s*([^=\n]+?)\s*==\s*$)'
    matches=list(re.finditer(pat,body))
    lead=body[:matches[0].start()].strip() if matches else body.strip()
    sections={}
    for i,m in enumerate(matches):
        name=m[1] or m[2]
        assert name not in sections,name
        sections[name]=body[m.end():matches[i+1].start() if i+1<len(matches) else len(body)].strip()
    return lead,sections

mapping={
 'Destiny':'destiny','Power':'power','Ability':'ability','Deploy':'deploy','Forfeit':'forfeit','Armor':'armor','Maneuver':'maneuver',
 'Hyperspeed':'hyperspeed','Landspeed':'landspeed','Landspeed (rule-derived)':'landspeed','Parsec':'parsec','Ferocity':'ferocity',
 'Uniqueness':'uniqueness','Icons':'icons','Printed icons':'icons','Printed game icons':'icons','Printed symbols':'icons',
 'Versions':'versions','Printings':'versions','Publisher':'publisher','Era':'era','Edition':'edition','Release':'release',
 'Border / finish':'border_finish','Size':'size','Year':'year','Likeness':'likeness',
 'Dark icons':'dark_icons','Dark Force Icons':'dark_icons','Dark Side Force icons':'dark_icons','Dark Force':'dark_icons',
 'Light icons':'light_icons','Light Force Icons':'light_icons','Light Side Force icons':'light_icons','Light Force':'light_icons',
}
section_fields={'Notes':'notes','Sources':'sources','See Also':'see_also','See also':'see_also','Characteristics':'characteristics','Comparison with the English printing':'translation_note'}
drafts=[];details=[];unknown=collections.Counter();reference_repairs=[]
for title in titles:
    page=heads[title];rev=page['revisions'][0];old=rev['slots']['main']['content']
    working=old
    if '<ref name="photo" />' in working and not re.search(r'<ref name="photo"\s*>',working):
        filename=re.search(r'\[\[File:([^|\]]+)',working)[1]
        working=working.replace('<ref name="photo" />',f'<ref name="photo">[[:File:{filename}|Original Japanese printed face]].</ref>',1)
        reference_repairs.append(dict(title=title,source_file=filename,repair='define existing photo reference using the existing printing-specific File'))
    code=mw.parse(working)
    tables=[t for t in code.filter_tags() if str(t.tag)=='table' and t.has('class') and 'card-infobox' in str(t.get('class').value)]
    assert len(tables)==1,(title,len(tables))
    rawtable=str(tables[0]);cells=[]
    for m in re.finditer(r'<tr>\s*<th>(.*?)</th>\s*<td>(.*?)</td>\s*</tr>',rawtable,re.S):cells.append((plain(m[1]),m[2].strip()))
    assert cells,title
    stats=dict(cells)
    cats=[str(l.title).strip()[9:] for l in code.filter_wikilinks() if str(l.title).strip().startswith('Category:')]
    bodytags=[t for t in code.filter_tags() if classed(t,'card-body')]
    if bodytags:
        assert len(bodytags)==1,title
        body=str(bodytags[0].contents)
    else:
        body=working.replace(rawtable,'',1)
    navs=[t for t in code.filter_tags() if classed(t,'card-nav')]
    hats=[t for t in code.filter_tags() if classed(t,'card-hatnote')]
    portraits=[t for t in code.filter_tags() if classed(t,'card-portrait')]
    image='';image_note=''
    if portraits:
        portrait=str(portraits[0].contents)
        links=[l for l in mw.parse(portrait).filter_wikilinks() if str(l.title).startswith('File:')]
        if links:
            image=str(links[0].title)[5:]
            image_note=portrait.replace(str(links[0]),'',1).strip()
    else:
        image=''
    # Separate simple-layout Versions table, retaining its original content.
    version_tables=[t for t in mw.parse(body).filter_tags() if str(t.tag)=='table' and '! Versions' in str(t)]
    for v in version_tables:
        match=re.search(r'!\s*Versions\s*\n\|-\s*\n\|\s*(.*?)\n\|}',str(v),re.S)
        assert match,(title,str(v)[:100])
        if 'Versions' in stats:
            replacement='<table class="wikitable"><tr><th>Versions</th></tr><tr><td>'+match[1].strip()+'</td></tr></table>'
            body=body.replace(str(v),replacement,1)
            continue
        stats['Versions']=match[1].strip();cells.append(('Versions',match[1].strip()))
        body=body.replace(str(v),'',1)
    if not bodytags:
        for t in navs+hats+portraits:body=body.replace(str(t),'',1)
        body=body.replace('__NOTOC__','')
    body=re.sub(r'\[\[Category:[^\]]+\]\]','',body).strip()
    lead,sections=split_sections(body)
    is_ja='Japanese' in title
    english_title=stats.get('Title')
    if not english_title:
        match=re.search(r"'''(.*?)'''",lead,re.S)
        assert match,title
        english_title=match[1]
    params=collections.OrderedDict(title=english_title)
    params['side']=firstlink(stats['Side'])
    rawtype=stats.get('Type',stats.get('Card type',''))
    primary=re.match(r'(Epic Event|Defensive Shield|Jedi Test|Character|Device|Effect|Interrupt|Location|Starship|Vehicle|Weapon|Creature|Objective)\b',plain(rawtype))
    assert primary,(title,rawtype)
    params['type']=primary[1]
    params['type_display']=rawtype
    if 'Card type' in stats:params['label_type']='Card type'
    if 'Set' in stats and stats['Set'].startswith('[['):
        params['set']=firstlink(stats['Set'])
        params['set_display']=stats['Set']
    elif is_ja:
        candidates=[c for c in cats if 'Japanese' in c]
        assert len(candidates)==1,(title,candidates)
        params['set']=candidates[0]
    else:
        params['set']='Oversized cards'
        params['set_display']=stats['Set']
        params['category_override']=''.join('[[Category:'+c+']]' for c in cats)
    if is_ja:
        japanese_categories=[c for c in cats if 'Japanese' in c]
        if len(japanese_categories)==1:params['set']=japanese_categories[0]
    params['language']='ja' if is_ja else 'en'
    lang_label='Printed language' if 'Printed language' in stats else ('Language' if 'Language' in stats else None)
    if lang_label:
        params['language_display']=stats[lang_label]
        params['label_language']=lang_label
    if navs:params['navigation']=str(navs[0].contents).strip()
    if hats:params['hatnote']=str(hats[0].contents).strip().removeprefix("''").removesuffix("''")
    if image:params['image']=image
    if image_note:params['image_note']=image_note
    if lead:params['lead']=lead
    handled={'Title','Side','Type','Card type','Set','Printed language','Language'}
    ids=stats.get('Printing ID',stats.get('GEMP ID'))
    if ids:
        params['gemp_id']=re.sub(r'</?code>','',ids)
        params['label_gemp_id']='Printing ID' if 'Printing ID' in stats else 'GEMP ID'
        handled.update(['Printing ID','GEMP ID'])
    if 'Rarity' in stats:
        params['rarity']=plain(stats['Rarity'])
        params['rarity_display']=stats['Rarity']
        handled.add('Rarity')
    for label,value in cells:
        if label in mapping and mapping[label] not in params:
            key=mapping[label];params[key]=value;handled.add(label)
            if key in ['dark_icons','light_icons','icons','landspeed','versions']:
                params['label_'+key]=label
    extras=[(label,value) for label,value in cells if label not in handled]
    if extras:
        params['extra_info']='\n'.join('<tr><th>'+label+'</th><td>'+value+'</td></tr>' for label,value in extras)
        unknown.update(label for label,value in extras)
    for name,key in [('Title','printed_title'),('Card Text','printed_game_text' if is_ja else 'game_text'),('Lore','printed_lore' if is_ja else 'lore'),('Translation of Japanese Text','translation')]:
        if name in sections:
            value=sections.pop(name)
            if key=='lore' and value.startswith("''") and value.endswith("''"):value=value[2:-2]
            params[key]=value or '<nowiki />'
    for name,key in section_fields.items():
        if name in sections:
            params[key]=sections.pop(name) or '<nowiki />'
            if key=='see_also':params['see_also_heading']=name
    if 'References' in sections:
        assert '<references' in sections.pop('References'),title
        params['has_refs']='1'
    if sections:
        params['extra_sections']='\n'.join('<h2>'+name+'</h2>\n'+value for name,value in sections.items())
    auto={'Cards',params['set'],params['side'],params['type']}
    extra_cats=[c for c in cats if c not in auto] if 'category_override' not in params else []
    template=Template('Card\n')
    for key,value in params.items():template.add(key,value+'\n',showkey=True,preserve_spacing=False)
    new=str(template)+'\n'+''.join('[[Category:'+c+']]' for c in extra_cats)+'\n'
    parsed=mw.parse(new).filter_templates(recursive=False)
    assert len(parsed)==1 and str(parsed[0].name).strip()=='Card',title
    assert len(parsed[0].params)==len(params),title
    findings=lint(new,title)[0]
    assert set(findings)<=set(backlog.get(title,[])),(title,findings)
    drafts.append(dict(title=title,text=new,before_revid=rev['revid'],before_timestamp=rev['timestamp'],before_sha256=hashlib.sha256(old.encode()).hexdigest(),layout='simple' if 'Card type' in stats else 'template-look',set=params['set'],is_ja=is_ja,source_categories=cats))
    details.append(dict(title=title,params=params,source_sections=split_sections(body)[1],extra_info_labels=[x[0] for x in extras]))
(root/'drafts.json').write_text(json.dumps(drafts,ensure_ascii=False,indent=2),encoding='utf8')
(root/'conversion-details.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),encoding='utf8')
(root/'reference-repairs.json').write_text(json.dumps(reference_repairs,ensure_ascii=False,indent=2),encoding='utf8')
(root/'lint-backlog.csv').write_text('title,flags\n'+''.join('"'+r['title'].replace('"','""')+'","'+'; '.join(r['flags']).replace('"','""')+'"\n' for r in summary['lint']),encoding='utf8')
print(len(drafts),'converted drafts; extra fields retained:',dict(unknown))
