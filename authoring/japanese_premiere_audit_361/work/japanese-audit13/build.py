import difflib
import hashlib
import json
from pathlib import Path
import re
import sys

sys.path.insert(0, 'work/wiki-tools')
from style_lint import lint

root = Path('work/japanese-audit13')
live = json.loads((root / 'live.json').read_bytes())
census = json.loads((root / 'census.json').read_bytes())
readings = {r['number']: r for r in json.loads((root / 'readings.json').read_bytes())}

# Visual observations of the Japanese faces, not values copied from English.
# Pilot/Warrior repeated glyphs are retained (Tonnika Sisters).
groups = {
 'Droid': [1,5,6,18,24,25,32,163,175,186,188,192,193,197],
 'Rebel': [2,22,26], 'Rebel; Pilot; Warrior': [3,8,11,13,19,23,29],
 'Rebel; Warrior': [10,17,21,28], 'Rebel; Pilot': [27],
 'Alien': [7,9,12,14,16,20,31,33,177,182,183,184,187,191,198],
 'Alien; Pilot': [4,15], 'Alien; Warrior': [30,169,171,176,189,196],
 'Alien; Pilot; Warrior': [172,190], 'Alien; Warrior; Warrior': [195],
 'Imperial': [181], 'Imperial; Warrior': [166,170,178,194],
 'Imperial; Pilot': [165,180,185], 'Imperial; Pilot; Warrior': [164,167,168,173,174,179],
 'Starship; Pilot; Nav Computer; Scomp Link': [140,146,147,301,302],
 'Starship; Nav Computer; Scomp Link': [141,142,143,144,145],
 'Starship': [299,300], 'Starship; Pilot': [303,304],
 'Starship; Pilot; Nav Computer': [305], 'Starship; Nav Computer': [306],
 'Vehicle': [148,149,150,151,307,308,309,310],
}
icons = {n: value.split('; ') for value, numbers in groups.items() for n in numbers}
locations = {
 121:(0,0,2),122:(0,0,5),123:(1,0,None),124:(1,1,None),125:(0,0,None),126:(2,1,8),
 127:(1,2,7),128:(2,2,None),129:(1,1,None),130:(1,1,None),131:(1,1,None),132:(1,2,None),
 133:(1,2,None),134:(1,2,None),135:(1,2,4),136:(1,1,None),137:(0,1,None),138:(0,1,None),139:(0,2,None),
 281:(0,1,2),282:(1,1,5),283:(1,0,None),284:(1,0,None),285:(1,1,None),286:(1,0,None),287:(1,0,None),
 288:(2,1,8),289:(2,1,7),290:(2,2,None),291:(1,1,None),292:(1,1,None),293:(1,1,None),294:(2,1,None),
 295:(2,1,None),296:(2,1,4),297:(1,1,None),298:(1,1,None),
}
location_glyphs = {}
for n in locations:
    if locations[n][2] is not None:
        location_glyphs[n] = ['Planet']
    elif n in [123,125,283,284,286,287]:
        location_glyphs[n] = ['Interior Site','Mobile']
    elif n in [124,285]:
        location_glyphs[n] = ['Interior Site','Exterior Site','Mobile']
    elif n in [128,138,139,290]:
        location_glyphs[n] = ['Interior Site','Planet']
    elif n in [129,136,291,297]:
        location_glyphs[n] = ['Interior Site','Exterior Site','Planet']
    else:
        location_glyphs[n] = ['Exterior Site','Planet']
    if n in [123,124,129,132,136,139,283,285,286,287,291,294,297]:
        location_glyphs[n].append('Scomp Link')

def section(text, name, body):
    if '<h2>'+name+'</h2>' not in text:
        assert '<h2>References</h2>' in text
        return text.replace('<h2>References</h2>', '<h2>'+name+'</h2>\n'+body.rstrip()+'\n<h2>References</h2>',1)
    pattern = r'(<h2>' + re.escape(name) + r'</h2>\s*).*?(?=<h2>|</div>\s*\[\[Category:)'
    result, count = re.subn(pattern, lambda m: m[1] + body.rstrip() + '\n', text, flags=re.S)
    assert count == 1, name
    return result

def field(text, name, value):
    pattern = r'<tr><th>' + re.escape(name) + r'</th><td>.*?</td></tr>\s*'
    row = f'<tr><th>{name}</th><td>{value}</td></tr>\n' if value is not None else ''
    if re.search(pattern, text, re.S):
        return re.sub(pattern, lambda m: row, text, count=1, flags=re.S)
    assert value is not None
    return text.replace('</table>', row+'</table>', 1)

