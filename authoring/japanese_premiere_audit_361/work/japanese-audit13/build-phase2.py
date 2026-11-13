import difflib
import hashlib
import json
from pathlib import Path
import re
import sys

sys.path.insert(0,'work')
from audit_wiki_card_titles import pages
sys.path.insert(0,'work/wiki-tools')
from style_lint import lint

root=Path('work/japanese-audit13')
if not (root/'phase1-payload.json').exists():
    (root/'phase1-payload.json').write_bytes((root/'payload.json').read_bytes())
heads=json.loads((root/'checked-heads.json').read_bytes())
census=json.loads((root/'census.json').read_bytes())
observed={r['number']:r for r in json.loads((root/'observations.json').read_bytes())}
video=json.loads((root/'video-capture.json').read_bytes())
assert video['verified']
photos=json.loads((root/'files-payload.json').read_bytes())
captures=list(map(json.loads,(root/'image-captures.jsonl').read_text().splitlines()))
assert len(captures)==2 and all(r['verified'] for r in captures)
heads.update(pages([f['title'] for f in photos]))
rows=[]
diffs=[]
def field(text,name,value):
    pattern=r'<tr><th>'+re.escape(name)+r'</th><td>.*?</td></tr>\s*'
    row=f'<tr><th>{name}</th><td>{value}</td></tr>\n'
    if re.search(pattern,text,re.S):return re.sub(pattern,lambda m:row,text,count=1,flags=re.S)
    return text.replace('</table>',row+'</table>',1)

def draft(title,text,why,number=None):
    rev=heads[title]['revisions'][0]
    before=rev['slots']['main']['content']
    if '<ref name="jp-face" />' in text and not re.search(r'<ref name="jp-face"\s*>',text):
        file=re.search(r'\[\[File:([^|\]]+)',text)[1]
        text=text.replace('<ref name="jp-face" />',f'<ref name="jp-face">[[:File:{file}|Original Japanese printed face]].</ref>',1)
    assert text!=before,title
    assert not lint(text,title)[0],(title,lint(text,title)[0])
    rows.append(dict(number=number,title=title,text=text,before_text=before,before_revid=rev['revid'],before_sha256=hashlib.sha256(before.encode()).hexdigest(),summary='Verify Japanese Premiere symbols and preserve original source evidence (#361)',changes=why))
    diffs.append(''.join(difflib.unified_diff(before.splitlines(True),text.splitlines(True),fromfile=title+' before',tofile=title+' after')))

set_title='Premiere (Japanese)'
set_text=heads[set_title]['revisions'][0]['slots']['main']['content']
for card in census:
    n,title=card['number'],card['title']
    before=heads[title]['revisions'][0]['slots']['main']['content']
    text=before
    changes=[]
    if card['lint_flags']:
        assert all(f.startswith('ARCHIVE') for f in card['lint_flags'])
        def archived(m):
            if 'https://www.youtube.com/watch?v=qqdS5JpNPiE' not in m[0]:return m[0]
            assert 'web.archive.org' not in m[0]
            original=m[0]
            if original.startswith('<ref>') and observed[n]['icons_observed']:
                original=original.replace('<ref>','<ref name="video">',1)
            return original[:-6]+f' Preserved copy: [{video["capture"]} Internet Archive watch page]. [[:File:{card["files"][0]}|Preserved card frame]].</ref>'
        text=re.sub(r'<ref\b(?![^>]*?/\s*>)[^>]*>.*?</ref>',archived,text,flags=re.S)
        text=re.sub(r'(?m)^\* (\[https://www.youtube.com/watch\?v=qqdS5JpNPiE[^\n]+)$',lambda m:'* '+m[1]+f' Preserved copy: [{video["capture"]} Internet Archive watch page].',text)
        assert text!=before,title
        if observed[n]['icons_observed']:
            text=field(text,'Icons',' '.join('[['+i+']]' for i in observed[n]['icons_observed'])+'<ref name="video" />')
            changes.append('face-verified printed symbols')
        changes.append('verified archived watch-page citation and preserved frame link')
    if n in [299,300]:
        ref='<ref name="video" />' if n==299 else '<ref name="jp-face" />'
        text=field(text,'Hyperspeed','None (no hyperdrive)'+ref)
        changes.append('explicit printed absence of hyperdrive; no invented numeric hyperspeed')
    if n==31:
        text=field(text,'Uniqueness','Restricted (three asterisks)<ref name="jp-face" />')
        changes.append('three printed uniqueness asterisks')
    if n==165:
        text=field(text,'Icons','[[Imperial]] [[Pilot]]<ref name="jp-face" />')
        note='The preserved frame shows the Imperial and Pilot icons. Its lower edge is cropped, so it does not establish whether any additional icon is printed below the visible area.<ref name="jp-face" />\n'
        assert '<h2>Notes</h2>' in text
        text=text.replace('<h2>Notes</h2>','<h2>Notes</h2>\n'+note,1)
        changes.append('visible Imperial/Pilot symbols, with explicit lower-edge evidence limit')
    if n in [25,185]:
        photo=next(f for f in photos if f'-{n}o-' in f['name'])
        old_file=card['files'][0]
        assert old_file in text
        text=text.replace(old_file,photo['name'])
        text=field(text,'Icons','[[Droid]]<ref name="jp-face" />' if n==25 else '[[Imperial]] [[Pilot]]<ref name="jp-face" />')
        text=field(text,'Deploy','1' if n==25 else '2')
        text=field(text,'Forfeit','3')
        set_text=set_text.replace(old_file,photo['name'])
        changes.append('complete collector photograph replaces crop; full bottom edge verifies deploy/forfeit and icon extent')
    if text!=before:draft(title,text,changes,n)
for photo in photos:
    cap=next(r for r in captures if r['title']==photo['title'])
    text=photo['desc'].replace('\n\n== References ==',f'<ref name="uploaded-face">Preserved copy: [{cap["capture"]} Internet Archive uploaded JPEG], byte-checked against the original photograph.</ref>\n\n== References ==')
    draft(photo['title'],text,['verified preservation link for exact uploaded original JPEG'])
draft(set_title,set_text,['complete R4-E1 and Lieutenant Tanbris face thumbnails'])
(root/'phase2-payload.json').write_text(json.dumps(dict(rows=rows),ensure_ascii=False,indent=2),encoding='utf8')
(root/'payload.json').write_bytes((root/'phase2-payload.json').read_bytes())
(root/'phase2.diff').write_text('\n'.join(diffs),encoding='utf8')
print(len(rows),'phase-two drafts; all zero lint')
