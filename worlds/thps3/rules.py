from __future__ import annotations

from typing import TYPE_CHECKING

from .data import (
    HIDDEN_DECK_REQUIREMENTS,
    GOAL_BY_LEVEL_AND_ID,
    LEVEL_BY_KEY,
    OBJECTIVE_REQUIREMENTS,
    SKATE_LETTER_REQUIREMENTS,
    SKATER_BY_NAME,
    SKATER_LAYOUTS,
    STAT_POINT_REQUIREMENTS,
)
from .locations import (
    DECK_BY_LOCATION_NAME,
    GOAL_BY_LOCATION_NAME,
    STAT_POINT_BY_LOCATION_NAME,
)
if TYPE_CHECKING:
    from .world import THPS3World


def _meets_requirement(state, requirement, world, level_key, trick_style) -> bool:
    if isinstance(requirement, str):
        return state.has(requirement, world.player)
    if isinstance(requirement, list):
        return not requirement or any(
            _meets_requirement(state, entry, world, level_key, trick_style)
            for entry in requirement
        )

    checks = []
    if trick_style in requirement:
        checks.append(_meets_requirement(
            state, requirement[trick_style], world, level_key, trick_style
        ))
    if "any" in requirement:
        checks.append(sum(
            _meets_requirement(state, entry, world, level_key, trick_style)
            for entry in requirement["any"]
        ) >= requirement.get("count", 1))
    if "all" in requirement:
        checks.append(all(
            _meets_requirement(state, entry, world, level_key, trick_style)
            for entry in requirement["all"]
        ))
    if "goal_id" in requirement:
        checks.append(state.has(
            GOAL_BY_LEVEL_AND_ID[
                (level_key, requirement["goal_id"])
            ].item_name,
            world.player,
        ))
    return all(checks)


def set_rules(world: THPS3World) -> None:
    skater = SKATER_BY_NAME[world.selected_skater_name]
    layouts = SKATER_LAYOUTS[skater.key]
    trick_style = layouts["style"]
    for location_name, goal in (
        GOAL_BY_LOCATION_NAME.items()
        if "objectives" in world.enabled_location_types else ()
    ):
        if goal not in world.selected_goals:
            continue
        location = world.get_location(location_name)
        requirement = (
            SKATE_LETTER_REQUIREMENTS[str(layouts["skate"])][goal.level_key]
            if goal.name == "Collect S-K-A-T-E"
            else OBJECTIVE_REQUIREMENTS[goal.level_key][goal.name]
        )
        world.set_rule(
            location,
            lambda state, unlock=goal.item_name, req=requirement,
                    level=goal.level_key: (
                state.has(unlock, world.player)
                and _meets_requirement(
                    state, req, world, level, trick_style
                )
            ),
        )

    for location_name, stat_point in (
        STAT_POINT_BY_LOCATION_NAME.items()
        if "stat points" in world.enabled_location_types else ()
    ):
        if stat_point.level_key not in world.active_level_keys:
            continue
        requirement = STAT_POINT_REQUIREMENTS[str(layouts["stats"])][
            stat_point.level_key
        ][f"Stat Point {stat_point.point_id}"]
        world.set_rule(
            world.get_location(location_name),
            lambda state, req=requirement, level=stat_point.level_key: (
                _meets_requirement(state, req, world, level, trick_style)
            ),
        )

    for location_name, deck in (
        DECK_BY_LOCATION_NAME.items()
        if "hidden decks" in world.enabled_location_types else ()
    ):
        if deck.level_key not in world.active_level_keys:
            continue
        requirement = HIDDEN_DECK_REQUIREMENTS[str(layouts["deck"])][
            deck.level_key
        ]
        world.set_rule(
            world.get_location(location_name),
            lambda state, req=requirement, level=deck.level_key: (
                _meets_requirement(state, req, world, level, trick_style)
            ),
        )

    for gap in world.selected_gaps:
        location = world.get_location(gap.location_name)
        any_items = tuple(gap.required_trick_items)
        all_items = tuple(gap.required_all_trick_items)
        required_goals = tuple(
            GOAL_BY_LEVEL_AND_ID[(gap.level_key, goal_id)]
            for goal_id in gap.required_goal_ids
        )
        world.set_rule(
            location,
            lambda state, any_req=any_items, all_req=all_items, goals=required_goals: (
                (not any_req or state.has_any(any_req, world.player))
                and state.has_all(all_req, world.player)
                and all(state.has(goal.item_name, world.player) for goal in goals)
            ),
        )

    career_complete = world.get_location("Career Complete")
    mode = world.options.completion_goal.current_key
    if mode in {"levels", "level_tour"}:
        groups = tuple(
            tuple(
                goal.location_name for goal in world.selected_goals
                if goal.level_key == level.key
            )
            for level in world.active_levels
        )
        thresholds = (
            tuple(map(len, groups)) if mode == "levels" else
            tuple(
                min(int(world.options.required_objectives_per_level), len(group))
                for group in groups
            )
        )
        required_groups = int(world.options.required_levels) if mode == "levels" else len(groups)
    else:
        if mode == "objectives":
            names = tuple(
                goal.location_name for goal in world.selected_goals
            )
            required = int(world.options.required_objectives)
        elif mode == "cruise_ship":
            names = tuple(
                goal.location_name for goal in world.selected_goals
                if goal.level_key == "cruise_ship"
            )
            required = len(names)
        elif mode == "gold_medals":
            names = tuple(
                goal.location_name for goal in world.selected_goals
                if goal.name == "Gold Medal"
            )
            required = int(world.options.required_gold_medals)
        elif mode == "goal_type":
            goal_type_id = int(world.options.completion_goal_type)
            names = tuple(
                goal.location_name for goal in world.selected_goals
                if goal.goal_id == goal_type_id
                and not LEVEL_BY_KEY[goal.level_key].competition
            )
            required = len(names)
        elif mode == "gap_hunt":
            names = tuple(gap.location_name for gap in world.selected_gaps)
            required = world.required_gap_count
        elif mode == "collectibles":
            names = (
                tuple(
                    name for name, point in STAT_POINT_BY_LOCATION_NAME.items()
                    if point.level_key in world.active_level_keys
                )
                if "stat points" in world.enabled_location_types else ()
            ) + (
                tuple(
                    name for name, deck in DECK_BY_LOCATION_NAME.items()
                    if deck.level_key in world.active_level_keys
                )
                if "hidden decks" in world.enabled_location_types else ()
            )
            required = int(world.options.required_collectibles)
        else:
            names = (
                (tuple(
                    goal.location_name for goal in world.selected_goals
                )
                 if "objectives" in world.enabled_location_types else ())
                + tuple(gap.location_name for gap in world.selected_gaps)
                + (tuple(
                    name for name, point in STAT_POINT_BY_LOCATION_NAME.items()
                    if point.level_key in world.active_level_keys
                )
                   if "stat points" in world.enabled_location_types else ())
                + (tuple(
                    name for name, deck in DECK_BY_LOCATION_NAME.items()
                    if deck.level_key in world.active_level_keys
                )
                   if "hidden decks" in world.enabled_location_types else ())
            )
            required = int(world.options.required_checks)
        groups, thresholds, required_groups = (names,), (required,), 1
    world.set_rule(
        career_complete,
        lambda state, targets=groups, needed=thresholds, group_count=required_groups: sum(
            sum(state.can_reach_location(name, world.player) for name in names) >= threshold
            for names, threshold in zip(targets, needed)
        ) >= group_count,
    )
    world.multiworld.completion_condition[world.player] = (
        lambda state: state.has("Victory", world.player)
    )