def link_translation(text):
    aliases = {'C-3PO':'C-3PO (See-Threepio)', 'R2-D2':'R2-D2 (Artoo-Detoo)'}
    names = ['Owen Lars','Beru Lars','Luke Skywalker','Obi-Wan Kenobi','Han Solo','CZ-3 (Seezee-Three)',
             'Hydroponics Station','Vaporator',"Lars' Moisture Farm",'Red Leader','Gold 5','Mantellian Savrip']
    aliases.update({name:name for name in names})
    pattern = '|'.join(re.escape(name) for name in sorted(aliases,key=len,reverse=True))
    return re.sub(r'(?<![\w\[])('+pattern+r')(?![\w\]])',lambda m:'[['+aliases[m[1]]+'|'+m[1]+']]',text)

payload, observations, diffs, deferred = [], [], [], []
for card in census:
    n, title = card['number'], card['title']
    revision = live[title]['revisions'][0]
    before = revision['slots']['main']['content']
    text = before
    file = card['files'][0]
    face_ref = '<ref name="jp-face" />'
    if not re.search(r'<ref name="jp-face"\s*>', text):
        face_ref = f'<ref name="jp-face">[[:File:{file}|Original Japanese printed face]].</ref>'
    changes = []
    if n in readings:
        reading = readings[n]
        text = re.sub(r"'''Incomplete documentation:'''[^\n]*\n", '', text)
        # An imported title's photograph reference was undefined on these pages.
        text = text.replace('<ref name="photograph" />', '')
        text = section(text, 'Card Text', f'<span lang="ja">{reading["game"]}</span>'+face_ref)
        text = section(text, 'Lore', f"''<span lang=\"ja\">{reading['lore']}</span>''"+'<ref name="jp-face" />')
        translation = "'''Title:''' " + card['stats']['Title'] + ".\n\n'''Card text:''' " + link_translation(reading['game_en']) + "\n\n'''Lore:''' " + link_translation(reading['lore_en'])
        text = section(text, 'Translation of Japanese Text', translation)
        for key, value in reading['stats'].items():
            text = field(text, key, value)
        if reading.get('comparison'):
            # Place the explanation outside the source transcription and translation.
            text = text.replace('<h2>References</h2>', '<h2>Notes</h2>\n'+reading['comparison']+'<ref name="jp-face" />\n<h2>References</h2>')
        changes.append('Japanese lore/game text and separate translations from face')
    if n in [49,53,63,69]:
        old_type = card['stats']['Type']
        new_type = '[[Effect]]' + (' ([[Utinni Effect]])' if n == 69 else '')
        text = text.replace(old_type,new_type)
        text = text.replace('[[Category:Character]]','[[Category:Effect]]').replace('[[Category:Creature]]','[[Category:Effect]]')
        changes.append('printed Effect classification')
    if n == 49:
        game = 'どちらかを選ぶ。１：ドロイドを除く、パイロットでないキャラクターに配備し、パイロット技能［パイロットアイコン］を与える。そのキャラクターが操縦する宇宙船の戦闘力は＋２される。２：パイロットに配備し、キャラクターが操縦する宇宙船の戦闘力にさらに＋１する。（「意識操作」の影響を受けない）'
        text = section(text,'Card Text','<span lang="ja">'+game+'</span>'+face_ref)
        changes.append('complete truncated Japanese game text, including inline Pilot symbol')
    if n in [12,182]:
        text = field(text,'Deploy','*')
        changes.append('printed variable deploy symbol')
    if n in [13,32,192,197]:
        subtype = 'Droid' if n in [32,192,197] else 'Rebel'
        text = field(text,'Type','[[Character]] ([['+subtype+']])')
        changes.append('printed character subtype')
    if n == 86:
        text = field(text,'Destiny','3'+face_ref)
        changes.append('destiny 3')
    if n in icons and not card['lint_flags']:
        value = ' '.join('[['+icon+']]' for icon in icons[n])
        # Do not assert absent lower-edge symbols on Lieutenant Tanbris's cropped image.
        if n not in [165,185]:
            text = field(text,'Icons',value+(face_ref if n not in readings else '<ref name="jp-face" />'))
            changes.append('visible printed symbols')
    if n in locations:
        dark, light, parsec = locations[n]
        for label in ['Destiny','Deploy']:
            if label in card['stats']:
                text = field(text,label,None)
        text = field(text,'Dark icons',str(dark))
        text = field(text,'Light icons',str(light))
        text = field(text,'Icons',' '.join('[['+icon+']]' for icon in location_glyphs[n])+face_ref)
        if parsec is not None:
            text = field(text,'Parsec',str(parsec))
        changes.append('face-counted Force icons and location symbols; printed parsec for systems; remove unprinted destiny/deploy defaults')
    if n in [122,127,298]:
        old_game = card['sections']['Card Text'].strip()
        if n == 122:
            old_game = "'''Light Side:''' " + old_game
            native = 'ここを支配していれば、フォース消耗が＋１される。'
            side = 'Dark Side'
            english = 'If you control here, Force drain +1.'
        elif n == 127:
            old_game = "'''Light Side:''' " + old_game
            native = 'タトゥイーンを占領している場合、ここにいる自分の宇宙船１隻につき、タトゥイーンの位置カード上での戦闘時で、合計戦力に＋１。'
            side = 'Dark Side'
            english = 'If you occupy Tatooine, total power in battles at Tatooine sites is +1 for each of your starships here.'
        else:
            native = 'ここを占領していれば、フォース消耗に＋１。'
            side = 'Light Side'
            english = 'If you occupy here, Force drain +1.'
        text = section(text, 'Card Text', old_game+'\n\n'+"'''"+side+":''' <span lang=\"ja\">"+native+'</span><ref name="jp-face" />')
        translated = card['sections']['Translation of Japanese Text'].rstrip()+'\n\n'+"'''"+side+" card text:''' "+english
        text = section(text, 'Translation of Japanese Text',translated)
        changes.append('previously omitted opposite-side Japanese location text and translation')
    if text != before:
        for source_name in ['photo','photograph']:
            if not re.search(r'<ref name="'+source_name+r'"\s*>',text):
                text = text.replace('<ref name="'+source_name+'" />','<ref name="jp-face" />')
        if '<ref name="jp-face" />' in text and not re.search(r'<ref name="jp-face"\s*>',text):
            text = text.replace('<ref name="jp-face" />',f'<ref name="jp-face">[[:File:{file}|Original Japanese printed face]].</ref>',1)
    flags = lint(text, title)[0]
    if text != before:
        if flags:
            deferred.append(dict(number=n,title=title,reason='Existing citation lint requires verified preservation before editing',flags=flags))
        else:
            payload.append(dict(number=n,title=title,text=text,before_text=before,before_revid=revision['revid'],before_sha256=hashlib.sha256(before.encode()).hexdigest(),summary='Complete face-verified Japanese Premiere text, icons and printed values (#361)',changes=changes))
            diffs.append(''.join(difflib.unified_diff(before.splitlines(True),text.splitlines(True),fromfile=title+' before',tofile=title+' after')))
    observations.append(dict(number=n,title=title,icons_observed=icons.get(n),location_observation=locations.get(n),location_glyphs=location_glyphs.get(n),source_file=file,changes=changes,published_candidate=any(p['number']==n for p in payload)))

