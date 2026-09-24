"""Thunderbird's optional AP boss check."""

import json

from BaseClasses import CollectionState
from test.bases import WorldTestBase


class TestThunderbirdBossItem(WorldTestBase):
    game = "ZALiA"
    options = {"boss_item_locations": True, "crystals_required_count": 6}

    def test_check_and_fight_rule(self):
        loc = self.multiworld.get_location("Great Palace: Thunderbird Boss Item", self.player)
        self.assertIsNotNone(loc.address)
        self.assertFalse(loc.locked)
        ids = json.loads(self.world.fill_slot_data()["boss_item_location_ids"])
        self.assertEqual(ids["7"], loc.address)

        state = CollectionState(self.multiworld)
        for item in ("AllKey", "Glove", "Skill: Stab Down"):
            state.collect(self.world.create_item(item), prevent_sweep=True)
        self.assertFalse(loc.access_rule(state))
        state.collect(self.world.create_item("Spell: Thunder"), prevent_sweep=True)
        self.assertTrue(loc.access_rule(state))
