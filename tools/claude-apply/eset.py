#!/usr/bin/env python3
"""eset.py <tgz> <dir-in-tgz> <ticket> : unpack an errgen draft dir into /tmp/batches groups e<ticket>t, e<ticket>m<i>"""
import sys,os,json,shutil,tarfile
tgz,d,t=sys.argv[1:4]; os.chdir("/tmp/batches")
tarfile.open(tgz).extractall("eraw")
src=os.path.join("eraw",d)
rows=[l.rstrip('\n').split('\t') for l in open(src+'/apply.tsv') if l.strip()]
b=json.load(open(src+'/base_revids.json'))
T=[r for r in rows if r[0].startswith('Template:')]; M=[r for r in rows if not r[0].startswith('Template:')]
out=[]
for name,lst in [(f"e{t}t",T)]+[(f"e{t}m{i}",M[i*15:(i+1)*15]) for i in range((len(M)+14)//15)]:
    if not lst: continue
    shutil.rmtree(name,ignore_errors=True); os.makedirs(name)
    open(name+'/apply.tsv','w').write(''.join('\t'.join(r)+'\n' for r in lst))
    json.dump({r[0]:b[r[0]] for r in lst if r[0] in b},open(name+'/base_revids.json','w'))
    for r in lst: shutil.copy(src+'/'+os.path.basename(r[1]),name)
    out.append(name)
print(" ".join(out))