assert len(payload) >= 60
set_page = json.loads((root/'set-head.json').read_bytes())['Premiere (Japanese)']
set_rev = set_page['revisions'][0]
set_before = set_rev['slots']['main']['content']
set_text = set_before
for card in payload:
    title, n = card['title'],card['number']
    pattern = r'(?m)^\| \[\[File:[^\n]+\|link='+re.escape(title)+r'\]\][^\n]*$'
    found = re.search(pattern,set_text)
    assert found,title
    cells=found[0].split(' || ')
    assert len(cells)==6,title
    if n in readings or n in [49,122,127,298]:
        native=re.search(r'<h2>Card Text</h2>\s*(.*?)(?=<h2>)',card['text'],re.S)[1].strip()
        cells[5]=re.sub(r'<ref\b[^>]*>.*?</ref>|<ref\b[^>]*/>','',native,flags=re.S).replace('\n',' ')
    if n in locations:
        cells[4]=str(locations[n][2]) if locations[n][2] is not None else '—'
    set_text=set_text[:found.start()]+' || '.join(cells)+set_text[found.end():]
# The two Location tables contain parsec, not destiny. Site faces have neither.
set_text=re.sub(r'(==== \[\[Location\]\] ====\n\{\|[^\n]+\n! Image !! Card !! Type !! Rarity !! )Destiny',r'\g<1>Parsec',set_text)
assert set_text.count('!! Parsec !! Game text')==2
assert not lint(set_text,'Premiere (Japanese)')[0]
payload.append(dict(title='Premiere (Japanese)',text=set_text,before_text=set_before,before_revid=set_rev['revid'],before_sha256=hashlib.sha256(set_before.encode()).hexdigest(),summary='Reconcile verified Japanese text and label location parsec values correctly (#361)',changes=['verified native text synchronized','location tables display parsec; no invented destiny']))
diffs.append(''.join(difflib.unified_diff(set_before.splitlines(True),set_text.splitlines(True),fromfile='Premiere (Japanese) before',tofile='Premiere (Japanese) after')))
(root/'payload.json').write_text(json.dumps(dict(rows=payload),ensure_ascii=False,indent=2),encoding='utf8')
(root/'observations.json').write_text(json.dumps(observations,ensure_ascii=False,indent=2),encoding='utf8')
(root/'deferred.json').write_text(json.dumps(deferred,ensure_ascii=False,indent=2),encoding='utf8')
(root/'changes.diff').write_text('\n'.join(diffs),encoding='utf8')
print(len(payload),'guarded drafts;',len(deferred),'deferred lint conflicts;',len(readings),'complete text readings')
