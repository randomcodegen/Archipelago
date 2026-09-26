from test.bases import WorldTestBase
from ..catalog import (AMMO_FILLERS, AS_MAPS, CTF_MAPS, DM_MAPS, DOM_MAPS, MAPS,
                       ITEM_NAME_TO_ID, LOCATION_NAME_TO_ID, PICKUPS, objective_labels,
                       PICKUP_CLASS_FAMILY, PICKUP_FAMILIES, PICKUP_TYPE_CLASSES,
                       PICKUP_TYPE_NAMES, PICKUP_NAMES, PICKUP_BASE, TEAM_FRAG_BASE, WEAPONS)
from .. import UT99World


class TestUT99(WorldTestBase):
    game = "Unreal Tournament 99"

    def test_pool_and_start(self):
        self.assertEqual(len(self.multiworld.itempool),
                         sum(1 + len(objective_labels(name, self.world.frag_checks)) +
                             (self.world.frag_checks if name in MAPS[37:] else 0)
                             for name in self.world.selected_maps) +
                         sum(MAPS[p["map"]] in self.world.selected_maps for p in PICKUPS))
        self.assertTrue(self.can_reach_location(f"{self.world.starting_map} - Win"))
        locked = next(name for name in self.world.selected_maps if name != self.world.starting_map)
        self.assertFalse(self.can_reach_location(f"{locked} - Win"))
        self.collect(self.world.create_item(f"{locked} Unlock"))
        for weapon in self.world.stage_weapons[locked]:
            self.collect(self.world.create_item(weapon))
        self.assertTrue(self.can_reach_location(f"{locked} - Win"))

    def test_slot_contract(self):
        data = self.world.fill_slot_data()
        self.assertIn(data["starting_map"], data["selected_maps"])
        self.assertEqual(len(data["selected_maps"]), 10)
        self.assertEqual(data["goal_required"], 5)
        self.assertEqual(data["schema_version"], 11)
        self.assertEqual(data["weapon_logic_percentage"], 25)
        self.assertFalse(data["death_link"])
        self.assertEqual(data["pickup_locations"], sorted(
            PICKUP_BASE + i for i in self.world.included_pickups))
        self.assertEqual(len(set(ITEM_NAME_TO_ID.values())), len(ITEM_NAME_TO_ID))
        self.assertEqual(len(set(LOCATION_NAME_TO_ID.values())), len(LOCATION_NAME_TO_ID))
        self.assertEqual(ITEM_NAME_TO_ID["Health Refill"], 19990201)
        self.assertEqual(ITEM_NAME_TO_ID["Armor Refill"], 19990202)
        self.assertNotIn("Ammo Refill", ITEM_NAME_TO_ID)
        self.assertNotIn("Nothing", ITEM_NAME_TO_ID)
        self.assertEqual(ITEM_NAME_TO_ID["+2 Flak Shells"], 19990209)
        self.assertEqual(tuple(amount for _, amount, _ in AMMO_FILLERS),
                         (2, 5, 5, 5, 10, 2, 2, 2, 1))
        self.assertTrue({"Nothing", "Ammo Refill"}.isdisjoint(
            item.name for item in self.multiworld.itempool))
        available = {unlock[:-7] for name in self.world.selected_maps
                     for unlock in self.world.stage_weapons[name]}
        self.assertEqual(set(self.world.filler_items),
                         {"Health Refill", "Armor Refill"} |
                         {filler for (weapon, _), (filler, _, _) in zip(
                             WEAPONS, AMMO_FILLERS) if weapon in available})
        self.assertIn(self.world.get_filler_item_name(), self.world.filler_items)

    def test_goal(self):
        from BaseClasses import CollectionState
        state = CollectionState(self.multiworld)
        state.prog_items[self.player].clear()
        for name in self.world.selected_maps[:self.world.goal_required - 1]:
            state.prog_items[self.player][f"{name} Cleared"] = 1
        self.assertFalse(self.multiworld.completion_condition[self.player](state))
        state.prog_items[self.player][f"{self.world.selected_maps[-1]} Cleared"] = 1
        self.assertTrue(self.multiworld.completion_condition[self.player](state))


