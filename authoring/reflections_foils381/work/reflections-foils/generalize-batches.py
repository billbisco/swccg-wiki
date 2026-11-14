"""Retain the tested first-batch path while making later batches parameterized."""
from pathlib import Path
p=Path(__file__).parent
if (p/'build-batch.py').exists():
    print('One-time scaffold already generated; maintained batch tools must not be overwritten.')
    raise SystemExit(0)
for old,new in [('fetch-first-families.py','fetch-families.py'),('archive-images.py','archive-batch-images.py'),('build-first-preservation-links.py','build-preservation-links.py')]:
    s=(p/old).read_text(encoding='utf8')
    s=s.replace('import json,subprocess','import json,subprocess,sys').replace('import hashlib,json\n','import hashlib,json,sys\n')
    s=s.replace('root=Path(__file__).parent','root=Path(__file__).parent;stage=sys.argv[1]')
    import re
    s=re.sub(r"root/'first-([^']+)'",r"root/(stage+'-\1')",s)
    if new=='build-preservation-links.py':s=s.replace("assert len(captures)==10 and all(r['verified'] for r in captures.values())","assert captures and all(r['verified'] for r in captures.values())")
    (p/new).write_text(s,encoding='utf8')

s=(p/'build-first.py').read_text(encoding='utf8')
s=s.replace('root=Path(__file__).parent','root=Path(__file__).parent;stage=sys.argv[1]\nfrom source_registry import provenance\nfrom navigation import new_navigation')
s=re.sub(r"root/'first-([^']+)'",r"root/(stage+'-\1')",s)
s=s.replace("title=r['article'];pid='decipher-reflections-'", "title=r['article'];product=r['product'];product_label={'Reflections':'Reflections','Reflections II: Expanding the Galaxy':'Reflections II','Reflections III':'Reflections III'}[product];release={'Reflections':'January 2000','Reflections II: Expanding the Galaxy':'January 2001','Reflections III':'October 2001'}[product];pid='decipher-'+re.sub(r'[^a-z0-9]+','-',product_label.lower())+'-'")
s=s.replace("    face='<ref name=\"foil-face\">[[:'+f['title']+'|Original printed Reflections foil face]], PSA certification '+r['physical_cert']+'.</ref>'", "    p=provenance(r)\n    face='<ref name=\"foil-face\">[[:'+f['title']+'|Original printed '+product_label+' foil face]], '+p['credit']+'.</ref>'")
s=s.replace("for k in ['subtype','model']:","for k in ['subtype','type_display','model']:")
s=s.replace("set='Reflections'","set=product").replace("release='January 2000'","release=release")
s=s.replace("['destiny','power','ability','armor','maneuver','deploy','forfeit','printed_label']", "['destiny','power','ability','armor','maneuver','hyperspeed','deploy','forfeit','printed_label']")
s=s.replace("fields['version_label']='Reflections foil'", "fields['version_label']=product_label+' foil'")
s=s.replace("'[[Reflections]] · [['", "'[['+product+']] · [['")
s=s.replace("+' foil in [[Reflections]] in January 2000.","+' foil in [['+product+']] in '+release+'.")
start=s.index("    original_nav=nav(r['title'])")
end=s.index("    fields['has_refs']",start)
s=s[:start]+"    fields['versions']=new_navigation(r,heads,families,readings)\n    fields['sources']='* Original printed foil face: [[:'+f['title']+'|'+r['printed_title']+', '+product_label+' foil]], '+p['credit']+'.'\n"+s[end:]
s=s.replace("def entry(r):return \"'''Decipher (Reflections foil)''' — [[\"+r['article']+'|'+r['printed_title']+\" (Reflections foil)]]\"", "def entry(r):return \"'''Decipher (\"+{'Reflections':'Reflections','Reflections II: Expanding the Galaxy':'Reflections II','Reflections III':'Reflections III'}[r['product']]+\" foil)''' — [[\"+r['article']+'|'+r['printed_title']+\" (foil)]]\"")
(p/'build-batch.py').write_text(s,encoding='utf8')
