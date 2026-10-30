import re, pathlib
O = pathlib.Path("orig"); P = pathlib.Path("pkg/pages"); P.mkdir(parents=True, exist_ok=True)
pages = {}
def rd(t): return (O / (t.replace(" ", "_") + ".wiki")).read_text()
AW = "https://www.starwarsccg.org/community/awards/ Star Wars CCG Awards], starwarsccg.org"
FILES = {
"Dan Kim 2010 World Championship.png": f"""== Summary ==
[[Dan Kim]] (right, holding the trophy) after winning the [[2010 World Championship]]. Players Committee homepage banner, "Meet your 2010 World Champion! Dan Kim". The man shaking his hand on the left is not named.

* '''Source:''' starwarsccg.org homepage banner <code>images/banners/worlds2010.png</code>, shown January–February 2011. Homepage capture: [https://web.archive.org/web/20110126083123/http://www.starwarsccg.org/ Internet Archive, 26 January 2011]
* '''Image preserved copy:''' [https://web.archive.org/web/20110128170822/http://starwarsccg.org/images/banners/worlds2010.png Internet Archive]
* '''Date:''' August 2010
* '''Identification:''' banner text names Dan Kim; the name label sits over the man on the right.

[[Category:Photographs of players]]""",
"Justin Desai 2013 World Championship.jpg": f"""== Summary ==
[[Justin Desai]] with the trophy after winning the [[2013 World Championship]]. Players Committee homepage banner, "World Champion 2013 – Congratulations Justin Desai".

* '''Source:''' starwarsccg.org homepage banner, shown August–December 2013 (linked to the forum announcement, topic 52082). Original: https://res.starwarsccg.org/wp/wp-content/uploads/Worldchamp.jpg (fetched 30 October 2026; the banner was never captured by the Internet Archive)
* '''Date:''' August 2013
* '''Identification:''' banner text.

[[Category:Photographs of players]]""",
"Emil Wallin and Brian Terwilliger 2014 World Championship.jpg": f"""== Summary ==
[[Brian Terwilliger]] (left, runner-up) and [[Emil Wallin]] (right, champion) with their trophies at the [[2014 World Championship]]. Players Committee homepage banner: "Congratulations Emil Wallin 2 time World Champion / Congratulations Brian Terwilliger Worlds Runner-up".

* '''Source:''' starwarsccg.org homepage banner. Homepage capture: [https://web.archive.org/web/20141008112257/http://www.starwarsccg.org/ Internet Archive, 8 October 2014]
* '''Original image:''' https://res.starwarsccg.org/wp/wp-content/uploads/banner-world-champions-20141.jpg
* '''Image preserved copy:''' [https://web.archive.org/web/20180604161703/http://www.starwarsccg.org/wp/wp-content/uploads/banner-world-champions-20141.jpg Internet Archive]
* '''Date:''' August 2014
* '''Identification:''' the banner names both players but not their positions. The man on the right matches Emil Wallin's [[:File:Emil Wallin 2015 Hall of Fame.jpg|2015 Hall of Fame photo]].

[[Category:Photographs of players]]""",
"Justin Desai and Jonny Chu 2015 World Championship.jpg": f"""== Summary ==
[[Jonny Chu]] (left, runner-up) and [[Justin Desai]] (right, champion) with their trophies at the [[2015 World Championship]] in Philadelphia. Featured image of the Players Committee post "World Champion Crowned in Philadelphia" (12 August 2015): "Justin defeated Jon Chu in the final match". Cropped to the photo (the original has a grey gradient on the left).

* '''Source:''' [https://web.archive.org/web/20151106000000/http://www.starwarsccg.org/wp/world-champion-crowned-in-philadelphia/ World Champion Crowned in Philadelphia], starwarsccg.org (Internet Archive)
* '''Original image:''' https://res.starwarsccg.org/wp/wp-content/uploads/chu-desai.jpg
* '''Image preserved copy:''' [https://web.archive.org/web/20151106060725/http://www.starwarsccg.org/wp/wp-content/uploads/chu-desai.jpg Internet Archive]
* '''Date:''' August 2015
* '''Identification:''' the post names both finalists but not their positions. The man on the left matches Jonny Chu in the [[:File:2013 Hall of Fame inaugural class.jpg|2013 Hall of Fame class photo]]; the man on the right matches Justin Desai's [[:File:Justin Desai 2013 World Championship.jpg|2013 champion photo]].

[[Category:Photographs of players]]""",
"Steve Baroni 2012 Match Play Championship.jpg": f"""== Summary ==
[[Steve Baroni]] with the trophy after winning the [[2012 Match Play Championship]]. Players Committee homepage banner: "KTOD dominates the MPC – Steve Baroni is the 2012 MPC Champion!" (KTOD: [[Kashyyyk Train of Dominance]]). The right half of the banner is a film still.

* '''Source:''' starwarsccg.org homepage banner <code>images/banners/mpc2012_champ_v2.jpg</code>. Homepage capture: [https://web.archive.org/web/20120308225002/http://www.starwarsccg.org/ Internet Archive, 8 March 2012]
* '''Image preserved copy:''' [https://web.archive.org/web/20130209065426/http://www.starwarsccg.org/images/banners/mpc2012_champ_v2.jpg Internet Archive]
* '''Date:''' February 2012
* '''Identification:''' banner text.

[[Category:Photographs of players]]""",
"Scott Lingrell Lifetime Achievement Award.png": f"""== Summary ==
[[Scott Lingrell]] with the Lifetime Achievement Award the players gave him in 2011. From the [[Hall of Fame]] section of the Players Committee awards page, captioned "Scott, with his Lifetime Achievement Award".

* '''Source:''' [{AW}; awards page capture: [https://web.archive.org/web/20160413093058/http://www.starwarsccg.org/community/awards/ Internet Archive, 13 April 2016]
* '''Original image:''' https://res.starwarsccg.org/wp/wp-content/uploads/sl-la.png
* '''Date:''' 2011 award; photo date not stated
* '''Identification:''' awards page caption.

[[Category:Photographs of players]]""",
"2013 Hall of Fame inaugural class.jpg": f"""== Summary ==
The inaugural Players Committee [[Hall of Fame]] class, enshrined at the [[2013 World Championship]] on 10 August 2013. From left: [[Kevin Shannon]], [[Jonny Chu]], [[Justin Desai]], [[Angelo Consoli]].

* '''Source:''' [{AW}; awards page capture: [https://web.archive.org/web/20160413093058/http://www.starwarsccg.org/community/awards/ Internet Archive, 13 April 2016]
* '''Original image:''' https://res.starwarsccg.org/wp/wp-content/uploads/HOF-Inagural-Class.jpg
* '''Image preserved copy (300 px):''' [https://web.archive.org/web/20160413094039/http://www.starwarsccg.org/wp/wp-content/uploads/HOF-Inagural-Class-300x225.jpg Internet Archive]
* '''Date:''' 10 August 2013
* '''Identification:''' awards page captions: "Kevin Shannon on left", "Jonny Chu second from left", "Justin Desai third from left", "Angelo Consoli far right". The single-person photos [[:File:Kevin Shannon 2013 Hall of Fame.jpg]], [[:File:Justin Desai 2013 Hall of Fame.jpg]] and [[:File:Angelo Consoli 2013 Hall of Fame.jpg]] are crops of this photo.

[[Category:Photographs of players]]
[[Category:Photographs]]""",
}
for f, d in FILES.items(): pages["File:" + f] = d

