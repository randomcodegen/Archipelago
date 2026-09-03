from .bases import Quake3TestBase
from ..rules import required_count


class TestDefaultSelection(Quake3TestBase):
    def test_pool_size_clamps_to_enabled_maps(self):
        from ..data.generated import MAPS

        cases = (
            ({}, 26),
            ({"q3_maps": {"q3dm0": 1, "q3dm1": 0}}, 1),
            ({"cpma": True, "q3_maps": {"q3dm0": 1}, "cpma_maps": {"cpm3": 1}}, 2),
            ({"cpma": True, "q3_maps": {}, "cpma_maps": {"cpm3": 1}}, 1),
            ({"cpma": True, "cpma_maps": {m["key"]: 1 for m in MAPS if m["key"].startswith("cpm")}}, 60),
        )
        for options, expected in cases:
            with self.subTest(options=options):
                self.options = {"map_pool_size": 60, "maximum_starting_weapons": 8, **options}
                self.world_setup(seed=42)
                self.assertEqual(len(self.world.selected_map_keys), expected)
                self.assertEqual(len(self.world.fill_slot_data()["selected_maps"]), expected)
                self.assertEqual(self.world.goal_required, required_count(expected, 50))

    def test_clamping_does_not_allow_empty_or_disabled_cpma_pools(self):
        from Options import OptionError

        for options in (
            {"q3_maps": {}, "cpma_maps": {}},
            {"cpma": False, "cpma_maps": {"cpm3": 1}},
        ):
            with self.subTest(options=options):
                self.options = {"map_pool_size": 60, **options}
                with self.assertRaises(OptionError):
                    self.world_setup(seed=42)

    def test_default_selection_is_cached_and_sorted(self):
        self.assertEqual(len(self.world.selected_map_keys), 10)
        indices = [self.world.item_name_to_id[
            self.world_map(key)["stage_item_name"]
        ] for key in self.world.selected_map_keys]
        self.assertEqual(indices, sorted(indices))
        self.assertIn(self.world.starting_map_key, self.world.selected_map_keys)

    def test_same_seed_repeats_selection_and_start(self):
        self.world_setup(seed=123456)
        first = (self.world.selected_map_keys, self.world.starting_map_key)
        self.world_setup(seed=123456)
        self.assertEqual(first, (self.world.selected_map_keys, self.world.starting_map_key))

    def world_map(self, key):
        from ..data.generated import MAP_BY_KEY
        return MAP_BY_KEY[key]


class TestOneMapSelection(Quake3TestBase):
    options = {"map_pool_size": 1, "goal_percentage": 1}

    def test_one_map_boundary(self):
        self.assertEqual(len(self.world.selected_map_keys), 1)
        self.assertEqual(self.world.goal_required, 1)


class TestConfiguredMapPool(Quake3TestBase):
    options = {
        "cpma": True,
        "q3_maps": {"q3dm0": 1},
        "cpma_maps": {"cpm3": 1},
        "map_pool_size": 0,
    }

    def test_zero_size_uses_all_enabled_maps(self):
        self.assertEqual(self.world.selected_map_keys, ["q3dm0", "cpm3"])


class TestFullMapSelection(Quake3TestBase):
    options = {"map_pool_size": 26, "goal_percentage": 100}

    def test_full_map_boundary(self):
        self.assertEqual(len(set(self.world.selected_map_keys)), 26)
        self.assertEqual(self.world.goal_required, 26)


class TestMaximumStartingWeapons(Quake3TestBase):
    options = {"map_pool_size": 26, "weapon_logic_percentage": 100,
               "maximum_starting_weapons": 2}

    def test_starting_map_respects_cap(self):
        from ..data.generated import MAP_BY_KEY

        starting_map = MAP_BY_KEY[self.world.starting_map_key]
        self.assertLessEqual(len(starting_map["weapon_families"]), 2)


def test_goal_rounding_examples():
    assert required_count(1, 1) == 1
    assert required_count(26, 1) == 1
    assert required_count(3, 50) == 2
    assert required_count(26, 100) == 26
