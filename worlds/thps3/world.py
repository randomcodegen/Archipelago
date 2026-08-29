from __future__ import annotations

from collections.abc import Mapping
from random import Random
from typing import Any

from Options import OptionError
from worlds.AutoWorld import World

from . import items, locations, regions, rules
from .data import (
    CLIENT_PROTOCOL_VERSION,
    DECK_BY_LEVEL,
    DECKS,
    GAME_NAME,
    GAPS_BY_LEVEL,
    GOAL_BY_LEVEL_AND_ID,
    GOALS_BY_LEVEL,
    HIDDEN_DECK_REQUIREMENTS,
    LEVELS,
    NORMAL_GOAL_NAMES,
    OBJECTIVE_REQUIREMENTS,
    SKATE_LETTER_REQUIREMENTS,
    SKATER_BY_NAME,
    SKATER_LAYOUTS,
    STAT_POINT_REQUIREMENTS,
    STAT_POINTS_BY_LEVEL,
    GapData,
    GoalData,
    LevelData,
    select_all_gap_checks,
    select_skater,
)
from .options import THPS3Options
from .web_world import THPS3WebWorld


class THPS3World(World):
    """
    Skate through Tony Hawk's Pro Skater 3 while Archipelago controls access to
    levels, career goals, trick categories, gaps, and the selected pro skater.
    """

    game = GAME_NAME
    ut_can_gen_without_yaml = True
    web = THPS3WebWorld()
    options_dataclass = THPS3Options
    options: THPS3Options

    item_name_to_id = items.ITEM_NAME_TO_ID
    location_name_to_id = locations.LOCATION_NAME_TO_ID

    item_name_groups = {
        "Level Access": set(items.LEVEL_ACCESS_ITEMS.values()),
        "Objective Unlocks": set(items.GOAL_UNLOCK_ITEMS),
        "Trick Categories": set(items.TRICK_CATEGORY_ITEMS),
    }
    location_name_groups = {
        level.name: {
            *(
                goal.location_name
                for goal in GOALS_BY_LEVEL[level.key]
            ),
            *(
                stat_point.location_name
                for stat_point in STAT_POINTS_BY_LEVEL[level.key]
            ),
            *(
                gap.location_name
                for gap in GAPS_BY_LEVEL[level.key]
            ),
            DECK_BY_LEVEL[level.key].location_name,
        }
        for level in LEVELS
    }

    selected_skater_name: str
    starting_level_key: str
    active_levels: tuple[LevelData, ...]
    active_level_keys: frozenset[str]
    selected_gaps: tuple[GapData, ...]
    selected_goals: tuple[GoalData, ...]
    goal_unlocks: tuple[GoalData, ...]
    required_gap_count: int
    enabled_location_types: frozenset[str]

    def __init__(self, multiworld, player: int) -> None:
        super().__init__(multiworld, player)
        passthrough = getattr(multiworld, "re_gen_passthrough", {}).get(self.game, {})
        self.ut_seed = passthrough.get("ut_seed", self.random.getrandbits(64))
        self.random = Random(self.ut_seed)

    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        return slot_data

    def generate_early(self) -> None:
        passthrough = getattr(self.multiworld, "re_gen_passthrough", {}).get(self.game, {})
        for name, value in passthrough.get("options", {}).items():
            setattr(self.options, name, self.options_dataclass.type_hints[name].from_any(value))

        pool = sorted(self.options.skater_pool.value, key=str.casefold)
        if not pool:
            raise OptionError("skater_pool must contain at least one skater")
        if not self.options.filler_item_weights:
            raise OptionError("filler_item_weights must contain at least one item")

        requested_levels = {
            name for name, enabled in self.options.level_pool.value.items() if enabled
        }
        eligible_levels = tuple(
            level for level in LEVELS if level.name in requested_levels
        )
        if not eligible_levels:
            raise OptionError("level_pool must enable at least one level")
        level_count = int(self.options.level_pool_size)
        if level_count > len(eligible_levels):
            raise OptionError(
                f"level_pool_size exceeds the {len(eligible_levels)} eligible levels"
            )
        selected_level_keys = {
            level.key for level in (
                self.random.sample(eligible_levels, level_count)
                if level_count else eligible_levels
            )
        }
        self.active_levels = tuple(
            level for level in LEVELS if level.key in selected_level_keys
        )
        self.active_level_keys = frozenset(level.key for level in self.active_levels)

        self.selected_skater_name = select_skater(pool, self.random)
        layouts = SKATER_LAYOUTS[SKATER_BY_NAME[self.selected_skater_name].key]
        opening_levels = [
            level for level in self.active_levels
            if any(
                requirement == []
                for requirement in OBJECTIVE_REQUIREMENTS[level.key].values()
            )
        ]
        self.starting_level_key = self.random.choice(
            opening_levels or self.active_levels
        ).key
        completion_mode = self.options.completion_goal.current_key
        goal_type_id = (
            int(self.options.completion_goal_type)
            if completion_mode == "goal_type" else None
        )
        max_goals = int(self.options.max_objectives_per_level)
        selected_goals: list[GoalData] = []
        for level in self.active_levels:
            goals = GOALS_BY_LEVEL[level.key]
            if len(goals) <= max_goals:
                selected_goals.extend(goals)
                continue
            forced = []
            if goal_type_id is not None and not level.competition:
                forced.append(next(goal for goal in goals if goal.goal_id == goal_type_id))
            if completion_mode == "gold_medals" and level.competition:
                forced.append(next(goal for goal in goals if goal.name == "Gold Medal"))
            if level.key == self.starting_level_key:
                opening = next(
                    (goal for goal in goals
                     if (
                         SKATE_LETTER_REQUIREMENTS[str(layouts["skate"])][level.key]
                         if goal.name == "Collect S-K-A-T-E"
                         else OBJECTIVE_REQUIREMENTS[level.key][goal.name]
                     ) == []),
                    goals[0],
                )
                if opening not in forced and len(forced) < max_goals:
                    forced.append(opening)
            chosen = {
                *forced,
                *self.random.sample(
                    [goal for goal in goals if goal not in forced],
                    max_goals - len(forced),
                ),
            }
            selected_goals.extend(goal for goal in goals if goal in chosen)
        self.selected_goals = tuple(selected_goals)
        requested_location_types = {
            name
            for name, enabled in self.options.location_type_filter.value.items()
            if enabled
        }
        self.enabled_location_types = frozenset({
            *(name for name in ("objectives",)
              if name in requested_location_types),
            *({"gaps"} if "gaps" in requested_location_types
              and int(self.options.gap_checks_percentage) else set()),
            *({"stat points"} if "stat points" in requested_location_types
              and self.options.stat_point_checks else set()),
            *({"hidden decks"} if "hidden decks" in requested_location_types
              and self.options.hidden_deck_checks else set()),
        })
        gap_percentage = (
            int(self.options.gap_checks_percentage)
            if "gaps" in self.enabled_location_types else 0
        )
        if gap_percentage and not any(GAPS_BY_LEVEL.values()):
            raise OptionError(
                "gap_checks_percentage cannot be enabled until the verified "
                "THPS3 gap checksum catalogue is installed"
            )
        self.selected_gaps = select_all_gap_checks(
            gap_percentage,
            self.random,
            {
                level.key: (
                    GAPS_BY_LEVEL[level.key]
                    if level.key in self.active_level_keys else ()
                )
                for level in LEVELS
            },
        )
        required_goal_keys = {
            (goal.level_key, goal.goal_id) for goal in self.selected_goals
        }

        def add_requirement_goals(level_key: str, requirement: Any) -> None:
            if isinstance(requirement, list):
                for entry in requirement:
                    add_requirement_goals(level_key, entry)
            elif isinstance(requirement, dict):
                if "goal_id" in requirement:
                    required_goal_keys.add((level_key, requirement["goal_id"]))
                for key in ("any", "all", "street", "vert"):
                    add_requirement_goals(level_key, requirement.get(key, []))

        if "objectives" in self.enabled_location_types:
            for goal in self.selected_goals:
                add_requirement_goals(
                    goal.level_key,
                    SKATE_LETTER_REQUIREMENTS[str(layouts["skate"])][goal.level_key]
                    if goal.name == "Collect S-K-A-T-E"
                    else OBJECTIVE_REQUIREMENTS[goal.level_key][goal.name],
                )
        for level in self.active_levels:
            if "stat points" in self.enabled_location_types:
                for requirement in STAT_POINT_REQUIREMENTS[str(layouts["stats"])][
                    level.key
                ].values():
                    add_requirement_goals(level.key, requirement)
            if "hidden decks" in self.enabled_location_types:
                add_requirement_goals(
                    level.key,
                    HIDDEN_DECK_REQUIREMENTS[str(layouts["deck"])][level.key],
                )
        for gap in self.selected_gaps:
            required_goal_keys.update(
                (gap.level_key, goal_id) for goal_id in gap.required_goal_ids
            )
        self.goal_unlocks = tuple(
            GOAL_BY_LEVEL_AND_ID[key] for key in sorted(required_goal_keys)
        )
        self.required_gap_count = (
            len(self.selected_gaps) * int(self.options.required_gap_percentage) + 99
        ) // 100
        location_counts = {
            "objectives": (
                len(self.selected_goals)
                if "objectives" in self.enabled_location_types else 0
            ),
            "gaps": len(self.selected_gaps),
            "stat points": (
                5 * len(self.active_levels)
                if "stat points" in self.enabled_location_types else 0
            ),
            "hidden decks": (
                len(self.active_levels)
                if "hidden decks" in self.enabled_location_types else 0
            ),
        }
        if not sum(location_counts.values()):
            raise OptionError("location_type_filter must enable at least one location")
        if completion_mode in {
            "objectives", "levels", "cruise_ship", "gold_medals",
            "goal_type", "level_tour",
        } and not location_counts["objectives"]:
            raise OptionError(f"completion_goal '{completion_mode}' requires objective locations")
        if completion_mode == "gap_hunt" and not location_counts["gaps"]:
            raise OptionError("completion_goal 'gap_hunt' requires gap locations")
        if completion_mode == "cruise_ship" and "cruise_ship" not in self.active_level_keys:
            raise OptionError("completion_goal 'cruise_ship' requires Cruise Ship")
        if completion_mode == "goal_type" and not any(
            not level.competition for level in self.active_levels
        ):
            raise OptionError("completion_goal 'goal_type' requires a career level")
        available = {
            "objectives": location_counts["objectives"],
            "levels": len(self.active_levels),
            "gold_medals": sum(level.competition for level in self.active_levels),
            "collectibles": location_counts["stat points"] + location_counts["hidden decks"],
            "total_checks": sum(location_counts.values()),
        }
        required_option = {
            "objectives": "required_objectives",
            "levels": "required_levels",
            "gold_medals": "required_gold_medals",
            "collectibles": "required_collectibles",
            "total_checks": "required_checks",
        }.get(completion_mode)
        if required_option:
            option = getattr(self.options, required_option)
            option.value = min(option.value, available[completion_mode])

    def create_regions(self) -> None:
        regions.create_regions(self)
        locations.create_locations(self)

    def create_items(self) -> None:
        items.create_items(self)

    def create_item(self, name: str) -> items.THPS3Item:
        return items.create_item(self, name)

    def get_filler_item_name(self) -> str:
        weights = self.options.filler_item_weights
        return self.random.choices(
            items.FILLER_ITEMS,
            weights=[weights.get(name, 0) for name in items.FILLER_ITEMS],
        )[0]

    def set_rules(self) -> None:
        rules.set_rules(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        selected_skater = SKATER_BY_NAME[self.selected_skater_name]
        completion_mode = self.options.completion_goal.current_key
        completion_required = int({
            "objectives": self.options.required_objectives,
            "levels": self.options.required_levels,
            "cruise_ship": sum(
                goal.level_key == "cruise_ship" for goal in self.selected_goals
            ),
            "gold_medals": self.options.required_gold_medals,
            "goal_type": sum(not level.competition for level in self.active_levels),
            "gap_hunt": self.required_gap_count,
            "collectibles": self.options.required_collectibles,
            "total_checks": self.options.required_checks,
            "level_tour": min(
                int(self.options.required_objectives_per_level),
                int(self.options.max_objectives_per_level),
            ),
        }[completion_mode])
        return {
            "protocol_version": CLIENT_PROTOCOL_VERSION,
            "ut_seed": self.ut_seed,
            "options": self.options.as_dict(
                "skater_pool",
                "level_pool",
                "level_pool_size",
                "gap_checks_percentage",
                "stat_point_checks",
                "hidden_deck_checks",
                "location_type_filter",
                "filler_item_weights",
                "max_objectives_per_level",
                "completion_goal",
                "completion_goal_type",
                "required_objectives",
                "required_levels",
                "required_gold_medals",
                "required_gap_percentage",
                "required_collectibles",
                "required_checks",
                "required_objectives_per_level",
            ),
            "selected_skater": {
                "key": selected_skater.key,
                "name": selected_skater.name,
            },
            "stat_points_are_locations": (
                "stat points" in self.enabled_location_types
            ),
            "hidden_decks_are_locations": (
                "hidden decks" in self.enabled_location_types
            ),
            "active_gaps": [
                {
                    "level": gap.level_key,
                    "checksum": gap.checksum,
                    "name": gap.name,
                    "location_id": locations.GAP_LOCATION_NAME_TO_ID[gap.location_name],
                    "any_items": sorted(gap.required_trick_items),
                    "all_items": sorted(gap.required_all_trick_items),
                    "goal_items": [
                        GOAL_BY_LEVEL_AND_ID[(gap.level_key, goal_id)].item_name
                        for goal_id in sorted(gap.required_goal_ids)
                    ],
                }
                for gap in self.selected_gaps
            ],
            "goal_locations": [
                {
                    "level": goal.level_key,
                    "goal_id": goal.goal_id,
                    "name": goal.name,
                    "item_name": goal.item_name,
                    "location_id": locations.GOAL_LOCATION_NAME_TO_ID[goal.location_name],
                    "precollected": "objectives" not in self.enabled_location_types,
                }
                for goal in self.selected_goals
            ],
            "goal_unlocks": [
                {
                    "level": goal.level_key,
                    "goal_id": goal.goal_id,
                    "item_name": goal.item_name,
                }
                for goal in self.goal_unlocks
            ],
            "stat_point_locations": [
                {
                    "level": stat_point.level_key,
                    "point_id": stat_point.point_id,
                    "location_id": locations.STAT_POINT_LOCATION_NAME_TO_ID[
                        stat_point.location_name
                    ],
                    "precollected": "stat points" not in self.enabled_location_types,
                }
                for level in self.active_levels
                for stat_point in STAT_POINTS_BY_LEVEL[level.key]
            ],
            "deck_locations": [
                {
                    "level": deck.level_key,
                    "location_id": locations.DECK_LOCATION_NAME_TO_ID[
                        deck.location_name
                    ],
                    "precollected": "hidden decks" not in self.enabled_location_types,
                }
                for deck in DECKS
                if deck.level_key in self.active_level_keys
            ],
            "levels": {
                level.key: {
                    "name": level.name,
                    "level_num": level.level_num,
                    "competition": level.competition,
                }
                for level in self.active_levels
            },
            "gap_checks_percentage": int(self.options.gap_checks_percentage),
            "collectible_markers_default": False,
            "completion_goal": {
                "mode": completion_mode,
                "required": completion_required,
                **({
                    "type": NORMAL_GOAL_NAMES[int(self.options.completion_goal_type)]
                } if completion_mode == "goal_type" else {}),
            },
        }
