"""Ralltiir Operations (V) must map to 702_210042 and never fall back to a Decipher id."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import gemp_importable as gi  # noqa: E402
import gemp_map as gm  # noqa: E402

V_TITLES = [
    "Ralltiir Operations (V)",
    "Ralltiir Operations / In The Hands Of The Empire (V)",
    "Ralltiir Operations / In The Hands Of The Empire (V) (Errata)",
    "Ralltiir Operations / In The Hands Of The Empire (V) (Errata 2)",
]


def test_override_maps_virtual_titles_to_702():
    for title in V_TITLES:
        card = gi.lookup(title, "DARK", None)
        assert card["cardId"] == "702_210042", title
        resolved, how = gm.resolve(title, "DARK")
        assert resolved and resolved["cardId"] == "702_210042", (title, how, resolved)


def test_decipher_title_still_maps_to_7_300():
    assert gi.lookup("Ralltiir Operations", "DARK", None)["cardId"] == "7_300"
    assert gi.lookup("Ralltiir Operations / In The Hands Of The Empire", "DARK", None)["cardId"] == "7_300"


def test_missing_virtual_title_does_not_fall_back_to_decipher():
    try:
        gi.lookup("This Card Does Not Exist (V)", "DARK", None)
    except KeyError:
        pass
    else:
        raise AssertionError("expected KeyError for an unknown (V) title")
    xml, notes = gi.xml_for([(1, "This Card Does Not Exist (V)", None)], "DARK", None)
    assert any("omits This Card Does Not Exist (V): not in GEMP" in n for n in notes)
    assert "7_300" not in xml


def test_xml_for_emits_702_for_ralltiir_operations_v():
    xml, _notes = gi.xml_for([(1, "Ralltiir Operations (V)", None)], "DARK", None)
    assert 'blueprintId="702_210042"' in xml
    assert "7_300" not in xml


if __name__ == "__main__":
    test_override_maps_virtual_titles_to_702()
    test_decipher_title_still_maps_to_7_300()
    test_missing_virtual_title_does_not_fall_back_to_decipher()
    test_xml_for_emits_702_for_ralltiir_operations_v()
    print("ok")
