"""Canonical, deduplicated family links without inventing playable mappings."""
import re
import mwparserfromhell as mw

def card(s):return next(t for t in mw.parse(s).filter_templates(recursive=False) if str(t.name).strip()=='Card')

def canonical(title,heads):
    seen=set()
    while title in heads and title not in seen:
        seen.add(title);p=heads[title]
        if 'revisions' not in p:break
        m=re.match(r'#REDIRECT\s*\[\[([^\]]+)\]\]',p['revisions'][0]['slots']['main']['content'],re.I)
        if not m:break
        title=m[1]
    return title

def label(title,t):
    era=str(t.get('era').value) if t.has('era') else ''
    suffix=' Errata'+(' 2' if '(Errata 2)' in title else ' 3' if '(Errata 3)' in title else '') if '(Errata' in title else ''
    for key in ['Virtual Original','Virtual Legacy','Virtual Modern']:
        if key in era:return key+suffix
    if '(PC Errata' in title:return 'PC Errata'+(' 2' if '(PC Errata 2)' in title else '')
    if '(Errata' in title:return 'Decipher Errata'+(' 2' if '(Errata 2)' in title else '')
    if 'Japanese' in title:return 'Decipher (Japanese)'
    for qualifier in ['Revised','Unlimited','Reflections III Foil','Reflections II Foil','Reflections Foil']:
        if '('+qualifier+')' in title:return 'Decipher ('+qualifier.replace('Foil','foil')+')'
    return 'Decipher'

def new_navigation(r,heads,families,readings):
    root_title=canonical(r['title'],heads)
    root=card(heads[root_title]['revisions'][0]['slots']['main']['content'])
    oldvalue='\n'.join(str(root.get(k).value) for k in ['versions','printings'] if root.has(k))
    navigators=[t for t in mw.parse(oldvalue).filter_templates() if str(t.name).strip().startswith('Card versions/')]
    if navigators:
        assert len(navigators)==1
        return str(navigators[0])
    order=[root_title]+[canonical(str(w.title).strip(),heads) for w in mw.parse(oldvalue).filter_wikilinks()]+families[r['title']]
    current_batch={row['article'] for row in readings}
    order=list(dict.fromkeys(t for t in order if t in families[r['title']] and t not in current_batch))
    entries=[]
    for i,title in enumerate(order):
        t=card(heads[title]['revisions'][0]['slots']['main']['content']);prefix=label(title,t)
        group=0 if prefix.startswith('Decipher') and 'Errata' not in prefix else 1 if prefix.startswith('Decipher') else 2 if prefix.startswith('PC') else 3 if prefix.startswith('Virtual Original') else 4 if prefix.startswith('Virtual Legacy') else 5
        entries.append((group,i,"'''"+prefix+"''' — [["+title+']]'))
    for row in readings:
        if row['title']!=r['title'] and row['title'] not in order:continue
        product={'Reflections':'Reflections','Reflections II: Expanding the Galaxy':'Reflections II','Reflections III':'Reflections III'}[row['product']]
        dest="'''this page'''" if row['article']==r['article'] else '[['+row['article']+']]'
        entries.append((0,10000,"'''Decipher ("+product+" foil)''' — "+dest))
    return '<br />'.join(e[2] for e in sorted(entries))
