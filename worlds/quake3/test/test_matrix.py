from .bases import Quake3TestBase
from ..rules import required_count


class TestOptionMatrix(Quake3TestBase):
    def test_pool_logic_and_goal_boundaries(self):
        for pool_size in (1, 10, 26):
            for logic in (0, 50, 100):
                for goal in (1, 50, 100):
                    with self.subTest(pool_size=pool_size, logic=logic, goal=goal):
                        self.options = {
                            "map_pool_size": pool_size,
                            "weapon_logic_percentage": logic,
                            "item_logic_percentage": logic,
                            "goal_percentage": goal,
                        }
                        self.world_setup(seed=pool_size * 10000 + logic * 100 + goal)
                        slot = self.world.fill_slot_data()
                        self.assertEqual(len(slot["selected_maps"]), pool_size)
                        self.assertEqual(len(set(slot["selected_maps"])), pool_size)
                        self.assertIn(slot["starting_map"], slot["selected_maps"])
                        self.assertEqual(slot["goal_required"], required_count(pool_size, goal))
                        self.assertEqual(slot["weapon_logic_percentage"], logic)
                        self.assertEqual(slot["item_logic_percentage"], logic)
                        self.collect_all_but(())
                        for key in slot["selected_maps"]:
                            self.assertTrue(self.can_reach_entrance(f"Enter {key}"))
