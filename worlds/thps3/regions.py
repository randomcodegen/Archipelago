from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region

from .items import LEVEL_ACCESS_ITEMS

if TYPE_CHECKING:
    from .world import THPS3World


def create_regions(world: THPS3World) -> None:
    menu = Region("Menu", world.player, world.multiworld)
    level_regions = [
        Region(level.key, world.player, world.multiworld)
        for level in world.active_levels
    ]
    world.multiworld.regions += [menu, *level_regions]

    for level, level_region in zip(world.active_levels, level_regions):
        access_item = LEVEL_ACCESS_ITEMS[level.key]
        menu.connect(
            level_region,
            f"Enter {level.name}",
            lambda state, item=access_item: state.has(item, world.player),
        )
