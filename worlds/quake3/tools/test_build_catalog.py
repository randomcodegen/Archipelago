import struct

import pytest

from build_catalog import (
    BASE_ITEM_CLASSNAMES,
    ITEM_FAMILIES,
    ITEM_DISPLAY_NAMES,
    build_pickups,
    build_traversals,
    encoded_catalog,
    entity_is_active,
    parse_arenas,
    parse_blocks,
    read_bsp_entities,
)


def test_invalid_fraglimit_falls_back_by_bot_count():
    arenas = parse_arenas("""
        { map one bots sarge fraglimit 0 }
        { map two bots "sarge ranger" }
        { map many bots "sarge ranger keel" fraglimit 69 }
        { map explicit bots sarge fraglimit 15 }
    """)
    assert {key: arena["frag_limit"] for key, arena in arenas.items()} == {
        "one": 10, "two": 15, "many": 20, "explicit": 15,
    }


def make_bsp(entity_text: str, *, offset: int = 144) -> bytes:
    entity_data = entity_text.encode("latin-1") + b"\0"
    header = bytearray(offset)
    struct.pack_into("<4sI", header, 0, b"IBSP", 46)
    struct.pack_into("<ii", header, 8, offset, len(entity_data))
    return bytes(header) + entity_data


def test_parse_blocks_handles_quotes_bare_values_comments_and_escapes():
    text = '// comment\n{ "classname" "item_health" wait -1 "sound" "" "note" "say \\"hi\\"" }'
    assert parse_blocks(text) == [{
        "classname": "item_health",
        "wait": "-1",
        "sound": "",
        "note": 'say "hi"',
    }]


def test_read_bsp_entities_preserves_entity_order():
    entities = read_bsp_entities(make_bsp('{"classname" "worldspawn"}{"classname" "item_quad"}'))
    assert [entity["classname"] for entity in entities] == ["worldspawn", "item_quad"]


@pytest.mark.parametrize("offset,size", [(143, 1), (144, 50), (-1, 1), (144, -1)])
def test_read_bsp_entities_rejects_bad_lump_bounds(offset, size):
    data = bytearray(make_bsp("{}"))
    struct.pack_into("<ii", data, 8, offset, size)
    with pytest.raises(ValueError, match="out of bounds"):
        read_bsp_entities(bytes(data))


def test_spawn_filters_match_base_free_for_all_branch():
    assert entity_is_active({}, "ffa")
    assert not entity_is_active({"notfree": "1"}, "ffa")
    assert not entity_is_active({"notq3a": "1"}, "tournament")
    assert entity_is_active({"notteam": "1"}, "ffa")
    assert entity_is_active({"gametype": "ffa team"}, "ffa")
    assert not entity_is_active({"gametype": "team ctf"}, "ffa")
    assert entity_is_active({"gametype": "tournament"}, "tournament")


def test_all_item_classnames_have_unlock_families():
    assert ITEM_FAMILIES["ammo_rockets"] == "Rocket Launcher"
    assert ITEM_FAMILIES["item_health_mega"] == "Mega Health"
    assert all(ITEM_FAMILIES.values())
    assert set(ITEM_DISPLAY_NAMES) == set(ITEM_FAMILIES)
    assert set(ITEM_FAMILIES) <= BASE_ITEM_CLASSNAMES
    assert BASE_ITEM_CLASSNAMES - set(ITEM_FAMILIES) == {
        "weapon_gauntlet", "weapon_grapplinghook",
        "team_CTF_redflag", "team_CTF_blueflag"
    }


def test_item_team_becomes_one_pickup_with_multiple_variants():
    pickups = build_pickups([
        {"classname": "item_quad", "origin": "1 2 3", "team": "powerup"},
        {"classname": "item_invis", "origin": "1 2 4", "team": "powerup"},
    ], "test", "ffa")
    assert len(pickups) == 1
    assert pickups[0]["classnames"] == ["item_quad", "item_invis"]
    assert pickups[0]["families"] == ["Quad Damage", "Invisibility"]
    assert [variant["bsp_entity_ordinal"] for variant in pickups[0]["variants"]] == [1, 2]


def test_traversals_are_individual_and_skip_spectator_teleporters():
    traversals = build_traversals([
        {"classname": "worldspawn"},
        {"classname": "trigger_push"},
        {"classname": "trigger_teleport"},
        {"classname": "trigger_push"},
        {"classname": "trigger_teleport", "spawnflags": "1"},
        {"classname": "trigger_push", "notfree": "1"},
    ], "ffa")
    assert traversals == [
        {"ordinal": 1, "kind_ordinal": 1, "bsp_entity_ordinal": 2, "kind": "jump_pad"},
        {"ordinal": 2, "kind_ordinal": 1, "bsp_entity_ordinal": 3, "kind": "teleporter"},
        {"ordinal": 3, "kind_ordinal": 2, "bsp_entity_ordinal": 4, "kind": "jump_pad"},
    ]
def test_target_give_donor_is_not_a_world_pickup():
    pickups = build_pickups([
        {"classname": "item_armor_combat", "origin": "0 0 64", "targetname": "armor"},
        {"classname": "target_give", "origin": "0 0 32", "target": "armor"},
        {"classname": "target_give", "origin": "0 0 16"},
        {"classname": "item_armor_combat", "origin": "0 0 0"},
    ], "test", "ffa")
    assert [pickup["bsp_entity_ordinal"] for pickup in pickups] == [4]


def test_pretty_output_is_deterministic():
    catalog = {"schema_version": 1, "maps": [{"key": "q3dm0"}]}
    assert encoded_catalog(catalog) == encoded_catalog(catalog)
