from .bases import Quake3TestBase
from ..data.generated import MAP_BY_KEY


class TestCustomIncludedLocations(Quake3TestBase):
    options = {
        "map_pool_size": 26,
        "custom_included_locations": {"weapon_rocketlauncher": 100},
    }

    def test_only_configured_pickups_become_locations(self):
        pickup_names = {
            location.name for location in self.multiworld.get_locations(1)
            if location.address is not None and " - Pickup " in location.name
        }
        expected = {
            pickup["location_name"]
            for key in self.world.selected_map_keys
            for map_data in (MAP_BY_KEY[key],)
            for pickup in map_data["pickups"]
            if pickup["classname"] == "weapon_rocketlauncher"
        }
        self.assertEqual(pickup_names, expected)


class TestCustomIncludedTraversals(Quake3TestBase):
    options = {
        "map_pool_size": 26,
        "custom_included_locations": {"trigger_push": 100},
    }

    def test_only_jump_pads_become_traversal_locations(self):
        names = {location.name for location in self.multiworld.get_locations(1)
                 if location.address is not None and (" - Jump Pad " in location.name
                                                       or " - Teleporter " in location.name)}
        expected = {traversal["location_name"] for key in self.world.selected_map_keys
                    for traversal in MAP_BY_KEY[key]["traversals"] if traversal["kind"] == "jump_pad"}
        self.assertEqual(names, expected)