def addgal(t, before, lines, sec="== Photographs =="):
    """add lines to existing gallery in sec, or create section before `before`."""
    if sec in t:
        i = t.index(sec); j = t.index("</gallery>", i)
        return t[:j] + "\n".join(lines) + "\n" + t[j:]
    k = t.index(before)
    return t[:k] + sec + "\n<gallery>\n" + "\n".join(lines) + "\n</gallery>\n\n" + t[k:]

def inbox(t, img, cap):
    # insert or replace image row after the header row of the infobox
    lines = t.split("\n")
    row = f'| colspan="2" style="text-align:center;" | [[File:{img}|280px]]<br/><small>{cap}</small>'
    for i, l in enumerate(lines[:12]):
        if l.startswith('| colspan="2" style="text-align:center;" | [[File:'):
            lines[i] = row; return "\n".join(lines)
    for i, l in enumerate(lines[:5]):
        if l.startswith('! colspan="2" |'):
            lines[i+1:i+1] = ["|-", row]; return "\n".join(lines)
    raise SystemExit("no infobox")

R = "<ref name=\"pctrove{n}\">{c}</ref>"
# hubs
t = rd("2010 World Championship")
t = inbox(t, "Dan Kim 2010 World Championship.png", "Champion [[Dan Kim]] (right)")
t = addgal(t, "== See also ==", ["File:Dan Kim 2010 World Championship.png|[[Dan Kim]] (right), 2010 World Champion. Players Committee homepage banner."])
pages["2010 World Championship"] = t
t = rd("2013 World Championship")
t = inbox(t, "Justin Desai 2013 World Championship.jpg", "Champion [[Justin Desai]]")
t = addgal(t, "== See also ==", ["File:Justin Desai 2013 World Championship.jpg|[[Justin Desai]], 2013 World Champion. Players Committee homepage banner.",
    "File:2013 Hall of Fame inaugural class.jpg|The inaugural Hall of Fame class: [[Kevin Shannon]], [[Jonny Chu]], Justin Desai, [[Angelo Consoli]]"])
