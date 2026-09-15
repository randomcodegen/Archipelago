import inspect
import json
import random
import unittest
from collections import Counter
from unittest.mock import patch

from BaseClasses import CollectionState
from test.general import setup_multiworld
from worlds.zalia import ZALiAWorld
from worlds.zalia.Constants import (ITEM_BRACELET, ITEM_GLOVE, ITEM_KEY, KEY_MIDORO,
                                    KEY_THREE_EYE, SKILL_STAB_UP)


def evaluate(data, items):
    reached = {data['start']}
    while True:
        values = []
        for op, *args in data['nodes']:
            if op == 'const': value = args[0]
            elif op == 'item': value = items[args[0]]
            elif op == 'region': value = args[0] in reached
            else:
                a = [values[i] for i in args]
                if op == '&': value = bool(a[0] and a[1])
                elif op == '|': value = bool(a[0] or a[1])
                elif op == '+': value = a[0] + a[1]
                elif op == '>=': value = a[0] >= a[1]
                elif op == '!': value = not a[0]
                elif op == '?': value = a[1] if a[0] else a[2]
                else: raise AssertionError(op)
            values.append(value)
        more = {target for source, target, rule in data['entrances']
                if source in reached and values[rule]}
        if more <= reached:
            return {loc for loc, parent, rule in data['locations']
                    if parent in reached and values[rule]}
        reached |= more


class TestMapLogic(unittest.TestCase):
    def test_three_eye_first_key_gates(self):
        tools = {ITEM_BRACELET, ITEM_GLOVE, SKILL_STAB_UP}
        for keysanity in (0, 1):
            mw = setup_multiworld(ZALiAWorld, seed=914, options={
                'randomize_key_locations': keysanity,
                'randomize_dungeon_locations': 0, 'randomize_town_locations': 0,
            })
            world = mw.worlds[1]
            data = json.loads(world.fill_slot_data()['map_logic'])
            locations = [mw.get_location(name, 1) for name in (
                'P6 Key 4 (falling key)', 'P6 PBag: Endless pit 3',
                'P6 PBag: Falling key room')]
            for missing, key in [(set(), None), *[({tool}, None) for tool in sorted(tools)],
                                 (tools, ITEM_KEY), (tools, KEY_THREE_EYE)]:
                with self.subTest(keysanity=keysanity, missing=missing, key=key):
                    counts = Counter({name: 10 for name in world.item_name_to_id
                                      if name not in missing | {ITEM_KEY, KEY_THREE_EYE}})
                    if key:
                        counts[key] = 1
                    state = CollectionState(mw)
                    for name in counts.elements():
                        state.collect(world.create_item(name), prevent_sweep=True)
                    expected = key == ITEM_KEY or (key == KEY_THREE_EYE if keysanity else not missing)
                    reached = evaluate(data, counts)
                    for loc in locations:
                        self.assertEqual(loc.access_rule(state), expected, loc.name)
                        self.assertEqual(loc.address in reached, expected, loc.name)

    def test_midoro_pbags_require_three_keys(self):
        for randomized_keys in (0, 1):
            mw = setup_multiworld(ZALiAWorld, seed=914, options={
                'randomize_key_locations': randomized_keys,
                'randomize_dungeon_locations': 0, 'randomize_town_locations': 0,
            })
            world = mw.worlds[1]
            data = json.loads(world.fill_slot_data()['map_logic'])
            locations = [mw.get_location(name, 1) for name in (
                'PBag: P2 falling-block room', 'PBag: P2 Iron Knuckle room')]
            for keys, allkey, glove in ((0, 0, 1), (1, 0, 1), (2, 0, 1), (3, 0, 1),
                                        (0, 1, 1), (3, 0, 0), (0, 1, 0)):
                with self.subTest(randomized_keys=randomized_keys, keys=keys,
                                  allkey=allkey, glove=glove):
                    counts = Counter({KEY_MIDORO: keys, ITEM_KEY: allkey, ITEM_GLOVE: glove})
                    state = CollectionState(mw)
                    for name in counts.elements():
                        state.collect(world.create_item(name), prevent_sweep=True)
                    expected = bool(glove and (not randomized_keys or keys >= 3 or allkey))
                    reached = evaluate(data, counts)
                    for loc in locations:
                        self.assertEqual(loc.access_rule(state), expected, loc.name)
                        self.assertEqual(loc.address in reached, expected, loc.name)

    def test_export_without_core_source(self):
        mw = setup_multiworld([ZALiAWorld, ZALiAWorld], seed=914, options=[{}, {
            'starting_quest': 2, 'randomize_key_locations': 1,
            'randomize_town_locations': 1, 'randomize_dungeon_locations': 1,
            'boss_item_locations': 1, 'kakusu_individual_location_count': 12,
        }])
        expected = [world.fill_slot_data()['map_logic'] for world in mw.worlds.values()]
        getsource = inspect.getsource

        def packaged_source(module):
            if not module.__name__.startswith('worlds.zalia.'):
                raise OSError('could not get source code')
            return getsource(module)

        with patch('worlds.zalia.MapLogic.inspect.getsource', side_effect=packaged_source):
            actual = [world.fill_slot_data()['map_logic'] for world in mw.worlds.values()]
        self.assertEqual(actual, expected)

    def test_export_matches_ap_reachability(self):
        rng = random.Random(2901)
        for options in ({}, {'starting_quest': 2, 'randomize_key_locations': 1,
                             'randomize_town_locations': 1, 'randomize_dungeon_locations': 1,
                             'boss_item_locations': 1, 'kakusu_individual_location_count': 12},
                        {'hard_logic_tricks': 1, 'dark_room_difficulty': 2,
                         'randomize_key_locations': 0, 'crystals_required_count': 0}):
            mw = setup_multiworld(ZALiAWorld, seed=914, options=options)
            data = json.loads(mw.worlds[1].fill_slot_data()['map_logic'])
            pool = list(mw.itempool)
            for probability in (0, .2, .5, .8, 1):
                for _ in range(6):
                    state = CollectionState(mw)
                    counts = Counter(item.name for item in mw.precollected_items[1])
                    for item in pool:
                        if rng.random() < probability:
                            state.collect(item, prevent_sweep=True)
                            counts[item.name] += 1
                    expected = {loc.address for loc in mw.get_locations(1)
                                if loc.address is not None and loc.can_reach(state)}
                    self.assertEqual(evaluate(data, counts), expected, (options, probability))
