import hashlib
import json
import os
import re
from typing import Optional, Dict

from BaseClasses import Location

from .Constants import *
from .Items import (
    ITEM_CONTAINER_HP,
    ITEM_CONTAINER_MP,
    ITEM_1UP_DOLL,
    FILLER_ITEM_PBAG,
    ITEM_TYPE_TO_NAME,
)

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

# Set by _load_data()
LOCATION_DATA_CHECKSUM: Optional[str] = None

# raw JSON description -> new (palace-prefixed) loc
LOCATION_NAME_ALIASES: Dict[str, str] = {}

# _Palc<letter>_ room-name prefix -> palace tag
_PALACE_TAG_BY_LETTER: Dict[str, str] = {
    "A": "P1",
    "B": "P2",
    "C": "P3",
    "D": "P4",
    "E": "P5",
    "F": "P6",
    "G": "GP",
}


def _palace_tag(room_name: str) -> Optional[str]:
    """Palace tag ('P1'..'P6', 'GP') for a dungeon room_name like '_PalcF_02',
    or None if the room_name is not a palace room."""
    if room_name.startswith("_Palc") and len(room_name) > 5:
        return _PALACE_TAG_BY_LETTER.get(room_name[5].upper())
    return None


def _has_palace_tag(description: str, tag: str) -> bool:
    """True if the description already identifies its palace, so we must not
    prefix it again (e.g. 'P3 Item location', 'PBag: P5 Entrance', or any
    'Great Palace ...' name for the GP tag)."""
    lower = description.lower()
    tokens = re.split(r"[^a-z0-9]+", lower)
    if tag == "GP":
        return "great palace" in lower or "gp" in tokens
    return tag.lower() in tokens


def _palace_display_name(room_name: str, description: str) -> str:
    """Prefix a dungeon location's description with its palace tag (e.g.
    'P6 PBag: GLOVE and STABUP locked 1') unless it already names its palace."""
    tag = _palace_tag(room_name)
    if tag and not _has_palace_tag(description, tag):
        return f"{tag} {description}"
    return description


def _compute_location_checksum(entries) -> str:
    parts = []
    for entry in entries:
        loc_num = entry.get("location_num", 0)
        room_name = entry.get("room_name", "")
        description = entry.get("description", "")
        parts.append(f"{loc_num}:{room_name}:{description};")
    return hashlib.md5("".join(parts).encode("utf-8")).hexdigest()


class ZALiALocation(Location):
    game: str = GAME_NAME


class LocData:
    code: Optional[int]
    category: Optional[str]
    obscurity: int
    intended_item: Optional[str]
    quest: str

    def __init__(
        self,
        code: Optional[int] = None,
        category: Optional[str] = None,
        obscurity: int = 0,
        intended_item: Optional[str] = None,
        quest: str = "12",
    ):
        if code is not None:
            self.code = code + BASE_ID
        else:
            self.code = None
        self.category = category
        self.obscurity = obscurity
        self.intended_item = intended_item
        # Which quest(s) this loc exists in: "12" both (default)
        self.quest = quest if quest else "12"


def _load_data() -> Dict[str, LocData]:
    global LOCATION_DATA_CHECKSUM
    json_path = os.path.join(DATA_DIR, "zalia_data.json")
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"Data file not found: {json_path}")

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    LOCATION_DATA_CHECKSUM = _compute_location_checksum(data.get("locations", []))

    locations: Dict[str, LocData] = {}

    for entry in data.get("locations", []):
        raw_name = entry.get("description", "")
        if not raw_name:
            continue
        loc_num = entry.get("location_num", 0)
        category = entry.get("category", "")
        # Dungeon-interior checks get a 'P1'..'P6'/'GP' prefix
        name = raw_name
        if category == "_Dngn01":
            name = _palace_display_name(entry.get("room_name", ""), raw_name)
            if name != raw_name:
                LOCATION_NAME_ALIASES[raw_name] = name
        elif (
            category == "_Kaku01"
            and raw_name.startswith("Kakusu ")
            and raw_name[7:].isdigit()
        ):
            # Individual Kakusu checks: swap the numbered placeholder
            _idx = int(raw_name[7:])
            if 1 <= _idx <= len(KAKUSU_LOCATION_NAMES):
                name = KAKUSU_LOCATION_NAMES[_idx - 1]
                LOCATION_NAME_ALIASES[raw_name] = name
        obscurity = entry.get("obscurity", 0)
        gml_item_type = entry.get("item_type", "")
        # Quest membership ("12"/"01"/"02"); older exports omit it
        quest = str(entry.get("quest", "12")) or "12"

        # Map GML item type to friendly item name
        intended = ITEM_TYPE_TO_NAME.get(gml_item_type, None)

        # ID = location_num - 1 for stable 0-based indexing
        locations[name] = LocData(loc_num - 1, category, obscurity, intended, quest)

    return locations


