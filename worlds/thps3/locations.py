from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from .data import (
    DECKS,
    GAP_CATALOG_BY_LEVEL,
    GAME_NAME,
    GAPS_BY_LEVEL,
    GOALS,
    LEVEL_BY_KEY,
    STAT_POINTS,
    DeckData,
    GapData,
    GoalData,
    StatPointData,
)
from .items import THPS3Item

if TYPE_CHECKING:
    from .world import THPS3World


LOCATION_ID_BASE = 30_310_000
GAP_LOCATION_ID_BASE = 30_320_000
STAT_POINT_LOCATION_ID_BASE = 30_315_000
DECK_LOCATION_ID_BASE = 30_316_000

GOAL_LOCATION_NAME_TO_ID = {
    goal.location_name: (
        LOCATION_ID_BASE
        + (LEVEL_BY_KEY[goal.level_key].level_num * 100)
        + goal.goal_id
    )
    for goal in GOALS
}

STAT_POINT_LOCATION_NAME_TO_ID = {
    stat_point.location_name: (
        STAT_POINT_LOCATION_ID_BASE
        + (LEVEL_BY_KEY[stat_point.level_key].level_num * 100)
        + stat_point.point_id
    )
    for stat_point in STAT_POINTS
}

DECK_LOCATION_NAME_TO_ID = {
    deck.location_name: (
        DECK_LOCATION_ID_BASE
        + (LEVEL_BY_KEY[deck.level_key].level_num * 100)
    )
    for deck in DECKS
}

ALL_GAPS: tuple[GapData, ...] = tuple(
    gap
    for level_gaps in GAPS_BY_LEVEL.values()
    for gap in level_gaps
)

GAP_LOCATION_NAME_TO_ID = {
    gap.location_name: (
        GAP_LOCATION_ID_BASE
        + ((LEVEL_BY_KEY[level_key].level_num - 1) * 100)
        + offset
    )
    for level_key, level_gaps in GAP_CATALOG_BY_LEVEL.items()
    for offset, gap in enumerate(level_gaps)
    if gap in GAPS_BY_LEVEL[level_key]
}

LOCATION_NAME_TO_ID = {
    **GOAL_LOCATION_NAME_TO_ID,
    **STAT_POINT_LOCATION_NAME_TO_ID,
    **DECK_LOCATION_NAME_TO_ID,
    **GAP_LOCATION_NAME_TO_ID,
}

GOAL_BY_LOCATION_NAME: dict[str, GoalData] = {
    goal.location_name: goal
    for goal in GOALS
}

STAT_POINT_BY_LOCATION_NAME: dict[str, StatPointData] = {
    stat_point.location_name: stat_point
    for stat_point in STAT_POINTS
}

DECK_BY_LOCATION_NAME: dict[str, DeckData] = {
    deck.location_name: deck
    for deck in DECKS
}

GAP_BY_LOCATION_NAME: dict[str, GapData] = {
    gap.location_name: gap
    for gap in ALL_GAPS
}


class THPS3Location(Location):
    game = GAME_NAME


def create_locations(world: THPS3World) -> None:
    if "objectives" in world.enabled_location_types:
        for goal in world.selected_goals:
            region = world.get_region(goal.level_key)
            region.add_locations(
                {goal.location_name: GOAL_LOCATION_NAME_TO_ID[goal.location_name]},
                THPS3Location,
            )

    if "stat points" in world.enabled_location_types:
        for stat_point in STAT_POINTS:
            if stat_point.level_key not in world.active_level_keys:
                continue
            region = world.get_region(stat_point.level_key)
            region.add_locations(
                {
                    stat_point.location_name:
                        STAT_POINT_LOCATION_NAME_TO_ID[stat_point.location_name]
                },
                THPS3Location,
            )

    if "hidden decks" in world.enabled_location_types:
        for deck in DECKS:
            if deck.level_key not in world.active_level_keys:
                continue
            region = world.get_region(deck.level_key)
            region.add_locations(
                {deck.location_name: DECK_LOCATION_NAME_TO_ID[deck.location_name]},
                THPS3Location,
            )

    for gap in world.selected_gaps:
        region = world.get_region(gap.level_key)
        region.add_locations(
            {gap.location_name: GAP_LOCATION_NAME_TO_ID[gap.location_name]},
            THPS3Location,
        )

    menu = world.get_region("Menu")
    victory_location = THPS3Location(
        world.player,
        "Career Complete",
        None,
        menu,
    )
    victory_location.place_locked_item(
        THPS3Item(
            "Victory",
            ItemClassification.progression,
            None,
            world.player,
        )
    )
    menu.locations.append(victory_location)
    DeckData,
