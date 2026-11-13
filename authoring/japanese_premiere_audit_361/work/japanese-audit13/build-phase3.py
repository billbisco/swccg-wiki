import difflib
import hashlib
import json
from pathlib import Path
import re
import sys
sys.path.insert(0,'work/wiki-tools')
from style_lint import lint
root=Path('work/japanese-audit13')
if not (root/'merged-phase2-payload.json').exists():
    (root/'merged-phase2-payload.json').write_bytes((root/'payload.json').read_bytes())
heads=json.loads((root/'checked-heads.json').read_bytes())
census=json.loads((root/'census.json').read_bytes())
translations={
190:dict(game="When battling at a site where [[Dr. Evazan]] is present, you may add 3 to Ponda Baba's power, but only if none of your opponent's lightsabers is there. Adds 2 to the power of a starship he pilots.",lore="A male Quara (a fingered Aqualish), an assassin and smuggler. His partner Dr. Evazan fitted him with a poorly functioning bioprosthetic hand."),
263:dict(game="Choose any one weapon except a [[Gaderffii Stick]] or an Ewok weapon as the target. Draw destiny. If destiny is less than that weapon's destiny, the weapon is lost. If destiny is 0, the character or starship carrying the weapon is also lost at the same time.",lore="Weapons such as lightsabers, turbolasers and blasters operate using powerful energy cells or generators. Sometimes a cell overheats and explodes together with the weapon."),
264:dict(game="Choose one of the following. 1: Immediately cause any one Rebel trooper to be lost. 2: Use immediately after winning a battle in which a [[Dark Jedi]] participated. Use 1 Force and choose one opposing character that participated in the battle. Draw destiny. If destiny is greater than the target's ability, the target is lost.",lore="Darth Vader sometimes uses somewhat physical methods during interrogation. Captain Antilles of the Tantive IV chose death rather than reveal the whereabouts of the Death Star plans."),
265:dict(game="During a battle at a site, you may use two or more of your weapons there together and add their weapon destiny values to attack a single character or vehicle.",lore='“No one but Imperial stormtroopers could make a kill this precisely.”'),
}
rows=[];diffs=[]
for n in [18,23,86,190,263,264,265]:
    title=census[n-1]['title'];rev=heads[title]['revisions'][0]
    before=rev['slots']['main']['content'];text=before
    if n in [18,23]:
        text=text.replace('<h2>Translation of Japanese Text</h2>','<h2>Translation of Japanese Text</h2>\n'+"'''Title:''' "+census[n-1]['stats']['Title']+'.<ref name="jp-face" />\n',1)
    if n in translations:
        game,lore=translations[n]['game'],translations[n]['lore']
        match=re.search(r'(<h2>Translation of Japanese Text</h2>\s*)(.*?)(?=<h2>)',text,re.S)
        old=match[2].strip()
        if n==190:
            title_line,comparison=old.split('. The later ',1)
            old=title_line+'.'
            text=text.replace('<h2>Notes</h2>','<h2>Notes</h2>\n'+"'''Comparison with the English printing:''' The later "+comparison+'\n',1)
            match=re.search(r'(<h2>Translation of Japanese Text</h2>\s*)(.*?)(?=<h2>)',text,re.S)
        replacement=old+"\n\n'''Card text:''' "+game+'<ref name="jp-face" />'+"\n\n'''Lore:''' "+lore+'<ref name="jp-face" />\n'
        text=text[:match.start(2)]+replacement+text[match.end(2):]
    if n in [86,263,264,265]:
        subtype='Used Interrupt' if n==86 else 'Lost Interrupt'
        text,count=re.subn(r'<tr><th>Type</th><td>.*?</td></tr>',f'<tr><th>Type</th><td>[[Interrupt]] ([[{subtype}]])</td></tr>',text,count=1)
        assert count==1
    if '<ref name="jp-face" />' in text and not re.search(r'<ref name="jp-face"\s*>',text):
        filename=census[n-1]['files'][0]
        text=text.replace('<ref name="jp-face" />',f'<ref name="jp-face">[[:File:{filename}|Original Japanese printed face]].</ref>',1)
    assert not lint(text,title)[0],(title,lint(text,title)[0])
    rows.append(dict(number=n,title=title,text=text,before_text=before,before_revid=rev['revid'],before_sha256=hashlib.sha256(before.encode()).hexdigest(),summary='Complete missing Japanese-face translations and verified Interrupt subtypes (#361)',changes=['complete remaining translation components; preserve comparison note separately','face-verified Used/Lost subtype where inspected']))
    diffs.append(''.join(difflib.unified_diff(before.splitlines(True),text.splitlines(True),fromfile=title+' before',tofile=title+' after')))
(root/'phase3-payload.json').write_text(json.dumps(dict(rows=rows),ensure_ascii=False,indent=2),encoding='utf8')
(root/'payload.json').write_bytes((root/'phase3-payload.json').read_bytes())
(root/'phase3.diff').write_text('\n'.join(diffs),encoding='utf8')
print(len(rows),'final component-translation drafts; all zero lint')