def _load_hardcoded() -> Dict[str, LocData]:
    locations = {}

    west01 = {
        "Bottle (North Castle Zelda room)": LocData(0, "_West01", 0, ITEM_BOTTLE),
        "PBag: Roof of North Castle East Exit": LocData(
            1, "_West01", 0, FILLER_ITEM_PBAG
        ),
        "PBag: North Castle Lake west exit": LocData(2, "_West01", 0, FILLER_ITEM_PBAG),
        "PBag: Secret tile above North Castle": LocData(
            3, "_West01", 0, FILLER_ITEM_PBAG
        ),
        "PBag: Forest tile S of Tantari Desert": LocData(
            4, "_West01", 0, FILLER_ITEM_PBAG
        ),
        "PBag: Upper North Castle Hallway": LocData(5, "_West01", 2, FILLER_ITEM_PBAG),
        "PBag: North Castle vertical climb challenge": LocData(
            6, "_West01", 2, FILLER_ITEM_PBAG
        ),
        "PBag: Cave ruins under North Castle Lake": LocData(
            7, "_West01", 2, FILLER_ITEM_PBAG
        ),
        "South Parapa Container Piece": LocData(8, "_West01", 0, ITEM_CONTAINER_HP),
        "North Castle Field Container Piece": LocData(
            9, "_West01", 0, ITEM_CONTAINER_HP
        ),
        "Tantari Desert Container Piece": LocData(10, "_West01", 0, ITEM_CONTAINER_MP),
        "North Castle Cave Container Piece": LocData(
            11, "_West01", 0, ITEM_CONTAINER_MP
        ),
        "Parapa Shore Container Piece": LocData(12, "_West01", 0, ITEM_CONTAINER_MP),
        "TROPHY location": LocData(13, "_West01", 1, ITEM_TROPHY),
    }
    locations.update(west01)

    west02 = {
        "PBag: Cave N of Midoro Swamp": LocData(14, "_West02", 0, FILLER_ITEM_PBAG),
        "PBag: Secret tile SW of Royal Cemetery": LocData(
            15, "_West02", 0, FILLER_ITEM_PBAG
        ),
        "PBag: Forest tile E of Saria": LocData(16, "_West02", 0, FILLER_ITEM_PBAG),
        "PBag: Secret tile Midoro Swamp near P2": LocData(
            17, "_West02", 0, FILLER_ITEM_PBAG
        ),
        "Midoro Field Cave Container Piece": LocData(
            18, "_West02", 0, ITEM_CONTAINER_HP
        ),
        "Saria Bay Container Piece": LocData(19, "_West02", 0, ITEM_CONTAINER_MP),
        "Moruge Swamp Container Piece": LocData(20, "_West02", 0, ITEM_CONTAINER_HP),
        "Midoro Swamp Container Piece": LocData(21, "_West02", 0, ITEM_CONTAINER_MP),
        "Royal Cemetery Container Piece": LocData(22, "_West02", 0, ITEM_CONTAINER_HP),
        "FLOWER location": LocData(23, "_West02", 2, ITEM_FLOWER),
        "Bagu Item location (NOTE)": LocData(24, "_West02", 0, ITEM_NOTE),
        "Under Kings Tomb location (SHIELD)": LocData(25, "_West02", 1, ITEM_SHIELD),
    }
    locations.update(west02)

    sari = {
        "PBag: West Saria River Waterfall": LocData(26, "_Sari01", 0, FILLER_ITEM_PBAG),
        "MEAT location": LocData(27, "_Sari01", 0, ITEM_MEAT),
        "PBag: Forest above Saria Lake": LocData(28, "_Sari01", 0, FILLER_ITEM_PBAG),
    }
    locations.update(sari)

    dmountain = {
        "MIRROR location": LocData(29, "_DMtn01", 2, ITEM_MIRROR),
        "PBag: Island between Death Mtn and Royal Cemetery": LocData(
            30, "_DMtn01", 0, FILLER_ITEM_PBAG
        ),
        "Death Mtn Maze Container Piece (MAGIC)": LocData(
            31, "_DMtn01", 0, ITEM_CONTAINER_MP
        ),
        "Death Mtn Maze Container Piece (HEART)": LocData(
            32, "_DMtn01", 0, ITEM_CONTAINER_HP
        ),
        "Death Mtn Hole Container Piece": LocData(33, "_DMtn01", 0, ITEM_CONTAINER_MP),
        "HAMMER location": LocData(34, "_DMtn01", 1, ITEM_HAMMER),
        "Death Mtn Shoals Container Piece": LocData(
            35, "_DMtn01", 0, ITEM_CONTAINER_MP
        ),
        "Death Mtn 1up location": LocData(36, "_DMtn01", 0, ITEM_1UP_DOLL),
        "Boulder Circle Reward location (RING)": LocData(37, "_DMtn01", 1, ITEM_RING),
    }
    locations.update(dmountain)

    nisl = {
        "PBag: Island N of Tantari Desert": LocData(38, "_NIsl01", 0, FILLER_ITEM_PBAG),
        "PBag: Sea Cave N end of Ruto Mtns": LocData(
            39, "_NIsl01", 0, FILLER_ITEM_PBAG
        ),
        "North Isl Container Piece": LocData(40, "_NIsl01", 0, ITEM_CONTAINER_HP),
        "Whale Isl Item location (BOOK)": LocData(41, "_NIsl01", 0, ITEM_BOOK),
    }
    locations.update(nisl)

    rmtn = {
        "Ruto Mtn Container Piece": LocData(42, "_RMtn01", 0, ITEM_CONTAINER_MP),
        "PBag: N Ruto Mtn Ruins Plaforming Challenge": LocData(
            43, "_RMtn01", 0, FILLER_ITEM_PBAG
        ),
        "PBag: N Ruto Mtn Ruins Rocky Alcove": LocData(
            44, "_RMtn01", 0, FILLER_ITEM_PBAG
        ),
        "RescueFairy Location": LocData(45, "_RMtn01", 0, ITEM_RESCUE_FAIRY),
    }
    locations.update(rmtn)

    east = {
        "PBag: Kakusu Reward Area; Cave": LocData(46, "_SCon01", 2, FILLER_ITEM_PBAG),
        "Kakusu Reward Area; SWORD Location": LocData(47, "_SCon01", 2, ITEM_SWORD),
        "Nabooru Bay Cave Container Piece": LocData(
            48, "_Nabo01", 0, ITEM_CONTAINER_HP
        ),
        "P5 Sea Container Piece": LocData(49, "_Nabo01", 0, ITEM_CONTAINER_HP),
        "PBag: Secret desert tile S of P5": LocData(50, "_Nabo01", 0, FILLER_ITEM_PBAG),
        "PBag: Forest tile W of Nabooru": LocData(51, "_Nabo01", 0, FILLER_ITEM_PBAG),
        "PBag: Cave S of Nabooru": LocData(52, "_Nabo01", 0, FILLER_ITEM_PBAG),
        "PBag: Nabooru quest cave system 2": LocData(
            53, "_Nabo01", 1, FILLER_ITEM_PBAG
        ),
        "PBag: Nabooru quest cave system 1": LocData(
            54, "_Nabo01", 1, FILLER_ITEM_PBAG
        ),
        "PBag: Sea cave N of Darunia": LocData(55, "_Daru01", 0, FILLER_ITEM_PBAG),
        "PBag: Secret field tile E Darunia Field": LocData(
            56, "_Daru01", 0, FILLER_ITEM_PBAG
        ),
        "PBag: Nabooru Bay secret just S of Maze Isl Bridge": LocData(
            57, "_Daru01", 0, FILLER_ITEM_PBAG
        ),
        "Pendant Isl Container Piece": LocData(58, "_Daru01", 0, ITEM_CONTAINER_MP),
        "Carock 2 location (PENDANT)": LocData(59, "_Daru01", 1, ITEM_PENDANT),
        "PBag: Secret tile in VOD": LocData(60, "_VOD01", 3, FILLER_ITEM_PBAG),
        "VOD Container Piece": LocData(61, "_VOD01", 3, ITEM_CONTAINER_HP),
        "River Devil Lake Container Piece": LocData(
            62, "_Kasu01", 3, ITEM_CONTAINER_MP
        ),
        "PBag: Kasuto Swamp cave": LocData(63, "_Kasu01", 3, FILLER_ITEM_PBAG),
        "PBag: Secret tile Kasuto Swamp": LocData(64, "_Kasu01", 3, FILLER_ITEM_PBAG),
        "PBag: Secret forest tile NE of P6": LocData(
            65, "_Kasu01", 3, FILLER_ITEM_PBAG
        ),
        "Seashore-Desert Container-Piece": LocData(66, "_Kasu01", 3, ITEM_CONTAINER_HP),
        "Kasuto-Lake shoals": LocData(67, "_Kasu01", 2, ITEM_CONTAINER_MP),
        "PBag: Raft ride in the sea": LocData(68, "_Drag01", 1, FILLER_ITEM_PBAG),
        "PBag: Dragmire shoals location": LocData(69, "_Drag01", 2, FILLER_ITEM_PBAG),
        "MASK location": LocData(70, "_Drag01", 2, ITEM_MASK),
        "PBag: MASK room, bag 1": LocData(71, "_Drag01", 2, FILLER_ITEM_PBAG),
        "PBag: MASK room, bag 2": LocData(72, "_Drag01", 2, FILLER_ITEM_PBAG),
    }
    locations.update(east)

    maze = {
        "Shoals above P4": LocData(73, "_Maze01", 0, ITEM_1UP_DOLL),
        "CHILD location": LocData(74, "_Maze01", 0, ITEM_CHILD),
        "Maze Isl Hole Container Piece": LocData(75, "_Maze01", 0, ITEM_CONTAINER_MP),
    }
    locations.update(maze)

    town = {
        "JUMP spell room": LocData(76, "_Town01", 0, ITEM_CONTAINER_HP),
        "Target Minigame location": LocData(77, "_Town01", 0, ITEM_CONTAINER_HP),
        "PBag: FAIRY spell room": LocData(78, "_Town01", 0, FILLER_ITEM_PBAG),
        "Nabooru MAP item location": LocData(79, "_Town01", 0, ITEM_MAP1),
        "PBag: Nabooru Chimney PBag location": LocData(
            80, "_Town01", 0, FILLER_ITEM_PBAG
        ),
        "Mido Fairy Container Piece": LocData(81, "_Town01", 0, ITEM_CONTAINER_HP),
        "PBag: FIRE spell room": LocData(82, "_Town01", 0, FILLER_ITEM_PBAG),
        "Darunia Minigame Reward location": LocData(
            83, "_Town01", 0, ITEM_CONTAINER_HP
        ),
        "BRACELET location": LocData(84, "_Town01", 0, ITEM_BRACELET),
        "PBag: BRACELET room": LocData(85, "_Town01", 0, FILLER_ITEM_PBAG),
        "New Kasuto Quest Reward location": LocData(
            86, "_Town01", 0, ITEM_CONTAINER_MP
        ),
        "New Kasuto MAP item location": LocData(87, "_Town01", 0, ITEM_MAP2),
        "Old Kasuto magic piece location": LocData(88, "_Town01", 0, ITEM_CONTAINER_HP),
        "_Skill_Location_Mido": LocData(166, "_Town01", 0, SKILL_STAB_DOWN),
        "_Skill_Location_Darunia": LocData(167, "_Town01", 0, SKILL_STAB_UP),
    }
    locations.update(town)

    return locations


