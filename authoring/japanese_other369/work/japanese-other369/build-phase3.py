import hashlib,json,re,sys
from pathlib import Path
import requests
root=Path(__file__).parent
sys.path[:0]=[str(root.parent/'japanese-infobox287'/'vendor'),'work/wiki-tools']
import mwparserfromhell as mw
from style_lint import lint
readings=json.loads((root/'phase3-readings.json').read_bytes());photos={r['number']:r for r in json.loads((root/'recovered-face-manifest.json').read_bytes())}
files={r['card_title']:r for r in json.loads((root/'recovered-files-payload.json').read_bytes())}
# Candidate 6 was mislabeled by PSA: it is I'm On The Leader, whose article is already complete.
readings=[r for r in readings if r['n']!=6]
titles=[photos[r['n']]['title'] for r in readings]
def api(**kwargs):
    response=requests.get('https://wiki.swccg.com/api.php',params=dict(format='json',formatversion=2,**kwargs),timeout=60);response.raise_for_status();j=response.json();assert 'error' not in j,j;return j
heads={p['title']:p for p in api(action='query',titles='|'.join(titles),prop='revisions',rvprop='ids|timestamp|content',rvslots='main')['query']['pages']}
(root/'phase3-heads.json').write_text(json.dumps(heads,ensure_ascii=False,indent=2),encoding='utf8')
rows=[];by_title={}
for data in readings:
    title=photos[data['n']]['title'];by_title[title]=data;f=files[title];page=heads[title];rev=page['revisions'][0];old=rev['slots']['main']['content'];code=mw.parse(old)
    template=next(t for t in code.filter_templates(recursive=False) if str(t.name).strip()=='Card')
    ref='<ref name="jp-face-369">[[:'+f['title']+'|Original Japanese printed face]].</ref>'
    repeat='<ref name="jp-face-369" />'
    def add(key,value):template.add(key,value+'\n',preserve_spacing=False)
    english=title.removesuffix(' (Japanese)');add('title',english);add('image',f['name'])
    add('printed_title','<span lang="ja">'+data['title']+'</span>'+ref)
    if 'light_text' in data:
        add('type_display','[[Location]] ([[Site]])')
        add('printed_game_text',"'''Light Side:''' <span lang=\"ja\">"+data['light_text']+"</span>\n\n'''Dark Side:''' <span lang=\"ja\">"+data['dark_text']+'</span>'+repeat)
        translation="'''Title:''' "+data['translated_title']+"\n\n'''Light Side:''' "+data['translated_light']+"\n\n'''Dark Side:''' "+data['translated_dark']
        if template.has('printed_lore'):
            assert 'not yet transcribed' in str(template.get('printed_lore').value),title
            template.remove('printed_lore')
    else:
        add('type_display','[[Character]] ([[Droid]])')
        add('printed_game_text','<span lang="ja">'+data['game']+'</span>'+repeat)
        add('printed_lore',"''<span lang=\"ja\">"+data['lore']+"</span>''"+repeat)
        translation="'''Title:''' "+data['translated_title']+"\n\n'''Subtype:''' "+data['translated_subtype']+"\n\n'''Card text:''' "+data['translated_game']+"\n\n'''Lore:''' "+data['translated_lore']
        extra=str(template.get('extra_info').value).strip() if template.has('extra_info') else ''
        add('extra_info',extra+'\n<tr><th>Printed subtype</th><td><span lang="ja">'+data['subtype']+'</span>'+repeat+'</td></tr>\n<tr><th>Subtype</th><td>[[Droid]]</td></tr>')
    add('translation',translation)
    if data.get('translation_note'):add('translation_note',data['translation_note']+repeat)
    for field in ['destiny','power','deploy','forfeit','uniqueness','dark_icons','light_icons','icons']:
        if field in data:add(field,data[field]+repeat)
    for field in ['image_rotation','image_rotated_height']:
        if field in data:add(field,data[field])
    if template.has('image_note'):
        assert 'not yet available' in str(template.get('image_note').value),title
        template.remove('image_note')
    lead=str(template.get('lead').value).replace("'''"+title+"'''","'''"+english+"'''")
    lead=lead.replace("'''Incomplete article.''' The original Japanese card image has not yet been added here.",'').rstrip()
    add('lead',lead)
    if template.has('extra_sections'):
        assert str(template.get('extra_sections').value).strip()=='<h2>Statistics</h2>\nPrinted statistics, subtype, symbols and uniqueness markers: not yet transcribed.',title
        template.remove('extra_sections')
    new=str(code);assert not lint(new,title)[0],(title,lint(new,title))
    rows.append(dict(title=title,text=new,before_revid=rev['revid'],before_sha256=hashlib.sha256(old.encode()).hexdigest(),section=0,summary='Complete the original Japanese face, native text, translation and printed stats (#369)'))
sets=json.loads((root/'phase3-set-heads.json').read_bytes())
for title,page in sets.items():
    rev=page['revisions'][0];old=rev['slots']['main']['content'];new=old
    for card,data in by_title.items():
        if (title.startswith('Hoth'))!=(data['n'] in [1,2,3,4,5]):continue
        f=files[card];lines=[line for line in new.splitlines(True) if line.startswith('|') and '||' in line and ('[['+card+'|') in line]
        assert len(lines)==1,(title,card,lines)
        line=lines[0]
        if data.get('image_rotation'):
            thumb='<span style="display:inline-block;position:relative;width:37px;height:22px;vertical-align:middle;"><span style="position:absolute;left:0;top:22px;transform:rotate(-90deg);transform-origin:0 0;">[[File:'+f['name']+'|22px|link='+card+'|alt=Japanese '+card.removesuffix(' (Japanese)')+']]</span></span>'
        else:thumb='[[File:'+f['name']+'|36px|link='+card+'|alt=Japanese '+card.removesuffix(' (Japanese)')+']]'
        if title.startswith('Hoth'):
            updated=line.replace('[['+card+'|',thumb+' [['+card+'|',1)
        else:
            assert line.split('||',1)[0].strip()=='|',line
            updated='| '+thumb+' ||'+line.split('||',1)[1]
            assert not updated.rstrip().split('||')[-1].strip(),line
            updated=updated.rstrip()+' <span lang="ja">'+data['game']+'</span><ref name="photo-'+photos[data['n']]['uid']+'">[[:'+f['title']+'|Original Japanese printed face]].</ref>\n'
        new=new.replace(line,updated,1)
    assert new!=old,title
    sections=api(action='parse',page=title,prop='sections')['parse']['sections'];index=next(s['index'] for s in sections if s['line']=='Card list')
    section=api(action='query',titles=title,prop='revisions',rvprop='content',rvslots='main',rvsection=index)['query']['pages'][0]['revisions'][0]['slots']['main']['content']
    assert old.count(section)==1,title
    start=old.index(section);replacement=new[start:len(new)-(len(old)-start-len(section))] if len(old)>start+len(section) else new[start:]
    assert new==old[:start]+replacement+old[start+len(section):],title
    assert not lint(new,title)[0],(title,lint(new,title))
    rows.append(dict(title=title,text=new,section=index,section_text=replacement,before_revid=rev['revid'],before_sha256=hashlib.sha256(old.encode()).hexdigest(),summary='Link verified original Japanese faces and fill their checklist data (#369)'))
(root/'phase3-packet.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print(len(rows),'guarded card/set drafts; rejected Evader candidate excluded; lint 0')
