import json

from .bases import Quake3TestBase
from ..data.generated import CATALOG_HASH, MAP_BY_KEY


def validate_slot_data(data):
    assert set(data) == {
        "schema_version", "cpma", "catalog_hash", "selected_maps", "starting_map",
        "pickup_locations",
        "goal_type", "goal_required", "kill_check_increment",
        "weapon_logic_percentage", "item_logic_percentage",
    }
    assert data["schema_version"] == 8
    assert data["cpma"] in (0, 1)
    assert data["catalog_hash"] == CATALOG_HASH
    assert data["selected_maps"] == sorted(
        data["selected_maps"], key=lambda key: MAP_BY_KEY[key]["map_index"]
    )
    assert len(data["selected_maps"]) == len(set(data["selected_maps"]))
    assert data["starting_map"] in data["selected_maps"]
    valid_pickups = {
        pickup["location_id"] for key in data["selected_maps"] for pickup in MAP_BY_KEY[key]["pickups"]
    } | {traversal["location_id"] for key in data["selected_maps"]
         for traversal in MAP_BY_KEY[key]["traversals"]}
    assert set(data["pickup_locations"]) <= valid_pickups
    assert data["goal_type"] in (0, 1)
    assert data["goal_required"] >= 1
    assert 1 <= data["kill_check_increment"] <= 50
    if data["goal_type"] == 0:
        assert data["goal_required"] <= len(data["selected_maps"])
    assert 0 <= data["weapon_logic_percentage"] <= 100
    assert 0 <= data["item_logic_percentage"] <= 100
    assert len(json.dumps(data).encode()) < 32 * 1024


class TestDefaultSlotData(Quake3TestBase):
    def test_slot_data(self):
        data = self.world.fill_slot_data()
        validate_slot_data(data)
        self.assertEqual(data["selected_maps"], self.world.selected_map_keys)
        self.assertEqual(data["goal_required"], self.world.goal_required)


class TestFullSlotData(Quake3TestBase):
    options = {"map_pool_size": 26, "weapon_logic_percentage": 100, "item_logic_percentage": 100}

    def test_full_slot_data_stays_small(self):
        validate_slot_data(self.world.fill_slot_data())
