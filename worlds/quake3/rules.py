from worlds.generic.Rules import set_rule

from .data.generated import MAP_BY_KEY
from .regions import map_label


def required_count(total: int, percentage: int) -> int:
    return (total * percentage + 99) // 100


def unlock_names(families) -> list[str]:
    return [f"{family} Unlock" for family in families]


def set_rules(world) -> None:
    player = world.player
    weapon_percentage = world.options.weapon_logic_percentage.value
    item_percentage = world.options.item_logic_percentage.value
    for key in world.selected_map_keys:
        map_data = MAP_BY_KEY[key]
        stage_item = map_data["stage_item_name"]
        weapons = unlock_names(map_data["weapon_families"])
        items = unlock_names(map_data["nonweapon_families"])
        weapon_count = required_count(len(weapons), weapon_percentage)
        item_count = required_count(len(items), item_percentage)
        set_rule(world.multiworld.get_entrance(f"Enter {key}", player),
                 lambda state, stage_item=stage_item, weapons=weapons, items=items,
                 weapon_count=weapon_count, item_count=item_count:
                 state.has(stage_item, player)
                 and state.has_from_list_unique(weapons, player, weapon_count)
                 and state.has_from_list_unique(items, player, item_count))

        for pickup in map_data["pickups"]:
            if pickup["location_name"] not in world.included_pickup_locations:
                continue
            unlocks = unlock_names(pickup["families"])
            set_rule(world.multiworld.get_location(pickup["location_name"], player),
                     lambda state, unlocks=unlocks: state.has_from_list_unique(unlocks, player, 1))
        if map_data["powerup_frag_location_id"]:
            powerups = unlock_names(family for family in map_data["nonweapon_families"]
                                    if family in {"Quad Damage", "Battle Suit", "Haste", "Invisibility",
                                                  "Regeneration", "Flight"})
            set_rule(world.multiworld.get_location(map_data["powerup_frag_location_name"], player),
                     lambda state, powerups=powerups: state.has_from_list_unique(powerups, player, 1))

    if world.options.goal.value == 1:
        set_rule(world.multiworld.get_entrance("Reach Goal", player),
                 lambda state: state.has("Quad Token", player, world.goal_required))
    else:
        cleared_items = [f"{map_label(MAP_BY_KEY[key])} Cleared" for key in world.selected_map_keys]
        set_rule(world.multiworld.get_entrance("Reach Goal", player),
                 lambda state: state.has_from_list_unique(cleared_items, player, world.goal_required))
    world.multiworld.completion_condition[player] = lambda state: state.has("Victory", player)
