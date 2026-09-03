from .bases import Quake3TestBase
from ..data.generated import MAP_BY_KEY


class TestSelectedLocations(Quake3TestBase):
    options = {"map_pool_size": 26}

    def test_every_selected_check_is_present_once(self):
        addressed = [location for location in self.multiworld.get_locations(1) if location.address is not None]
        expected = sum(
            len(MAP_BY_KEY[key]["pickups"])
            + sum(traversal["location_name"] in self.world.included_traversal_locations
                  for traversal in MAP_BY_KEY[key]["traversals"])
            + bool(MAP_BY_KEY[key]["powerup_frag_location_id"])
            + MAP_BY_KEY[key]["frag_limit"] // self.world.options.kill_check_increment.value + 1
            for key in self.world.selected_map_keys
        )
        self.assertEqual(len(addressed), expected)
        self.assertEqual(len({location.name for location in addressed}), expected)
        self.assertEqual(len({location.address for location in addressed}), expected)
        for key in self.world.selected_map_keys:
            map_data = MAP_BY_KEY[key]
            region = self.multiworld.get_region(f"{map_data['name']} ({key})", 1)
            self.assertEqual(
                len([location for location in region.locations if location.address is not None]),
                len(map_data["pickups"])
                + sum(traversal["location_name"] in self.world.included_traversal_locations
                      for traversal in map_data["traversals"])
                + bool(map_data["powerup_frag_location_id"])
                + map_data["frag_limit"] // self.world.options.kill_check_increment.value + 1,
            )


class TestEveryFragLocation(Quake3TestBase):
    options = {"map_pool_size": 1, "kill_check_increment": 1}

    def test_increment_one_keeps_every_frag(self):
        map_data = MAP_BY_KEY[self.world.selected_map_keys[0]]
        region = self.multiworld.get_region(f"{map_data['name']} ({map_data['key']})", 1)
        kills = [location for location in region.locations if " - Kill " in location.name]
        self.assertEqual(len(kills), map_data["frag_limit"])
