"""Repair edition prefixes while retaining every existing link and gameplay code."""
import hashlib,json,re,subprocess,sys
from pathlib import Path
sys.path.insert(0,'work/japanese-infobox287/vendor');import mwparserfromhell as mw
sys.path.insert(0,'work/wiki-tools')
from navigation import label,canonical
from publication_policy import lint
root=Path(__file__).parent;last=int(sys.argv[1]);readings=[];by_stage={};summary='Use existing explicit publication labels in foil family navigation; retain printed fields (#381)'
for stage in ['first',*['batch'+str(n) for n in range(2,last+1)]]:
 if not (root/(stage+'-new-receipts.jsonl')).exists():continue
 for row in json.loads((root/(stage+'-readings.json')).read_bytes()):readings.append(row);by_stage[row['article']]=stage
(root/'published-nav-readings.json').write_text(json.dumps(readings,ensure_ascii=False,indent=2),encoding='utf8')
receipts={r['title']:r for r in map(json.loads,(root/'published-nav-repair-receipts.jsonl').read_text(encoding='utf8').splitlines())} if (root/'published-nav-repair-receipts.jsonl').exists() else {}
original=json.loads((root/'published-nav-first-heads.json').read_bytes())
subprocess.run([sys.executable,str(root/'fetch-families.py'),'published-nav'],check=True)
heads=json.loads((root/'published-nav-family-heads.json').read_bytes());families=json.loads((root/'published-nav-families.json').read_bytes());packets=[]
proof_file=root/'published-nav-conservation.json';proof={r['title']:r for r in json.loads(proof_file.read_bytes())} if proof_file.exists() else {}
def card(text):return next(t for t in mw.parse(text).filter_templates(recursive=False) if str(t.name).strip()=='Card')
def prefixes(row):
 t=card(heads[canonical(row['title'],heads)]['revisions'][0]['slots']['main']['content']);known={}
 for key in ['versions','printings']:
  if not t.has(key):continue
  for bit in re.split(r'<br\s*/?>',str(t.get(key).value)):
   m=re.search(r"'''([^']+)'''",bit)
   if m:
    for link in mw.parse(bit).filter_wikilinks():known.setdefault(canonical(str(link.title).strip(),heads),m[1])
 return known
def relabel(value,preferred):
 result=[]
 for index,bit in enumerate(re.split(r'<br\s*/?>',value.strip())):
  m=re.search(r"'''([^']+)'''",bit);targets=[canonical(str(l.title).strip(),heads) for l in mw.parse(bit).filter_wikilinks()];target=next((t for t in targets if t in heads and 'revisions' in heads[t] and card_or_none(heads[t]['revisions'][0]['slots']['main']['content'])),None)
  prefix=m[1] if m else ''
  if m and target:
   prefix=label(target,card(heads[target]['revisions'][0]['slots']['main']['content']),preferred.get(target));bit=bit[:m.start(1)]+prefix+bit[m.end(1):]
  group=0 if prefix.startswith('Decipher') and 'Errata' not in prefix else 1 if prefix.startswith('Decipher') else 2 if prefix.startswith('PC') else 3 if prefix.startswith('Virtual Original') else 4 if prefix.startswith('Virtual Legacy') else 5
  result.append((group,index,bit))
 new='<br />'.join(x[2] for x in sorted(result))
 assert sorted(re.findall(r'<code>.*?</code>',value))==sorted(re.findall(r'<code>.*?</code>',new))
 assert sorted(str(l) for l in mw.parse(value).filter_wikilinks())==sorted(str(l) for l in mw.parse(new).filter_wikilinks())
 return new
def card_or_none(text):
 return any(str(t.name).strip()=='Card' for t in mw.parse(text).filter_templates(recursive=False))
# Remove obsolete, generated-but-never-applied plans from the earlier attempt.
for stage in set(by_stage.values()):
 f=root/(stage+'-correction-packet.json')
 if f.exists():
  prior=json.loads(f.read_bytes());prior=[r for r in prior if r.get('summary')!=summary or r['title'] in receipts];f.write_text(json.dumps(prior,ensure_ascii=False,indent=2),encoding='utf8')
for row in readings:
 h=heads[row['article']];rev=h['revisions'][0];old=rev['slots']['main']['content'];code=mw.parse(old);t=card(code);base=t
 if row['article'] in receipts and hashlib.sha256(old.encode()).hexdigest()==receipts[row['article']]['sha256']:
  base=card(original[row['article']]['revisions'][0]['slots']['main']['content'])
 preferred=prefixes(row);changed=False
 before={str(p.name).strip():str(p.value) for p in t.params if str(p.name).strip() not in ['versions','printings']}
 for key in ['versions','printings']:
  if not t.has(key):continue
  value=str(base.get(key).value) if base.has(key) else str(t.get(key).value)
  if '{{Card versions/' in value:continue
  value=relabel(value,preferred)
  if str(t.get(key).value).strip()!=value.strip():t.get(key).value=value+'\n';changed=True
 if not changed:continue
 after={str(p.name).strip():str(p.value) for p in t.params if str(p.name).strip() not in ['versions','printings']};assert before==after
 text=str(code);assert not lint(text,row['article'])[0]
 packet=dict(title=row['article'],text=text,before_revid=rev['revid'],before_sha256=hashlib.sha256(old.encode()).hexdigest(),section=0,summary=summary)
 packets.append(packet);proof[row['article']]=dict(title=row['article'],before_revid=rev['revid'],non_navigation_fields_unchanged=True,existing_gameplay_codes_and_links_retained=True)
 f=root/(by_stage[row['article']]+'-correction-packet.json');prior=json.loads(f.read_bytes()) if f.exists() else [];prior=[p for p in prior if p['title']!=row['article']];prior.append(packet);f.write_text(json.dumps(prior,ensure_ascii=False,indent=2),encoding='utf8')
(root/'published-nav-repair-packet.json').write_text(json.dumps(packets,ensure_ascii=False,indent=2),encoding='utf8');proof_file.write_text(json.dumps(list(proof.values()),ensure_ascii=False,indent=2),encoding='utf8');print(len(packets),'foil prefix repairs, preserving every existing gameplay code/link and all printed fields')
