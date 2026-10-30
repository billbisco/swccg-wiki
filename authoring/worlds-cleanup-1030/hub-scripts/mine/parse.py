import re,json
def sections(txt):
    out=[];cur='_lead';buf=[]
    for line in txt.split('\n'):
        m=re.match(r'^(==+)\s*(.*?)\s*\1\s*$',line)
        if m: out.append((cur,'\n'.join(buf)));cur=m.group(2);buf=[]
        else: buf.append(line)
    out.append((cur,'\n'.join(buf)));return out
def tables(sec):
    tabs=[]
    for t in re.findall(r'\{\|.*?\n\|\}',sec,re.S):
        rows=[];hdr=None
        for chunk in re.split(r'\n\|-[^\n]*',t):
            lines=[l for l in chunk.split('\n') if l.startswith('|') or l.startswith('!')]
            lines=[l for l in lines if not l.startswith('{|') and l!='|}']
            if not lines: continue
            s=' '.join(lines)
            if s.startswith('!'):
                hdr=[c.strip() for c in re.split(r'!!|\n!',s.lstrip('!'))];continue
            cells=[c.strip() for c in re.split(r'\|\|',s[1:])]
            rows.append(cells)
        tabs.append((hdr,rows))
    return tabs
def links(s): return [m.split('|')[0].strip() for m in re.findall(r'\[\[([^\]]+)\]\]',s)]
