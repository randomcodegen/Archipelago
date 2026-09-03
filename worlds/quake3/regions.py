from BaseClasses import Item, ItemClassification, Region

from .data.generated import MAP_BY_KEY
from .items import Quake3Item
from .locations import Quake3Location


def map_label(map_data: dict) -> str:
    return f"{map_data['name']} ({map_data['key']})"


def create_regions(world) -> None:
    menu = Region("Menu", world.player, world.multiworld)
    goal = Region("Goal", world.player, world.multiworld)
    world.multiworld.regions.extend([menu, goal])

    for key in world.selected_map_keys:
        map_data = MAP_BY_KEY[key]
        label = map_label(map_data)
        region = Region(label, world.player, world.multiworld)
        for pickup in map_data["pickups"]:
            if pickup["location_name"] not in world.included_pickup_locations:
                continue
            region.locations.append(Quake3Location(
                world.player, pickup["location_name"], pickup["location_id"], region
            ))
        for kill in map_data["kills"]:
            if kill["number"] % world.options.kill_check_increment.value:
                continue
            region.locations.append(Quake3Location(
                world.player, kill["location_name"], kill["location_id"], region
            ))
        for traversal in map_data["traversals"]:
            if traversal["location_name"] not in world.included_traversal_locations:
                continue
            region.locations.append(Quake3Location(
                world.player, traversal["location_name"], traversal["location_id"], region
            ))
        if map_data["powerup_frag_location_id"]:
            region.locations.append(Quake3Location(
                world.player, map_data["powerup_frag_location_name"],
                map_data["powerup_frag_location_id"], region
            ))
        region.locations.append(Quake3Location(
            world.player, map_data["clear_location_name"], map_data["clear_location_id"], region
        ))
        clear_event = Quake3Location(world.player, f"{label} Can Be Cleared", None, region)
        clear_event.place_locked_item(Quake3Item(
            f"{label} Cleared", ItemClassification.progression, None, world.player
        ))
        region.locations.append(clear_event)
        world.multiworld.regions.append(region)
        menu.connect(region, f"Enter {key}")

    victory = Quake3Location(world.player, "Victory", None, goal)
    victory.place_locked_item(Quake3Item("Victory", ItemClassification.progression, None, world.player))
    goal.locations.append(victory)
    menu.connect(goal, "Reach Goal")
