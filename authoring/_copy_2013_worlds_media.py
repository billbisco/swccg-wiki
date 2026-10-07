#!/usr/bin/env python3
from __future__ import annotations
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2013-events"
MEDIA = ROOT / "y2013-worlds-media"
MEDIA.mkdir(parents=True, exist_ok=True)

JOBS = [
    (SRC / "2013WorldsDay1.pdf", "2013 Worlds Day 1.pdf"),
    (SRC / "2013WorldsDay2.pdf", "2013 Worlds Day 2.pdf"),
    (SRC / "2013WorldsDay3.pdf", "2013 Worlds Day 3.pdf"),
    (
        SRC / "extract" / "worlds_d1_p01.png",
        "2013 Worlds Day 1 p01 Stephen Cellucci LS.png",
    ),
    (
        SRC / "extract" / "worlds_d1_p02.png",
        "2013 Worlds Day 1 p02 Stephen Cellucci DS.png",
    ),
    (
        SRC / "extract" / "worlds_d1_p03.png",
        "2013 Worlds Day 1 p03 Jeremy Gardner LS.png",
    ),
    (
        SRC / "extract" / "worlds_d1_p04.png",
        "2013 Worlds Day 1 p04 Jeremy Gardner DS.png",
    ),
    (
        SRC / "extract" / "worlds_d1_p05.png",
        "2013 Worlds Day 1 p05 Ross Littauer DS.png",
    ),
    (
        SRC / "extract" / "worlds_d1_p06.png",
        "2013 Worlds Day 1 p06 Ross Littauer LS.png",
    ),
    (
        SRC / "extract" / "worlds_d1_p11.png",
        "2013 Worlds Day 1 p11 Nathan Way LS.png",
    ),
    (
        SRC / "extract" / "worlds_d1_p12.png",
        "2013 Worlds Day 1 p12 Nathan Way DS.png",
    ),
    (
        SRC / "extract" / "worlds_d1_p07.png",
        "2013 Worlds Day 1 p07 Aaron Kia DS.png",
    ),
    (
        SRC / "extract" / "worlds_d1_p08.png",
        "2013 Worlds Day 1 p08 Aaron Kia LS.png",
    ),
    (
        SRC / "extract" / "worlds_d1_p09.png",
        "2013 Worlds Day 1 p09 Drew Powers LS.png",
    ),
    (
        SRC / "extract" / "worlds_d1_p10.png",
        "2013 Worlds Day 1 p10 Drew Powers DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p01.png",
        "2013 Worlds Day 2 p01 Seth Acree DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p02.png",
        "2013 Worlds Day 2 p02 Seth Acree LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p03.png",
        "2013 Worlds Day 2 p03 Barry Alperstein DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p04.png",
        "2013 Worlds Day 2 p04 Barry Alperstein LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p05.png",
        "2013 Worlds Day 2 p05 John Anderson LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p06.png",
        "2013 Worlds Day 2 p06 John Anderson DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p07.png",
        "2013 Worlds Day 2 p07 Casey Anis LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p09.png",
        "2013 Worlds Day 2 p09 Charles Arlandson LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p10.png",
        "2013 Worlds Day 2 p10 Charles Arlandson DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p11.png",
        "2013 Worlds Day 2 p11 Vikram Bali DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p12.png",
        "2013 Worlds Day 2 p12 Vikram Bali LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p08.png",
        "2013 Worlds Day 2 p08 Casey Anis DS.png",
    ),
    (
        SRC / "extract" / "worlds_d3_p04.png",
        "2013 Worlds Day 3 p04 Vikram Bali LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p13.png",
        "2013 Worlds Day 2 p13 Amar Banger DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p14.png",
        "2013 Worlds Day 2 p14 Amar Banger LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p15.png",
        "2013 Worlds Day 2 p15 Steve Baroni DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p16.png",
        "2013 Worlds Day 2 p16 Steve Baroni LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p17.png",
        "2013 Worlds Day 2 p17 Pär Birgander DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p18.png",
        "2013 Worlds Day 2 p18 Pär Birgander LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p19.png",
        "2013 Worlds Day 2 p19 Brandon Stern DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p20.png",
        "2013 Worlds Day 2 p20 Brandon Stern LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p21.png",
        "2013 Worlds Day 2 p21 Victor G. Brusca LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p22.png",
        "2013 Worlds Day 2 p22 Victor G. Brusca DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p23.png",
        "2013 Worlds Day 2 p23 Justin Carulli DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p24.png",
        "2013 Worlds Day 2 p24 Justin Carulli LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p25.png",
        "2013 Worlds Day 2 p25 Stephen Cellucci DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p26.png",
        "2013 Worlds Day 2 p26 Jonny Chu LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p27.png",
        "2013 Worlds Day 2 p27 Jonny Chu DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p28.png",
        "2013 Worlds Day 2 p28 Angelo Consoli DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p29.png",
        "2013 Worlds Day 2 p29 Angelo Consoli LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p30.png",
        "2013 Worlds Day 2 p30 Justin Desai DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p31.png",
        "2013 Worlds Day 2 p31 Justin Desai LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p32.png",
        "2013 Worlds Day 2 p32 Brian Fred DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p33.png",
        "2013 Worlds Day 2 p33 Brian Fred LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p34.png",
        "2013 Worlds Day 2 p34 Jeremy G LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p35.png",
        "2013 Worlds Day 2 p35 Jeremy G DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p36.png",
        "2013 Worlds Day 2 p36 Joe Giannetti DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p37.png",
        "2013 Worlds Day 2 p37 Joe Giannetti LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p38.png",
        "2013 Worlds Day 2 p38 Chris Gogolen LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p39.png",
        "2013 Worlds Day 2 p39 Chris Gogolen DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p40.png",
        "2013 Worlds Day 2 p40 Tom Haid LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p41.png",
        "2013 Worlds Day 2 p41 Tom Haid DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p42.png",
        "2013 Worlds Day 2 p42 Matthew Harrison-Trainor LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p43.png",
        "2013 Worlds Day 2 p43 Matthew Harrison-Trainor DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p44.png",
        "2013 Worlds Day 2 p44 Brian Herold LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p45.png",
        "2013 Worlds Day 2 p45 Brian Herold DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p46.png",
        "2013 Worlds Day 2 p46 Tom H LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p47.png",
        "2013 Worlds Day 2 p47 Tom H DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p48.png",
        "2013 Worlds Day 2 p48 Ryan Jellison DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p49.png",
        "2013 Worlds Day 2 p49 Ryan Jellison LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p50.png",
        "2013 Worlds Day 2 p50 Stephen Kin DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p51.png",
        "2013 Worlds Day 2 p51 Stephen Kin LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p52.png",
        "2013 Worlds Day 2 p52 Aaron Kinser DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p53.png",
        "2013 Worlds Day 2 p53 Aaron Kinser LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p54.png",
        "2013 Worlds Day 2 p54 Jack Koswicki DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p55.png",
        "2013 Worlds Day 2 p55 Jack Koswicki LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p56.png",
        "2013 Worlds Day 2 p56 Cole Lepine LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p57.png",
        "2013 Worlds Day 2 p57 Cole Lepine DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p58.png",
        "2013 Worlds Day 2 p58 Scott Lingrell DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p59.png",
        "2013 Worlds Day 2 p59 Scott Lingrell LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p60.png",
        "2013 Worlds Day 2 p60 Ross Littauer DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p61.png",
        "2013 Worlds Day 2 p61 Ross Littauer LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p62.png",
        "2013 Worlds Day 2 p62 Josh Mack LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p63.png",
        "2013 Worlds Day 2 p63 Josh Mack DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p64.png",
        "2013 Worlds Day 2 p64 Chris Menzel DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p65.png",
        "2013 Worlds Day 2 p65 Chris Menzel LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p66.png",
        "2013 Worlds Day 2 p66 Aaron Nelson LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p67.png",
        "2013 Worlds Day 2 p67 Aaron Nelson DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p68.png",
        "2013 Worlds Day 2 p68 Jake Nelson DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p69.png",
        "2013 Worlds Day 2 p69 Jake Nelson LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p70.png",
        "2013 Worlds Day 2 p70 Mitch Wieland LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p71.png",
        "2013 Worlds Day 2 p71 Mitch Wieland DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p72.png",
        "2013 Worlds Day 2 p72 Matt Paragano DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p73.png",
        "2013 Worlds Day 2 p73 Matt Paragano LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p74.png",
        "2013 Worlds Day 2 p74 Pistone LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p75.png",
        "2013 Worlds Day 2 p75 Pistone DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p76.png",
        "2013 Worlds Day 2 p76 Drew Powers DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p77.png",
        "2013 Worlds Day 2 p77 Drew Powers LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p78.png",
        "2013 Worlds Day 2 p78 Nick Reisch LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p79.png",
        "2013 Worlds Day 2 p79 Nick Reisch DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p80.png",
        "2013 Worlds Day 2 p80 Mike Richards DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p81.png",
        "2013 Worlds Day 2 p81 Mike Richards LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p83.png",
        "2013 Worlds Day 2 p83 Schwartz DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p84.png",
        "2013 Worlds Day 2 p84 Schwartz LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p85.png",
        "2013 Worlds Day 2 p85 Greg Shaw DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p86.png",
        "2013 Worlds Day 2 p86 Greg Shaw LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p87.png",
        "2013 Worlds Day 2 p87 Steve Skilton DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p88.png",
        "2013 Worlds Day 2 p88 Steve Skilton LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p89.png",
        "2013 Worlds Day 2 p89 RSmith LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p90.png",
        "2013 Worlds Day 2 p90 RSmith DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p91.png",
        "2013 Worlds Day 2 p91 Matt Sokol DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p92.png",
        "2013 Worlds Day 2 p92 Matt Sokol LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p93.png",
        "2013 Worlds Day 2 p93 Conrad Simmering LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p94.png",
        "2013 Worlds Day 2 p94 Conrad Simmering DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p95.png",
        "2013 Worlds Day 2 p95 Nicholas Tobin DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p96.png",
        "2013 Worlds Day 2 p96 Nicholas Tobin LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p97.png",
        "2013 Worlds Day 2 p97 Chris Twigg LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p98.png",
        "2013 Worlds Day 2 p98 Chris Twigg DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p99.png",
        "2013 Worlds Day 2 p99 VeeZ DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p100.png",
        "2013 Worlds Day 2 p100 VeeZ LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p101.png",
        "2013 Worlds Day 2 p101 Micah Wall DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p102.png",
        "2013 Worlds Day 2 p102 Micah Wall LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p103.png",
        "2013 Worlds Day 2 p103 Nathan Wall LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p104.png",
        "2013 Worlds Day 2 p104 Nathan Way DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p105.png",
        "2013 Worlds Day 2 p105 Stu Wall LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p106.png",
        "2013 Worlds Day 2 p106 Stu Wall DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p107.png",
        "2013 Worlds Day 2 p107 Emil Wallin LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p108.png",
        "2013 Worlds Day 2 p108 Emil Wallin DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p109.png",
        "2013 Worlds Day 2 p109 Walseth DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p110.png",
        "2013 Worlds Day 2 p110 Walseth LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p111.png",
        "2013 Worlds Day 2 p111 Ryan Washeleski DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p112.png",
        "2013 Worlds Day 2 p112 Ryan Washeleski LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p113.png",
        "2013 Worlds Day 2 p113 Chris Westergard LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p114.png",
        "2013 Worlds Day 2 p114 Chris Westergard DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p115.png",
        "2013 Worlds Day 2 p115 Thomas Whaley LS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p116.png",
        "2013 Worlds Day 2 p116 Thomas Whaley DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p117.png",
        "2013 Worlds Day 2 p117 Chris Wirfs DS.png",
    ),
    (
        SRC / "extract" / "worlds_d2_p118.png",
        "2013 Worlds Day 2 p118 Chris Wirfs LS.png",
    ),
    (
        SRC / "extract" / "worlds_d3_p01.png",
        "2013 Worlds Day 3 p01 Steve Baroni DS.png",
    ),
    (
        SRC / "extract" / "worlds_d3_p02.png",
        "2013 Worlds Day 3 p02 Steve Baroni LS.png",
    ),
    (
        SRC / "extract" / "worlds_d3_p05.png",
        "2013 Worlds Day 3 p05 Jonny Chu DS.png",
    ),
    (
        SRC / "extract" / "worlds_d3_p06.png",
        "2013 Worlds Day 3 p06 Jonny Chu LS.png",
    ),
    (
        SRC / "extract" / "worlds_d3_p07.png",
        "2013 Worlds Day 3 p07 Justin Desai DS.png",
    ),
    (
        SRC / "extract" / "worlds_d3_p08.png",
        "2013 Worlds Day 3 p08 Justin Desai LS.png",
    ),
    (
        SRC / "extract" / "worlds_d3_p11.png",
        "2013 Worlds Day 3 p11 Kevin Shannon DS.png",
    ),
    (
        SRC / "extract" / "worlds_d3_p12.png",
        "2013 Worlds Day 3 p12 Kevin Shannon LS.png",
    ),
    (
        SRC / "extract" / "worlds_d3_p13.png",
        "2013 Worlds Day 3 p13 Reid Smith LS.png",
    ),
    (
        SRC / "extract" / "worlds_d3_p14.png",
        "2013 Worlds Day 3 p14 Reid Smith DS.png",
    ),
    (
        SRC / "extract" / "worlds_d3_p15.png",
        "2013 Worlds Day 3 p15 Emil Wallin LS.png",
    ),
    (
        SRC / "extract" / "worlds_d3_p16.png",
        "2013 Worlds Day 3 p16 Emil Wallin DS.png",
    ),
]
for src, name in JOBS:
    dest = MEDIA / name
    if not src.exists():
        raise SystemExit(f"missing {src}")
    shutil.copy2(src, dest)
    print("copy", dest.name, dest.stat().st_size)
print("DONE", MEDIA)
