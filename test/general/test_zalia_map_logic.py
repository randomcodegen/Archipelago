import json
import random
import unittest
from collections import Counter

from BaseClasses import CollectionState
from test.general import setup_multiworld
from worlds.zalia import ZALiAWorld


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
