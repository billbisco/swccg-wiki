"""Reconcile checklist spellings/qualifiers; retain the exact source label."""
import collections,difflib,json,re,unicodedata
from pathlib import Path
root=Path(__file__).parent
rows=json.loads((root/'manifest.json').read_bytes());pdf=json.loads((root/'pdf-checklist-ledger.json').read_bytes())
def norm(s):
    s=re.sub(r'\{.*?\}|\(.*?\)','',s)
    return re.sub(r'[^a-z0-9]','',unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower())
spelling={'Braniac':'Brainiac','Captain Gilad Pallaeon':'Captain Gilad Pellaeon','Lott Dodd':'Lott Dod','Talon Karde':'Talon Karrde','Yoda, Jedi Council Member':'Yoda, Senior Council Member','Lando With Vibro Axe':'Lando With Vibro-Ax','Executor : Holotheater':'Executor: Holotheatre','U-3PO':'U-3PO (Yoo-Threepio)','IT-O':'IT-O (Eyetee-Oh)','2-1B':'2-1B (Too-Onebee)'}
matched=set();problems=[]
for p in pdf:
    if p['rarity']=='P':continue
    label=re.sub(r'\s*\{.*?\}','',p['label']).strip();label=spelling.get(label,label)
    candidates=[(i,r) for i,r in enumerate(rows) if r['product']==p['product'] and r['side']==p['side'] and norm(label) in [norm(r['label']),norm(r['checklist_target'])]]
    if len(candidates)!=1:problems.append(dict(pdf=p,candidates=[r['label'] for i,r in candidates]));continue
    i,r=candidates[0];assert i not in matched;r.update(checklist_number=p['number'],pdf_page=p['page'],pdf_label=p['label'],alternate_image=p['alternate_image'],language='Japanese' if p['japanese'] else 'English');matched.add(i)
    assert r['rarity']==p['rarity'],(r,p)
    if r['alternate_image'] and not r['existing_article']:
        r['proposed_article']=r['label']+' (AI) (Reflections III Foil)'
    if r['product']=='Reflections' and r['label']=='Artoo':r.update(counterpart_candidates=["Artoo (Jabba's Palace)"],proposed_article='Artoo (Reflections Foil)')
    if r['product']=='Reflections' and r['label']=='Boba Fett':r['counterpart_candidates']=['Boba Fett (Cloud City)','Boba Fett (Special Edition)']
    if r['label']=='Death Star' and r['side']=='Light':r.update(counterpart_candidates=['Death Star (Special Edition)'],proposed_article='Death Star (Light) (Reflections Foil)')
    if r['label']=='Death Star' and r['side']=='Dark' and r['product']=='Reflections':r['proposed_article']='Death Star (Dark) (Reflections Foil)'
    if r['label']=='Leia' and r['product'].startswith('Reflections II'):r['counterpart_candidates']=['Leia (Jedi Pack)','Leia (ESB Two-Player)']
    if r['label']=='See-Threepio':r['counterpart_candidates']=["See-Threepio (Enhanced Jabba's Palace)"]
    if r['label']=='Kiffex' and r['side']=='Light':r.update(counterpart_candidates=["Kiffex (Jabba's Palace)"],proposed_article='Kiffex (Light) (Reflections II Foil)')
    if r['label']=='Kiffex' and r['side']=='Dark':r['proposed_article']='Kiffex (Dark) (Reflections II Foil)'
    if r['label']=='Hoth: Wampa Cave':r['counterpart_candidates']=['Hoth: Wampa Cave (7th Marker)']
    if r['label'] in ['Artoo & Threepio','Owen Lars & Beru Lars','Dr. Evazan & Ponda Baba']:r['counterpart_candidates']=[r['label'].replace(' & ',' & •')]
assert not problems,problems
assert len(matched)==314,len(matched)
(root/'manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print('314/314 source rows reconciled;',sum(r['alternate_image'] for r in rows),'AI foils; 15 Japanese pack foils; five excluded toppers')
