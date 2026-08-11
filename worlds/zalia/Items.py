import json
import pkgutil
from typing import Optional, Dict, Tuple

from BaseClasses import Item, ItemClassification as ItemClass

from .Constants import *

class ZALiAItem(Item):
    game: str = GAME_NAME


class ItemData:
    item_class: ItemClass
    code: Optional[int]
    count: int
    count_extra: int

    def __init__(
        self,
        item_class: ItemClass,
        code: Optional[int] = None,
        count: int = 1,
        count_extra: int = 0,
    ):
        self.item_class = item_class
        self.code = code
        if code is not None:
            self.code += BASE_ID
        if self.item_class in (ItemClass.filler, ItemClass.trap) or code is None:
            self.count = 0
            self.count_extra = 0
        else:
            self.count = count
            self.count_extra = count_extra

    def create_item(self, player: int):
        return ZALiAItem(item_data_names[self], self.item_class, self.code, player)


def _gml_name_to_friendly(gml_name: str) -> str:
    gml_name = gml_name.strip("_")
    return gml_name.replace("_", " ").title()


# Map GML item_type constants to friendly item names
ITEM_TYPE_TO_NAME: Dict[str, str] = {
    "_CANDLE": ITEM_CANDLE,
    "_GLOVE": ITEM_GLOVE,
    "_RAFT": ITEM_RAFT,
    "_BOOTS": ITEM_BOOTS,
    "_FLUTE": ITEM_FLUTE,
    "_CROSS": ITEM_CROSS,
    "_HAMMER": ITEM_HAMMER,
    "_BRACELET": ITEM_BRACELET,
    "_MIRROR": ITEM_MIRROR,
    "_FLOWER": ITEM_FLOWER,
    "_BOOK": ITEM_BOOK,
    "_MEAT": ITEM_MEAT,
    "_SHIELD": ITEM_SHIELD,
    "_ALLKEY": ITEM_KEY,
    "_PENDANT": ITEM_PENDANT,
    "_SWORD": ITEM_SWORD,
    "_TROPHY": ITEM_TROPHY,
    "_RING": ITEM_RING,
    "_MASK": ITEM_MASK,
    "_NOTE": ITEM_NOTE,
    "_MAP1": ITEM_MAP1,
    "_MAP2": ITEM_MAP2,
    "_CHILD": ITEM_CHILD,
    "_RFAIRY": ITEM_RESCUE_FAIRY,
    "_BOTTLE": ITEM_BOTTLE,
    "_HEART": ITEM_CONTAINER_HP,
    "_MAGIC": ITEM_CONTAINER_MP,
    "_1UP": ITEM_1UP_DOLL,
    "_PBAG": FILLER_ITEM_PBAG,
}

GML_SPELL_TO_NAME: Dict[str, str] = {
    "_PROTECT": SPELL_PROTECT,
    "_JUMP": SPELL_JUMP,
    "_HEAL": SPELL_HEAL,
    "_FAIRY": SPELL_FAIRY,
    "_FIRE": SPELL_FIRE,
    "_REFLECT": SPELL_REFLECT,
    "_ENIGMA": SPELL_ENIGMA,
    "_THUNDER": SPELL_THUNDER,
    "_SUMMON": SPELL_SUMMON,
}

GML_SKILL_TO_NAME: Dict[str, str] = {
    "_STABDOWN": SKILL_STAB_DOWN,
    "_STABUP": SKILL_STAB_UP,
}

# Item types that should be progression
PROGRESSION_ITEM_KEYS = {
    "_CANDLE",
    "_GLOVE",
    "_RAFT",
    "_BOOTS",
    "_FLUTE",
    "_CROSS",
    "_HAMMER",
    "_BRACELET",
    "_MIRROR",
    "_FLOWER",
    "_BOOK",
    "_MEAT",
    "_SHIELD",
    "_ALLKEY",
    "_PENDANT",
    "_SWORD",
    "_TROPHY",
    "_RING",
    "_MASK",
    "_NOTE",
    "_CHILD",
}


def _load_data() -> Tuple[
    Dict[str, ItemData],
    Dict[str, ItemData],
    Dict[str, ItemData],
    Dict[str, ItemData],
    Dict[str, ItemData],
    Dict[str, ItemData],
]:
    raw = pkgutil.get_data(__name__, "data/zalia_data.json")
    if raw is None:
        raise FileNotFoundError("Data file not found: data/zalia_data.json")
    data = json.loads(raw)

    # Count instances from the data file for variable-count
    heart_count = sum(
        1 for loc in data.get("locations", []) if loc.get("item_type") == "_HEART"
    )
    magic_count = sum(
        1 for loc in data.get("locations", []) if loc.get("item_type") == "_MAGIC"
    )
    doll_count = sum(
        1 for loc in data.get("locations", []) if loc.get("item_type") == "_1UP"
    )
    pbag_count = sum(
        1 for loc in data.get("locations", []) if loc.get("item_type") == "_PBAG"
    )

    # Use hardcoded item definitions with FIXED indices
    return _build_hardcoded(heart_count, magic_count, doll_count, pbag_count)