class TestSmallPool(TestUT99):
    options = {"included_maps": list(MAPS[:2]), "map_pool_size": 2, "goal_percentage": 100}

    def test_slot_contract(self):
        self.assertEqual(self.world.fill_slot_data()["goal_required"], 2)
        self.assertEqual(len(self.multiworld.itempool), 10 + sum(p["map"] < 2 for p in PICKUPS))


class TestFullPool(TestUT99):
    options = {"map_pool_size": len(MAPS), "goal_percentage": 1, "frag_check_increment": 25,
               "match_frag_limit": 100}

    def test_slot_contract(self):
        self.assertEqual(self.world.fill_slot_data()["goal_required"], 1)
        self.assertEqual(len(self.multiworld.itempool),
                         sum(1 + len(objective_labels(name, 4)) + (4 if name in MAPS[37:] else 0)
                             for name in MAPS) + len(PICKUPS))


def test_kill_check_spacing():
    from test.general import setup_multiworld
    for increment, limit in [(1, 20), (2, 20), (3, 20), (1, 100)]:
        multiworld = setup_multiworld(UT99World, options={
            "included_maps": list(DM_MAPS[:2]), "map_pool_size": 2,
            "frag_check_increment": increment, "match_frag_limit": limit})
        world = multiworld.worlds[1]
        assert world.fill_slot_data()["match_frag_limit"] == limit
        locations = [loc for loc in multiworld.get_locations() if loc.address is not None]
        pickups = sum(MAPS[p["map"]] in world.selected_maps for p in PICKUPS)
        assert len(locations) == 2 * (1 + limit // increment) + pickups == len(multiworld.itempool)
        for name in world.selected_maps:
            assert multiworld.get_location(f"{name} - Frag Milestone {limit // increment}", 1)
        from Fill import distribute_items_restrictive
        distribute_items_restrictive(multiworld)
        assert multiworld.can_beat_game()
    for i, name in enumerate(DM_MAPS):
        assert LOCATION_NAME_TO_ID[f"{name} - Win"] == 19991000 + i * 101
        for step in range(1, 101):
            assert LOCATION_NAME_TO_ID[f"{name} - Frag Milestone {step}"] == 19991000 + i * 101 + step
    assert LOCATION_NAME_TO_ID[f"{DM_MAPS[-1]} - Frag Milestone 100"] == 19994736
    assert len(set(LOCATION_NAME_TO_ID.values())) == len(LOCATION_NAME_TO_ID)


def test_ctf_dom_assault_locations():
    from Fill import distribute_items_restrictive
    from test.general import setup_multiworld

    names = [DM_MAPS[0], CTF_MAPS[0], DOM_MAPS[0], AS_MAPS[0]]
    multiworld = setup_multiworld(UT99World, options={
        "included_maps": names, "map_pool_size": 4,
        "maximum_starting_weapons": 9, "custom_included_locations": {},
    })
    world = multiworld.worlds[1]
    assert set(world.selected_maps) == set(names)
    for name in names:
        index = MAPS.index(name)
        base = 19991000 + (index * 101 if index < 37 else 3737 + (index - 37) * 20)
        assert LOCATION_NAME_TO_ID[f"{name} - Win"] == base
        for step, label in enumerate(objective_labels(name, world.frag_checks), 1):
            assert multiworld.get_location(f"{name} - {label}", 1).address == base + step
        if index >= 37:
            for step in range(1, world.frag_checks + 1):
                assert multiworld.get_location(f"{name} - Frag Milestone {step}", 1).address == (
                    TEAM_FRAG_BASE + (index - 37) * 101 + step)
    assert objective_labels(CTF_MAPS[0]) == ["Capture 1", "Capture 2", "Capture 3"]
    assert objective_labels(DOM_MAPS[0]) == ["Score 25", "Score 50", "Score 75", "Score 100"]
    assert len(objective_labels(AS_MAPS[0])) == 3
    distribute_items_restrictive(multiworld)
    assert multiworld.can_beat_game()


def test_pickup_catalog_and_access():
    from test.general import setup_multiworld
    from BaseClasses import CollectionState
    multiworld = setup_multiworld(UT99World, options={"map_pool_size": 2, "frag_check_increment": 25})
    world = multiworld.worlds[1]
    assert world.fill_slot_data()["pickup_catalog_version"] == 2
    assert 0 < len(PICKUPS) < 5000 and len(set(PICKUP_NAMES)) == len(PICKUPS)
    state = CollectionState(multiworld)
    for i, (pickup, name) in enumerate(zip(PICKUPS, PICKUP_NAMES)):
        assert LOCATION_NAME_TO_ID[name] == PICKUP_BASE + i
        assert len(pickup["position"]) == 3 and pickup["radius"] > 0 and pickup["height"] > 0
        if MAPS[pickup["map"]] in world.selected_maps:
            loc = multiworld.get_location(name, 1)
            family = PICKUP_CLASS_FAMILY[pickup["class"].lower()] + " Unlock"
            assert loc.can_reach(state) == (MAPS[pickup["map"]] == world.starting_map and
                                            state.has(family, world.player))
    pickup = next(p for p in PICKUPS if MAPS[p["map"]] == world.starting_map)
    family = PICKUP_CLASS_FAMILY[pickup["class"].lower()] + " Unlock"
    location = multiworld.get_location(f"{world.starting_map} - Pickup {pickup['actor']}", 1)
    state.prog_items[world.player].pop(family, None)
    assert not location.can_reach(state)
    state.prog_items[world.player][family] = 1
    assert location.can_reach(state)
    assert len(PICKUP_FAMILIES) == 8
    from Fill import distribute_items_restrictive
    distribute_items_restrictive(multiworld)
    assert multiworld.can_beat_game()


def test_custom_included_locations():
    from test.general import setup_multiworld
    classname = "Botpack.MedBox"
    multiworld = setup_multiworld(UT99World, options={
        "included_maps": list(MAPS[:2]),
        "map_pool_size": 2,
        "match_frag_limit": 1,
        "custom_included_locations": {classname: 100},
    })
    world = multiworld.worlds[1]
    expected = {
        i for i, pickup in enumerate(PICKUPS)
        if pickup["map"] < 2 and pickup["class"] == classname
    }
    assert world.included_pickups == expected
    assert world.fill_slot_data()["pickup_locations"] == sorted(PICKUP_BASE + i for i in expected)
    locations = {location.address for location in multiworld.get_locations(1)}
    assert {PICKUP_BASE + i for i in range(len(PICKUPS))} & locations == {
        PICKUP_BASE + i for i in expected
    }


def test_pickup_type_unlocks():
    from test.general import setup_multiworld
    from BaseClasses import CollectionState
    from Fill import distribute_items_restrictive
    multiworld = setup_multiworld(UT99World, options={
        "included_maps": list(MAPS[:2]), "map_pool_size": 2,
        "pickup_unlock_mode": "type", "frag_check_increment": 25,
    })
    world = multiworld.worlds[1]
    assert world.fill_slot_data()["pickup_unlock_mode"] == 1
    assert world.create_item("Flak Cannon Unlock").classification.name == "progression"
    assert world.create_item("Med Box Pickup Unlock").classification.name == "progression"
    pickup = next(p for p in PICKUPS if MAPS[p["map"]] == world.starting_map)
    classname = pickup["class"].lower()
    unlock = PICKUP_TYPE_NAMES[PICKUP_TYPE_CLASSES.index(classname)]
    location = multiworld.get_location(f"{world.starting_map} - Pickup {pickup['actor']}", 1)
    state = CollectionState(multiworld)
    state.prog_items[1][PICKUP_CLASS_FAMILY[classname] + " Unlock"] = 1
    assert not location.can_reach(state)
    state.prog_items[1][unlock] = 1
    assert location.can_reach(state)
    distribute_items_restrictive(multiworld)
    assert multiworld.can_beat_game()


def test_no_pickup_locations_still_fills():
    from Fill import distribute_items_restrictive
    from test.general import setup_multiworld
    multiworld = setup_multiworld(UT99World, options={
        "included_maps": list(MAPS[:2]),
        "map_pool_size": 2,
        "frag_check_increment": 25,
        "match_frag_limit": 1,
        "custom_included_locations": {},
    })
    assert not multiworld.worlds[1].included_pickups
    distribute_items_restrictive(multiworld)
    assert multiworld.can_beat_game()


def test_weapon_logic_and_starting_cap():
    from BaseClasses import CollectionState
    from Fill import distribute_items_restrictive
    from Options import OptionError
    from test.general import setup_multiworld
    import pytest

    for percentage in (0, 50, 100):
        multiworld = setup_multiworld(UT99World, options={
            "included_maps": ["DM-Fractal", "DM-Barricade"], "map_pool_size": 2,
            "weapon_logic_percentage": percentage, "maximum_starting_weapons": 9,
        })
        world = multiworld.worlds[1]
        assert world.fill_slot_data()["weapon_logic_percentage"] == percentage
        required = (len(world.stage_weapons[world.starting_map]) * percentage + 99) // 100
        starting = {item.name for item in multiworld.precollected_items[1]}
        assert world.starting_map + " Unlock" in starting
        assert len(starting.intersection(world.stage_weapons[world.starting_map])) == required
        assert multiworld.get_entrance(f"Enter {world.starting_map}", 1).can_reach(CollectionState(multiworld))
        other = next(name for name in world.selected_maps if name != world.starting_map)
        needed = (len(world.stage_weapons[other]) * percentage + 99) // 100
        for held in (max(0, needed - 1), needed):
            state = CollectionState(multiworld)
            state.prog_items[1].clear()
            state.prog_items[1][other + " Unlock"] = 1
            for weapon in world.stage_weapons[other][:held]:
                state.prog_items[1][weapon] = 1
            assert multiworld.get_entrance(f"Enter {other}", 1).can_reach(state) == (held >= needed)
        distribute_items_restrictive(multiworld)
        assert multiworld.can_beat_game()

    constrained = setup_multiworld(UT99World, options={
        "included_maps": ["DM-Fractal", "DM-Barricade"], "map_pool_size": 2,
        "weapon_logic_percentage": 100, "maximum_starting_weapons": 2,
    })
    assert constrained.worlds[1].starting_map == "DM-Fractal"
    with pytest.raises(OptionError, match="Maximum Starting Weapons"):
        setup_multiworld(UT99World, options={
            "included_maps": ["DM-Barricade", "DM-Conveyor"], "map_pool_size": 2,
            "weapon_logic_percentage": 100, "maximum_starting_weapons": 2,
        })


def test_multiworld_fill():
    from test.general import setup_multiworld
    from Fill import distribute_items_restrictive
    from worlds.apquest import APQuestWorld
    for seed in range(10):
        world = setup_multiworld([UT99World, UT99World, APQuestWorld], seed=seed,
                                 options=[{"map_pool_size": 2}, {"map_pool_size": len(MAPS)}, {}])
        distribute_items_restrictive(world)
        assert not world.get_unfilled_locations()
        assert world.can_beat_game()


def test_invalid_pool():
    import pytest
    from Options import OptionError
    from test.general import setup_multiworld
    with pytest.raises(OptionError, match="at least two"):
        setup_multiworld(UT99World, options={"included_maps": [MAPS[0]]})
