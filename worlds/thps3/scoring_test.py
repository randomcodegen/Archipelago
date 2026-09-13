from itertools import combinations
from types import SimpleNamespace
from unittest import TestCase

from .data import OBJECTIVE_REQUIREMENTS, TRICK_CATEGORY_ITEMS
from .rules import _meets_requirement


class TestScoringRequirements(TestCase):
    def test_scoring_combinations(self):
        goals = {
            "High Score", "Pro Score", "Sick Score",
            "Bronze Medal", "Silver Medal", "Gold Medal",
            "Impress the Skaters", "Impress the Neversoft Girls",
        }
        requirements = [
            (level, name, requirement)
            for level, entries in OBJECTIVE_REQUIREMENTS.items()
            for name, requirement in entries.items()
            if name in goals
        ]
        self.assertEqual(len(requirements), 29)
        routes = (
            {"Grind Tricks", "Manual Tricks"},
            {"Grab Tricks", "Reverts", "Manual Tricks"},
        )
        hardest = {
            ("airport", "Sick Score"), ("los_angeles", "Sick Score"),
            ("cruise_ship", "Sick Score"), ("tokyo", "Gold Medal"),
        }
        lip_route = {"Lip Tricks", "Reverts", "Manual Tricks"}
        world = SimpleNamespace(player=1)
        # All 128 inventories cover missing links, extra tricks, and the harder goals.
        for size in range(len(TRICK_CATEGORY_ITEMS) + 1):
            for inventory in combinations(TRICK_CATEGORY_ITEMS, size):
                state = SimpleNamespace(has=lambda item, player: item in inventory)
                for level, name, requirement in requirements:
                    expected = any(route <= set(inventory) for route in routes) or (
                        (level, name) not in hardest and lip_route <= set(inventory)
                    )
                    if (level, name) == ("foundry", "High Score"):
                        expected = bool(set(inventory) & {
                            "Grind Tricks", "Grab Tricks", "Flip Tricks", "Lip Tricks",
                        })
                    for style in ("street", "vert"):
                        with self.subTest(inventory=inventory, level=level, goal=name, style=style):
                            self.assertEqual(
                                _meets_requirement(state, requirement, world, level, style),
                                expected,
                            )

