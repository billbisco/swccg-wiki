"""Add catalog identities to reused Japanese foils without changing content/mappings."""
import hashlib,json,re,sys
from pathlib import Path
sys.path.insert(0,'work/japanese-infobox287/vendor');import mwparserfromhell as mw
root=Path(__file__).parent;heads=json.loads((root/'final-inventory-heads.json').read_bytes())
packet=[];proof=[]
for row in json.loads((root/'manifest.json').read_bytes()):
    if row['language']!='Japanese':continue
    title=row['proposed_article'];head=heads[title];rev=head['revisions'][0];old=rev['slots']['main']['content'];code=mw.parse(old)
    t=next(t for t in code.filter_templates(recursive=False) if str(t.name).strip()=='Card')
    if t.has('publication_id'):continue
    product={'Reflections II: Expanding the Galaxy':'reflections-ii','Reflections III':'reflections-iii'}[row['product']]
    base=re.sub(r' \(Japanese Reflections (?:II|III) Foil\)$','',title);assert base!=title
    pid='decipher-'+product+'-'+re.sub(r'[^a-z0-9]+','-',base.lower()).strip('-')+'-foil-ja'
    t.add('publication_id',pid+'\n',before='image',preserve_spacing=False)
    text=str(code);t.remove('publication_id');assert str(code)==old
    packet.append(dict(title=title,text=text,before_revid=rev['revid'],before_sha256=hashlib.sha256(old.encode()).hexdigest(),section=0,summary='Add distinct Japanese foil publication identity; preserve printed fields and existing gameplay mappings (#381)'))
    proof.append(dict(title=title,publication_id=pid,all_preexisting_source_exactly_conserved=True,playable_ids_unchanged=True))
for name,data in [('japanese-publication-identity-packet.json',packet),('japanese-publication-identity-conservation.json',proof)]:
    (root/name).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
print(len(packet),'catalog identities prepared; existing Japanese content and gameplay mappings conserved')
