from .bases import Quake3TestBase
from ..rules import required_count


def test_required_unique_rounding():
    assert required_count(7, 0) == 0
    assert required_count(3, 1) == 1
    assert required_count(3, 50) == 2
    assert required_count(3, 100) == 3


class TestStartingLogicZero(Quake3TestBase):
    options = {"weapon_logic_percentage": 0, "item_logic_percentage": 0}

    def test_starting_stage_reachable(self):
        self.assertTrue(self.can_reach_entrance(f"Enter {self.world.starting_map_key}"))


class TestStartingLogicFull(Quake3TestBase):
    options = {"weapon_logic_percentage": 100, "item_logic_percentage": 100}

    def test_starting_stage_reachable(self):
        self.assertTrue(self.can_reach_entrance(f"Enter {self.world.starting_map_key}"))


class TestPickupUnlockLogic(Quake3TestBase):
    options = {"weapon_logic_percentage": 0, "item_logic_percentage": 0}

    def test_hidden_pickup_requires_its_unlock(self):
        from ..data.generated import MAP_BY_KEY

        pickup = MAP_BY_KEY[self.world.starting_map_key]["pickups"][0]
        self.assertFalse(self.can_reach_location(pickup["location_name"]))
        self.collect_by_name(f"{pickup['family']} Unlock")
        self.assertTrue(self.can_reach_location(pickup["location_name"]))
