import re,sys,json,later
for n in range(1,18):
    w=open(f'now{n}.wiki').read()
    table,rep=later.build_section(w)
    m=re.search(r'=== Later printings ===\n\{\|.*?\n\|\}',w,re.S)
    assert m and table, n
    w2=w[:m.start()]+'=== Later printings ===\n'+table+w[m.end():]
    open(f'final/ovs{n}.wiki','w').write(w2)
    old=len(re.findall(r'\(revised text\)|\(same text\)',m.group(0))); new=len(re.findall(r'\(revised text\)|\(same text\)',table))
    rows_old=len(re.findall(r'^\| \d+ \|\|',m.group(0),re.M)); rows_new=len(re.findall(r'^\| \d+ \|\|',table,re.M))
    print(n,'modern',old,'->',new,'rows',rows_old,'->',rows_new)