try:
    location_dict = _load_data()
except (FileNotFoundError, json.JSONDecodeError, KeyError):
    location_dict = _load_hardcoded()

# Crystal locs — one real AP check per crystal palace
_CRYSTAL_LOC_BASE = (
    max(
        (v.code - BASE_ID for v in location_dict.values() if v.code is not None),
        default=0,
    )
    + 1
)
location_dict_crystals: Dict[str, LocData] = {
    loc_name: LocData(_CRYSTAL_LOC_BASE + i, "_Dngn01", 0, None)
    for i, (_item, loc_name) in enumerate(PALACE_CRYSTAL.values())
}
location_dict.update(location_dict_crystals)

# Boss-item locs — one optional real check per palace boss
_BOSS_ITEM_LOC_BASE = _CRYSTAL_LOC_BASE + len(location_dict_crystals)
location_dict_boss_items: Dict[str, LocData] = {
    loc_name: LocData(_BOSS_ITEM_LOC_BASE + i, "_Dngn01", 0, None)
    for i, loc_name in enumerate(PALACE_BOSS_ITEM.values())
}
location_dict.update(location_dict_boss_items)

location_dict_events: Dict[str, LocData] = {
    EVENT_VICTORY: LocData(),
}


def location_in_quest(loc_name: str, quest: int) -> bool:
    """True if `loc_name` should be created for the given starting quest (1 or 2).
    Locations tagged for both quests ("12"), untagged, or not in the datapackage
    (crystals, boss items, events) count as present. Only the quest-specific
    exports ("01"/"02") are filtered out for the other quest."""
    ld = location_dict.get(loc_name)
    if ld is None:
        return True
    return str(quest) in ld.quest
