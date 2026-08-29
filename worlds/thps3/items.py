from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

from .data import (
    GAME_NAME, GOALS, LEVELS, OBJECTIVE_REQUIREMENTS,
    TRICK_CATEGORY_ITEMS,
)

if TYPE_CHECKING:
    from .world import THPS3World


ITEM_ID_BASE = 30_300_000

SCORE_BONUS_ITEM = "Score Bonus"
TIME_BONUS_ITEM = "+1 Second"
FILLER_ITEMS = (SCORE_BONUS_ITEM, TIME_BONUS_ITEM)
STAT_POINT_ITEM = "Stat Point"
LEVEL_ACCESS_ITEMS = {
    level.key: f"{level.name} Access"
    for level in LEVELS
}
GOAL_UNLOCK_ITEMS = tuple(goal.item_name for goal in GOALS)

PROGRESSION_ITEM_NAMES: tuple[str, ...] = (
    *LEVEL_ACCESS_ITEMS.values(),
    *TRICK_CATEGORY_ITEMS,
    *GOAL_UNLOCK_ITEMS,
)

ALL_ITEM_NAMES: tuple[str, ...] = (
    *PROGRESSION_ITEM_NAMES,
    *FILLER_ITEMS,
    STAT_POINT_ITEM,
)

ITEM_NAME_TO_ID = {
    **{
        name: ITEM_ID_BASE + offset
        for offset, name in enumerate(LEVEL_ACCESS_ITEMS.values(), start=1)
    },
    **{
        name: ITEM_ID_BASE + offset
        for offset, name in enumerate(TRICK_CATEGORY_ITEMS, start=10)
    },
    SCORE_BONUS_ITEM: ITEM_ID_BASE + 17,
    STAT_POINT_ITEM: ITEM_ID_BASE + 18,
    TIME_BONUS_ITEM: ITEM_ID_BASE + 1_000,
    **{
        name: ITEM_ID_BASE + offset
        for offset, name in enumerate(GOAL_UNLOCK_ITEMS, start=19)
    },
}

ITEM_CLASSIFICATIONS = {
    name: ItemClassification.progression
    for name in PROGRESSION_ITEM_NAMES
}
ITEM_CLASSIFICATIONS.update(
    (name, ItemClassification.filler) for name in FILLER_ITEMS
)
ITEM_CLASSIFICATIONS[STAT_POINT_ITEM] = ItemClassification.useful


class THPS3Item(Item):
    game = GAME_NAME


def create_item(world: THPS3World, name: str) -> THPS3Item:
    return THPS3Item(
        name,
        ITEM_CLASSIFICATIONS[name],
        ITEM_NAME_TO_ID[name],
        world.player,
    )


def create_items(world: THPS3World) -> None:
    starting_goals = tuple(
        goal for goal in world.selected_goals
        if goal.level_key == world.starting_level_key
    )
    opening_goal = next(
        (
            goal for goal in starting_goals
            if OBJECTIVE_REQUIREMENTS[world.starting_level_key].get(goal.name) == []
        ),
        starting_goals[0],
    )
    active_goals = world.goal_unlocks
    active_access_items = {
        key: item for key, item in LEVEL_ACCESS_ITEMS.items()
        if key in world.active_level_keys
    }
    unfilled_location_count = len(
        world.multiworld.get_unfilled_locations(world.player)
    )
    stat_point_item_count = (
        5 * len(world.active_levels)
        if "stat points" in world.enabled_location_types else 0
    )
    pool_before_goal_unlocks = (
        len(active_access_items) - 1
        + len(active_goals)
        + len(TRICK_CATEGORY_ITEMS)
        + stat_point_item_count
    )
    goals_only = world.enabled_location_types == {"objectives"}
    if goals_only:
        world.multiworld.local_early_items[world.player]["Grind Tricks"] = 1
    required_starting_goals = list(starting_goals) if goals_only else [opening_goal]
    starting_trick_items: tuple[str, ...] = ()
    if "objectives" not in world.enabled_location_types:
        required_starting_goals = list(starting_goals)
        starting_trick_items = TRICK_CATEGORY_ITEMS
    starting_goal_count = min(
        len(active_goals),
        max(
            len(required_starting_goals),
            pool_before_goal_unlocks - unfilled_location_count,
        ),
    )
    starting_goal_unlocks = [
        *(goal.item_name for goal in required_starting_goals),
        *world.random.sample(
            [goal.item_name for goal in active_goals if goal not in required_starting_goals],
            starting_goal_count - len(required_starting_goals),
        ),
    ]
    starting_items = (
        LEVEL_ACCESS_ITEMS[world.starting_level_key],
        *starting_goal_unlocks,
        *starting_trick_items,
    )
    for item_name in starting_items:
        world.push_precollected(world.create_item(item_name))

    item_names: list[str] = [
        access_item
        for level_key, access_item in active_access_items.items()
        if level_key != world.starting_level_key
    ]
    item_names.extend(
        item_name
        for item_name in (goal.item_name for goal in active_goals)
        if item_name not in starting_goal_unlocks
    )
    item_names.extend(
        item_name for item_name in TRICK_CATEGORY_ITEMS
        if item_name not in starting_trick_items
    )
    item_names.extend([STAT_POINT_ITEM] * stat_point_item_count)

    overflow = len(item_names) - unfilled_location_count
    for item_name in (
        *([STAT_POINT_ITEM] * stat_point_item_count),
        *TRICK_CATEGORY_ITEMS,
        *(item for key, item in active_access_items.items()
          if key != world.starting_level_key),
    ):
        if overflow <= 0:
            break
        if item_name in item_names:
            item_names.remove(item_name)
            world.push_precollected(world.create_item(item_name))
            overflow -= 1
    if overflow > 0:
        raise ValueError("not enough THPS3 locations for the required item pool")

    itempool = [world.create_item(item_name) for item_name in item_names]
    filler_count = unfilled_location_count - len(itempool)
    if filler_count < 0:
        raise ValueError(
            f"THPS3 has {len(itempool)} required items but only "
            f"{unfilled_location_count} unfilled locations"
        )

    itempool.extend(world.create_filler() for _ in range(filler_count))
    world.multiworld.itempool += itempool