pages["2013 World Championship"] = t
t = rd("2014 World Championship")
t = inbox(t, "Emil Wallin and Brian Terwilliger 2014 World Championship.jpg", "Runner-up [[Brian Terwilliger]] (left) and champion [[Emil Wallin]] (right)")
t = addgal(t, "== See also ==", ["File:Emil Wallin and Brian Terwilliger 2014 World Championship.jpg|[[Brian Terwilliger]] (runner-up, left) and [[Emil Wallin]] (champion, right). Players Committee homepage banner."])
pages["2014 World Championship"] = t
t = rd("2015 World Championship")
t = inbox(t, "Justin Desai and Jonny Chu 2015 World Championship.jpg", "Runner-up [[Jonny Chu]] (left) and champion [[Justin Desai]] (right)")
t = addgal(t, "== See also ==", ["File:Justin Desai and Jonny Chu 2015 World Championship.jpg|[[Jonny Chu]] (runner-up, left) and [[Justin Desai]] (champion, right)"])
pages["2015 World Championship"] = t
# people
t = rd("Dan Kim")
t = "[[File:Dan Kim 2010 World Championship.png|thumb|right|300px|Dan Kim (right) after winning the [[2010 World Championship]].]]\n" + t
pages["Dan Kim"] = t
t = rd("Emil Wallin")
t = addgal(t, "== Community card ==", ["File:Emil Wallin and Brian Terwilliger 2014 World Championship.jpg|With runner-up [[Brian Terwilliger]] (left) after winning the [[2014 World Championship]]"])
pages["Emil Wallin"] = t
t = rd("Brian Terwilliger")
t = addgal(t, "== Miscellaneous decklists ==", ["File:Emil Wallin and Brian Terwilliger 2014 World Championship.jpg|Runner-up (left) at the [[2014 World Championship]], with champion [[Emil Wallin]]"])
pages["Brian Terwilliger"] = t
t = rd("Justin Desai")
t = addgal(t, "== Other games ==", ["File:Justin Desai 2013 World Championship.jpg|2013 World Champion",
    "File:Justin Desai and Jonny Chu 2015 World Championship.jpg|2015 World Champion (right), with runner-up [[Jonny Chu]]",
    "File:2013 Hall of Fame inaugural class.jpg|Third from left in the inaugural [[Hall of Fame]] class, 2013"])
pages["Justin Desai"] = t
t = rd("Jonny Chu")
t = addgal(t, "== Community card ==", ["File:Justin Desai and Jonny Chu 2015 World Championship.jpg|Runner-up (left) at the [[2015 World Championship]], with champion [[Justin Desai]]",
    "File:2013 Hall of Fame inaugural class.jpg|Second from left in the inaugural [[Hall of Fame]] class, 2013"])
pages["Jonny Chu"] = t
t = rd("Scott Lingrell")
t = addgal(t, "== Community card ==", ["File:Scott Lingrell Lifetime Achievement Award.png|With his Lifetime Achievement Award (2011)"])
pages["Scott Lingrell"] = t
t = rd("Steve Baroni")
t = "[[File:Steve Baroni 2012 Match Play Championship.jpg|thumb|right|300px|Steve Baroni, 2012 [[Match Play Championship]] champion (Players Committee banner).]]\n" + t
pages["Steve Baroni"] = t
for n in ["Kevin Shannon", "Angelo Consoli"]:
    pass
# 2012 MPC winner
t = rd("2012 Match Play Championship")
ref = '<ref name="mpcbanner">Players Committee homepage banner "Steve Baroni is the 2012 MPC Champion!", starwarsccg.org. Preserved copy: [https://web.archive.org/web/20120308225002/http://www.starwarsccg.org/ Internet Archive, 8 March 2012]; image [[:File:Steve Baroni 2012 Match Play Championship.jpg]].</ref>'
assert "* '''Winner:''' —" in t
t = t.replace("* '''Winner:''' —", "* '''Winner:''' [[Steve Baroni]]" + ref)
t = "[[File:Steve Baroni 2012 Match Play Championship.jpg|thumb|right|300px|Champion [[Steve Baroni]].]]\n" + t
pages["2012 Match Play Championship"] = t
# Hall of Fame
t = rd("Hall of Fame")
t = t.replace("== Inductees ==\n", "== Inductees ==\n[[File:2013 Hall of Fame inaugural class.jpg|thumb|right|300px|The inaugural class, 10 August 2013: [[Kevin Shannon]], [[Jonny Chu]], [[Justin Desai]], [[Angelo Consoli]].]]\n", 1)
t = t.replace("[[Scott Lingrell]] received one from the players in 2011.", "[[Scott Lingrell]] received one from the players in 2011 ([[:File:Scott Lingrell Lifetime Achievement Award.png|photo]]).", 1)
pages["Hall of Fame"] = t
rows = []
for k, v in pages.items():
    fn = re.sub(r"[^\w.-]+", "_", k) + ".wiki"; (P / fn).write_text(v)
    rows.append(f"{k}\tpages/{fn}")
pathlib.Path("pkg/all.tsv").write_text("\n".join(rows) + "\n")
print(len(rows))
