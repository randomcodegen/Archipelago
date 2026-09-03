import json
from pathlib import Path

from export_catalog import ITEM_BASE, LOCATION_BASE, build_tables, c_output, python_output


def real_tables():
    catalog = json.loads((Path(__file__).parents[1] / "data" / "maps.json").read_text())
    return build_tables(catalog)


def test_generated_ids_are_unique_and_reserved():
    tables = real_tables()
    item_ids = list(tables["item_name_to_id"].values())
    location_ids = list(tables["location_name_to_id"].values())
    assert len(item_ids) == len(set(item_ids))
    assert len(location_ids) == len(set(location_ids))
    assert min(item_ids) >= ITEM_BASE and max(item_ids) <= ITEM_BASE + 999
    assert min(location_ids) >= LOCATION_BASE and max(location_ids) < LOCATION_BASE + 64 * 512


def test_generated_outputs_are_deterministic_and_share_hash():
    tables = real_tables()
    assert python_output(tables) == python_output(tables)
    assert c_output(tables) == c_output(tables)
    expected = tables["catalog_hash"].encode()
    assert expected in python_output(tables)
    assert expected in c_output(tables)


def test_map_pickup_and_location_lookups_are_complete():
    tables = real_tables()
    assert len(tables["maps"]) == 60
    for map_data in tables["maps"]:
        assert (len(map_data["pickups"]) + len(map_data["traversals"]) + len(map_data["kills"]) + 1
                + bool(map_data["powerup_frag_location_id"])) == sum(
            name.startswith(f"{map_data['name']} ({map_data['key']}) -")
            for name in tables["location_name_to_id"]
        )
