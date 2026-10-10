#!/usr/bin/env python3
"""Dest Game Players Network user-submitted 60s (start at listing page 63, oldest first)."""
from __future__ import annotations

import html as htmlmod
import re
import sys
from collections import defaultdict
from pathlib import Path

from generate_decipher_designs import (
    DARK_SHARED,
    OBJ_FACE,
    TYPE_ORDER,
    infer_start,
    table_from_cards,
    wiki_card,
)
from generate_decipher_worlds import CATS, PAGES, TITLES, slug_file, write_page
from gemp_importable import (
    deck_name,
    load_cards,
    lookup,
    safe_deck_filename,
    set_num,
    wiki_download_line,
    xml_for,
)

ROOT = Path(__file__).resolve().parent
CACHE = ROOT / "gpn-decks"
GEMP_OUT = ROOT / "gemp-import-gpn"
HUB = "Game Players Network decks"
INDEX_TS = "20050430203312"
DETAIL_TS = "20051102154456"


def listing_url(page: int) -> str:
    return (
        f"https://web.archive.org/web/{INDEX_TS}/"
        f"http://gameplayersnetwork.com/card/decks.asp?gm=starwars&ord=&pg={page}"
    )


INDEX_URL = listing_url(63)
DETAIL_URL = (
    "https://web.archive.org/web/"
    + DETAIL_TS
    + "/http://gameplayersnetwork.com/card/decks.asp?gm=starwars&id={id}"
)

# Oldest remaining GPN listing first (page 63), then walk backward.
PAGE63_IDS = [29, 40, 54, 56, 57, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 70]
PAGE62_IDS = [
    78, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 101, 102,
    118, 119, 120, 122, 123,
]
PAGE61_IDS = [
    128, 130, 137, 138, 139, 140, 141, 142, 143, 145,
    146, 147, 150, 154, 155, 158, 159, 161, 170, 171,
]
PAGE60_IDS = [
    172, 173, 174, 175, 177, 178, 179, 180, 186, 187,
    188, 189, 190, 192, 193, 194, 198, 199, 200, 202,
]
PAGE59_IDS = [
    203, 207, 208, 210, 211, 213, 214, 220, 225, 236,
    238, 239, 241, 244, 264, 278, 294, 296, 299, 300,
]
PAGE58_IDS = [
    301, 305, 310, 314, 320, 328, 333, 351, 355, 364,
    370, 372, 373, 396, 454, 455, 456, 472, 481,
]
PAGE57_IDS = [
    486, 490, 491, 492, 500, 522, 533, 591, 594, 596,
    600, 772, 805, 954, 1060, 1123, 1124, 1165, 1257, 1289,
]
PAGE56_IDS = [
    1325, 1335, 1403, 1404, 1445, 1448, 1517, 1553, 1578, 1585,
    1591, 1599, 1600, 1601, 1602, 1603, 1604, 1605, 1607, 1608,
]
PAGE55_IDS = [
    1612, 1621, 1622, 1635, 1637, 1639, 1645, 1646, 1661, 1670,
    1672, 1676, 1699, 1710, 1711, 1716, 1725, 1735, 1737, 1766,
]
PAGE54_IDS = [
    1787, 1788, 1796, 1797, 1799, 1800, 1808, 1819, 1820, 1821,
    1831, 1833, 1834, 1836, 1916, 1931, 1957, 1980, 1984, 1989,
]
PAGE53_IDS = [
    2032, 2049, 2052, 2054, 2055, 2057, 2063, 2076, 2086, 2087,
    2089, 2098, 2108, 2114, 2116, 2130, 2148, 2155, 2156, 2161,
]
PAGE52_IDS = [
    2176, 2177, 2180, 2181, 2207, 2217, 2224, 2237, 2244, 2245,
    2261, 2262, 2266, 2271, 2275, 2276, 2278, 2279, 2281, 2288,
]
PAGE51_IDS = [
    2306, 2321, 2322, 2342, 2348, 2349, 2350, 2353, 2361, 2400,
    2401, 2404, 2435, 2447, 2449, 2454, 2474, 2484, 2501, 2503,
]
PAGE50_IDS = [
    2513, 2521, 2529, 2542, 2548, 2559, 2565, 2566, 2567, 2568,
    2575, 2580, 2583, 2584, 2585, 2587, 2603, 2614, 2615, 2625,
]
PAGE49_IDS = [
    2628, 2630, 2632, 2634, 2636, 2641, 2644, 2649, 2651, 2653,
    2655, 2657, 2661, 2662, 2663, 2664, 2665, 2669, 2671, 2673,
]
PAGE48_IDS = [
    2674, 2675, 2676, 2679, 2695, 2701, 2705, 2713, 2715, 2728,
    2729, 2730, 2732, 2733, 2745, 2748, 2754, 2756, 2765, 2766,
]
PAGE47_IDS = [
    2769, 2771, 2772, 2783, 2785, 2789, 2803, 2811, 2830, 2843,
    2849, 2850, 2851, 2854, 2857, 2870, 2874, 2880, 2881, 2907,
]
PAGE46_IDS = [
    2909, 2929, 2931, 2933, 2947, 2953, 2969, 2976, 2981, 2982,
    2984, 3003, 3004, 3010, 3017, 3025, 3027, 3028, 3036, 3037,
]
PAGE45_IDS = [
    3041, 3043, 3045, 3046, 3052, 3053, 3060, 3068, 3071, 3072,
    3076, 3079, 3080, 3081, 3082, 3084, 3085, 3088, 3089, 3102,
]
PAGE44_IDS = [
    3107, 3108, 3109, 3120, 3121, 3123, 3131, 3132, 3134, 3143,
    3150, 3151, 3154, 3155, 3156, 3165, 3166, 3167, 3180, 3186,
]
PAGE43_IDS = [
    3188, 3189, 3192, 3193, 3195, 3196, 3201, 3202, 3204, 3205,
    3208, 3209, 3210, 3213, 3216, 3222, 3225, 3226, 3228, 3229,
]
PAGE42_IDS = [
    3236, 3238, 3241, 3255, 3259, 3263, 3265, 3267, 3268, 3270,
    3274, 3281, 3282, 3283, 3287, 3293, 3295, 3296, 3298, 3300,
]
PAGE41_IDS = [
    3301, 3309, 3312, 3313, 3314, 3315, 3317, 3321, 3322, 3326,
    3332, 3334, 3336, 3348, 3349, 3353, 3355, 3360, 3361, 3365,
]
PAGE40_IDS = [
    3368, 3369, 3370, 3373, 3375, 3377, 3378, 3381, 3385, 3390,
    3391, 3392, 3393, 3395, 3405, 3406, 3408, 3412, 3414, 3415,
]
PAGE39_IDS = [
    3416, 3435, 3438, 3441, 3446, 3448, 3457, 3467, 3473, 3474,
    3475, 3476, 3480, 3482, 3485, 3486, 3490, 3491, 3500, 3501,
]
PAGE38_IDS = [
    3510, 3511, 3525, 3526, 3532, 3539, 3544, 3551, 3552, 3553,
    3567, 3573, 3578, 3582, 3583, 3584, 3585, 3586, 3593, 3594,
]
PAGE37_IDS = [
    3599, 3607, 3618, 3619, 3620, 3634, 3641, 3648, 3650, 3651,
    3652, 3653, 3657, 3658, 3659, 3663, 3664, 3665, 3666, 3670,
]
PAGE36_IDS = [
    3675, 3676, 3679, 3680, 3681, 3682, 3691, 3693, 3694, 3695,
    3701, 3702, 3703, 3704, 3705, 3706, 3707, 3720, 3721, 3727,
]
PAGE35_IDS = [
    3729, 3731, 3736, 3740, 3742, 3744, 3748, 3750, 3755, 3756,
    3757, 3760, 3765, 3769, 3771, 3773, 3782, 3786, 3790, 3804,
]
PAGE34_IDS = [
    3808, 3809, 3816, 3819, 3825, 3826, 3829, 3833, 3835, 3836,
    3839, 3840, 3841, 3843, 3844, 3845, 3850, 3854, 3855, 3858,
]
PAGE33_IDS = [
    3859, 3860, 3861, 3862, 3865, 3866, 3867, 3868, 3874, 3875,
    3876, 3877, 3884, 3890, 3891, 3897, 3902, 3905, 3906, 3907,
]
PAGE32_IDS = [
    3911, 3917, 3920, 3922, 3926, 3927, 3928, 3929, 3933, 3934,
    3935, 3940, 3941, 3949, 3952, 3962, 3964, 3967, 3968, 3969,
]
PAGE31_IDS = [
    3970, 3971, 3973, 3974, 3978, 3982, 3984, 3986, 3987, 3988,
    3991, 3992, 3993, 3998, 3999, 4000, 4004, 4025, 4026, 4028,
]
PAGE30_IDS = [
    4031, 4033, 4034, 4035, 4038, 4040, 4046, 4053, 4054, 4055,
    4058, 4061, 4068, 4072, 4080, 4087, 4089, 4091, 4093, 4102,
]
PAGE29_IDS = [
    4107, 4108, 4112, 4119, 4120, 4125, 4131, 4134, 4147, 4149,
    4155, 4156, 4157, 4163, 4164, 4169, 4171, 4172, 4175, 4176,
]
PAGE28_IDS = [
    4183, 4187, 4191, 4196, 4197, 4199, 4206, 4210, 4211, 4212,
    4213, 4229, 4237, 4240, 4243, 4248, 4249, 4253, 4254, 4258,
]
PAGE27_IDS = [
    4262, 4263, 4264, 4265, 4266, 4267, 4269, 4270, 4271, 4272,
    4273, 4274, 4275, 4276, 4277, 4278, 4280, 4282, 4285, 4286,
]
PAGE26_IDS = [
    4287, 4288, 4289, 4290, 4292, 4293, 4294, 4298, 4299, 4302,
    4303, 4304, 4308, 4309, 4312, 4313, 4317, 4319, 4321, 4328,
]
PAGE25_IDS = [
    4329, 4330, 4331, 4333, 4335, 4336, 4338, 4340, 4342, 4343,
    4346, 4349, 4351, 4352, 4353, 4356, 4362, 4363, 4364, 4365,
]
PAGE24_IDS = [
    4367, 4368, 4369, 4370, 4376, 4380, 4383, 4390, 4396, 4397,
    4402, 4403, 4404, 4405, 4407, 4410, 4420, 4423, 4432, 4443,
]
PAGE23_IDS = [
    4445, 4446, 4448, 4450, 4453, 4454, 4456, 4458, 4459, 4460,
    4462, 4463, 4465, 4473, 4475, 4477, 4483, 4485, 4486, 4487,
]
PAGE22_IDS = [
    4489, 4492, 4493, 4495, 4498, 4501, 4507, 4511, 4515, 4519,
    4524, 4525, 4534, 4535, 4540, 4544, 4545, 4546, 4547, 4548,
]
PAGE21_IDS = [
    4557, 4558, 4559, 4569, 4573, 4575, 4623, 4624, 4626, 4628,
    4631, 4632, 4639, 4640, 4641, 4642, 4643, 4644, 4645, 4646,
]
PAGE20_IDS = [
    4648, 4651, 4654, 4656, 4658, 4661, 4667, 4672, 4673, 4691,
    4692, 4694, 4700, 4718, 4729, 4734, 4739, 4740, 4748, 4749,
]
PAGE19_IDS = [
    4756, 4775, 4785, 4796, 4797, 4800, 4805, 4806, 4807, 4808,
    4809, 4810, 4811, 4812, 4813, 4818, 4828, 4829, 4832, 4833,
]
PAGE18_IDS = [
    4834, 4835, 4841, 4842, 4844, 4860, 4861, 4879, 4886, 4887,
    4895, 4898, 4901, 4902, 4903, 4906, 4907, 4908, 4914, 4915,
]
PAGE17_IDS = [
    4960, 4961, 4968, 4971, 4973, 4974, 4979, 4980, 4988, 4989,
    4990, 4991, 4997, 5000, 5003, 5008, 5012, 5013, 5015, 5021,
]
PAGE16_IDS = [
    5032, 5036, 5037, 5039, 5040, 5041, 5042, 5047, 5051, 5053,
    5054, 5055, 5063, 5064, 5066, 5067, 5068, 5069, 5070, 5071,
]
PAGE15_IDS = [
    5072, 5075, 5076, 5080, 5081, 5089, 5094, 5095, 5096, 5100,
    5102, 5104, 5105, 5108, 5109, 5112, 5113, 5114, 5115, 5117,
]
PAGE14_IDS = [
    5119, 5122, 5124, 5125, 5130, 5132, 5135, 5140, 5141, 5145,
    5147, 5149, 5150, 5153, 5162, 5164, 5165, 5167, 5168, 5169,
]
PAGE13_IDS = [
    5170, 5176, 5177, 5178, 5179, 5180, 5183, 5184, 5194, 5196,
    5197, 5199, 5202, 5214, 5216, 5222, 5227, 5236, 5237,
]
PAGE_IDS = {
    63: PAGE63_IDS,
    62: PAGE62_IDS,
    61: PAGE61_IDS,
    60: PAGE60_IDS,
    59: PAGE59_IDS,
    58: PAGE58_IDS,
    57: PAGE57_IDS,
    56: PAGE56_IDS,
    55: PAGE55_IDS,
    54: PAGE54_IDS,
    53: PAGE53_IDS,
    52: PAGE52_IDS,
    51: PAGE51_IDS,
    50: PAGE50_IDS,
    49: PAGE49_IDS,
    48: PAGE48_IDS,
    47: PAGE47_IDS,
    46: PAGE46_IDS,
    45: PAGE45_IDS,
    44: PAGE44_IDS,
    43: PAGE43_IDS,
    42: PAGE42_IDS,
    41: PAGE41_IDS,
    40: PAGE40_IDS,
    39: PAGE39_IDS,
    38: PAGE38_IDS,
    37: PAGE37_IDS,
    36: PAGE36_IDS,
    35: PAGE35_IDS,
    34: PAGE34_IDS,
    33: PAGE33_IDS,
    32: PAGE32_IDS,
    31: PAGE31_IDS,
    30: PAGE30_IDS,
    29: PAGE29_IDS,
    28: PAGE28_IDS,
    27: PAGE27_IDS,
    26: PAGE26_IDS,
    25: PAGE25_IDS,
    24: PAGE24_IDS,
    23: PAGE23_IDS,
    22: PAGE22_IDS,
    21: PAGE21_IDS,
    20: PAGE20_IDS,
    19: PAGE19_IDS,
    18: PAGE18_IDS,
    17: PAGE17_IDS,
    16: PAGE16_IDS,
    15: PAGE15_IDS,
    14: PAGE14_IDS,
    13: PAGE13_IDS,
}
ID_TO_PAGE = {did: pg for pg, ids in PAGE_IDS.items() for did in ids}

# GPN handle as published. Signed names stay on the stub as aliases.
HANDLE_NOTE = {
    "Lancer4life": "The GPN lists are signed David Jones",
    "Compulsion": "The GPN list is signed Matthew",
}

# Bare handle collides with a live {{Card}} title. Dest the player as {handle} (GPN).
HANDLE_PAGE = {
    "Bravo 3": "Bravo 3 (GPN)",
    "yoda": "Yoda (GPN)",
    "Yoda": "Yoda (GPN)",
    "Elis Helrot": "Elis Helrot (GPN)",
    "icebreath": "David Kangas",
    "Icebreath": "David Kangas",
    "Wedge231": "Chris Wodicka",
    "Exar Kun": "Exar Kun (GPN)",
    "Aves": "Aves (GPN)",
}

# Duplicate published title on the same handle (pg=26 4287/4288).
WIKI_TITLE_SUFFIX = {
    4288: " (4288)",
    5012: " (5012)",
}

# Original Virtual Set 1 slips (2002 PDF). Wiki dest matches 2002 Worlds, not current V21.
ORIGINAL_VS = {
    "Blaster Rack (V)": ("EFFECT", "Blaster Rack (V) (Virtual Set 1)"),
    "Darth Vader (V)": ("CHARACTER", "Darth Vader (V) (Virtual Set 1)"),
    "Prophetess (V)": ("CHARACTER", "Prophetess (V) (Virtual Set 1)"),
    "Luke Skywalker (V)": ("CHARACTER", "Luke Skywalker (V) (Virtual Set 1)"),
    "Bo Shek (V)": ("CHARACTER", "Bo Shek (V) (Virtual Set 1)"),
    "Fusion Generator Supply Tanks (V)": ("DEVICE", None),
    "Sai'torr Kal Fas (V)": ("EFFECT", "Sai'torr Kal Fas (V) (Virtual Set 1)"),
    "Han's Heavy Blaster Pistol (V)": (
        "WEAPON",
        "Han's Heavy Blaster Pistol (V) (Virtual Set 1)",
    ),
    "Black 2 (V)": ("STARSHIP", "Black 2 (V) (Virtual Set 1)"),
    "Gold 1 (V)": ("STARSHIP", "Gold 1 (V) (Virtual Set 1)"),
    "Assault Rifle (V)": ("WEAPON", "Assault Rifle (V) (Virtual Set 1)"),
    "BoShek (V)": ("CHARACTER", "Bo Shek (V) (Virtual Set 1)"),
    "General Tagge (V)": ("CHARACTER", "General Tagge (V) (Virtual Set 2)"),
    "Admiral Motti (V)": ("CHARACTER", "Admiral Motti (V) (Virtual Set 2)"),
    "Kitik Keed Kak (V)": ("CHARACTER", "Kitik Keed'kak (V) (Virtual Set 2)"),
    "Kitik Keed'kak (V)": ("CHARACTER", "Kitik Keed'kak (V) (Virtual Set 2)"),
    "Commander Praji (V)": ("CHARACTER", "Commander Praji (V) (Virtual Set 2)"),
    "Death Star Sentry (V)": ("EFFECT", "Death Star Sentry (V) (Virtual Set 2)"),
    "The Empire's Back (V)": ("INTERRUPT", "The Empire's Back (V) (Virtual Set 2)"),
    "We're All Gonna Be A Lot Thinner! (V)": (
        "INTERRUPT",
        "We're All Gonna Be A Lot Thinner! (V) (Virtual Set 2)",
    ),
    "Molator (V)": ("EFFECT", "Molator (V) (Virtual Set 2)"),
    "Imperial-Class Star Destroyer (V)": (
        "STARSHIP",
        "Imperial-Class Star Destroyer (V) (Virtual Set 2)",
    ),
    "Imperial-class Star Destroyer (V)": (
        "STARSHIP",
        "Imperial-Class Star Destroyer (V) (Virtual Set 2)",
    ),
    "I Find Your Lack Of Faith Disturbing (V)": (
        "EFFECT",
        "I Find Your Lack Of Faith Disturbing (V) (Virtual Set 2)",
    ),
    "Stormtrooper (V)": ("CHARACTER", "Stormtrooper (V) (Virtual Set 2)"),
    "Escape Pod (V)": ("INTERRUPT", "Escape Pod (V) (Virtual Set 2)"),
    "Leia's Back (V)": ("INTERRUPT", "Leia's Back (V) (Virtual Set 2)"),
    "Tarkin (V)": ("CHARACTER", "Tarkin (V) (Virtual Set 3)"),
    "Merc Sunlet (V)": ("EFFECT", "Merc Sunlet (V) (Virtual Set 3)"),
    "A Tremor In The Force (V)": ("EFFECT", "A Tremor In The Force (V) (Virtual Set 2)"),
    "Advance Preparation (V)": ("INTERRUPT", "Advance Preparation (V) (Virtual Set 3)"),
    "Rebel Tech (V)": ("CHARACTER", "Rebel Tech (V) (Virtual Set 3)"),
    "General Dodonna (V)": ("CHARACTER", "General Dodonna (V) (Virtual Set 2)"),
    "For Luck (V)": ("EFFECT", "For Luck (V) (Virtual Set 3)"),
    "Chewbacca (V)": ("CHARACTER", "Chewbacca (V) (Virtual Set 3)"),
    "R2-D2 (V)": ("CHARACTER", "R2-D2 (Artoo-Detoo) (V) (Virtual Set 3)"),
    "R2-D2 (Artoo-Detoo) (V)": (
        "CHARACTER",
        "R2-D2 (Artoo-Detoo) (V) (Virtual Set 3)",
    ),
    "Red 5 (V)": ("STARSHIP", "Red 5 (V) (Virtual Set 3)"),
    "Sabotage (V)": ("INTERRUPT", "Sabotage (V) (Virtual Set 3)"),
    "Wokling (V)": ("EFFECT", "Wokling (V) (Virtual Set 3)"),
    "Solomahal (V)": ("EFFECT", "Solomahal (V) (Virtual Set 3)"),
    "Cantina Brawl (V)": ("INTERRUPT", "Cantina Brawl (V) (Virtual Set 2)"),
    "K'lor'slug (V)": ("EFFECT", "K'lor'slug (V) (Virtual Set 2)"),
    "Rycar Ryjerd (V)": ("EFFECT", "Rycar Ryjerd (V) (Virtual Set 2)"),
    "Rebel Reinforcements (V)": (
        "INTERRUPT",
        "Rebel Reinforcements (V) (Virtual Set 2)",
    ),
    "Djas Puhr (V)": ("CHARACTER", "Djas Puhr (V) (Virtual Set 2)"),
    "Return Of A Jedi (V)": ("INTERRUPT", "Return Of A Jedi (V) (Virtual Set 2)"),
    "Return of a Jedi (V)": ("INTERRUPT", "Return Of A Jedi (V) (Virtual Set 2)"),
    "Return of the Jedi (V)": ("INTERRUPT", "Return Of A Jedi (V) (Virtual Set 2)"),
    "Han's Back (V)": ("INTERRUPT", "Han's Back (V) (Virtual Set 2)"),
    "Luke's Back (V)": ("INTERRUPT", "Luke's Back (V) (Virtual Set 2)"),
    "Yavin Sentry (V)": ("EFFECT", "Yavin Sentry (V) (Virtual Set 2)"),
    "Yavin 4 Sentry (V)": ("EFFECT", "Yavin Sentry (V) (Virtual Set 2)"),
    "Affect Mind (V)": ("EFFECT", "Affect Mind (V) (Virtual Set 2)"),
    "Cell 2187 (V)": ("EFFECT", "Cell 2187 (V) (Virtual Set 3)"),
    "Commander Vanden Willard (V)": (
        "CHARACTER",
        "Commander Vanden Willard (V) (Virtual Set 3)",
    ),
    "Leia's Sporting Blaster (V)": (
        "WEAPON",
        "Leia's Sporting Blaster (V) (Virtual Set 3)",
    ),
    "Logistical Delay (V)": ("EFFECT", "Logistical Delay (V) (Virtual Set 3)"),
    "A Disturbance In The Force (V)": (
        "EFFECT",
        "A Disturbance In The Force (V) (Virtual Set 3)",
    ),
    "Leia (V)": ("CHARACTER", "Leia (V) (Virtual Set 3)"),
    "Grand Moff Tarkin (V)": ("CHARACTER", "Tarkin (V) (Virtual Set 3)"),
    "Oo-ta Goo-ta, Solo? (V)": (
        "INTERRUPT",
        "Oo-ta Goo-ta, Solo? (V) (Virtual Set 3)",
    ),
    "Tarkin (V)": ("CHARACTER", "Tarkin (V) (Virtual Set 3)"),
    "Greedo (V)": ("CHARACTER", "Greedo (V) (Virtual Set 3)"),
    "Dannik Jerriko (V)": ("CHARACTER", "Dannik Jerriko (V) (Virtual Set 3)"),
    "Ket Maliss (V)": ("EFFECT", "Ket Maliss (V) (Virtual Set 3)"),
    "Reegesk (V)": ("CHARACTER", "Reegesk (V) (Virtual Set 3)"),
    "Labria (V)": ("CHARACTER", "Labria (V) (Virtual Set 2)"),
    "Bantha (V)": ("VEHICLE", "Bantha (V) (Virtual Set 2)"),
    "Imperial Reinforcements (V)": (
        "INTERRUPT",
        "Imperial Reinforcements (V) (Virtual Set 2)",
    ),
    "Sunsdown (V)": ("EFFECT", "Sunsdown (V) (Virtual Set 2)"),
    "They're On Dantooine (V)": (
        "EFFECT",
        "They're On Dantooine (V) (Virtual Set 3)",
    ),
    "Rebel Trooper (V)": ("CHARACTER", "Rebel Trooper (V) (Virtual Set 2)"),
    "Undercover (V)": ("EFFECT", None),
}
CLONE_PAGES = Path(r"C:\Users\gythe\.grok\swccg-wiki\pages")

MONTHS = [
    "",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

# Newest printed set in the list -> encyclopedia format + GEMP pool.
# GEMP printed-set prefixes (ignore 100+ premiums / virtual when dating the pool).
SET_FORMAT = [
    (14, "Premiere - Reflections III", "open_no_virtual"),
    (13, "Premiere - Theed Palace", "open_no_virtual"),
    (12, "Premiere - Coruscant", "open_no_virtual"),
    (11, "Premiere - Tatooine", "premiere_tatooine"),
    (10, "Premiere - Reflections II", "premiere_ref2"),
    (9, "Premiere - Death Star II", "premiere_ds2"),
    (8, "Premiere - Endor", "premiere_endor"),
    (7, "Premiere - Special Edition", "premiere_se"),
]

GPN_ALIAS = {
    "Hidden Base/Systems Will Slip Through Your Fingers": "Hidden Base",
    "Do or Do Not/Wise Advice": "Do, Or Do Not & Wise Advice",
    "Do Or Do Not/Wise Advice": "Do, Or Do Not & Wise Advice",
    "Grimtaash/Shocking Information": "Grimtaash & Shocking Information",
    "Hunt Down and Destroy the Jedi/Their Fire has gone out of the Universe": (
        "Hunt Down And Destroy The Jedi"
    ),
    "Hunt Down And Destroy The Jedi/Their Fire Has Gone Out Of The Universe": (
        "Hunt Down And Destroy The Jedi"
    ),
    "you can either profit by this...or be destroyed": (
        "You Can Either Profit By This… Or Be Destroyed"
    ),
    "My Lord Is That Legal/ I Will Make It Legal": "My Lord, Is That Legal?",
    "My Lord Is That Legal/I Will Make It Legal": "My Lord, Is That Legal?",
    "Battle Order & First strike": "Battle Order & First Strike",
    "Imperial Arrest Order & Secret Plans": "Imperial Arrest Order & Secret Plans",
    "Insurrection & aim high": "Insurrection & Aim High",
    "insurrection & aim high": "Insurrection & Aim High",
    "your insight seerves you well & staging areas": (
        "Your Insight Serves You Well & Staging Areas"
    ),
    "Clack'Dor VII": "Clak'dor VII",
    "Clack&#39;Dor VII": "Clak'dor VII",
    "Wed Bantha Droid": "WED-9-M1 'Bantha' Droid",
    "WED-15-77": "WED-9-M1 'Bantha' Droid",
    "Polarized Negative Power Couplings": "Polarized Negative Power Coupling",
    "Grimtaash/Shocking Information": "Shocking Information & Grimtaash",
    "Grimtaash & Shocking Information": "Shocking Information & Grimtaash",
    "you can either profit by this...or be destroyed": "You Can Either Profit By This...",
    "You Can Either Profit By This… Or Be Destroyed": "You Can Either Profit By This...",
    "You Can Either Profit By This... Or Be Destroyed": "You Can Either Profit By This...",
    "This Is Outrageous": "This Is Outrageous!",
    "Blow / Parried": "Blow Parried",
    "Blow Parried": "Blow Parried",
    "Uh Oh!": "Uh-oh!",
    "Uh Oh": "Uh-oh!",
    "WYS": "Watch Your Step",
    "Hunt Down": "Hunt Down And Destroy The Jedi",
    "DB 94": "Tatooine: Docking Bay 94",
    "Heading": "Heading For The Medical Frigate",
    "Luke JK": "Luke Skywalker, Jedi Knight",
    "Luke Skywalker, JK": "Luke Skywalker, Jedi Knight",
    "Chewie, Enraged": "Chewie, Enraged",
    "OOC & TT": "Out Of Commission & Transmission Terminated",
    "Out of Commisssion & Transmission Terminated": "Out Of Commission & Transmission Terminated",
    "Sorry About the Mess & Blaster P": "Sorry About The Mess & Blaster Proficiency",
    "Sprry about the Mess & Blaster Proficiency": "Sorry About The Mess & Blaster Proficiency",
    "Hooujix": "Houjix",
    "DVDLOTS": "Darth Vader, Dark Lord Of The Sith",
    "DLOTS": "Darth Vader, Dark Lord Of The Sith",
    "GMT": "Grand Moff Tarkin",
    "U-3P0": "U-3PO (Yoo-Threepio)",
    "U-3PO": "U-3PO (Yoo-Threepio)",
    "Holotheatre": "Executor: Holotheatre",
    "Med Chamber": "Executor: Meditation Chamber",
    "Watto Box": "Watto's Box",
    "Start Your Engines": "Start Your Engines!",
    "Agents of the Black Sun": "Agents Of Black Sun",
    "Black Sun Scum": "Agents Of Black Sun",
    "Tatooine: JP": "Tatooine: Jabba's Palace",
    "JP: AC": "Jabba's Palace: Audience Chamber",
    "JP: LC": "Jabba's Palace: Audience Chamber",
    "Tatooine: DB": "Tatooine: Docking Bay 94",
    "We'll Handle This/Duel Of The Fates": "We'll Handle This",
    "Naboo: TP Generator": "Naboo: Theed Palace Generator",
    "Naboo: TP Generator Core": "Naboo: Theed Palace Generator Core",
    "Naboo: TP Throne Room": "Naboo: Theed Palace Throne Room",
    "Threepio, Naked": "Threepio With His Parts Showing",
    "Threepeo With His Parts Showing": "Threepio With His Parts Showing",
    "threepio w/ his parts showing": "Threepio With His Parts Showing",
    "threepio w\\ his parts showing": "Threepio With His Parts Showing",
    "Padmé Naberrie": "Padme Naberrie",
    "Padme' Naberrie": "Padme Naberrie",
    "Padme": "Padme Naberrie",
    "An Unusual Amount of Fear (pick your fave Shields)": "An Unusual Amount Of Fear",
    "Ralthir Freighter Captains": "Ralltiir Freighter Captain",
    "Ralthir Freighter Captain": "Ralltiir Freighter Captain",
    "YT-1300": "YT-1300 Transport",
    "Millenium Falcons": "Millennium Falcon",
    "Millenium Falcon": "Millennium Falcon",
    "Ralthir": "Ralltiir",
    "Tatooine Cantina": "Tatooine: Cantina",
    "Tatooine Docking Bay 94": "Tatooine: Docking Bay 94",
    "Watch Your Step/ This Place Can Be A Little Rough": "Watch Your Step",
    "Kessel Runs": "Kessel Run",
    "Squadren Assignments": "Squadron Assignments",
    "Squadron Assignments": "Squadron Assignments",
    "Anikan's Lightsaber": "Anakin's Lightsaber",
    "Obi Wan's Journal": "Obi-Wan's Journal",
    "Home One Docking Bay": "Home One: Docking Bay",
    "Hoth Docking Bay": "Hoth: Echo Docking Bay",
    "Nobel Sacrafice": "Noble Sacrifice",
    "Han With Heavy Blaster": "Han With Heavy Blaster Pistol",
    "Chewbacca Protector": "Chewbacca, Protector",
    "Chewie with Blaster Rifle": "Chewie With Blaster Rifle",
    "Luke Skywalker Rebel Scout": "Luke Skywalker, Rebel Scout",
    "Dont Get Cocky": "Don't Get Cocky",
    "Don't Get Cocky": "Don't Get Cocky",
    "Obi-Wan, Jedi Knight": "Obi-Wan Kenobi, Jedi Knight",
    "Obi Wan, PL": "Obi-Wan Kenobi, Padawan Learner",
    "Lando with Blaster": "Lando With Blaster Pistol",
    "Lando With Blaster Pistol (don't have a new Lando yet!)": "Lando With Blaster Pistol",
    "Han woth Heavy Blaster": "Han With Heavy Blaster Pistol",
    "Jar Jar": "Jar Jar Binks",
    "Dont do that Again": "Don't Do That Again",
    "Honor": "Honor Of The Jedi",
    "Darth Maul Young Apprentice": "Darth Maul, Young Apprentice",
    "Darth Maul, Young App": "Darth Maul, Young Apprentice",
    "Dr. Evazan and Ponda Baba": "Dr. Evazan & Ponda Baba",
    "Janus": "Janus Greejatus",
    "Dengar with Blaster": "Dengar With Blaster Carbine",
    "Dengar with Gun": "Dengar With Blaster Carbine",
    "mara's Lightsaber": "Mara Jade's Lightsaber",
    "Mara's Saber": "Mara Jade's Lightsaber",
    "Maul's Double Bladed Saber": "Maul's Double-Bladed Lightsaber",
    "Maul's Double Bladed Lightsaber": "Maul's Double-Bladed Lightsaber",
    "Darth Maul's Lightsaber": "Maul's Double-Bladed Lightsaber",
    "Mauls Sith Infiltrator": "Maul's Sith Infiltrator",
    "Fett in Slave": "Boba Fett In Slave I",
    "Zuckuss in MH": "Zuckuss In Mist Hunter",
    "Podracer Collission": "Podracer Collision",
    "Twilek": "Twi'lek Advisor",
    "Prince Xixor": "Prince Xizor",
    "IG88 with Gun": "IG-88 With Riot Gun",
    "4LOM with Gun": "4-LOM With Concussion Rifle",
    "Fett with Gun": "Boba Fett With Blaster Rifle",
    "Bossk with Gun": "Bossk With Mortar Gun",
    "Jabba's Palace Audience Chamber": "Jabba's Palace: Audience Chamber",
    "Tatooine: Docking Bay": "Tatooine: Docking Bay 94",
    "Hoth Echo Command Center": "Hoth: Echo Command Center (War Room)",
    "Anakins*s Podracer": "Anakin's Podracer",
    "Tatooine Mos Espa": "Tatooine: Mos Espa",
    "Tatooine Hutt Trade Route": "Tatooine: Hutt Trade Route (Desert)",
    "Tatooine Lars Farm": "Tatooine: Lars' Moisture Farm",
    "Owen and Beru Lars": "Owen Lars & Beru Lars",
    "Yarna d*al* Gargan": "Yarna d'al' Gargan",
    "Savrip": "N'asr'al'hagh (Nasrallah) Savrip",
    "CC: Guest Quarters": "Cloud City: Guest Quarters",
    "Pucmir Thryss": "Pucumir Thryss",
    "You'll Find I’m Ful of Suprises": "You'll Find I'm Full Of Surprises",
    "Jrdi Presense": "Jedi Presence",
    "Obi-Wan’s Journal": "Obi-Wan's Journal",
    "Qui-Gon’s Lightsaber": "Qui-Gon Jinn's Lightsaber",
    "Obi-Wan’s Lightsaber": "Obi-Wan's Lightsaber",
    "Luke’s Lightsaber": "Luke's Lightsaber",
    "Anakin’s Lightsaber": "Anakin's Lightsaber",
    "Wedge Antilles Red Squadren Leader": "Wedge Antilles, Red Squadron Leader",
    "Tatooine : Desert Landing Site": "Tatooine: Desert Landing Site",
    "Tatooine : Jabbas Palace": "Tatooine: Jabba's Palace",
    "Jabbas Palace : Audience Chamber": "Jabba's Palace: Audience Chamber",
    "Jabbas Palace : Enterance Cavern": "Jabba's Palace: Entrance Cavern",
    "Mara Jade, The Emperors Hand": "Mara Jade, The Emperor's Hand",
    "Mara Jades Lightsaber": "Mara Jade's Lightsaber",
    "Mauls Double Bladed Lightsaber": "Maul's Double-Bladed Lightsaber",
    "Vaders Lightsaber": "Vader's Lightsaber",
    "Ommni Box & Its Worse": "Omni-Box & It's Worse",
    "Navar Yalnal": "Nevar Yalnal",
    "Circle is now Complete": "The Circle Is Now Complete",
    "Galactic Senate": "Coruscant: Galactic Senate",
    "Yeb Yeb Adem’ thorn": "Yeb Yeb Adem'thorn",
    "Maul’s Double Bladed Lightsaber": "Maul's Double-Bladed Lightsaber",
    "Vader’s Lightsaber": "Vader's Lightsaber",
    "Luke's Saber": "Luke's Lightsaber",
    "Anakin's Saber": "Anakin's Lightsaber",
    "Red Squad 1": "Red Squadron 1",
    "X-Wing Cannon": "X-Wing Laser Cannon",
    "X-Wing Laser Cannons": "X-Wing Laser Cannon",
    "Artoo, I have a bad feeling": "Artoo I Have A Bad Feeling About This",
    "Ive Got a Bad Feeling about this": "I've Got A Bad Feeling About This",
    "Effective repairs": "Effective Repairs",
    "Were you looking for me?": "Were You Looking For Me?",
    "Control & Tunnel Vision": "Control & Tunnel Vision",
    "Dont get cocky": "Don't Get Cocky",
    "Run Luke Run": "Run Luke, Run!",
    "Han with Blaster": "Han With Heavy Blaster Pistol",
    "Luke with Saber": "Luke With Lightsaber",
    "Raltiir Freighter Captain": "Ralltiir Freighter Captain",
    "Cantina": "Tatooine: Cantina",
    "Tatooine: Heading": "Heading For The Medical Frigate",
    "Tatooine: Insurrection": "Insurrection",
    "Tatooine: Battle Plan": "Battle Plan",
    "Tatooine: Squadron Assignments": "Squadron Assignments",
    "Tatooine: DB 94": "Tatooine: Docking Bay 94",
    "Tatooine: Luke JK": "Luke Skywalker, Jedi Knight",
    "Tatooine: Chewie, Enraged": "Chewie, Enraged",
    "Tatooine: Dash": "Dash Rendar",
    "Tatooine: Mirax": "Mirax Terrik",
    "Tatooine: Talon": "Talon Karrde",
    "Greeta": "Greedo",
    "High Speed Tactics": "High-speed Tactics",
    "Insignificant Losses": "Insignificant Rebellion",
    "Vibro Axe": "Vibro-Ax",
    "Rebel Snowspeeder x14 (The destiny 3 ones from hoth 2p game)": "Rebel Snowspeeder",
    "Rebel Snowspeeder x14": "Rebel Snowspeeder",
    "(S) = Start": "",
    "S) = starting": "",
    "Starting Interrupt:": "",
    "Charecters:": "",
    "Interupts": "",
    "Admirals Orders:": "",
    "Combat Vehicles:": "",
    "Weapons & Devices:": "",
    "Starships and Vehicles:": "",
    "Luke with Lightsaber": "Luke With Lightsaber",
    "Obi Wan with Lightsaber": "Obi-Wan With Lightsaber",
    "Obi-Wan with Lightsaber": "Obi-Wan With Lightsaber",
    "Heading for the Medical Frigate": "Heading For The Medical Frigate",
    "Eyes in the Dark": "Eyes In The Dark",
    "Red Leader in Red 1": "Red Leader In Red 1",
    "Gold Leader in Gold 1": "Gold Leader In Gold 1",
    "Anger, Fear and Aggression": "Anger, Fear, Aggression",
    "Kessel (Marker)": "Kessel",
    "We'll Handle This!": "We'll Handle This",
    "We'll Handle This": "We'll Handle This",
    "Fear Is my Ally": "Fear Is My Ally",
    "Visage Of the Emperor": "Visage Of The Emperor",
    "The Phantom Menace": "The Phantom Menace",
    "Watto's Box": "Watto's Box",
    "Mara jade's Lightsaber": "Mara Jade's Lightsaber",
    "Maul's Double Bladed Lightsaber": "Darth Maul's Lightsaber",
    "Imperial Holotable": "Death Star: Conference Room",
    "Tatooine Marketplace": "Tatooine: Marketplace",
    "Tatooine Podrace Arena": "Tatooine: Podrace Arena",
    "Executor Meditation Chamber": "Executor: Meditation Chamber",
    "Executor Holotheatre": "Executor: Holotheatre",
    "Maul's Sith Infiltrator": "Maul's Sith Infiltrator",
    "Sebulba's Podracer": "Sebulba's Podracer",
    "Mara Jade The Emperor's Hand": "Mara Jade, The Emperor's Hand",
    "Darth Vader With Lightsaber": "Darth Vader With Lightsaber",
    "Darth Vader Dark Lord of the Sith": "Darth Vader, Dark Lord Of The Sith",
    "Start Your Engines!": "Start Your Engines!",
    "Shut Him Up Or Shut Him Down": "Shut Him Up Or Shut Him Down",
    "The Circle Is now Complete": "The Circle Is Now Complete",
    "It's Worse": "It's Worse",
    "I Have You Now": "I Have You Now",
    "Operational As Planned": "Operational As Planned",
    "Focused Attack": "Focused Attack",
    "Tatoonie: Desert Landing Site": "Tatooine: Desert Landing Site",
    "Lord Maul": "Darth Maul",
    "Yeb Yeb Adem thorn": "Yeb Yeb Adem'thorn",
    "Yeb Yeb Adem� thorn": "Yeb Yeb Adem'thorn",
    "Toonbuck Toora": "Toonbuck Toora",
    "Zuckass In Mist Hunter": "Zuckuss In Mist Hunter",
    "This Is Outrageous": "This Is Outrageous",
    "Motion Supported": "Motion Supported",
    "Our Blockade Is Perfectly Legal": "Our Blockade Is Perfectly Legal",
    "Squabbling Delegates": "Squabbling Delegates",
    "Maul Strikes": "Maul Strikes",
    "Blow Parried": "Blow Parried",
    "luke skywalker rebel scout": "Luke Skywalker, Rebel Scout",
    "luke w\\lightsaber": "Luke With Lightsaber",
    "luke w/lightsaber": "Luke With Lightsaber",
    "master luke": "Master Luke",
    "mirax terrik": "Mirax Terrik",
    "threepio w\\ his parts showing": "Threepio With His Parts Showing",
    "threepio w/ his parts showing": "Threepio With His Parts Showing",
    "captain panaka": "Captain Panaka",
    "ki-adi-mundi": "Ki-Adi-Mundi",
    "caldera righim": "Caldera Righim",
    "padame newbarrie": "Padme Naberrie",
    "lando w\\ vibro-ax": "Lando With Vibro-Ax",
    "lando w/ vibro-ax": "Lando With Vibro-Ax",
    "boushh": "Boushh",
    "obi-wan w\\ lightsaber": "Obi-Wan With Lightsaber",
    "obi-wan w/ lightsaber": "Obi-Wan With Lightsaber",
    "melas": "Melas",
    "han solo": "Han Solo",
    "han w\\ heavy blaster pistal": "Han With Heavy Blaster Pistol",
    "han w/ heavy blaster pistal": "Han With Heavy Blaster Pistol",
    "chewbacca, protector": "Chewbacca, Protector",
    "chewie w\\ blaster rifle": "Chewie With Blaster Rifle",
    "chewie w/ blaster rifle": "Chewie With Blaster Rifle",
    "qui-gon jinn": "Qui-Gon Jinn",
    "master qui-gon": "Master Qui-Gon",
    "artoo": "Artoo",
    "corran horn": "Corran Horn",
    "shmi skiwalker": "Shmi Skywalker",
    "qui-gons lightsaber": "Qui-Gon Jinn's Lightsaber",
    "panaka's blaster": "Panaka's Blaster",
    "anikin's lightsaber": "Anakin's Lightsaber",
    "lukes light saber": "Luke's Lightsaber",
    "honor of the jedi": "Honor Of The Jedi",
    "goo nee tay": "Goo Nee Tay",
    "the camp": "The Camp",
    "weapon levitation": "Weapon Levitation",
    "too close for comfort": "Too Close For Comfort",
    "mindful of the future": "Mindful Of The Future",
    "iconsquential bariers": "Inconsequential Barriers",
    "the signal": "The Signal",
    "rebel barrier": "Rebel Barrier",
    "heading for the medical frigate": "Heading For The Medical Frigate",
    "anakin's podracer": "Anakin's Podracer",
    "city outskirts": "Tatooine: City Outskirts",
    "slave quarters": "Tatooine: Slave Quarters",
    "mos espa docking bay": "Tatooine: Mos Espa Docking Bay",
    "jabba's place": "Tatooine: Jabba's Palace",
    "audience chamber": "Jabba's Palace: Audience Chamber",
    "entrance cavern": "Jabba's Palace: Entrance Cavern",
    "antechamber": "Jabba's Palace: Antechamber",
    "Tatooine: city outskirts": "Tatooine: City Outskirts",
    "Tatooine: slave quarters": "Tatooine: Slave Quarters",
    "Tatooine: mos espa docking bay": "Tatooine: Mos Espa Docking Bay",
    "Tatooine: jabba's place": "Tatooine: Jabba's Palace",
    "Jabba's Palace: audience chamber": "Jabba's Palace: Audience Chamber",
    "Jabba's Palace: entrance cavern": "Jabba's Palace: Entrance Cavern",
    "Jabba's Palace: antechamber": "Jabba's Palace: Antechamber",
    # Last-wins corrections (later keys beat earlier typos).
    "This Is Outrageous": "This Is Outrageous!",
    "Maul's Double Bladed Lightsaber": "Maul's Double-Bladed Lightsaber",
    "Savrip": "Mantellian Savrip",
    "Ommni Box & Its Worse": "Ommni Box & It's Worse",
    "Artoo, I have a bad feeling": "Artoo, I Have A Bad Feeling About This",
    "Artoo I Have A Bad Feeling About This": "Artoo, I Have A Bad Feeling About This",
    "CC: Lower Corridor": "Cloud City: Lower Corridor",
    "CC: North Corridor": "Cloud City: North Corridor",
    "CC: Carbonite Chamber": "Cloud City: Carbonite Chamber",
    "CC: Core Tunnel": "Cloud City: Core Tunnel",
    "Omni Box and Its Worse": "Ommni Box & It's Worse",
    "Omni Box & Its worse": "Ommni Box & It's Worse",
    "Omni Box/Its Worse": "Ommni Box & It's Worse",
    "Omni-Box & It's Worse": "Ommni Box & It's Worse",
    "Force Lightening": "Force Lightning",
    "Aurra Sings Blaster": "Aurra Sing's Blaster Rifle",
    "Bossk in HT": "Bossk In Hound's Tooth",
    "Vaders Obs": "Vader's Obsession",
    "Tatooine: Lars Farm": "Tatooine: Lars' Moisture Farm",
    "Mirax": "Mirax Terrik",
    "Talon": "Talon Karrde",
    "Wedge": "Wedge Antilles",
    "Tatooine Celeb": "Tatooine Celebration",
    "Spacfeport Docking Bay": "Spaceport Docking Bay",
    "Ill Take the Leader": "I'll Take The Leader",
    "I'll Take The Leader": "I'll Take The Leader",
    "Outriders": "Outrider",
    "Fallen Portals": "Fallen Portal",
    "You'll Find I'm Ful of Suprises": "You'll Find I'm Full Of Surprises",
    "Luke Skywalker Jedi Knight": "Luke Skywalker, Jedi Knight",
    "Nien Numb": "Nien Nunb",
    "Gold Squadren 1": "Gold Squadron 1",
    "Red Squadren 1": "Red Squadron 1",
    "Cloud City Platform 327(Docking Bay)": "Cloud City: Platform 327 (Docking Bay)",
    "Cloud City Platform 327 (Docking Bay)": "Cloud City: Platform 327 (Docking Bay)",
    "Cloud City Carbonite Chamber": "Cloud City: Carbonite Chamber",
    "Cloud City North Corridor": "Cloud City: North Corridor",
    "Cloud City Guest Quarters": "Cloud City: Guest Quarters",
    "Bespin Cloud City": "Bespin: Cloud City",
    "Focussed Attack": "Focused Attack",
    "Speeder Bikes": "Speeder Bike",
    "BF in S1": "Boba Fett In Slave I",
    "Dengar in P1": "Dengar In Punishing One",
    "Qui-Gon Jinn's Saber": "Qui-Gon Jinn's Lightsaber",
    "Gui-Gon's Saber (Destiny 5)": "Qui-Gon Jinn's Lightsaber",
    "Gui-Gon's Saber": "Qui-Gon Jinn's Lightsaber",
    "Obi-Wan Kenobi's Saber": "Obi-Wan's Lightsaber",
    "Obi-Wan's Saber (Destiny 2)": "Obi-Wan's Lightsaber",
    "Han, Chewie and the Falcon": "Han, Chewie, And The Falcon",
    "Ani's Podracer": "Anakin's Podracer",
    "Bith Shuffle/Desperate Reach": "The Bith Shuffle & Desperate Reach",
    "Ghhhk/Those Rebels Won't Escape Us": "Ghhhk & Those Rebels Won't Escape Us",
    "There Is No Try/Oppressive Enforcement": "There Is No Try & Oppressive Enforcement",
    "Search & Destroy": "Search And Destroy",
    "Yeb Yeb Adem' thorn": "Yeb Yeb Adem'thorn",
    "Yeb Yeb Adem'thorn": "Yeb Yeb Adem'thorn",
    # Page 62 slang (last-wins).
    "the emporers": "Emperor Palpatine",
    "the emperors": "Emperor Palpatine",
    "mara jade the emporer's hand": "Mara Jade, The Emperor's Hand",
    "boba fett w/ blaster rifle": "Boba Fett With Blaster Rifle",
    "dr evazan & ponda baba": "Dr. Evazan & Ponda Baba",
    "4-lom w/ concustion rifle": "4-LOM With Concussion Rifle",
    "IG-88 w/ riot gon": "IG-88 With Riot Gun",
    "Bossk w/ mortar gun": "Bossk With Mortar Gun",
    "Mual's double-bladed lightsaber": "Maul's Double-Bladed Lightsaber",
    "they are sill coming through!": "They're Still Coming Through!",
    "neimodian advisor": "Neimoidian Advisor",
    "Naboo:Battle plains": "Naboo: Battle Plains",
    "Court/isewyd": "Court Of The Vile Gangster",
    "JP: Dung": "Jabba's Palace: Dungeon",
    "JP: Aud. Cham": "Jabba's Palace: Audience Chamber",
    "Tat: GPO Carkoon": "Tatooine: Great Pit Of Carkoon",
    "Prep. Defen": "Prepared Defenses",
    "Prep. Def": "Prepared Defenses",
    "Prep. Defenses": "Prepared Defenses",
    "Prepared Def": "Prepared Defenses",
    "Prepared Defences": "Prepared Defenses",
    "FearIMA": "Fear Is My Ally",
    "Dengars modified Riot Gun": "Dengar's Modified Riot Gun",
    "Dr. E's Blaster": "Dr. Evazan's Sawed-off Blaster",
    "Scum and viliany": "Scum And Villainy",
    "Endor Ops": "Endor Operations",
    "Bunker": "Endor: Bunker",
    "Landing Platform": "Endor: Landing Platform (Docking Bay)",
    "Landing platform": "Endor: Landing Platform (Docking Bay)",
    "Oppresive Enforcement": "Oppressive Enforcement",
    "Ancient Forest": "Endor: Ancient Forest",
    "Forest Clearing": "Endor: Forest Clearing",
    "Dark Forest": "Endor: Dark Forest",
    "Tempest Scout4": "Tempest Scout 4",
    "CCT/MFD": "Carbon Chamber Testing",
    "IAO": "Imperial Arrest Order",
    "MOB.PTS": "Mobilization Points",
    "AWU": "All Wrapped Up",
    "AW Up": "All Wrapped Up",
    "JPrize": "Jabba's Prize",
    "CC:ST": "Cloud City: Security Tower",
    "CC:CC": "Cloud City: Carbonite Chamber",
    "CCConsole": "Carbonite Chamber Console",
    "VibroAX": "Vibro-Ax",
    "MJ's stick": "Mara Jade's Lightsaber",
    "A Million Voices": "A Million Voices Crying Out",
    "YCHF/MPoints": "You Cannot Hide Forever & Mobilization Points",
    "Defensive Fire/ Hutt Smooch": "Defensive Fire & Hutt Smooch",
    "Defen. Fire/ Hutt Smooch": "Defensive Fire & Hutt Smooch",
    "Short-range Fighters": "Short Range Fighters",
    "Darth Maul (Tatooine)": "Darth Maul, Young Apprentice",
    "Emperor Palpatine(DSII)": "Emperor Palpatine",
    "TDIGWATT/PIDAIAF": "This Deal Is Getting Worse All The Time",
    "This Deal Is Getting Worse All The Time/Pray": "This Deal Is Getting Worse All The Time",
    "Do They Have Code Clearance?": "Do They Have A Code Clearance?",
    "IAO/S Plans": "Imperial Arrest Order & Secret Plans",
    "Bespin: CC": "Bespin: Cloud City",
    "CC: Security Tower": "Cloud City: Security Tower",
    "CC: Chasm Walkway": "Cloud City: Chasm Walkway",
    "CC: Incerator": "Cloud City: Incinerator",
    "CC: Downtown Plaza": "Cloud City: Downtown Plaza",
    "Short Range Fighters/ WYB": "Short Range Fighters & Watch Your Back!",
    "HFTMF": "Heading For The Medical Frigate",
    "Forest": "Endor: Dense Forest",
    "Endor: Landing Platform(Docking Bay)": "Endor: Landing Platform (Docking Bay)",
    "Obi-Wan Kenobi {Premiere}": "Obi-Wan Kenobi",
    "ASP-707 [Ayeesspee]": "ASP-707 (Ayesspee)",
    "R2-D2 [Artoo-Detoo] {A New Hope Version}": "R2-D2 (Artoo-Detoo)",
    "Nar Shaddaa WC & Out Of S": "Nar Shaddaa Wind Chimes & Out Of Somewhere",
    "Soryy About TM & Blaster P": "Sorry About The Mess & Blaster Proficiency",
    "Either Way you Win": "Either Way, You Win",
    "Rebel Landing Site": "Endor: Rebel Landing Site (Forest)",
    "YISYW": "Your Insight Serves You Well",
    "Strike planning": "Strike Planning",
    "Back Door": "Endor: Back Door",
    "LSJK": "Luke Skywalker, Jedi Knight",
    "Hidden Forest Trail": "Endor: Hidden Forest Trail",
    "Hidden Base/SWSTYF": "Hidden Base",
    "Heading 4 the Med. Frigate": "Heading For The Medical Frigate",
    "Squ. Assignments": "Squadron Assignments",
    "Men. Fades": "Menace Fades",
    "HB: Endor": "Endor",
    "Ral. Operative": "Ralltiir Operative",
    "Kiffex Op": "Kiffex Operative",
    "Both. Op": "Bothawui Operative",
    "Kirdo 3 Op": "Kirdo III Operative",
    "Wedge Ant., RS Leader": "Wedge Antilles, Red Squadron Leader",
    "Lee-Bo": "LE-BO2D9 (Leebo)",
    "Tcho Celchu": "Tycho Celchu",
    "LS, JK": "Luke Skywalker, Jedi Knight",
    "Windchimes/ OO somewhere": "Nar Shaddaa Wind Chimes & Out Of Somewhere",
    "A Few Maneu.": "A Few Maneuvers",
    "It could b worse": "It Could Be Worse",
    "Con. / TVision": "Control & Tunnel Vision",
    "OOC/ TT": "Out Of Commission & Transmission Terminated",
    "Red Sq. 7": "Red Squadron 7",
    "Green Sq. 3": "Green Squadron 3",
    "There Is Good in Him/I can save him": "There Is Good In Him",
    "Heading the Medical Frigate": "Heading For The Medical Frigate",
    "Leitenet Blount": "Lieutenant Blount",
    "Lietenant Page": "Lieutenant Page",
    "R2-D2(Artoo-Detoo)-New Hope": "R2-D2 (Artoo-Detoo)",
    "Luke w/ Lightsaber": "Luke With Lightsaber",
    "Endor: docking bay": "Endor: Landing Platform (Docking Bay)",
    "Extr: Medit. Chamber": "Executor: Meditation Chamber",
    "Mara Jade, the EMP": "Mara Jade, The Emperor's Hand",
    "Captain Palleon": "Captain Pellaeon",
    "Chimera": "Chimaera",
    "Bosk in hound tooth": "Bossk In Hound's Tooth",
    "Twi'lek Advisor": "Twi'lek Advisor",
    "Vader's Obsession": "Vader's Obsession",
    "It's worse (combo card)": "It's Worse",
    "You can't hide forever": "You Cannot Hide Forever",
    "mind what you have learned/save you it can": "Mind What You Have Learned",
    "Dagaboah": "Dagobah",
    "Dagaboah:yoda's hut": "Dagobah: Yoda's Hut",
    "Dagaboah:bog clearing": "Dagobah: Bog Clearing",
    "Dagaboah:swamp": "Dagobah: Swamp",
    "Dagaboah:jungle": "Dagobah: Jungle",
    "Dagaboah:training area": "Dagobah: Training Area",
    "Cloud city:guest quarters": "Cloud City: Guest Quarters",
    "Cloud city:lower corridor": "Cloud City: Lower Corridor",
    "Obi-won kenobi": "Obi-Wan Kenobi",
    "captin han solo": "Captain Han Solo",
    "gold leader in red 1": "Gold Leader In Gold 1",
    "Lightsaber Combat Objective": "Let Them Make The First Move",
    "Naboo: Generator": "Naboo: Theed Palace Generator",
    "Naboo: Generator Core": "Naboo: Theed Palace Generator Core",
    "Fear is Our Ally": "Fear Is My Ally",
    "Blockade Falgship: Bridge": "Blockade Flagship: Bridge",
    "Emperor Palpaltine": "Emperor Palpatine",
    "Boba Fett, BH": "Boba Fett, Bounty Hunter",
    "Might Jabba": "Mighty Jabba",
    "Ponda Boba/Dr. E": "Dr. Evazan & Ponda Baba",
    "Vader's Whacker": "Vader's Lightsaber",
    "Mara's Whacker": "Mara Jade's Lightsaber",
    "Maul's Double Whacker": "Maul's Double-Bladed Lightsaber",
    "Court of the Vile/Enjoy watching you die": "Court Of The Vile Gangster",
    "Tat: Pit of Carkoon": "Tatooine: Great Pit Of Carkoon",
    "JP: Dungeon": "Jabba's Palace: Dungeon",
    "JP: Aud Chamber": "Jabba's Palace: Audience Chamber",
    "Inconsiquential Loses": "Insignificant Rebellion",
    "4-LOM w/gun": "4-LOM With Concussion Rifle",
    "IG-88 w/gun": "IG-88 With Riot Gun",
    "Dengar w/gun": "Dengar With Blaster Carbine",
    "Bossk w/gun": "Bossk With Mortar Gun",
    "Aurra Sing's Rifle": "Aurra Sing's Blaster Rifle",
    "Podrace Arena": "Tatooine: Podrace Arena",
    "Anikans Racer": "Anakin's Podracer",
    "Hutt Trade Route": "Tatooine: Hutt Trade Route (Desert)",
    "Agents In the Court/": "Agents In The Court",
    "Jawa Camp": "Tatooine: Jawa Camp",
    "Jawa Canyon": "Tatooine: Jawa Canyon",
    "Lars Farm": "Tatooine: Lars' Moisture Farm",
    "Marketplace": "Tatooine: Marketplace",
    "Dune Sea Sabbac": "Dune Sea Sabacc",
    "Go Nee Tay": "Goo Nee Tay",
    "Kalit's Sand Crawler": "Kalit's Sandcrawler",
    "Utinni": "Utinni!",
    "Jawa (courscant)": "Jawa",
    "Jawa (coruscant)": "Jawa",
    "General Madine": "General Crix Madine",
    "Boush": "Boushh",
    "Boussh": "Boushh",
    "Rik, Hero of the Dune Sea": "R'kik D'nec, Hero Of The Dune Sea",
    "Sniper & Darkstrike": "Sniper & Dark Strike",
    "Prepared Defense": "Prepared Defenses",
    "Insinifigant Rebellion": "Insignificant Rebellion",
    "Imperial Arrest Order/ Secret Plan": "Imperial Arrest Order & Secret Plans",
    "Red Leader In Red One": "Red Leader In Red 1",
    "The Shield Is Down!": "The Shield Is Down",
    "Order to Engage": "Order To Engage",
    "On the Edge": "On The Edge",
    "Ithorian": "Ithorian",
    "Chewbacca Of Kashyyyk": "Chewbacca Of Kashyyyk",
    "···Ithorian": "Ithorian",
    "Padmé Naberrie": "Padme Naberrie",
    "Obi-Wan's Lightsaber": "Obi-Wan's Lightsaber",
    "Qui-Gon Jinn's Lightsaber": "Qui-Gon Jinn's Lightsaber",
    "Luke's Lightsaber": "Luke's Lightsaber",
    "Were You Looking For Me?": "Were You Looking For Me?",
    "Lost In the Wilderness": "Lost In The Wilderness",
    "Lando In Millennium Falcon": "Lando In Millennium Falcon",
    "Portable Scanner": "Portable Scanner",
    "Deactivate The Shield Generator": "Deactivate The Shield Generator",
    "Brisky Morning Munchen": "Brisky Morning Munchen",
    "I'm Sorry": "I'm Sorry",
    "We're The Bait": "We're The Bait",
    "Crush the Rebellion": "Crush The Rebellion",
    "Agents In the Court": "Agents In The Court",
    "Podrace Prep": "Podrace Prep",
    "Underworld Contacts": "Underworld Contacts",
    "I Did It!": "I Did It!",
    "TK 422": "TK-422",
    "Aved Lunn": "Aved Luun",
    "Blue Milk": "Blue Milk",
    "Nar Shadda Wind Chimes": "Nar Shaddaa Wind Chimes",
    "Jawa Siesta": "Jawa Siesta",
    "Restricted Deployment": "Restricted Deployment",
    "Bargaining Table": "Bargaining Table",
    "Harvest": "Harvest",
    "Sandwhirl": "Sandwhirl",
    "Audience Chamber": "Jabba's Palace: Audience Chamber",
    "BHBM/TYFP": "Bring Him Before Me",
    "Ds2: Throne Room": "Death Star II: Throne Room",
    "Ds2: Docking Bay": "Death Star II: Docking Bay",
    "CC: Docking Bay": "Cloud City: Platform 327 (Docking Bay)",
    "Sith Probes": "Sith Probe Droid",
    "Dengar with Blaster Rifle": "Dengar With Blaster Carbine",
    "Dv, DLOTS": "Darth Vader, Dark Lord Of The Sith",
    "Aurra Sings Blaster Rifle": "Aurra Sing's Blaster Rifle",
    "Mauls Double Bladed Saber": "Maul's Double-Bladed Lightsaber",
    "Mara Jades Saber": "Mara Jade's Lightsaber",
    "Darth Vaders Saber": "Vader's Lightsaber",
    "Vaders Stick": "Force Pike",
    "IG-88 with gun": "IG-88 With Riot Gun",
    "Slave 1": "Slave I",
    "Boba Fett In Slave 1": "Boba Fett In Slave I",
    "Twi 'lek Advisor": "Twi'lek Advisor",
    "Disrupto Pistol": "Disruptor Pistol",
    "Boba Fett, bounty hunter": "Boba Fett, Bounty Hunter",
    "let them make the first move": "Let Them Make The First Move",
    "deep hatred": "Deep Hatred",
    "Qui-gon's end": "Qui-Gon's End",
    "Imperial arrest order & secret plans": "Imperial Arrest Order & Secret Plans",
    "fear is my ally": "Fear Is My Ally",
    "lord maul": "Darth Maul",
    "darth vader w/lightsaber": "Darth Vader With Lightsaber",
    "P-60": "P-60",
    "guri": "Guri",
    "blizzard 4": "Blizzard 4",
    "intruder missile": "Intruder Missile",
    "i have you now": "I Have You Now",
    "masterful move": "Masterful Move",
    "force field": "Force Field",
    "coruscant docking bay": "Coruscant: Docking Bay",
    "theed palace courtyard": "Naboo: Theed Palace Courtyard",
    "theed palace throne room": "Naboo: Theed Palace Throne Room",
    "thhede palace docking bay": "Naboo: Theed Palace Docking Bay",
    "thede palace generator": "Naboo: Theed Palace Generator",
    "theed palace generator core": "Naboo: Theed Palace Generator Core",
    "death star 2 docking bay": "Death Star II: Docking Bay",
    "Bossk w/ gun": "Bossk With Mortar Gun",
    "Dr. E + Ponda Baba": "Dr. Evazan & Ponda Baba",
    "Darth Vader w/ Stick": "Darth Vader With Lightsaber",
    "IG-88 w/ gun": "IG-88 With Riot Gun",
    "4-lom w/ gun": "4-LOM With Concussion Rifle",
    "Boba Fett w/ gun": "Boba Fett With Blaster Rifle",
    "Def. Fire/ Hutt Smooch": "Defensive Fire & Hutt Smooch",
    "AOrnament/WWookiee": "Abyssin Ornament & Wounded Wookiee",
    "OB/ It's worse": "Ommni Box & It's Worse",
    "Oo-ta Goo-ta Solo?": "Oo-ta Goo-ta, Solo?",
    "Any Methods N.": "Any Methods Necessary",
    "Any Methods N": "Any Methods Necessary",
    "IG-88 in ship": "IG-88 In IG-2000",
    "Zuckuss in ship": "Zuckuss In Mist Hunter",
    "Bossk in ship": "Bossk In Hound's Tooth",
    "Dengar in ship": "Dengar In Punishing One",
    "Boba Fett in ship": "Boba Fett In Slave I",
    "T: Desert Heart": "Tatooine: Desert Heart",
    "T: Lars' Moisture Farm": "Tatooine: Lars' Moisture Farm",
    "T: Tusken Canyon": "Tatooine: Tusken Canyon",
    "T: Docking Bay": "Tatooine: Docking Bay 94",
    "T: Desert": "Tatooine: Desert",
    "JP: Dung.": "Jabba's Palace: Dungeon",
    "JP: Aud. Cham.": "Jabba's Palace: Audience Chamber",
    "Power of the Hutt": "Power Of The Hutt",
    "Res Luk Ra'auf": "Res Luk Ra'auf",
    "RLRa'auf": "Res Luk Ra'auf",
    "Tempest Scout5": "Tempest Scout 5",
    "Tempest Scout6": "Tempest Scout 6",
    "AT-ST Duel Cannon": "AT-ST Dual Cannon",
    "V Lsaber": "Vader's Lightsaber",
    "FLightning": "Force Lightning",
    "Omn/Its worse": "Ommni Box & It's Worse",
    "PTChamber": "Prepare The Chamber",
    "OtGt Solo?": "Oo-ta Goo-ta, Solo?",
    "AO/WW": "Abyssin Ornament & Wounded Wookiee",
    "SLNHerder": "Scruffy-Looking Nerf Herder",
    "DF/HSmooch": "Defensive Fire & Hutt Smooch",
    "FField": "Force Field",
    "DV, DLOTS": "Darth Vader, Dark Lord Of The Sith",
    "DV w/LS": "Darth Vader With Lightsaber",
    "Ugn": "Ugnaught",
    "DPuhr": "Djas Puhr",
    "LCalrissian": "Lando Calrissian",
    "PXixor": "Prince Xizor",
    "D w/ B Carbine": "Dengar With Blaster Carbine",
    "IG88 w/ gun": "IG-88 With Riot Gun",
    "Murtoc Yine": "Murttoc Yine",
    "E Mon": "Ephant Mon",
    "MJ, TEH": "Mara Jade, The Emperor's Hand",
    "Ugolste": "Ugloste",
    "JKast": "Jodo Kast",
    "BMalar": "Bane Malar",
    "4LOM w/ gun": "4-LOM With Concussion Rifle",
    "GA Thrawn": "Grand Admiral Thrawn",
    "MJabba": "Mighty Jabba",
    "JT Hutt": "Jabba The Hutt",
    "B in Bus": "Bossk In Hound's Tooth",
    "Z in MH": "Zuckuss In Mist Hunter",
    "Temp. 1": "Tempest Scout 1",
    "C-Freeze": "Carbon-Freezing",
    "POT Force": "Presence Of The Force",
    "DB-": "Spaceport Docking Bay",
    "DB": "Spaceport Docking Bay",
    "Exe.": "Executor",
    "Exe": "Executor",
    "Coru.": "Coruscant",
    "Coru": "Coruscant",
    "End.": "Endor",
    "End": "Endor",
    "Tat.": "Tatooine",
    "Tat": "Tatooine",
    "CC.": "Bespin: Cloud City",
    "CC": "Bespin: Cloud City",
    "DSII": "Death Star II",
    "Jabbas palace AC": "Jabba's Palace: Audience Chamber",
    "Ghhhk/TRWE Us": "Ghhhk & Those Rebels Won't Escape Us",
    "Control/ Set For Stun": "Control & Set For Stun",
    "OS-72-1 in ship": "OS-72-1 In Obsidian 1",
    "OS-72-2 in ship": "OS-72-2 In Obsidian 2",
    "The Shield Is Down": "The Shield Is Down!",
    "The Shield Is Down!": "The Shield Is Down!",
    "Obi w/Lightsaber": "Obi-Wan With Lightsaber",
    "Jedi Light Saber": "Jedi Lightsaber",
    "Shocking Info": "Shocking Information",
    "Gold Leader in Gold One": "Gold Leader In Gold 1",
    "Dereck 'Hobbie' Kilvian": "Derek 'Hobbie' Klivian",
    "This absolutely Right": "This Is Absolutely Right",
    "Lando In Millenium Falcon": "Lando In Millennium Falcon",
    "A Few Maneu": "A Few Maneuvers",
    "Nice of u guys 2 drop by": "Nice Of You Guys To Drop By",
    "Red Sq. 1": "Red Squadron 1",
    "Home 1": "Home One",
    "Captain Pellaeon": "Captain Gilad Pellaeon",
    "Mara Jade Lightsaber": "Mara Jade's Lightsaber",
    "Hunt down and Destroy": "Hunt Down And Destroy The Jedi",
    "anger,fear,aggression": "Anger, Fear, Aggression",
    "trafic control": "Traffic Control",
    "anakins lightsaber": "Anakin's Lightsaber",
    "anikans lightsaber": "Anakin's Lightsaber",
    "obi-won's lightsaber": "Obi-Wan's Lightsaber",
    "luk's backpack": "Luke's Backpack",
    "the signal": "The Signal",
    "Omni Box/It's Worse": "Ommni Box & It's Worse",
    "This is Some Rescue": "This Is Some Rescue!",
    "Drop": "Drop!",
    "Blast Door Control": "Blast Door Controls",
    "Secret Plans/Imperial Arrest Order": "Imperial Arrest Order & Secret Plans",
    "Boba Fett's Rifle": "Boba Fett's Blaster Rifle",
    "Dengar's Riot Gun": "Dengar's Modified Riot Gun",
    "Feltipern's Stun Gun": "Feltipern Trevagg's Stun Rifle",
    "Tat: Jabba's Palace": "Tatooine: Jabba's Palace",
    "JP: Entrance Chamber": "Jabba's Palace: Entrance Cavern",
    "JP: Rancor Pit": "Jabba's Palace: Rancor Pit",
    "CC: Docking Bay": "Cloud City: East Platform (Docking Bay)",
    "I wonder who they found": "I Wonder Who They Found",
    # Page 61 last-wins (do not map Imperial Holotable away).
    "Imperial Holotable": "Imperial Holotable",
    "No money,No parts,No deal/ You're a slave?": "No Money, No Parts, No Deal!",
    "No money,No parts,No deal/ You're a slave": "No Money, No Parts, No Deal!",
    "Imperial Arrest Order/ Secret Plans": "Imperial Arrest Order & Secret Plans",
    "Imperial Arrest Order/Secret Plans": "Imperial Arrest Order & Secret Plans",
    "Where are those Droidekas?": "Where Are Those Droidekas?!",
    "Desert Landing Site": "Tatooine: Desert Landing Site",
    "I will find them quickly master": "I Will Find Them Quickly, Master",
    "silence is golden": "Silence Is Golden",
    "if the trace was correct": "If The Trace Was Correct",
    "Rollin, Rolling, Rolling": "Rollin' And Rollin'",
    "Master, Destroyers": "Master, Destroyers",
    "Plead My Case To The Senate/Sanity and Compassion": "Plead My Case To The Senate",
    "Punch It!!": "Punch It",
    "Out of Commission an Transmission Terminated": "Out Of Commission & Transmission Terminated",
    "Liana Merrian": "Liana Merian",
    "Obi Wan Kenobi with Lightsaber": "Obi-Wan With Lightsaber",
    "Master Qui-Gon": "Qui-Gon Jinn",
    "Spaceport:Docking Bay": "Spaceport Docking Bay",
    "Mos Espa:Docking Bay": "Tatooine: Mos Espa Docking Bay",
    "Plea to the Court": "Plea To The Court",
    "Might of the Republic": "Might Of The Republic",
    "Speak with the Jedi Council": "Speak With The Jedi Council",
    "We Wish to Board at Once": "We Wish To Board At Once",
    "This Deal Is Getting Worse All The Time/Pray I Don't Alter It Any Futher": (
        "This Deal Is Getting Worse All The Time"
    ),
    "This Deal is Getting Worse All The Time/": "This Deal Is Getting Worse All The Time",
    "Cloud City:Upper Walkway": "Cloud City: Upper Walkway",
    "Twi'leck Advisor": "Twi'lek Advisor",
    "Bespin:Cloud City": "Bespin: Cloud City",
    "Cloud City:Incinerator": "Cloud City: Incinerator",
    "Cloud City:Carbonite Chamber": "Cloud City: Carbonite Chamber",
    "Alert My Star Destroyer": "Alert My Star Destroyer!",
    "Mob Points & You Cannot Hide Forever": "You Cannot Hide Forever & Mobilization Points",
    "You Cannot Hide Forever/Mobilization Points": "You Cannot Hide Forever & Mobilization Points",
    "Cloud City: Docking Bay": "Cloud City: East Platform (Docking Bay)",
    "Cloud City: West Galery": "Cloud City: West Gallery",
    "Dr. Evanez & Ponda Boba": "Dr. Evazan & Ponda Baba",
    "Dr. Evazan & Ponda Boba": "Dr. Evazan & Ponda Baba",
    "Dr Evezan and Ponda Boba": "Dr. Evazan & Ponda Baba",
    "Dr E. & Ponda B": "Dr. Evazan & Ponda Baba",
    "IG-88 with Riot Gun": "IG-88 With Riot Gun",
    "Janus Greegatus": "Janus Greejatus",
    "Dark Maneuvers/Talon Roll": "Dark Maneuvers & Talon Roll",
    "Ghhk/Those Rebels won't Escape Us": "Ghhhk & Those Rebels Won't Escape Us",
    "Limited Resorces": "Limited Resources",
    "Unexpected Interuption": "Unexpected Interruption",
    "Unsalvagable": "Unsalvageable",
    "Tantive 4": "Tantive IV",
    "The Force is Strong With This One": "The Force Is Strong With This One",
    "Gift of the Mentor": "Gift Of The Mentor",
    "Yavin 4:War Room": "Yavin 4: Massassi War Room",
    "Yavin 4:Massassi Ruins": "Yavin 4: Massassi Ruins",
    "Dejarik Holo-gameboard": "Dejarik Hologame Board",
    "Tatooine:Obi Wan's Hut": "Tatooine: Obi-Wan's Hut",
    "Tatooine:Lars' Moisture Farm": "Tatooine: Lars' Moisture Farm",
    "Tatooine:Mos Eisley": "Tatooine: Mos Eisley",
    "Kal Falnl C'ndros": "Kal'Falnl C'ndros",
    "Chewbacca of Kashyyk": "Chewbacca Of Kashyyyk",
    "Ewok Spearmen": "Ewok Spearman",
    "My Kind Of Stormtroopers/Who cares you don't flip": "My Kind Of Scum",
    "Desert Heart": "Tatooine: Desert Heart",
    "JP: Lower Passages": "Jabba's Palace: Lower Passages",
    "Mosep (rep)": "Mosep",
    "Mosep": "Mosep",
    "Vader w/ Lightsaber": "Darth Vader With Lightsaber",
    "Vader with Saber": "Darth Vader With Lightsaber",
    "Trooper Davin Felth (Filthy Dave)": "Trooper Davin Felth",
    "Maras saber": "Mara Jade's Lightsaber",
    "Perepared Defenses": "Prepared Defenses",
    "Well Guarded (always S)": "Well Guarded",
    "TINT/Oppresive Enforcement (always S)": "There Is No Try & Oppressive Enforcement",
    "Let them make the first move/ALWWHR": "Let Them Make The First Move",
    "Let Them Make The First Move/At Last We Will Have Revenge": "Let Them Make The First Move",
    "Let Them Make The First Move/...Revenge": "Let Them Make The First Move",
    "Emperor Palpetine": "Emperor Palpatine",
    "EPP Vader": "Darth Vader With Lightsaber",
    "3720 to 1": "3,720 To 1",
    "3720 To 1": "3,720 To 1",
    "Bad feeling Have I": "Bad Feeling Have I",
    "Overseeing it personally": "Overseeing It Personally",
    "Podrace Collission": "Podrace Collision",
    "Sense/Recoil in Fear": "Sense & Recoil In Fear",
    "Trooper Sabbac": "Trooper Sobbac",
    "Walkeemui": "Malastare",
    "Tatooine: Lars Moisture Farm": "Tatooine: Lars' Moisture Farm",
    "Big One": "The Big One: Asteroid Cave Or Space Slug Belly",
    "Siener Fleet Systems": "Sienar Fleet Systems",
    "Oppressive Enforcement/There is no try": "There Is No Try & Oppressive Enforcement",
    "Concussion Missles": "Concussion Missiles",
    "Scimtar Squadron Tie Bomber": "Scimitar Squadron TIE Bomber",
    "Tie Bomber": "TIE Bomber",
    "They Will Be NO Match For You": "They Will Be No Match For You",
    "Blockade Flagship Bridge": "Blockade Flagship: Bridge",
    "Sense & Uncertain is the Future": "Sense & Uncertain Is The Future",
    "Hidden Base Obj": "Hidden Base",
    "Hidden Base Obj.": "Hidden Base",
    "An Unusual amount of fear": "An Unusual Amount Of Fear",
    "Bothuwai": "Bothawui",
    "I'll Take the Leader": "I'll Take The Leader",
    "Artoo in Red 5": "Artoo In Red 5",
    "Han, Chewie, and the Falcon": "Han, Chewie, And The Falcon",
    "Wedge Antilles, RSL": "Wedge Antilles, Red Squadron Leader",
    "Lt. Blount": "Lieutenant Blount",
    "Col. Crac": "Colonel Cracken",
    "Accelerate Our Plans": "We Must Accelerate Our Plans",
    "We Must Accelerate Our PLans": "We Must Accelerate Our Plans",
    "I'd Just As Soon Kiss A Wookie": "I'd Just As Soon Kiss A Wookiee",
    "Tatooine: Lar's Moisture Farm": "Tatooine: Lars' Moisture Farm",
    "Lt. Commander Arden": "Lieutenant Commander Arnet",
    "Those Rebels Wont Escape Us": "Those Rebels Won't Escape Us",
    "Jabba": "Jabba The Hutt",
    "Coruscant:Imperial City": "Coruscant: Imperial City",
    "Boring Conversatin Anyway": "Boring Conversation Anyway",
    "Vibro Ax": "Vibro-Ax",
    "Hoth:Main Power Generators": "Hoth: Main Power Generators",
    "Hoth:North Ridge": "Hoth: North Ridge",
    "Hoth:Echo Corridor": "Hoth: Echo Corridor",
    "Hoth:Echo Docking Bay": "Hoth: Echo Docking Bay",
    "Hoth:Echo Command Center(War Room)": "Hoth: Echo Command Center (War Room)",
    "Derrek 'Hobbie' Klivian": "Derek 'Hobbie' Klivian",
    "Incom Corporaton": "Incom Corporation",
    "Echo Base Garrsion": "Echo Base Garrison",
    "Naboo:TP Gen Core": "Naboo: Theed Palace Generator Core",
    "Boba Fett W/Rifle": "Boba Fett With Blaster Rifle",
    "Dengar W/Blaster": "Dengar With Blaster Carbine",
    "4-LOM W/Rifle": "4-LOM With Concussion Rifle",
    "Oh, Switch Off!": "Oh, Switch Off",
    "Vader's Saber": "Vader's Lightsaber",
    "Aurra Sing's Rifle": "Aurra Sing's Blaster Rifle",
    "Feltipern Trefagg": "Feltipern Trevagg",
    "Boba Fett (CC)": "Boba Fett",
    "Scum And Villany": "Scum And Villainy",
    "Agents Of The Black Sun/Vengeance Of The Dark Prince": "Agents Of Black Sun",
    "Cloud City:East Platform(Docking Bay)": "Cloud City: East Platform (Docking Bay)",
    "Ben Kenobi": "Ben Kenobi",
    "General Calrissian": "General Calrissian",
    "Planetary Subjugation": "Occupation",
    "Search And Destroy": "Search And Destroy",
    "Search & Destroy": "Search And Destroy",
    "Coruscant (Special Edition)": "Coruscant",
    "Tatooine (Coruscant)": "Tatooine",
    "x1 This Deal Is Getting Worse All The Time": "This Deal Is Getting Worse All The Time",
    "Strike Blocked": "Strike Blocked",
    "Abyss": "Abyss",
    "Figrin": "Figrin D'an",
    "D'an": "Figrin D'an",
    "Darth Vader, DLOTS": "Darth Vader, Dark Lord Of The Sith",
    "Sebulba's Racer": "Sebulba's Podracer",
    "Coruscant: Jedi Council Chambers": "Coruscant: Jedi Council Chamber",
    "Punch It": "Punch It!",
    "Queen Amidala's Blaster": "Amidala's Blaster",
    "Artoo In Red 5": "Artoo-Detoo In Red 5",
    "Col. Cracken": "Colonel Cracken",
    "Col. Crac": "Colonel Cracken",
    "Out of Commission & Trans. Term": "Out Of Commission & Transmission Terminated",
    "All wings Report In & Dark. Spin": "All Wings Report In & Darklighter Spin",
    "Houjx & Out of Nowhere": "Houjix & Out Of Nowhere",
    "A tragedy has Occured": "A Tragedy Has Occurred",
    "Don't do that agian": "Don't Do That Again",
    "Big One": "Big One: Asteroid Cave Or Space Slug Belly",
    "Scimtar Squadron Tie Bomber": "Scimitar Squadron TIE",
    "Planetary Subjugation": "Planetary Subjugation",
    "Daulty Dofine": "Daultay Dofine",
    "Self Destruct Mechanism": "Self-Destruct Mechanism",
    "Rollin, Rolling, Rolling": "Rolling, Rolling, Rolling",
    "Master, Destroyers": "Master, Destroyers!",
    "Dark Maneuvers & Talon Roll": "Dark Maneuvers & Tallon Roll",
    "Dark Maneuvers/Talon Roll": "Dark Maneuvers & Tallon Roll",
    "Ghhk & Those Rebels Won't Escape Us": "Ghhhk & Those Rebels Won't Escape Us",
    "Dejarik Hologame Board": "Dejarik Hologameboard",
    "Endor System": "Endor",
    "Nebulon B-Frigate": "Nebulon-B Frigate",
    "Mara Jade, TEH": "Mara Jade, The Emperor's Hand",
    "TINT/Oppresive Enforcement": "There Is No Try & Oppressive Enforcement",
    "Maul's Double-Bladed Saber": "Maul's Double-Bladed Lightsaber",
    "Trooper Sabbac": "Trooper Sabacc",
    "Podrace Collision": "Podracer Collision",
    "Podrace Collission": "Podracer Collision",
    "Sense/Recoil in Fear": "Sense & Recoil In Fear",
    "Lt. Commander Arden": "Lieutenant Arnet",
    "Watto's Junkyard": "Tatooine: Watto's Junkyard",
    "Mos Espa": "Tatooine: Mos Espa",
    "Naboo: TP Gen Core": "Naboo: Theed Palace Generator Core",
    "Hoth: Echo Command Center(War Room)": "Hoth: Echo Command Center (War Room)",
    "Cloud City: East Platform(Docking Bay)": "Cloud City: East Platform (Docking Bay)",
    "Mos Espa: Docking Bay": "Tatooine: Mos Espa Docking Bay",
    "Yavin 4: War Room": "Yavin 4: Massassi War Room",
    "Tatooine: Obi Wan's Hut": "Tatooine: Obi-Wan's Hut",
    "Spaceport: Docking Bay": "Spaceport Docking Bay",
    # Page 60 slang (last-wins).
    "Darth Vader w/ Lightsaber": "Darth Vader With Lightsaber",
    "Lord Vader": "Lord Vader",
    "Maul's Lightsaber": "Maul's Double-Bladed Lightsaber",
    "Visage of the Emperor": "Visage Of The Emperor",
    "Fear is my Ally": "Fear Is My Ally",
    "They Will Be No Match for You": "They Will Be No Match For You",
    "Zuckuss in Mist Hunter": "Zuckuss In Mist Hunter",
    "Bossk in Hound's Tooth": "Bossk In Hound's Tooth",
    "This is Some Rescue!": "This Is Some Rescue!",
    "Masterful Move & Endor Occupation": "Masterful Move & Endor Occupation",
    "HB/SWSTYF": "Hidden Base",
    "Rend. point": "Rendezvous Point",
    "HB indecator": "Kessel",
    "The signal": "The Signal",
    "S-foils": "S-foils",
    "Boushe": "Boushh",
    "Obi w/saber": "Obi-Wan With Lightsaber",
    "Luke w/saber": "Luke With Lightsaber",
    "qui-gon w/saber": "Qui-Gon Jinn With Lightsaber",
    "x-Wing": "X-wing",
    "X-wing assult squad.": "X-wing Assault Squadron",
    "X-wing assult squad": "X-wing Assault Squadron",
    "x-wing laser cannon": "X-wing Laser Cannon",
    "Jedi resilance": "A Jedi's Resilience",
    "Jedi Resiliance": "A Jedi's Resilience",
    "We wish to bourd at once": "We Wish To Board At Once",
    "All wings report in": "All Wings Report In",
    "Organized attack": "Organized Attack",
    "Projection of a skywalker": "Projection Of A Skywalker",
    "The planet that its farthest from": "The Planet That's Farthest Away",
    "The Planet That It's Farthest From": "The Planet That's Farthest Away",
    "thrown back": "Thrown Back",
    "Tat(old one)": "Tatooine",
    "Coruscant(old one)": "Coruscant",
    "Aquaris(just for early force)": "Aquaris",
    "An unusual amount of fearfulness": "An Unusual Amount Of Fear",
    "QUIET MINING COLONY / independence": "Quiet Mining Colony",
    "Leia's Quarters": "Cloud City: West Gallery",
    "Head for the frigate": "Heading For The Medical Frigate",
    "Squdron Assignments": "Squadron Assignments",
    "KeepThe Empire Out": "Keep Your Eyes Open",
    "West Gallery": "Cloud City: West Gallery",
    "Incinerator": "Cloud City: Incinerator",
    "Carbon Chamber": "Cloud City: Carbonite Chamber",
    "CC Sector": "Bespin: Cloud City",
    "EPP Luke": "Luke With Lightsaber",
    "EPP Leia": "Leia With Blaster Rifle",
    "New Slave Leia": "Princess Leia, Slave",
    "Captain Han": "Captain Han Solo",
    "Lando Innocent Scoundrel": "Lando Calrissian, Scoundrel",
    "EPP Obi Wan": "Obi-Wan With Lightsaber",
    "EPP Qui gon": "Qui-Gon Jinn With Lightsaber",
    "ELyk Rhu": "Elyhek Rue",
    "Ten Numb, Superstar": "Ten Numb",
    "Wedge, RSL": "Wedge Antilles, Red Squadron Leader",
    "Pucimer Thryss": "Pucumir Thryss",
    "Falcon": "Millennium Falcon",
    "RedSquad 1": "Red Squadron 1",
    "Red 7": "Red Squadron 7",
    "Blue 5": "Blue Squadron 5",
    "Path ofleast Resistance": "Path Of Least Resistance",
    "ALter": "Alter",
    "All Wings Combo": "All Wings Report In & Darklighter Spin",
    "Off The Edge": "On The Edge",
    "Dont do that again": "Don't Do That Again",
    "Legendary Starfighter": "Legendary Starfighter",
    "X Wing Cannon": "X-wing Laser Cannon",
    "I'll Take the Leader": "I'll Take The Leader",
    "An Unsual Amount Of Fear": "An Unusual Amount Of Fear",
    "Innocent Scoundrel": "Innocent Scoundrel",
    "Wookie Strangle": "Wookiee Strangle",
    "Chewbacca, Enraged": "Chewie, Enraged",
    "Lando w/ Blaster Rifle": "Lando With Blaster Pistol",
    "Obi Wan w/ Lightsaber": "Obi-Wan With Lightsaber",
    "Heading For The Medical Frigage": "Heading For The Medical Frigate",
    "Do Or Do Not & Wise Advice": "Do, Or Do Not & Wise Advice",
    "You've Never Won A Podrace?": "You Have Never Won A Race?",
    "Captain Gilad Pallaeon": "Captain Gilad Pellaeon",
    "Dr. Evaazan & Ponda Baba": "Dr. Evazan & Ponda Baba",
    "Darth Maul's Double Bladed Lighstaber": "Maul's Double-Bladed Lightsaber",
    "Omni Box & It's Worse": "Ommni Box & It's Worse",
    "Tempest 1": "Tempest Scout 1",
    "you can either profit by this or be destroyed": "You Can Either Profit By This...",
    "audience chamber (with tk-422)": "Jabba's Palace: Audience Chamber",
    "jabbas palace": "Tatooine: Jabba's Palace",
    "pod racer prep": "Podrace Prep",
    "anikens pod": "Anakin's Podracer",
    "do or do not and wise advice": "Do, Or Do Not & Wise Advice",
    "luke/lightsaber": "Luke With Lightsaber",
    "chewbaca protector": "Chewbacca, Protector",
    "colenol cracken": "Colonel Cracken",
    "r2-x2": "R2-X2 (Artoo-Extoo)",
    "r'kik odec": "R'kik D'nec, Hero Of The Dune Sea",
    "general calrisian": "General Calrissian",
    "owen and beru": "Owen Lars & Beru Lars",
    "ardon vapor crell": "Ardon 'Vapor' Crell",
    "twass khaa": "Tawss Khaa",
    "mon calmari starship": "Mon Calamari Star Cruiser",
    "arc welder": "Arc Welder",
    "obiwans saber": "Obi-Wan's Lightsaber",
    "bo shuda": "Bo Shuda",
    "what are you tryin to push on us": "What're You Tryin' To Push On Us?",
    "no disentigrations": "No Disintegrations",
    "civil disorder": "Civil Disorder",
    "someone who loves you": "Someone Who Loves You",
    "i did it!": "I Did It!",
    "mon calmari": "Mon Calamari",
    "obi wans hut": "Tatooine: Obi-Wan's Hut",
    "city outscirts": "Tatooine: City Outskirts",
    "docking bay 94": "Tatooine: Docking Bay 94",
    "Do, Or Do Not& Wise Advice": "Do, Or Do Not & Wise Advice",
    "Do, Or Do Not & Wise Advice": "Do, Or Do Not & Wise Advice",
    "Insurrection& Aim High": "Insurrection & Aim High",
    "Artoo&Threepio": "See-Threepio",
    "Horox Ryder": "Horox Ryyder",
    "Sorry About The Mess & Blaster Proficiency": "Sorry About The Mess & Blaster Proficiency",
    "Out Of Commission & Transmission Terminated": "Out Of Commission & Transmission Terminated",
    "The Bith Shuffle & Desperate Reach": "The Bith Shuffle & Desperate Reach",
    "Run Luke, Run": "Run Luke, Run!",
    "ISB Objective": "ISB Operations",
    "Mob. Points": "Mobilization Points",
    "IAO & Secret Plans": "Imperial Arrest Order & Secret Plans",
    "Flagship Bridge": "Executor: Holotheatre",
    "Executor: DB": "Executor: Docking Bay",
    "Spaceport: DB": "Spaceport Docking Bay",
    "5D6-RA7": "5D6-RA-7 (Fivedesix)",
    "Commander Merrejek": "Commander Merrejk",
    "Admiral Chiranneu": "Admiral Chiraneau",
    "Epp Maul": "Darth Maul, Young Apprentice",
    "4-Lom With Gun": "4-LOM With Concussion Rifle",
    "Tie Cannon": "Boosted TIE Cannon",
    "MWYHL/SYIC": "Mind What You Have Learned",
    "Obi-Wan with Lighsaber": "Obi-Wan With Lightsaber",
    "Qui-Gon with Lightsaber": "Qui-Gon Jinn With Lightsaber",
    "Jar-Jar's Electropole": "Electropole",
    "Out of Commision & Transmission Terminated": "Out Of Commission & Transmission Terminated",
    "A Jedi's Resiliance": "A Jedi's Resilience",
    "Brisky Mornin' Munchin": "Brisky Morning Munchen",
    "Unctrollable Fury": "Uncontrollable Fury",
    "WED15-17 'Septoid' Droid": "WED15-I662 ('Septoid' Droid)",
    "Evacuate?": "Evader",
    "Beseiged": "Besieged",
    "This deal is getting worse all the time/Why did I get married?": (
        "This Deal Is Getting Worse All The Time"
    ),
    "Imp arrest order/secret plans": "Imperial Arrest Order & Secret Plans",
    "CC Upper Walkway": "Cloud City: Upper Walkway",
    "Mob points": "Mobilization Points",
    "Darth Vader dlots": "Darth Vader, Dark Lord Of The Sith",
    "Darth Maul, ya": "Darth Maul, Young Apprentice",
    "Thrawn": "Grand Admiral Thrawn",
    "Emp Palpatine -destiny 6": "Emperor Palpatine",
    "Dr E & Ponda Baba": "Dr. Evazan & Ponda Baba",
    "Baron Soonter Fel": "Baron Soontir Fel",
    "Xixor": "Prince Xizor",
    "OS 72-10": "OS-72-10",
    "P59": "P-59",
    "Saber 1": "Saber 1",
    "Saber 2": "Saber 2",
    "we must accelerate our plans": "We Must Accelerate Our Plans",
    "CC occupation": "Cloud City Occupation",
    "I'd just as soon kiss a wookie": "I'd Just As Soon Kiss A Wookiee",
    "imp supply": "Imperial Supply",
    "they must never again leave this city": "They Will Be Lost And Confused",
    "masterful move/endor occupation": "Masterful Move & Endor Occupation",
    "imp command": "Imperial Command",
    "Maul's jedi kabob": "Maul's Double-Bladed Lightsaber",
    "Sfs ls-9.3 laser cannons": "SFS L-s9.3 Laser Cannons",
    "carbonite chamber": "Cloud City: Carbonite Chamber",
    "west gallery": "Cloud City: West Gallery",
    "cloud city": "Bespin: Cloud City",
    "Agents In The Court/We Hate Imperials": "Agents In The Court",
    "Obi Wan's Apparition": "Obi-Wan's Apparition",
    "Nar Shadda Wind Chimes & Out Of Somewhere": "Nar Shaddaa Wind Chimes & Out Of Somewhere",
    "Yarna d'al Gargan": "Yarna d'al' Gargan",
    "han chewie and the falcon": "Han, Chewie, And The Falcon",
    "legendary starship": "Legendary Starfighter",
    "it coud be worse": "It Could Be Worse",
    "x wing las cannon": "X-wing Laser Cannon",
    "Dont'Do That Again": "Don't Do That Again",
    "The Sheild is Down!": "The Shield Is Down!",
    "Rebel Strike Team/Garrison Destroyed": "Rebel Strike Team",
    "Hoth: Docking Bay": "Hoth: Echo Docking Bay",
    "Hoth: War Room": "Hoth: Echo Command Center (War Room)",
    "Luke With Stick": "Luke With Lightsaber",
    "Obi-Wan With Stick": "Obi-Wan With Lightsaber",
    "DSII Wedge": "Wedge Antilles, Red Squadron Leader",
    "Hobbie": "Derek 'Hobbie' Klivian",
    "Obi's Stick": "Obi-Wan's Lightsaber",
    "Do, Or Do Not/ Wise Advice": "Do, Or Do Not & Wise Advice",
    "AOBS/VOTDP": "Agents Of Black Sun",
    "Coruscant (special Ed one)": "Coruscant",
    "YCHF & Mob. Pts.": "You Cannot Hide Forever & Mobilization Points",
    "YCHF & Mob. Pts": "You Cannot Hide Forever & Mobilization Points",
    "You Have Never Won A Race?": "You Have Never Won A Race?",
    "YCHF": "You Cannot Hide Forever",
    "CHYBC": "Come Here You Big Coward",
    "4-Lom w/Conc. Rifle": "4-LOM With Concussion Rifle",
    "Dengar w/ Carbine": "Dengar With Blaster Carbine",
    "Emperor Palpy": "Emperor Palpatine",
    "Sebulbas Pod": "Sebulba's Podracer",
    "Bossk In Bus": "Bossk In Hound's Tooth",
    "Mauls Ship": "Maul's Sith Infiltrator",
    "Zuckuss In Ship": "Zuckuss In Mist Hunter",
    "CC: Dbay": "Cloud City: East Platform (Docking Bay)",
    "Coruscant: Dbay": "Coruscant: Docking Bay",
    "D*II: Dbay": "Death Star II: Docking Bay",
    "Lat. Dmg.": "Lateral Damage",
    "Aurras Rifle": "Aurra Sing's Blaster Rifle",
    "HDADTJ": "Hunt Down And Destroy The Jedi",
    "Ex: Holo": "Executor: Holotheatre",
    "Ex: MC": "Executor: Meditation Chamber",
    "Darth Vader DLOTS": "Darth Vader, Dark Lord Of The Sith",
    "Darth Vader EPP": "Darth Vader With Lightsaber",
    "Darth Maul, YA 2": "Darth Maul, Young Apprentice",
    "4-LOM EJP": "4-LOM With Concussion Rifle",
    "Maul Strike": "Maul Strikes",
    "The Cirlce is Now Complete": "The Circle Is Now Complete",
    "Obi-Wans Lightsaber": "Obi-Wan's Lightsaber",
    "Anakins Lightsaber": "Anakin's Lightsaber",
    "Derek \"Hobbie\" Klivian": "Derek 'Hobbie' Klivian",
    "Tatooine:Jawa Camp": "Tatooine: Jawa Camp",
    "Tatooine:Jundland Wastes": "Tatooine: Jundland Wastes",
    "Tatooine:Lars' Moisture Farm": "Tatooine: Lars' Moisture Farm",
    "Star Destroyer:Launch Bay": "Star Destroyer: Launch Bay",
    "Death Star:War Room": "Death Star: War Room",
    "Tie Advancedx1": "TIE Advanced x1",
    "Enhanced Tie Laser Cannon": "Enhanced TIE Laser Cannon",
    "Boosted Tie Cannon": "Boosted TIE Cannon",
    "Tatooine: Hutt Trade Route": "Tatooine: Hutt Trade Route (Desert)",
    "Kalit": "Kalit",
    "Figrin D'an": "Figrin D'an",
    "Anakin's Saber": "Anakin's Lightsaber",
    "Endor: Landing Platform": "Endor: Landing Platform (Docking Bay)",
    "Endor: Rebel Landing Site": "Endor: Rebel Landing Site (Forest)",
    "There Is Good In Him/I Can Save Him": "There Is Good In Him",
    "Lieutenant s'too vees": "Lieutenant S'Too-Vees",
    "debnoli": "Debnoli",
    "hydroponics station": "Hydroponics Station",
    "The Planet That's Farthest Away": "The Planet That It's Farthest From",
    "The Planet That It's Farthest From": "The Planet That It's Farthest From",
    "Tat (old one)": "Tatooine",
    "Coruscant (old one)": "Coruscant",
    "Princess Leia, Slave": "Princess Leia Organa",
    "AO": "I'll Take The Leader",
    "qui gon jinn": "Qui-Gon Jinn",
    "obi wan kenobi": "Obi-Wan Kenobi",
    "Lieutenant S'Too-Vees": "Lieutenant s'Too Vees",
    "Lieutenant s'Too Vees": "Lieutenant s'Too Vees",
    "Ardon 'Vapor' Crell": 'Ardon "Vapor" Crell',
    'Ardon "Vapor" Crell': 'Ardon "Vapor" Crell',
    "No Disintegrations": "No Disintegrations!",
    "Do They Have A Code Clearance": "Do They Have A Code Clearance?",
    "Come Here You Big Cowards": "Come Here You Big Coward",
    "WED15-I662 ('Septoid' Droid)": "WED15-l7 'Septoid' Droid",
    "WED15-17 'Septoid' Droid": "WED15-l7 'Septoid' Droid",
    "WED15-l7 'Septoid' Droid": "WED15-l7 'Septoid' Droid",
    "CC: Port Town District": "Cloud City: Port Town District",
    "Lat. Dmg": "Lateral Damage",
    "Vibro-Axe": "Vibro-Ax",
    "4-LOM EJP": "4-LOM With Concussion Rifle",
    "–LOM EJP": "4-LOM With Concussion Rifle",
    "-LOM EJP": "4-LOM With Concussion Rifle",
    "docking bay": "Cloud City: East Platform (Docking Bay)",
    # Page 59 slang (last-wins).
    "RTP/SIAEM": "Rescue The Princess",
    "DS: DBC": "Death Star: Detention Block Corridor",
    "DS: DB": "Death Star: Docking Bay 327",
    "Y4: WR": "Yavin 4: Massassi War Room",
    "Y4: DB": "Yavin 4: Docking Bay",
    "Han EPP": "Han With Heavy Blaster Pistol",
    "Luke EPP": "Luke With Lightsaber",
    "Obi EPP": "Obi-Wan With Lightsaber",
    "D: Yoda's Hut": "Dagobah: Yoda's Hut",
    "H1: War Room": "Home One: War Room",
    "Obi wan's Lightsaber": "Obi-Wan's Lightsaber",
    "Gif t of the Mentor": "Gift Of The Mentor",
    "Do They Have A Code Clerance?": "Do They Have A Code Clearance?",
    "You've Never Won A Race!?": "You Have Never Won A Race?",
    "You've Never Won A Race": "You Have Never Won A Race?",
    "Maul with Lightsaber": "Darth Maul With Lightsaber",
    "Bib Fortuna (RIII)": "Bib Fortuna",
    "Elis Herlot": "Elis Helrot",
    "Neiomoidian Advisor": "Neimoidian Advisor",
    "Tatooine: Jabbas Palace": "Tatooine: Jabba's Palace",
    "Oo-ta-Goo-ta, Solo?": "Oo-ta Goo-ta, Solo?",
    "E: Holotheater": "Executor: Holotheatre",
    "E: Meditation Chamber": "Executor: Meditation Chamber",
    "T: Podrace Arena": "Tatooine: Podrace Arena",
    "No Escape (usually)": "No Escape",
    "Boba Fett: Bounty Hunter": "Boba Fett, Bounty Hunter",
    "Boba Fett; Bounty Hunter": "Boba Fett, Bounty Hunter",
    "Dr. E & Ponda Baba": "Dr. Evazan & Ponda Baba",
    "Dr Evezan and Ponda Boba": "Dr. Evazan & Ponda Baba",
    "Darth Maul YA": "Darth Maul, Young Apprentice",
    "Darth Vader w/saber": "Darth Vader With Lightsaber",
    "Darth Vader w/Lightsaber": "Darth Vader With Lightsaber",
    "Kedar the Black": "Keder the Black",
    "Broken Concentration (start v MWYHL)": "Broken Concentration",
    "Imperial Arrest Order/Secret Plans (alt start)": "Imperial Arrest Order & Secret Plans",
    "T: Docking Bay 94": "Tatooine: Docking Bay 94",
    "Phantom Menace": "The Phantom Menace",
    "Nemodian Advisor": "Neimoidian Advisor",
    "Zuckus in Mist Hunter": "Zuckuss In Mist Hunter",
    "Let' Them Make the First Move/At Last We Will Have Revenge": "Let Them Make The First Move",
    "Let Them Make the First Move/At Last We Will Have Revenge": "Let Them Make The First Move",
    "Lord Maul": "Darth Maul",
    "Destroyer Drois": "Destroyer Droid",
    "Dioxix": "Dioxis",
    "Aura Sing's Blaster Rifle": "Aurra Sing's Blaster Rifle",
    "We'll Handle This/Duel Of The Fates": "We'll Handle This",
    "We'll handle this/duel of the fates": "We'll Handle This",
    "Inner Strenght": "Inner Strength",
    "Brisky Morning Muchen": "Brisky Morning Munchen",
    "A Traegdy Has Occurred": "A Tragedy Has Occurred",
    "Captain Panka": "Captain Panaka",
    "Jar-Jar": "Jar Jar Binks",
    "Supreme Chanceller Valorum": "Supreme Chancellor Valorum",
    "Yaura": "Yarua",
    "Gimme A Lift": "Gimme A Lift!",
    "A Step Back": "A Step Backward",
    "A Step Backwards": "A Step Backward",
    "darth Mauls Demise": "Darth Maul's Demise",
    "Pankas gun": "Panaka's Blaster",
    "Jar-Jar Electropole": "Jar Jar's Electropole",
    "Jar-Jar's Electropole": "Jar Jar's Electropole",
    "TDIGWATT": "This Deal Is Getting Worse All The Time",
    "Naboo Generator": "Naboo: Theed Palace Generator",
    "Naboo Generator core": "Naboo: Theed Palace Generator Core",
    "Anakin's racer": "Anakin's Podracer",
    "obi with lightsaber": "Obi-Wan With Lightsaber",
    "quigon, jedi master": "Qui-Gon Jinn, Jedi Master",
    "yoda master of the force": "Yoda, Master Of The Force",
    "screaming lando": "Lando Calrissian, Scoundrel",
    "han chewie falcon": "Han, Chewie, And The Falcon",
    "Han, Chewie & The Falcon": "Han, Chewie, And The Falcon",
    "quigon's d5 saber": "Qui-Gon Jinn's Lightsaber",
    "x wing laser cannons": "X-wing Laser Cannon",
    "out of commission& tran terminated": "Out Of Commission & Transmission Terminated",
    "roo close for comfort": "Too Close For Comfort",
    "My Lord, Is That Legal?/I Will": "My Lord, Is That Legal?",
    "My Lord, Is That Legal?/I Will Make It Legal.": "My Lord, Is That Legal?",
    "IG-88 w/Riot Gun": "IG-88 With Riot Gun",
    "Mara Jade; Emperor's Hand": "Mara Jade, The Emperor's Hand",
    "Darth Maul w/Lightsaber": "Darth Maul With Lightsaber",
    "Ghhhk & Those Rebels Wont Escape Us": "Ghhhk & Those Rebels Won't Escape Us",
    "Get over here you Coward": "Come Here You Big Coward",
    "Oppressive Enforcment": "Oppressive Enforcement",
    "P59": "P-59",
    "P60": "P-60",
    "Plead My Case": "Plead My Case To The Senate",
    "Plead My Case...": "Plead My Case To The Senate",
    "COR: galatic Senate": "Coruscant: Galactic Senate",
    "COR: Jedi Council Chamber": "Coruscant: Jedi Council Chamber",
    "Sei Tara": "Sei Taria",
    "Queen Amidala, ruler!": "Queen Amidala",
    "Senator Paply": "Senator Palpatine",
    "Yoda, SCM": "Yoda, Senior Council Member",
    "Qui-Gon Jedi Master": "Qui-Gon Jinn, Jedi Master",
    "Jedi Luke": "Luke With Lightsaber",
    "Lando, Scoundrel": "Lando Calrissian, Scoundrel",
    "Wedge, Red Squad leader": "Wedge Antilles, Red Squadron Leader",
    "Red Squad 1": "Red Squadron 1",
    "Indipendence": "Independence",
    "Coruscant (new one)": "Coruscant",
    "Coruscant (SE)": "Coruscant",
    "COR: Docking Bay": "Coruscant: Docking Bay",
    "NAB: Docking Bay": "Naboo: Theed Palace Docking Bay",
    "NAB: Throne Room": "Naboo: Theed Palace Throne Room",
    "NAB: Courtyard": "Naboo: Theed Palace Courtyard",
    "NAB: Battle Plains": "Naboo: Battle Plains",
    "Luke's Saber": "Luke's Lightsaber",
    "Panaka's Balster": "Panaka's Blaster",
    "Qui-Gon's Saber(R3)": "Qui-Gon Jinn's Lightsaber",
    "Scrambled Transmissions": "Scrambled Transmission",
    "Qui-Gon Jinn w/ Lightsaber": "Qui-Gon Jinn With Lightsaber",
    "Intruder Missle": "Intruder Missile",
    "Nute Gunray, Neimodian Viceroy": "Nute Gunray, Neimoidian Viceroy",
    "OWO-1 w/ Backup": "OWO-1 With Backup",
    "After Her": "After Her!",
    "Battle Droid Blaster Rifles": "Battle Droid Blaster Rifle",
    "Invasion/In Complete Control": "Invasion",
    "Tactiacl Support": "Tactical Support",
    "Elite Squaron Stormtrooper": "Elite Squadron Stormtrooper",
    "Blaster Rifle": "Blaster Rifle",
    "You Cannot Hide Forever/Mobilization Points": "You Cannot Hide Forever & Mobilization Points",
    "Ortug": "Ortugg",
    "Prince Xixor": "Prince Xizor",
    "Maul's Lightsaber": "Maul's Double-Bladed Lightsaber",
    "Vibro Ax": "Vibro-Ax",
    "Mara Jade, TEH": "Mara Jade, The Emperor's Hand",
    "Darth Maul x2": "Darth Maul",
    "Lord Vader": "Lord Vader",
    "Maul's Double-bladed saber": "Maul's Double-Bladed Lightsaber",
    "Maul's saber (only 1 of the good kind)": "Maul's Double-Bladed Lightsaber",
    "Mara Jade's saber": "Mara Jade's Lightsaber",
    "Vader's saber": "Darth Vader's Lightsaber",
    "Hunt Down": "Hunt Down And Destroy The Jedi",
    "Twi'leck advisor": "Twi'lek Advisor",
    "Twi'leck Advisor": "Twi'lek Advisor",
    "Naboo : Theed Palace Generator Core": "Naboo: Theed Palace Generator Core",
    "Naboo : Theed Palace Generator": "Naboo: Theed Palace Generator",
    "I have You Now": "I Have You Now",
    "We'll Let Fate-a Decide, Huh": "We'll Let Fate-a Decide, Huh?",
    "Hoth: Echo Command Center": "Hoth: Echo Command Center (War Room)",
    "Artoo": "R2-D2 (Artoo-Detoo)",
    "Threepio": "C-3PO (See-Threepio)",
    "Chewie, Enraged": "Chewie",
    "Panaka, Protector of the Queen": "Captain Panaka",
    "Your Insights Serve You Well": "Your Insight Serves You Well",
    "bith shuffel and desperate reach": "The Bith Shuffle & Desperate Reach",
    "whaaaaaaaaaoooow!": "WHAAAAAAAAAOOOOW!",
    "Podrace arena": "Tatooine: Podrace Arena",
    "Naboo system": "Naboo",
    "Bossk In Hounds Tooth": "Bossk In Hound's Tooth",
    "Bossk in Hounds Tooth": "Bossk In Hound's Tooth",
    "Cloud City: East Platform": "Cloud City: East Platform (Docking Bay)",
    "Obi-Wan, Jedi Knight": "Obi-Wan Kenobi, Jedi Knight",
    "Liana Merian": "Liana Merian",
    "Phylo Gandish": "Phylo Gandish",
    "Stay Here Where it's Safe": "Stay Here, Where It's Safe",
    "Mindful Of The Force": "Mindful Of The Future",
    "R2-D2 In Red 5": "Red 5",
    "Spaceport:Docking Bay": "Spaceport Docking Bay",
    "Obi Wan Kenobi with Lightsaber": "Obi-Wan With Lightsaber",
    "A Jedi's Resiliance": "A Jedi's Resilience",
    "Out of Commission an Transmission Terminated": "Out Of Commission & Transmission Terminated",
    "Concussion Grenade": "Concussion Grenade",
    "General Solo": "General Solo",
    "General Han Solo": "General Solo",
    "Speak With Jedi Council": "Speak With The Jedi Council",
    "Speak With the Jedi Council": "Speak With The Jedi Council",
    "Gravest Of Circumstances": "The Gravest Of Circumstances",
    "Qui-Gon's Saber": "Qui-Gon Jinn's Lightsaber",
    "Maul's saber": "Maul's Double-Bladed Lightsaber",
    "At Last, We Are Getting Results": "At Last We Are Getting Results",
    "Chewie, Enraged": "Chewie, Enraged",
    "Tatooine (ep 1)": "Tatooine",
    "No Money, No Parts": "No Money, No Parts, No Deal!",
    "No Money, No Parts, No Deal/You're a Slave": "No Money, No Parts, No Deal!",
    "You Have Never Won A Race?": "You've Never Won A Race?",
    "You've Never Won A Race": "You've Never Won A Race?",
    "Fighter's Coming In": "Fighters Coming In",
    "SFS 9.3 Laser Cannon": "SFS L-s9.3 Laser Cannons",
    "Sniper/Dark Strike": "Sniper & Dark Strike",
    "Sniper/ Dark Strike": "Sniper & Dark Strike",
    "Darth Maul w/ Lightsaber": "Darth Maul With Lightsaber",
    "Darth Vader w/ Lighsaber": "Darth Vader With Lightsaber",
    "Darth Vader w/saber": "Darth Vader With Lightsaber",
    "4-LOM w/ Concussion Rifle": "4-LOM With Concussion Rifle",
    "4-Lom with Concussion Rifle": "4-LOM With Concussion Rifle",
    "Dr. Evazan/Ponda Baba": "Dr. Evazan & Ponda Baba",
    "Graga": "Gragra",
    "Darth Maul (tat)": "Darth Maul",
    "Darth Maul (Tatooine)": "Darth Maul",
    "Jabba's Palace": "Tatooine: Jabba's Palace",
    "Jabba's Audience Chamber": "Jabba's Palace: Audience Chamber",
    "Tatooine System": "Tatooine",
    "DS 2 Dbay": "Death Star II: Docking Bay",
    "You Cannot Hide Forever/Mob Points": "You Cannot Hide Forever & Mobilization Points",
    "YCHF/Mob. Points": "You Cannot Hide Forever & Mobilization Points",
    "you cannot hide forever/moby points": "You Cannot Hide Forever & Mobilization Points",
    "You Cannot Hide Forever/ Mobilization Points": "You Cannot Hide Forever & Mobilization Points",
    "Captain Dultay Dofine": "Captain Daultay Dofine",
    "Infintry Battle Droid": "Infantry Battle Droid",
    "STAP Laser Cannon": "STAP Blaster Cannons",
    "Halt": "Halt!",
    "We're Hit Artoo!": "We're Hit, Artoo",
    "We're Hit, Artoo": "We're Hit, Artoo",
    "Open Fire": "Open Fire!",
    "We Have A Plan (WHAP)": "We Have A Plan",
    "We Have A Plan /They Will Be Lost And Confused": "We Have A Plan",
    "We Have A Plan / They Will Be Lost And Confused": "We Have A Plan",
    "Theed Palace: Hallway": "Naboo: Theed Palace Hallway",
    "Theed palace: throne room": "Naboo: Theed Palace Throne Room",
    "brisky mornin munchen": "Brisky Morning Munchen",
    "Qui Gon": "Qui-Gon Jinn",
    "we dont have time for this": "We Don't Have Time For This",
    "We Don't Have Time for This": "We Don't Have Time For This",
    "panaka protector of the queen": "Panaka, Protector Of The Queen",
    "No Giben Up General Jar Jar": "No Giben Up, General Jar Jar!",
    "They win this round": "They Win This Round",
    "wesa gotta grand army": "Wesa Gotta Grand Army",
    "yoda master of the force": "Yoda, Master Of The Force",
    "Executor: Holotheater": "Executor: Holotheatre",
    "Prepared Defense": "Prepared Defenses",
    "Prep. Def.": "Prepared Defenses",
    "Search & Destroy": "Search And Destroy",
    "Zuckus In Mist Hunter": "Zuckuss In Mist Hunter",
    "Bossk In Hounds Tooth": "Bossk In Hound's Tooth",
    "Invasion/ In Complete Control": "Invasion",
    "Nothing Can Get Through Our Shields": "Nothing Can Get Through Our Shield",
    "Droid Rack": "Droid Racks",
    "Droid Racks": "Droid Racks",
    "Battle Droid Racks": "Droid Racks",
    "You May Begin Landing Your Troops": "Begin Landing Your Troops",
    "Cease Fire": "Cease Fire!",
    "Televann Koreyy": "Televan Koreyy",
    "Darth Maul w/ saber": "Darth Maul With Lightsaber",
    "Maul's ship": "Maul's Sith Infiltrator",
    "Ghhk/Those Rebels": "Ghhhk & Those Rebels Won't Escape Us",
    "Ghhk/Those Rebels...": "Ghhhk & Those Rebels Won't Escape Us",
    "Nemoidian Advisor": "Neimoidian Advisor",
    "Twi'lek": "Twi'lek Advisor",
    "Battle Order/First Strike": "Battle Order & First Strike",
    "Begin Landing Your Troops (Coruscant IAO)": "Begin Landing Your Troops",
    "Hoth: Echo Doccking Bay": "Hoth: Echo Docking Bay",
    "Maul with Double Saber": "Darth Maul With Lightsaber",
    "Vader with Saber": "Darth Vader With Lightsaber",
    "OWO-1 with Backup": "OWO-1 With Backup",
    "Imperial Arrest Order/ Secret Plans": "Imperial Arrest Order & Secret Plans",
    "iao/secret plans": "Imperial Arrest Order & Secret Plans",
    "Energy Shell Launcher": "Energy Shell Launchers",
    "Twilek Advisor": "Twi'lek Advisor",
    "y4: massassi war room": "Yavin 4: Massassi War Room",
    "yisw/staging areas": "Your Insight Serves You Well & Staging Areas",
    "insurrection/aim high": "Insurrection & Aim High",
    "home 1: db": "Home One: Docking Bay",
    "hoth: echo db": "Hoth: Echo Docking Bay",
    "epp obi-wan": "Obi-Wan With Lightsaber",
    "threepio whps": "Threepio With His Parts Showing",
    "qui-gon's ligtsaber": "Qui-Gon Jinn's Lightsaber",
    "home one": "Home One",
    "control/tunnel vision": "Control & Tunnel Vision",
    "Control/ Tunnel Vision": "Control & Tunnel Vision",
    "satm/blaster proficiency": "Sorry About The Mess & Blaster Proficiency",
    "where you looking for me?": "Were You Looking For Me?",
    "ooc/tt": "Out Of Commission & Transmission Terminated",
    "emporer palpatine": "Emperor Palpatine",
    "fett on crack": "Boba Fett With Blaster Rifle",
    "aurra": "Aurra Sing",
    "iggy with gun": "IG-88 With Riot Gun",
    "mauls double stick": "Maul's Double-Bladed Lightsaber",
    "maras stick": "Mara Jade's Lightsaber",
    "fetts blaster": "Boba Fett With Blaster Rifle",
    "aurras blaster": "Aurra Sing's Blaster Rifle",
    "Off The Edge": "Off The Edge",
    "visage of the emporer": "Visage Of The Emperor",
    "through the corridor": "Through The Corridor",
    "mara jade": "Mara Jade, The Emperor's Hand",
    "tarkin": "Grand Moff Tarkin",
    "executor db": "Executor: Docking Bay",
    "naboo db": "Naboo: Theed Palace Docking Bay",
    "Obi-Won w/lightsaber": "Obi-Wan With Lightsaber",
    "Han w/Heavy Blaster Pistol": "Han With Heavy Blaster Pistol",
    "Out of Commission & Transmission": "Out Of Commission & Transmission Terminated",
    "Terminated": "Transmission Terminated",
    "WHAAAAAAOOOOOOW!": "WHAAAAAAAAAOOOOW!",
    "SYCFA/THIS OBJECTIVE DON'T FLIP!": "Set Your Course For Alderaan",
    "Thok &Thug": "Thok & Thug",
    "Dr. Evazan's Sawed off Blaster": "Dr. Evazan's Sawed-off Blaster",
    "Dr. Evazan’s Sawed off Blaster": "Dr. Evazan's Sawed-off Blaster",
    "There is no Try/ Oppressive Enforcement": "There Is No Try & Oppressive Enforcement",
    "Jabba": "Jabba The Hutt",
    "Boba Fett in Slave 1": "Boba Fett In Slave I",
    "Dengar with Blaster Rifle": "Dengar With Blaster Carbine",
    "Power of the Hutt": "Power Of The Hutt",
    "Agents in the Court/ No Love for the Empire": "Agents In The Court",
    "Lando with Vibro ax": "Lando With Vibro-Ax",
    "Han with Heavy": "Han With Heavy Blaster Pistol",
    "Sense/ Recoil in Fear": "Sense & Recoil In Fear",
    "JP: Audience Chamber": "Jabba's Palace: Audience Chamber",
    "Lars' Moisture Farm": "Tatooine: Lars' Moisture Farm",
    "Lars’ Moisture Farm": "Tatooine: Lars' Moisture Farm",
    "WYS/This Place Can Be A Little Dangerous": "Watch Your Step",
    "Ralltir Freighter Captain": "Ralltiir Freighter Captain",
    "Lando in Falcon": "Lando In Millennium Falcon",
    "YT-1300 Class Freighter": "YT-1300 Transport",
    "We're Doomed!": "We're Doomed",
    "We’re Doomed!": "We're Doomed",
    "Houjix & Out of Nowhere": "Houjix & Out Of Nowhere",
    "How did We Get Into This Mess?": "How Did We Get Into This Mess?",
    "Lando with Blaster Rifle": "Lando With Blaster Rifle",
    "Death Star II (in hand)": "Death Star II",
    "Moff Jerjerrod (in hand)": "Moff Jerjerrod",
    "Desparate Counter (in hand)": "Desperate Counter",
    "Desparate Counter": "Desperate Counter",
    "SFS L-s 7.2 Cannon": "SFS L-s7.2 TIE Cannon",
    "COR: Galatic Senate (shiny)": "Coruscant: Galactic Senate",
    "COR: Galatic Senate": "Coruscant: Galactic Senate",
    "Supreme Chancellor valorum (shiny)": "Supreme Chancellor Valorum",
    "Senator Palpy": "Senator Palpatine",
    "Queen Amidala, Ruler": "Queen Amidala",
    "Qui-Gon, Jedi Master": "Qui-Gon Jinn, Jedi Master",
    "Depa Bilaba": "Depa Billaba",
    "CPT. Panaka": "Captain Panaka",
    "Han w/ Balster": "Han With Heavy Blaster Pistol",
    "Wedge, Red-Squad Leader": "Wedge Antilles, Red Squadron Leader",
    "Asscertaining The Truth": "Ascertaining The Truth",
    "Anakin's Racer (shiny)": "Anakin's Podracer",
    "Anakin's Racer": "Anakin's Podracer",
    "Red Sqaud 1": "Red Squadron 1",
    "NAB: Theed Courtyard": "Naboo: Theed Palace Courtyard",
    "NAB: Theed Generator": "Naboo: Theed Palace Generator",
    "Quiggy's Saber": "Qui-Gon Jinn's Lightsaber",
    "Quiggy's Saber (R3)": "Qui-Gon Jinn's Lightsaber",
    "Panaka's Balster": "Panaka's Blaster",
    "Tendau bendon": "Tendau Bendon",
    "Plead My Case to the Senate": "Plead My Case To The Senate",
    "Plead My Case to the Senate...": "Plead My Case To The Senate",
    "R2-D2 in Red 5": "Artoo-Detoo In Red 5",
    "R2-D2 In Red 5": "Artoo-Detoo In Red 5",
    "Red Leader in Red 1": "Red Leader In Red 1",
    "Indipendence": "Independence",
    "Threepio with his parts showing": "Threepio With His Parts Showing",
    "Yarna D’al Gargan": "Yarna d'al' Gargan",
    "Nar Shadda Wind chimes": "Nar Shaddaa Wind Chimes",
    "Hutt Trade Route": "Tatooine: Hutt Trade Route (Desert)",
    "<>Spaceport Docking bay": "Spaceport Docking Bay",
    "Spaceport Docking bay": "Spaceport Docking Bay",
    "Coruscant(Special Edition)": "Coruscant",
    "Tatooine: Docking Bay": "Tatooine: Docking Bay 94",
    "Cloud City: Platform 327": "Cloud City: Platform 327 (Docking Bay)",
    "Millenium Falcon": "Millennium Falcon",
    "X-Wing Laser Cannons": "X-Wing Laser Cannon",
    "Honor of the Jedi": "Honor Of The Jedi",
    "Tempest 1": "Tempest 1",
    "Blizzard Walker": "Blizzard Walker",
    "Imperial Walker": "Imperial Walker",
    "AT-AT Driver": "AT-AT Driver",
    "AT-ST Pilot": "AT-ST Pilot",
    "Energy Shell Launchers": "Energy Shell Launchers",
    "AAT Laser Cannon": "AAT Laser Cannon",
    "Battle Deployment": "Battle Deployment",
    "Walker Garrison": "Walker Garrison",
    "Trample": "Trample",
    "Debris Zone": "Debris Zone",
    "Mos Espa Docking Bay": "Tatooine: Mos Espa Docking Bay",
    "Mos Espa": "Tatooine: Mos Espa",
    "Watto's Junkyard": "Tatooine: Watto's Junkyard",
    "Blockade Flagship Bridge": "Blockade Flagship: Bridge",
    "Masterful Move/Endor Occupation": "Masterful Move & Endor Occupation",
    "Imperial Arrest Order/Secret Plans": "Imperial Arrest Order & Secret Plans",
    "Wipe Them Out, All of Them": "Wipe Them Out, All Of Them",
    "After Her": "After Her!",
    "Search and Destroy": "Search And Destroy",
    "Ghhhk/Those Rebels Won't Escape Us": "Ghhhk & Those Rebels Won't Escape Us",
    "There Is No Try/ Oppressive Enforcement": "There Is No Try & Oppressive Enforcement",
    "Operational as Planned": "Operational As Planned",
    "Power of the Hutt": "Power Of The Hutt",
    "Scum and Villainy": "Scum And Villainy",
    "Owen and Beru Lars": "Owen Lars & Beru Lars",
    "Han, Chewie, and the Falcon": "Han, Chewie, And The Falcon",
    "Seeking an Audience": "Seeking An Audience",
    "An Unusual amount of Fear": "An Unusual Amount Of Fear",
    "Yarna D'al Gargan": "Yarna d'al' Gargan",
    "Lando, Scoundrel": "Lando Calrissian, Scoundrel",
    "draw their fire": "Draw Their Fire",
    "tatooine: obi-wan's hut": "Tatooine: Obi-Wan's Hut",
    "coruscant: jedi council chamber": "Coruscant: Jedi Council Chamber",
    "dagobah: yoda's hut": "Dagobah: Yoda's Hut",
    "luke skywalker, jedi knight": "Luke Skywalker, Jedi Knight",
    "leia, rebel princess": "Leia, Rebel Princess",
    "dash rendar": "Dash Rendar",
    "revolution": "Revolution",
    "bacta tank": "Bacta Tank",
    "blaster deflection": "Blaster Deflection",
    "run luke, run!": "Run Luke, Run!",
    "a jedi's resilience": "A Jedi's Resilience",
    "prepared defenses": "Prepared Defenses",
    "naboo: theed palace generator core": "Naboo: Theed Palace Generator Core",
    "naboo: theed palace generator": "Naboo: Theed Palace Generator",
    "colo claw fish": "Colo Claw Fish",
    "darth sidious": "Darth Sidious",
    "janus greejatus": "Janus Greejatus",
    "sim aloo": "Sim Aloo",
    "snoova": "Snoova",
    "p-59": "P-59",
    "force lightning": "Force Lightning",
    "It's a Trap!": "It's A Trap!",
    "I Thought they Smelled Bad on the Outside": "I Thought They Smelled Bad On The Outside",
    "We Don't Have Time for This": "We Don't Have Time For This",
    "Gailid": "Gailid",
    "4-LOM With Concussion Rifle": "4-LOM With Concussion Rifle",
    "R2-D2": "R2-D2 (Artoo-Detoo)",
    "Chewie with Blaster Rifle": "Chewie With Blaster Rifle",
    "Heading for the Medical Frigate": "Heading For The Medical Frigate",
    "That Thing's Operational": "That Thing's Operational",
    "Boba Fett in Slave I": "Boba Fett In Slave I",
    "We Shall Double Our Efforts!": "We Shall Double Our Efforts!",
    "Sei Tara": "Sei Taria",
    "Jedi Luke": "Luke With Lightsaber",
    "Obi-Wan, Jedi Knight": "Obi-Wan Kenobi, Jedi Knight",
    "Might Of the Republic": "Might Of The Republic",
    "I've Decided To Go Back": "I've Decided To Go Back",
    "Stay Here Where It's Safe": "Stay Here, Where It's Safe",
    "I Will Not Defer": "I Will Not Defer",
    "Plea To The Court": "Plea To The Court",
    "Secure Route": "Secure Route",
    "Defiance": "Defiance",
    "Liberty": "Liberty",
    "Spiral": "Spiral",
    "Red 5": "Red 5",
    "Naboo": "Naboo",
    "NAB: Docking Bay": "Naboo: Theed Palace Docking Bay",
    "NAB: Throne Room": "Naboo: Theed Palace Throne Room",
    "COR: Docking Bay": "Coruscant: Docking Bay",
    "Luke's Saber": "Luke's Lightsaber",
    "Panaka's Blaster": "Panaka's Blaster",
    # Page 57 slang (last-wins).
    "Darth Vader With Lighsaber": "Darth Vader With Lightsaber",
    "Chimarea": "Chimaera",
    "My Lord, Is That Legal?/I Will Make It Legal": "My Lord, Is That Legal?",
    "Senate Overcam": "Senate Hovercam",
    "COTVG/ISEWYD": "Court Of The Vile Gangster",
    "Jabbas Palace: Audience Chamber": "Jabba's Palace: Audience Chamber",
    "Jabbas Palace: Dungeon": "Jabba's Palace: Dungeon",
    "Jabbas Palace: Rancor Pit": "Jabba's Palace: Rancor Pit",
    "Dengars Riot Gun": "Dengar's Modified Riot Gun",
    "Jade's Stick": "Mara Jade's Lightsaber",
    "Boba Fett's Gun": "Boba Fett's Blaster Rifle",
    "Mara Jade TEH": "Mara Jade, The Emperor's Hand",
    "Maul with double bladed stick": "Maul's Double-Bladed Lightsaber",
    "The Hyperdrive Generators Gone": "The Hyperdrive Generator's Gone",
    "Tatooine City Outskirts": "Tatooine: City Outskirts",
    "Tatooine Watto's Junkyard": "Tatooine: Watto's Junkyard",
    "Anakins Podracer": "Anakin's Podracer",
    "Bonta Eve Podrace": "Boonta Eve Podrace",
    "Brisky Morning Munchin": "Brisky Morning Munchen",
    "Lando w. Axe": "Lando With Vibro-Ax",
    "Quigon Jinn Jedi Master": "Qui-Gon Jinn, Jedi Master",
    "Obi-Wan PL": "Obi-Wan Kenobi, Padawan Learner",
    "Tendau Bandon": "Tendau Bendon",
    "Queens Royal Starship": "Queen's Royal Starship",
    "SATM/BP": "Sorry About The Mess & Blaster Proficiency",
    "S/RIF": "Sense & Recoil In Fear",
    "A/FF": "Alter & Friendly Fire",
    "Path of Least Resistance/Revealed": "Path Of Least Resistance & Revealed",
    "A Jedi's Resilliance": "A Jedi's Resilience",
    "A Jedi's Resilence": "A Jedi's Resilience",
    "YCEPBT/OBD": "You Can Either Profit By This...",
    "Tatooine: Obi's hutt": "Tatooine: Obi-Wan's Hut",
    "Tatooine: Toche Station": "Tatooine: Tosche Station",
    "Toche Station": "Tatooine: Tosche Station",
    "Han with Gun": "Han With Heavy Blaster Pistol",
    "Lando with Gun": "Lando With Blaster Pistol",
    "Chewie with Gun": "Chewie With Blaster Rifle",
    "Princess Leia Organna": "Princess Leia Organa",
    "Obiwan with Stick": "Obi-Wan With Lightsaber",
    "Its Not My Fault": "It's Not My Fault!",
    "It's Not My Fault": "It's Not My Fault!",
    "I Must be Allowed to Speak": "I Must Be Allowed To Speak",
    "I Must be Allowed to Speak/": "I Must Be Allowed To Speak",
    "Uh-oh": "Uh-oh!",
    "Do or Do Not": "Do, Or Do Not",
    "Watch Your Step/This Place Can Be A Little Rough": "Watch Your Step",
    "Tatooine (Premire)": "Tatooine",
    "Tatooine (Premiere)": "Tatooine",
    "Asteroid Sector": "Asteroid Field",
    "LE-B02D9": "LE-BO2D9 (Leebo)",
    "Wedge Antillies": "Wedge Antilles",
    "Wedge Antillies, Red Squadron Leader": "Wedge Antilles, Red Squadron Leader",
    "They'd Be Crazy To Follow Us": "They'd Be Crazy To Follow Us",
    "Quiet Mining Colony / Independent Organization": "Quiet Mining Colony",
    "Cloud City: 1/0 Site": "Cloud City: Upper Plaza Corridor",
    "Lando, The \"I Didn't Do It\" R3 Version": "Lando Calrissian, Scoundrel",
    "Elyek Rue": "Elyhek Rue",
    "Pucimir Thryss": "Pucumir Thryss",
    "Sorry About The Mess & Blaster Profiency": "Sorry About The Mess & Blaster Proficiency",
    "RTP/Sometimes I Amaze Even Myself": "Rescue The Princess",
    "Rescue The Princess/Sometimes I Amaze Even Myself": "Rescue The Princess",
    "D*: Detention Block Corridor": "Death Star: Detention Block Corridor",
    "D*: Docking Bay": "Death Star: Docking Bay 327",
    "Y4: War Room": "Yavin 4: Massassi War Room",
    "Han w/Heavy Blaster": "Han With Heavy Blaster Pistol",
    "Han w/ Heavy Blaster Pistol": "Han With Heavy Blaster Pistol",
    "OOC/Trans Term": "Out Of Commission & Transmission Terminated",
    "I Hope She's Allright": "I Hope She's All Right",
    "Home One DB": "Home One: Docking Bay",
    "Tatooine DB": "Tatooine: Docking Bay 94",
    "It's A Trap": "It's A Trap!",
    "Plead My Case/Sanity and Compassion": "Plead My Case To The Senate",
    "Plead My Case To The Senate / Sanity And Compassion": "Plead My Case To The Senate",
    "An Unuusual Amount of Fear": "An Unusual Amount Of Fear",
    "Han, Chewie an the Falcon": "Han, Chewie, And The Falcon",
    "Supreme Chancellor Valorrum": "Supreme Chancellor Valorum",
    "Padme Nabarrie": "Padme Naberrie",
    "Mace-Windu": "Mace Windu",
    "Alter/Friendly Fear": "Alter & Friendly Fire",
    "Alter/Friendly Fire": "Alter & Friendly Fire",
    "Sense (premiere)": "Sense",
    "Shocking Revelation/Grimtaash": "Shocking Information & Grimtaash",
    "Out of Commissiion/Transmission Terminated": "Out Of Commission & Transmission Terminated",
    "Disrupter Pistol": "Disruptor Pistol",
    "Admiral Chiranaeu": "Admiral Chiraneau",
    "Admiral Peitt": "Admiral Piett",
    "Bring Him Before Me/": "Bring Him Before Me",
    "Bring Him Before Me/Take Your Father's Place": "Bring Him Before Me",
    "Death Star 2: Docking Bay": "Death Star II: Docking Bay",
    "Death Star 2: Throne Room": "Death Star II: Throne Room",
    "Tatooine (Episode 1)": "Tatooine",
    "Obsession": "Vader's Obsession",
    "Yarna dal Gargan": "Yarna d'al' Gargan",
    "Qui Gons Saber": "Qui-Gon Jinn's Lightsaber",
    "Obi-Wans Saber": "Obi-Wan's Lightsaber",
    "Anakins Saber": "Anakin's Lightsaber",
    "Agents in the Court/...": "Agents In The Court",
    "Agents in the Court/": "Agents In The Court",
    "What Are You Trying To Push On Us?": "What're You Tryin' To Push On Us?",
    "Death Star: Central Control": "Death Star: Central Core",
    "Ounee Tay": "Ounee Ta",
    "Resistence": "Resistance",
    "*Resistence": "Resistance",
    "Wipe Them Out, All Of Tham": "Wipe Them Out, All Of Them",
    "CC: East Platform": "Cloud City: East Platform (Docking Bay)",
    "Dark Maneuvers/Tallon Roll": "Dark Maneuvers & Tallon Roll",
    "Proton Torpedos": "Proton Torpedoes",
    "Correlian Slip": "Corellian Slip",
    "Deactivate The Sheild Generator": "Deactivate The Shield Generator",
    "Blastech E-11B Blaster Rifle": "BlasTech E-11B Blaster Rifle",
    "Chewbacca of Kashyyyk": "Chewbacca Of Kashyyyk",
    "X-Wing": "X-wing",
    "Hunt down and destroy the jedi/thier fire has gone out of the universe": (
        "Hunt Down And Destroy The Jedi"
    ),
    "Holotheater": "Executor: Holotheatre",
    "Meditation Chamber": "Executor: Meditation Chamber",
    "Sebulbas": "Sebulba's Podracer",
    "Evader/Monnok": "Evader & Monnok",
    "Twi lek Advisor": "Twi'lek Advisor",
    "Do Or Do Not & Wise Advise": "Do, Or Do Not & Wise Advice",
    "Your Insights Serves You Well": "Your Insight Serves You Well",
    "Qui-Gon's Lightsaber": "Qui-Gon Jinn's Lightsaber",
    "Vaders Lightsaber": "Vader's Lightsaber",
    "Vader's Lightsaber": "Vader's Lightsaber",
    "Darth Vader's Lightsaber": "Darth Vader's Lightsaber",
    "Tempest 1": "Tempest Scout 1",
    "OS-72-1 in Obsidian 1": "OS-72-1 In Obsidian 1",
    "OS-72-2 in Obsidian 2": "OS-72-2 In Obsidian 2",
    "This Deal Is Getting Worse All The Time/...": "This Deal Is Getting Worse All The Time",
    "Do They Have A Code Clearance": "Do They Have A Code Clearance?",
    "The Phantom Menace (AI)": "The Phantom Menace",
    "Lt. Pol Treidum": "Lt. Pol Treidum",
    "I'll Take The Leader": "I'll Take The Leader",
    "I’ll Take The Leader": "I'll Take The Leader",
    "Off The Edge": "Off The Edge",
    "Lord Vader": "Lord Vader",
    "Flagship Executor": "Flagship Executor",
    "The Emperor": "The Emperor",
    "You've Never Won A Race?": "You've Never Won A Race?",
    "You Have Never Won A Race?": "You've Never Won A Race?",
    "Qui-Gon Jinns Lightsaber": "Qui-Gon Jinn's Lightsaber",
    "Sorry about the Mess/Blaster Proficiency": "Sorry About The Mess & Blaster Proficiency",
    "Obi-Wan's Lightsaber (premiere)": "Obi-Wan's Lightsaber",
    "Obi-Wans Lightsaber (Premiere Version)": "Obi-Wan's Lightsaber",
    "We Have a Plan/They Will be Lost and Confused": "We Have A Plan",
    "Your Insight Serves You Well/Staging Area's": "Your Insight Serves You Well & Staging Areas",
    "Shocking Information/Grimtaash": "Shocking Information & Grimtaash",
    "Out of Commision/Transmission Terminated": "Out Of Commission & Transmission Terminated",
    "Let Them Make The First Move/At Last We Will Have Our Revenge": "Let Them Make The First Move",
    "Let Them Make the First Move/At Last We Will Have Our Revenge": "Let Them Make The First Move",
    "Imperial Arrrest Order/Secret Plans": "Imperial Arrest Order & Secret Plans",
    "Battle Plan/ Draw Their Fire": "Battle Plan & Draw Their Fire",
    "Control/ Tunnel Vision": "Control & Tunnel Vision",
    "Crossifire": "Crossfire",
    "Inconaequential Losses": "Inconsequential Losses",
    "Nute Gunray, Nemoidian Viceroy": "Nute Gunray, Neimoidian Viceroy",
    "Drop Your Weapons!": "Drop Your Weapons",
    "Admiral Chinareau": "Admiral Chiraneau",
    "Vader's lighsaber": "Vader's Lightsaber",
    "Dr. Evezan": "Dr. Evazan",
    "Dreadnaught Class Heavy Cruiser": "Dreadnaught-Class Heavy Cruiser",
    "Death Star: Docking Bay": "Death Star: Docking Bay 327",
    "Astroid Field": "Asteroid Field",
    "Staging Area": "Staging Areas",
    "Had with Heavy Blaster Pistol": "Han With Heavy Blaster Pistol",
    "Chewie with Blaster Pistol": "Chewie With Blaster Rifle",
    "Squad Assignments": "Squadron Assignments",
    "Trail": "Endor: Hidden Forest Trail",
    "Dense Forest": "Endor: Dense Forest",
    "Ewok Sentries": "Ewok Sentry",
    "Geberal Crix Madine": "General Crix Madine",
    "Lt. Page": "Lieutenant Page",
    "EPP Obi": "Obi-Wan With Lightsaber",
    "U3PO": "U-3PO (Yoo-Threepio)",
    "Dark Manuevers & Tallon Roll": "Dark Maneuvers & Tallon Roll",
    "Operational as planed": "Operational As Planned",
    "Operational As Planned": "Operational As Planned",
    "Mobilization Points/ You cannot hide forever": "You Cannot Hide Forever & Mobilization Points",
    "You cannot hide forever": "You Cannot Hide Forever",
    "Death star 2": "Death Star II",
    "Death Star 2": "Death Star II",
    "DS2 Coolant shaft": "Death Star II: Coolant Shaft",
    "DS2 capacitors": "Death Star II: Capacitors",
    "Rendilli": "Rendili",
    "Renduli": "Rendili",
    "Lt Cabbel": "Lieutenant Cabbel",
    "Commander Merrijk": "Commander Merrejk",
    "Adm Motti": "Admiral Motti",
    "Adm Ozzel": "Admiral Ozzel",
    "Cpt Sarkli": "Captain Sarkli",
    "Darth maul with saber": "Darth Maul With Lightsaber",
    "Hoth power gen": "Hoth: Main Power Generators",
    "North ridge": "Hoth: North Ridge",
    "Hoth War room": "Hoth: Echo Command Center (War Room)",
    "Hoth corridor": "Hoth: Echo Corridor",
    "Hoth DB": "Hoth: Echo Docking Bay",
    "Chandrilla": "Chandrila",
    "Leia with blaster": "Leia With Blaster Rifle",
    "Han/blaster": "Han With Heavy Blaster Pistol",
    "Lt Blount": "Lieutenant Blount",
    "Lt. Blount": "Lieutenant Blount",
    "Princes Leia Organa": "Princess Leia Organa",
    "Ig-88 w/ riot gun": "IG-88 With Riot Gun",
    "Zuckess in Misthunter": "Zuckuss In Mist Hunter",
    "Distrupter Pistol": "Disruptor Pistol",
    "Wipe Them Out All Of Them": "Wipe Them Out, All Of Them",
    "Rise My Friend": "Rise, My Friend",
    "Endor Ops/": "Endor Operations",
    "Endor Ops": "Endor Operations",
    "Endo Ops": "Endor Operations",
    "Bunker": "Endor: Bunker",
    "Endor Docking Bay": "Endor: Landing Platform (Docking Bay)",
    "Ominous Rumours": "Ominous Rumors",
    "That Things Operational": "That Thing's Operational",
    "Twilek Advisors": "Twi'lek Advisor",
    "Gift of the Mentor": "Gift Of The Mentor",
    "Blaster Rack (VSC)": "Blaster Rack (V)",
    "Blaster Rack(VSC)": "Blaster Rack (V)",
    "Blaster Rack (Virtual Card)": "Blaster Rack (V)",
    "Blaster Rack (V-Card version)": "Blaster Rack (V)",
    "Darth Vader (Virtual)": "Darth Vader (V)",
    "Priestess (Virtual)": "Prophetess (V)",
    "Priestess (V)": "Prophetess (V)",
    "Darth Vader (virtual card!)": "Darth Vader (V)",
    "V Luke Skywalker": "Luke Skywalker (V)",
    "V BoShek": "Bo Shek (V)",
    "V Fusion Generator Supply Tanks": "Fusion Generator Supply Tanks (V)",
    "I Can't Shake Him": "I Can't Shake Him!",
    "Qui-Gon": "Qui-Gon Jinn",
    "EPP Vader": "Darth Vader With Lightsaber",
    "EPP Luke": "Luke Skywalker, Jedi Knight",
    "EPP Leia": "Leia With Blaster Rifle",
    "Han with Heavy Blaster Pistol": "Han With Heavy Blaster Pistol",
    "Leia with Blaster Rifle": "Leia With Blaster Rifle",
    "Luke's Lightsaber": "Luke's Lightsaber",
    "I Know": "I Know",
    "Protector": "Protector",
    # Page 56 slang (last-wins).
    "JPSD Lando": "Lando With Vibro-Ax",
    "Captian Gilad Pallaeon": "Captain Gilad Pellaeon",
    "Bane Maler": "Bane Malar",
    "Chimara": "Chimaera",
    "Chimera": "Chimaera",
    "Zuckuss in MistHunter": "Zuckuss In Mist Hunter",
    "Zuckuss in M.H": "Zuckuss In Mist Hunter",
    "Zuckuss in M.H.": "Zuckuss In Mist Hunter",
    "Bossk in H.T": "Bossk In Hound's Tooth",
    "Bossk in H.T.": "Bossk In Hound's Tooth",
    "enter the beaurocrat": "Enter The Bureaucrat",
    "Enter the beaurocrat": "Enter The Bureaucrat",
    "Omnious Rumors": "Ominous Rumors",
    "omnious rumors": "Ominous Rumors",
    "We are in attack position now": "We're In Attack Position Now",
    "All Wings Report In And Darklighter Spin": "All Wings Report In & Darklighter Spin",
    "Clearing": "Endor: Forest Clearing",
    "Signal": "The Signal",
    "Lt Blount": "Lieutenant Blount",
    "Jeron web": "Jeroen Webb",
    "Enranged chewie": "Chewie, Enraged",
    "Adm Ackbar": "Admiral Ackbar",
    "obi with saber": "Obi-Wan With Lightsaber",
    "Qui gon with saber": "Qui-Gon Jinn With Lightsaber",
    "Lando Calrisian, scoundrel": "Lando Calrissian, Scoundrel",
    "Gen Carlist Rieeken": "General Carlist Rieekan",
    "Gold squadron Ywings": "Gold Squadron Y-wing",
    "green squad Awing": "Green Squadron A-wing",
    "Blue squad B wing": "Blue Squadron B-wing",
    "Independance": "Independence",
    "Contol/Tunnel Vision": "Control & Tunnel Vision",
    "Nabrun lieds": "Nabrun Leids",
    "Echo base ops": "Echo Base Operations",
    "Mantillian savrip": "Mantellian Savrip",
    "Anakins pod racer": "Anakin's Podracer",
    "Ultimadum": "Ultimatum",
    "Kashyyk": "Kashyyyk",
    "Your Insights Serve You Well": "Your Insight Serves You Well",
    "Commander Merrijk": "Commander Merrejk",
    # Page 55 slang
    "I did It": "I Did It!",
    "Chewie Enraged": "Chewie, Enraged",
    "Qui Gon Jinn, Jedi Master": "Qui-Gon Jinn, Jedi Master",
    "Qui Gon Jedi Master": "Qui-Gon Jinn, Jedi Master",
    "Master Qui Gon": "Master Qui-Gon",
    "Qui Gon With Lightsaber": "Qui-Gon Jinn With Lightsaber",
    "Obi Wan Kenobi Jedi Knight": "Obi-Wan Kenobi, Jedi Knight",
    "A tremor (or disturbance I forget exactly what its called) in the force": (
        "A Tremor In The Force"
    ),
    "Qui Gon Jinn's Lightsaber": "Qui-Gon Jinn's Lightsaber",
    "Quis Saber": "Qui-Gon Jinn's Lightsaber",
    "Carbon Chamber Tasting /My Favorite Decoration": "Carbon Chamber Testing",
    "Carbon Chamber Tasting / My Favorite Decoration": "Carbon Chamber Testing",
    "Carbonit Chamber Console": "Carbonite Chamber Console",
    "Bragus Glee": "Brangus Glee",
    "Tatoine: Docking Bay 94": "Tatooine: Docking Bay 94",
    "Executer": "Executor",
    "You Can Either Profit By This": "You Can Either Profit By This...",
    "You Can Either Profit By This/Or Be Destroyed": "You Can Either Profit By This...",
    "You Can Either Profit By This.../ Or Be Destroyed": "You Can Either Profit By This...",
    "You Can Either Profit By This.../Or Be Destroyed": "You Can Either Profit By This...",
    "Tatooine: Audience Chamber": "Jabba's Palace: Audience Chamber",
    "Projectino of a Skywalker": "Projection Of A Skywalker",
    "Captain Daulty Dofine": "Captain Daultay Dofine",
    "3B3-1024": "3B3-1204",
    "Droid Starfighter Laser Cannon": "Droid Starfighter Laser Cannons",
    "There Is Good In Him/I Feel The Conflict": "There Is Good In Him",
    "Arto, Brave Little Droid": "Artoo, Brave Little Droid",
    "no money, no parts, no deal": "No Money, No Parts, No Deal!",
    "No Money, No parts, No deal/ You're A Slave?": "No Money, No Parts, No Deal!",
    "wattos junkyard": "Tatooine: Watto's Junkyard",
    "Tat: Watt's Junkyard": "Tatooine: Watto's Junkyard",
    "jundland wastes": "Tatooine: Jundland Wastes",
    "lars moisture farm": "Tatooine: Lars' Moisture Farm",
    "maul with saber": "Darth Maul With Lightsaber",
    "televynn koreyy": "Televan Koreyy",
    "dr. e and ponda baba": "Dr. Evazan & Ponda Baba",
    "Dr. Evanzan & Ponda Baba": "Dr. Evazan & Ponda Baba",
    "DR. E/Ponda Boba": "Dr. Evazan & Ponda Baba",
    "DrE Combo": "Dr. Evazan & Ponda Baba",
    "Bring Him Before Me/He is Before Me": "Bring Him Before Me",
    "SYCFA": "Set Your Course For Alderaan",
    "DS DB": "Death Star: Docking Bay 327",
    "Alderan": "Alderaan",
    "Prepared d": "Prepared Defenses",
    "Prepaired Defenses": "Prepared Defenses",
    "Mobpoints": "Mobilization Points",
    "Mobolizaiton Points": "Mobilization Points",
    "IAO/SP": "Imperial Arrest Order & Secret Plans",
    "Secret Plans/IAO": "Imperial Arrest Order & Secret Plans",
    "Inconsequental Losses": "Inconsequential Losses",
    "DS War": "Death Star: War Room",
    "Piett": "Admiral Piett",
    "Mejjerick": "Commander Merrejk",
    "Ref 3 Fett": "Boba Fett, Bounty Hunter",
    "Garrison": "Walker Garrison",
    "Interceptor": "TIE Interceptor",
    "SFS": "SFS L-s9.3 Laser Cannons",
    "SFS Laser Cannons": "SFS L-s9.3 Laser Cannons",
    "SFS 9.3 laser cannons": "SFS L-s9.3 Laser Cannons",
    "I cant Shake him": "I Can't Shake Him!",
    "Sineer Fleet Systems": "Sienar Fleet Systems",
    "Dreaded Imperial Star Fleet": "Dreaded Imperial Starfleet",
    "HB": "Hidden Base",
    "Rendevous Point": "Rendezvous Point",
    "Endor Back Door": "Endor: Back Door",
    "squad assign": "Squadron Assignments",
    "Aim High/Insurrection": "Insurrection & Aim High",
    "Thats One": "That's One",
    "X-Wing Cannons": "X-wing Laser Cannon",
    "Qui-Gonn Jinn": "Qui-Gon Jinn",
    "Crix Madine": "General Crix Madine",
    "General Clarissian": "General Calrissian",
    "Jedi's Resilience": "A Jedi's Resilience",
    "Jedi Resilence": "A Jedi's Resilience",
    "Cloud City Chasm Walkway": "Cloud City: Chasm Walkway",
    "Cloud City Lower Corridor": "Cloud City: Lower Corridor",
    "Cloud City West Gallery": "Cloud City: West Gallery",
    "Cloud City Docking Bay": "Cloud City: Platform 327 (Docking Bay)",
    "Maul with Double Bladed Saber": "Darth Maul With Lightsaber",
    "Boba Fett (special Ed)": "Boba Fett",
    "Major Turr Phenrir": "Major Turr Phennir",
    "Admiral Piet": "Admiral Piett",
    "Mob Points/YCHF": "You Cannot Hide Forever & Mobilization Points",
    "Fetts Blaster Rifle": "Boba Fett's Blaster Rifle",
    "DR E's Gun": "Dr. Evazan's Sawed-off Blaster",
    "COTVG": "Court Of The Vile Gangster",
    "Dungeon": "Jabba's Palace: Dungeon",
    "Pit of Carkoon": "Tatooine: Great Pit Of Carkoon",
    "Galid": "Gailid",
    "Rancor Pit": "Jabba's Palace: Rancor Pit",
    "Lando Calirrision, Scoundrel": "Lando Calrissian, Scoundrel",
    "Lando With Vibro Axe": "Lando With Vibro-Ax",
    "Ric Olié": "Ric Olie",
    "Anackin's Lightsaber": "Anakin's Lightsaber",
    "Spaceport DB": "Spaceport Docking Bay",
    "Tatooine: Mos Espa DB": "Tatooine: Mos Espa Docking Bay",
    "Lt. Arnet": "Lieutenant Arnet",
    "Mauls Double-Bladed Lightsaber": "Maul's Double-Bladed Lightsaber",
    "Mauls Double": "Maul's Double-Bladed Lightsaber",
    "Id Just As Soon Kiss a Wookie": "I'd Just As Soon Kiss A Wookiee",
    "We'll Handle this/Duel of Fates": "We'll Handle This",
    "Inner strengh": "Inner Strength",
    "Generator": "Naboo: Theed Palace Generator",
    "Generator Core": "Naboo: Theed Palace Generator Core",
    "Heading for the Medical": "Heading For The Medical Frigate",
    "Insights": "Your Insight Serves You Well",
    "Sal'torr Kal Fas (V)": "Sai'torr Kal Fas (V)",
    "Sai'torr Kal Faas (v)": "Sai'torr Kal Fas (V)",
    "Sai'torr Kal Faas (V)": "Sai'torr Kal Fas (V)",
    "Jedi Council Chamber": "Coruscant: Jedi Council Chamber",
    "Mace Windu Jedi Master": "Mace Windu, Jedi Master",
    "Parts out there Threepio": "Threepio With His Parts Showing",
    "Threepio with Parts Showing": "Threepio With His Parts Showing",
    "Intruider Missle": "Intruder Missile",
    "Han, Chewie Falcon": "Han, Chewie, And The Falcon",
    "Bith Shuffle/Despereate Reach": "The Bith Shuffle & Desperate Reach",
    "Shocking/Grimtassh": "Shocking Information & Grimtaash",
    "Free Ride/Endor Cele": "Free Ride & Endor Celebration",
    "Were you looking for me": "Were You Looking For Me?",
    "Houjix/Outa Nowhere": "Houjix & Out Of Nowhere",
    "Speak with the Council": "Speak With The Jedi Council",
    "Barrier": "Rebel Barrier",
    "Let them make the first move/At last we have revenge": "Let Them Make The First Move",
    "Start ur Engines": "Start Your Engines!",
    "Boonta Eve": "Boonta Eve Podrace",
    "Wattos Box": "Watto's Box",
    "Blockade Bridge": "Blockade Flagship: Bridge",
    "Emperor": "Emperor Palpatine",
    "Emperor Palpantine": "Emperor Palpatine",
    "4-lom with conc": "4-LOM With Concussion Rifle",
    "Xizor": "Prince Xizor",
    "Boba Bounty Hunter": "Boba Fett, Bounty Hunter",
    "Iggy with Riot": "IG-88 With Riot Gun",
    "Vaders Saber": "Vader's Lightsaber",
    "Phantom Meanace": "The Phantom Menace",
    "Seach and Destroy": "Search And Destroy",
    "Ommni box/Its worse": "Ommni Box & It's Worse",
    "WE must accelerate plans": "We Must Accelerate Our Plans",
    "Circle": "The Circle Is Now Complete",
    "This some Rescue": "This Is Some Rescue!",
    "Pod collision": "Podracer Collision",
    "Sorry About The Mess & Blaster Profieciency": "Sorry About The Mess & Blaster Proficiency",
    "Tat: Tosche Station": "Tatooine: Tosche Station",
    "Tat: Cantina": "Tatooine: Cantina",
    "Tat: Mos Espa": "Tatooine: Mos Espa",
    "Tat: Podrace Arena": "Tatooine: Podrace Arena",
    "Tat: Marketplace": "Tatooine: Marketplace",
    "Sniper and Dark Strike": "Sniper & Dark Strike",
    # Page 54 slang (last-wins).
    "Horax Ryyder": "Horox Ryyder",
    "Mace Windo": "Mace Windu",
    "Tatoonie": "Tatooine",
    "DSF-1308": "DFS-1308",
    "Invasion/Complete Control": "Invasion",
    "Nute Gunray, Viceroy": "Nute Gunray, Neimoidian Viceroy",
    "Watch Your Setp": "Watch Your Step",
    "Heading for the Frigate": "Heading For The Medical Frigate",
    "heading for the boat": "Heading For The Medical Frigate",
    "Squad Ass": "Squadron Assignments",
    "Wedge (ANH)": "Wedge Antilles",
    "Chewie with Blaster": "Chewie With Blaster Rifle",
    "Yotts Oren": "Yotts Orren",
    "Honor of a Jedi": "Honor Of The Jedi",
    "out of control/transmission terminated": (
        "Out Of Commission & Transmission Terminated"
    ),
    "it's a hit": "It's A Hit!",
    "all wings/darklighter spin": "All Wings Report In & Darklighter Spin",
    "free ride/endor celebration": "Free Ride & Endor Celebration",
    "houjix/out of Nowhere": "Houjix & Out Of Nowhere",
    "Houjix/Out of Nowhere": "Houjix & Out Of Nowhere",
    "Sai-Tor KalFas (V)": "Sai'torr Kal Fas (V)",
    "saitor kal fas (V)": "Sai'torr Kal Fas (V)",
    "Naked Threepio": "Threepio With His Parts Showing",
    "Qui-Gonn w/stick": "Qui-Gon Jinn With Lightsaber",
    "Wedge Antilles, Red leader": "Wedge Antilles, Red Squadron Leader",
    "Capt. Han Solo": "Captain Han Solo",
    "Lando w/Ax": "Lando With Vibro-Ax",
    "Yarn'Al'Gargan": "Yarna d'al' Gargan",
    "Millenium Falcon (old)": "Millennium Falcon",
    "OOC/Trans. Terminated": "Out Of Commission & Transmission Terminated",
    "Chewie's Bowcaster": "Chewbacca's Bowcaster",
    "Theed Palace Generator": "Naboo: Theed Palace Generator",
    "Executor Docking Bay": "Executor: Docking Bay",
    "Darth maul's double-bladed Lightsaber": "Maul's Double-Bladed Lightsaber",
    "Mobilization Points/You Cannot Hide forever": (
        "You Cannot Hide Forever & Mobilization Points"
    ),
    "Monnok/Evader": "Evader & Monnok",
    "Ric Olié, Bravo Leader": "Ric Olie, Bravo Leader",
    "Hidden Base/Systems will Slip": "Hidden Base",
    "The Spiral": "Spiral",
    "A Few Manuevers": "A Few Maneuvers",
    "a few manuevers": "A Few Maneuvers",
    "We'll Handle This/ Duel Of The Fates": "We'll Handle This",
    "CC: West Gallery": "Cloud City: West Gallery",
    "Vader w/ Stick": "Darth Vader With Lightsaber",
    "Maul w/ Stick": "Darth Maul With Lightsaber",
    "Dr. E/Ponda Baba": "Dr. Evazan & Ponda Baba",
    "Mara's Stick": "Mara Jade's Lightsaber",
    "Quiet Mining Colony/Independent Operation": "Quiet Mining Colony",
    "CC: Guest Guarters": "Cloud City: Guest Quarters",
    "CC: Carbon Chamber": "Cloud City: Carbonite Chamber",
    "CC: Platform 327": "Cloud City: Platform 327 (Docking Bay)",
    "EPP Qui-gon": "Qui-Gon Jinn With Lightsaber",
    "epp quigon": "Qui-Gon Jinn With Lightsaber",
    "Atroo, BLD": "Artoo, Brave Little Droid",
    "All Wing Report In/Darklighter Spin": "All Wings Report In & Darklighter Spin",
    "Kaskyyyk": "Kashyyyk",
    "Rallitiir Freighter Captain": "Ralltiir Freighter Captain",
    "Nar Shada Wind Chimes": "Nar Shaddaa Wind Chimes",
    "General Jar-Jar": "General Jar Jar",
    "Kaado": "Kaadu",
    "No Giben Up, General Jar Jar": "No Giben Up, General Jar Jar!",
    "Slight Weapons Malfunctions": "Slight Weapons Malfunction",
    "Captain Tarpels Electropole": "Captain Tarpals' Electropole",
    "The Hyperdrive Generator's Gone/The 7 side": "The Hyperdrive Generator's Gone",
    "Tat: Watto's Junkyard": "Tatooine: Watto's Junkyard",
    "Tat: City Outskirts": "Tatooine: City Outskirts",
    "claw fish": "Colo Claw Fish",
    "tat obi": "Obi-Wan Kenobi, Padawan Learner",
    "tat panaka": "Captain Panaka",
    "cc lando": "Lando Calrissian",
    "anh chewie": "Chewbacca",
    "crscnt ric ole": "Ric Olie",
    "Boshek (V)": "Bo Shek (V)",
    "BoShek (V)": "Bo Shek (V)",
    "bravo scrub 2": "Bravo 2",
    "bravo scrub 3": "Bravo 3",
    "panaka's gun": "Panaka's Blaster",
    "xwing cannon": "X-wing Laser Cannon",
    "ric's ship": "Bravo 1",
    "No Money, No Parts, No Deal / You're A Slave": "No Money, No Parts, No Deal!",
    "YCHF / MOB": "You Cannot Hide Forever & Mobilization Points",
    "IAO / Secret Plans": "Imperial Arrest Order & Secret Plans",
    "Dr. Evazon & Panda Baba": "Dr. Evazan & Ponda Baba",
    "Tatoonie Occupation": "Tatooine Occupation",
    "TINT & OE": "There Is No Try & Oppressive Enforcement",
    "sab'e": "Sabe",
    "shimi skywalker": "Shmi Skywalker",
    "obi-wan lightsaber": "Obi-Wan's Lightsaber",
    "armanent dismantled": "Armament Dismantled",
    "vote now": "Vote Now!",
    "you'll find i'm full of suprises": "You'll Find I'm Full Of Surprises",
    "tatoonine": "Tatooine",
    "dantoonine": "Dantooine",
    "Darth Maul, Sith Apprentice": "Darth Maul, Young Apprentice",
    "Admiral Thrawn": "Grand Admiral Thrawn",
    "I-G88 With Riot Gun": "IG-88 With Riot Gun",
    "Dr.E / Ponda Boba": "Dr. Evazan & Ponda Baba",
    "Vader's Stick": "Vader's Lightsaber",
    "Darth Maul's Double Stick": "Maul's Double-Bladed Lightsaber",
    "Mara Jade's Stick": "Mara Jade's Lightsaber",
    "Chimeras": "Chimaera",
    "All to Easy": "All Too Easy",
    "Cloud City: Droid Incinerator": "Cloud City: Incinerator",
    "No, No, No/You're a slave?!?": "No Money, No Parts, No Deal!",
    "Spaceport Dockingbay": "Spaceport Docking Bay",
    "Colonel David Jon": "Colonel Davod Jon",
    "Projective Telapathy": "Projective Telepathy",
    "Lando With Vibro-Axe": "Lando With Vibro-Ax",
    "Ralltiir Ops": "Ralltiir Operations",
    "Lt. Watts": "Lieutenant Watts",
    "Sgt. Barich": "Sergeant Barich",
    "Sgt. Elsek": "Sergeant Elsek",
    "Sgt. Irol": "Sergeant Irol",
    "Besipin": "Bespin",
    "Cloud City DB": "Cloud City: Docking Bay",
    "Cloud City Guest Quarters": "Cloud City: Guest Quarters",
    "Cloud City Carbonite Chamber": "Cloud City: Carbonite Chamber",
    "Leia Rebel Princess": "Leia, Rebel Princess",
    "Luke Skywalker Jedi Knight": "Luke Skywalker, Jedi Knight",
    "Obi Wan with Lightsaber": "Obi-Wan With Lightsaber",
    "Qui Gon with Lightsaber": "Qui-Gon Jinn With Lightsaber",
    "Luke with Lightsaber": "Luke With Lightsaber",
    "Han with Heavy Blaster Pistol": "Han With Heavy Blaster Pistol",
    "Chewie with Blaster Rifle": "Chewie With Blaster Rifle",
    "Lando with Blaster Pistol": "Lando With Blaster Pistol",
    "Leia with Blaster Rifle": "Leia With Blaster Rifle",
    "Threepio with Parts Showing": "Threepio With His Parts Showing",
    "Chewbacca Protector": "Chewbacca, Protector",
    "Lando Scoundrel": "Lando Calrissian, Scoundrel",
    "Boshek": "BoShek",
    "Wedge Red Squadren Leader": "Wedge Antilles, Red Squadron Leader",
    "Puccimr Thyrss": "Pucumir Thryss",
    "Artoo Brave Little Droid": "Artoo, Brave Little Droid",
    "Artoo-Detoo, Brave Little Droid": "Artoo, Brave Little Droid",
    "Blast The Door Kid": "Blast The Door, Kid!",
    "Corran Horne": "Corran Horn",
    "Millenium Falcon": "Millennium Falcon",
    "Red Squadren 1": "Red Squadron 1",
    "Squadren Assignments": "Squadron Assignments",
    "X-Wing Laser Cannons": "X-wing Laser Cannon",
    "Run Luke Run": "Run Luke, Run!",
    "All Wings Report In/Darklighter Spin": "All Wings Report In & Darklighter Spin",
    "Sorry About The Mess/Blaster proficiency": "Sorry About The Mess & Blaster Proficiency",
    "I'll Take the Leader": "I'll Take The Leader",
    "Insurrection and Aim High": "Insurrection & Aim High",
    "Obi's Journal": "Obi-Wan's Journal",
    "Do They Have Code Clearance": "Do They Have A Code Clearance?",
    "Naboo: Theed Palce Generator Core": "Naboo: Theed Palace Generator Core",
    "Moff Jejerrod": "Moff Jerjerrod",
    "Storm Trooper Garrison": "Stormtrooper Garrison",
    "Blockade Flagship Hallway": "Blockade Flagship: Hallway",
    "Executer: Holotherater": "Executor: Holotheatre",
    "Naboo Theed Palace Generator": "Naboo: Theed Palace Generator",
    "Imperial Artilery": "Imperial Artillery",
    "Battle Drois Blaster": "Battle Droid Blaster Rifle",
    "Maul's Double Bladded Lightsaber": "Maul's Double-Bladed Lightsaber",
    "Naboo Theed Docking Bay": "Naboo: Theed Palace Docking Bay",
    "Scum & Villainy": "Scum And Villainy",
    "Were The Bait": "We're The Bait",
    "Mandalorian Battle Armor": "Mandalorian Armor",
    "Hounds Tooth": "Hound's Tooth",
    "Bosk with Motar Gun": "Bossk With Mortar Gun",
    "Laria": "Labria",
    "Naboo: Boss Nass Chambers": "Naboo: Boss Nass' Chambers",
    "Caldera Righam": "Caldera Righim",
    "Direct Assult": "Direct Assault",
    "Percise Hit": "Precise Hit",
    "Chewie of Kashyyyk": "Chewbacca Of Kashyyyk",
    "Chief Charpa": "Chief Chirpa",
    "Ewok Trbesman": "Ewok Tribesman",
    "Luke, Rebel Scout": "Luke Skywalker, Rebel Scout",
    "Ewok Catapault": "Ewok Catapult",
    "The Hyperdrive Generator's Gone/ We'll need a New One": "The Hyperdrive Generator's Gone",
    "Heading for the Heading Medical Frigate": "Heading For The Medical Frigate",
    "Obi-Wan, Padawan Learner": "Obi-Wan Kenobi, Padawan Learner",
    "Padmée Naberrrie": "Padme Naberrie",
    "What're you tryin' to push on us": "What're You Tryin' To Push On Us?",
    "Goo nee tai": "Goo Nee Tay",
    "Yoda's stew & you do have your moments": "Yoda Stew & You Do Have Your Moments",
    "Out of commission & Transmision terminated": "Out Of Commission & Transmission Terminated",
    "Let Them Make a Move": "Let Them Make The First Move",
    "Seb's Racer": "Sebulba's Podracer",
    "Theed Palace Docking Bay": "Naboo: Theed Palace Docking Bay",
    "Dr. Evazan & PB": "Dr. Evazan & Ponda Baba",
    "Fett in Slv I": "Boba Fett In Slave I",
    "Bossk in Tooth": "Bossk In Hound's Tooth",
    "IG in IG-2000": "IG-88 In IG-2000",
    "Zickuss in MH": "Zuckuss In Mist Hunter",
    "Maul's Double-Lightsaber": "Maul's Double-Bladed Lightsaber",
    "Blaster Rack (Original)": "Blaster Rack",
    "Alderaan system": "Alderaan",
    "Death Star system": "Death Star",
    "DS: Docking Bay 327": "Death Star: Docking Bay 327",
    "Cpt. Yorr": "Captain Yorr",
    "Mjr Turr Phennir": "Major Turr Phennir",
    "Cpt Lennox": "Captain Lennox",
    "Cmdr Brandei": "Commander Brandei",
    "Lt Pol Treidum": "Lt. Pol Treidum",
    "Lieutenant Pol Treidum": "Lt. Pol Treidum",
    "Imperial Trooper Guard Diansom": "Imperial Trooper Guard Dainsom",
    "All power to weaopns": "All Power To Weapons",
    "DS: War Room": "Death Star: War Room",
    "DS Docking Bay control room 327": "Death Star: Docking Control Room 327",
    "DS: level 4 military corridor": "Death Star: Level 4 Military Corridor",
    "DS: Conference Room": "Death Star: Conference Room",
    "Denegar in Punishing One": "Dengar In Punishing One",
    "Endor Occupation & Masterful Move": "Masterful Move & Endor Occupation",
    "Get to Your Ships": "Get To Your Ships!",
    "Tatooine (PR)": "Tatooine",
    "Han With Heavey Blaster Pistol": "Han With Heavy Blaster Pistol",
    "R2 in R5": "Artoo-Detoo In Red 5",
    "Goo Ney Tay": "Goo Nee Tay",
    "Strike bloked": "Strike Blocked",
    "A Jedis Resilience": "A Jedi's Resilience",
    "Were are you looking for me ?": "Were You Looking For Me?",
    "Were are you looking for me?": "Were You Looking For Me?",
    "Cards Starting": "STARTING",
    "Agents of Black Sun/Vengeance of the Dark Prince": "Agents Of Black Sun",
    "Mobilisation Points/You Cannot Hide Forever": (
        "You Cannot Hide Forever & Mobilization Points"
    ),
    "Bossk In": "Bossk In Hound's Tooth",
    "Boba Fett Bounty Hunter": "Boba Fett, Bounty Hunter",
    "Bad Feeling": "Bad Feeling Have I",
    "We Must Accelrate our Plans": "We Must Accelerate Our Plans",
    "Oh Switch Off": "Oh, Switch Off",
    "Control and Set for Stun": "Control & Set For Stun",
    "Pull All Section on alert": "Put All Sections On Alert",
    "Sense & UITF": "Sense & Uncertain Is The Future",
    "Off. Dolphe": "Officer Dolphe",
    "Lt. Arven Wendik": "Lieutenant Arven Wendik",
    "Lt. Rya Kirsch": "Lieutenant Rya Kirsch",
    "Off. Elberger": "Officer Ellberger",
    "A Vergeance in the Force": "A Vergence In The Force",
    "It's On automatic pilot!": "It's On Automatic Pilot!",
    "The Gravest of circumstances": "The Gravest Of Circumstances",
    "Podrace Prep (recycles)": "Podrace Prep",
    "Hunt Down/Fire's Out": "Hunt Down And Destroy The Jedi",
    "Visage OTE": "Visage Of The Emperor",
    "PrepDefense": "Prepared Defenses",
    "Tatooine Maul": "Darth Maul",
    "GM Tarkin": "Grand Moff Tarkin",
    "Dre & Panda": "Dr. Evazan & Ponda Baba",
    "R3 Boba Fett": "Boba Fett, Bounty Hunter",
    "Maul's Double Saber": "Maul's Double-Bladed Lightsaber",
    "Maul's Double-Saber": "Maul's Double-Bladed Lightsaber",
    "Maul's Double-saber": "Maul's Double-Bladed Lightsaber",
    "Masterful Move Combo": "Masterful Move & Endor Occupation",
    "Circle Now Complete": "The Circle Is Now Complete",
    "Sense (non-combo)": "Sense",
    "TPM": "The Phantom Menace",
    "N: Swamp": "Naboo: Swamp",
    "N: Theed Docking Bay": "Naboo: Theed Palace Docking Bay",
    "N: Theed Generator Core": "Naboo: Theed Palace Generator Core",
    "N: Theed Generator": "Naboo: Theed Palace Generator",
    "N: Theed Throne Room": "Naboo: Theed Palace Throne Room",
    "Nute Grunway, Nemoidian Viceroy": "Nute Gunray, Neimoidian Viceroy",
    "Aromored Attack Tank": "Armored Attack Tank",
    "DFS Squadron Fighter": "DFS Squadron Starfighter",
    "BD Blaster Rifle": "Battle Droid Blaster Rifle",
    "Droid Fighter Laser Cannons": "Droid Starfighter Laser Cannons",
    "throne room": "Death Star II: Throne Room",
    "insignifcant rebellion": "Insignificant Rebellion",
    "Insignificant rebellion": "Insignificant Rebellion",
    "Vader with lightsaber": "Darth Vader With Lightsaber",
    "Darth Vader with saber": "Darth Vader With Lightsaber",
    "Bobba Fett bounty hunter": "Boba Fett, Bounty Hunter",
    "Ig-88 with roit gun": "IG-88 With Riot Gun",
    "Emperors power": "Emperor's Power",
    "Tatooine docking bay": "Tatooine: Docking Bay 94",
    "Your powers are weak old man": "Your Powers Are Weak, Old Man",
    "Vaders Anger": "Vader's Anger",
    "The empires back": "The Empire's Back",
    "Vaders eye": "Vader's Eye",
    "Lightsaber deficiency": "Lightsaber Deficiency",
    "Sniper & Dark strike": "Sniper & Dark Strike",
    "Grand moff Tarkin": "Grand Moff Tarkin",
    "Blaster rack": "Blaster Rack",
    "Kitik keed'kak": "Kitik Keed'kak",
    "An Unusual Amount of Fear (w/ shields)": "An Unusual Amount Of Fear",
    "Unusual Amount of Fear": "An Unusual Amount Of Fear",
    "Leia w/ Blaster": "Leia With Blaster Rifle",
    "Luke w/ stick": "Luke With Lightsaber",
    "Nebrun Lieds": "Strike Blocked",
    "Secret plans (the effect)": "Secret Plans",
    "Alderran": "Alderaan",
    "Imperial Acadamy Training": "Imperial Academy Training",
    "Heading for Medical Frigate": "Heading For The Medical Frigate",
    "Ewok Celeb": "Ewok Celebration",
    "Shield Is Down": "The Shield Is Down!",
    "The Shield Is Down": "The Shield Is Down!",
    "Deactivate Shield Generator": "Deactivate The Shield Generator",
    "Chirpa's Hut": "Endor: Chief Chirpa's Hut",
    "Chirpa": "Chief Chirpa",
    "Tribesman": "Ewok Tribesman",
    "Crix": "General Crix Madine",
    "Luke, Jedi": "Luke Skywalker, Jedi Knight",
    "Luke, Scout": "Luke Skywalker, Rebel Scout",
    "TIE Advance": "TIE Advanced x1",
    "Stormtrooper Offcer": "Snowtrooper Officer",
    "Lietenant Hebsly": "Lieutenant Hebsly",
    "Diruptor Pistol": "Disruptor Pistol",
    "Stormtrooper Utlility Belt": "Stormtrooper Utility Belt",
    "Enhanced TIE Cannon": "Enhanced TIE Laser Cannon",
    "Aquilash": "Aqualish",
    "Veers": "General Veers",
    "Admiral Chianeau": "Admiral Chiraneau",
    "Masterful Move & Endor Operations": "Masterful Move & Endor Occupation",
    "You Cannot Hide Forever / Mob Points": (
        "You Cannot Hide Forever & Mobilization Points"
    ),
    "Epp Vaders": "Darth Vader With Lightsaber",
    "Epp Mauls": "Darth Maul, Young Apprentice",
    "Imperial Walkers": "Imperial Walker",
    "Neimoidian Advisors": "Neimoidian Advisor",
    "Twi'lek Advisors": "Twi'lek Advisor",
    "Tramples": "Trample",
    "Imperial Commands": "Imperial Command",
    "Walker Garrisons": "Walker Garrison",
    "We're in Attack Position Now": "We're In Attack Position Now",
    "Prepare for a Surface Attack": "Prepare For A Surface Attack",
    "Moff Jerrjerrod": "Moff Jerjerrod",
    "Death Star II: Collant Shft": "Death Star II: Coolant Shaft",
    "There is No Try": "There Is No Try",
    "Leave Them to Me": "Leave Them To Me",
    "Blaster Wreck (V)": "Blaster Rack (V)",
    "Flagship DB": "Executor: Docking Bay",
    "Flagship Hallway": "Executor: Main Corridor",
    "Bridge": "Blockade Flagship: Bridge",
    "Aurra's Blaster": "Aurra Sing's Blaster Rifle",
    "Fett's Blaster": "Boba Fett's Blaster Rifle",
    "Ponda's Blaster": "Ponda Baba's Hold-out Blaster",
    "THe Empire's Back": "The Empire's Back",
    "Dr. Eavazan & Ponda Baba": "Dr. Evazan & Ponda Baba",
    "Captain Sarkili": "Captain Sarkli",
    "Maul's Sith Infiltraitor": "Maul's Sith Infiltrator",
    "Victory Destroyer": "Victory-Class Star Destroyer",
    "The Emperor": "Emperor Palpatine",
    "Tatooine: Carkoon Pit": "Tatooine: Great Pit Of Carkoon",
    "Death Star Docking Bay": "Death Star: Docking Bay 327",
    "Guri (NEW 6/15/02)": "Guri",
    "Maul's Sith Infiltrator (OUT 6/15/02)": "Maul's Sith Infiltrator",
    "There They Are": "There They Are!",
    "armament dismantled": "Armament Dismantled",
    "run, luke, run": "Run Luke, Run!",
    "Massassi Base Operations/OIAM": "Massassi Base Operations / One In A Million",
    "Great Shot,Kid!": "Great Shot, Kid!",
    "Lt. Chamberlyn": "Lieutenant Chamberlyn",
    "Down With The Emperor": "Down With The Emperor!",
    "You Can Either Profit By This / Or Be Destroyed": "You Can Either Profit By This...",
    "Another Pathetic Lifeform or": "Another Pathetic Lifeform",
    "Courscant: Jedi Council Chamber": "Coruscant: Jedi Council Chamber",
    "Where You Looking For Me": "Were You Looking For Me?",
    "Twi lek Adivisor": "Twi'lek Advisor",
    "Orimaarko": "Orrimaarko",
    "Yub Yub": "Yub Yub!",
    "A Tradgedy Has Occurred": "A Tragedy Has Occurred",
    "Luke, Jedi Knight": "Luke Skywalker, Jedi Knight",
    "Flagship: Bridge": "Blockade Flagship: Bridge",
    "Flagship: DB": "Executor: Docking Bay",
    "Flagship: Hallway": "Executor: Main Corridor",
    "Dr. E. & Ponda Baba": "Dr. Evazan & Ponda Baba",
    "Dr. E and Ponda Boba": "Dr. Evazan & Ponda Baba",
    "Boba Fett's Blaster": "Boba Fett's Blaster Rifle",
    "Masterful Move & Endor Celebration": "Masterful Move & Endor Occupation",
    "There is Good in Him/ I Can Save Him": "There Is Good In Him",
    "There's Good In Him / I Can Save Him": "There Is Good In Him",
    "There's Good In Him": "There Is Good In Him",
    "There Is Good In Him / I Can Save Him": "There Is Good In Him",

    "No Money, No Parts, No Deal!/You're A Slave?": (
        "No Money, No Parts, No Deal! / You're A Slave?"
    ),
    "No Money,No Parts, No Deal / You're A Slave?": (
        "No Money, No Parts, No Deal! / You're A Slave?"
    ),
    "Bring Him Before Me/ Take Your Father's Place": (
        "Bring Him Before Me / Take Your Father's Place"
    ),
    "Death Star II Throne Room": "Death Star II: Throne Room",
    "Agents Of Black Sun/Vengence Of The Dark Prince": (
        "Agents Of Black Sun / Vengeance Of The Dark Prince"
    ),
    "IT-O [Eyetee-Oh]": "IT-O (Eyetee-Oh)",
    "U-3PO [Yoo-Threepio]": "U-3PO (Yoo-Threepio)",
    "Aiii! Aaa! Agggggggggg!": "Aiiii! Aaa! Agggggggggg!",
    "HOTH: MAIN POWER GENERATORS": "Hoth: Main Power Generators",
    "HOTH: SNOW TRENCH": "Hoth: Snow Trench",
    "HOTH: DEFENSIVE PERIMETER": "Hoth: Defensive Perimeter",
    "ECHO BASETROOPER OFFICER": "Echo Base Trooper Officer",
    "LANDO CALRISSIAN SCOUNDREL": "Lando Calrissian, Scoundrel",
    "COMMANER WEDGE ANTILLES": "Commander Wedge Antilles",
    "ECHO BASE TROPER RIFLE": "Echo Base Trooper Rifle",
    "GOLAN LAER BATTERY": "Golan Laser Battery",
    "MON CALIMARI STAR CRUSIER": "Mon Calamari Star Cruiser",
    "CORILIEN CORVETTE": "Corellian Corvette",
    "Captain Gilad Pellason": "Captain Gilad Pellaeon",
    "Televon Koreyy": "Televan Koreyy",
    "4LOM w/ Concussion Rifle": "4-LOM With Concussion Rifle",
    "IG88 w/ Riot Gun": "IG-88 With Riot Gun",
    "Dengar w/ Blaster Carbine": "Dengar With Blaster Carbine",
    "Gamall Wironnic": "Gamall Wironicc",
    "Maul's DoubleBladed Lightsaber": "Maul's Double-Bladed Lightsaber",
    "Omii Box & It's Worse": "Ommni Box & It's Worse",
    "Neimoddian Advisor": "Neimoidian Advisor",
    "Artoo-Deetoo In Red 5": "Artoo-Detoo In Red 5",
    "Security Tower": "Cloud City: Security Tower",
    "East Platform": "Cloud City: East Platform (Docking Bay)",
    "Port Town District": "Cloud City: Port Town District",
    "Tusken Canyon": "Tatooine: Tusken Canyon",
    "Lar's Moisture Farm": "Tatooine: Lars' Moisture Farm",
    "D: BOG CLEARING": "Dagobah: Bog Clearing",
    "D: SWAMP": "Dagobah: Swamp",
    "D: JUNGLE": "Dagobah: Jungle",
    "D: TRAINING AREA": "Dagobah: Training Area",
    "D: YODA'S HUT": "Dagobah: Yoda's Hut",
    "QUEEN ADMIDALA": "Queen Amidala",
    "LUKE SKYWALER, JEDI KNIGHT": "Luke Skywalker, Jedi Knight",
    "ANAKINS LIGHT SABER": "Anakin's Lightsaber",
    "CONCUSSION GERNADE": "Concussion Grenade",
    "OBIWANS LIGHTSABER": "Obi-Wan's Lightsaber",
    "LET THE WOOKIE WIN": "Let The Wookiee Win",
    "WED15-I7 'Septoid' Droid": "WED15-l7 'Septoid' Droid",
    "Empire's Back": "The Empire's Back",
    "Death Star: Docking Bay Control Room": "Death Star: Docking Control Room 327",
    "Prepared Denfences": "Prepared Defenses",
    "You Cannot Hide Forever & Mobilisation Points": (
        "You Cannot Hide Forever & Mobilization Points"
    ),
    "You Cannot Hide Forever/ Mob Points": (
        "You Cannot Hide Forever & Mobilization Points"
    ),
    "Fear is My Ally + DS": "Fear Is My Ally",
    "Fear Is My Alley w/ten shields": "Fear Is My Ally",
    "Fear is My Ally and 10 shields": "Fear Is My Ally",
    "Fear is my Ally w/ 10 sheilds": "Fear Is My Ally",
    "Endor Bunker": "Endor: Bunker",
    "Endor Landing PLatform": "Endor: Landing Platform (Docking Bay)",
    "Scythe Sqadron TIEs": "Scythe Squadron TIE",
    "The Emporers Sword": "The Emperor's Sword",
    "The Emporers Shield": "The Emperor's Shield",
    "We Have Something Special Planned": "Something Special Planned For Them",
    "They're Still Coming Through": "They're Still Coming Through!",
    "Sebulba's Pod racer": "Sebulba's Podracer",
    "Victory Class Star Destroyer": "Victory-Class Star Destroyer",
    "Ree Yees": "Ree-Yees",
    "Dengar w/Blaster Carbine": "Dengar With Blaster Carbine",
    "Jawa (Tatooine)": "Jawa",
    "Jabba's Palace: Audiene Chamber": "Jabba's Palace: Audience Chamber",
    "Rystáll": "Rystall",
    "Hidden Base System": "Hidden Base",
    "No Money, No Parts, No Deal!/Youre a Slave?": (
        "No Money, No Parts, No Deal! / You're A Slave?"
    ),
    "Darth Maul w Lightsaber": "Darth Maul With Lightsaber",
    "4-Lom w Concussion Rifle": "4-LOM With Concussion Rifle",
    "Objective- Carbon Chamber Testing": "Carbon Chamber Testing",
    "PB and Dre": "Dr. Evazan & Ponda Baba",
    "Dre and pb": "Dr. Evazan & Ponda Baba",
    "(cc) boba fett": "Boba Fett",
    "boba fett cc": "Boba Fett",
    "Emperior Palpatine": "Emperor Palpatine",
    "Darth Maul's Double bladed lightsaber": "Maul's Double-Bladed Lightsaber",
    "Tatoonie: Docking bay 94": "Tatooine: Docking Bay 94",
    "Jabba's Palce: Audience Chamber": "Jabba's Palace: Audience Chamber",
    "Carbon Freezing": "Carbon-Freezing",
    "CArbonfreezing": "Carbon-Freezing",
    "Weapon levatation": "Weapon Levitation",
    "Evader& Monnok": "Evader & Monnok",
    "Sense& uncertain is the future": "Sense & Uncertain Is The Future",
    "Defensive Fire& Hutt Smooch": "Defensive Fire & Hutt Smooch",
    "Force lighting": "Force Lightning",
    "Sniper/ Darkstrike": "Sniper & Dark Strike",
    "Weapon of a ungreatful son": "Weapon Of An Ungrateful Son",
    "Dark jedi presense": "Dark Jedi Presence",
    "Res luk ra auf": "Res Luk Ra'auf",
    "Hoth: Echo War Room": "Hoth: Echo Command Center (War Room)",
    "General Dodonna (V)": "General Dodonna",
    "Cap'n Han Solo": "Captain Han Solo",
    "Obi-wan's stick": "Obi-Wan's Lightsaber",
    "Refelection": "Reflection",
    "Admiral Chiraneu": "Admiral Chiraneau",
    "R3-T6, Brave Little Planet Killer": "R3-T6 (Arthree-Teesix)",
    "Put All Sections on Alert!": "Put All Sections On Alert",
    "Flagship Ops": "Flagship Operations",
    "Tattoine": "Tatooine",
    "Home 1 DB": "Home One: Docking Bay",
    "Luke Skywalker Virtual": "Luke Skywalker (V)",
    "Theron Nutt": "Theron Nett",
    "Ralltir Freighter Capn": "Ralltiir Freighter Captain",
    "Ralltir Freighter Cap": "Ralltiir Freighter Captain",
    "Fusion Generator Supply Tanks Virtual": "Fusion Generator Supply Tanks (V)",
    "Hans Dice Virtual": "Han's Dice",
    "Hans Dice (V)": "Han's Dice",
    "Han's Dice (V)": "Han's Dice",
    "Draw Thier Fire": "Draw Their Fire",
    "Tattoine Celebration": "Tatooine Celebration",
    "Local Uprising/Liberation": "Local Uprising",
    "Sai'Tor Kal Fas (V)": "Sai'torr Kal Fas (V)",
    "An Unusual Amount of Fear +8": "An Unusual Amount Of Fear",
    "Leia w/Blaster": "Leia With Blaster Rifle",
    "Projection of Skywalker": "Projection Of A Skywalker",
    "Han's Heavy Blaster": "Han's Heavy Blaster Pistol",
    "My Kind Of Scum (Wittin)": "My Kind Of Scum",
    "Tatooine: Judland Wastes": "Tatooine: Jundland Wastes",
    "Mobb Points": "Mobilization Points",
    "Carbon chamber console": "Carbonite Chamber Console",
    "jabbas prize": "Jabba's Prize",
    "Tatooine DB 94": "Tatooine: Docking Bay 94",
    "East platform CC": "Cloud City: East Platform (Docking Bay)",
    "Tatooine Desert Landing site": "Tatooine: Desert Landing Site",
    "Tatooine Audience Chamber": "Jabba's Palace: Audience Chamber",
    "Maul's dble saber": "Maul's Double-Bladed Lightsaber",
    "SFS LS 9.3 laser cannons": "SFS L-s9.3 Laser Cannons",
    "Trooper garrison": "Stormtrooper Garrison",
    "ugholste": "Ugloste",
    "ig88 w/ riot": "IG-88 With Riot Gun",
    "bossk w/ mortar": "Bossk With Mortar Gun",
    "Baron fel": "Baron Soontir Fel",
    "Blizzard 2 (vehicle)": "Blizzard 2",
    "Court of the Vile Gangster/I Shall Enjoy Watching You Die": (
        "Court Of The Vile Gangster"
    ),
    "Defensive Fire/Hutt Smooch": "Defensive Fire & Hutt Smooch",
    "Sarlaac": "Sarlacc",
    "Hallway": "Naboo: Theed Palace Hallway",
    "Courtyard": "Naboo: Theed Palace Courtyard",
    "Throne Room": "Naboo: Theed Palace Throne Room",
    "Sai Tor Kal Fas (V)": "Sai'torr Kal Fas (V)",
    "Nass' Chambers": "Naboo: Boss Nass' Chambers",
    "Obi Wan Kenobi, Jedi Knight": "Obi-Wan Kenobi, Jedi Knight",
    "Obi-Wan Kenobi JedI Knight": "Obi-Wan Kenobi, Jedi Knight",
    "Qui Gon Jinn with Lightsaber": "Qui-Gon Jinn With Lightsaber",
    "Qui-Gon Jinn with Lightsaber": "Qui-Gon Jinn With Lightsaber",
    "Horace Vansil": "Horace Vancil",
    "Obi Wan's Lightsaber (Ep.1)": "Obi-Wan's Lightsaber",
    "K'Lor Slug": "K'lor'slug",
    "Alter (Ep.1)": "Alter",
    "Are You Brain Dead": "Are You Brain Dead?!",
    "Niado Deugad": "Niado Duegad",
    "Cloud City: East Landing Platform": "Cloud City: East Platform (Docking Bay)",
    "Dr. Evazans Sawed-off Blaster": "Dr. Evazan's Sawed-off Blaster",
    "Ommni Box/It's Worse": "Ommni Box & It's Worse",
    "Ommni Box combo": "Ommni Box & It's Worse",
    "Sense/Uncertain Is The Future": "Sense & Uncertain Is The Future",
    "Battle Order/ First Strke": "Battle Order & First Strike",
    "Mara Jade, Emperor's Hand": "Mara Jade, The Emperor's Hand",
    "Sith Infiltrator": "Maul's Sith Infiltrator",
    "Aurra Sing Blaster Rifle": "Aurra Sing's Blaster Rifle",
    "Maul Double-Sided Lightsaber": "Maul's Double-Bladed Lightsaber",
    "Fear Is My Ally w/:": "Fear Is My Ally",
    "Oo-ta Goo-ta, Solo? (V)": "Oo-ta Goo-ta, Solo?",
    "Sebulbas Podracer": "Sebulba's Podracer",
    "Control/Set for Stun": "Control & Set For Stun",
    "Emperor's Shield, The": "The Emperor's Shield",
    "Emperor's Sword, The": "The Emperor's Sword",
    "Death Star II: Capacitators": "Death Star II: Capacitors",
    "Come Here Your Big Coward": "Come Here You Big Coward",
    "You've Never Won A Race)": "You've Never Won A Race?",
    "Naboo: Theed Generator": "Naboo: Theed Palace Generator",
    "Naboo: Theed Generator Core": "Naboo: Theed Palace Generator Core",
    "Tatooine: Maul's Landing Site": "Tatooine: Desert Landing Site",
    "Dr. E & PB": "Dr. Evazan & Ponda Baba",
    "Sith Probe Droids": "Sith Probe Droid",
    "Blaster Rack (?)": "Blaster Rack",
    "Dr. Evazen & Ponda Baba": "Dr. Evazan & Ponda Baba",
    "Dark Jedi Lightsabers": "Dark Jedi Lightsaber",
    "E-Web Blaster": "E-web Blaster",
    "I-G88's Pulse Cannon": "IG-88's Pulse Cannon",
    "Look Sir Droids": "Look Sir, Droids",
    "Death Star: Docking Control Room": "Death Star: Docking Control Room 327",
    "jabba's Palace: Dungeaon": "Jabba's Palace: Dungeon",
    "Admiral Acbar": "Admiral Ackbar",
    "Copmmander Wedge Antiles": "Commander Wedge Antilles",
    "Hoth: Defensive Perimet": "Hoth: Defensive Perimeter (3rd Marker)",
    "Dagobah: yodah's Hut": "Dagobah: Yoda's Hut",
    "Medium Repeating Blaste Cannon": "Medium Repeating Blaster Cannon",
    "Hoth Main Power Generator": "Hoth: Main Power Generators (1st Marker)",
    "Hoth North Ridge": "Hoth: North Ridge (4th Marker)",
    "Quick Draw or Commando Training": "Quick Draw",
    "Commando Training or Quick Draw": "Commando Training",
    "Echo Docking Bay": "Hoth: Echo Docking Bay",
    "Echo Corridor": "Hoth: Echo Corridor",
    "Echo Command Center": "Hoth: Echo Command Center (War Room)",
    "Hoth System": "Hoth",
    "Aquarius": "Aquaris",
    "Liuetenant Greeve": "Lieutenant Greeve",
    "EB Troopers": "Echo Base Trooper",
    "EB Blasters": "Echo Base Trooper Rifle",
    "Chewi, Enraged": "Chewie, Enraged",
    "B-wings": "B-wing Attack Fighter",
    "A-wings": "A-wing",
    "Snowseeders": "Snowspeeder",
    "Luke with Stick": "Luke With Lightsaber",
    "Princess Organa": "Princess Leia",
    "General Solo": "General Han Solo",
    "Rune Haako, Leagal Counsel": "Rune Haako, Legal Counsel",
    "Guri - No deck is complete without her": "Guri",
    "Naboo: Throne Room": "Naboo: Theed Palace Throne Room",
    "Enter the Bureacrat": "Enter The Bureaucrat",
    "Maul's Stick": "Maul's Double-Bladed Lightsaber",
    "Naboo Theed Palacae Generator": "Naboo: Theed Palace Generator",
    "Naboo Theed Palacae Generator core": "Naboo: Theed Palace Generator Core",
    "profit by this/or be destroyed": "You Can Either Profit By This...",
    "You've Gotta a Lot of Guts Coming Here": "You've Got A Lot Of Guts Coming Here",
    "We have a Plan/ They will be lost and confused": "We Have A Plan",
    "Naboo Theed Palace Courtyard": "Naboo: Theed Palace Courtyard",
    "Naboo Theed Palace Hallway": "Naboo: Theed Palace Hallway",
    "Naboo Theed Palace Throne room": "Naboo: Theed Palace Throne Room",
    "Alter and Friendly Fire": "Alter & Friendly Fire",
    "Asscension guns": "Ascension Guns",
    "Nabrum Leids": "Nabrun Leids",
    "RadiantVII": "Radiant VII",
    "Tawass Khaa": "Tawss Khaa",
    "Ki-Adi Mundi": "Ki-Adi-Mundi",
    "Help Me Obi Wan Kenobi": "Help Me Obi-Wan Kenobi",
    "Tatoine": "Tatooine",
    "Mace Windu JedI Master": "Mace Windu, Jedi Master",
    "Yoda Master of the force": "Yoda, Master Of The Force",
    "Qui-Gon-Jinn Jedi Master": "Qui-Gon Jinn, Jedi Master",
    "Panaka Protector of the Queen": "Panaka, Protector Of The Queen",
    "Sache": "Sabe",
    "Naboo: Generator Core": "Naboo: Theed Palace Generator Core",
    "The Bith Shuffle/ Desperate Reach": "The Bith Shuffle & Desperate Reach",
    "YCHF & Mob Points": "You Cannot Hide Forever & Mobilization Points",
    "CC: Carbointe Chamber": "Cloud City: Carbonite Chamber",
    "CC East Platform": "Cloud City: East Platform (Docking Bay)",
    "Exector: Docking Bay": "Executor: Docking Bay",
    "Grand Admiral Thrwan": "Grand Admiral Thrawn",
    "4-Lom w/ rifle": "4-LOM With Concussion Rifle",
    "Obidian 8": "Obsidian 8",
    "OS 72-1 in Obsidian 1": "OS-72-1 In Obsidian 1",
    "OS 72-2 in Obsidian 2": "OS-72-2 In Obsidian 2",
    "MM & Endor Occupation": "Masterful Move & Endor Occupation",
    "We must accllerate our plans": "We Must Accelerate Our Plans",
    "Galiad": "Gailid",
    "Death Squadron SD": "Death Squadron Star Destroyer",
    "Victory-class SD": "Victory-Class Star Destroyer",
    "TIE Defender Mark 1": "TIE Defender Mark I",
    "SFS L-s 9.3 Laser Cannons": "SFS L-s9.3 Laser Cannons",
    "Defelector Shield Generators": "Deflector Shield Generators",
    "Grey Squadron 1": "Gray Squadron 1",
    "Grey Squadron 2": "Gray Squadron 2",
    "Enhanced Proton Torpedos": "Enhanced Proton Torpedoes",
    "Blizard 4": "Blizzard 4",
    "Derek 'Hobbie' Kilvian": "Derek 'Hobbie' Klivian",
    "Massassi Base Operations/ One in a Million": "Massassi Base Operations",
    "Darth Sideous": "Darth Sidious",
    "0W0-1 with backup": "OWO-1 With Backup",
    "00M-9": "OOM-9",
    "Zuckuss in the Mist Hunter": "Zuckuss In Mist Hunter",
    "Zuckuss in Mist Hunter": "Zuckuss In Mist Hunter",
    "Zuckess in Mist Hunter": "Zuckuss In Mist Hunter",
    "AAT Assualt leader": "AAT Assault Leader",
    "Alter and Collateral Damage": "Alter & Collateral Damage",
    "The Ebb of Battle": "The Ebb Of Battle",
    "N: Battle Plains": "Naboo: Battle Plains",
    "N: Theed Palace Throne Room": "Naboo: Theed Palace Throne Room",
    "Elite Squadron Stormtroopers": "Elite Squadron Stormtrooper",
    "Stormtroopers": "Stormtrooper",
    "Corporal Avirik": "Corporal Avarik",
    "Blasted Drid": "Blasted Droid",
    "Imperial Arest order & Secret plans": "Imperial Arrest Order & Secret Plans",
    "Darth Vader w lightsaber": "Darth Vader With Lightsaber",
    "Stortrooper Garison": "Stormtrooper Garrison",
    "Death star II Docking bay": "Death Star II: Docking Bay",
    "HDADTJ/ TFHGOOTU": "Hunt Down And Destroy The Jedi",
    "Ex: Holotheater": "Executor: Holotheatre",
    "Ex: Meditation Chamber": "Executor: Meditation Chamber",
    "Ex: Docking Bay": "Executor: Docking Bay",
    "TT: Marketplace": "Tatooine: Marketplace",
    "TT: Docking Bay 94": "Tatooine: Docking Bay 94",
    "Darth Vaders lightsaber": "Darth Vader's Lightsaber",
    "Mauls double lightsaber": "Maul's Double-Bladed Lightsaber",
    "Polarized Negative Power Thingy": "Polarized Negative Power Coupling",
    "R-3P0": "R-3PO (Ar-Threepio)",
    "Leesub Sirlin": "Leesub Sirln",
    "Through The Force You'll See Stuff": "Through The Force Things You Will See",
    "Obi-Wan's Saber": "Obi-Wan's Lightsaber",
    "X- Wings": "X-wing",
    "X-Wings": "X-wing",
    "Out Of Nowhere & Houjix": "Houjix & Out Of Nowhere",
    "Sullest": "Sullust",
    "Tatooine: Lars'Moisture Farm": "Tatooine: Lars' Moisture Farm",
    "Endor: chief chirpa's hutt": "Endor: Chief Chirpa's Hut",
    "Anakin's Poadracer": "Anakin's Podracer",
    "Courscant: Jedi counsel Chamber": "Coruscant: Jedi Council Chamber",
    "Han Chewie in the falcon": "Han, Chewie, And The Falcon",
    "Obi-wans's Lightsaber (premier)": "Obi-Wan's Lightsaber",
    "Lando Calrissian Scounderel": "Lando Calrissian, Scoundrel",
    "Corrn Horn": "Corran Horn",
    "qui-gon jinn Jedi master": "Qui-Gon Jinn, Jedi Master",
    "loosing track": "Losing Track",
    "weapon levfitation": "Weapon Levitation",
    "draw there fire": "Draw Their Fire",
    "Correlian Corvette": "Corellian Corvette",
    "Yavin 4: War Woom": "Yavin 4: Massassi War Room",
    "All Wings Report In/ Darklighter Spin": "All Wings Report In & Darklighter Spin",
    "Houjix/ Out of Nowhere": "Houjix & Out Of Nowhere",
    "Shocking Information/ Grimtaash": "Shocking Information & Grimtaash",
    "Dart Vader": "Darth Vader",
    "Gran Moff Tarkin": "Grand Moff Tarkin",
    "Imp. Class SD": "Imperial-Class Star Destroyer",
    "Vict. Class SD": "Victory-Class Star Destroyer",

    "Han (V)": "Han Solo",
    "Come with Mw (V)": "Come With Me",
    "Come With Me (V)": "Come With Me",
    "Intruder Missiles": "Intruder Missile",
    "LE-BO209 (Leebo)": "LE-BO2D9 (Leebo)",
    "IG88": "IG-88",
    "IG88 with Riot Gun": "IG-88 With Riot Gun",
    "Boba Fett with Blaster": "Boba Fett With Blaster Rifle",
    "Lando (dark side)": "Lando Calrissian",
    "The Emporor": "Emperor Palpatine",
    "Emporor Palpitine": "Emperor Palpatine",
    "IG88's Pulse Cannon": "IG-88's Pulse Cannon",
    "IG88's Neutral Inhubitor": "IG-88's Neural Inhibitor",
    "IG2000": "IG-2000",
    "IG88 in IG2000": "IG-88 In IG-2000",
    "Tie Defender": "TIE Defender Mark I",
    "Ket Mallise": "Ket Maliss",
    "Naboo: Ohta Gunga Entrance": "Naboo: Otoh Gunga Entrance",
    "Naboo: Theed Generators": "Naboo: Theed Palace Generator",
    "Agents of Black Sun/Vengance of the Dark Prince": (
        "Agents Of Black Sun / Vengeance Of The Dark Prince"
    ),
    "Tatooine : Docking Bay 94": "Tatooine: Docking Bay 94",
    "Areil Schous": "Arleil Schous",
    "Proton Torpeodes": "Proton Torpedoes",
    "Endor Landing Platform (Docking Bay)": "Endor: Landing Platform (Docking Bay)",
    "Sentinel Class Landing Craft": "Sentinel-Class Landing Craft",
    "Naboo Theed Palace Generator Core": "Naboo: Theed Palace Generator Core",
    "Jersus Jannick": "Jerus Jannick",
    "Twi'lek Adviser": "Twi'lek Advisor",
    "Endor Rebel Landing Site": "Endor: Rebel Landing Site (Forest)",
    "SaltorrKalFas (V)": "Sai'torr Kal Fas (V)",
    "Chewbacca of Kashhyyk": "Chewbacca Of Kashyyyk",
    "Tyderium": "Tydirium",
    "Obi-Wan's Lightsaber (episode 1)": "Obi-Wan's Lightsaber (Coruscant)",
    "An Unusual Ammount Of Fear": "An Unusual Amount Of Fear",
    "N: Ohta Gunga Entrance": "Naboo: Otoh Gunga Entrance",
    "N: Theed Generators": "Naboo: Theed Palace Generator",
    "Plo Kloon": "Plo Koon",
    "DS 181-3": "DS-181-3",
    "DS 181-4": "DS-181-4",
    "Space Port Docking Bay": "Spaceport Docking Bay",
    "Death Star II Coolant Shaft": "Death Star II: Coolant Shaft",
    "Death Star II Capacitors": "Death Star II: Capacitors",
    "Death Star II Reactor Core": "Death Star II: Reactor Core",
    "Devastor": "Devastator",
    "Suprise Assualt": "Surprise Assault",
    "Tatooine E1": "Tatooine (Coruscant)",
    "YT1300 Transport": "YT-1300 Transport",
    'WED-1016 "Techie" Droid': "WED-1016 'Techie' Droid",
    "Short Range Fighters & Watch Your Back": "Short Range Fighters & Watch Your Back!",
    "We Shall Double Our Efforts": "We Shall Double Our Efforts!",
    "Broken Fett": "Boba Fett, Bounty Hunter",
    "Klor Slug (V)": "K'lor'slug (V)",
    "Solamahal (V)": "Solomahal (V)",
    "Yoda Stew/You Do Have Your Moments": "Yoda Stew & You Do Have Your Moments",
    "Set Your Course For Alderaan/The Ultimate Power in The Universe": (
        "Set Your Course For Alderaan / The Ultimate Power In The Universe"
    ),
    "Death Star: Detention Block": "Death Star: Detention Block Corridor",
    "Hoth: Defensive Perimeter 3rd": "Hoth: Defensive Perimeter (3rd Marker)",
    "Hoth: North Ridge 4th": "Hoth: North Ridge (4th Marker)",
    "Hoth: Ice Plains 5th": "Hoth: Ice Plains (5th Marker)",
    "Hoth: Mountains 6th": "Hoth: Mountains (6th Marker)",
    "Hoth: Wampa Cave 7th": "Hoth: Wampa Cave (7th Marker)",
    "Elite Squadron Stormtooper": "Elite Squadron Stormtrooper",
    'WED15-17 "Septoid" Droid': "WED15-l7 'Septoid' Droid",
    "AT-AT Cannons": "AT-AT Cannon",
    "Electro Rangefinder": "Electro-Rangefinder",
    "Judlandw Wastes": "Tatooine: Jundland Wastes",
    "Tatooine: Judlandw Wastes": "Tatooine: Jundland Wastes",
    "Jawa Canyon": "Tatooine: Jawa Canyon",
    "Tatooine: Jawa Canyon": "Tatooine: Jawa Canyon",
    "Hutt Canyon": "Tatooine: Hutt Canyon",
    "Tatooine: Hutt Canyon": "Tatooine: Hutt Canyon",
    "R'kik D'nec Hero of the Dune Sea": "R'kik D'nec, Hero Of The Dune Sea",
    "Don't Underestimate out chances": "Don't Underestimate Our Chances",
    "Endor Operations/Imperial Outpost": "Endor Operations",
    "Endor Operation/ Imperial Outpost": "Endor Operations",
    "Endor Operation/Imperial Outpost": "Endor Operations",
    "Darth Vader w/ Lightsabre": "Darth Vader With Lightsaber",
    "Vengence": "Vengeance",
    "Imperial Class Star Destroyer": "Imperial-Class Star Destroyer",
    "Endor: Landing Platform": "Endor: Landing Platform (Docking Bay)",
    "Jedi Test #1": "A Jedi's Strength",
    "Wyren Serper": "Wyron Serper",
    "Biker Scout": "Biker Scout Trooper",
    "Captain Yor": "Captain Yorr",
    "4-LOM With Concusion Rifle": "4-LOM With Concussion Rifle",
    "Djas Phur (V)": "Djas Puhr (V)",
    "Alter or Alter and Collateral Damage": "Alter & Collateral Damage",
    "Sai Torr Kal'Fas (V)": "Sai'torr Kal Fas (V)",
    "Sai Torr Kal'Fas": "Sai'torr Kal Fas",
    "Cloud City: Carbonite Freezing Chamber": "Cloud City: Carbonite Chamber",
    "Padme Amidala": "Queen Amidala, Ruler Of Naboo",
    "Obi-Wan w/ saber": "Obi-Wan Kenobi With Lightsaber",
    "Luke w/ saber": "Luke Skywalker With Lightsaber",
    "Meditate": "Meditation",
    "Return of a Jedi": "Return Of A Jedi",
    "Return of the Jedi": "Return Of A Jedi",
    "Quiet Mining Colony/ Independent Operation": "Quiet Mining Colony",
    "QMC/IO": "Quiet Mining Colony",
    "Pucumir Thyrss": "Pucumir Thryss",
    "Admiral Chiraneu": "Admiral Chiraneau",
    "Adiral Chiraneau": "Admiral Chiraneau",
    "DSII: DB": "Death Star II: Docking Bay",
    "DS: DB control room": "Death Star: Detention Block Control Room",
    "DS: DB 327": "Death Star: Docking Bay 327",
    "Death Star: Docking Bay": "Death Star: Docking Bay 327",
    "Endor: DB": "Endor: Landing Platform (Docking Bay)",
    "Executor: DB": "Executor: Docking Bay",
    "SFS L-s.9.3 Laser Cannons": "SFS L-s9.3 Laser Cannons",
    "Seinar Fleet Systems": "Sienar Fleet Systems",
    "Boba Fett in Slave 1": "Boba Fett In Slave I",
    "Tusken Raider Ep 1": "Tusken Raider (Coruscant)",
    "Ghhk and Those Rebels Won't Escape Us": "Ghhk & Those Rebels Won't Escape Us",
    "Gaderffi Stick": "Gaderffii Stick",
    "Thermal Detenator": "Thermal Detonator",
    "Desert": "Tatooine: Desert",
    "Cloud City Sabaac": "Cloud City Sabacc",
    "Dr. Evezan & Ponda Baba": "Dr. Evazan & Ponda Baba",
    "Courascant": "Coruscant",
    "Courascant: Docking Bay": "Coruscant: Docking Bay",
    "Courascant: Galactic Senate": "Coruscant: Galactic Senate",
    "Courascant: Jedi Council Chamber": "Coruscant: Jedi Council Chamber",
    "Deepa Bilaba": "Depa Billaba",
    "Pio Koon": "Plo Koon",
    "Mas Ameda": "Mas Amedda",
    "Sel Tarta": "Sei Taria",
    "Supreme Chancelor Valorum": "Supreme Chancellor Valorum",
    "Tedau Benden": "Tendau Bendon",
    "Obi-Wan Kenobi, Padiwan Learner": "Obi-Wan Kenobi, Padawan Learner",
    "Couracant Guard": "Coruscant Guard",
    "Master Qui-Gon": "Qui-Gon Jinn",
    "Kal'Falnl'C'nDros": "Kal'Falnl C'ndros",
    "Wedge Antilles,RSL": "Wedge Antilles, Red Squadron Leader",
    "Heading For The Frigate": "Heading For The Medical Frigate",
    "CC:Docking Bay": "Cloud City: Platform 327 (Docking Bay)",
    "CC: Docking Bay": "Cloud City: Platform 327 (Docking Bay)",
    "Houjixx": "Houjix",
    "Comence Primary Ignition": "Commence Primary Ignition",
    "Man Calamari": "Mon Calamari",
    "Imperial Trooper Gaurd": "Imperial Trooper Guard",
    "P-58": "P-59",
    "Colonel Dvod Jon": "Colonel Davod Jon",
    "Tatoonie : Docking Bay 94": "Tatooine: Docking Bay 94",
    "Tatoonie : Mos Eisley": "Tatooine: Mos Eisley",
    "Home One : War Room": "Home One: War Room",
    "Yavin 4 : Massasi War Room": "Yavin 4: Massassi War Room",
    "Yavin 4: War Room": "Yavin 4: Massassi War Room",
    "Yavin 4: Massasi War Room": "Yavin 4: Massassi War Room",
    "Squardron Assignment": "Squadron Assignments",
    "Launching the Assualt": "Launching The Assault",
    "Collsion": "Collision",
    "Blasted Varmits": "Blasted Varmints",
    "Red Squardon 7": "Red 7",
    "Lieutenant Telsj": "Lieutenant Telsij",
    "I'll take the leader": "I'll Take The Leader",
    "Fusion Generator Supply Tank (V)": "Fusion Generator Supply Tanks (V)",
    "Leia, Rebel Princess": "Princess Leia",
    "Any Methods Necessary (S.I.)": "Any Methods Necessary",
    "Han Solo (V)": "Han Solo",
    "Queen Amidala, Ruler of the Naboo": "Queen Amidala, Ruler Of Naboo",
    "Dr. Evazan and Ponda Boba": "Dr. Evazan & Ponda Baba",
    "Yoda, Senior Council Member": "Yoda, Senior Council Member",
    "Yoda, You Seek Yoda": "Yoda, You Seek Yoda",
    "Great Shot, Kid!": "Great Shot, Kid!",
    "Collsion": "Podracer Collision",
    "Collision": "Podracer Collision",
    "Yavin 4 : Docking Bay": "Yavin 4: Docking Bay",
    "Obi-Wan Kenobi With Lightsaber": "Obi-Wan With Lightsaber",
    "Luke Skywalker With Lightsaber": "Luke With Lightsaber",
    "Tatoonie: Mos Eisley": "Tatooine: Mos Eisley",
    "Luck Skywalker Rebel Scout": "Luke Skywalker, Rebel Scout",
    "Tantooine: Docking Bay 927": "Death Star: Docking Bay 327",
    "Naboo: Dacking Bay": "Naboo: Theed Palace Docking Bay",
    "Grand Moff Tarkin (V)": "Tarkin (V)",
    "Grand Moff Tarkin V": "Tarkin (V)",
    "Trooper Assults": "Trooper Assault",
    "Dark Jedi Presense": "Dark Jedi Presence",
    "Hoth: Echo Base War Room": "Hoth: Echo Command Center (War Room)",
    "Hoth: Echo Base Docking Bay": "Hoth: Echo Docking Bay",
    "Bravo Leader": "Ric Olie, Bravo Leader",
    "Derek 'Hobbie' Klivan": "Derek 'Hobbie' Klivian",
    "Han' Heavy Blaster Pistol (V)": "Han's Heavy Blaster Pistol (V)",
    "Han's Heavy Blaster (V)": "Han's Heavy Blaster Pistol (V)",
    "Saitorr Kal Fas (V)": "Sai'torr Kal Fas (V)",
    "Sai'Tor Kal'Fas (V)": "Sai'torr Kal Fas (V)",
    "Echo Base Operations (EBO)": "Echo Base Operations",
    "Docking and Repair Facilites (D&R;)": "Docking And Repair Facilities",
    "Docking and Repair Facilites": "Docking And Repair Facilities",
    "Lando in the Millenium Falcon": "Lando In Millennium Falcon",
    "TDIGWAAT": "This Deal Is Getting Worse All The Time",
    "Dark Deal (DD)": "Dark Deal",
    "Zuckuss in Mist Hunter (ZiMH)": "Zuckuss In Mist Hunter",
    "LTMTFM / ALWWHR": "Let Them Make The First Move",
    "LTMTFM/ALWWHR": "Let Them Make The First Move",
    "Ponda Baba & Dr. Evazan": "Dr. Evazan & Ponda Baba",
    "WYS / TPCBALR": "Watch Your Step",
    "WYS/TPCBALR": "Watch Your Step",
    "Your Insights & Staging Areas": "Your Insight Serves You Well & Staging Areas",
    "Enraged": "Chewie, Enraged",
    "No Question's Asked": "No Questions Asked",
    "Its a Hit!": "It's A Hit!",
    "Houjix and Out of Nowhere": "Houjix & Out Of Nowhere",
    "Hyper Escpae": "Hyper Escape",
    "R'kic D'Nec": "R'kik D'nec, Hero Of The Dune Sea",
    "Hero Of The Dune Sea": "R'kik D'nec, Hero Of The Dune Sea",
    "Uttini!": "Utinni!",
    "Figirin' D'an": "Figrin D'an",
    "Artoo (or R2-D2 (V))": "R2-D2 (V)",
    "Fire Extingusher": "Fire Extinguisher",
    "You Can Either Profit By This?/Or Be Destroyed": "You Can Either Profit By This...",
    "You Can Either Profit By This?/Or Be Destroyed": "You Can Either Profit By This...",
    "Or Do Not & Wise Advice": "Do, Or Do Not & Wise Advice",
    "And The Falcon": "Han, Chewie, And The Falcon",
    "Zuckess": "Zuckuss",
    "The Emperor's Hand": "Mara Jade, The Emperor's Hand",
    "Emperor's Power": "Emperor's Power",
    "Corellian Freighter (Endor card)": "Spiral",
    "Luke Sywalker (V)": "Luke Skywalker (V)",
    "Qui-Gon W/Lightsaber": "Qui-Gon Jinn With Lightsaber",
    "Obi-Wan W/Lightsaber": "Obi-Wan With Lightsaber",
    "Im on the Leader": "I'll Take The Leader",
    "Nar Shadaa Wind Chimes": "Nar Shaddaa Wind Chimes",
    "Yavin 4: Massasi Throne Room": "Yavin 4: Massassi Throne Room",
    "Kid!": "Great Shot, Kid!",
    "Bespin: Cloud City (Duh!)": "Bespin: Cloud City",
    "Major Turr Phenir": "Major Turr Phennir",
    "loctions:planet coruscant": "Coruscant",
    "loctions: planet coruscant": "Coruscant",
    "tatooine mos espa docking bay": "Tatooine: Mos Espa Docking Bay",
    "planet tatooine": "Tatooine",
    "planet coruscant": "Coruscant",
    "mos eisley": "Tatooine: Mos Eisley",
    "b wing attack fighters": "B-wing Attack Fighter",
    "queens royal ship": "Queen's Royal Starship",
    "corellion corvettes": "Corellian Corvette",
    "nebulan b frigate": "Nebulon-B Frigate",
    "master gui gonn": "Qui-Gon Jinn",
    "qui gonn jinn with lightsaber": "Qui-Gon Jinn With Lightsaber",
    "lietenant williams": "Lieutenant Williams",
    "Kiffex (Naboo)": "Kiffex",
    "SYCFA/TUPITU": "Set Your Course For Alderaan",
    "A Million Voice Crying Out": "A Million Voices Crying Out",
    "jedi council chamber": "Coruscant: Jedi Council Chamber",
    "coruscant docking bay": "Coruscant: Docking Bay",
    "tatooine city outskirts": "Tatooine: City Outskirts",
    "marketplace": "Tatooine: Marketplace",
    "ric ollie": "Ric Olie",
    "squadron assighnments": "Squadron Assignments",
    "lukes backpack": "Luke's Backpack",
    "gold 1 ( aka the millenium flacon)": "Gold 1",
    "Come Here, You Big Coward": "Come Here You Big Coward",
    "An Unusual Amount Of Fear (+10)": "An Unusual Amount Of Fear",
    "any good chewbacca I used chewbacca of kashykk because it's the only one I have but you can use a diffrent one": "Chewbacca Of Kashyyyk",
    "ang good kind of han I used general solo because again he was the only one I had he works though": "General Solo",
    "General Solo": "General Solo",
    "lieutenant nataan": "Lieutenant Naytaan",
    "jedi lightsabers": "Jedi Lightsaber",
    "Hyper Route Navigation Chart": "Hyperoute Navigation Chart",
    "Hyper Route Navigation Chart (optional)": "Hyperoute Navigation Chart",
    "Put All Sectors On Alert": "Put All Sections On Alert",
    "Come Here You Big Coward!": "Come Here You Big Coward",
    "TAT: Great Pit of Carcoon": "Tatooine: Great Pit Of Carkoon",
    "Fear Is My Ally +Any Def.Shields": "Fear Is My Ally",
    "Bossk w/Mortar Cannon Thingy": "Bossk With Mortar Gun",
    "4-Lom w/Concussion Rifle": "4-LOM With Concussion Rifle",
    "Ak Rev": "Ak-rev",
    "TEH": "Mara Jade, The Emperor's Hand",
    "Oota Goota Solo? (V)": "Oo-ta Goo-ta, Solo? (V)",
    "Oo-ta Goo-ta, Solo? (V)": "Oo-ta Goo-ta, Solo? (V)",
    "Hoth: Defensive Perimiter": "Hoth: Defensive Perimeter",
    "Hoth defensive perimeter": "Hoth: Defensive Perimeter",
    "Captain Godhert": "Captain Godherdt",
    "Blizzard Walker x2 (Tempest 1)": "Blizzard Walker",
    "Rescue The Princess/Sometimes I Amaze": "Rescue The Princess",
    "Han w/blaster": "Han With Heavy Blaster Pistol",
    "Jedi's Resilliance": "A Jedi's Resilience",
    "Squardon Assignments": "Squadron Assignments",
    "Collison": "Collision",
    "Lieutenant Telsjj": "Lieutenant Telsij",
    "Lessub Sirln": "Leesub Sirln",
    "Dune Sea Sabbacc": "Dune Sea Sabacc",
    "An Unusual Amount Of Fears": "An Unusual Amount Of Fear",
    "Jedi Master": "Yoda",
    "Lando Calrissisan, Scoundrel": "Lando Calrissian, Scoundrel",
    "Chewie And The Falcon": "Han, Chewie, And The Falcon",
    "Obi-Wan's Lighsaber": "Obi-Wan's Lightsaber",
    "DSII: Throne Room": "Death Star II: Throne Room",
    "Mobilization Point": "Mobilization Points",
    "DSII: Docking Bay": "Death Star II: Docking Bay",
    "Dengar With Blaster Carabine": "Dengar With Blaster Carbine",
    "My Friend": "Rise, My Friend",
    "Flaghsip": "Flagship Executor",
    "Quiet Mining Colony/Independent Operations": "Quiet Mining Colony",
    "Lando w/ Blaster Pistol": "Lando With Blaster Pistol",
    "Hoth Ice plains": "Hoth: Ice Plains",
    "Fear is my ally + shields": "Fear Is My Ally",
    "IAO combo": "Imperial Arrest Order & Secret Plans",
    "Boba fett BH": "Boba Fett, Bounty Hunter",
    "Dr E and Ponda B": "Dr. Evazan & Ponda Baba",
    "Imperial Class star dest (V)": "Imperial-Class Star Destroyer (V)",
    "Chimeara": "Chimaera",
    "Dengar in PO": "Dengar In Punishing One",
    "Hoth: north ridge": "Hoth: North Ridge",
    "Hoth mountains": "Hoth: Mountains",
    "Imperial command": "Imperial Command",
    "Ghhk combo": "Ghhhk & Those Rebels Won't Escape Us",
    "Start: dantooine": "Dantooine",
    "Rouvendous point": "Rendezvous Point",
    "Raltir frighter capitan": "Ralltiir Freighter Captain",
    "LE-BO2D9 [Leebo]": "LE-BO2D9 (Leebo)",
    "Asteroid sancuary": "Asteroid Sanctuary",
    "(V) Sai'torr Kal Fas": "Sai'torr Kal Fas (V)",
    "Artoo I've got a bad feeling about this": "I've Got A Bad Feeling About This",
    "Luke's lighsaber": "Luke's Lightsaber",
    "Cuncussion missiles": "Concussion Missiles",
    "General Tagge (V?)": "General Tagge (V)",
    "Imperial Arest Order": "Imperial Arrest Order",
    "Courusant: Docking Bay": "Coruscant: Docking Bay",
    "Tie Defender Mark 1": "TIE Defender Mark I",
    "Boba Fett in Slave 1": "Boba Fett In Slave I",
    "Mauls Double Bladed Lightsaber": "Maul's Double-Bladed Lightsaber",
    "Vadar's Lightsaber": "Vader's Lightsaber",
    "Aura Sing's Blaster rifle": "Aurra Sing's Blaster Rifle",
    "Lord Maul": "Darth Maul",
    "StormTrooper Garrison": "Stormtrooper Garrison",
    "bounty hunter": "Boba Fett, Bounty Hunter",
    "Dark lord of the sith": "Darth Vader, Dark Lord Of The Sith",
    "Dr. Evan & Ponda Baba": "Dr. Evazan & Ponda Baba",
    "Deystroyer Droid": "Destroyer Droid",
    "Heading For The Medical Firgate": "Heading For The Medical Frigate",
    "Heading To the Medical Frigate": "Heading For The Medical Frigate",
    "Heading for the Med frig": "Heading For The Medical Frigate",
    "K'lor Slug (V)": "K'lor'slug (V)",
    "Dabobah: Swamp": "Dagobah: Swamp",
    "Docking & Repair Facilities": "Docking And Repair Facilities",
    "Owen & Beru Lars": "Owen Lars & Beru Lars",
    "Dark Manuevers": "Dark Maneuvers",
    "Solo? (V)": "Oo-ta Goo-ta, Solo? (V)",
    "Out of Commision": "Out Of Commission",
    "Fear Ds My Ally": "Fear Is My Ally",
    "Ralltiir Operations/In The Hands Of The Empire": "Ralltiir Operations",
    "Ralltiir Operations/In the Hands of the Empire": "Ralltiir Operations",
    "Spaceport: Prefect's Office": "Spaceport Prefect's Office",
    "The Emperors Hand": "Mara Jade, The Emperor's Hand",
    "Dreadnaught-Class Heavy Crusier": "Dreadnaught-Class Heavy Cruiser",
    "Dreadnaught": "Dreadnaught-Class Heavy Cruiser",
    "Location; Hoth 5th Marker": "Hoth: Ice Plains",
    "Hoth: 5th Marker": "Hoth: Ice Plains",
    "Hoth: 7th Marker": "Hoth: Wampa Cave",
    "Hoth: 6th Marker": "Hoth: Mountains",
    "Hoth: 4th Marker": "Hoth: North Ridge",
    "Hoth: 3rd Marker": "Hoth: Defensive Perimeter",
    "Tempest Scout 1 (AT-ST)": "Tempest Scout 1",
    "Vader w/ Saber": "Darth Vader With Lightsaber",
    "Maul w/ Saber": "Darth Maul With Lightsaber",
    "Capt. Pellaeon": "Captain Gilad Pellaeon",
    "Com. Igar": "Commander Igar",
    "Prepare for surface attack": "Prepare For A Surface Attack",
    "Wookie": "Wookiee",
    "Leia With Blaster Riffle": "Leia With Blaster Rifle",
    "Rescue the princess/ Sometimes i amaze even Myself": "Rescue The Princess",
    "Yavin 4: DB": "Yavin 4: Docking Bay",
    "D*: DB": "Death Star: Docking Bay 327",
    "D*: Detention block corrador": "Death Star: Detention Block Corridor",
    "Chebacca's bowcaster": "Chewbacca's Bowcaster",
    "Han's gun (V)": "Han's Heavy Blaster Pistol (V)",
    "Electrobinocs": "Electrobinoculars",
    "D* plans": "Death Star Plans",
    "Sorry about the mess/ blaster proficiency": "Sorry About The Mess",
    "its a trap": "It's A Trap!",
    "It's A Trap": "It's A Trap!",
    "the force is strong w/ this one": "The Force Is Strong With This One",
    "boss nass chambers": "Naboo: Boss Nass' Chambers",
    "CZ-4": "CZ-3 (Seezee-Three)",
    "Twi'lik Adviser": "Twi'lek Advisor",
    "A Few Manuvers": "A Few Maneuvers",
    "R'kik D'nec": "R'kik D'nec, Hero Of The Dune Sea",
    "Test #1: GW": "Great Warrior",
    "Test#2: AJS": "A Jedi's Strength",
    "Test#3: DOE": "Domain Of Evil",
    "Test#4: SMN": "Size Matters Not",
    "TEST#5: IITFYS": "It Is The Future You See",
    "TEST#6: YMCV": "You Must Confront Vader",
    "Tattooine: Docking Bay 94": "Tatooine: Docking Bay 94",
    "Qui-Gon w/ Saber": "Qui-Gon Jinn With Lightsaber",
    "Lando w/ Ax": "Lando With Vibro-Ax",
    "Chewie & Falcon": "Han, Chewie, And The Falcon",
    "Tatooine: Obi's Hut": "Tatooine: Obi-Wan's Hut",
    "Dreadnaught Cruiser": "Dreadnaught-Class Heavy Cruiser",
    "(V)Tarkin": "Tarkin (V)",
    "Maul w/Saber": "Darth Maul With Lightsaber",
    "Lt Endicott": "Lieutenant Endicott",
    "Wakelmui": "Wakeelmui",
    "YA": "Darth Maul, Young Apprentice",
    "Ghhhk & Those Rebel Won't Escape Us": "Ghhhk & Those Rebels Won't Escape Us",
    "Its Worse": "It's Worse",
    "Zuckuss In Mish Hunter": "Zuckuss In Mist Hunter",
    "Cloud City: Carbon Chamber": "Cloud City: Carbonite Chamber",
    "Bad Feeling Have 1": "Bad Feeling Have I",
    "Mobilizaton Points": "Mobilization Points",
    "Grand Admiral Trawn": "Grand Admiral Thrawn",
    "R2-A5 (droid)": "R2-A5 (Artoo-Ayfive)",
    "Hidden Base/Slip through": "Hidden Base",
    "Squadran Assignments": "Squadron Assignments",
    "Lt. Naytaan": "Lieutenant Naytaan",
    "Bren Quersy": "Bren Quersey",
    "Derek 'Hobbie' Kilivian": "Derek 'Hobbie' Klivian",
    "Red Sqaudron 4": "Red Squadron 4",
    "Red Sqaudron 7": "Red Squadron 7",
    "Is That Legal/ I Will Make It Legal": "My Lord, Is That Legal?",
    "My Lord, Is That Legal/ I Will Make It Legal": "My Lord, Is That Legal?",
    "My Lord, Is That Legal / I Will Make It Legal": "My Lord, Is That Legal?",
    "Dr. Evazan And Ponda Paba": "Dr. Evazan & Ponda Baba",
    "Edcel Bar Ganes": "Edcel Bar Gane",
    "Executer: Docking Bay": "Executor: Docking Bay",
    "Admiral Chinearu": "Admiral Chiraneau",
    "Captain Gilead Pellaeon": "Captain Gilad Pellaeon",
    "Dark Maneuvers/Tallon Roll": "Dark Maneuvers & Tallon Roll",
    "Projecton Of A Skywalker": "Projection Of A Skywalker",
    "Agents of the Black Sun/Vengance of the Dark Prince": "Agents Of Black Sun",
    "Infomration Exchange": "Information Exchange",
    "IMPERIAl navy helmsman": "Imperial Helmsman",
    "eg-6 power droid": "EG-6 (Eegee-Six)",
    "luke's speeder": "Luke's X-34 Landspeeder",
    "Wolking (V)": "Wokling (V)",
    "Commander Evram Lajae (V)": "Commander Evram Lajaie",
    "Colonel Feyn Gospic (V)": "Colonel Feyn Gospic",
    "Leia w/ Blaster Rifle": "Leia With Blaster Rifle",
    "Obi-Wan Kenobi w/ Lightsaber": "Obi-Wan With Lightsaber",
    "Strike Force": "Strikeforce",
    "Artoo-Deeto in Red 5": "Artoo-Detoo In Red 5",
    "Admeril ozzel": "Admiral Ozzel",
    "admeril motti": "Admiral Motti",
    "bobafett": "Boba Fett",
    "blizard walker": "Blizzard Walker",
    "captin lenox": "Captain Lennox",
    "chif bast": "Chief Bast",
    "captin jonus": "Captain Jonus",
    "djas phur": "Djas Puhr",
    "dr evazans sawed off blaster": "Dr. Evazan's Sawed-Off Blaster",
    "death sqadren": "Death Squadron",
    "dark colabortion": "Dark Collaboration",
    "dark manevers/tallon roll": "Dark Maneuvers & Tallon Roll",
    "ghanna gleemort": "Ghana Gleemort",
    "its worse": "It's Worse",
    "imperail class star destroyer": "Imperial-Class Star Destroyer",
    "jabbas sail barge": "Jabba's Sail Barge",
    "jabbas palace audeince chamber": "Jabba's Palace: Audience Chamber",
    "kitik keed kak": "Kitik Keed'kak",
    "lietenennt cabbel": "Lieutenant Cabbel",
    "major turr phener": "Major Turr Phennir",
    "miiyoom onith": "M'iiyoom Onith",
    "prohetess": "Prophetess",
    "rached hyst": "Rachalt Hyst",
    "scitar 2": "Scimitar 2",
    "skythe1": "Scythe 1",
    "tatooine jabbas palace": "Tatooine: Jabba's Palace",
    "visage of the emperer": "Visage Of The Emperor",
    "ob: rebel strike team/garrison destroyed": "Rebel Strike Team",
    "rebel strike team/garrison destroyed": "Rebel Strike Team",
    "colonel craken": "Colonel Cracken",
    "colonel craken (pilot)": "Colonel Cracken",
    "lieutenant blount (pilot)": "Lieutenant Blount",
    "captain yutani": "Captain Yutani",
    "lieutant greeve": "Lieutenant Greeve",
    "obi-wan, padawan learner": "Obi-Wan Kenobi, Padawan Learner",
    "obi-wan,padawan learner": "Obi-Wan Kenobi, Padawan Learner",
    "take the initative": "Take the Initiative",
    "Echo Base War Room": "Hoth: Echo Command Center (War Room)",
    "echo base war room": "Hoth: Echo Command Center (War Room)",
    "Echo Base Ops": "Echo Base Operations",
    "Gen. Calrissian": "General Calrissian",
    "Gen. Crix Madine": "General Crix Madine",
    "tydrium": "Tydirium",
    "convert landing": "Covert Landing",
    "Sai'tor Kal Fas": "Sai'torr Kal Fas",
    "Sal'torr Kal Fas": "Sai'torr Kal Fas",
    "Sal'torr Kal Fas (V)": "Sai'torr Kal Fas (V)",
    "Dr.Evazan & Ponda Baba": "Dr. Evazan & Ponda Baba",
    "Dr. Evazan & Ponda Baba": "Dr. Evazan & Ponda Baba",
    "Ommini Box & It's Worse": "Ommni Box & It's Worse",
    "Dengar In Punising One": "Dengar In Punishing One",
    "Caridia": "Carida",
    "court of the vile": "Court Of The Vile Gangster",
    "dangar": "Dengar",
    "dr. e and ponda b": "Dr. Evazan & Ponda Baba",
    "he's all yours bounty hunter": "He's All Yours, Bounty Hunter",
    "docking bay for tatooine": "Tatooine: Docking Bay 94",
    "fett in slave 1": "Boba Fett In Slave I",
    "dengar in dunishing one": "Dengar In Punishing One",
    "death star assualt squdron": "Death Star Assault Squadron",
    "flagship exector": "Flagship Executor",
    "B-Wing": "B-wing Attack Fighter",
    "Tat DB": "Tatooine: Docking Bay 94",
    "Chewie protector": "Chewbacca, Protector",
    "Cap. Han": "Captain Han Solo",
    "Artoo-Detoo in Red5": "Artoo-Detoo In Red 5",
    "Artoo-Detoo in Red 5": "Artoo-Detoo In Red 5",
    "Luke Skywalker,Jedi Knight": "Luke Skywalker, Jedi Knight",
    "Luke, JK": "Luke Skywalker, Jedi Knight",
    "Gift of a Mentor": "Gift Of The Mentor",
    "Clash Of Saber": "Clash Of Sabers",
    "You Can Either Profit By this..../Or Be Destroyed": "You Can Either Profit By This...",
    "Jabaa's Palace: Audiance Chamber": "Jabba's Palace: Audience Chamber",
    "Chebacca, Protector": "Chewbacca, Protector",
    "What're You Tryin' To Puch On Us?": "What're You Tryin' To Push On Us?",
    "Becta Tack": "Bacta Tank",
    "Run Luke, Run": "Run Luke, Run!",
    "Out Of Commission & Transmition Terminated": "Out Of Commission & Transmission Terminated",
    "Ree-Yee": "Ree-Yees",
    "Heading For The Med Frigate": "Heading For The Medical Frigate",
    "Jar Jar's Pole": "Jar Jar's Electropole",
    "Ke Chu Ke Kukuta": "Ke Chu Ke Kukuta?",
    "Hold Together": "Hear Me Baby, Hold Together",
    "Hear Me Baby, Hold Together": "Hear Me Baby, Hold Together",
    "Docking Bay 327": "Death Star: Docking Bay 327",
    "Darth Maul (T)": "Darth Maul, Young Apprentice",
    "Sith Infiltrator": "Maul's Sith Infiltrator",
    "Scimitar Squadron Tie": "Scimitar Squadron TIE",
    "Neimodian Advisor": "Neimoidian Advisor",
    "I Can't Shake Him": "I Can't Shake Him!",
    "IAO / Secret Plans": "Imperial Arrest Order & Secret Plans",
    "Home one DB": "Home One: Docking Bay",
    "Obi-Wan (Premiere)": "Obi-Wan Kenobi",
    "Obi-Wan": "Obi-Wan Kenobi",
    "This Deal": "This Deal Is Getting Worse All The Time",
    "Upper Walkway": "Cloud City: Upper Walkway",
    "IAO & SP": "Imperial Arrest Order & Secret Plans",
    "Downtown Plaza": "Cloud City: Downtown Plaza",
    "Casino": "Cloud City: Casino",
    "Iggy w/ Gun": "IG-88 With Riot Gun",
    "Sidious": "Darth Sidious",
    "Palpatine": "Emperor Palpatine",
    "Obsidian TIE": "Obsidian Squadron TIE",
    "OS-72-1 in Ob1": "OS-72-1 In Obsidian 1",
    "CCOcc": "Cloud City Occupation",
    "Imp Artillery": "Imperial Artillery",
    "Lando w/ Vibro Axe": "Lando With Vibro-Ax",
    "Jar-Jar Binks": "Jar Jar Binks",
    "Mellinium Falcon": "Millennium Falcon",
    "Omni Box": "Ommni Box",
    "Raltiir Operations/In the Hands of the Empire": "Ralltiir Operations",
    "Ralltiir Operations/In The Hand Of The Empire": "Ralltiir Operations",
    "M'iiyoom Oonith": "M'iiyoom Onith",
    "Royal Guards": "Royal Guard",
    "Yave 4: War Room": "Yavin 4: Massassi War Room",
    "Slight Weapons Malfuntion": "Slight Weapons Malfunction",
    "Closer?": "Closer?!",
    "Qui-Gon w/ Lightsaber": "Qui-Gon Jinn With Lightsaber",
    "IT-0": "IT-O (Eyetee-Oh)",
    "WED15-1662 'Treadwell' Droid": "WED15-I662 'Treadwell' Droid",
    "IM4-099": "IM4-099 (Eyeemmfour)",
    "Airica": "Arica",
    "Captin Needa": "Captain Needa",
    "Rector Terminal": "Reactor Terminal",
    "Besieged (V)": "Besieged",
    "Fondor system": "Fondor",
    "Corulag system": "Corulag",
    "Rendili system": "Rendili",
    "Oo-ta Goo-ta, Solo (V)": "Oo-ta Goo-ta, Solo? (V)",
    "Oo-ta Goo-ta, Solo": "Oo-ta Goo-ta, Solo?",
    "Pray I Don't Alter It Any Futher": "Pray I Don't Alter It Any Further",
    "You Swindled Me": "You Swindled Me!",
    "Hoth: Main Power Generators 1st Marker": "Hoth: Main Power Generators",
    "Hoth: North Ridge 4th Marker": "Hoth: North Ridge",
    "Artoo-Deto In Red 5": "Artoo-Detoo In Red 5",
    "Set Your Course For Alderaan/ The Ultimate Power In The Universe": "Set Your Course For Alderaan",
    "Rendili Star Drive": "Rendili StarDrive",
    "My Kind Of Scum/ Fearless And Inventive": "My Kind Of Scum",
    "Rep: Ghana Gleemort": "Ghana Gleemort",
    "Gamorrean Guards": "Gamorrean Guard",
    "Tusken Raiders": "Tusken Raider",
    "Salicious Crumb": "Salacious Crumb",
    "Endor Operations/ Imperial Outpost": "Endor Operations",
    "Battle Order % First Strike": "Battle Order & First Strike",
    "WED 9M1 Bantha Droid": "WED-9-M1 'Bantha' Droid",
    "Rendevouz Point": "Rendezvous Point",
    "ISB Operations/Empire's Sinister Agents": "ISB Operations",
    "Captain Piet": "Captain Piett",
    "Stormtrooper Garison": "Stormtrooper Garrison",
    "Hoth Echo Corridor": "Hoth: Echo Corridor",
    "Hoth Echo Docking Bay": "Hoth: Echo Docking Bay",
    "Sense& Recoil In Fear": "Sense & Recoil In Fear",
    "Coruscant Jedi Council Chamber": "Coruscant: Jedi Council Chamber",
    "ISBO": "ISB Operations",
    "Courascant: Imperial Square": "Coruscant: Imperial Square",
    "Sergant Tarl": "Sergeant Tarl",
    "Vaders Lightsaber (Premier)": "Vader's Lightsaber",
    "Projected Telepathy": "Projective Telepathy",
    "Under Cover": "Undercover",
    "Courasant DB": "Coruscant: Docking Bay",
    "Courascant: Imperial City": "Coruscant: Imperial City",
    "Courascant (SE)": "Coruscant",
    "Generic Dockingbay": "Spaceport Docking Bay",
    "Mobilization Pts": "Mobilization Points",
    "DV w/saber": "Darth Vader With Lightsaber",
    "Darth Maul w/saber": "Darth Maul With Lightsaber",
    "Darth Maul w/Saber": "Darth Maul With Lightsaber",
    "Coruscant: DB": "Coruscant: Docking Bay",
    "Coruscant:DB": "Coruscant: Docking Bay",
    "BHBM/TYFP": "Bring Him Before Me",
    "DSII:Throne Room": "Death Star II: Throne Room",
    "DSII:DB": "Death Star II: Docking Bay",
    "IAO": "Imperial Arrest Order",
    "Fear is M Ally": "Fear Is My Ally",
    "Prep'd Defenses": "Prepared Defenses",
    "There is No Try & Oppresive Enforcement": "There Is No Try & Oppressive Enforcement",
    "Allegations fo Corruption": "Allegations Of Corruption",
    "You Cannot Hde Forever": "You Cannot Hide Forever",
    "d*: Central Core": "Death Star: Central Core",
    "d*: Conference Room": "Death Star: Conference Room",
    "d*: War Room": "Death Star: War Room",
    "da: Cave": "Dagobah: Cave",
    "h: Wampa Cave": "Hoth: Wampa Cave",
    "ex: Meditation Chamber": "Executor: Meditation Chamber",
    "Thero Nett": "Theron Nett",
    "Greeen Squadron 3": "Green Squadron 3",
    "Lift Tubes": "Lift Tube",
    "A Million Voices": "A Million Voices Crying Out",
    "Omni Box & It's Worse": "Ommni Box & It's Worse",
    "Weapon Levitaion": "Weapon Levitation",
    "Enter the Burueacrat": "Enter The Bureaucrat",
    "You're All Clear Kid": "You're All Clear Kid!",
    "Youre All Clear Kid": "You're All Clear Kid!",
    "CC: Incinerator": "Cloud City: Incinerator",
    "Luke Skywalker: RS": "Luke Skywalker, Rebel Scout",
    "Lando": "Lando Calrissian",
    "Seargent Edian": "Sergeant Edian",
    "21b (V)": "2-1B (Too-Onebee)",
    "21B (V)": "2-1B (Too-Onebee)",
    "2-1B (V)": "2-1B (Too-Onebee)",
    "Han's Blaster (V)": "Han's Heavy Blaster Pistol (V)",
    "Into The Ventilation Shaft Lefty": "Into The Ventilation Shaft, Lefty",
    "The Bith Shuffle & Desprate Reach": "The Bith Shuffle & Desperate Reach",
    "Flyboy (V)": "Into The Garbage Chute, Flyboy",
    "Into The Garbage Chute, Flyboy (V)": "Into The Garbage Chute, Flyboy",
    "Do, or do not & Wise Advise": "Do, Or Do Not & Wise Advice",
    "Do, or Do Not & Wise Advise": "Do, Or Do Not & Wise Advice",
    "or do not & Wise Advise": "Do, Or Do Not & Wise Advice",
    "Wise Advise": "Wise Advice",
    "Endor: landing platform DB": "Endor: Landing Platform (Docking Bay)",
    "Endor: Landing Platform DB": "Endor: Landing Platform (Docking Bay)",
    "3, 720 To 1": "3,720 To 1",
    "3,720 To 1": "3,720 To 1",
    "You Cannon Hide Forever & Mobilization Points": "You Cannot Hide Forever & Mobilization Points",
    "Blizard Scout 1 (V)": "Blizzard Scout 1",
    "Blizzard Scout 1 (V)": "Blizzard Scout 1",
    "Security Precautions (V)": "Security Precautions",
    "Sai'torr Kel Fas (V)": "Sai'torr Kal Fas (V)",
    "Sai'torr Kel Fas (v)": "Sai'torr Kal Fas (V)",
    "Cloud City: Docking Bay 327": "Cloud City: Platform 327 (Docking Bay)",
    "Out Of Commission/Transmission Terminated": "Out Of Commission & Transmission Terminated",
    "Commander Luke Skywalker (V)": "Commander Luke Skywalker",
    "General Carlist Rieekan (V)": "General Carlist Rieekan",
    "Dual Laser Cannon (V)": "Dual Laser Cannon",
    "Derek \"Hobbie\" Klivan": "Derek 'Hobbie' Klivian",
    "Derek 'Hobbie' Klivan": "Derek 'Hobbie' Klivian",
    "Derek 'Hobbie' Kilvian": "Derek 'Hobbie' Klivian",
    "Wedge Antillies, Red Squadron Leader": "Wedge Antilles, Red Squadron Leader",
    "Squad Assignments": "Squadron Assignments",
    "Millenium Falcon": "Millennium Falcon",
    "Commander Evram Lajaie (V)": "Commander Evram Lajaie",
    "No Money, No Parts, No Deal!/You're A Slave?": "No Money, No Parts, No Deal!",
    "No Money, No Parts, No Deal! / You're A Slave?": "No Money, No Parts, No Deal!",
    "Bib Fortuna (reflections3)": "Bib Fortuna",
    "Masterful Move And Endor Occupation": "Masterful Move & Endor Occupation",
    "ISB Operations/ Emperor's Sinister Agents": "ISB Operations",
    "ISB Operations/Emperor's Sinister Agents": "ISB Operations",
    "Yavin IV: Docking Bay": "Yavin 4: Docking Bay",
    "Corpral Derdram": "Corporal Derdram",
    "Corpral Breezer": "Corporal Beezer",
    "Corporal Breezer": "Corporal Beezer",
    "Corpral Janse": "Corporal Janse",
    "Thok and Thug": "Thok & Thug",
    "You Cannot Hide Forever and Mobilization Points": "You Cannot Hide Forever & Mobilization Points",
    "Zuckuss's Snare Rifle": "Zuckuss' Snare Rifle",
    "Medium Bulk Frieghter": "Medium Bulk Freighter",
    "Hoth: Echo Command Center 9 (War Room)": "Hoth: Echo Command Center (War Room)",
    "Hoth: Echo Command Center 9(War Room)": "Hoth: Echo Command Center (War Room)",
    "Hoth: Main Generators": "Hoth: Main Power Generators",
    "Couruscant: Jedi Council Chamber": "Coruscant: Jedi Council Chamber",
    "A Jedi's Patients": "A Jedi's Patience",
    "Docking And Repair Facility": "Docking And Repair Facilities",
    "Obi-Wan's Lightsaber (ep 1)": "Obi-Wan's Lightsaber",
    "Lando, Calrissian": "Lando Calrissian",
    "General Veers (V)": "General Veers",
    "Blizzard 2 (V)": "Blizzard 2",
    "Blizzard 1 (V)": "Blizzard 1",
    "Captain Piett (V)": "Captain Piett",
    "Captain Lennox (V)": "Captain Lennox",
    "Sergeant Major Bursk (V)": "Sergeant Major Bursk",
    "Imperial Occupation/Imperial Control (V)": "Imperial Occupation",
    "Imperial Occupation / Imperial Control (V)": "Imperial Occupation",
    "Imperial Occupation (V)": "Imperial Occupation",
    "Imperial Control (V)": "Imperial Control",
    "Imperial Domination (V)": "Imperial Domination",
    "Reactor Terminal (V)": "Reactor Terminal",
    "Death Squadron (V)": "Death Squadron",
    "Send A Detachment Down (V)": "Send A Detachment Down",
    "A Dark Time For The Rebellion (V)": "A Dark Time For The Rebellion",
    "Debris Zone (V)": "Debris Zone",
    "Stop Motion (V)": "Stop Motion",
    "AT-AT Cannon (V)": "AT-AT Cannon",
    "I Find Your Lack Of Faith (V)": "I Find Your Lack Of Faith Disturbing",
    "Motti (V)": "Admiral Motti (V)",
    "We'll Let Fate Decide, Huh?": "We'll Let Fate-A Decide, Huh?",
    "We will handle this": "We'll Handle This",
    "Naboo: Docking Bay": "Naboo: Theed Palace Docking Bay",
    "Naboo: Generator Core": "Naboo: Theed Palace Generator Core",
    "Naboo: Generator": "Naboo: Theed Palace Generator",
    "Naboo: Throne Room": "Naboo: Theed Palace Throne Room",
    "Qui Gon Jinn, jedi master": "Qui-Gon Jinn, Jedi Master",
    "Qui-Gon Jinn, jedi master": "Qui-Gon Jinn, Jedi Master",
    "Qui Gon's Saber": "Qui-Gon's Lightsaber",
    "Obiwan's Lightsaber": "Obi-Wan's Lightsaber",
    "You will find i'm full of surprises": "You'll Find I'm Full Of Surprises",
    "You Will Find That I Am Full Of Surprises": "You'll Find I'm Full Of Surprises",
    "They win this round": "They Win This Round",
    "Twilek Advisor": "Twi'lek Advisor",
    "Saber Proficiency": "Lightsaber Proficiency",
    "Secure Root": "Secure Route",
    "Secure Position": "Secure Route",
    "This deal is getting worse all the time": "This Deal Is Getting Worse All The Time",
    "Batle Droid officer": "Battle Droid Officer",
    "Aura Sing": "Aurra Sing",
    "Aurra Sing's BR": "Aurra Sing's Blaster Rifle",
    "Bobba Fett in Slave 1": "Boba Fett In Slave I",
    "Darth Vader's saber": "Vader's Lightsaber",
    "Figther Cover": "Fighter Cover",
    "All too Easy": "All Too Easy",
    "They must never again leave this city": "They Must Never Again Leave This City",
    "Obsidian Squadron Tie": "Obsidian Squadron TIE",
    "Battle Droid BR": "Battle Droid Blaster Rifle",
    "OWO-1 w/ backup": "OWO-1 With Backup",
    "OWO-1 With Backup Droid": "OWO-1 With Backup",
    "Deflector Shield Generators (V)": "Deflector Shield Generators",
    "Leia w/Blaster Rifle": "Leia With Blaster Rifle",
    "Chewie w/Blaster Rifle": "Chewie With Blaster Rifle",
    "Yavin 4 massassi war room": "Yavin 4: Massassi War Room",
    "Tatoine: lars' moisture farm": "Tatooine: Lars' Moisture Farm",
    "Tatoine: mos esley": "Tatooine: Mos Eisley",
    "Tatoine: dune sea": "Tatooine: Dune Sea",
    "Tatoine Utility Belt": "Tatooine Utility Belt",
    "Collision !": "Collision",
    "Don't Get Too Cocky": "Don't Get Cocky",
    "There is good in him/I can Save him": "There Is Good In Him",
    "Jedi Knight": "Luke Skywalker, Jedi Knight",
    "Reactor TerminalLateral Damage": "Reactor Terminal",
    "Afect mind": "Affect Mind",
    "MPG": "Main Power Generators",
    "4th marker": "Hoth: North Ridge (4th Marker)",
    "3rd Marker": "Hoth: Defensive Perimeter (3rd Marker)",
    "2nd Marker": "Hoth: Snow Trench (2nd Marker)",
    "Maneuvering Flaps (V)": "Maneuvering Flaps",
    "Echo DB": "Hoth: Echo Docking Bay",
    "Captain Solo": "Captain Han Solo",
    "Commander Luke (V)": "Commander Luke Skywalker",
    "Commander Wedge": "Commander Wedge Antilles",
    "Dack": "Dack Ralter",
    "General Rieekan (V)": "General Carlist Rieekan",
    "Local Uprising/Liberation (V)": "Local Uprising",
    "Heading for": "Heading For The Medical Frigate",
    "Squad. Assignments": "Squadron Assignments",
    "We'll Handle This/Duel Of The fades": "We'll Handle This",
    "Wockling (V)": "Wokling (V)",
    "Set Your Course For Alderaan/The Ultimate": "Set Your Course For Alderaan",
    "DS: DockingBay": "Death Star: Docking Bay 327",
    "Come Here You Big Howard": "Come Here, You Big Coward",
    "You Cannot Hide Forever + Mob Points": "You Cannot Hide Forever & Mobilization Points",
    "Derek 'Hobbie' Kilivan": "Derek 'Hobbie' Klivian",
    "Attack Pattern Delta (V)": "Attack Pattern Delta",
    "DBO/MDTYR": "Dantooine Base Operations",
    "Chewie w/Rifle": "Chewie With Blaster Rifle",
    "Qui-Gon w/Stick": "Qui-Gon Jinn With Lightsaber",
    "Luke w/Stick": "Luke With Lightsaber",
    "Obi w/Stick": "Obi-Wan With Lightsaber",
    "B-Wing Attack Squad": "B-wing Attack Fighter",
    "X-Wing Assault Squad": "X-wing Assault Squadron",
    "Y-Wing Assault Squad": "Y-wing Assault Squadron",
    "Suprise Assault": "Surprise Assault",
    "Set Your Course For Alderaan (3ANTH)": "Set Your Course For Alderaan",
    "Tat: hut trade rout": "Tatooine: Hutt Trade Route (Desert)",
    "Nar shaddaa wind chims & out of somwhere": "Nar Shaddaa Wind Chimes & Out Of Somewhere",
    "vaporatior": "Vaporator",
    "hydrosponics station": "Hydroponics Station",
    "Tat: Jawa camp": "Tatooine: Jawa Camp",
    "Tat: Jundland wastes": "Tatooine: Jundland Wastes",
    "Tat: Jawa canyon": "Tatooine: Jawa Canyon",
    "Cardia": "Carida",
    "IT-0 (V)": "IT-O (Eyetee-Oh)",
    "Bossk in Hound's Touth": "Bossk In Hound's Tooth",
    "Oo-ta Goo-ta Solo? (V)": "Oo-ta Goo-ta, Solo? (V)",
    "Tatooine (pre)": "Tatooine",
    "a tragedy has occured": "A Tragedy Has Occurred",
    "A Tragedy Has Occured": "A Tragedy Has Occurred",
    "I Find Your Lack Of Faith": "I Find Your Lack Of Faith Disturbing",
    "LE-BO2O9": "LE-BO2D9 (Leebo)",
    "Rebel Princess": "Leia, Rebel Princess",
    "Sai-torr Kal Fas (V)": "Sai'torr Kal Fas (V)",
    "Yoda's Gimmer Stick": "Yoda's Gimer Stick",
    "Main Power Generators": "Hoth: Main Power Generators (1st Marker)",
    "Hoth: Main Power Generators": "Hoth: Main Power Generators (1st Marker)",
    "Lock (V)": "Romas \"Lock\" Navander",
    "Wes": "Wes Janson",
    "Zev": "Zev Senesca",
    "Plusar Skate": "Pulsar Skate",
    "Echo Med Lab (V)": "Hoth: Echo Med Lab",
    "Snow Trench": "Hoth: Snow Trench (2nd Marker)",
    "Defense Perimeter": "Hoth: Defensive Perimeter (3rd Marker)",
    "Zev Zenesca": "Zev Senesca",
    "Tryn Farr (V)": "Toryn Farr",
    "Romas 'Lock' Navander": "Romas \"Lock\" Navander",
    "Dack Raltar": "Dack Ralter",
    "Red Squadron Leader": "Red Leader",
    "T47 Battle Formation": "T-47 Battle Formation",
    "Han, Chewie+Falcon": "Han, Chewie, And The Falcon",
    "Han, Chewie & Falcon": "Han, Chewie, And The Falcon",
    "HanChewie+Falcon": "Han, Chewie, And The Falcon",
    "HanChewie & Falcon": "Han, Chewie, And The Falcon",
    "Rogue1": "Rogue 1",
    "Rogue2": "Rogue 2",
    "Rogue3": "Rogue 3",
    "Rogue4": "Rogue 4",
    "Obi Wan, Jedi Knight": "Obi-Wan Kenobi",
    "Scoundrel": "Lando Calrissian, Scoundrel",
    "Are You Brain Dead": "Are You Brain Dead?!",
    "Anakin's LS": "Anakin's Lightsaber",
    "Luke's LS": "Luke's Lightsaber",
    "Qui-Gon's LS": "Qui-Gon Jinn's Lightsaber",
    "Vader's LS": "Vader's Lightsaber",
    "Maul's Double Bladed LS": "Maul's Double-Bladed Lightsaber",
    "Artoo In Red5": "Artoo-Detoo In Red 5",
    "Baron Sontir Fel": "Baron Soontir Fel",
    "Dr.E": "Dr. Evazan",
    "Black2 (V)": "Black 2 (V)",
    "Saber1": "Saber 1",
    "Blizzard4": "Blizzard 4",
    "Stalker (V)": "Stalker",
    "Projection of a Skywalker": "Projection Of A Skywalker",
    "Any Methods Necessary (ENC)": "Any Methods Necessary",
    "IG-88 With Riot Gun (ENCC0": "IG-88 With Riot Gun",
    "Dr. Evazen's Sawed-off Blaster": "Dr. Evazan's Sawed-off Blaster",
    "Dr. Evazen’s Sawed-off Blaster": "Dr. Evazan's Sawed-off Blaster",
    "Dr. Evazen’s Sawed-off Blaster": "Dr. Evazan's Sawed-off Blaster",
    "Sai'Tor'Kal Fas (V)": "Sai'torr Kal Fas (V)",
    "Houjixx & Out of Nowhere": "Houjix & Out Of Nowhere",
    "Houjixx": "Houjix",
    "Bith Shuffle & Desperate Reach": "The Bith Shuffle & Desperate Reach",
    "Blaster Proficiency & Combo": "Sorry About The Mess & Blaster Proficiency",
    "SorryAboutTheMess & BlasterProficiency": "Sorry About The Mess & Blaster Proficiency",
    "Romas 'Lock' Navander (V)": "Romas \"Lock\" Navander",
    "Romas “Lock” Navander (V)": "Romas \"Lock\" Navander",
    "Chadrila": "Chandrila",
    "Docking And Repair Facilies": "Docking And Repair Facilities",
    "Correllian Slip": "Corellian Slip",
    "Heavy Turbolaser Batteries": "Heavy Turbolaser Battery",
    "Massassi Base Operations/One In A Million": "Massassi Base Operations",
    "You're All Clear, Kid!": "You're All Clear Kid!",
    "Youre All Clear, Kid!": "You're All Clear Kid!",
    "Death Star Trench": "Death Star: Trench",
    "Death Star:Trench": "Death Star: Trench",
    "Premiere Vader": "Darth Vader",
    "Mara Jade, THE": "Mara Jade, The Emperor's Hand",
    "Bobo Fett, BH": "Boba Fett, Bounty Hunter",
    "Bobo Fett": "Boba Fett",
    "Dr.Evazon & PB": "Dr. Evazan & Ponda Baba",
    "Maul's double stick": "Maul's Double-Bladed Lightsaber",
    "Always Thinking with You Stomach": "Always Thinking With Your Stomach",
    "Image of the Dark Lord (V)": "Image Of The Dark Lord",
    "Local Uprising/ Liberation (V)": "Local Uprising",
    "Local Uprising/Liberation (V)": "Local Uprising",
    "Commander Luke Skwalker (V)": "Commander Luke Skywalker",
    "Tigram Jamiro (V)": "Tigran Jamiro",
    "Walker Sighting (V)": "Walker Sighting",
    "Great Shot Kid!": "Great Shot, Kid!",
    "An Unusual Amount of Fear w/Enhanced Proton Torpedoes": "An Unusual Amount Of Fear",
    "and Attack Run": "Attack Run",
    "Wedge Antiles, Red Squadron Leader": "Wedge Antilles, Red Squadron Leader",
    "General Dodanna (V)": "General Dodonna",
    "General Dodanna(v)": "General Dodonna",
    "Rhomas \"Lock\" Navender (V)": "Romas \"Lock\" Navander",
    "Rhomas \"Lock\" Navender(v)": "Romas \"Lock\" Navander",
    "Toryn Farr (V)": "Toryn Farr",
    "Wryon Serper (V)": "Wyron Serper",
    "Red Squadron One": "Red Squadron 1",
    "X-Wing Lasers": "X-wing Laser Cannon",
    "Coruscant (sped)": "Coruscant",
    "Short-Range Fighers": "Short-Range Fighters",
    "Squadron Assignment": "Squadron Assignments",
    "Cloud City: Lower Corrider": "Cloud City: Lower Corridor",
    "Im Sorry": "I'm Sorry",
    "Dantoine": "Dantooine",
    "Correscant": "Coruscant",
    "Ralitir": "Ralltiir",
    "Kessel (one is base)": "Kessel",
    "Dantooine Base Operations/More Dangerous Than You Realize": "Dantooine Base Operations",
    "Ice Plains": "Hoth: Ice Plains (5th Marker)",
    "Htoh: Mountains": "Hoth: Mountains (6th Marker)",
    "Target The Main Generators": "Target The Main Generator",
    "dabobah: yoda's hut": "Dagobah: Yoda's Hut",
    "dabobah:yoda's hut": "Dagobah: Yoda's Hut",
    "Jabba's Palace Dungeon": "Jabba's Palace: Dungeon",
    "No Bargain or Power of the Hutt": "No Bargain",
    "Victory-Class Stardestroyer": "Victory-Class Star Destroyer",
    "CC: Incinterator": "Cloud City: Incinerator",
    "Cloud City: Incinterator": "Cloud City: Incinerator",
    "Yavin 4: Breifing Room": "Yavin 4: Briefing Room",
    "Bomarr Monk": "B'omarr Monk",
    "Out of Somewhere & Nar Shadda Chimes": "Nar Shaddaa Wind Chimes & Out Of Somewhere",
    "Out Of Somewhere & Nar Shadda Chimes": "Nar Shaddaa Wind Chimes & Out Of Somewhere",
    "M-iiyoom Onith": "M'iiyoom Onith",
    "Reacter Terminal": "Reactor Terminal",
    "Oh Switch Off": "Oh, Switch Off",
    "Qui Gon w/ Lightsaber": "Qui-Gon Jinn With Lightsaber",
    "Qui-Gon w/ Lightsaber": "Qui-Gon Jinn With Lightsaber",
    "Yavin 4: Massassi HQ": "Yavin 4: Massassi Headquarters",
    "Wesa Gotta A Grand Army": "Wesa Gotta Grand Army",
    "Set Your Course To Alderaan": "Set Your Course For Alderaan",
    "Set Your Course To Alderaan / The Ultimate Power In The Universe": (
        "Set Your Course For Alderaan"
    ),
    "Set Your Course For Alderaan / The Ultimate Power In The Universe": (
        "Set Your Course For Alderaan"
    ),
    "Set Your Course for Alderaan/The Ultimate Power in the Universe": (
        "Set Your Course For Alderaan"
    ),
    "Set Your Course For Alderaan/The Ultimate Power In The Universe": (
        "Set Your Course For Alderaan"
    ),
    "Commence primay igntion": "Commence Primary Ignition",
    "Deflector Sheild Generator (V)": "Deflector Shield Generators",
    "Deflector Shield Generator (V)": "Deflector Shield Generators",
    "Deflector Sheild Generator": "Deflector Shield Generators",
    "Deflector Shield Generator": "Deflector Shield Generators",
    "Executor, Control Station": "Executor: Control Station",
    "Executor, Comm Station": "Executor: Comm Station",
    "Executor, main corridor": "Executor: Main Corridor",
    "Executor, Main Corridor": "Executor: Main Corridor",
    "Executor, Holotheater": "Executor: Holotheatre",
    "Executor, Meditation Chamber": "Executor: Meditation Chamber",
    "Executor, docking bay": "Executor: Docking Bay",
    "Executor, Docking Bay": "Executor: Docking Bay",
    "DS, Docking bay": "Death Star: Docking Bay 327",
    "DS, Docking Bay": "Death Star: Docking Bay 327",
    "DS, Level 4 Corridor": "Death Star: Level 4 Military Corridor",
    "DS, War Room": "Death Star: War Room",
    "Yavin 4, docking bay": "Yavin 4: Docking Bay",
    "Yavin 4, Docking Bay": "Yavin 4: Docking Bay",
    "Death Star DB 327": "Death Star: Docking Bay 327",
    "Captain Godhert": "Captain Godherdt",
    "Kashyyk": "Kashyyyk",
    "Chimera": "Chimaera",
    "Boba Fett With Balster Rifle": "Boba Fett With Blaster Rifle",
    "Navy Trooper Shield Tech": "Navy Trooper Shield Technician",
    "Sgt. Tarl": "Sergeant Tarl",
    "Lambada-class Shuttle": "Lambda-Class Shuttle",
    "Lambada-Class Shuttle": "Lambda-Class Shuttle",
    "Any Methods Neccessary": "Any Methods Necessary",
    "Seargeant Elsek": "Sergeant Elsek",
    "Seargeant Major Bursk (V)": "Sergeant Major Bursk",
    "Sergeant Major Bursk (V)": "Sergeant Major Bursk",
    "Local Trouble (V)": "Local Defense",
    "Local Trouble": "Local Defense",
    "Courscant": "Coruscant",
    "Doda Bodonawieedo": "Dodo Bodonawieedo",
    "Oota Goota, Solo? (V)": "Oo-ta Goo-ta, Solo? (V)",
    "Oota Goota, Solo?": "Oo-ta Goo-ta, Solo?",
    "Scum & Villany": "Scum And Villainy",
    "Qui-Gon Jinn Jedi Knight": "Qui-Gon Jinn",
    "Porn Star Threepio": "Threepio With His Parts Showing",
    "R2 D2 in Red 5": "Artoo-Detoo In Red 5",
    "R2 D2 In Red 5": "Artoo-Detoo In Red 5",
    "Han Chewie & Falcon": "Han, Chewie, And The Falcon",
    "Qui-Gon's R3 Lightsaber": "Qui-Gon Jinn's Lightsaber",
    "Nute Gunray, Neimodian Viceroy": "Nute Gunray, Neimoidian Viceroy",
    "Blockage Battleship: Bridge": "Blockade Flagship: Bridge",
    "Krayt Dragon Bones (V)": "Krayt Dragon Bones",
    "Stop Motion- (V)": "Stop Motion",
    "Stop Motion (V)": "Stop Motion",
    "Zuckuss In Mist Hunter-": "Zuckuss In Mist Hunter",
    "Tattoine: great pit of Carkoon": "Tatooine: Great Pit Of Carkoon",
    "Tattoine: Great Pit Of Carkoon": "Tatooine: Great Pit Of Carkoon",
    "Dejas Puhr (V)": "Djas Puhr (V)",
    "Dejas Puhr": "Djas Puhr",
    "Dr Evazon's Sawed-off Blaster": "Dr. Evazan's Sawed-off Blaster",
    "Dr. Evazan Sawed-off Blaster": "Dr. Evazan's Sawed-off Blaster",
    "Ponda Boba's Hold-out Blaster": "Ponda Baba's Hold-out Blaster",
    "Watch Your Back": "Watch Your Back!",
    "Jabbas through with you": "Jabba's Through With You",
    "No money, no part, no deal!": "No Money, No Parts, No Deal!",
    "No Money, No Parts, No Deal!/You're A Slave?": "No Money, No Parts, No Deal!",
    "No money, no part, no deal! / You're a slave?": "No Money, No Parts, No Deal!",
    "Dertroyer Droid": "Destroyer Droid",
    "Vaders's Lightsaber": "Vader's Lightsaber",
    "Sense/Uncertain is the Future": "Sense & Uncertain Is The Future",
    "Sense/Uncertain Is The Future": "Sense & Uncertain Is The Future",
    "Evacuate?": "You Overestimate Their Chances",
    "Darth Vader, Dark Lord of Sith": "Darth Vader, Dark Lord Of The Sith",
    "What're You Tryin To Push On Us?": "What're You Tryin' To Push On Us?",
    "Wookie Roar": "Wookiee Roar",
    "Out Of Commission and Transmission Terminated": (
        "Out Of Commission & Transmission Terminated"
    ),
    "Sense and Recoil In Fear": "Sense & Recoil In Fear",
    "Sense/Recoil In Fear": "Sense & Recoil In Fear",
    "Rebal Planners": "Rebel Planners",
    "Rebal Fleet": "Rebel Fleet",
    "Genareal Calrissian": "General Calrissian",
    "Wedge Antilles (any)": "Wedge Antilles",
    "Green Squdron 1": "Green Squadron 1",
    "Red Squdron X-wing": "Red Squadron X-wing",
    "Naboo: Jungle": "Jungle",
    "Naboo: DB": "Naboo: Theed Palace Docking Bay",
    "Captain Dolfine TP": "Captain Daultay Dofine",
    "Tank Comander": "Tank Commander",
    "Maul Saber": "Maul's Double-Bladed Lightsaber",
    "Droid S. Laser cannon": "Droid Starfighter Laser Cannons",
    "Dfs-Squadron": "Droid Starfighter",
    "Aat Assault Leader": "AAT Assault Leader",
    "Aat": "Armored Attack Tank",
    "Fight Cover": "Fighter Cover",
    "Derek Hobbie Klivian": "Derek 'Hobbie' Klivian",
    "R2D2 (V)": "R2-D2 (Artoo-Detoo) (V)",
    "R2D2": "R2-D2 (Artoo-Detoo)",
    "21-B (V)": "2-1B (Too-Onebee)",
    "21-B": "2-1B (Too-Onebee)",
    "Speak To The Jedi Council": "Speak With The Jedi Council",
    "We're You Looking For Me?": "Were You Looking For Me?",
    "Are You Brain Dead?": "Are You Brain Dead?!",
    "Nar Shaada Wind Chimes & Out Of Somewhere": (
        "Nar Shaddaa Wind Chimes & Out Of Somewhere"
    ),
    "Nar Shaada Wind Chimes": "Nar Shaddaa Wind Chimes",
    "D-Class Heavy Cruiser": "Dreadnaught-Class Heavy Cruiser",
    "Boba Fett in S1": "Boba Fett In Slave I",
    "Quiet Mining Colony/Independant Operation": "Quiet Mining Colony",
    "Cloud City: East Platform Docking Bay": "Cloud City: East Platform (Docking Bay)",
    "Boba Fett (CC Version)": "Boba Fett",
    "Zuckuss Snare Rifle": "Zuckuss' Snare Rifle",
    "Lando Calrissian, Scoundril": "Lando Calrissian, Scoundrel",
    "Briskey Morning Munchen": "Brisky Morning Munchen",
    "Captin Gilad Pelleaeon": "Captain Gilad Pellaeon",
    "Captin Godherdt": "Captain Godherdt",
    "Death Star Assault Squaron": "Death Star Assault Squadron",
    "Dominater": "Dominator",
    "Leesub Sirin": "Leesub Sirln",
    "Owen Lars& Beru Lars": "Owen Lars & Beru Lars",
    "Jedi Saber": "Jedi Lightsaber",
    "Inconsequentail Losses": "Inconsequential Losses",
    "Death Star 2 Throne Room": "Death Star II: Throne Room",
    "Prepare Defenses": "Prepared Defenses",
    "Emperor Pal": "Emperor Palpatine",
    "Full Scale Assult": "Full Scale Alert",
    "Ability Ability Ability": "Ability, Ability, Ability",
    "Boba Fett in Slave One": "Boba Fett In Slave I",
    "Zuccuss in Mist Hunter": "Zuckuss In Mist Hunter",
    "Qui-Gon Ginn": "Qui-Gon Jinn",
    "Found Someone Have You": "Found Someone You Have",
    "Tunnel Vison": "Tunnel Vision",
    "Visored Vison": "Visored Vision",
    "Out Of Commission/Tranmission Terminated": (
        "Out Of Commission & Transmission Terminated"
    ),
    "Owo-1 w/ backup": "OWO-1 With Backup",
    "Ssa-1015": "SSA-1015",
    "3b3-888": "3B3-888",
    "Twi'lek Adivsor": "Twi'lek Advisor",
    "Twi-lek Advisor": "Twi'lek Advisor",
    "Mott (V)": "Admiral Motti (V)",
    "Mott (v)": "Admiral Motti (V)",
    "Mott": "Admiral Motti",
    "Ten Nunb": "Ten Numb",
    "Slight Weapon Malfunction": "Slight Weapons Malfunction",
    "Heavy Turbolaster Battery": "Heavy Turbolaser Battery",
    "IAO&SP": "Imperial Arrest Order & Secret Plans",
    "IAO&SP;": "Imperial Arrest Order & Secret Plans",
    "Mobilization Points combo": "You Cannot Hide Forever & Mobilization Points",
    "D*2: DB": "Death Star II: Docking Bay",
    "D*2:DB": "Death Star II: Docking Bay",
    "Imperial Square": "Coruscant: Imperial Square",
    "Imperial City": "Coruscant: Imperial City",
    "Blockade Flagship: DB": "Blockade Flagship: Docking Bay",
    "Blockade Flagship:DB": "Blockade Flagship: Docking Bay",
    "Yavin: DB": "Yavin 4: Docking Bay",
    "Tattooine: Mos Espa Docking Bay": "Tatooine: Mos Espa Docking Bay",
    "Lando w/Vibro Ax": "Lando With Vibro-Ax",
    "Wedge Antillies, RSL": "Wedge Antilles, Red Squadron Leader",
    "Kier Santage": "Keir Santage",
    "Advanced Preperation (V)": "Advance Preparation (V)",
    "Advanced Preparation (V)": "Advance Preparation (V)",
    "All Wings Report In combo": "All Wings Report In & Darklighter Spin",
    "Briefing Room": "Yavin 4: Briefing Room",
    "Massassi Headquarters": "Yavin 4: Massassi Headquarters",
    "R2 in Red 5": "Artoo-Detoo In Red 5",
    "Inconsiquential Losses": "Inconsequential Losses",
    "Pit of Carcoon": "Tatooine: Great Pit Of Carkoon",
    "Dungean": "Jabba's Palace: Dungeon",
    "Imp Blaster": "Imperial Blaster",
    "Antipersonel Laser": "Antipersonnel Laser Cannon",
    "Anti-Personnel Laser Cannon": "Antipersonnel Laser Cannon",
    "Blaster Rifel": "Blaster Rifle",
    "MJ's Lightsaber": "Mara Jade's Lightsaber",
    "Assault Rifel": "Assault Rifle",
    "Mandolarian Armor": "Mandalorian Armor",
    "Maldalorian Armor": "Mandalorian Armor",
    "Jodo Cast": "Jodo Kast",
    "Dr Evazen & Ponda Baba": "Dr. Evazan & Ponda Baba",
    "Dr. Evansen & Ponda Baba": "Dr. Evazan & Ponda Baba",
    "Bosk w/ gun": "Bossk With Mortar Gun",
    "Carbon Chamber Testing/My Favorite Decoration": "Carbon Chamber Testing",
    "Malastaire": "Malastare",
    "Sense and Uncertain is the Future": "Sense & Uncertain Is The Future",
    "Sense and Uncertain Is The Future": "Sense & Uncertain Is The Future",
    "We're In Attack Position Now!": "We're In Attack Position Now",
    "Gammorean Guards": "Gamorrean Guard",
    "Mi'iyoom Onith": "M'iiyoom Onith",
    "DLOFTS": "Darth Vader, Dark Lord Of The Sith",
    "Darth Vader, DLOFTS": "Darth Vader, Dark Lord Of The Sith",
    "Den of Theives": "Den Of Thieves",
    "Fel": "Baron Soontir Fel",
    "Phennir": "Major Turr Phennir",
    "Commander Merrjyk": "Commander Merrejk",
    "Niemiodian Advisor": "Neimoidian Advisor",
    "Imp-Class SD": "Imperial-Class Star Destroyer",
    "General Reeikan (V)": "General Carlist Rieekan",
    "General Reeikan": "General Carlist Rieekan",
    "Tigrin Jamiro (V)": "Tigran Jamiro",
    "Artoo Detoo In Red 5": "Artoo-Detoo In Red 5",
    "Court object": "Court Of The Vile Gangster",
    "Lye-Me": "Lyn Me",
    "Jabba's Barge": "Jabba's Sail Barge",
    "Denfensive fire & Hutt Smooch": "Defensive Fire & Hutt Smooch",
    "LUKE SKYWALKER": "Luke Skywalker",
    "LUKE SKYWALKER (non-virtual)": "Luke Skywalker",
    "NAR SHADDA CHIMES & OUT OF SOMEWHERE": "Nar Shaddaa Wind Chimes & Out Of Somewhere",
    "Trooper Utris M'tok": "Trooper Utris M'Toc",
    "Trooper Utris Mtok": "Trooper Utris M'Toc",
    "Temmto Pagalies' Podracer": "Teemto Pagalies' Podracer",
    "Scum And Villaniy": "Scum And Villainy",
    "Hyperwave Scan (V)": "Hyperwave Scan",
    "4lom w/gun": "4-LOM With Concussion Rifle",
    "Space Port DB": "Spaceport Docking Bay",
    "Tatoine DB": "Tatooine: Docking Bay 94",
    "CC DB": "Cloud City: East Platform (Docking Bay)",
    "Jabba's sail Barge Bassanger Deck": "Jabba's Sail Barge: Passenger Deck",
    "Jabba's Sale barge": "Jabba's Sail Barge",
    "Carbon Chamber Testing/MFD": "Carbon Chamber Testing",
    "Skum and Villany": "Scum And Villainy",
    "Boba Fett w/ Blaster": "Boba Fett With Blaster Rifle",
    "Jabba's Space Crusier": "Jabba's Space Cruiser",
    "Jabbas space cruiser": "Jabba's Space Cruiser",
    "Darth Sidous": "Darth Sidious",
    "Darht Vader's Saber": "Darth Vader's Lightsaber",
    "Cloud City: Carbon Chamber": "Cloud City: Carbonite Chamber",
    "Cloud City Carbon Chamber": "Cloud City: Carbonite Chamber",
    "Cloud City Dinig Room": "Cloud City: Dining Room",
    "Cloud City Downtown Plaza": "Cloud City: Downtown Plaza",
    "Cloud City East Platform": "Cloud City: East Platform (Docking Bay)",
    "Cloud City Casino": "Cloud City: Casino",
    "Why Didn't You Tell Me": "Why Didn't You Tell Me?",
    "Imp-Class SD (V)": "Imperial-Class Star Destroyer (V)",
    "Death Star: DB": "Death Star: Docking Bay 327",
    "Endor: Landing platform (DB)": "Endor: Landing Platform (Docking Bay)",
    "Endor: Landing platform": "Endor: Landing Platform (Docking Bay)",
    "Endor:Landing Platform(db)": "Endor: Landing Platform (Docking Bay)",
    "Endor: Landing Platform (db)": "Endor: Landing Platform (Docking Bay)",
    "Endor: Rebal landing site (forest)": "Endor: Rebel Landing Site (Forest)",
    "Endor: Rebal landing site": "Endor: Rebel Landing Site (Forest)",
    "Independaence": "Independence",
    "Yub tub!": "Yub Yub!",
    "the Traitor of Jawa Canyon": "Iasa, The Traitor Of Jawa Canyon",
    "Iasa, the Traitor of Jawa Canyon": "Iasa, The Traitor Of Jawa Canyon",
    "Uttini! (V)": "Utinni!",
    "Abyssin Ormanent": "Abyssin Ornament",
    "Abyssian Ornament": "Abyssin Ornament",
    "MKOS/FAI": "My Kind Of Scum",
    "Tatooine: Jundland Waste": "Tatooine: Jundland Wastes",
    "Nemodien Advisor": "Neimoidian Advisor",
    "Armored Assault Tank": "Armored Attack Tank",
    "ISB Operations/ Empire's Sinister Agents": "ISB Operations",
    "SFS Lr-s9.3 Laser Cannons": "SFS L-s9.3 Laser Cannons",
    "SFS 9.3 TIE cannons": "SFS L-s9.3 Laser Cannons",
    "Commander Wedge Antillies": "Commander Wedge Antilles",
    "Ob-Wan Kenobi, Padawan Learner": "Obi-Wan Kenobi, Padawan Learner",
    "Lando Calrssian": "Lando Calrissian",
    "Secret Plans & Imperial Arrest Order": "Imperial Arrest Order & Secret Plans",
    "We're the Bait": "We're The Bait",
    "Aiiii! Aaa! Aggggggggg!": "Aiiii! Aaa! Agggggggggg!",
    "EV-909": "EV-9D9",
    "Dengar w/ Blaster": "Dengar With Blaster Carbine",
    "OS-71-1 In Obsidian 1": "OS-72-1 In Obsidian 1",
    "Endor Operations/no flip": "Endor Operations",
    "Operation As Planned": "Operational As Planned",
    "Moff Jerjerroed": "Moff Jerjerrod",
    "DSII: Coolant Shaft": "Death Star II: Coolant Shaft",
    "DSII:Capacitors": "Death Star II: Capacitors",
    "DSII: Capacitors": "Death Star II: Capacitors",
    "DSII:Reactor Core": "Death Star II: Reactor Core",
    "DSII: Reactor Core": "Death Star II: Reactor Core",
    "Rendezevous Point": "Rendezvous Point",
    "Bothauwi": "Bothawui",
    "Derek Hobbie Kilvian": "Derek 'Hobbie' Klivian",
    "Qui-Gonn's Lightsaber": "Qui-Gon Jinn's Lightsaber",
    "Heavy Turbolasers": "Heavy Turbolaser Battery",
    "B-Wing Attack Fighters": "B-wing Attack Fighter",
    "Control/Tunnel Vison": "Control & Tunnel Vision",
    "Sprial": "Spiral",
    "Elephant Mon": "Ephant Mon",
    "4-Lom with rifle": "4-LOM With Concussion Rifle",
    "Heading for the MF": "Heading For The Medical Frigate",
    "Head for the Medical Frigate": "Heading For The Medical Frigate",
    "superfical damage": "Superficial Damage",
    "an usual amount of fear": "An Unusual Amount Of Fear",
    "An Usual Amount of Fear": "An Unusual Amount Of Fear",
    "Unusual Amout of Fear": "An Unusual Amount Of Fear",
    "great forest": "Endor: Great Forest",
    "Great Forest": "Endor: Great Forest",
    "anicent forest": "Endor: Ancient Forest",
    "chewie of kash": "Chewbacca Of Kashyyyk",
    "Chewbacca of Kaysssk": "Chewbacca Of Kashyyyk",
    "beezer": "Corporal Beezer",
    "midge": "Corporal Midge",
    "kensari": "Corporal Kensaric",
    "yutani": "Captain Yutani With Blaster Cannon",
    "dresselian scout": "Dresselian Commando",
    "blastec-E blaster rifle": "BlasTech E-11B Blaster Rifle",
    "mercinary armor": "Mercenary Armor",
    "ewok capapult": "Ewok Catapult",
    "rebel artillry": "Rebel Artillery",
    "suprise counter assualt": "Surprise Counter Assault",
    "Na Shardda Wind Chimes": "Nar Shaddaa Wind Chimes",
    "Nar Shadda Wind Chimes": "Nar Shaddaa Wind Chimes",
    "endor DB": "Endor: Landing Platform (Docking Bay)",
    "Crush": "Crush The Rebellion",
    "Sniper combo": "Sniper & Dark Strike",
    "Cloud City: DB": "Cloud City: Platform 327 (Docking Bay)",
    "Dengar w/bc": "Dengar With Blaster Carbine",
    "IG-88 w/rg": "IG-88 With Riot Gun",
    "4-lom w/cr": "4-LOM With Concussion Rifle",
    "4-LOM w/cr": "4-LOM With Concussion Rifle",
    "Bossk w/mg": "Bossk With Mortar Gun",
    "Dr Evazan & Ponda Boba": "Dr. Evazan & Ponda Baba",
    "Gamorrean Gaurd": "Gamorrean Guard",
    "Gommorrean Guard": "Gamorrean Guard",
    "Umpass Stay": "Umpass-stay",
    "Owo-1 w/bu": "OWO-1 With Backup",
    "OWO-1 w/bu": "OWO-1 With Backup",
    "Boba Fett's BR": "Boba Fett With Blaster Rifle",
    "Naboo BR": "Naboo Blaster Rifle",
    "Sai-Torr Kal Fass (V)": "Sai'torr Kal Fas (V)",
    "Obi Wan JK": "Obi-Wan Kenobi, Jedi Knight",
    "Qui Gon w/ls": "Qui-Gon Jinn With Lightsaber",
    "Qui Gon w/saber": "Qui-Gon Jinn With Lightsaber",
    "Braniac": "Brainiac",
    "Lando Calrissian, Scoundral": "Lando Calrissian, Scoundrel",
    "Scoundral": "Lando Calrissian, Scoundrel",
    "Chewi Enraged": "Chewie, Enraged",
    "Han's Heavy Blaster Rifle": "Han's Heavy Blaster Pistol",
    "Totooine: Mos Eisley": "Tatooine: Mos Eisley",
    "Out of Commissoin & Transmission terminated": (
        "Out Of Commission & Transmission Terminated"
    ),
    "Alter & Unfriendly Fire": "Unfriendly Fire",
    "End of Reign": "End Of A Reign",
    "I don't need ther scum, Either": "I Don't Need Their Scum, Either",
    "I don't need ther scum": "I Don't Need Their Scum, Either",
    "Tosche Station": "Tatooine: Tosche Station",
    "Obi-Wan Kenobi: Padawan Learner": "Obi-Wan Kenobi, Padawan Learner",
    "Daugther of Skywalker": "Daughter Of Skywalker",
    "Kal-Falnl C'ndros": "Kal'Falnl C'ndros",
    "Qui-Gonn Jinn's Lightsaber": "Qui-Gon Jinn's Lightsaber",
    "Heavy Turbolaser": "Heavy Turbolaser Battery",
    "Imperial Artillary": "Imperial Artillery",
    "Echo: DB": "Hoth: Echo Docking Bay",
    "Rendevous Poin": "Rendezvous Point",
    "Das Rendar": "Dash Rendar",
    "Leebo": "LE-BO2D9 (Leebo)",
    "Chewi w/br": "Chewie With Blaster Rifle",
    "Obi-Wan w/saber": "Obi-Wan Kenobi With Lightsaber",
    "Leia w/br": "Leia With Blaster Rifle",
    "Mara saber": "Mara Jade's Lightsaber",
    "Mandolorian armor": "Mandalorian Armor",
    "Blaster Proficiancy": "Blaster Proficiency",
    "Ralitir Freighter Captain": "Ralltiir Freighter Captain",
    "Obiwan's Cape": "Obi-Wan's Cape",
    "yt1300": "YT-1300 Transport",
    "z95": "Z-95 Headhunter",
    "Only Politics": "No Civility, Only Politics",
    "No Civility, Only Politics": "No Civility, Only Politics",
    "Inconsequetial Losses": "Inconsequential Losses",
    "Imperial Class SD": "Imperial-Class Star Destroyer",
    "Victory SD": "Victory-Class Star Destroyer",
    "Twi-lek Adviser": "Twi'lek Advisor",
    "Tatioone": "Tatooine",
    "Tatioone: Desert": "Tatooine: Desert",
    "Gammorean Guard": "Gamorrean Guard",
    "Gammorean Axe": "Gamorrean Ax",
    "Scum and Villiany": "Scum And Villainy",
    "WMAOP": "We Must Accelerate Our Plans",
    "Evader combo": "Evader & Monnok",
    "Holotable": "Imperial Holotable",
    "SFS L-s7.2 TIE Cannons": "SFS L-s7.2 TIE Cannon",
    "boba w/ gun": "Boba Fett With Blaster Rifle",
    "captain gillad palaeon": "Captain Gilad Pellaeon",
    "Zuckuss's gun": "Zuckuss' Snare Rifle",
    "Ig88 in ship": "IG-88 In IG-2000",
    "Blockade flagship DB": "Blockade Flagship: Docking Bay",
    "Coruscant DB": "Coruscant: Docking Bay",
    "Executer DB": "Executor: Docking Bay",
    "Jabba's sail Barge Passanger Deck": "Jabba's Sail Barge: Passenger Deck",
    "Sunsdown & TCFS": "Sunsdown & Too Cold For Speeders",
    "Corporal Dreslonan": "Corporal Drazin",
    "Luetenant Arnet": "Lieutenant Arnet",
    "Luetenant Grond": "Lieutenant Grond",
    "Luetenant Renz": "Lieutenant Renz",
    "Seargant Barich": "Sergeant Barich",
    "Seargant Elsik": "Sergeant Elsek",
    "Go for Help": "Go For Help!",
    "Blaster Riffle": "Blaster Rifle",
    "Lamda Class Shuttle": "Lambda-Class Shuttle",
    "Graysquadron 2": "Gray Squadron 2",
    "Correllian Corvette": "Corellian Corvette",
    "Nebulon B Frigate": "Nebulon-B Frigate",
    "Officer Elberger": "Officer Ellberger",
    "Comm. Wedge Antilles": "Commander Wedge Antilles",
    "Kairie Neth": "Karie Neth",
    "Ex: Holotheatre": "Executor: Holotheatre",
    "Dag: Cave": "Dagobah: Cave",
    "Bith Shuffle / Desperate Reach": "The Bith Shuffle & Desperate Reach",
    "Lukes's Back": "Luke's Back",
    "Inserrection / Aim High": "Insurrection & Aim High",
    "Uncontrolable Fury": "Uncontrollable Fury",
    "Dejarik Hologramboard": "Dejarik Hologameboard",
    "Fear is my ally w/10 shields": "Fear Is My Ally",
    "Fear Is My Ally w/10 shields": "Fear Is My Ally",
    "Bring Them Before Me/Take Their Butts To A Kicking": "Bring Him Before Me",
    "DS II: Throne Room": "Death Star II: Throne Room",
    "DS II: Docking Bay": "Death Star II: Docking Bay",
    "IAO&SC": "Imperial Arrest Order & Secret Plans",
    "IAO&SC;": "Imperial Arrest Order & Secret Plans",
    "IAO & SC": "Imperial Arrest Order & Secret Plans",
    "Mob.points": "Mobilization Points",
    "Yavin 4 DB": "Yavin 4: Docking Bay",
    "Mara Jade's Lighsaber": "Mara Jade's Lightsaber",
    "Chiamera": "Chimaera",
    "Insurrection combo": "Insurrection & Aim High",
    "Gospic (V)": "Colonel Feyn Gospic",
    "Commander Vandan Willard (V)": "Commander Vanden Willard",
    "Suppresive Fire": "Suppressive Fire",
    "Med Lab": "Hoth: Echo Med Lab",
    "Forest": "Forest",
    "Tempest 1": "Tempest 1",
    "Niedo Duegad": "Niado Duegad",
    "Cloud city ; Security tower": "Cloud City: Security Tower",
    "tie Advanced": "TIE Advanced x1",
    "tie Advanced x1": "TIE Advanced x1",
    "Cloud City: East Platform DB": "Cloud City: East Platform (Docking Bay)",
    "ISB Ops": "ISB Operations",
    "Imperial Arrest": "Imperial Arrest Order",
    "The Emperors Sword": "The Emperor's Sword",
    "Zuckes in Mist Hunter": "Zuckuss In Mist Hunter",
    "MJTEH": "Mara Jade, The Emperor's Hand",
    "Mara TEH": "Mara Jade, The Emperor's Hand",
    "Mara Jade, TEH": "Mara Jade, The Emperor's Hand",
    "Corporal Vandoly": "Corporal Vandolay",
    "Boba Fett with Blaster Riffle": "Boba Fett With Blaster Rifle",
    "4-LOM with concussion riffle": "4-LOM With Concussion Rifle",
    "Zuckus": "Zuckuss",
    "Feltipern Travugg": "Feltipern Trevagg",
    "Darth Vader with Light saber": "Darth Vader With Lightsaber",
    "Darth Maul with Light saber": "Darth Maul With Lightsaber",
    "Rune Hako": "Rune Haako",
    "Miner Droid": "LIN-V8M (Elleyein-Veeateemm)",
    "Kryat Dragon Bones": "Krayt Dragon Bones",
    "Boskk's Mortar Gun": "Bossk With Mortar Gun",
    "Bossk w/Mortar Gun": "Bossk With Mortar Gun",
    "Bosk w/gun": "Bossk With Mortar Gun",
    "Feltipern's Stungun": "Feltipern Trevagg's Stun Rifle",
    "Any Methods Necesary": "Any Methods Necessary",
    "Alter/Collateral Damage": "Alter & Collateral Damage",
    "Oo-ta Goo-ta Solo (V)": "Oo-ta Goo-ta, Solo? (V)",
    "oota goota (V)": "Oo-ta Goo-ta, Solo? (V)",
    "oota goota": "Oo-ta Goo-ta, Solo?",
    "Coruscant: Docking Boy": "Coruscant: Docking Bay",
    "Rebel Artillary": "Rebel Artillery",
    "Agents of the Black Sun/Vengence of the Dark Prince": (
        "Agents Of Black Sun / Vengeance Of The Dark Prince"
    ),
    "Coruscant system": "Coruscant",
    "Boba Fett Cloud City": "Boba Fett (CS)",
    "BFBH": "Boba Fett, Bounty Hunter",
    "Boba Fett bh": "Boba Fett, Bounty Hunter",
    "Denagr in Punishing One": "Dengar In Punishing One",
    "Houjiix": "Houjix",
    "Romas ?Lock? Navander": "Romas \"Lock\" Navander",
    "Audience champer": "Jabba's Palace: Audience Chamber",
    "dungean": "Jabba's Palace: Dungeon",
    "sarlaac pit": "Tatooine: Great Pit Of Carkoon",
    "Ket Malis (V)": "Ket Maliss (V)",
    "EV9D9": "EV-9D9",
    "Scum": "Scum And Villainy",
    "Aii!! AHH!!!! Agggg!!": "Aiiii! Aaa! Agggggggggg!",
    "spc prt db": "Spaceport Docking Bay",
    "Cor db": "Coruscant: Docking Bay",
    "Exe db": "Executor: Docking Bay",
    "droid workshop": "Jabba's Palace: Droid Workshop",
    "Passenger deck": "Jabba's Sail Barge: Passenger Deck",
    "lower passages": "Jabba's Palace: Lower Passages",
    "Dengar's big gun": "Dengar's Modified Riot Gun",
    "Boba in ship": "Boba Fett In Slave I",
    "Boba Fett in Slave 1": "Boba Fett In Slave I",
    "Sail barge": "Jabba's Sail Barge",
    "Wach Your Step/This Place Is Always Rough": "Watch Your Step",
    "YISYW & SA": "Your Insight Serves You Well & Staging Areas",
    "An Unsuals Amunt Of Fear": "An Unusual Amount Of Fear",
    "Chebacca": "Chewbacca",
    "Lando w/Blaster Pistol": "Lando With Blaster Pistol",
    "Out Of Comission & Transmission Terminated": "Out Of Commission & Transmission Terminated",
    "Rebell Barrier": "Rebel Barrier",
    "Nar Shaddaa Wind Chimes & OOS": "Nar Shaddaa Wind Chimes & Out Of Somewhere",
    "Advance Prep (V)": "Advance Preparation (V)",
    "We Wish You To Board At Once": "We Wish To Board At Once",
    "The Deal is Getting Wose All the Time": "This Deal Is Getting Worse All The Time",
    "Cloud Cidy: Port Town District": "Cloud City: Port Town District",
    "Moblization Points": "Mobilization Points",
    "Cloud City: Carbonate Chamber": "Cloud City: Carbonite Chamber",
    "Cloud City: Secuity Tower": "Cloud City: Security Tower",
    "4lom w/gun": "4-LOM With Concussion Rifle",
    "dengar w/gun": "Dengar With Blaster Carbine",
    "Ig88": "IG-88",
    "Ig88 in ship": "IG-88 In IG-2000",
    "Mara's stick": "Mara Jade's Lightsaber",
    "Mandolarian armor": "Mandalorian Armor",
    "Sarlaac": "Sarlacc",
    "Space port Docking Bay": "Spaceport Docking Bay",
    "Coruscant: Imperial city": "Coruscant: Imperial City",
    "Precision targeting": "Precision Targeting",
    "Elis Herlot": "Elis Helrot",
    "Projection of a skywalker (to a site)": "Projection Of A Skywalker",
    "Ralitir Freighter Captn": "Ralltiir Freighter Captain",
    "Cptn Han": "Captain Han Solo",
    "Milenium Falcon": "Millennium Falcon",
    "Millennnium Falcon": "Millennium Falcon",
    "Staging Areas & Your Insight Serves You Well": (
        "Your Insight Serves You Well & Staging Areas"
    ),
    "I Hope She's Alright": "I Hope She's All Right",
    "Set Your Course For Bespin/Cloud City Will Slip Through Your Fingers": (
        "Hidden Base"
    ),
    "Hidden base/ The more systems...": "Hidden Base",
    "Hidden base/ The more systems": "Hidden Base",
    "Dantoine/ flipped": "Dantooine",
    "Dantoine": "Dantooine",
    "Red 1 w/ Red Leader": "Red Leader In Red 1",
    "Quad laser cannons": "Quad Laser Cannon",
    "Targeting computer": "Targeting Computer",
    "Stay Sharp": "Stay Sharp!",
    "Biggs (V)": "Biggs Darklighter",
    "Artoo (V)": "R2-D2 (Artoo-Detoo) (V)",
    "CC Boba Fett": "Boba Fett (CS)",
    "Feltprin Trevagg": "Feltipern Trevagg",
    "IG-88 with Rion Gun": "IG-88 With Riot Gun",
    "Oota Goota Solo (V)": "Oo-ta Goo-ta, Solo? (V)",
    "Oota Goota Solo (v)": "Oo-ta Goo-ta, Solo? (V)",
    "We Must Accerate Our Plans": "We Must Accelerate Our Plans",
    "Feltipren Trevagg's Stun Rifle": "Feltipern Trevagg's Stun Rifle",
    "SYCFA/TUPINT": "Set Your Course For Alderaan",
    "Ghhk": "Ghhhk",
    "Dr. Evazan & Walrus Man": "Dr. Evazan & Ponda Baba",
    "Mara Jade's LS": "Mara Jade's Lightsaber",
    "Mara Jade’s LS": "Mara Jade's Lightsaber",
    "Maul's Double LS": "Maul's Double-Bladed Lightsaber",
    "Maul’s Double LS": "Maul's Double-Bladed Lightsaber",
    "Security Precations": "Security Precautions",
    "Imperial Helmsmen": "Imperial Helmsman",
    "Sergant Barich": "Sergeant Barich",
    "Sargent Elesk": "Sergeant Elsek",
    "BobaFett in slave 1": "Boba Fett In Slave I",
    "tie intercepters": "TIE Interceptor",
    "Mual Strikes": "Maul Strikes",
    "Heavy frie zone": "Heavy Fire Zone",
    "Flawless Marksmenship": "Flawless Marksmanship",
    "Relentless Pursuits": "Relentless Pursuit",
    "seeder bikes": "Speeder Bike",
    "endor forest clearing": "Endor: Forest Clearing",
    "sheild genreators": "Deflector Shield Generators",
    "They Must Never Again Leave the City": "They Must Never Again Leave This City",
    "You Can Either Profit By This…/ Or Be Destroyed": "You Can Either Profit By This...",
    "Han With Blaster Pistol": "Han With Heavy Blaster Pistol",
    "Insurection & Aim High": "Insurrection & Aim High",
    "Lando Salrissian, Scoundrel": "Lando Calrissian, Scoundrel",
    "Padm'e Naberrie": "Padme Naberrie",
    "Aremote Planet": "A Remote Planet",
    "Tatoine Celebration": "Tatooine Celebration",
    "Land With Vibro-Ax": "Lando With Vibro-Ax",
    "Red Squaron Leader": "Wedge Antilles, Red Squadron Leader",
    "Lighsaber Proficiency": "Lightsaber Proficiency",
    "Dagobah System": "Dagobah",
    "Dagobah Training Area": "Dagobah: Training Area",
    "Tatooine Mos Espa: Docking Bay": "Tatooine: Mos Espa Docking Bay",
    "BlasTech E-118 Blaster Rifle": "BlasTech E-11B Blaster Rifle",
    "Merciniery Armor": "Mercenary Armor",
    "Test 1": "Great Warrior",
    "Test 2": "A Jedi's Strength",
    "Test 3": "It Is The Future You See",
    "Test 4": "Domain Of Evil",
    "Test 5": "Size Matters Not",
    "Honor of a Jedi": "Honor Of The Jedi",
    "Sai'toor Kal Fas (V)": "Sai'torr Kal Fas (V)",
    "Boba Fett w/blaster": "Boba Fett With Blaster Rifle",
    "Dengar w/carbine": "Dengar With Blaster Carbine",
    "Bossk w/mortar": "Bossk With Mortar Gun",
    "Wittin!!!": "Wittin",
    "R1-G6": "R1-G4 (Arone-Geefour)",
    "Jade's Saber": "Mara Jade's Lightsaber",
    "ion cannons": "Ion Cannon",
    "heavy turo laserbattery": "Heavy Turbolaser Battery",
    "dark jedi light saber": "Dark Jedi Lightsaber",
    "Wedge Antilles, Red Squaron Leader": "Wedge Antilles, Red Squadron Leader",
    "Obi-Wan Kenobi, Padawan Larner": "Obi-Wan Kenobi, Padawan Learner",
    # Page 27 slang (last-wins).
    "Utinni (V)": "Utinni!",
    "Utinni! (V)": "Utinni!",
    "Secret Plan": "Secret Plans",
    "Sergant Elsek": "Sergeant Elsek",
    "Endor Dense Forest": "Endor: Dense Forest",
    "What Are You Trying to Push On Us": "What're You Tryin' To Push On Us?",
    "What Are You Trying To Push On Us": "What're You Tryin' To Push On Us?",
    "COTG/ISEWYD": "Court Of The Vile Gangster",
    "Jabba's Palace: Great Pit Of Carkoon": "Tatooine: Great Pit Of Carkoon",
    "Sense/Uncertain In The Future": "Sense & Uncertain Is The Future",
    "Captian Piett": "Captain Piett",
    "Death Star Gunners": "Death Star Gunner",
    "Imperial Class Star Destroyers (V)": "Imperial-Class Star Destroyer (V)",
    "Imperial Class Star Destroyer (V)": "Imperial-Class Star Destroyer (V)",
    "Imperial Class SD (V)": "Imperial-Class Star Destroyer (V)",
    "Agents In The Court / No Love For The Empire": "Agents In The Court",
    "Agents In The Court/No Love For The Empire(Aved Luun)": "Agents In The Court",
    "Agents In The Court/No Love For The Empire (Aved Luun)": "Agents In The Court",
    "Tatoonie: Lar's Moisture Farm": "Tatooine: Lars' Moisture Farm",
    "Tatooine: Lar's Moisture Farm": "Tatooine: Lars' Moisture Farm",
    "Owen Lars/Beru Lars": "Owen Lars & Beru Lars",
    "Jabba's Palace: Dundeon": "Jabba's Palace: Dungeon",
    "Jabba's Palace Rancor Pit": "Jabba's Palace: Rancor Pit",
    "Judo Kast": "Jodo Kast",
    "IG-88 With Riot Run": "IG-88 With Riot Gun",
    "Hut Smooch": "Hutt Smooch",
    "Deal's Worse/Alter Further": "This Deal Is Getting Worse All The Time",
    "Let Them Make The First Move/At Last We Will Hve Revenge": "Let Them Make The First Move",
    "Coran Horn": "Corran Horn",
    "NMNPND/": "No Money, No Parts, No Deal!",
    "NMNPND": "No Money, No Parts, No Deal!",
    "wipe them out, all out them": "Wipe Them Out, All Of Them",
    "you cannot hide forever & mob. points": "You Cannot Hide Forever & Mobilization Points",
    "vadre'S lightsaber": "Vader's Lightsaber",
    "vadre's lightsaber": "Vader's Lightsaber",
    "ghhhk & those rebels won't": "Ghhhk & Those Rebels Won't Escape Us",
    "ghhhk & those rebels won’t": "Ghhhk & Those Rebels Won't Escape Us",
    "MWYHL / SYIC": "Mind What You Have Learned",
    "your insight serves you well & staging area": (
        "Your Insight Serves You Well & Staging Areas"
    ),
    "an unusual amout of fear": "An Unusual Amount Of Fear",
    "EPP han": "Han With Heavy Blaster Pistol",
    "EPP leia": "Leia With Blaster Rifle",
    "EPP obi": "Obi-Wan With Lightsaber",
    "threepio with is part showing": "Threepio With His Parts Showing",
    "like's backpack": "Luke's Backpack",
    "life dept": "Life Debt",
    "Jedi Test #1": "Great Warrior",
    "Jedi Test #2": "A Jedi's Strength",
    "Jedi Test #3": "It Is The Future You See",
    "Jedi Test #4": "Domain Of Evil",
    "Jedi Test #5": "Size Matters Not",
    "Jedi Test #6": "You Must Confront Vader",
    "My Lord, Is That Legal/I Will make It Legal": "My Lord, Is That Legal?",
    "My Lord, Is That Legal/I Will Make It Legal": "My Lord, Is That Legal?",
    "Galatic Senate": "Coruscant: Galactic Senate",
    "I Will Find Them Qucikly, Master": "I Will Find Them Quickly, Master",
    "I Will Find Them Qucikly": "I Will Find Them Quickly, Master",
    "Oota Goo-ta": "Oo-ta Goo-ta, Solo?",
    "The Phamtom Menace": "The Phantom Menace",
    "Toonbuck Tora": "Toonbuck Toora",
    "Desvastor": "Devastator",
    "Squabbling Delagates": "Squabbling Delegates",
    "ISB Operations/ESA": "ISB Operations",
    "Imperial Arrest Order & SP": "Imperial Arrest Order & Secret Plans",
    "Hoth: DB": "Hoth: Echo Docking Bay",
    "Executor DB": "Executor: Docking Bay",
    "Darth Vader w/Lightasaber": "Darth Vader With Lightsaber",
    "Captian Gilad Pellaeon": "Captain Gilad Pellaeon",
    "Dodo Bodonawieddo": "Dodo Bodonawieedo",
    "Imp Barriers": "Imperial Barrier",
    "Oota Goo-ta, Solo?": "Oo-ta Goo-ta, Solo?",
    "Oota Goo-ta, Solo? (V)": "Oo-ta Goo-ta, Solo? (V)",
    "Res Luk Ra'auf?": "Res Luk Ra'auf",
    "AOBS/ Vengeance of the Dark Prince": "Agents Of Black Sun",
    "AOBS/ Vengeance Of The Dark Prince": "Agents Of Black Sun",
    "Agents Of Black Sun/Vengeance Of The Dark Prince": "Agents Of Black Sun",
    "4-LOM with Rifle": "4-LOM With Concussion Rifle",
    "Bring Him Before Me / Take Your Father Place": "Bring Him Before Me",
    "Bring Him Before Me / Take Your Father's Place": "Bring Him Before Me",
    "Take Your Father Place": "Take Your Father's Place",
    "Krayt Dragon Bones (V)": "Krayt Dragon Bones",
    "Informat (V)": "Informant",
    "Informat": "Informant",
    "alter  & collateral damage": "Alter & Collateral Damage",
    "alter & collateral damage": "Alter & Collateral Damage",
    "padmé naberrie": "Padme Naberrie",
    "Qui-Gon Jinn With Lightsaber": "Qui-Gon Jinn With Lightsaber",
    "Maul's Double Bladed Lightsaber": "Maul's Double-Bladed Lightsaber",
    "There is No Try/ Oppressive Enforcement": "There Is No Try & Oppressive Enforcement",
    "There Is No Try/ Oppressive Enforcement": "There Is No Try & Oppressive Enforcement",
    "Spaceport: Docking Bay": "Spaceport Docking Bay",
    "Ig-88 in Ig-2000": "IG-88 In IG-2000",
    "Ig-88 w/ Riot Gun": "IG-88 With Riot Gun",
    "Dengar w/ Blaster Carbine": "Dengar With Blaster Carbine",
    "4-LOM w/ Concussion Rifle": "4-LOM With Concussion Rifle",
    "IG-88 w/ Riot Gun": "IG-88 With Riot Gun",
    "Bossk w/ Mortar Gun": "Bossk With Mortar Gun",
    "Omni Box & its worse": "Ommni Box & It's Worse",
    "Workling": "Wokling",
    "Docking And Repai Facilities": "Docking And Repair Facilities",
    "Imperial Occuation/Imperial Control (V)": "Imperial Occupation",
    "Baron Sonntir Fel": "Baron Soontir Fel",
    "Baron Soonir Fel": "Baron Soontir Fel",
    "Imperial Barriers": "Imperial Barrier",
    "Pointman": "Point Man",
    "Themal Detonator": "Thermal Detonator",
    "The Hyperdrive Generator's Gone/We'll Need A New One": (
        "The Hyperdrive Generator's Gone"
    ),
    "Tat: Mos Espa Docking Bay": "Tatooine: Mos Espa Docking Bay",
    "Brave Little Droid": "Artoo, Brave Little Droid",
    "Captain Pelleaon": "Captain Gilad Pellaeon",
    "We're All Going To Be A Lot Thinner (V)": (
        "We're All Gonna Be A Lot Thinner! (V)"
    ),
    "Tatooine: Audience Chamber (Han Solo)": "Tatooine: Audience Chamber",
    "Artoo (1 or 6)": "Artoo",
    "Court of the Vile Ganster": "Court Of The Vile Gangster",
    "Jabba's Palace: Dugeon": "Jabba's Palace: Dungeon",
    "Tatoonine": "Tatooine",
    "I Will Find Them Quickly Master": "I Will Find Them Quickly, Master",
    "Sence & Uncertain Is the Future": "Sense & Uncertain Is The Future",
    "Flagship Opperations": "Flagship Operations",
    "Endor: Chief Chirp's Hut": "Endor: Chief Chirpa's Hut",
    "An Unsual Amount of Fear": "An Unusual Amount Of Fear",
    "An Unusual Ammount Of Fear": "An Unusual Amount Of Fear",
    "Sorry About The Mess & Blaster Proficency": (
        "Sorry About The Mess & Blaster Proficiency"
    ),
    "Sence & Recoil In Fear": "Sense & Recoil In Fear",
    "Millinium Falcon": "Millennium Falcon",
    "R2-D2 In Red 5": "Artoo-Detoo In Red 5",
    "Leia with Blaster Riffle": "Leia With Blaster Rifle",
    "Han with Heavy Blaster": "Han With Heavy Blaster Pistol",
    "Lightsaber Profiency": "Lightsaber Proficiency",
    "Quigon with Lightsaber": "Qui-Gon Jinn With Lightsaber",
    "Quigon With Lightsaber": "Qui-Gon Jinn With Lightsaber",
    "Insurection": "Insurrection",
    "Oppressive Enforcements": "Oppressive Enforcement",
    "Sienar Fleet System": "Sienar Fleet Systems",
    "Daughter Of Skywalker (train her)": "Daughter Of Skywalker",
    "Figrin Dan": "Figrin D'an",
    "Chewie w/ Blaster": "Chewie With Blaster Rifle",
    "Han w/ Heavy Blaster Rifle": "Han With Heavy Blaster Pistol",
    "Corporal Vandoloy": "Corporal Vandolay",
    "Probe Droid Laser Cannon": "Probe Droid Laser",
    "Probe Telemetry (V)": "Probe Telemetry",
    "Raltir": "Ralltiir",
    "TIE Assult Squardon": "TIE Assault Squadron",
    "Battle Plan & Draw There Fire": "Battle Plan & Draw Their Fire",
    "A Jedi's Resilence": "A Jedi's Resilience",
    "MWYHL": "Mind What You Have Learned",
    "Join Me": "Join Me!",
    "If the Trace Was Correct": "If The Trace Was Correct",
    "Obi-wan With Lightsaber": "Obi-Wan With Lightsaber",
    # Page 25 slang (last-wins).
    "Heading for the Med. Frigate": "Heading For The Medical Frigate",
    "Yavin4": "Yavin 4",
    "Bigg Darklighter (V)": "Biggs Darklighter",
    "Fusion Gen. Supply Tanks (V)": "Fusion Generator Supply Tanks (V)",
    "Incosequential Losses": "Inconsequential Losses",
    "Cloudcity: Guest Quarters": "Cloud City: Guest Quarters",
    "Cloudcity: Lower Corridor": "Cloud City: Lower Corridor",
    "Cloudcity: Platform 327": "Cloud City: Platform 327 (Docking Bay)",
    "Cloudcity: Carbonite Chamber": "Cloud City: Carbonite Chamber",
    "Cloudcity: West Gallery": "Cloud City: West Gallery",
    "Cloudcity: Down Town Plaza": "Cloud City: Downtown Plaza",
    "Cloudcity: North Corridor": "Cloud City: North Corridor",
    "Cloudcity Celebration": "Cloud City Celebration",
    "Cloudcity: West Platform": "Cloud City: East Platform (Docking Bay)",
    "Chewcacca With Blaster Riffle": "Chewie With Blaster Rifle",
    "Lando With Blaster Riffle": "Lando With Blaster Rifle",
    "Dengar w/ Gun": "Dengar With Blaster Carbine",
    "Darth Vader w/ saber": "Darth Vader With Lightsaber",
    "Darth Vader w/ Saber": "Darth Vader With Lightsaber",
    "Sand Whirl": "Sandwhirl",
    "Abbyssin Ornament & Wounded Wookie": "Abyssin Ornament & Wounded Wookiee",
    "Iggy in IG-2000": "IG-88 In IG-2000",
    "Dantooine Base Ops": "Dantooine Base Operations",
    "Scanner Techs (V)": "Scanner Techs",
    "What're You Trying to Push on Us?": "What're You Tryin' To Push On Us?",
    "Hot Jedi": "Honor Of The Jedi",
    "H,C & F": "Han, Chewie, And The Falcon",
    "H, C & F": "Han, Chewie, And The Falcon",
    "Qui w/Stick": "Qui-Gon Jinn With Lightsaber",
    "Owen & Beru": "Owen Lars & Beru Lars",
    "Houjix & OON": "Houjix & Out Of Nowhere",
    "A Jedi's Resiliance": "A Jedi's Resilience",
    "Yoda, MotF": "Yoda, Master Of The Force",
    "Insignificate Rebellion": "Insignificant Rebellion",
    "Begin Landing Our Troops": "Begin Landing Your Troops",
    "You Can Not Hide Forever & Mobilization Points": (
        "You Cannot Hide Forever & Mobilization Points"
    ),
    "Darth Maul's Doublebladed Lightsaber": "Maul's Double-Bladed Lightsaber",
    "Dengar In Punishing 1": "Dengar In Punishing One",
    "Alter & Collaterial Damage": "Alter & Collateral Damage",
    "Coursant: Docking Bay": "Coruscant: Docking Bay",
    "Something Special Planned": "Something Special Planned For Them",
    "Death Star: Detionblock Corridor": "Death Star: Detention Block Corridor",
    "Captain Gilad Pelleaon": "Captain Gilad Pellaeon",
    "Danroe": "Imperial Commander",
    "Superlazer": "Superlaser",
    "Heavy Turbo Lazer Battery": "Heavy Turbolaser Battery",
    "A Long Day Remembered": "A Day Long Remembered",
    "Ghhhk & Those Rebels Won't Excape Us": (
        "Ghhhk & Those Rebels Won't Escape Us"
    ),
    "the Emperors Shield": "The Emperor's Shield",
    "The Emperors Shield": "The Emperor's Shield",
    "Elite StormTrooper": "Elite Squadron Stormtrooper",
    "G M Tarkin": "Grand Moff Tarkin",
    "Ltnt. Grond": "Lieutenant Grond",
    "ltnt. Arnet": "Lieutenant Arnet",
    "Ltnt. Hebsly": "Lieutenant Hebsly",
    "OWO-1 w/backup": "OWO-1 With Backup",
    "Imp-class": "Imperial-Class Star Destroyer",
    "D Squad SD": "Death Squadron Star Destroyer",
    "RO/ITHOTE": "Ralltiir Operations",
    "Sudden Impact (V)": "Sudden Impact",
    "Nemoidian Pilot": "Neimoidian Pilot",
    "Lord Maul": "Darth Maul",
    "Hunt Down And Destroy The Jedi/They're Fired From The Universe": (
        "Hunt Down And Destroy The Jedi"
    ),
    "Ececutor: Meditation Chamber": "Executor: Meditation Chamber",
    "Res Luk Raauf": "Res Luk Ra'auf",
    "Scum And Villian": "Scum And Villainy",
    "Virgo": "Virago",
    "Sarlac": "Sarlacc",
    "Obi-Wan Kenobi, Padawan": "Obi-Wan Kenobi, Padawan Learner",
    "Han, Chewie And The Falcon": "Han, Chewie, And The Falcon",
    "DTF": "Draw Their Fire",
    "Ralltir": "Ralltiir",
    "Han w/ Blaster": "Han With Heavy Blaster Pistol",
    "Qui-Gonn W/ Saber": "Qui-Gon Jinn With Lightsaber",
    "Obi w/ Saber": "Obi-Wan With Lightsaber",
    "Lando , Scoundrel": "Lando Calrissian, Scoundrel",
    "Lando, Scoundrel": "Lando Calrissian, Scoundrel",
    "Han, Chewie, Falcon": "Han, Chewie, And The Falcon",
    "Hoth: Defensive Per": "Hoth: Defensive Perimeter (3rd Marker)",
    "The Snigal": "The Signal",
    "Gray Squadron One": "Gray Squadron 1",
    "The Hyperdrive Is Gone": "The Hyperdrive Generator's Gone",
    "An Unusal Amount Of Fear": "An Unusual Amount Of Fear",
    "Tatooine: Market Place": "Tatooine: Marketplace",
    "Tatooine: Toshce Station": "Tatooine: Tosche Station",
    "Corusant: Jedi Council Chamber": "Coruscant: Jedi Council Chamber",
    "Quigon Jinn": "Qui-Gon Jinn",
    "Obi-Wan Padawan": "Obi-Wan Kenobi, Padawan Learner",
    "Ki Adi Mundi": "Ki-Adi-Mundi",
    "Quigon's Lightsaber": "Qui-Gon Jinn's Lightsaber",
    "Amadala's Blaster": "Amidala's Blaster",
    "Desparate Tactics": "Desperate Tactics",
    "Golan Laser Batter": "Golan Laser Battery",
    "Profit or be destroyed": "You Can Either Profit By This...",
    "Tatooine: Jabba's pallace": "Tatooine: Jabba's Palace",
    "Jabba's Palace: Audeince chamber": "Jabba's Palace: Audience Chamber",
    "Pod arena": "Tatooine: Podrace Arena",
    "Annie's pod": "Anakin's Podracer",
    "Lando w/vibro-ax": "Lando With Vibro-Ax",
    "Klatooinian Rev": "Klatooinian Revolutionary",
    "Klatooinian Rev.": "Klatooinian Revolutionary",
    "Lt. s'Too Vees": "Lieutenant s'Too Vees",
    "Corp. Marmor": "Corporal Marmor",
    "Comm. Vanden Willard (V)": "Commander Vanden Willard (V)",
    "Gen. Solo": "General Solo",
    "Luke Skywalker, Reb Scout": "Luke Skywalker, Rebel Scout",
    "Luke w/saber": "Luke With Lightsaber",
    "Obi-wan w/saber": "Obi-Wan With Lightsaber",
    "Panaka, POTQ": "Panaka, Protector Of The Queen",
    "Maj. Panno": "Major Panno",
    "Maj. Olander Brit": "Major Olander Brit",
    "Q-Gon's Saber": "Qui-Gon Jinn's Lightsaber",
    "Luke's Saber": "Luke's Lightsaber",
    "Leia's sporting blaster": "Leia's Sporting Blaster",
    "Jedi Saber": "Jedi Lightsaber",
    "Some one who loves you": "Someone Who Loves You",
    "You insight serves you well": "Your Insight Serves You Well",
    "A tragity Has occurred": "A Tragedy Has Occurred",
    "Superficial dammage": "Superficial Damage",
    "I did It": "I Did It!",
    "The Hyperdrive Generator's Gone /WNANO": "The Hyperdrive Generator's Gone",
    "Tenau Bendon": "Tendau Bendon",
    "Obi-Wan, PL": "Obi-Wan Kenobi, Padawan Learner",
    "Figrin' D'an": "Figrin D'an",
    "Into The Garbage Chute Flyboy (V)": "Into The Garbage Chute, Flyboy",
    "TIE Interector": "TIE Interceptor",
    "Sythe 3": "Scythe 3",
    "SFS L-s7.2 TIECannon": "SFS L-s7.2 TIE Cannon",
    "ISB Ops./Empire's Sinister Agents": "ISB Operations",
    "Oppressive Eforcement": "Oppressive Enforcement",
    "Imp. Class Star Destroyer (V)": "Imperial-Class Star Destroyer (V)",
    "Fett in ship": "Boba Fett In Slave I",
    "Imp. Command": "Imperial Command",
    "Abyssin Ornament/ Wounded Wookie": "Abyssin Ornament & Wounded Wookiee",
    "Agents Of Black Sun/ Vengeance Of The Dark Prince": "Agents Of Black Sun",
    "All Wraped Up": "All Wrapped Up",
    "Mobilazation Points": "Mobilization Points",
    "Hoth MPG": "Hoth: Main Power Generators (1st Marker)",
    "EBG": "Echo Base Garrison",
    "M Flaps": "Maneuvering Flaps",
    "M Flaps (V)": "Maneuvering Flaps",
    "Aim High & Insurrection": "Insurrection & Aim High",
    "3nd marker": "Hoth: Defensive Perimeter (3rd Marker)",
    "Incom corp": "Incom Corporation",
    "Anger Fear Aggression": "Anger, Fear, Aggression",
    "Out of Commission combo": "Out Of Commission & Transmission Terminated",
    "Free Ride combo": "Free Ride & Endor Celebration",
    "Bossk (V)": "Bossk",
    "IG-88 (V)": "IG-88",
    "SE Jabba": "Jabba The Hutt",
    "Close Call (V)": "Close Call",
    "Defensive Fire (V)": "Defensive Fire",
    "Flagship (V)": "Flagship",
    "Jabba's Palace: Lower Passageways": "Jabba's Palace: Lower Passages",
    "A Jedi's Resilence": "A Jedi's Resilience",
    "Roar": "Wookiee Roar",
    "Tatooine: Roar": "Wookiee Roar",
    "Concusion Missiles": "Concussion Missiles",
    "You Can Either Profit By This…/Or Be Destroyed": "You Can Either Profit By This...",
    "Han w/ Heavy Blaster": "Han With Heavy Blaster Pistol",
    "Threepio w/ Parts Showing": "Threepio With His Parts Showing",
    "YISYW/Staging Areas": "Your Insight Serves You Well & Staging Areas",
    "Do, Or Do Not/Wise Advice": "Do, Or Do Not & Wise Advice",
    "Hoth: 1st Marker": "Hoth: Main Power Generators (1st Marker)",
    "Wedge Antilies, Red Squadron Leader": "Wedge Antilles, Red Squadron Leader",
    "X-Wing Squadron": "X-wing",
    "Incom Corperation": "Incom Corporation",
    "Yarna Dal Garnel": "Yarna d'al' Gargan",
    "Keffix": "Kiffex",
    "Tallon Rolls": "Tallon Roll",
    "Short Range Fighters/Watch Your Back!": "Short Range Fighters & Watch Your Back!",
    "Stormtroopers (V)": "Stormtrooper (V)",
    "Don't Get y": "Don't Get Cocky",
    "Naboo: Swamps": "Naboo: Swamp",
    "Nute Gunray, Nemoidian Viceroy": "Nute Gunray, Neimoidian Viceroy",
    "Nemoidian Viceroy": "Nute Gunray, Neimoidian Viceroy",
    "Tade Federation Battleship": "Trade Federation Battleship",
    "Hound's Tooth (V)": "Hound's Tooth",
    "Well Handle This / Duel of the Fates": "We'll Handle This",
    "Well Handle This / Duel Of The Fates": "We'll Handle This",
    "Qui Gon Jin Jedi Master": "Qui-Gon Jinn, Jedi Master",
    "Ki Adi Mudi": "Ki-Adi-Mundi",
    "Han Chewi and the Falcon": "Han, Chewie, And The Falcon",
    "Obi Wan's Lightsabre": "Obi-Wan's Lightsaber",
    "Qui Gon Jin's Lightsabre": "Qui-Gon Jinn's Lightsaber",
    "Depa Bilba": "Depa Billaba",
    "Sai'tor kal fas (V)": "Sai'torr Kal Fas (V)",
    "Dagobah: Yoda's Hutt": "Dagobah: Yoda's Hut",
    "Qui-Gonn Jinn with Lightsaber": "Qui-Gon Jinn With Lightsaber",
    "Son of Skywalker (V)": "Son of Skywalker",
    "Yoda (V)": "Yoda",
    "Electro-Binoculars": "Electrobinoculars",
    "Jedi Resilliance": "A Jedi's Resilience",
    "Manuevering Flaps (V)": "Maneuvering Flaps",
    "General Carlist Riekkan (V)": "General Carlist Rieekan",
    "Corporal Delvar": "Corporal Delevar",
    "Rouge 4": "Rogue 4",
    "Frosbite (V)": "Frostbite",
    "Fear is ms Ally": "Fear Is My Ally",
    "Admiral Chiranau": "Admiral Chiraneau",
    "Main Power Generator": "Hoth: Main Power Generators (1st Marker)",
    "Secret Plans combo": "Secret Plans",
    "Come With We (V)": "Come With Me",
    "Imperial-Class SD": "Imperial-Class Star Destroyer",
    "Zuckess in Ship": "Zuckuss In Mist Hunter",
    "AT-AT Cannons (V)": "AT-AT Cannon",
    "Obi-wan's Lightsabre": "Obi-Wan's Lightsaber",
    "Qui gon Jin's Lightsabre": "Qui-Gon Jinn's Lightsaber",
    "Luke's Lightsabre": "Luke's Lightsaber",
    "Cor: Galactic Senate": "Coruscant: Galactic Senate",
    "wampas": "Wampa",
    "Vader w/stick": "Darth Vader With Lightsaber",
    "Dr. E's Sawed-Off Blaster": "Dr. Evazan's Sawed-off Blaster",
    "Endor: Landing Plaform (Docking Bay)": "Endor: Landing Platform (Docking Bay)",
    "I Can Feel The Conflict": "I Feel The Conflict",
    "HDADTJ/TFHGOOTU": "Hunt Down And Destroy The Jedi",
    "LLL (V) or Blaster Rack (V)- if they play LSC": "Location, Location, Location",
    "LLL (V)or Blaster Rack (V)-Whichever you didn't start": "Blaster Rack (V)",
    "BFHI (V)": "Bad Feeling Have I",
    "Darth Sidius": "Darth Sidious",
    "Aurra Sing's Blaster riffle": "Aurra Sing's Blaster Rifle",
    "Alert My Star Destroyer! (V)": "Alert My Star Destroyer!",
    "Found Someone You Have (V)": "Found Someone You Have",
    "Kryat Dragon Bones (V)": "Krayt Dragon Bones",
    "Punishing One (V)": "Punishing One",
    "Spaceport: Docking Bay": "Spaceport Docking Bay",
    "Jabba's Sail Barge Passenger Deck": "Jabba's Sail Barge: Passenger Deck",
    "Honor Or The Jedi": "Honor Of The Jedi",
    "Starship Levitation (V)": "Starship Levitation",
    "Jedi Levitation (V)": "Jedi Levitation",
    "Yodass Hope": "Yoda's Hope",
    "A Jediss Strength": "A Jedi's Strength",
    "Vader w/saber": "Darth Vader With Lightsaber",
    "SFS L-s9.3 TIE Cannon": "SFS L-s9.3 Laser Cannons",
    "Flawless Markmanship": "Flawless Marksmanship",
    "Sense combo": "Sense",
    "Your Insight Serves You Well & Stagin Areas": "Your Insight Serves You Well & Staging Areas",
    "Qui-Gon Jinn w/Lightsaber": "Qui-Gon Jinn With Lightsaber",
    "Obi-Wan w/Ligthsaber": "Obi-Wan With Lightsaber",
    "Obi-Wan's Ligthsaber": "Obi-Wan's Lightsaber",
    "Maul's Double-Bladed Ligthsaber": "Maul's Double-Bladed Lightsaber",
    "Vader's Ligthsaber": "Vader's Lightsaber",
    "Rondevous Point": "Rendezvous Point",
    "Slayn and Korpil Facility": "Slayn & Korpil Facilities",
    "Slayn & Korpil Facility": "Slayn & Korpil Facilities",
    "Jungle< proxying DAG: Jungle": "Jungle",
    "Comm Wedge Antilles": "Commander Wedge Antilles",
    "Admiral Akbar": "Admiral Ackbar",
    "Dagobah: Swamp or Dagobah: Bog Clearing": "Dagobah: Swamp",
    "court": "Court Of The Vile Gangster",
    "Prep def": "Prepared Defenses",
    "Desalijic tatoo (V)": "Desilijic Tattoo",
    "Desijilic Tatoo (V)": "Desilijic Tattoo",
    "LLL (V)": "Location, Location, Location",
    "Allwrapped up": "All Wrapped Up",
    "epp dengar": "Dengar With Blaster Carbine",
    "Dr e and panda b": "Dr. Evazan & Ponda Baba",
    "Sali crum": "Salacious Crumb",
    "epp Bossk": "Bossk With Mortar Gun",
    "Iggy (V)": "IG-88",
    "4lom epp": "4-LOM With Concussion Rifle",
    "spc port db": "Spaceport Docking Bay",
    "Droid workshop": "Jabba's Palace: Droid Workshop",
    "jabba's palace": "Jabba's Palace: Entrance Cavern",
    "Dagoba Cave": "Dagobah: Cave",
    "Sale barge": "Jabba's Sail Barge",
    "epp mist hunter": "Zuckuss In Mist Hunter",
    "epp ig2000": "IG-88 In IG-2000",
    "Ket Malis (V)": "Ket Maliss (V)",
    "Mj's stick": "Mara Jade's Lightsaber",
    "Dengar's big gun": "Dengar's Modified Riot Gun",
    "Felterprin trevagg's gun": "Blaster",
    "Hold-out Blaster": "Blaster",
    "Manuvering Flaps (V)": "Maneuvering Flaps",
    "Lock\" Navander (V)": "Romas \"Lock\" Navander",
    "Mandolarian armor": "Mandalorian Armor",
    "Twi'lik advisor": "Twi'lek Advisor",
    "Jabba's through w/ you": "Jabba's Through With You",
    "oota goota (V)": "Oo-ta Goo-ta, Solo? (V)",
    "Imperial berier": "Imperial Barrier",
    "mara jade teh": "Mara Jade, The Emperor's Hand",
    "ev9d9": "EV-9D9",
    "audience chamber": "Jabba's Palace: Audience Chamber",
    "sarlaac pit": "Tatooine: Great Pit Of Carkoon",
    "dungean": "Jabba's Palace: Dungeon",
    "IG-88's Neural Inhibitor (V)": "IG-88's Neural Inhibitor",
    "RL in R1": "Red Leader In Red 1",
    "GL in G1": "Gold Leader In Gold 1",
    "Arliel Schous": "Arleil Schous",
    "Blaster Rifles": "Blaster Rifle",
    "Death Star 2: Docking Bay 327": "Death Star II: Docking Bay",
    "DS-18-13": "DS-181-3",
    "DS-18-14": "DS-181-4",
    "Hoth Main Powergenerators": "Hoth: Main Power Generators (1st Marker)",
    "Hoth Echo Command Center": "Hoth: Echo Command Center (War Room)",
    "Hoth North Ridge": "Hoth: North Ridge (4th Marker)",
    "Hoth Echo Docking Bay": "Hoth: Echo Docking Bay",
    "Hoth Echo Med Lab": "Hoth: Echo Med Lab",
    "Hoth Snow Trench": "Hoth: Snow Trench (2nd Marker)",
    "Hoth Defensive Perimeter": "Hoth: Defensive Perimeter (3rd Marker)",
    "Echo Base Garision": "Echo Base Garrison",
    "Stike Planning": "Strike Planning",
    "Dual Lasser Cannon (V)": "Dual Laser Cannon",
    "Derek 'Hobbue'Klivian": "Derek 'Hobbie' Klivian",
    "Wedge Antilles, Red Squadren Leader": "Wedge Antilles, Red Squadron Leader",
    "dart vader, dark lord of the sith": "Darth Vader, Dark Lord Of The Sith",
    "tatooine: catina": "Tatooine: Cantina",
    "Hunt Down/Fire's Gone Out": "Hunt Down And Destroy The Jedi",
    "Visage o/t Empy": "Visage Of The Emperor",
    "Ex: Med": "Executor: Meditation Chamber",
    "Executor: Med": "Executor: Meditation Chamber",
    "Ex: Holo": "Executor: Holotheatre",
    "Executor: Holo": "Executor: Holotheatre",
    "Coruscant: Imp Square": "Coruscant: Imperial Square",
    "DV w/ Stick": "Darth Vader With Lightsaber",
    "Mara, TEH": "Mara Jade, The Emperor's Hand",
    "Fett w/ gun": "Boba Fett With Blaster Rifle",
    "IG-88 in IG-2k": "IG-88 In IG-2000",
    "ZiMH": "Zuckuss In Mist Hunter",
    "BFiS1": "Boba Fett In Slave I",
    "DiPO": "Dengar In Punishing One",
    "Weapon Lev": "Weapon Levitation",
    "Image o/t Dark Lord (V)": "Image Of The Dark Lord",
    "Heading f/t Medical Frigate": "Heading For The Medical Frigate",
    "Keeping t/ Empire Out Forever": "Keeping The Empire Out Forever",
    "SquAssin": "Squadron Assignments",
    "B: Cloud City": "Bespin: Cloud City",
    "Bespin: Cloud City": "Bespin: Cloud City",
    "SOS (V)": "Son of Skywalker",
    "Han's (V) Blaster": "Han's Heavy Blaster Pistol (V)",
    "Ani's Stick": "Anakin's Lightsaber",
    "Chewie's Stick": "Chewbacca's Bowcaster",
    "Luke's Stick": "Luke's Lightsaber",
    "Gold Squad 1": "Gold Squadron 1",
    "Red Squad 4": "Red Squadron 4",
    "Red Squad 1": "Red Squadron 1",
    "Clash": "Clash Of Sabers",
    "Path & Revealed": "Path Of Least Resistance & Revealed",
    "Saber Prof": "Lightsaber Proficiency",
    "CC Celebration": "Cloud City Celebration",
    "LS, JK": "Luke Skywalker, Jedi Knight",
    "Captain Han": "Captain Han Solo",
    "Wedge, RSL": "Wedge Antilles, Red Squadron Leader",
    "Obi's Stick": "Obi-Wan's Lightsaber",
    "X-Wing Cannons": "X-wing Laser Cannon",
    "Tattoo (V)": "Desilijic Tattoo",
    "Coruscant: Imp City": "Coruscant: Imperial City",
    "Dengar (V)": "Dengar",
    "Dengar's Carbine": "Dengar's Blaster Carbine",
    "IGGY's Pulse Cannon": "IG-88's Pulse Cannon",
    "Bossk's Mortar": "Bossk's Mortar Gun",
    "Ponda Boba's Hold-out": "Ponda Baba's Hold-out Blaster",
    "IGGY's Inhibitor (V)": "IG-88's Neural Inhibitor",
    "Control & SFS": "Control & Set For Stun",
    "Presence o/t Force": "Presence Of The Force",
    "DODN & Wise Advice": "Do, Or Do Not & Wise Advice",
    "Hoth: MPG": "Hoth: Main Power Generators (1st Marker)",
    "Hoth: 4th marker": "Hoth: North Ridge (4th Marker)",
    "Hoth: Echo DB": "Hoth: Echo Docking Bay",
    '"Lock" Navander (V)': 'Romas "Lock" Navander',
    "Rieekan (V)": "General Carlist Rieekan",
    "Farmboy (V)": "Luke Skywalker (V)",
    "Chewie, Protector": "Chewbacca, Protector",
    "Dodonna (V)": "General Dodonna (V)",
    "Biggs": "Biggs Darklighter",
    "Y-Wing Squadron": "Y-wing",
    "Echo Base Ops": "Echo Base Operations",
    "TDIGWATT/PIDAIF": "This Deal Is Getting Worse All The Time",
    "Elite Squad Stormtrooper": "Elite Squadron Stormtrooper",
    "Imp Domination (V)": "Imperial Domination",
    "IAO & SP": "Imperial Arrest Order & Secret Plans",
    "YCHF & Mob Points": "You Cannot Hide Forever & Mobilization Points",
    "Bespin: CC": "Bespin: Cloud City",
    "MLITL / IWMIL": "My Lord, Is That Legal?",
    "Coruscant: Galactic Senat": "Coruscant: Galactic Senate",
    "Lott Dot": "Lott Dod",
    "Ask Moe": "Aks Moe",
    "Capitan Gilad Pellaeon": "Captain Gilad Pellaeon",
    "Maul's Double Bladed Lightsabre": "Maul's Double-Bladed Lightsaber",
    "Sunsdown/ To Cold For The Speeders": "Sunsdown & Too Cold For Speeders",
    "On The Pay Roll Of The Trade Federation": "On The Payroll Of The Trade Federation",
    "No Civility Only Politics": "No Civility, Only Politics",
    "WHT/TDOF": "We'll Handle This",
    "Bontaa Eve Podrace": "Boonta Eve Podrace",
    "Qui Gon Jinn Jedi Master": "Qui-Gon Jinn, Jedi Master",
    "Qui Gon's Lightsabre": "Qui-Gon Jinn's Lightsaber",
    "Obi wans Lightsabre": "Obi-Wan's Lightsaber",
    "Leias Blaster Rifle": "Leia's Blaster Rifle",
    "Courage Of The Skywalker": "Courage Of A Skywalker",
    "Speak To The Jedi Council": "Speak With The Jedi Council",
    "Imperial Class Star Destrover (V)": "Imperial-Class Star Destroyer (V)",
    "Mace Windu Jedi Master": "Mace Windu, Jedi Master",
    "Yoda Master Of The Force": "Yoda, Master Of The Force",
    "Naboo Theed Palace Generator": "Naboo: Theed Palace Generator",
    "Naboo Theed Palace Generator Core": "Naboo: Theed Palace Generator Core",
    "Coruscant Jedi Council Chamber": "Coruscant: Jedi Council Chamber",
    "Circle": "The Circle Is Now Complete",
    "Hobbie": "Derek 'Hobbie' Klivian",
    "Mirax": "Mirax Terrik",
    "Dash": "Dash Rendar",
    "Artoo": "R2-D2 (Artoo-Detoo)",
    "Princess Organa": "Princess Leia",
    "Agents of Black Sun/Vengeance of the Dark Sun": "Agents Of Black Sun",
    "The Emporer": "The Emperor",
    "IG-88's Nueral Inhibitor": "IG-88's Neural Inhibitor",
    "Prescence of the Force": "Presence Of The Force",
    "Kitik Keed'tik (V)": "Kitik Keed'kak (V)",
    "Kitik Keed’tik (V)": "Kitik Keed'kak (V)",
    "OS-71-2 In Obsidian 2": "OS-72-2 In Obsidian 2",
    "OS-71-1 In Obsidian 1": "OS-72-1 In Obsidian 1",
    "Tallon Roll & Dark Manuevers": "Dark Maneuvers & Tallon Roll",
    "Boba Fett w/ Rifle": "Boba Fett With Blaster Rifle",
    "Dr. Evazan & Ponda": "Dr. Evazan & Ponda Baba",
    "Rescue The Prince/Sometimes I Amaze Even Myself": "Rescue The Princess",
    "Obi-Won With Lightsaber": "Obi-Wan With Lightsaber",
    "Lando Calrisian Scoundrel": "Lando Calrissian, Scoundrel",
    "R2D2 In Red 5": "Artoo-Detoo In Red 5",
    "R2 in Red 5": "Artoo-Detoo In Red 5",
    "Qui Gon's Lightsaber": "Qui-Gon Jinn's Lightsaber",
    "Artoo and Threepio": "Artoo & Threepio",
    "Mobilization Points & You Cannot Hide Forever": "You Cannot Hide Forever & Mobilization Points",
    "Sergeant Elesk": "Sergeant Elsek",
    "EX-10 (Effex-ten) Medical Droid": "FX-10 (Effex-ten)",
    "Flagships Executor": "Flagship Executor",
    "Saber One": "Saber 1",
    "You Cannot Hide Forever/Mob. Points": "You Cannot Hide Forever & Mobilization Points",
    "Admiral Chieranu": "Admiral Chiraneau",
    "Oppresive Enforcment": "Oppressive Enforcement",
    "Advance Preperation (V)": "Advance Preparation (V)",
    "Dagobah: Jungle": "Jungle",
    "Naboo: Boss Nass's Chambers": "Naboo: Boss Nass' Chambers",
    "King Xizor": "Prince Xizor",
    "Desilijic Tatoo (V)": "Desilijic Tattoo",
    "EPP Luke Skywalker": "Luke With Lightsaber",
    "Obi wans Lightsabre ( Ref 3 )": "Obi-Wan's Lightsaber",
    "Darth Maul Demise": "Darth Maul's Demise",
    "Arment Dismanteled": "Disarmed",
    "Strangles": "Strangle",
    "Honor of a Jedi": "Honor Of The Jedi",
    "Old Pirates": "Old Allies",
    "Artoo in Red 5": "Artoo-Detoo In Red 5",
    "Artoo-Deeto in Red 5": "Artoo-Detoo In Red 5",
    "Darth Vader, Darth Lord Of The Sith": "Darth Vader, Dark Lord Of The Sith",
    "Qui Gon Jinn w/ Lightsaber": "Qui-Gon Jinn With Lightsaber",
    "Obi Wan Kenobi w/ Lightsaber": "Obi-Wan With Lightsaber",
    "Masayana": "Masanya",
    "X Wing Laser Cannon": "X-wing Laser Cannon",
    "Location Location Location (V)": "Location, Location, Location",
    "Location, Location, Location, (V)": "Location, Location, Location",
    "Kiffix": "Kiffex",
    "RalOps/ITHOFE": "Ralltiir Operations",
    "Bike Scout": "Biker Scout Trooper",
    "Officer Evaz": "Officer Evax",
    "Dreanaught-Class Heavy Cruiser": "Dreadnaught-Class Heavy Cruiser",
    "Masterful Move & Ender Occupation": "Masterful Move & Endor Occupation",
    "Lando In Millienium Falcon": "Lando In Millennium Falcon",
    "Oota-goota Solo?": "Oo-ta Goo-ta, Solo? (V)",
    "Oota-goota Solo": "Oo-ta Goo-ta, Solo? (V)",
    "Court of the Vile Gangster/ I shall enjoy watching you die": "Court Of The Vile Gangster",
    "Great Pit of Carkoon": "Tatooine: Great Pit Of Carkoon",
    "Dr Evazan and Ponda Baba": "Dr. Evazan & Ponda Baba",
    "jedi light sabers": "Jedi Lightsaber",
    "blasTech E-11B Blaster Rife": "BlasTech E-11B Blaster Rifle",
    "Obi-Wan with light saber": "Obi-Wan With Lightsaber",
    "Commande Wedge Antilles": "Commander Wedge Antilles",
    "BoSheck": "BoShek",
    "Seargent Doallyn": "Sergeant Doallyn",
    "Seargent Junkin": "Sergeant Junkin",
    "Seargant Bruckman": "Sergeant Bruckman",
    "Rouge 3": "Rogue 3",
    "Obi-Wan's light saber": "Obi-Wan's Lightsaber",
    "first marker": "Hoth: Main Power Generators (1st Marker)",
    "second marker": "Hoth: Snow Trench (2nd Marker)",
    "third marker": "Hoth: Defensive Perimeter (3rd Marker)",
    "fourth marker": "Hoth: North Ridge (4th Marker)",
    "war room": "Hoth: Echo Command Center (War Room)",
    "EBO": "Echo Base Operations",
    "Theron Hett": "Theron Nett",
    "Gold Squadron One": "Gold Squadron 1",
    "Big One: Asteroid Cave/Space Slug Belly": "Big One: Asteroid Cave Or Space Slug Belly",
    "Hidden Base/ Systems Will Slip Through Your Fingers": "Hidden Base",
    "Hidden Base/Flip Side": "Hidden Base",
    "Hidden Base/SWSTYF": "Hidden Base",
    "Woking (V)": "Wokling (V)",
    "Genral Veers": "General Veers",
    "Gteneral Veers": "General Veers",
    "Corporal Avirak": "Corporal Avarik",
    "Corporla Avirak": "Corporal Avarik",
    "Super Laser": "Superlaser",
    "Temest 1": "Tempest 1",
    "Deah Star": "Death Star",
    "Docking control room": "Death Star: Docking Control Room 327",
    "Detention block": "Death Star: Detention Block Corridor",
    "Kyshyyk": "Kashyyyk",
    "Kahyyk": "Kashyyyk",
    "Kashyyk": "Kashyyyk",
    "Rathial": "Ralltiir",
    "IG-200": "IG-2000",
    "Niado Duagad": "Niado Duegad",
    "Admiral Ackabar": "Admiral Ackbar",
    "Jeck Porkins": "Jek Porkins",
    "Boshek": "BoShek",
    "Targeting Compuer": "Targeting Computer",
    "concussion missle": "Concussion Missiles",
    "Luke With Ligthsaber": "Luke With Lightsaber",
    "Luke with Ligtsaber": "Luke With Lightsaber",
    "Obi- Wan With lightsaber": "Obi-Wan With Lightsaber",
    "Chewbacca of Kashyyk": "Chewbacca Of Kashyyyk",
    "Death Star 2: Coolant Shaft": "Death Star II: Coolant Shaft",
    "Death Star 2: Capacitors": "Death Star II: Capacitors",
    "Death Star 2: Reactor Core": "Death Star II: Reactor Core",
    "Darth Vader w Saber": "Darth Vader With Lightsaber",
    "Darth Maul w Saber": "Darth Maul With Lightsaber",
    "Darth Maul w/ Lightsaber": "Darth Maul With Lightsaber",
    "Dreadnought Class Heavy Cruiser": "Dreadnaught-Class Heavy Cruiser",
    "Superlaser Mark 2": "Superlaser Mark II",
    "SFS L-s9.3 Laser Cannon": "SFS L-s9.3 Laser Cannons",
    "Intrder Missile": "Intruder Missile",
    "Start Destroyer!": "Star Destroyer!",
    "Star Destoryer": "Star Destroyer!",
    "An Unusual Amount Of Fear w/Shields only": "An Unusual Amount Of Fear",
    "Heading For THe Medical Frigate": "Heading For The Medical Frigate",
    "Heading For A Medical Frigate": "Heading For The Medical Frigate",
    "Profit": "You Can Either Profit By This...",
    "Sorry About The Mess combo": "Sorry About The Mess & Blaster Proficiency",
    "WWTBAO": "We Wish To Board At Once",
    "MotF": "Yoda, Master Of The Force",
    "Beggar's Canyon": "Tatooine: Beggar's Canyon",
    "Anikan's Lightsaber": "Anakin's Lightsaber",
    "Qui-Gon's Lightsaber (Tat)": "Qui-Gon Jinn's Lightsaber",
    "Obi-Wan's Lightsaber (Pre)": "Obi-Wan's Lightsaber",
    "Wedges Antilles, Red Squadron Leader": "Wedge Antilles, Red Squadron Leader",
    "Derek “Hobbie” Kilvian": "Derek 'Hobbie' Klivian",
    "Derek \"Hobbie\" Kilvian": "Derek 'Hobbie' Klivian",
    "Kessell": "Kessel",
    "Artoo In Red 5": "Artoo-Detoo In Red 5",
    "Home 1": "Home One",
    "A Few Manuevers": "A Few Maneuvers",
    "Han with Heavy Blaster Pistol": "Han With Heavy Blaster Pistol",
    "Chewie with Blaster Rifle": "Chewie With Blaster Rifle",
    "Lando with Vibro Ax": "Lando With Vibro-Ax",
    "Artoo-Detoo in Red5": "Artoo-Detoo In Red 5",
    "Red Squadron7": "Red Squadron 7",
    "Red Squadron4": "Red Squadron 4",
    "Bravo3": "Bravo 3",
    "Bravo5": "Bravo 5",
    "Golan LAser Battery": "Golan Laser Battery",
    "Proton Torpedoes (E1)": "Proton Torpedoes",
    "Return of a Jedi": "Return Of A Jedi",
    "Lukes Back": "Luke's Back",
    "Dengar with Blaster Carbine": "Dengar With Blaster Carbine",
    "Tie Interceptor": "TIE Interceptor",
    "Scythe Squadron Tie": "Scythe Squadron TIE",
    "Imerial-Class Star Destroyer": "Imperial-Class Star Destroyer",
    "Single Trooer Aerial Platform": "Single Trooper Aerial Platform",
    "SFS-L-s7.2 Tie Cannon": "SFS L-s7.2 TIE Cannon",
    "AAT Laser CAnnon": "AAT Laser Cannon",
    "The Empires Back": "The Empire's Back",
    "Naboo Theed Palace: Hall Way": "Naboo: Theed Palace Hallway",
    "Tatooine Mos Eisley": "Tatooine: Mos Eisley",
    "Blokade Flagship: Docking Bay": "Blockade Flagship: Docking Bay",
    "Padme' Naberrie": "Padme Naberrie",
    "Rycar Ryjerd(V)": "Rycar Ryjerd (V)",
    "Genearl Carlist Rieekan(V)": "General Carlist Rieekan",
    "Nar Shaddaa Wind Chimes & Out of Nowhere": "Nar Shaddaa Wind Chimes & Out Of Somewhere",
    "Run, Luke, Run!": "Run Luke, Run!",
    "Obi Wan's Journal": "Obi-Wan's Journal",
    "The Signal (Uh-Oh)": "The Signal",
    "Jabba’s Palace: Audience Chamber": "Jabba's Palace: Audience Chamber",
    "Wookie": "Wookiee",
    "Scimitar Squadron TIE Bomber": "Scimitar Squadron TIE",
    "Dreadnaught": "Dreadnaught-Class Heavy Cruiser",
    "Coruscant (Ep1)": "Coruscant",
    "Tatooine (Ep1)": "Tatooine",
    "I Can’t Shake Him": "I Can't Shake Him",
    "Rayc Ryjerd (V)": "Rycar Ryjerd (V)",
    "Bron Burs (V)": "Bron Burs",
    "Scrambled Transmission (V)": "Scrambled Transmission",
    "Asteroids Do Not Concern Me (V)": "Asteroids Do Not Concern Me",
    "General Carlist Rieekan (V)": "General Carlist Rieekan",
    "IG-88's pulse cannon": "IG-88's Pulse Cannon",
    "Antipersonel laser cannon": "Antipersonnel Laser Cannon",
    "Antipersonel Laser Cannon": "Antipersonnel Laser Cannon",
    "Turbolase battery": "Turbolaser Battery",
    "central core": "Death Star: Central Core",
    "military corridor": "Death Star: Level 4 Military Corridor",
    "congerence room": "Death Star: Conference Room",
    "Wron turn": "Wrong Turn",
    "ability, ability, aility": "Ability, Ability, Ability",
    "look sir, droids": "Look Sir, Droids",
    "look sir": "Look Sir, Droids",
    "he is no ready": "He Is Not Ready",
    "he is not ready": "He Is Not Ready",
    "Commnce primary ignition": "Commence Primary Ignition",
    "Detention block Corridor": "Death Star: Detention Block Corridor",
    "Dark Jedi Lightasaber": "Dark Jedi Lightsaber",
    "X wing laser canon": "X-wing Laser Cannon",
    "Genearl Carlist Rieekan (V)": "General Carlist Rieekan",
    "Jabbaâs Palace: Audience Chamber": "Jabba's Palace: Audience Chamber",
    "Stay Sharp": "Stay Sharp!",
    "Mind What You Have Learned/SYIC": "Mind What You Have Learned",
    "Threepio, Naked": "Threepio With His Parts Showing",
    "thgisdniH": "Hindsight",
    "Set Your Course For Alderaan/TUPITU": "Set Your Course For Alderaan",
    "You Cannot Hide Forever & Mob Points": "You Cannot Hide Forever & Mobilization Points",
    "Big One: Asteroid Cave": "Big One: Asteroid Cave Or Space Slug Belly",
    "Capt' Han Solo": "Captain Han Solo",
    "'Respectable' Lando": "Lando Calrissian, Scoundrel",
    "Farmboy Luke (V)": "Luke Skywalker (V)",
    "Yoda Stew & You Have Your Moments": "Yoda Stew & You Do Have Your Moments",
    "Djus Phur (V)": "Djas Puhr (V)",
    "Aurra Sing's Blaster": "Aurra Sing's Blaster Rifle",
    "Away Put Your Weapons (V)": "Away Put Your Weapon",
    "Obi-Wans Cape (V)": "Obi-Wan's Cape",
    "First Officer Thannespi": "First Officer Thaneespi",
    "Major Hassh'n": "Major Haash'n",
    "Millenniun Falcon": "Millennium Falcon",
    "Mellennium Falcon": "Millennium Falcon",
    "Jabba the hut": "Jabba The Hutt",
    "Dengar with BC": "Dengar With Blaster Carbine",
    "Bossk with MG": "Bossk With Mortar Gun",
    "The Will Be No Match For You": "They Will Be No Match For You",
    "You Can Either Profit From This": "You Can Either Profit By This...",
    "He's A Man": "Lando's Not A System, He's A Man",
    "MJ": "Mara Jade, The Emperor's Hand",
    "Lieutennant Blount": "Lieutenant Blount",
    "Prepare For A Surface Assault": "Prepare For A Surface Attack",
    "Sinear Fleet Systems": "Sienar Fleet Systems",
    "Fear Is My Ally & Ten Shields": "Fear Is My Ally",
    "Take Evasive Action! (V)": "Take Evasive Action",
    "Houndstooth (V)": "Hound's Tooth",
    "Coruscant, Ep1": "Coruscant",
    "Set Your Course For Alderaan/I'm Determined To Flip": "Set Your Course For Alderaan",
    "Darth Vader With Ligthsaber": "Darth Vader With Lightsaber",
    "Darth Maul With Ligthsaber": "Darth Maul With Lightsaber",
    "Obi-Wan, Padawan": "Obi-Wan Kenobi, Padawan Learner",
    "Lando w/ Vibro Ax": "Lando With Vibro-Ax",
    "Naboo Blaster Rifles": "Naboo Blaster Rifle",
    "SATM & Blaster Proficiency": "Sorry About The Mess & Blaster Proficiency",
    "Into the Garbage Shoot Flyboy (V)": "Into The Garbage Chute, Flyboy",
    "X-Wing Cannon": "X-wing Laser Cannon",
    "X-Wing Laser Cannons": "X-wing Laser Cannon",
    "Slight Weapons Malfuntion": "Slight Weapons Malfunction",
    "Intruder Missle": "Intruder Missile",
    "Yoda's Gimmer Stick": "Yoda's Gimer Stick",
    "Red Squad 1": "Red Squadron 1",
    "Gold Squad 1": "Gold Squadron 1",
    "Wedge, RSL": "Wedge Antilles, Red Squadron Leader",
    "Boba fett, bountyhunter": "Boba Fett, Bounty Hunter",
    "Asteroids Do Not Concern Me, Admiral (V)": "Asteroids Do Not Concern Me",
    "this deck is 4 cards over the 60 card limit": "",
    "dr. evazon and ponda baba": "Dr. Evazan & Ponda Baba",
    "dr. evazon's sawed-off blaster": "Dr. Evazan's Sawed-off Blaster",
    "KTEOF": "Keep Your Eyes Open",
    "The Bith Shuffle/Desperate Reach": "The Bith Shuffle & Desperate Reach",
    "Tatooine: Jabba's Palce": "Tatooine: Jabba's Palace",
    "Jabba, The Hutt": "Jabba The Hutt",
    "Jabba's Barge: Passenger Deck": "Jabba's Sail Barge: Passenger Deck",
    "Bib Foruna": "Bib Fortuna",
    "Hoth: Ice Plains (5th)": "Hoth: Ice Plains (5th Marker)",
    "Hoth: Main Power Generators (1st)": "Hoth: Main Power Generators (1st Marker)",
    "Hoth: North Ridge (4th)": "Hoth: North Ridge (4th Marker)",
    "Hoth: Defensive Perimeter (3rd)": "Hoth: Defensive Perimeter (3rd Marker)",
    "Chimes & Out Of Somewhere": "Nar Shaddaa Wind Chimes & Out Of Somewhere",
    "OOC & Transmission Terminated": "Out Of Commission & Transmission Terminated",
    "Bith Shuffle & Desparate Reach": "The Bith Shuffle & Desperate Reach",
    "Imperial Attrocity": "Imperial Atrocity",
    "Princess Rebel": "Leia, Rebel Princess",
    "Alert My Star Destroyer (V)": "Alert My Star Destroyer!",
    "Ralltir Ops": "Ralltiir Operations",
    "Tat D-bay": "Tatooine: Docking Bay 94",
    "Blockade Fship D-bay": "Blockade Flagship: Docking Bay",
    "DSII D-Bay": "Death Star II: Docking Bay",
    "Endor L-platform": "Endor: Landing Platform (Docking Bay)",
    "S-port D-bay": "Spaceport Docking Bay",
    "S-port Prefects Office": "Spaceport Prefect's Office",
    "S-port Street": "Spaceport Street",
    "Emergency Deploymnent": "Emergency Deployment",
    "Abyssin Orn": "Abyssin Ornament",
    "Dlots": "Darth Vader, Dark Lord Of The Sith",
    "Darth Sideous": "Darth Sidious",
    "Kir kanos": "Kir Kanos",
    "Tempest Scout": "Tempest Scout 1",
    "T Scout 3": "Tempest Scout 3",
    "T Scout 5": "Tempest Scout 5",
    "Tempest": "Tempest 1",
    "Disrptor Pistol": "Disruptor Pistol",
    "Mob Points combo": "You Cannot Hide Forever & Mobilization Points",
    "Capt. Han": "Captain Han Solo",
    "Han Solo w/ Heavy Blaster Pistol": "Han With Heavy Blaster Pistol",
    "Dejarik Holotable": "Dejarik Hologameboard",
    "Projections of a Skywalker": "Projection Of A Skywalker",
    "Weesa Gotta Grand Army": "Wesa Gotta Grand Army",
    "I-T0 (V)": "IT-O (Eyetee-Oh)",
    "Spaceport City Docking Bay": "Spaceport Docking Bay",
    "Small Range Fighters & Watch You Back!": "Short Range Fighters & Watch Your Back!",
    "No Money, No Parts, No Deal/You're A Slave?": "No Money, No Parts, No Deal!",
    "YCHF & Mobilization Points": "You Cannot Hide Forever & Mobilization Points",
    "Allegations": "Allegations Of Corruption",
    "Coward": "He's A Coward",
    "Oppressive": "Oppressive Enforcement",
    "Sentry (V)": "Death Star Sentry (V)",
    "FIMA": "Fear Is My Ally",
    "Lower Corridor": "Cloud City: Lower Corridor",
    "Bespin CC": "Bespin: Cloud City",
    "Dr. E & Ponda B": "Dr. Evazan & Ponda Baba",
    "Dr. E&Ponda B": "Dr. Evazan & Ponda Baba",
    "BiHT": "Bossk In Hound's Tooth",
    "SRF combo": "Short Range Fighters & Watch Your Back!",
    "Control combo": "Control & Set For Stun",
    "Alter combo": "Alter & Collateral Damage",
    "Ghhhk combo": "Ghhhk & Those Rebels Won't Escape Us",
    "AAA": "Ability, Ability, Ability",
    "Lat Damage": "Lateral Damage",
    "CCO": "Cloud City Occupation",
    "Hoth 4th marker": "Hoth: North Ridge (4th Marker)",
    "Hoth 1st Marker": "Hoth: Main Power Generators (1st Marker)",
    "Eco base DB": "Hoth: Echo Docking Bay",
    "Eco Base War Room": "Hoth: Echo Command Center (War Room)",
    "Eco Base Corridor": "Hoth: Echo Corridor",
    "General Carlist Riken (V)": "General Carlist Rieekan",
    "Capt Han Solo": "Captain Han Solo",
    "Miriax Terik": "Mirax Terrik",
    "Bigs Darklighter (V)": "Biggs Darklighter",
    "Tyco": "Tycho Celchu",
    "Princess Leia (V)": "Leia (V)",
    "X-Wing Laser canons": "X-wing Laser Cannon",
    "Carbon testing": "Carbon-Freezing",
    "Any means necessary": "Any Methods Necessary",
    "Neado Duegad": "Niado Duegad",
    "Bossk W/ Mortor gun": "Bossk With Mortar Gun",
    "Blater rack (V)": "Blaster Rack (V)",
    "Tatooine occ": "Tatooine Occupation",
    "Reactor term": "Reactor Terminal",
    "East db": "East Platform (Docking Bay)",
    "Fetts blaster rifle": "Boba Fett's Blaster Rifle",
    "Fett's blaster rifle": "Boba Fett's Blaster Rifle",
    "Trevaggs stun rifle": "Feltipern Trevagg's Stun Rifle",
    "Tat JP": "Tatooine: Jabba's Palace",
    "Jp audience chamber": "Jabba's Palace: Audience Chamber",
    "annies pod": "Anakin's Podracer",
    "Tat pod arena": "Tatooine: Podrace Arena",
    "boonta P.R": "Boonta Eve Podrace",
    "Chewie- protector": "Chewbacca, Protector",
    "Liea (V)": "Leia (V)",
    "Luke, reb scout": "Luke Skywalker, Rebel Scout",
    "Padme nebarrie": "Padme Naberrie",
    "Lightsaber prof": "Lightsaber Proficiency",
    "Slight weap malfuc": "Slight Weapons Malfunction",
    "Tat city outskirts": "Tatooine: City Outskirts",
    "BHBM": "Bring Him Before Me",
    "Commander Merejk": "Commander Merrejk",
    "KKK (V)": "Kitik Keed'kak (V)",
    "DSquad SD": "Death Squadron Star Destroyer",
    "Darth Maul's Twinsaber": "Maul's Double-Bladed Lightsaber",
    "Pres of Force": "Presence Of The Force",
    "AAA or the Endor Effect": "Ability, Ability, Ability",
    "Maul's Desert Landing Site": "Tatooine: Desert Landing Site",
    "Boba Fett (V)": "Boba Fett",
    "Boba Fett's Gun (V)": "Boba Fett's Blaster Rifle",
    "Deslijic Tattoo (V)": "Desilijic Tattoo",
    "Despair (V)": "Despair",
    "Jabba's Bounty": "Hutt Bounty",
    "Imperial Decree (V)": "Imperial Decree",
    "He's All Yours Bounty Hunter (V)": "He's All Yours, Bounty Hunter",
    "Kuat Drive Yards (V)": "Kuat Drive Yards",
    "Corporal Vandolay (V)": "Corporal Vandolay",
    "Deflector Sheild Generators (V)": "Deflector Shield Generators",
    "Rune Haako, Legal Council": "Rune Haako, Legal Counsel",
    "Skate": "Pulsar Skate",
    "Control & Tunnel": "Control & Tunnel Vision",
    "The Bith Shuffle & Desparate Reach": "The Bith Shuffle & Desperate Reach",
    "Bith Shuffle & Desparate Reach": "The Bith Shuffle & Desperate Reach",
    "All Wings & Darklighter Spin": "All Wings Report In & Darklighter Spin",
    "Out Of Commission & Tranny Terminated": "Out Of Commission & Transmission Terminated",
    "Projection": "Projection Of A Skywalker",
    "Control and Tunnel vision": "Control & Tunnel Vision",
    "Nar shadda wind chimes combo": "Nar Shaddaa Wind Chimes & Out Of Somewhere",
    "X-wing lazer cannons": "X-wing Laser Cannon",
    "The Emperor (V)": "Emperor Palpatine",
    "Mauls Saber": "Maul's Double-Bladed Lightsaber",
    "Ghhhk & TRWEU": "Ghhhk & Those Rebels Won't Escape Us",
    "Ability": "Ability, Ability, Ability",
    "Dengar With Carbine": "Dengar With Blaster Carbine",
    "Ability Ability Ability (V)": "Ability, Ability, Ability",
    "Imp Propaganda (V)": "Imperial Propaganda",
    "Wedge RSL": "Wedge Antilles, Red Squadron Leader",
    "Bright Hope (V)": "Bright Hope",
    "Tantive": "Tantive IV",
    "Keep Your Eyes Open (V)": "Keep Your Eyes Open",
    "Slight Weapon's Malfunction": "Slight Weapons Malfunction",
    "Corusant: Galatic Senate": "Coruscant: Galactic Senate",
    "Tatooine: Podrace Area": "Tatooine: Podrace Arena",
    "Sebulas Podracer": "Sebulba's Podracer",
    "Down With The Emperor (V)": "Down With The Emperor!",
    "Control/TV": "Control & Tunnel Vision",
    "Location (V)": "Location, Location, Location",
    "TMNALTC": "They Must Never Again Leave This City",
    "Krayt Bones (V)": "Krayt Dragon Bones",
    "General Dodona (V)": "General Dodonna (V)",
    "Lando Screamer": "Lando Calrissian, Scoundrel",
    "Artoo in Red Five": "Artoo-Detoo In Red 5",
    "Rebel Planers": "Rebel Planners",
    "Report To Your Ships/Squadron Assignments": "Squadron Assignments",
    "A Jedi Resilience": "A Jedi's Resilience",
    "Were Doomed": "We're Doomed",
    "Bith Shuffle Combo": "The Bith Shuffle & Desperate Reach",
    "Cloud City: East db": "Cloud City: East Platform (Docking Bay)",
    "Trevagg's stun rifle": "Feltipern Trevagg's Stun Rifle",
    "Tatooine: market place": "Tatooine: Marketplace",
    "Tat market place": "Tatooine: Marketplace",
    "Jp enterance cavern": "Jabba's Palace: Entrance Cavern",
    "Jabba's Palace: enterance cavern": "Jabba's Palace: Entrance Cavern",
    "Out rider": "Outrider",
    "Qui-gon's saper": "Qui-Gon Jinn's Lightsaber",
    "Qui-gons saper": "Qui-Gon Jinn's Lightsaber",
    "Obi-wans' saber": "Obi-Wan's Lightsaber",
    "Obi-wans saber": "Obi-Wan's Lightsaber",
    "Anikins saber": "Anakin's Lightsaber",
    "Anakin Skywalker's Lightsaber": "Anakin's Lightsaber",
    "Sebula's Podracer": "Sebulba's Podracer",
    "Obi's Saber": "Obi-Wan's Lightsaber",
    "Qui's Saber": "Qui-Gon Jinn's Lightsaber",
    "Ani's Saber": "Anakin's Lightsaber",
    "Chewie's Saber": "Chewbacca's Bowcaster",
    "Orrimaarka": "Orrimaarko",
    "Captain Bewil (V)": "Captain Bewil",
    "Ability^3 (V)": "Ability, Ability, Ability",
    "Ability ^3": "Ability, Ability, Ability",
    "Ability^3": "Ability, Ability, Ability",
    "Interrogation Room": "Cloud City: Interrogation Room",
    "Upper Plaza Corridor": "Cloud City: Upper Plaza Corridor",
    "Fett's gun (V)": "Boba Fett's Blaster Rifle",
    "Profit/be destroyed": "You Can Either Profit By This… Or Be Destroyed",
    "TAT Jabba's Palace": "Tatooine: Jabba's Palace",
    "Seeking An Audience (V)": "Seeking An Audience",
    "Leia RP": "Leia, Rebel Princess",
    "R3 Chewie": "Chewbacca Of Kashyyyk",
    "Epod (V)": "Escape Pod (V)",
    "Padmen Naberrie": "Padme Naberrie",
    "A Jedi's Reslience": "A Jedi's Resilience",
    "Imperial Attrocity (V)": "Imperial Atrocity",
    "Leia's Blaster Riffle": "Leia's Blaster Rifle",
    "Court Of The Vile Ganster": "Court Of The Vile Gangster",
    "IG 88 (V)": "IG-88",
    "Boba Fett CC (V)": "Boba Fett",
    "4 Lom With Concussion Rifle": "4-LOM With Concussion Rifle",
    "Sence & Uncertain Is The Future": "Sense & Uncertain Is The Future",
    "IG 88's Neural Inhibitor (V)": "IG-88's Neural Inhibitor",
    "Lar's Moisture Farm": "Tatooine: Lars' Moisture Farm",
    "Scum And Villiany": "Scum And Villainy",
    "Zuckus in Mist Hunter": "Zuckuss In Mist Hunter",
    "My Lord Is That Legal? / I Will Make It Legal": "My Lord, Is That Legal?",
    "Prepared Fences": "Prepared Defenses",
    "Dengar In Punish One": "Dengar In Punishing One",
    "Yeb Yeb": "Yeb Yeb Adem'thorn",
    "Senate Cam": "Senate Hovercam",
    'Romas "Lock" Navender (V)': 'Romas "Lock" Navander',
    "Jabba's Palace: Lower Passage": "Jabba's Palace: Lower Passages",
    "JP: Lower Passage": "Jabba's Palace: Lower Passages",
    "Sai'tor Kal Fas (V)": "Sai'torr Kal Fas (V)",
    "North Corridor": "Cloud City: North Corridor",
    "EPP Qui": "Qui-Gon Jinn With Lightsaber",
    "R3 Lando": "Lando Calrissian, Scoundrel",
    "Dolphe": "Officer Dolphe",
    "AWRI/Spin": "All Wings Report In & Darklighter Spin",
    "Captain Makador": "Captain Madakor",
    "Whooo": "Whoooo!",
    "Big Boomers": "Big Boomers!",
    "Endor: Rebel Landing Site": "Endor: Rebel Landing Site (Forest)",
    "Vane (V)": "Weather Vane",
    "Quigon With Lightsaber": "Qui-Gon Jinn With Lightsaber",
    "Obiwan With Lightsaber": "Obi-Wan With Lightsaber",
    "Beldon's Eye (V)": "Beldon's Eye",
    "Wookie Strangle (V)": "Wookiee Strangle",
    "Boba Fett's Blaster Rifle (V)": "Boba Fett's Blaster Rifle",
    "Computer Interface (V)": "Computer Interface",
    "Revealed & Path Of Least Resistance": "Path Of Least Resistance & Revealed",
    "Defensive Fire & Hutt Smootch": "Defensive Fire & Hutt Smooch",
    "Baskol Yeerisrim": "Baskol Yeesrim",
    "All Power Too Weapons": "All Power To Weapons",
    "Squabling Delegates": "Squabbling Delegates",
    "JSB: Passenger Deck": "Jabba's Sail Barge: Passenger Deck",
    "Boba Fett on Crack": "Boba Fett, Bounty Hunter",
    "OOC combo": "Out Of Commission & Transmission Terminated",
    "Houjix combo": "Houjix & Out Of Nowhere",
    "combat Responce": "Combat Response",
    "Establish Secert Base": "Establish Secret Base",
    "Ommuins Rumors": "Ominous Rumors",
    "Overseeing it Personaly": "Overseeing It Personally",
    "Pressence of the Force": "Presence Of The Force",
    "Blizard Scout 1": "Blizzard Scout 1",
    "Sergent Elsek": "Sergeant Elsek",
    "Sergent Barich": "Sergeant Barich",
    "Barron Soontir Fel": "Baron Soontir Fel",
    "Rycar (V)": "Rycar Ryjerd",
    "DOS": "Daughter Of Skywalker",
    "Qui's Stick": "Qui-Gon Jinn's Lightsaber",
    "Sense & Recoil": "Sense & Recoil In Fear",
    "Hoth: Med Lab (V)": "Hoth: Echo Med Lab",
    "Corran": "Corran Horn",
    "Dual Laser Cannons (V)": "Dual Laser Cannon",
    "ANSB": "A New Secret Base",
    "Ephont Mon": "Ephant Mon",
    "Hound's Touth (V)": "Hound's Tooth",
    "Twi'ek Advisor": "Twi'lek Advisor",
    "There Is No Try combo": "There Is No Try & Oppressive Enforcement",
    "Tatooine: Judland Wasted": "Tatooine: Jundland Wastes",
    "Gaderfii Stick": "Gaderffii Stick",
    "Gray Squad 1": "Gray Squadron 1",
    "Green Squad 1": "Green Squadron 1",
    "Short-range Fighters combo": "Short Range Fighters & Watch Your Back!",
    'Romas "Lock" Navader (V)': 'Romas "Lock" Navander',
    "We Muse Accelerate Our Plans": "We Must Accelerate Our Plans",
    "Leavatation Attack (V)": "Levitation Attack",
    "Batle Order": "Battle Order",
    "General Walex Blisses": "General Walex Blissex",
    "Luke's Blaster Pistol (V)": "Luke's Blaster Pistol",
    "Courage of a Skywalker (V)": "Courage Of A Skywalker",
}

HEADER_RE = re.compile(
    r"^[-–—*]*\s*&?\s*"
    r"(ojective|objcetive|objectives?|locations?|locatioins|loctions?|sites?|effects?|"
    r"interrupts?|interupts?|interupt|"
    r"vechiles?|endless droids|admirels?\s+orders?|ships\s*/\s*vehicles|"
    r"ships and vehicles|"
    r"inturrupts|"
    r"starships?\s+and\s+capital\s+starships?|"
    r"star destroyers?|"
    r"interupts?\s*/\s*effects?|interrupts?\s*&\s*effects?|effects?\s*&\s*interrupts?|"
    r"characters?\s*[-–—]\s*(?:imperial|alien|droid)(?:\s*/\s*(?:imperial|alien|droid))?|"
    r"characters?|charecters?|charactures?|charaters?|charactors?|charachters?|senators?|starships?|"
    r"ships?|starfighters?|vehicles?|vehicle|veichles?|weapons?|systems?|"
    r"creatures?|creatur[es]*|sith dudes|devices?|jedi tests?|jedi|epic events?|"
    r"podracers?|poderace|podracer|pod\s*racers?|"
    r"starting(?:\s+(?:effects?(?:/side\s*deck)?|cards?|objective|interrupt|effect\s*&\s*shields))?|"
    r"start(?:\s*int\.?)?|essentials|strategy|republic|"
    r"unknown type|ships\s*/\s*pilots|starships\s*/\s*vehicles|"
    r"reserve deck|deck name|"
    r"admiral'?s?\s*orders?|combat vehicles?|other(?:\s+locations?)?|devises?|"
    r"cards?\s+locations?|sites?\s*/\s*locations?|devices?\s*/\s*weapons?|"
    r"locations?\s*/\s*objectives?|objectives?\s*/\s*locations?|"
    r"devices?\s+and\s+weapons?|weapons?\s+and\s+devices?|"
    r"device\s*/\s*weapons?|weapons\s*/\s*devices?|weapons?/devices?|"
    r"weapons?\s*&\s*vehicles?|vehicles?\s*/\s*starships?|"
    r"defensive sheilds?|defensive shied(?:\s+deck(?:\s+with\s+\d+\s+shields?)?)?|"
    r"defensive shields?|def\s*sheilds?|def\s*shields?|def\s*shlds?|"
    r"d-shields|shields?|"
    r"side cards|10 side cards|weapons\s*&\s*devices|weapons\s+and\s+devices|"
    r"starships\s+and\s+vehicles|starships\s*&\s*vehicles|starships?\s*/\s*vehicles?|"
    r"ships\s*&\s*weapons|guys|misc\.?|purple|"
    r"fear is my ally cards|"
    r"effects?\s*\([^)]*political[^)]*\)|"
    r"rebels?|aliens?|droids?|parsecs?|space|used interrupts?|lost interrupts?|"
    r"darth maul character|imperials?|dark side|light side|"
    r"dark jedi(?:\s+master)?(?:\s*/\s*maul icon)?|maul icon|the fleet|"
    r"undercover spies|"
    r"bounty hunters?|"
    r"effect/?int|"
    r"starters|"
    r"last slot|"
    r"optional/?sideboard(?:\s+cards)?|"
    r"sideboard(?:\s+cards)?|"
    r"weopons|"
    r"characters?\s*/\s*droids?\s*/\s*creatures?|"
    r"characters?\s*/\s*creatures?|"
    r"characters? with ships|"
    r"hftmf pulls|"
    r"\bao\b|"
    r"\bair\b|"
    r"optional|"
    r"adm\s+orders?|usual start|stuff|racers|version|"
    r"cards?\s+starting|politicians?|jedi\s+and\s+friends|"
    r"ships\s+and\s+pilots|crazy\s+cards|crazies|sith|specials|orders|stating|"
    r"crazy\s+walkers|creature\s+vehicles|troopers?|"
    r"pilots?(?:\s*/\s*drivers?)?|rares|"
    r"effects?\s*/\s*interrupts?|interrupts?\s*/\s*effects?|"
    r"specials?|red cards|"
    r"starships?\s+and\s+vechiles?|"
    r"vehicles?\s*&\s*starships?|"
    r"starships?\s*/\s*vehicles?\s*/\s*podracers?|"
    r"characters?\s*:\s*(?:droid|alien|dark jedi.*)|"
    r"effects?\s+and\s+interrupts?|interrupts?\s+and\s+effects?|"
    r"green cards|blue cards|blue|green|red(?!\s+\d)|deck|"
    r"starting effects?|starting interrupts?|"
    r"a brief rundown|"
    r"purple cards|white cards|"
    r"immediate effects?|"
    r"locations?\s*/\s*planets?|"
    r"objectives?\s*/\s*starting(?:\s+stuff)?|"
    r"the starting stuff|"
    r"starting stuff|"
    r"objectives?\s*/\s*epic events?|"
    r"locales|"
    r"with defensive shields?|"
    r"characters?\s*\([^)]*\)|"
    r"destiny\s+\d+\s+cards|"
    r"sites?\s*/\s*systems?|"
    r"vehicles?\s*&\s*starships?|"
    r"non\s+jedi|"
    r"starting\s+hand|"
    r"space|land|battle|"
    r"weapons?\s*/\s*effects?|"
    r"systems?\s+and\s+sites?|"
    r"command cards?|"
    r"sights?|"
    r"under starting effect|"
    r"\+?\d+\s+optional cards|"
    r"interrupt/effect|"
    r"light side deck|"
    r"vehicles and starships|"
    r"characters?\s*&\s*droids|"
    r"sideboard options|"
    r"staring|"
    r"walkers|"
    r"weapons?\s*\+\s*devices?|"
    r"sites?\s*\(\s*(?:planetary|land)\)|"
    r"character weapons|"
    r"capital starships|"
    r"used/?starting interrupts?|"
    r"my (?:light|dark) side star wars cards deck|"
    r"droids?\s*-+\s*\d+|"
    r"essential defensive shields|"
    r"cards|"
    r"command|"
    r"weapons?/vehicles?|"
    r"weapons?\s*/\s*vehicles?|"
    r"starting cards|"
    r"sites?\s*\(\s*interior\s*\)|"
    r"used/?lost interrupts?|"
    r"epics?|"
    r"weapons?\s*/\s*vehicles?\s*/\s*devices?|"
    r"optional\s*/\s*interchangeable|"
    r"systems?\s*\(\s*\d+\s*-\s*\d+\s*\)|"
    r"characters?\s+and\s+droids?|"
    r"interrrupts?\s*/\s*effects?|"
    r"effects?\s*,\s*interrupts?\s*,\s*and\s+admiral'?s?\s+orders?|"
    r"interrupts?\s+and\s+effects?\s*\(\s*non-starting\s*\)|"
    r"effects?\s*\(\s*non-starting\s*\)|"
    r"characters?\s+droids?\s+creatures?|"
    r"characters?\s+and\s+creatures?|"
    r"weapons?\s+and\s+gadgets?|"
    r"political\s+effects?|"
    r"fighters?|"
    r"starting\s+interrupts?\s+and\s+effects?|"
    r"interrupts?\s*/\s*effects?\s*/\s*weapons?|"
    r"vehicles?\s+and\s+shuttles?|"
    r"capitol\s+ships?|"
    r"star\s+fighters?|"
    r"interuppts?|"
    r"characters?\s*/\s*starships?|"
    r"effect'?s?|"
    r"interrupt'?s?|"
    r"characters?\s*\(\s*\d+.*|"
    r"deck\s*\d+\s*\(\s*(?:dark|light).*|"
    r"devices?\s*/\s*jedi tests?|"
    r"locations?\s*(?:\(\s*\d+\s*\))?\s*ds\s*/\s*ls|"
    r"in\s+hand|"
    r"planets?|"
    r"interupts?\s+and\s+effects?|"
    r"starting\s+interupts?\s+and\s+effects?|"
    r"starship weapons?|"
    r"devices?\s*&\s*weapons?|"
    r"people|"
    r"ships?\s*&\s*vehicles?|"
    r"star\s+ships?|"
    r"epic\s+event'?s?|"
    r"intrupts?|"
    r"weopons?\s*/\s*devices?|"
    r"reserves?|"
    r"critters?|"
    r"sites?\s+and\s+planets?|"
    r"statops.*|"
    r"the\s+deck|"
    r"locations?\s+w/\s+parsec\s+numbers?|"
    r"admirals?'s?\s+orders?|"
    r"black\s+cards?|"
    r"sites?\s*/\s*planets?|"
    r"weapons?\s+and\s+devces?|"
    r"effects?\s+and\s+interrups?|"
    r"charakter|"
    r"locations?\s*/\s*planetes?|"
    r"characters?\s*\([^)]*\)|"
    r"destroyers?|"
    r"testing.*|"
    r"locations?\s*\(\s*\)|"
    r"senate|"
    r"under fear|"
    r"interrupts?\s+effects?|"
    r"droids?\s*&?\s*vehicles?|"
    r"charters?|"
    r"\bchars\b|"
    r"\bints\b|"
    r"under auaof|"
    r"auaof|"
    r"in hand|"
    r"hb marker swap|"
    r"kessel\s*/\s*kiffex\s+hb\s+system|"
    r"creatures?\s*/\s*ao\s*/\s*devices?|"
    r"isb agents|"
    r"fighting characters|"
    r"docking bays|"
    r"loactions|"
    r"battling|"
    r"musicians|"
    r"other characters|"
    r"under fima|"
    r"ralltiir\s+hb\s+system|"
    r"third effect|"
    r"weapons?\s*\(\s*\d+\s+cards?\)|"
    r"devices?\s*\(\s*\d+\s+cards?\)|"
    r"locations?\s*\(\s*\d+\s+cards?\)|"
    r"effects?\s*\(\s*\d+\s+cards?\)|"
    r"interrupts?\s*\(\s*\d+\s+cards?\)|"
    r"deck"
    r")"
    r"\s*[:.\-–—/>;]*\s*"
    r"(?:[\(\[]?\s*[xX]?\s*\d+(?:\s*,\s*\d+\s+\w+)?\s*[\)\]]?)?"
    r"\s*[:.\-–—*;]*\s*$",
    re.I,
)
SKIP_LINE_RE = re.compile(
    r"^(?:(?:\d+\s+)?side cards|10 side cards|fear\s*$|(?:\d+\s+)?side board|"
    r"and \d+ defensive s|"
    r"-?\d+\s+shields?(?:\s+that.*)?"
    r"|10 shields|"
    r"shields\s*-?\s*\d+|"
    r"and shields|"
    r"remember to use|does not count|besides above|"
    r"\(this depends on opponent.*\)|\(\*=always\)|"
    r"\(effect to be named later\)|"
    r"or none of those effects|-{3,}|"
    r".*fitting in current meta|"
    r"--?your choice.*|"
    r"just make ['’]?em good|"
    r"hb\s*\(indicator\)|"
    r"hb\s*indicator|"
    r"choose yer fav|"
    r"effect/side deck.*|"
    r"hidden base\(system\)|"
    r"\[(?:starting cards|decklist)\]|"
    r"!+.*don.?t know what to add.*|"
    r"\[insert \d+ shields|"
    r"def shields?\.\.+|"
    r"copied from card game organizer|"
    r"https?://\s*www\.angelfire|"
    r"deck name\s*:.*|"
    r"6 other shields of your choice|"
    r"the other \d+ can be whatever|"
    r"defensiver shields|"
    r"any other \d+ doesn.?t matter.*|"
    r"a bunch|"
    r"\[version[^\]]*\]|"
    r"usual start|"
    r"stuff\s*:?\s*\d*|"
    r"asdf|"
    r"deck fire|"
    r"x{6,}|"
    r".*card that lets me stack a destiny|"
    r"racers|"
    r"all the e1 shields.*|"
    r"interrupts?\s*\(\s*\)|"
    r"dshields:?|"
    r"\+\s*\(\s*\d+\s+sh(?:ie|ei)lds?\s*\)|"
    r"thank you|"
    r"your ship\??|"
    r"tatooine:\s*jawa pass|"
    r"hidden base system|"
    r"dfdaf|shgggshghs|"
    r"^req\.?$|"
    r"^flagship$|"
    r"sideboard options:.*|"
    r"any persona of jabba|"
    r"any darth with lightsaber|"
    r"any bossk persona or sarlaac|"
    r"any hologram cards|"
    r"its supposed to be fun|"
    r"ya im gonna lose|"
    r"master of the force|"
    r"^56$|"
    r"a brief rundown|"
    r"(?:\d+x?\s+)?to be named later|"
    r"(?:\d+\s+)?shields\s*-?\s*pick your favs|"
    r"(?:\d+x?\s+)?dark hate|"
    r"gasp, no starting.*|"
    r"indicates new stuff|"
    r"dagobah:\s*any site will do|"
    r"give or take a few\.?|"
    r"thingy|"
    r"red cards?\s*/\s*\*?aos?:?|"
    r"ps will add a dark deck.*|"
    r"shields\s+fanfare|"
    r"draw six more cards.*|"
    r"table|"
    r"hand|"
    r"these are in alphabetical order|"
    r"total cards:?\s*\d*|"
    r"total:?\s*\d*|"
    r"last slot:?|"
    r"average destiny.*|"
    r"light jawa deck|"
    r"x-wing deck|"
    r"jabba's new bodyguards|"
    r"slots\s+for\s+characters|"
    r"hidden base\s*=\s*your choice|"
    r"capture the falcon|"
    r"(?:\d+\s*[xX]\s+)?assorted darth vaders|"
    r"edit note:.*|"
    r"army droid|"
    r"jango fett|"
    r"dengars advanced weapon thingy|"
    r"take out the duplicates.*|"
    r"!+\s*objective.*|"
    r"system of choice under hb|"
    r"any system parsec.*|"
    r"^a jedi's$|"
    r"destiny stats;.*|"
    r"total[;:].*|"
    r"(?:\d+\+)+\d+=\d+|"
    r"hb marker|"
    r"rebel pilots?|"
    r"^\d{1,2}$|"
    r"assorted nonunique starfighters|"
    r"classic form deck|"
    r"interchangeable cards.*|"
    r"[-–—*]*\s*optional/?interchangeable.*|"
    r"any matching blaster.*|"
    r"any system(?:,|\s+parsec).*|"
    r"standard deck style|"
    r"^\d+/\d+$|"
    r"p-60 or p-59|"
    r"all my star destroyers.*|"
    r"and one more effect of your choice.*|"
    r"reveal rr.?uruurrr or ur.?ru.?r for your rep.*|"
    r"^red 4$|"
    r"ewok rescue|"
    r"and admiral'?s?\s+orders?|"
    r"and one more effect|"
    r"one more effect|"
    r"^either$|"
    r"and effects?|"
    r"^catman421$|"
    r"gpn sw ccg dicussion board moderator|"
    r"^obsidian 1$|"
    r"^hb system$|"
    r"check\s*:.*|"
    r"any version of jabba|"
    r"reveal\s+rep.*|"
    r"^updates?$|"
    r"^remove:?$|"
    r"^add:?$|"
    r"\d+\s+def\s+shields?|"
    r"^rest of the cards:?$|"
    r"^#\s*name$|"
    r"^type\s*#\s*name$|"
    r"possible hidden bases:?|"
    r"^\[(?:locations|starships|creatures|effects|characters|interrupts|starting)\]$|"
    r"^0\s+(?:sites?|characters?|starships?|effects?|locations?|weapons?|vehicles?|interrupts?)\s*$|"
    r"jp alien that adds to drains|"
    r"please rate this update.*|"
    r"i think i may need some more locations.*|"
    r"(?:\d+\s+)?destiny\s+card'?s?.*|"
    r"any effect'?s?\s+weapon'?s?\s+or\s+interrupt'?s?.*|"
    r"total card count.*|"
    r"number check:.*|"
    r"in\s+hand\s+due\s+to.*|"
    r"system parsec.*|"
    r"other cards i want to get.*|"
    r"^or$|"
    r"just about the same as any other.*|"
    r"just got another copy of.*|"
    r"note:\s*i do know that there are virtuals.*|"
    r".*and other:?\s*\)?\s*$|"
    r"statops.*|"
    r"see bounty hunter cult|"
    r"more anti-retreival stuff|"
    r"blizzard 1 and general veers|"
    r"classic shields|"
    r"marker\s*\(\s*usually|"
    r"^marker$|"
    r"hidden\s+base\"?\s*system.*|"
    r"cobined attack|"
    r"combined attack|"
    r"ds-61-1$|"
    r"hidden base marker|"
    r"wh+a+o+w!?|"
    r"card i need to get|"
    r"^x$|"
    r"^ep1$|"
    r"this deck is 4 cards over.*|"
    r"i need help eliminating extras|"
    r"i might want to add another docking bay.*|"
    r"one other effect see below|"
    r"\*?=?\s*strat notes?|"
    r"cards i.?m .*trying.* to fit in.*|"
    r"some cards that i want to add.*|"
    r".*any suggestions for shields.*|"
    r"normal shields|"
    r"hb marker(?:\s*\(.*)?$|"
    r"kessel\s*/\s*kiffex\s+hb\s+system|"
    r"^bld$|"
    r"number\s+type\s+name|"
    r"star wars:\s*ccg|"
    r"light side yavin \d+ deck|"
    r"hidden base indicator|"
    r"cards i would put in if i had them.*|"
    r"cards i.?d like to add in.*|"
    r"sos for master luke.*|"
    r"master qui for qui-gon jinn.*|"
    r"dos for leia.*|"
    r"obi,?\s*padawan for ben kenobi.*|"
    r"etc\b.*|"
    r"all six jedi tests|"
    r"shields?\s*\(including.*|"
    r"oddball(?:\s*-\s*\d+)?$|"
    r"\+)$",
    re.I,
)
NOTE_RE = re.compile(
    r"besides above|none of those effects|amnecessary|"
    r"depends on opponent|should i even try|"
    r"and 10 defensive s|10 defensive sheilds|"
    r"shields that i.?m not going to list|"
    r"effect to be named later|^shields?\s*:\s*\d+|"
    r"insert \d+ shields that meta|"
    r"copied from card game organizer|angelfire\.com|"
    r"remember, i just put this together|im me on aim|"
    r"6 other shields of your choice|the other \d+ can be whatever|"
    r"on the docking bays, i know|with whatever 10 shields|"
    r"with 10 shields of your choice|please give me|"
    r"doesn.?t matter all to much",
    re.I,
)
QTY_XFIRST = re.compile(r"^[xX](\d+)\s*(.+)$")
QTY_PAREN_X = re.compile(r"^(.*?)[\(\[]\s*[xX]\s*(\d+)\s*[\)\]]$")
QTY_PAREN_NX = re.compile(r"^(.*?)[\(\[]\s*(\d+)\s*[xX]\s*[\)\]]$")
QTY_TAIL_NX = re.compile(r"^(.*?)\s+(\d+)\s*[xX]$")
HEADER_PREFIX_RE = re.compile(
    r"^(?:starting(?:\s+(?:objective|effects?|interrupts?|cards?|location))?|objectives?|"
    r"obj\.?|ob|"
    r"epic events?|"
    r"locations?|"
    r"sites?|effects?|interrupts?|interupts|characters?|charactures?|charaters?|charactors?|charachters?|"
    r"starships?|ships?|vehicles?|veichles?|weapons?|systems?|devices?|"
    r"reserve deck|dark side|light side)\s*:\s+",
    re.I,
)
TYPE_QTY_NAME_RE = re.compile(
    r"^(?:starting\s+)?"
    r"(?:obj(?:ective|\.)?|locations?|sites?|interrupts?|"
    r"e\.|epic events?|characters?|starships?|starship|"
    r"effects?|devices?|device|weapons?|weapon|jedi tests?)\s+"
    r"(\d+)\s+(.+)$",
    re.I,
)
QTY_TYPE_NAME_RE = re.compile(
    r"^(\d+)\s+"
    r"(?:starting\s+)?"
    r"(?:obj(?:ective|\.)?|locations?|sites?|starting interrupts?|"
    r"starting effects?|immediate effects?|interrupts?|epic events?|"
    r"characters?|starships?|starship|effects?|devices?|device|"
    r"weapons?|weapon|jedi tests?|admiral'?s orders?)\s+"
    r"(.+)$",
    re.I,
)
SIDE_DECK_RE = re.compile(
    r"^(?:[-–—*]*\s*optional/?interchangeable.*|"
    r"deck\s*2\s*\(\s*light.*|"
    r"optional\s+sideboard(?:\s+cards?)?|"
    r"(?:starting\s+effects?\s*&\s*shields|"
    r"starting\s+effect.*/)?(?:side deck|def\s*sheilds|def\s*shields|"
    r"defensive sheilds?|defensive shied|defensive shields?|def shields?|"
    r"d-shields|fear is my ally cards|shields\s*-?\s*\d*))\b",
    re.I,
)
PLANET_RE = re.compile(
    r"^(tatooine|jabba's place|jabba's palace|naboo|endor|hoth|dagobah|coruscant)\s*:\s*$",
    re.I,
)
QTY_LEAD = re.compile(r"^(\d+)\s*[xX]\s+(.*)$")
QTY_FRONT = re.compile(r"^(\d+)\s+(?![xX]\s)(.+)$")
QTY_TAIL = re.compile(r"^(.*?)\s+[xX]\s*(\d+)$")
QTY_STAR = re.compile(r"^(.*?)\s*\\?\*\s*(\d+)(\s*\(V\))?$")
QTY_GLUE = re.compile(r"^(.*[^\s])[xX](\d+)$")
QTY_PAREN = re.compile(r"^(.*?)[\(\[](\d+)[\)\]]$")
VIRTUAL_MARK_RE = re.compile(r"(?i)\b(?:v|vsc|virtual|v-card)\b")
SET_PAREN_RE = re.compile(
    r"\s*\(\s*(?:"
    r"Premiere|Premier|PRE|A New Hope|ANH|Hoth|Dagobah|Dag|DAG|DEGO|Cloud City|CC|"
    r"Jabba'?s Palace|JP|Special Edition|SPEC|"
    r"Endor|END|Death Star II|DS II|DS2|DSII|Tatooine|TAT|"
    r"Coruscant|CORU|COR|Theed Palace|THEED|"
    r"Reflections(?: II| III)?|REFII|REFIII|REF\s*II|REF\s*III|"
    r"Enhanced Premiere|ENPRE|ENPREMIERE|Enhanced Cloud City|ENCC|ENC|"
    r"Prem|"
    r"Enhanced Jabba'?s Palace|ENJP|JABA|Jedi Pack|"
    r"sped|"
    r"Third Anthology|3ANTH|3\s*Anth|"
    r"vehicle|ep\.?\s*1|episode\s*1|episode\s+one"
    r")\s*\)\s*$",
    re.I,
)
SHIP_PILOT_SPLIT = [
    (
        re.compile(r"(?i)^Virago\s+Zuck?h?uss In Mist Hunter$"),
        "Virago",
        "Zuckuss In Mist Hunter",
    ),
    (re.compile(r"(?i)^Saber 1\s*/\s*Baron.*$"), "Saber 1", "Baron Soontir Fel"),
    (re.compile(r"(?i)^Saber 2\s*/\s*Major Phoenirr$"), "Saber 2", "Major Turr Phennir"),
    (re.compile(r"(?i)^Saber 3\s*/\s*DS-181-3$"), "Saber 3", "DS-181-3"),
    (re.compile(r"(?i)^Saber 4\s*/\s*DS-181-4$"), "Saber 4", "DS-181-4"),
    (re.compile(r"(?i)^Onyx 1\s*/\s*Colonel Jendon$"), "Onyx 1", "Colonel Jendon"),
    (re.compile(r"(?i)^Colonel Jendon\s*/\s*Onyx\s*1$"), "Colonel Jendon", "Onyx 1"),
    (re.compile(r"(?i)^Captain Yorr\s*/\s*Onyx\s*2$"), "Captain Yorr", "Onyx 2"),
    (re.compile(r"(?i)^Guri\s*/\s*Stinger$"), "Guri", "Stinger"),
    (re.compile(r"(?i)^Lieutenant Hebsly\s*/\s*Scythe\s*1$"), "Lieutenant Hebsly", "Scythe 1"),
    (re.compile(r"(?i)^Major Mianda\s*/\s*Scythe\s*3$"), "Major Mianda", "Scythe 3"),
    (re.compile(r"(?i)^Baron Soontir Fel\s*/\s*Saber\s*1$"), "Baron Soontir Fel", "Saber 1"),
    (re.compile(r"(?i)^Major Turr Phennir\s*/\s*Saber\s*2$"), "Major Turr Phennir", "Saber 2"),
    (re.compile(r"(?i)^Prince Xizor\s*/\s*Virago$"), "Prince Xizor", "Virago"),
    (re.compile(r"(?i)^Black 2\s*/\s*DS-61-2$"), "Black 2", "DS-61-2"),
    (re.compile(r"(?i)^Slave 1\s*/\s*Boba Fett$"), "Slave I", "Boba Fett"),
    (re.compile(r"(?i)^Bespin Cloud City$"), "Bespin", "Cloud City"),
    (
        re.compile(r"(?i)^Endor and Rebel Landing Site$"),
        "Endor",
        "Endor: Rebel Landing Site (Forest)",
    ),
    (
        re.compile(
            r"(?i)^Cloud city Carbonite chamber w/\s*Console$"
        ),
        "Cloud City: Carbonite Chamber",
        "Carbonite Chamber Console",
    ),
    (
        re.compile(r"(?i)^Bacta Tank Bargaining Table$"),
        "Bacta Tank",
        "Bargaining Table",
    ),
]


def _strip_long_paren(name: str, min_len: int) -> str:
    m = re.search(rf"\s*\(([^)]{{{min_len},}})\)\s*$", name)
    if not m:
        return name
    if VIRTUAL_MARK_RE.search(m.group(1)):
        return name
    return name[: m.start()].rstrip()


def clean_name(name: str) -> str:
    name = htmlmod.unescape(name)
    name = name.replace("\xa0", " ").replace("\\", "/")
    name = name.replace("\u2019", "'").replace("\u2018", "'").replace("`", "'")
    name = name.replace("\x92", "'").replace("\ufffd", "'")
    name = name.replace("â€™", "'").replace("â€˜", "'").replace("âs", "'s")
    name = name.replace("¡¦", "'").replace("\xa1\xa6", "'")
    name = re.sub(r"<>\s*proxying\s+.*", "", name, flags=re.I)
    name = re.sub(r"<?\s*proxying\s+.*", "", name, flags=re.I)
    name = re.sub(r"[<>]+", " ", name)
    name = re.sub(r"(?<=[A-Za-z])\?(?=[A-Za-z])", "'", name)
    name = re.sub(r"\?(?=s(?:\s|$))", "'", name)
    name = name.replace("\u00b4", "'").replace("\u00b4", "'").replace("´", "'")
    name = name.replace("\ufeff", "")
    name = name.replace("\u201c", '"').replace("\u201d", '"')
    name = re.sub(r"<[^>]+>", "", name)
    name = re.sub(r"^[\u00b7·•*<>\"\s]+", "", name)
    name = re.sub(r"\*+$", "", name)
    if re.match(r"^\(\s*v\s*\)\s*", name, re.I):
        name = re.sub(r"^\(\s*v\s*\)\s*", "", name, flags=re.I).strip()
        if not re.search(r"\(V\)\s*$", name):
            name = name + " (V)"
    name = re.sub(
        r"^(objective|req|starting interrupt|starting effects?|starting)\s*[-–—:]?\s+",
        "",
        name,
        flags=re.I,
    )
    name = re.sub(r"^\(\s*cc\s*\)\s*", "", name, flags=re.I)
    name = re.sub(r"^D:\s*", "Dagobah: ", name, flags=re.I)
    name = re.sub(r"^N:\s*", "Naboo: ", name, flags=re.I)
    name = re.sub(r"^CC:\s*", "Cloud City: ", name, flags=re.I)
    name = re.sub(r"^Tat:\s*", "Tatooine: ", name, flags=re.I)
    name = re.sub(r"^Tatoine:\s*", "Tatooine: ", name, flags=re.I)
    name = re.sub(r"^JP:\s*", "Jabba's Palace: ", name, flags=re.I)
    name = re.sub(r"^Cor:\s*", "Coruscant: ", name, flags=re.I)
    name = re.sub(r"^Ex:\s*", "Executor: ", name, flags=re.I)
    name = re.sub(r"^B:\s*", "Bespin: ", name, flags=re.I)
    name = re.sub(r"^Dag:\s*", "Dagobah: ", name, flags=re.I)
    name = re.sub(r"^D\*2:\s*", "Death Star II: ", name, flags=re.I)
    name = re.sub(r"^D\*:\s*", "Death Star: ", name, flags=re.I)
    name = re.sub(r"^Y4:\s*", "Yavin 4: ", name, flags=re.I)
    name = re.sub(r"^End:\s*", "Endor: ", name, flags=re.I)
    name = re.sub(r"^JSB:\s*", "Jabba's Sail Barge: ", name, flags=re.I)
    name = re.sub(r"\s*\(\s*Epic Event\s*\)\s*$", "", name, flags=re.I)
    name = re.sub(r"\s*\(\s*1\s+icon\s*\)\s*$", "", name, flags=re.I)
    name = re.sub(r"\s*\(\s*\d-\d\s+version\s*\)\s*$", "", name, flags=re.I)
    name = re.sub(r"\s*\(\s*versus\b.*", "", name, flags=re.I)
    name = re.sub(r"\s*\(\s*does not cancel[^)]*\)", "", name, flags=re.I)
    name = re.sub(r"\s*\(\s*get some devices\s*\)", "", name, flags=re.I)
    name = re.sub(r"\s*\(\s*test\s+\d+\s*\)", "", name, flags=re.I)
    name = re.sub(r"\s*\(\s*AO\s*\)\s*$", "", name, flags=re.I)
    name = re.sub(r"\s*\(\s*I GOT ONE!?\s*\)\s*$", "", name, flags=re.I)
    name = re.sub(r"\s*\(\s*pull d-bays\s*\)\s*$", "", name, flags=re.I)
    name = re.sub(r"\s*\(\s*can't find anyone[^)]*\)\s*$", "", name, flags=re.I)
    name = re.sub(r"\s*-{2,}that's.*$", "", name, flags=re.I)
    name = re.sub(r"\s*\(\s*AI Foil\)\s*$", "", name, flags=re.I)
    name = re.sub(r"^ProjectionOf\s+", "Projection Of ", name, flags=re.I)
    name = re.sub(r"\?([^?]{2,24})\?", r'"\1"', name)
    name = re.sub(r"\s*\(\s*I'm Sorry\s*\)\s*$", "", name, flags=re.I)
    name = re.sub(r"\s*\(\s*Ref\s*3\s*\)\s*$", "", name, flags=re.I)
    name = re.sub(r"\s*\(\s*pullable[^)]*\)\s*$", "", name, flags=re.I)
    name = re.sub(r"\s*\(ENCC0?\s*$", "", name, flags=re.I)
    name = re.sub(r"\s*\(\s*one is base\s*\)\s*$", "", name, flags=re.I)
    name = re.sub(r"\s*\(\s*any\s*\)\s*$", "", name, flags=re.I)
    name = re.sub(r"\s*\(\s*(?:Gold|Gray Squadron)\s+\d+\s*\)\s*$", "", name, flags=re.I)
    name = re.sub(r"\s*\(\s*non-virtual\s*\)\s*$", "", name, flags=re.I)
    name = re.sub(r"\s*\(\s*(?:LS|Rep|db)\s*\)\s*$", "", name, flags=re.I)
    name = re.sub(r"\s*\(\s*(?:\d+\s+)?(?:DH|CF)\s*\)\s*$", "", name, flags=re.I)
    name = re.sub(r"\s*\(\s*x\s*\d+\s+if\s+rep\s*\)\s*$", "", name, flags=re.I)
    name = re.sub(r"\s*\(\s*forest\s*\)\s*$", "", name, flags=re.I)
    name = re.sub(r"\s*/\s*no flip\s*$", "", name, flags=re.I)
    name = re.sub(r"(?i)^\*{0,5}DS\*{2,}\s*", "", name)
    name = SET_PAREN_RE.sub("", name)
    name = re.sub(r"(?<=[A-Za-z])\+(?=[A-Za-z])", " & ", name)
    name = re.sub(r"(?i)\s+virtual$", " (V)", name)
    name = re.sub(r"\s+", " ", name).strip(" -.,;:")
    name = re.sub(
        r"\s*\((?:VSC|V-?Card(?: version)?|Virtual(?: Card!?)?(?: version)?)\)\s*$",
        " (V)",
        name,
        flags=re.I,
    )
    name = re.sub(
        r"\s*\((?:spy|undercover spy)\)\s*$",
        "",
        name,
        flags=re.I,
    )
    name = _strip_long_paren(name, 15)
    name = re.sub(
        r"\s*\((?:S|C|U|R|P|R2|R3|RIII|AI|EP1|CC|EJP|SE|usually|alt start|"
        r"Marker|political effect|start|starting|10 defensive shields|"
        r"Pull one of my lightsabers|rep is [^)]+|don't have[^)]+|only for [^)]+|"
        r"only 1 of the good kind|start v [^)]+|Shield|Ep\.?1|\?|S\.?I\.?|not starting)\)\s*$",
        "",
        name,
        flags=re.I,
    )
    name = re.sub(r"\s*\(Marker\)\s*$", "", name, flags=re.I)
    name = re.sub(r"\s*\(only if needed\)\s*$", "", name, flags=re.I)
    name = re.sub(r"\s*\(if needed\)\s*$", "", name, flags=re.I)
    name = re.sub(r"\s*\((?:one starts?|start|starting)\)\s*$", "", name, flags=re.I)
    name = re.sub(r"&([A-Za-z][^&;]{1,40});", r" & \1", name)
    name = re.sub(r"(?<=[a-z])&(?=[A-Za-z])", " & ", name)
    name = re.sub(r"\s*:\s*", ": ", name)
    name = re.sub(r":(\S)", r": \1", name)
    name = re.sub(r",(\S)", r", \1", name)
    name = re.sub(r"([^\s])\(", r"\1 (", name)
    name = re.sub(r"\s*\(\s*pilot\s*\)\s*$", "", name, flags=re.I)
    name = re.sub(r"\s*\(\s*(?:ground|space|anywhere)\s*\)\s*$", "", name, flags=re.I)
    name = re.sub(r"\s*\(\s*guess\s*\)\s*$", "", name, flags=re.I)
    name = re.sub(r"\s*\(\s*for\s+[^)]+\)\s*$", "", name, flags=re.I)
    name = re.sub(r"\s+aka\s+.*?(?=\s*\(V\)\s*$|$)", "", name, flags=re.I)
    name = re.sub(r"\s*\(\s*(?:Gold|Gray Squadron)\s+\d+\s*\)\s*$", "", name, flags=re.I)
    name = re.sub(r"\s*(?:\.\.\.|\u2026)(?:\s*\(.*\))?$", "", name)
    name = re.sub(r"['.\u2026\ufffd]+(?:\s*\(.*\))?$", "", name)
    name = re.sub(r"(?i)\s+objective$", "", name)
    name = name.strip(" -.,;:")
    if name in GPN_ALIAS:
        return GPN_ALIAS[name]
    key = name.casefold()
    for a, b in GPN_ALIAS.items():
        ak = a.replace("\u2019", "'").replace("\u2018", "'").replace("`", "'").casefold()
        if ak == key:
            return b
    return name


def parse_qty_line(line: str) -> tuple[int, str] | None:
    line = htmlmod.unescape(line)
    line = re.sub(r"<[^>]+>", "", line)
    line = re.sub(r"\s{2,}\d{1,2}\s*$", "", line)
    line = re.sub(r"\s+", " ", line).strip()
    if re.search(r"(?i)dagobah:\s*swamp\s+or\s+dagobah:\s*bog\s+clearing", line):
        if re.search(r"(?i)whichever", line):
            return 1, "Dagobah: Bog Clearing"
        return 1, "Dagobah: Swamp"
    line = re.sub(r"\s*\(\s*pullable[^)]*\)\s*$", "", line, flags=re.I)
    line = re.sub(r"\s*\[s\]\s*", " ", line, flags=re.I)
    line = re.sub(r"\s*\[v\]\s*", " (V) ", line, flags=re.I)
    line = re.sub(r"\s*\[[^\]]{1,24}\]\s*", " ", line)
    line = re.sub(r"\s*\(\s*trade\s*\)\s*", " ", line, flags=re.I)
    line = re.sub(r"\s+trade\s*$", "", line, flags=re.I)
    line = re.sub(r"\s+", " ", line).strip()
    line = re.sub(r"(?<=[A-Za-z])\s+(1[3-9]|[2-9]\d)\s*$", "", line)
    line = re.sub(r"^[\u00b7·•*]+\s*", "", line)
    line = re.sub(r"^\d+\.\s+", "", line)
    line = re.sub(r"(?i)^(?:\d+\s*[xX]\s+)?\*{0,5}DS\*{2,}\s*", "", line)
    line = SET_PAREN_RE.sub("", line)
    if re.fullmatch(r"[\d+\s=]+", line):
        return None
    line = re.sub(r"(\*\s*\d+)\s+\d{1,2}\s*$", r"\1", line)
    line = re.sub(
        r"\s+(?:and|w/?|with)\s*(?:\d+|ten)\s+(?:defensive\s+)?sh(?:ie|ei)lds?(?:\s*\([^)]*\))?\s*$",
        "",
        line,
        flags=re.I,
    )
    line = re.sub(r"\s+w/\s*:?\s*$", "", line, flags=re.I)
    line = re.sub(r"\s*\+\s*DS\s*$", "", line, flags=re.I)
    line = re.sub(r"\*+$", "", line).strip()
    line = re.sub(
        r"(?i)^((?:\d+\s*[xX]\s+)?)(An Unusual Amm?ount of Fear|An Usual Amount of Fear|An Unsuals Amunt Of Fear|An Unsual Amount of Fear|Unusual Amou?nt of Fear|Fear Is My Ally)\s*(?:\+|w/?|\().*",
        r"\1\2",
        line,
    )
    line = re.sub(
        r"(?i)^((?:\d+\s*[xX]\s+)?)(An Unusual Amm?ount of Fear|An Usual Amount of Fear|An Unsuals Amunt Of Fear|An Unsual Amount of Fear|Unusual Amou?nt of Fear|Fear Is My Ally)\s*[xX]\s*\d+\s*(?:\+|()).*",
        r"\1\2",
        line,
    )
    line = re.sub(
        r"(?i)^((?:\d+\s*[xX]\s+)?)(An Unusual Amm?ount of Fear|An Usual Amount of Fear|An Unsuals Amunt Of Fear|An Unsual Amount of Fear|Unusual Amou?nt of Fear|Fear Is My Ally)\s*[xX]\s*\d+\s+sh(?:ie|ei)lds?.*",
        r"\1\2",
        line,
    )
    line = re.sub(
        r"\s*\((?:S|C|U|R|P|R2|R3|RIII|AI|SI|SE|SL|Tech|rep|always S|Marker|"
        r"one starts?|start|starting|usually|alt start|in hand|shiny|WHAP|"
        r"premiere|premire|premiere version|old|NEW|R3\s+ver|Shield|Ep\.?1|"
        r"S\.?I\.?|not starting|non-V)\)\s*$",
        "",
        line,
        flags=re.I,
    )
    line = re.sub(r"\s*\(\s*r\s*\d+\s+versions?\s*\)\s*$", "", line, flags=re.I)
    line = re.sub(
        r"\s*\((?:VSC|V-?Card(?: version)?|Virtual(?: Card!?)?(?: version)?)\)\s*$",
        " (V)",
        line,
        flags=re.I,
    )
    line = re.sub(r"\s*\(\s*v\s*\d+\s*,[^)]*\)", " (V)", line, flags=re.I)
    line = re.sub(r"\s*\(\s*v\s*\d+\s*,.*$", " (V)", line, flags=re.I)
    line = re.sub(r"\s*\(\s*v\s*\d+\s*\)", " (V)", line, flags=re.I)
    line = re.sub(r"\s*\(\s*v\s*\)", " (V)", line, flags=re.I)
    line = re.sub(r"\s*\[V(?:C)?\]\s*$", " (V)", line, flags=re.I)
    line = re.sub(r"\s*\(\s*vc\s*\)\s*$", " (V)", line, flags=re.I)
    line = re.sub(r"\s*\+\s*\d+\s+(?:defensive\s+)?shields?\s*$", "", line, flags=re.I)
    line = re.sub(
        r"\s*\+\s*(?:any\s+)?(?:def\.?\s*)?shields?\s*$",
        "",
        line,
        flags=re.I,
    )
    line = re.sub(r"\s+with\s+\d+\s+defensive\s+shields?\s*$", "", line, flags=re.I)
    line = re.sub(r"\s*[-–—]\s*\d+\s+sh(?:ie|ei)lds?\s*-?\s*$", "", line, flags=re.I)
    line = re.sub(r"\s*\(\s*\d+\s+sh(?:ie|ei)lds?\s*\)\s*$", "", line, flags=re.I)
    line = re.sub(r"\s*\(\d+\s+shields?,.*$", "", line, flags=re.I)
    line = re.sub(r"\s*\((?:recycles|w/\s*shields)\)\s*$", "", line, flags=re.I)
    line = re.sub(r"\s+w/\s*sh(?:ie|ei)lds?\s*$", "", line, flags=re.I)
    line = re.sub(r"(?i)\s+V$", " (V)", line)
    line = re.sub(r"\s*\((?:NEW|OUT)\s+\d+/\d+/\d+\)\s*$", "", line, flags=re.I)
    line = re.sub(r"\s*\((?:Starting)\)\s*$", "", line, flags=re.I)
    line = re.sub(r"\s*\(\s*Start(?:ing)?\s*\)", "", line, flags=re.I)
    line = re.sub(r"([xX]\d+)\s+\d+(?:/\d+)?\s*$", r"\1", line)
    line = re.sub(r"<+$", "", line).strip()
    line = re.sub(r"\s*\(\s*system\s*\)\s*$", "", line, flags=re.I)
    line = re.sub(r"\s*\(\s*SE\s*\)\s*$", "", line, flags=re.I)
    line = re.sub(r"\s*\(\s*se\s*\)", " ", line, flags=re.I)
    line = re.sub(r"\s+", " ", line).strip()
    line = re.sub(r"\s+\d+/\d+\s*$", "", line)
    for _ in range(3):
        nxt = re.sub(
            r"\s*\((?:Sith|Ally|Vader'?s)[^)]*\)\s*$",
            "",
            line,
            flags=re.I,
        )
        if nxt == line:
            break
        line = nxt
    line = re.sub(r"\s*\(\s*huge\s*\)\s*$", "", line, flags=re.I)
    line = re.sub(
        r"\s*\((?:spy|undercover spy)\)\s*$",
        "",
        line,
        flags=re.I,
    )
    line = _strip_long_paren(line, 12)
    line = re.sub(r"\s*\(\s*destiny\s+\d+\s*\)\s*$", "", line, flags=re.I)
    line = re.sub(r"\s*\(\s*D\s*\d+\s*\)?\s*$", "", line, flags=re.I)
    line = re.sub(r"\s*\(\s*D\s*[@?]?\s*\)?\s*$", "", line, flags=re.I)
    line = re.sub(r"\s*\(\s*optional\s*\)\s*$", "", line, flags=re.I)
    line = re.sub(r"\s*\(\s*Tempest\s+\d+\s*\)\s*$", "", line, flags=re.I)
    line = re.sub(r"\s*\(\s*[0-7]\s*\)", "", line)
    line = re.sub(r"\s*\(\s*[0-7]\s*/\s*[0-7]\s*\)", "", line)
    line = re.sub(r"\s*\(\s*[0-7]\s+destiny!?\s*\)", "", line, flags=re.I)
    line = re.sub(r"\s*\(\s*(?:\d+\s+)?(?:DH|CF)\s*\)", "", line, flags=re.I)
    line = re.sub(r"\s*\(\s*x\s*\d+\s+if\s+rep\s*\)", "", line, flags=re.I)
    line = re.sub(
        r"\s*\+\s*the Effects of your choice from the Deck\s*$",
        "",
        line,
        flags=re.I,
    )
    if re.search(r"lightsaber|saber", line, re.I):
        line = re.sub(r"\s*\(\s*[1-7]\s*\)\s*$", "", line)
    mbr = re.match(r"^\[([^\]]+)\](?:\s*[-–—:.]?\s*\d+)?\s*$", line)
    if mbr:
        line = mbr.group(1).strip()
    line = re.sub(r"\s*\+\s*\d+\s*$", "", line)
    line = HEADER_PREFIX_RE.sub("", line).strip()
    m_type = TYPE_QTY_NAME_RE.match(line)
    if m_type and 1 <= int(m_type.group(1)) <= 40:
        return int(m_type.group(1)), clean_name(m_type.group(2))
    m_qtype = QTY_TYPE_NAME_RE.match(line)
    if m_qtype and 1 <= int(m_qtype.group(1)) <= 40:
        return int(m_qtype.group(1)), clean_name(m_qtype.group(2))
    if not line or line in {"Back to Top", "-"}:
        return None
    if re.fullmatch(r"[+\-–—*]+", line):
        return None
    if HEADER_RE.match(line):
        return None
    m_px = re.match(r"^\(\s*(\d+)\s*[xX]\s*\)\s*(.+)$", line)
    if m_px and 1 <= int(m_px.group(1)) <= 40:
        return int(m_px.group(1)), clean_name(m_px.group(2))
    m_px = re.match(r"^\(\s*[xX]\s*(\d+)\s*\)\s*(.+)$", line)
    if m_px and 1 <= int(m_px.group(1)) <= 40:
        return int(m_px.group(1)), clean_name(m_px.group(2))
    if re.match(r"^3,?720\s+to\s+1", line, re.I):
        m = QTY_TAIL.match(line) or QTY_PAREN.match(line)
        qty = int(m.group(2)) if m else 1
        return qty, "3,720 To 1"
    m = QTY_XFIRST.match(line)
    if m:
        return int(m.group(1)), clean_name(m.group(2))
    m = QTY_LEAD.match(line)
    if m:
        return int(m.group(1)), clean_name(m.group(2))
    m = QTY_FRONT.match(line)
    if (
        m
        and m.group(2).strip()
        and not m.group(2).startswith("http")
        and 1 <= int(m.group(1)) <= 20
    ):
        rest = m.group(2).strip()
        if re.match(r"^[\u2013\u2014\-–—]?\s*LOM\b", rest, re.I):
            return 1, clean_name("4-LOM EJP")
        return int(m.group(1)), clean_name(rest)
    m = QTY_STAR.match(line)
    if m and m.group(2).isdigit():
        name = (m.group(1) + (m.group(3) or "")).strip()
        return int(m.group(2)), clean_name(name)
    m = QTY_GLUE.match(line)
    if (
        m
        and m.group(2).isdigit()
        and 1 <= int(m.group(2)) <= 20
        and not re.match(r"^[A-Z]-", m.group(1))
        and not m.group(1).endswith("-")
    ):
        return int(m.group(2)), clean_name(m.group(1))
    m = re.match(r"^(.*?)\s+[xX]\s*(\d+)\s*\(V\)\s*$", line)
    if m and m.group(1).strip() and 1 <= int(m.group(2)) <= 20:
        return int(m.group(2)), clean_name(m.group(1) + " (V)")
    m = re.match(r"^(.*[^\s\d])[xX](\d+)\s*\(V\)\s*$", line)
    if (
        m
        and m.group(1).strip()
        and 1 <= int(m.group(2)) <= 20
        and not m.group(1).endswith("-")
    ):
        return int(m.group(2)), clean_name(m.group(1) + " (V)")
    m = QTY_TAIL_NX.match(line)
    if m and m.group(1).strip() and 1 <= int(m.group(2)) <= 20:
        return int(m.group(2)), clean_name(m.group(1))
    m = QTY_TAIL.match(line)
    if m and m.group(1).strip():
        return int(m.group(2)), clean_name(m.group(1))
    m = QTY_PAREN_X.match(line)
    if m and m.group(1).strip() and 1 <= int(m.group(2)) <= 20:
        return int(m.group(2)), clean_name(m.group(1))
    m = QTY_PAREN_NX.match(line)
    if m and m.group(1).strip() and 1 <= int(m.group(2)) <= 20:
        return int(m.group(2)), clean_name(m.group(1))
    m = QTY_PAREN.match(line)
    if m and m.group(1).strip() and not re.search(r"(Marker|political|defensive\s+shield)", m.group(0), re.I):
        left = clean_name(m.group(1))
        if HEADER_RE.match(left):
            return None
        return int(m.group(2)), left
    m = re.match(r"^(.*[A-Za-z]{4}.*)-([1-9]|1[0-9]|20)$", line)
    if m:
        return int(m.group(2)), clean_name(m.group(1))
    return 1, clean_name(line)


def section_text(html: str, start_pat: str, end_pats: list[str]) -> str:
    m = re.search(start_pat, html, re.I | re.S)
    if not m:
        return ""
    rest = html[m.end() :]
    ends = [len(rest)]
    for p in end_pats:
        em = re.search(p, rest, re.I | re.S)
        if em:
            ends.append(em.start())
    return rest[: min(ends)]


def parse_deck_html(path: Path) -> dict:
    raw = path.read_bytes()
    html = raw.decode("utf-8", "replace")
    if "�" in html:
        html = raw.decode("cp1252", "replace")
    title_m = re.search(r'class="pageTitle">\s*([^<]+?)\s*<', html, re.I | re.S)
    if not title_m:
        title_m = re.search(r"<b>([^<]+)</b>\s*</td></tr></table>\s*<table", html, re.I | re.S)
    title = htmlmod.unescape(title_m.group(1)).strip() if title_m else path.stem
    title = re.sub(r"\s+", " ", title)
    auth_m = re.search(r"profile\.asp\?id=([^\"'&]+)", html, re.I)
    author = htmlmod.unescape(urllib_unquote(auth_m.group(1))) if auth_m else "Unknown"
    author = author.replace("+", " ").strip()
    date_m = re.search(r"Date Posted.*?</td>\s*<td[^>]*>\s*(\d{1,2}/\d{1,2}/\d{4})", html, re.I | re.S)
    posted = date_m.group(1) if date_m else ""
    cat_m = re.search(r"Categories.*?</td>\s*<td[^>]*>\s*([^<]+)", html, re.I | re.S)
    category = re.sub(r"\s+", " ", htmlmod.unescape(cat_m.group(1))).strip() if cat_m else "Standard"
    desc_html = section_text(
        html,
        r"<b>The Description</b>",
        [r"<b>The Deck</b>", r'id="the_deck"', r"The Strategy"],
    )
    desc = strip_html(desc_html)
    deck_html = section_text(
        html,
        r"<b>The Deck</b>",
        [r"<b>The Strategy</b>", r"The Last 5 Comments", r'id="the_strategy"'],
    )
    strat_html = section_text(
        html,
        r"<b>The Strategy</b>",
        [r"<b>The Last 5 Comments</b>", r'id="the_comments"', r"View More Comments"],
    )
    rows = parse_card_lines(deck_html)
    did = int(re.search(r"id-(\d+)", path.name).group(1))
    return {
        "id": did,
        "title": title,
        "author": author,
        "posted": posted,
        "category": category,
        "description": desc,
        "strategy": strip_html(strat_html),
        "deck_raw": strip_html(deck_html),
        "rows": rows,
        "qty": sum(q for q, _ in rows),
        "url": DETAIL_URL.format(id=did),
        "uncaptured": "GPN listing-only dest" in html,
    }


def urllib_unquote(s: str) -> str:
    import urllib.parse

    return urllib.parse.unquote_plus(s)


def strip_html(chunk: str) -> str:
    chunk = re.sub(r"<br\s*/?>", "\n", chunk, flags=re.I)
    chunk = re.sub(r"</p>", "\n", chunk, flags=re.I)
    chunk = re.sub(r"<[^>]+>", "", chunk)
    chunk = htmlmod.unescape(chunk)
    chunk = re.sub(r"[ \t]+\n", "\n", chunk)
    chunk = re.sub(r"\n{3,}", "\n\n", chunk)
    lines = []
    for ln in chunk.splitlines():
        t = ln.strip()
        if t in {"Back to Top", "The Deck", "The Strategy", "The Description"}:
            continue
        if t.startswith("Thank you") or t.startswith("David Jones") or t.startswith("Matthew ("):
            continue
        lines.append(t)
    return "\n".join(lines).strip()


PERSONA_TAIL_RE = re.compile(
    r"(?i)^(or do not|dark lord of the sith|ruler of the naboo|"
    r"ruler of naboo|red squadron leader|rsl|scoundrel|scoundral|protector|"
    r"bounty hunter|padawan learner|padiwan learner|jedi knight|jk|"
    r"jedi master|master of the force|protector of the queen|"
    r"rebel scout|young apprentice|rebel princess|the emperor's hand|"
    r"senior council member|you seek yoda|kid!?|huh\??|you big coward|"
    r"hero of the dune sea|enraged|padawan larner|red squaron leader|neimoidian viceroy|nemoidian viceroy|"
    r"motf|bravo leader|reb scout|potq)"
    r"(?:\s*[xX]\s*\d+(?:\s+\d+(?:/\d+)?)?|\s*\(\s*\d+\s*\)|\s+[1-9]\d?)?\s*$"
)
COMMA_KEEP_RE = re.compile(
    r"(?i)^(?:(?:\d+\s*[xX]\s+)|(?:[xX]\d+\s+)|(?:\d+\s+)|(?:[A-Za-z.]+\s+\d+\s+))?(?:\(\s*v\s*\)\s+)?(?:anger,\s*fear|great shot,\s*kid|yoda,\s*you seek|"
    r"we'll let fate-a decide|come here,\s*you big coward|"
    r"ability,\s*ability|my lord,\s*is that legal|"
    r"look\s+sir|"
    r"wipe them out,\s*all of them|"
    r"luke,\s*jk|"
    r"hear me baby,\s*hold together|"
    r"run luke,\s*run|"
    r"run,\s*luke|"
    r"either way,\s*you win|"
    r"oo-ta goo-ta,\s*solo|"
    r"panaka,\s*protector|"
    r"chewie,\s*enraged|"
    r"lando salrissian,\s*scoundrel|"
    r"obi[- ]?wan(?:\s+kenobi)?,\s*padawan|"
    r"wedge antilles,\s*red squa|"
    r"3,\s*720|"
    r"into the garbage chute,\s*flyboy|"
    r"into the ventilation shaft,\s*lefty|"
    r"do,\s*or do not|"
    r"lando,\s*calrissian|"
    r"no money,\s*no parts|"
    r"qui[- ]?gon(?:\s+jinn)?,\s*jedi master|"
    r"han,\s*chewie|"
    r"yoda,\s*master of the force|"
    r"mace windu,\s*jedi master|"
    r"obi[- ]?wan(?:\s+kenobi)?,\s*jedi knight|"
    r"luke skywalker,\s*jedi knight|"
    r"lando calrissian,\s*scoundrel|"
    r"leia,\s*rebel princess|"
    r"han,\s*chewie\s*(?:and|&|\+)\s*the\s*falcon|"
    r"han,\s*chewie\+falcon|"
    r"mara jade,\s*the|"
    r"bobo fett,\s*bh|"
    r"wedge antiles,\s*red squadron|"
    r"you.?re all clear,\s*kid|"
    r"darth vader,\s*dark lord|"
    r"darth vader,\s*darth lord|"
    r"oh,?\s*switch off|"
    r"executor,\s*(?:control|comm|main|holo|meditation|docking)|"
    r"ds,\s*(?:level|war|docking)|"
    r"yavin 4,\s*docking|"
    r"no money,\s*no part|"
    r"nute gunray,\s*neimodian|"
    r"nute gunray,\s*neimoidian|"
    r"nute gunray,\s*nemoidian|"
    r"location,\s*location|"
    r"wipe them out,\s*all out|"
    r"i will find them|"
    r"oota goo-ta,\s*solo|"
    r"rune haako,\s*legal|"
    r"oota goota,\s*solo|"
    r"lando calrissian,\s*scoundril|"
    r"darth vader,\s*dlofts|"
    r"wedge antil+es,\s*rsl|"
    r"iasa,\s*the traitor|"
    r"ob-?wan kenobi,\s*padawan|"
    r"dv,\s*dlots|"
    r"boba fett,\s*bh|"
    r"boba fett,\s*bounty hunter|"
    r"darth maul,\s*young apprentice|"
    r"lando calrissian,\s*scoundral|"
    r"i don.?t need ther?\s+scum|"
    r"no civility,\s*only politics|"
    r"r.?kik d.?nec,\s*hero|"
    r"h,\s*c|"
    r"yoda,\s*motf|"
    r"mara,\s*teh|"
    r"ric olie,\s*bravo|"
    r"lando,\s*scoundrel|"
    r"obi[- ]?wan,\s*pl|"
    r"luke skywalker,\s*reb|"
    r"panaka,\s*potq|"
    r"anger,\s*fear|"
    r"threepio,\s*naked|"
    r"asteroids do not concern|"
    r"boba fett,\s*bounty|"
    r"he's a man|"
    r"coruscant,\s*ep|"
    r"into the garbage|"
    r"jabba,\s*the hutt|"
    r"no money,\s*no parts|"
    r"master,\s*destroyers|"
    r"luke,\s*reb|"
    r"chewie[- ],\s*protector)"
)
CSV_SENTENCE_RE = re.compile(
    r"(?i)\b(take|using|into your|because|although|deploy|anyone|although)\b"
)
GLUED_XN_RE = re.compile(
    r"(?<=[A-Za-z.!?')])[xX](\d+)(?:\s+\d+(?:/\d+)?)?\s+(?:go\s+)?(?=[A-Z])"
)
GLUED_SITE_RE = re.compile(r"(?<=\))(?=[A-Z][A-Za-z'.]+:)")


def split_glued_xn(line: str) -> list[str] | None:
    if not GLUED_XN_RE.search(line):
        return None
    parts: list[str] = []
    last = 0
    for m in GLUED_XN_RE.finditer(line):
        chunk = (line[last : m.start()] + "x" + m.group(1)).strip()
        if chunk:
            parts.append(chunk)
        last = m.end()
    rest = line[last:].strip()
    if rest:
        parts.append(rest)
    return parts if len(parts) >= 2 else None


def split_glued_sites(line: str) -> list[str] | None:
    if not GLUED_SITE_RE.search(line):
        return None
    parts = [p.strip() for p in GLUED_SITE_RE.split(line) if p.strip()]
    return parts if len(parts) >= 2 else None


def split_csv_cards(line: str) -> list[str] | None:
    if "," not in line:
        return None
    if " - " in line or CSV_SENTENCE_RE.search(line):
        return None
    if COMMA_KEEP_RE.match(line.strip()):
        return None
    parts: list[str] = []
    buf: list[str] = []
    depth = 0
    for ch in line:
        if ch == "(":
            depth += 1
            buf.append(ch)
        elif ch == ")":
            depth = max(0, depth - 1)
            buf.append(ch)
        elif ch == "," and depth == 0:
            part = "".join(buf).strip(" .")
            if part:
                parts.append(part)
            buf = []
        else:
            buf.append(ch)
    tail = "".join(buf).strip(" .")
    if tail:
        parts.append(tail)
    merged: list[str] = []
    for p in parts:
        if merged and PERSONA_TAIL_RE.match(p):
            merged[-1] = merged[-1] + ", " + p
        else:
            merged.append(p)
    if len(merged) < 2:
        return None
    if any(len(p) > 55 for p in merged):
        return None
    return merged


def parse_card_lines(deck_html: str) -> list[tuple[int, str]]:
    text = re.sub(r"<br\s*/?>", "\n", deck_html, flags=re.I)
    text = re.sub(r"</?(?:p|div|tr|td|li|ul|ol|table|b|i|strong|em)[^>]*>", "\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    text = htmlmod.unescape(text)
    prefix = ""
    ditto_planet = ""
    skip_shields = False
    stop_parse = False
    rows: list[tuple[int, str]] = []
    for raw in text.splitlines():
        raw = re.sub(r"^\t+", "", raw)
        if re.match(r"^ {3,}\S", raw) and not re.match(r"^ +(?:\d+\s|[xX]\d)", raw):
            stripped = raw.lstrip(" ")
            if (
                stripped
                and stripped[0].isalpha()
                and len(stripped) < 70
                and "." not in stripped
            ):
                raw = stripped
            else:
                continue
        raw = re.sub(r"\s{2,}\d{1,2}\s*$", "", raw)
        line = re.sub(r"\s+", " ", raw).replace("\ufeff", "").strip()
        raw_star = bool(re.match(r"^\*", line))
        line = re.sub(r"^[\u00b7·•*]+\s*", "", line)
        line = re.sub(r"\*+$", "", line).strip()
        line = re.sub(r"^[-–—]+", "", line).strip()
        line = re.sub(r"[-–—]+$", "", line).strip()
        line = re.sub(r"^<\s*", "", line).strip()
        line = re.sub(r"\s*>$", "", line).strip()
        line = re.sub(r">", " ", line)
        line = re.sub(r"<+$", "", line).strip()
        line = re.sub(r"(?<=[A-Za-z])\?(?=[A-Za-z])", "'", line)
        line = re.sub(r"\s+", " ", line).strip()
        if not line or line in {"Back to Top", "-"}:
            continue
        if "back to top" in line.casefold():
            continue
        if re.match(r"^strategy:?$", line, re.I):
            break
        if stop_parse:
            continue
        if re.match(
            r"(?i)^(?:optional/?interchangeable|optional\s+sideboard|sideboard|deck\s*2\s*\(\s*light|updates?$|cards\s+would\s+like\s+to\s+add|cards\s+i\s+want\s+to\s+get|card i need to get|some cards that i want to add|if\s+opponent\s+has\s+a\s+death\s+star)",
            line,
        ):
            stop_parse = True
            continue
        line = re.sub(r"\s+[-–—](?:used\b|your\b).*$", "", line, flags=re.I)
        if " - " in line and not re.search(r"\d+\s*-\s*\d+", line):
            depth = 0
            cut = -1
            i = 0
            while i < len(line) - 2:
                ch = line[i]
                if ch == "(":
                    depth += 1
                elif ch == ")":
                    depth = max(0, depth - 1)
                elif depth == 0 and line[i : i + 3] == " - ":
                    cut = i
                    break
                i += 1
            if cut >= 0:
                left = line[:cut].strip()
                if 3 <= len(left) <= 80:
                    line = left
        if len(line) > 160 and not re.match(r"^[xX]?\d+", line):
            continue
        jedi_ditto = re.match(r'^["\']+\s*["\']*\s*#\s*(\d+)\s*$', line)
        if jedi_ditto:
            n = int(jedi_ditto.group(1))
            tests = {
                1: "Great Warrior",
                2: "A Jedi's Strength",
                3: "It Is The Future You See",
                4: "Domain Of Evil",
                5: "Size Matters Not",
                6: "You Must Confront Vader",
            }
            if n in tests:
                rows.append((1, tests[n]))
                continue
        ditto = re.match(r'^["\']+\s*["\']*\s*:?\s*(.+)$', line)
        if ditto:
            site = ditto.group(1).strip().lstrip(": ").strip()
            planet = ditto_planet or prefix
            if planet:
                line = planet.rstrip(": ") + ": " + site
            else:
                line = site
        line = re.sub(r"^\((?:into\s+hands?)\)\s*", "", line, flags=re.I)
        if SKIP_LINE_RE.match(line) or re.fullmatch(r"\([^)]*\)", line) or NOTE_RE.search(line):
            continue
        if HEADER_RE.match(line) or SIDE_DECK_RE.match(line):
            prefix = ""
            ditto_planet = ""
            skip_shields = bool(
                SIDE_DECK_RE.match(line)
                or re.search(r"side cards|defensive shield|\bshields?\b|auaof", line, re.I)
            )
            continue
        if re.match(r"(?i)^ds-61-2\s*,\s*3\s*&\s*4$", line):
            for t in ("DS-61-2", "DS-61-3", "DS-61-4"):
                rows.append((1, t))
            continue
        if re.match(r"(?i)^ds-61-1\s*,\s*2\s+and\s+3$", line):
            for t in ("DS-61-2", "DS-61-3"):
                rows.append((1, t))
            continue
        m_tempest = re.match(
            r"(?i)^(?:\d+\s*[xX]\s+)?tempest scouts?\s+([\d,\sand]+)\s*$",
            line,
        )
        if m_tempest:
            for n in re.findall(r"\d+", m_tempest.group(1)):
                rows.append((1, f"Tempest Scout {n}"))
            continue
        go_m = re.match(
            r"^(.*?)\s*[xX]\s*(\d+)\s+go\s+(.*)$",
            line,
            re.I,
        )
        if go_m and go_m.group(1).strip() and go_m.group(3).strip():
            go_parts = (
                f"{go_m.group(1).strip()} x{go_m.group(2)}",
                go_m.group(3).strip(),
            )
            for part in go_parts:
                parsed_g = parse_qty_line(part.strip())
                if not parsed_g:
                    continue
                gq, gn = parsed_g
                gn = clean_name(gn)
                if not gn or HEADER_RE.match(gn) or SKIP_LINE_RE.match(gn):
                    continue
                rows.append((gq, gn))
            continue
        glued_parts = split_glued_xn(line)
        if glued_parts:
            for part in glued_parts:
                parsed_g = parse_qty_line(part.strip())
                if not parsed_g:
                    continue
                gq, gn = parsed_g
                gn = clean_name(gn)
                if not gn or HEADER_RE.match(gn) or SKIP_LINE_RE.match(gn):
                    continue
                rows.append((gq, gn))
            continue
        glued_sites = split_glued_sites(line)
        if glued_sites:
            for part in glued_sites:
                parsed_g = parse_qty_line(part.strip())
                if not parsed_g:
                    continue
                gq, gn = parsed_g
                gn = clean_name(gn)
                if not gn or HEADER_RE.match(gn) or SKIP_LINE_RE.match(gn):
                    continue
                rows.append((gq, gn))
            continue
        csv_parts = split_csv_cards(line)
        if csv_parts:
            for part in csv_parts:
                parsed_csv = parse_qty_line(part.strip())
                if not parsed_csv:
                    continue
                cq, cn = parsed_csv
                cn = clean_name(cn)
                if not cn or HEADER_RE.match(cn) or SKIP_LINE_RE.match(cn):
                    continue
                rows.append((cq, cn))
            continue
        if " | " in line:
            for part in line.split(" | "):
                parsed_p = parse_qty_line(part.strip().lstrip("-").strip())
                if not parsed_p:
                    continue
                pq, pn = parsed_p
                pn = clean_name(pn)
                if not pn or HEADER_RE.match(pn) or SKIP_LINE_RE.match(pn):
                    continue
                rows.append((pq, pn))
            continue
        if re.match(r"^and\s+", line, re.I) and "," in line:
            rest = re.sub(r"^and\s+", "", line, flags=re.I)
            for part in re.split(r",\s+and\s+|,\s+", rest):
                parsed = parse_qty_line(part.strip())
                if not parsed:
                    continue
                qty, name = parsed
                if not name or HEADER_RE.match(name) or SKIP_LINE_RE.match(name):
                    continue
                rows.append((qty, name))
            continue
        if skip_shields:
            continue
        if PLANET_RE.match(line):
            key = PLANET_RE.match(line).group(1)
            if key.lower().startswith("jabba"):
                prefix = "Jabba's Palace: "
            else:
                prefix = key.title() + ": "
            continue
        parsed = parse_qty_line(line)
        if not parsed:
            continue
        qty, name = parsed
        xm = re.search(
            r"(?:\s+x(\d+)|\s*\(\s*x(\d+)\s*\))\s*(?:\((?:NEW|new)\))?\s*$",
            name,
            re.I,
        )
        if xm:
            qty *= int(xm.group(1) or xm.group(2))
            name = name[: xm.start()].strip()
        bx = re.search(r"(?i)^(strike blocked)x\s+(\d+)\s*$", name)
        if bx:
            qty *= int(bx.group(2))
            name = bx.group(1)
        had_v = False
        if re.match(r"^\(\s*v\s*\)\s*", name, re.I):
            name = re.sub(r"^\(\s*v\s*\)\s*", "", name, flags=re.I)
            had_v = True
        if re.match(r"^\[V\]\s+", name, re.I):
            name = re.sub(r"^\[V\]\s+", "", name, flags=re.I)
            had_v = True
        if re.search(r"\s*\[V(?:C)?\]\s*$", name, re.I):
            name = re.sub(r"\s*\[V(?:C)?\]\s*$", "", name, flags=re.I)
            had_v = True
        if re.match(r"(?i)^virtual\s+", name):
            name = re.sub(r"(?i)^virtual\s+", "", name).strip()
            had_v = True
        if re.search(r"(?i)\s+V$", name) and not re.search(r"\(V\)\s*$", name):
            name = re.sub(r"(?i)\s+V$", "", name).strip()
            had_v = True
        if had_v and not re.search(r"\(V\)\s*$", name):
            name = name.strip() + " (V)"
        name = clean_name(name)
        if not name or len(name) < 2:
            continue
        if re.match(r"(?i)^all six$", name):
            for test in (
                "Great Warrior",
                "A Jedi's Strength",
                "It Is The Future You See",
                "Domain Of Evil",
                "Size Matters Not",
                "You Must Confront Vader",
            ):
                rows.append((1, test))
            continue
        if re.match(r"(?i)^ds-61-2\s*,\s*3\s*&\s*4$", name):
            for t in ("DS-61-2", "DS-61-3", "DS-61-4"):
                rows.append((1, t))
            continue
        if re.match(r"(?i)^ds-61-1\s*,\s*2\s+and\s+3$", name):
            for t in ("DS-61-2", "DS-61-3"):
                rows.append((1, t))
            continue
        if re.search(r"x{6,}", name, re.I):
            continue
        if re.search(r"card that lets me stack a destiny", name, re.I):
            continue
        if re.match(r"(?i)^\[(?:starting cards|version|decklist)", name):
            continue
        if re.match(r"^V\s+", name) and not re.match(r"^Vader", name, re.I):
            name = name[2:].strip() + " (V)"
        if HEADER_RE.match(name) or SKIP_LINE_RE.match(name) or re.fullmatch(r"\([^)]*\)", name):
            continue
        if re.match(r"(?i)^(?:ds2 sectors|dark jedi master(?:/maul icon)?|the fleet)$", name):
            if re.match(r"(?i)^ds2 sectors$", name):
                for sec in (
                    "Death Star II: Coolant Shaft",
                    "Death Star II: Capacitors",
                    "Death Star II: Reactor Core",
                ):
                    rows.append((1, sec))
            continue
        split_hit = None
        for pat, ship, pilot in SHIP_PILOT_SPLIT:
            if pat.match(name):
                split_hit = (ship, pilot)
                break
        if split_hit:
            rows.append((qty, split_hit[0]))
            rows.append((qty, split_hit[1]))
            continue
        if HEADER_RE.match(name):
            continue
        if raw_star and name.casefold() in STAR_SHIELD_NAMES:
            continue
        if rows and str(rows[-1][1]).endswith("/"):
            pq, pn = rows[-1]
            rows[-1] = (pq, clean_name(f"{pn}{name}"))
            continue
        if re.match(
            r"(?i)^(take your father.?s place|independent organization|"
            r"this place can be a little rough|or be destroyed|"
            r"sanity and compassion|sometimes i amaze even myself|"
            r"you.?re a slave\??)$",
            name,
        ):
            continue
        if name.startswith("/") and rows:
            rest = name[1:].strip()
            if re.match(
                r"(?i)^(DS-\d+|Scythe|Onyx|Saber|Black|Virago|Stinger|Slave)",
                rest,
            ):
                name = rest
            else:
                pq, pn = rows[-1]
                glued_name = clean_name(f"{pn} {name}")
                rows[-1] = (pq, glued_name)
                continue
        if re.search(
            r"useless gesture|weapon of a sith|fate deside|fate decide|"
            r"oppressive inforcement|you cannot hide for ever|allegations of corruption",
            name,
            re.I,
        ):
            continue
        if name in {"(S) = Start", "S) = starting"} or name.endswith("= Start") or name.endswith("= starting"):
            continue
        glue = re.search(
            r"(?i)^(darth vader, dark lord of the sith)\s*(darth vader w[/\\]lightsaber)$",
            name,
        )
        if glue:
            rows.append((1, clean_name(glue.group(1))))
            name = clean_name(glue.group(2))
        glued = re.search(
            r"(?i)^(coruscant: jedi council chambers?)\s*(heading for the medical frigate)$",
            name,
        )
        if glued:
            rows.append((qty, clean_name(glued.group(1))))
            name = clean_name(glued.group(2))
            qty = 1
        if prefix and ":" not in name:
            name = clean_name(prefix + name)
        if ":" in name:
            planet = name.split(":", 1)[0].strip()
            if planet and len(planet) < 40:
                ditto_planet = planet + ": "
        if rows and re.search(r"platform \(docking bay\)", name, re.I):
            pq, pn = rows[-1]
            if re.search(r"east\s*1", pn, re.I):
                rows[-1] = (pq, "Cloud City: East Platform (Docking Bay)")
                continue
        if re.search(r"tala twins", name, re.I):
            rows.append((1, "Tala 1"))
            rows.append((1, "Tala 2"))
            continue
        if re.search(r"bglee\s*bf", name, re.I):
            rows.append((1, "Brangus Glee"))
            name = "Boba Fett With Blaster Rifle"
        if re.search(r"their fire has|gone out of the univ", name, re.I):
            continue
        if re.match(r"(?i)^make it legal\.?$", name):
            if rows:
                prev = rows[-1][1]
                if re.search(r"(?i)my lord.*legal", prev):
                    rows[-1] = (rows[-1][0], "My Lord, Is That Legal?")
            continue
        if name.casefold() in {"d'an", "dan"} and rows and rows[-1][1].casefold() in {
            "figrin",
            "figrin d'an",
        }:
            pq, _ = rows[-1]
            rows[-1] = (pq, "Figrin D'an")
            continue
        if re.match(
            r"(?i)^(hidden base\s*\(system\)|hb\s*indicator|shields?|\d+\s+shields)$",
            name,
        ):
            continue
        rows.append((qty, name))
    return rows


SET_HINT = {
    "jawa (courscant)": ("Jawa", {12}),
    "jawa (coruscant)": ("Jawa", {12}),
    "coruscant (special edition)": ("Coruscant", {7}),
    "tatooine (coruscant)": ("Tatooine", {12}),
    "tatooine (ep 1)": ("Tatooine", {11}),
    "tatooine (episode 1)": ("Tatooine", {11}),
    "tatooine (premire)": ("Tatooine", {1}),
    "tatooine (premiere)": ("Tatooine", {1}),
    "tatooine (pr)": ("Tatooine", {1}),
    "boba fett (special ed)": ("Boba Fett", {7}),
    "boba fett (cs)": ("Boba Fett", {5}),
    "boba fett cloud city": ("Boba Fett", {5}),
    "cloud city boba fett": ("Boba Fett", {5}),
    "cc boba fett": ("Boba Fett", {5}),
    "darth maul (t)": ("Darth Maul, Young Apprentice", {12}),
    "coruscant (ep i / coruscant)": ("Coruscant", {12}),
    "naboo (ep i / coruscant)": ("Naboo", {12}),
    "tatooine (ep i / coruscant)": ("Tatooine", {12}),
    "alter (episode 1)": ("Alter", {12}),
    "proton torpedoes (ep.1)": ("Proton Torpedoes", {14}),
    "proton torpedoes (ep1)": ("Proton Torpedoes", {14}),
}

STAR_SHIELD_NAMES = {
    "resistance",
    "resistence",
    "allegations of corruption",
    "fanfare",
    "you've never won a race?",
    "wipe them out, all of them",
    "wipe them out, all of tham",
    "there is no try",
    "battle order",
    "come here you big coward",
    "do they have a code clearance",
    "do they have a code clearance?",
    "oppressive enforcement",
    "secret plans",
    "no escape",
    "leave them to me",
    "a useless gesture",
    "weapon of a sith",
    "my hidden base",
}


def original_vs_card(name: str, side: str) -> dict | None:
    spec = ORIGINAL_VS.get(name)
    if not spec:
        key = name.replace("\u2019", "'").replace("\u2018", "'").replace("`", "'").casefold()
        for a, b in ORIGINAL_VS.items():
            ak = a.replace("\u2019", "'").replace("\u2018", "'").replace("`", "'").casefold()
            if ak == key:
                spec = b
                name = a
                break
    if not spec:
        return None
    cat, dest = spec
    if dest is None and name == "Fusion Generator Supply Tanks (V)":
        dest = (
            "Fusion Generator Supply Tanks (V) (Dark) (Virtual Set 1)"
            if side.upper() == "DARK"
            else "Fusion Generator Supply Tanks (V) (Virtual Set 1)"
        )
    if dest is None and name == "Undercover (V)":
        dest = (
            "Undercover (V) (Dark) (Virtual Set 3)"
            if side.upper() == "DARK"
            else "Undercover (V) (Light) (Virtual Set 3)"
        )
    return {
        "title": dest,
        "cardCategory": cat,
        "cardId": None,
        "side": side,
        "original_vs": True,
    }


def try_lookup(name: str, side: str, allowed) -> dict | None:
    vs = original_vs_card(GPN_ALIAS.get(name, name), side) or original_vs_card(name, side)
    if vs:
        return vs
    hint = SET_HINT.get(name.casefold())
    if hint:
        try:
            return lookup(hint[0], side, hint[1])
        except KeyError:
            pass
    for cand in (name, GPN_ALIAS.get(name, name)):
        try:
            card = lookup(cand, side, allowed)
            if set_num(card.get("cardId") or "") < 200:
                return card
        except KeyError:
            continue
    want = GPN_ALIAS.get(name, name).casefold()
    side_u = side.upper()
    shield = None
    for c in load_cards():
        if (c.get("title") or "").casefold() != want:
            continue
        if allowed is not None:
            try:
                if set_num(c.get("cardId") or "") not in allowed:
                    continue
            except Exception:
                continue
        if (c.get("side") or "").upper() == side_u:
            return c
        if shield is None:
            shield = c
    return shield


def infer_side(rows: list[tuple[int, str]], title: str, desc: str) -> str:
    blob = f"{title}\n{desc}\n" + "\n".join(n for _, n in rows)
    dark_hits = len(
        re.findall(
            r"\b(vader|emperor|maul|hunt down|isb|imperial|visage|fear is my ally|"
            r"darth|senate mains|black sun|so much red|dark deck|dark side|"
            r"jabba|thugs|rumor ops)\b",
            blob,
            re.I,
        )
    )
    light_hits = len(
        re.findall(
            r"\b(hidden base|watch your step|profit|qmc|quiet mining|luke|obi|"
            r"we'll handle|jedi on qmc|ewoks|speeder scum|black sun scum)\b",
            blob,
            re.I,
        )
    )
    # Card-name side: try both
    scores = {"LIGHT": 0, "DARK": 0}
    for _, n in rows[:8]:
        for side in ("LIGHT", "DARK"):
            card = try_lookup(n, side, None)
            if card and (card.get("side") or "").upper() == side:
                scores[side] += 1
    if scores["DARK"] > scores["LIGHT"] + 1:
        return "DARK"
    if scores["LIGHT"] > scores["DARK"] + 1:
        return "LIGHT"
    if dark_hits > light_hits:
        return "DARK"
    return "LIGHT"


def format_from_cards(cards: list[tuple[int, dict]]) -> tuple[str, str]:
    vs_ns: list[int] = []
    for _, c in cards:
        title = c.get("title") or ""
        if c.get("original_vs") or "(Virtual Set" in title:
            m = re.search(r"Virtual Set (\d+)", title)
            vs_ns.append(int(m.group(1)) if m else 1)
    if vs_ns:
        n = max(vs_ns)
        return f"Premiere - Original VS{n}", "open_no_virtual"
    nums = [
        set_num(c["cardId"])
        for _, c in cards
        if c.get("cardId") and set_num(c["cardId"]) <= 20
    ]
    hi = max(nums) if nums else 9
    for threshold, wiki_fmt, gemp_code in SET_FORMAT:
        if hi >= threshold:
            return wiki_fmt, gemp_code
    return "Premiere - Death Star II", "premiere_ds2"


def display_date(posted: str) -> str:
    m = re.match(r"(\d{1,2})/(\d{1,2})/(\d{4})", posted or "")
    if not m:
        return posted
    month, day, year = int(m.group(1)), int(m.group(2)), int(m.group(3))
    return f"{day} {MONTHS[month]} {year}"


def sort_key(posted: str) -> tuple[int, int, int]:
    m = re.match(r"(\d{1,2})/(\d{1,2})/(\d{4})", posted or "")
    if not m:
        return (0, 0, 0)
    return (int(m.group(3)), int(m.group(1)), int(m.group(2)))


def lookup_rows(raw: list[tuple[int, str]], side: str, allowed) -> tuple[list[tuple[int, dict]], list[tuple[int, str]]]:
    out = []
    misses = []
    other = "DARK" if side == "LIGHT" else "LIGHT"
    for q, n in raw:
        card = try_lookup(n, side, allowed) or try_lookup(n, other, allowed)
        if card:
            out.append((q, card))
            continue
        m = re.match(r"^(.*\S)\s+(\d+)$", n)
        if m and 1 <= int(m.group(2)) <= 20:
            prefix = clean_name(m.group(1).strip())
            pcard = try_lookup(prefix, side, allowed) or try_lookup(prefix, other, allowed)
            if pcard:
                out.append((q * int(m.group(2)), pcard))
                continue
        m2 = re.match(r"^(.*[A-Za-z])([1-7])$", n)
        if m2:
            prefix = clean_name(m2.group(1))
            pcard = try_lookup(prefix, side, allowed) or try_lookup(prefix, other, allowed)
            if pcard:
                out.append((q, pcard))
                continue
        misses.append((q, n))
    return out, misses


# Controversial published titles: page title is {handle} DS|LS (Bill 2026-10-10).
# The published title stays in the source citation. Review list: ai-team-skills
# shared/swccg-wiki/wiki-docs/RENAMED-TITLES.md.
WITHHELD_TITLE = {
    3874: "LordHoban DS",
    1957: "ltkettch17 LS",
    211: "Winsafra DS",
}


def wiki_title_for(author: str, title: str, did: int | None = None) -> str:
    if did in WITHHELD_TITLE:
        return WITHHELD_TITLE[did]
    t = f"{author} {title}"
    t = t.replace("\u2019", "'").replace("\u2018", "'").replace("`", "'")
    t = t.replace("|", "/")
    t = re.sub(r"\[V\]", "(V)", t, flags=re.I)
    t = re.sub(r'["*?<>#\[\]{}]', "", t)
    t = re.sub(r"\s+", " ", t).strip()
    if did in WIKI_TITLE_SUFFIX:
        t = t + WIKI_TITLE_SUFFIX[did]
    if len(t) > 180:
        t = t[:177].rstrip() + "…"
    return t


def is_card_page(path: Path) -> bool:
    try:
        head = path.read_text(encoding="utf-8", errors="ignore")[:800]
    except OSError:
        return False
    return "{{Card" in head


def is_card_title(title: str) -> bool:
    slug = slug_file(title)
    for root in (PAGES, CLONE_PAGES):
        fp = root / slug
        if fp.is_file() and is_card_page(fp):
            return True
    return False


def player_dest(handle: str) -> str:
    if handle in HANDLE_PAGE:
        return HANDLE_PAGE[handle]
    dest = re.sub(r'["*?<>#\[\]{}]', "", handle)
    dest = re.sub(r"\s+", " ", dest).strip()
    if is_card_title(dest):
        return f"{dest} (GPN)"
    return dest or handle


def player_link(handle: str) -> str:
    dest = player_dest(handle)
    if dest == handle:
        return f"[[{handle}]]"
    return f"[[{dest}|{handle}]]"


def player_stub(player: str, bits: list[str], note: str = "") -> None:
    dest = player_dest(player)
    dest_dir = PAGES / "player-stubs"
    dest_dir.mkdir(exist_ok=True)
    for folder in (dest_dir, PAGES / "people", PAGES):
        fp = folder / slug_file(dest)
        if fp.exists() and is_card_page(fp):
            continue
        if fp.exists():
            text = fp.read_text(encoding="utf-8")
            extra = []
            for b in bits:
                title_bit = b.split("[[", 1)[-1].split("]]", 1)[0] if "[[" in b else b
                if title_bit not in text:
                    extra.append(b)
            if extra:
                block = "\n".join(extra) + "\n"
                if "== See also ==" in text:
                    text = text.replace("== See also ==", block + "\n== See also ==", 1)
                elif "== Decklists ==" in text or "== Tournament results ==" in text:
                    text = text.rstrip() + "\n" + block
                else:
                    text = text.rstrip() + "\n\n== Decklists ==\n\n" + block
                fp.write_text(text.replace("\r\n", "\n"), encoding="utf-8", newline="\n")
            rel = f"pages/{folder.name}/{fp.name}" if folder != PAGES else f"pages/{fp.name}"
            if folder == dest_dir:
                rel = f"pages/player-stubs/{fp.name}"
            TITLES.append((dest, rel))
            return
    lead_note = f" {note.rstrip('.')}." if note else ""
    hatnote = ""
    if dest.endswith(" (GPN)") and dest != player:
        hatnote = f" For the card of that name, see [[{player}]]."
    body = (
        f"'''{player}''' published constructed lists on [[Game Players Network]]."
        f"{lead_note}{hatnote}\n\n== Decklists ==\n\n"
        + "\n".join(bits)
        + "\n\n== See also ==\n\n* [[Game Players Network decks]]\n* [[Decklists]]\n\n"
        + CATS
        + "[[Category:Players]]\n"
    )
    fp = dest_dir / slug_file(dest)
    fp.write_text(body.strip() + "\n", encoding="utf-8", newline="\n")
    TITLES.append((dest, f"pages/player-stubs/{fp.name}"))


def existing_gemp_fn(wiki_title: str) -> str | None:
    fp = PAGES / slug_file(wiki_title)
    if not fp.exists():
        return None
    m = re.search(r"\[\[Media:([^|\]]+)", fp.read_text(encoding="utf-8"))
    if not m:
        return None
    return m.group(1).strip()


def write_deck(
    rec: dict,
    cards: list[tuple[int, dict]],
    fmt: str,
    gemp_code: str,
    side: str,
    wiki_only: bool = False,
) -> None:
    start, _ = infer_start(cards, side)
    vis = OBJ_FACE.get(start, start).split(" / ", 1)[0] if start != "—" else rec["title"]
    author = rec["author"]
    wiki_title = wiki_title_for(author, rec["title"], rec.get("id"))
    year = int(rec["posted"].split("/")[-1]) if rec["posted"] else 2001
    gemp_player = author
    last = author.split()[-1] if author.split() else author
    if last.isdigit() or len(last) <= 2:
        gemp_player = re.sub(r'["*?<>#\[\]{}\s]+', "", author)
    fn = safe_deck_filename(
        deck_name(fmt, vis, gemp_player, side, year, "GPN")
    ) + ".txt"
    skip_gemp = bool(rec.get("non_swccg_list") or rec.get("uncaptured") or not cards)
    if wiki_only:
        keep = existing_gemp_fn(wiki_title)
        if keep:
            fn = keep
        else:
            print("NOGEMP", rec["id"], wiki_title)
    elif skip_gemp:
        fn = ""
    else:
        GEMP_OUT.mkdir(exist_ok=True)
        dest_fn = GEMP_OUT / fn

        def gemp_name_taken(name: str) -> bool:
            want = name.lower()
            return any(p.name.lower() == want for p in GEMP_OUT.glob("*.txt"))

        if gemp_name_taken(fn):
            extra = re.sub(r"[^A-Za-z0-9]+", "", rec.get("title") or "")[:8] or str(rec.get("id"))
            fn = safe_deck_filename(
                dest_fn.stem.rsplit(" GPN", 1)[0] + " " + extra
            ) + ".txt"
            dest_fn = GEMP_OUT / fn
        if gemp_name_taken(fn):
            fn = safe_deck_filename(
                dest_fn.stem.rsplit(" GPN", 1)[0] + " " + str(rec.get("id"))
            ) + ".txt"
            dest_fn = GEMP_OUT / fn
        gemp_cards = [
            (q, c["title"], (c.get("side") or side))
            for q, c in cards
            if c.get("cardId")
            and (c.get("cardCategory") or "").upper() != "DEFENSIVE_SHIELD"
            and set_num(c["cardId"]) < 200
        ]
        xml, notes = xml_for(gemp_cards, side, gemp_code)
        dest_fn.write_text(xml, encoding="utf-8", newline="\n")
        if notes:
            print("NOTES", rec["id"], notes[:6])
    side_title = "Light" if side == "LIGHT" else "Dark"
    start_field = "—"
    if start != "—":
        cat = "OBJECTIVE" if start in OBJ_FACE or " / " in start else "LOCATION"
        start_field = wiki_card(start, side, cat)
    published = display_date(rec["posted"])
    desc = rec["description"].strip()
    strat = rec["strategy"].strip()
    table_cards = list(cards)
    if not rec.get("non_swccg_list"):
        for q, nmiss in rec.get("misses") or []:
            table_cards.append((q, {"title": nmiss, "cardCategory": "CHARACTER"}))
    n = sum(q for q, _ in table_cards)
    intro_bits: list[str] = []
    if desc:
        intro_bits.append(desc)
    if n == 0:
        if not rec.get("uncaptured") and not rec.get("non_swccg_list"):
            intro_bits.append("The published list has no cards.")
    elif n != 60:
        intro_bits.append(f"The published list has {n} cards.")
    if rec.get("id") == 4243:
        intro_bits.append(
            "The published post has two decks. This dest is the Dark list (Deck 1)."
        )
    intro_sec = (
        "== Introduction ==\n\n" + "\n\n".join(intro_bits) + "\n\n" if intro_bits else ""
    )
    after_sec = f"\n== Strategy ==\n\n{strat}\n" if strat else ""
    download = wiki_download_line(fn) if fn else ""
    if rec.get("non_swccg_list") and rec.get("deck_raw"):
        decklist = (
            '<div style="white-space:pre-wrap"><nowiki>\n'
            + rec["deck_raw"].strip()
            + "\n</nowiki></div>\n"
        )
    else:
        decklist = table_from_cards(table_cards, side)
    gemp_see = (
        ""
        if rec.get("non_swccg_list") or not fn
        else "* [[GEMP importable decklist]]\n"
    )
    withheld = " The published title is not used as the page title; it is kept in the source citation." if rec.get("id") in WITHHELD_TITLE else ""
    body = f"""'''{wiki_title}''' is a [[{side_title}]] constructed list published on [[Game Players Network]].{withheld}

== Deck info ==
* '''Player:''' {player_link(author)}
* '''Published:''' {published} (Game Players Network)
* '''GPN category:''' {rec['category']}
* '''Format:''' [[{fmt}]]
* '''Side:''' [[{side_title}]]
* '''Starting Card:''' {start_field}
* '''Strategy:''' {vis}
{download}

{intro_sec}== Decklist ==

{decklist}
{after_sec}
== See also ==

* [[Game Players Network decks]]
* {player_link(author)}
* [[Game Players Network]]
{gemp_see}
== Sources ==

* [{rec['url']} {rec['title']}] (Wayback, {DETAIL_TS})
* [{listing_url(rec.get('page', 63))} GPN Star Wars Decks page {rec.get('page', 63)}] (Wayback, {INDEX_TS})

{CATS}[[Category:Decklists]]
[[Category:{year}]]
[[Category:Game Players Network]]
"""
    write_page(wiki_title, body)
    rec["wiki_title"] = wiki_title
    rec["start"] = vis
    rec["side"] = side
    rec["fmt"] = fmt
    rec["gemp"] = fn
    rec["filename"] = f"pages/{slug_file(wiki_title)}"
    if not wiki_only:
        note = HANDLE_NOTE.get(author, "")
        player_stub(author, [f"* [[{wiki_title}]] ({side_title[0]}S, {published})"], note)
    TITLES.append((wiki_title, rec["filename"]))


def rewrite_hub(recs: list[dict]) -> None:
    rows = []
    for rec in sorted(recs, key=lambda r: (sort_key(r["posted"]), r["id"])):
        vis = rec.get("start") or rec["title"]
        disp = rec["title"].replace("|", "/").replace("\u2019", "'").replace("\u2018", "'")
        title_cell = f"[[{rec['wiki_title']}]]" if rec.get("id") in WITHHELD_TITLE else f"[[{rec['wiki_title']}|{disp}]]"
        rows.append(
            f"| {display_date(rec['posted'])}\n| [[{rec['fmt']}]]\n| {title_cell}\n"
            f"| [[{ 'Light' if rec['side']=='LIGHT' else 'Dark' }]]\n| {player_link(rec['author'])}"
        )
    table = (
        '{| class="wikitable sortable"\n'
        "! Date !! Format !! Title !! Side !! Author\n|-\n"
        + "\n|-\n".join(rows)
        + "\n|}"
    )
    body = f"""'''Game Players Network decks''' are constructed lists players posted on [[Game Players Network]] under Star Wars CCG Decks. The live site is gone. This archive starts at the last listing page (oldest remaining posts, November–December 2001) and works backward through the Wayback captures of decks.asp.

GPN split the catalog into Standard, Theme/Fun, and Scenario. Each article keeps the published title, the GPN handle as author, the card list, and a [[GEMP importable decklist|GEMP Importable deck]] download. Format is the printed-era pool the cards imply (late Decipher through Original Virtual when those cards appear).

A parent index of all published 60s is [[Decklists]]. Championship sheets stay on their event hubs.

== Lists ==

{table}

== See also ==

* [[Game Players Network]]
* [[Decklists]]
* [[Decipher deck designs]]
* [[DeckTech]]
* [[GEMP importable decklist]]
* [[Formats]]

== Sources ==

"""
    src_lines = []
    for pg in sorted(PAGE_IDS, reverse=True):
        src_lines.append(
            f"* [{listing_url(pg)} GPN Star Wars Decks page {pg}] (Wayback, 30 April 2005)"
        )
    src_lines.append(
        "* [https://web.archive.org/web/20050327114018/http://www.gameplayersnetwork.com/card/decks.asp?gm=starwars&ord=&pg=1 GPN Star Wars Decks page 1] (Wayback, 27 March 2005)"
    )
    body += "\n".join(src_lines) + f"""

{CATS}[[Category:Decklists]]
[[Category:Fan sites]]
[[Category:History]]
[[Category:Game Players Network]]
"""
    write_page(HUB, body)
    TITLES.append((HUB, f"pages/{slug_file(HUB)}"))


def patch_gpn_article() -> None:
    path = PAGES / "Game_Players_Network.wiki"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "Dest copies of those 60s belong on [[Decklists]].",
        "Published lists from that catalog are on [[Game Players Network decks]].",
    )
    text = text.replace(
        "Dest copies of those 60s live on [[Game Players Network decks]].",
        "Published lists from that catalog are on [[Game Players Network decks]].",
    )
    if "[[Game Players Network decks]]" not in text.split("== See also ==")[-1]:
        text = text.replace(
            "* [[History of the Players Committee]]",
            "* [[Game Players Network decks]]\n* [[History of the Players Committee]]",
        )
    path.write_text(text.replace("\r\n", "\n"), encoding="utf-8", newline="\n")
    TITLES.append(("Game Players Network", "pages/Game_Players_Network.wiki"))


def patch_decklists() -> None:
    path = PAGES / "Decklists.wiki"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    old = (
        "[[Game Players Network]] hosted a rated, user-submitted catalog "
        "(Standard, Theme/Fun, Scenario) around 2001–2005. Those 60s are not yet dested here. "
        "The working copy is the Wayback capture of decks.asp."
    )
    new = (
        "[[Game Players Network]] hosted a rated, user-submitted catalog "
        "(Standard, Theme/Fun, Scenario) around 2001–2005. Those lists start on "
        "[[Game Players Network decks]] (oldest remaining listing page first)."
    )
    text = text.replace(old, new)
    text = text.replace(
        "Dest copies start on [[Game Players Network decks]] (oldest remaining listing page first).",
        "Those lists start on [[Game Players Network decks]] (oldest remaining listing page first).",
    )
    text = text.replace(
        "* [[Decipher deck designs]] · [[DeckTech]] · [[Game Players Network]]",
        "* [[Decipher deck designs]] · [[DeckTech]] · [[Game Players Network decks]] · [[Game Players Network]]",
    )
    path.write_text(text.replace("\r\n", "\n"), encoding="utf-8", newline="\n")
    TITLES.append(("Decklists", "pages/Decklists.wiki"))


def page_from_argv() -> int | None:
    args = sys.argv[1:]
    for i, a in enumerate(args):
        if a == "--page" and i + 1 < len(args):
            return int(args[i + 1])
        if a.startswith("--page="):
            return int(a.split("=", 1)[1])
    return None


def resolve_rec(rec: dict) -> dict:
    rec["page"] = ID_TO_PAGE.get(rec["id"], rec.get("page", 63))
    title_cf = rec["title"].casefold()
    rec["rows"] = [
        (q, n) for q, n in rec["rows"] if n.casefold() != title_cf
    ]
    rec["qty"] = sum(q for q, _ in rec["rows"])
    side = infer_side(rec["rows"], rec["title"], rec["description"])
    cards, misses = lookup_rows(rec["rows"], side, None)
    if misses and len(cards) < max(8, rec["qty"] // 4):
        other = "DARK" if side == "LIGHT" else "LIGHT"
        cards2, misses2 = lookup_rows(rec["rows"], other, None)
        if len(cards2) > len(cards):
            side, cards, misses = other, cards2, misses2
    rec["side"] = side
    rec["cards"] = cards
    rec["misses"] = misses
    yj = any(
        re.search(
            r"(?i)(acclamator|kit fisto|clone platoon|at-te walker|padme amidala|"
            r"jedi starfighter scout|chancellor.?s guard|slkdjfgp)",
            n,
        )
        for _, n in rec["rows"]
    )
    if yj and len(cards) < 8:
        rec["non_swccg_list"] = True
        rec["rows"] = []
        rec["cards"] = []
        rec["misses"] = []
        rec["qty"] = 0
        cards, misses = [], []
        rec["cards"] = cards
        rec["misses"] = misses
    fmt, code = format_from_cards(cards)
    rec["fmt"] = fmt
    rec["gemp_code"] = code
    rec["wiki_title"] = wiki_title_for(rec["author"], rec["title"], rec.get("id"))
    start, _ = infer_start(cards, side)
    rec["start"] = (
        OBJ_FACE.get(start, start).split(" / ", 1)[0] if start != "—" else rec["title"]
    )
    return rec


def load_rec(did: int) -> dict | None:
    path = CACHE / f"id-{did}.html"
    if not path.exists():
        print("NOFILE", did)
        return None
    rec = parse_deck_html(path)
    return resolve_rec(rec)


def main() -> int:
    parse_only = "--parse-only" in sys.argv
    wiki_only = "--wiki-only" in sys.argv
    all_live = "--all" in sys.argv
    page_arg = page_from_argv()
    TITLES.clear()
    if all_live:
        write_ids = [
            did for pg in sorted(PAGE_IDS, reverse=True) for did in PAGE_IDS[pg]
        ]
    elif page_arg is not None:
        write_ids = PAGE_IDS[page_arg]
    else:
        write_ids = PAGE63_IDS
    hub_ids: list[int] = []
    for pg in sorted(PAGE_IDS, reverse=True):
        hub_ids.extend(PAGE_IDS[pg])
    recs: list[dict] = []
    fails = 0
    parse_ids = write_ids if (parse_only or wiki_only) else hub_ids
    for did in parse_ids:
        rec = load_rec(did)
        if rec is None:
            fails += 1
            continue
        print(
            f"PARSE id={did} pg={rec['page']} qty={rec['qty']} "
            f"got={sum(q for q, _ in rec['cards'])} miss={len(rec['misses'])} "
            f"{rec['side']} {rec['fmt']} {rec['author']!r} {rec['title']!r}"
        )
        if rec["misses"]:
            print(
                "  MISS",
                rec["misses"][:12],
                ("..." if len(rec["misses"]) > 12 else ""),
            )
        recs.append(rec)
        if parse_only:
            continue
        if did not in write_ids:
            continue
        if not rec["cards"]:
            if rec["qty"] == 0:
                print("EMPTY", did, rec["author"], rec["title"])
            else:
                print("FAIL no cards", did)
                fails += 1
                continue
        write_deck(
            rec,
            rec["cards"],
            rec["fmt"],
            rec["gemp_code"],
            rec["side"],
            wiki_only=wiki_only,
        )
    if not parse_only:
        if not wiki_only:
            rewrite_hub(recs)
            if page_arg in (None, 63) and not all_live:
                patch_gpn_article()
                patch_decklists()
        if all_live:
            tsv = ROOT / "y-gpn-intro-backfill.tsv"
        else:
            tsv_page = page_arg if page_arg is not None else 63
            tsv = ROOT / f"y-gpn-page{tsv_page}.tsv"
        seen = set()
        lines = []
        for title, rel in TITLES:
            key = (title, rel)
            if key in seen:
                continue
            seen.add(key)
            lines.append(f"{title}\t{rel}")
        tsv.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
        print("TSV", tsv, "n", len(lines), "GEMP", GEMP_OUT)
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
