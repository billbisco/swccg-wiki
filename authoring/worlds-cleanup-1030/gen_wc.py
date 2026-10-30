import re, glob, os, json
D = "../hubs_draft"
def strip_refs(s):
    s = re.sub(r"<ref[^>/]*/>", "", s); s = re.sub(r"(?s)<ref[^>]*>.*?</ref>", "", s)
    return s.strip()
rows = []
for y in range(1996, 2027):
    f = glob.glob(f"{D}/{y}_*World_Championship.wiki")[0]
    hub = os.path.basename(f)[:-5].replace("_", " ")
    t = open(f, encoding="utf-8").read()
    ib = t[:t.find("\n|}")]
    def cell(label):
        m = re.search(r"\n! " + label + r"\n\| (.*)", ib)
        return strip_refs(m.group(1)) if m else ""
    img = re.search(r"\[\[File:([^|\]]+)", ib)
    res = t[t.find("== Results =="):]
    r1 = re.search(r"\n\| 1 \|\| (.*)", res)
    dark = light = "—"
    if r1:
        parts = [p.strip() for p in r1.group(1).split("||")]
        if len(parts) >= 3: dark, light = strip_refs(parts[1]), strip_refs(parts[2])
    rows.append(dict(year=y, hub=hub, img=img.group(1).strip() if img else "", champ=cell("Champion"), ru=cell("Runner-up"),
        venue=cell("Venue"), dates=cell("Dates"), players=cell("Players"), fmt=cell("Format"), org=cell("Organizer"),
        dark=dark, light=light))
json.dump(rows, open("rows.json", "w"), indent=1, ensure_ascii=False)
for r in rows: print(r["year"], "|", r["img"][:40], "|", r["champ"], "|", r["ru"], "|", r["venue"][:60], "|", r["dates"][:40], "|", r["players"], "|", r["fmt"], "|", r["dark"][:50], "|", r["light"][:50])
