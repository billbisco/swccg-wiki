"""Guarded explicit card-date edits. No set fallback, network or live writes."""
from __future__ import annotations
import hashlib
import re

DATE_FIELDS = frozenset({'released', 'effective', 'remastered', 'blanked', 'retired'})

class UnsafeDateEdit(ValueError):
    pass

def sha256(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def split_outer(text):
    """Preserve top-level parameter spelling and whitespace byte for byte."""
    parts=[];start=0;depth=0;links=0;i=0
    masked=re.sub(r'<!--.*?-->|<nowiki\b[^>]*>.*?</nowiki\s*>',lambda m:' '*len(m[0]),text,flags=re.S|re.I)
    while i<len(text):
        pair=masked[i:i+2]
        if pair=='{{':depth+=1;i+=2;continue
        if pair=='}}':depth-=1;i+=2;continue
        if pair=='[[':links+=1;i+=2;continue
        if pair==']]':links-=1;i+=2;continue
        if masked[i]=='|' and depth==links==0:parts.append(text[start:i]);start=i+1
        i+=1
    parts.append(text[start:])
    return parts

def card_template(text):
    masked=re.sub(r'<!--.*?-->|<nowiki\b[^>]*>.*?</nowiki\s*>',lambda m:' '*len(m[0]),text,flags=re.S|re.I)
    stack=[];matches=[]
    for token in re.finditer(r'{{|}}',masked):
        if token[0]=='{{':stack.append(token.start())
        elif stack:
            begin=stack.pop();end=token.end();raw=text[begin+2:end-2];parts=split_outer(raw)
            if re.sub(r'^Template:','',parts[0].strip(),flags=re.I).casefold()=='card':matches.append((begin,end,parts))
    if len(matches)!=1:raise UnsafeDateEdit('Exactly one actual Card template is required')
    return matches[0]

def field_values(parts):
    fields={}
    for index,part in enumerate(parts[1:],1):
        if '=' not in part:continue
        key,value=part.split('=',1);key=key.strip()
        fields.setdefault(key,[]).append((index,value.strip()))
    return fields

def apply_date_claim(text, claim):
    """Apply one reviewed claim only to the exact original revision payload."""
    field=claim['field'];new=claim['new_value'];old=claim.get('old_value','')
    if field not in DATE_FIELDS:raise UnsafeDateEdit('Only named date fields may change')
    expected=claim.get('base_wikitext_sha256',claim.get('source_sha256'))
    if not expected or sha256(text)!=expected:raise UnsafeDateEdit('Base content changed')
    if new and not re.search(r'<ref\b',new,re.I):raise UnsafeDateEdit('Date value needs its source reference')
    begin,end,parts=card_template(text);before=field_values(parts)
    if len(before.get(field,[]))>1:raise UnsafeDateEdit('Duplicate date parameter')
    actual=before.get(field,[(None,'')])[0][1]
    if actual!=old:raise UnsafeDateEdit('Existing date differs from approved old value')
    if claim.get('card_uid') and before.get('card_uid',[(None,'')])[0][1]!=claim['card_uid']:raise UnsafeDateEdit('Card printing identity changed')
    if actual==new:return text
    if before.get(field):
        index=before[field][0][0];part=parts[index];key,previous=part.split('=',1)
        if not previous.strip():
            prefix=re.match(r'[ \t]*',previous)[0];suffix=previous[len(prefix):]
        else:
            prefix=previous[:len(previous)-len(previous.lstrip())];suffix=previous[len(previous.rstrip()):]
        parts[index]=key+'='+prefix+new+suffix
    else:
        index=before.get('versions',[(len(parts),None)])[0][0]
        parts.insert(index,field+'='+new+'\n')
    result=text[:begin]+'{{'+'|'.join(parts)+'}}'+text[end:]
    _,_,after_parts=card_template(result);after=field_values(after_parts)
    for key,value in before.items():
        if key!=field and after.get(key)!=[(i+(1 if not before.get(field) and i>=index else 0),v) for i,v in value]:
            raise UnsafeDateEdit('Unrelated card parameter changed')
    if after[field][0][1]!=new:raise UnsafeDateEdit('Date value did not round trip')
    return result
