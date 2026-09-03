import random
from BaseClasses import ItemClassification

from .bases import Quake3TestBase
from ..data.generated import AMMO_FILLERS, ITEM_NAME_TO_ID, MAP_BY_KEY
from ..items import FILLER_ITEMS, overflow_unlocks


def test_excess_unlocks_are_precollected():
    items = ["Stage Access", "Rocket Launcher Unlock", "Armor Unlock"]
    selected = overflow_unlocks(items, 2, random.Random(1))
    assert len(selected) == 1
    assert next(iter(selected)).endswith(" Unlock")


class TestItemPool(Quake3TestBase):
    def test_refills_are_filler_and_available_in_the_pool(self):
        for name in FILLER_ITEMS:
            self.assertEqual(self.world.create_item(name).classification, ItemClassification.filler)
        self.assertIn("+1 Health", self.world.filler_items)
        self.assertIn("+1 Armor", self.world.filler_items)
        self.assertTrue(all(self.world.get_filler_item_name() in FILLER_ITEMS for _ in range(30)))

    def test_pool_balances_unfilled_checks(self):
        addressed = [location for location in self.multiworld.get_locations(1) if location.address is not None]
        self.assertEqual(len(self.multiworld.itempool), len(addressed))

    def test_ammo_filler_matches_selected_weapon_families(self):
        families = {family for key in self.world.selected_map_keys for family in MAP_BY_KEY[key]["weapon_families"]}
        self.assertEqual(len(AMMO_FILLERS), 8)
        for index, (name, family, amount) in enumerate(AMMO_FILLERS):
            self.assertEqual(ITEM_NAME_TO_ID[name], 3370304 + index)
            self.assertGreater(amount, 0)
            self.assertEqual(name in self.world.filler_items, family in families)


    def test_starting_stage_is_precollected(self):
        name = MAP_BY_KEY[self.world.starting_map_key]["stage_item_name"]
        self.assertTrue(any(item.name == name for item in self.multiworld.precollected_items[1]))

    def test_unselected_stage_items_are_absent(self):
        present = {item.name for item in self.multiworld.itempool + self.multiworld.precollected_items[1]}
        for key, map_data in MAP_BY_KEY.items():
            self.assertEqual(map_data["stage_item_name"] in present, key in self.world.selected_map_keys)


class TestSmallMapFiller(Quake3TestBase):
    options = {"q3_maps": {"q3dm0": 1}, "cpma_maps": {}, "map_pool_size": 1}

    def test_unused_ammo_is_excluded(self):
        families = MAP_BY_KEY["q3dm0"]["weapon_families"]
        for name, family, _ in AMMO_FILLERS:
            self.assertEqual(name in self.world.filler_items, family in families)
            if family not in families:
                self.assertFalse(any(item.name == name for item in self.multiworld.itempool))
