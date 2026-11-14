"""Publication IDs retain side/art/title qualifiers without minting gameplay IDs."""
import re
def publication_id(article,product):
    product_label={'Reflections':'Reflections','Reflections II: Expanding the Galaxy':'Reflections II','Reflections III':'Reflections III'}[product]
    base=re.sub(r'\s*\(Reflections(?: II| III)? Foil\)$','',article);assert base!=article,article
    alternate='(AI)' in base;base=base.replace(' (AI)','')
    slug=re.sub(r'[^a-z0-9]+','-',base.lower()).strip('-')
    return 'decipher-'+re.sub(r'[^a-z0-9]+','-',product_label.lower())+'-'+slug+('-ai' if alternate else '')+'-foil-en'
