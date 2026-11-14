import collections,json,re
from pathlib import Path
import pymupdf
root=Path(__file__).parent;doc=pymupdf.open(root/'checklist.pdf')
rows=[];product=None;side=None
for i in range(27,32):
    page=doc[i]
    for left,right in [(0,333),(333,595)]:
        text=page.get_text(clip=pymupdf.Rect(left,80,right,785),sort=True)
        for line in text.splitlines():
            if 'Reflections III Foil Cards' in line:product='Reflections III';side=None
            elif 'Reflections II Foil Cards' in line:product='Reflections II: Expanding the Galaxy';side=None
            elif 'Reflections Foil Cards' in line:product='Reflections';side=None
            elif 'Tournament Promotional Foil' in line:product=None
            elif product and re.match(r'\s*(Dark|Light) Side',line):side=re.match(r'\s*(Dark|Light) Side',line)[1]
            m=re.search(r'R(\d+)\s*[—–-]\s*(.*?)\s+(UR|SR|VR|P)\s*$',line)
            if product and m:rows.append(dict(product=product,side=side,number=int(m[1]),label=m[2].strip(),rarity=m[3],page=i+1,japanese='{Japanese}' in m[2],alternate_image='{AI}' in m[2]))
(root/'pdf-checklist-ledger.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print(collections.Counter(r['product'] for r in rows))
for p,count in [('Reflections',114),('Reflections II: Expanding the Galaxy',105),('Reflections III',100)]:
    found={r['number'] for r in rows if r['product']==p};print(p,'missing',set(range(1,count+1))-found)
print('AI:',[(r['number'],r['label']) for r in rows if r['alternate_image']])