def _build_hardcoded(
    heart_count: int = 0, magic_count: int = 0, doll_count: int = 0, pbag_count: int = 0
) -> Tuple[
    Dict[str, ItemData],
    Dict[str, ItemData],
    Dict[str, ItemData],
    Dict[str, ItemData],
    Dict[str, ItemData],
    Dict[str, ItemData],
]:
    """Build item definitions with FIXED indices for stable AP item IDs."""
    tools: Dict[str, ItemData] = {
        ITEM_CANDLE: ItemData(ItemClass.progression, 0),
        ITEM_GLOVE: ItemData(ItemClass.progression, 1),
        ITEM_RAFT: ItemData(ItemClass.progression, 2),
        ITEM_BOOTS: ItemData(ItemClass.progression, 3),
        ITEM_FLUTE: ItemData(ItemClass.progression, 4),
        ITEM_CROSS: ItemData(ItemClass.progression, 5),
        ITEM_HAMMER: ItemData(ItemClass.progression, 6),
        ITEM_BRACELET: ItemData(ItemClass.progression, 7),
        ITEM_MIRROR: ItemData(ItemClass.progression, 8),
        ITEM_FLOWER: ItemData(ItemClass.progression, 9),
        ITEM_BOOK: ItemData(ItemClass.progression, 10),
        ITEM_MEAT: ItemData(ItemClass.progression, 11),
        ITEM_SHIELD: ItemData(ItemClass.progression, 12),
        ITEM_KEY: ItemData(ItemClass.progression, 13),
        ITEM_PENDANT: ItemData(ItemClass.progression, 14),
        ITEM_SWORD: ItemData(ItemClass.progression, 15),
        ITEM_TROPHY: ItemData(ItemClass.progression, 16),
        ITEM_RING: ItemData(ItemClass.progression, 17),
        ITEM_MASK: ItemData(ItemClass.progression, 18),
        ITEM_NOTE: ItemData(ItemClass.progression, 19),
        ITEM_MAP1: ItemData(ItemClass.useful, 20),
        ITEM_MAP2: ItemData(ItemClass.useful, 21),
        ITEM_CHILD: ItemData(ItemClass.progression, 22),
        ITEM_RESCUE_FAIRY: ItemData(ItemClass.progression, 23),
        ITEM_BOTTLE: ItemData(ItemClass.useful, 24),
    }

    spells: Dict[str, ItemData] = {
        SPELL_PROTECT: ItemData(ItemClass.progression, 25),
        SPELL_JUMP: ItemData(ItemClass.progression, 26),
        SPELL_HEAL: ItemData(ItemClass.progression, 27),
        SPELL_FAIRY: ItemData(ItemClass.progression, 28),
        SPELL_FIRE: ItemData(ItemClass.progression, 29),
        SPELL_REFLECT: ItemData(ItemClass.progression, 30),
        SPELL_ENIGMA: ItemData(ItemClass.progression, 31),
        SPELL_THUNDER: ItemData(ItemClass.progression, 32),
        SPELL_SUMMON: ItemData(ItemClass.progression, 33),
    }

    skills: Dict[str, ItemData] = {
        SKILL_STAB_DOWN: ItemData(ItemClass.progression, 34),
        SKILL_STAB_UP: ItemData(ItemClass.progression, 35),
    }

    # Variable-count containers (indices 36-38 always)
    useful: Dict[str, ItemData] = {}
    if heart_count > 0:
        useful[ITEM_CONTAINER_HP] = ItemData(
            ItemClass.useful, 36, count=1, count_extra=max(heart_count - 1, 0)
        )
    if magic_count > 0:
        useful[ITEM_CONTAINER_MP] = ItemData(
            ItemClass.useful, 37, count=1, count_extra=max(magic_count - 1, 0)
        )
    if doll_count > 0:
        useful[ITEM_1UP_DOLL] = ItemData(
            ItemClass.useful, 38, count=1, count_extra=max(doll_count - 1, 0)
        )

    # Keys (indices 39-44)
    keys: Dict[str, ItemData] = {
        KEY_PARAPA: ItemData(ItemClass.progression, 39, count=3),
        KEY_MIDORO: ItemData(ItemClass.progression, 40, count=4),
        KEY_ISLAND: ItemData(ItemClass.progression, 41, count=4),
        KEY_MAZE: ItemData(ItemClass.progression, 42, count=6),
        KEY_SEA: ItemData(ItemClass.progression, 43, count=5),
        KEY_THREE_EYE: ItemData(ItemClass.progression, 44, count=6),
    }

    # Filler (index 45)
    filler: Dict[str, ItemData] = {}
    if pbag_count > 0:
        filler[FILLER_ITEM_PBAG] = ItemData(ItemClass.filler, 45)

    return tools, spells, skills, useful, filler, keys


def _load_hardcoded() -> Tuple[
    Dict[str, ItemData],
    Dict[str, ItemData],
    Dict[str, ItemData],
    Dict[str, ItemData],
    Dict[str, ItemData],
    Dict[str, ItemData],
]:
    # Fallback with default counts
    return _build_hardcoded(heart_count=63, magic_count=34, doll_count=6, pbag_count=41)


try:
    (
        item_dict_tools,
        item_dict_spells,
        item_dict_skills,
        item_dict_useful,
        item_dict_filler,
        item_dict_keys,
    ) = _load_data()
except (FileNotFoundError, json.JSONDecodeError, KeyError):
    (
        item_dict_tools,
        item_dict_spells,
        item_dict_skills,
        item_dict_useful,
        item_dict_filler,
        item_dict_keys,
    ) = _load_hardcoded()

item_dict_events: Dict[str, ItemData] = {
    EVENT_VICTORY: ItemData(ItemClass.progression),
}

# Crystals are real progression items (fixed codes 46-51)


item_dict_crystals: Dict[str, ItemData] = {
    name: ItemData(ItemClass.progression, 46 + i)
    for i, name in enumerate(CRYSTAL_ITEMS)
}

item_dict: Dict[str, ItemData] = {
    **item_dict_tools,
    **item_dict_spells,
    **item_dict_skills,
    **item_dict_useful,
    **item_dict_filler,
    **item_dict_keys,
    **item_dict_crystals,
    **item_dict_events,
}

item_data_names: Dict[ItemData, str] = {value: key for key, value in item_dict.items()}
