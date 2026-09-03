from BaseClasses import Item, ItemClassification

from .data.generated import AMMO_FILLERS, ITEM_NAME_TO_ID

FILLER_ITEMS = ("Nothing", "+1 Health", "+1 Armor") + tuple(name for name, _, _ in AMMO_FILLERS)


class Quake3Item(Item):
    game = "Quake III Arena"


def create_item(player: int, name: str) -> Quake3Item:
    classification = ItemClassification.filler if name in FILLER_ITEMS else ItemClassification.progression
    return Quake3Item(name, classification, ITEM_NAME_TO_ID[name], player)


def overflow_unlocks(pool_names: list[str], capacity: int, random) -> set[str]:
    count = max(0, len(pool_names) - capacity)
    unlocks = [name for name in pool_names if name.endswith(" Unlock")]
    return set(random.sample(unlocks, min(count, len(unlocks))))
