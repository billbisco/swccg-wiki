import re
def sections(t):
    parts=re.split(r'^(={2,3}) *(.+?) *\1\s*$',t,flags=re.M)
    out=[('LEAD',2,parts[0])]
    for i in range(1,len(parts),3):
        out.append((parts[i+1],len(parts[i]),parts[i+2]))
    return out
def tables(txt):
    return re.findall(r'\{\|.*?\n\|\}',txt,flags=re.S)
def rows(tbl):
    lines=tbl.split('\n')
    hdr=[l for l in lines if l.startswith('!')]
    body=[]
    cur=None
    for l in lines[1:]:
        if l.startswith('|-') or l.startswith('|}'):
            cur=None; continue
        if l.startswith('!'): continue
        if l.startswith('|'):
            cells=[c.strip() for c in split_cells(l[1:])]
            body.append(cells)
    return hdr,body
def split_cells(s):
    # split on || not inside [[ ]]
    out=[];buf='';depth=0;i=0
    while i<len(s):
        if s.startswith('[[',i): depth+=1;buf+='[[';i+=2;continue
        if s.startswith(']]',i): depth-=1;buf+=']]';i+=2;continue
        if s.startswith('||',i) and depth==0: out.append(buf);buf='';i+=2;continue
        buf+=s[i];i+=1
    out.append(buf);return out
def nontable(txt):
    return re.sub(r'\{\|.*?\n\|\}','<<TABLE>>',txt,flags=re.S).strip()
