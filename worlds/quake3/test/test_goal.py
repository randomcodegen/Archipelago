from BaseClasses import CollectionState, ItemClassification

from .bases import Quake3TestBase
from ..data.generated import MAP_BY_KEY
from ..items import Quake3Item
from ..regions import map_label


class TestGoal(Quake3TestBase):
    options = {"map_pool_size": 3, "goal_percentage": 50}

    def test_exact_required_stage_events_reach_goal(self):
        state = CollectionState(self.multiworld)
        state.prog_items[1].clear()
        events = [f"{map_label(MAP_BY_KEY[key])} Cleared" for key in self.world.selected_map_keys]
        for name in events[:self.world.goal_required - 1]:
            state.collect(Quake3Item(name, ItemClassification.progression, None, 1))
        self.assertFalse(state.can_reach("Reach Goal", "Entrance", 1))
        state.collect(Quake3Item(events[self.world.goal_required - 1], ItemClassification.progression, None, 1))
        self.assertTrue(state.can_reach("Reach Goal", "Entrance", 1))

    def test_unselected_event_does_not_contribute(self):
        state = CollectionState(self.multiworld)
        state.prog_items[1].clear()
        unselected = next(key for key in MAP_BY_KEY if key not in self.world.selected_map_keys)
        name = f"{map_label(MAP_BY_KEY[unselected])} Cleared"
        state.collect(Quake3Item(name, ItemClassification.progression, None, 1))
        self.assertFalse(state.can_reach("Reach Goal", "Entrance", 1))


class TestQuadTokenGoal(Quake3TestBase):
    options = {
        "map_pool_size": 1,
        "goal": "quad_token_hunt",
        "quad_token_pool_percentage": 25,
        "quad_token_goal_percentage": 50,
    }

    def test_required_token_count_reaches_goal(self):
        state = CollectionState(self.multiworld)
        state.prog_items[1].clear()
        for _ in range(self.world.goal_required - 1):
            state.collect(Quake3Item("Quad Token", ItemClassification.progression, 3370301, 1))
        self.assertFalse(state.can_reach("Reach Goal", "Entrance", 1))
        state.collect(Quake3Item("Quad Token", ItemClassification.progression, 3370301, 1))
        self.assertTrue(state.can_reach("Reach Goal", "Entrance", 1))

    def test_token_pool_matches_generated_total(self):
        self.assertEqual(sum(item.name == "Quad Token" for item in self.multiworld.itempool),
                         self.world.quad_token_total)
