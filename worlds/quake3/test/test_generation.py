from .bases import Quake3TestBase


class TestDefaultGeneration(Quake3TestBase):
    def test_all_items_make_every_selected_stage_reachable(self):
        self.collect_all_but(())
        for key in self.world.selected_map_keys:
            self.assertTrue(self.can_reach_entrance(f"Enter {key}"))


class TestHalfLogicGeneration(Quake3TestBase):
    options = {"map_pool_size": 1, "weapon_logic_percentage": 50, "item_logic_percentage": 50}

    def test_generates(self):
        self.assertEqual(len(self.world.selected_map_keys), 1)


class TestFullLogicGeneration(Quake3TestBase):
    options = {"map_pool_size": 26, "weapon_logic_percentage": 100, "item_logic_percentage": 100}

    def test_generates(self):
        self.assertEqual(len(self.world.selected_map_keys), 26)
