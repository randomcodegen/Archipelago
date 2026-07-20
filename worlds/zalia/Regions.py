from typing import List, Dict

from BaseClasses import MultiWorld, Region, Entrance, Location

from . import Locations
from .Constants import *

CATEGORY_TO_REGION: Dict[str, str] = {
    "_West01": REGION_Z1_AREA,
    "_West02": REGION_MIDORO_FIELD,
    # "_Sari01" is the SOUTH Saria overworld (MEAT, West Saria)
    "_Sari01": REGION_SARIA2,
    "_DMtn01": REGION_DEATH_MTN,
    "_NIsl01": REGION_NORTH_ISLANDS,
    "_RMtn01": REGION_RUTO_MTNS,
    "_SCon01": REGION_SOUTH_CONTINENT,
    "_Nabo01": REGION_NABOORU,
    "_Daru01": REGION_DARUNIA_FIELD,
    "_VOD01": REGION_VALLEY_OF_DEATH,
    "_Kasu01": REGION_KASUTO_AREA,
    "_Drag01": REGION_DRAGMIRE,
    "_Maze01": REGION_MAZE_ISL,
    "_Town01": REGION_Z1_AREA,
    "_Dngn01": REGION_CRYSTAL_HOLDER,
    "_Kaku01": REGION_Z1_AREA,
}

# Town-interior loc name → the town region it belongs to
TOWN_LOC_TO_REGION: Dict[str, str] = {
    "_Spell_Location_Rauru": REGION_RAURU,
    "_Spell_Location_Ruto": REGION_RUTO,
    "_Spell_Location_Saria": REGION_SARIA,
    "_Spell_Location_Mido": REGION_MIDO,
    "_Spell_Location_Nabooru": REGION_NABOORU,
    "_Spell_Location_Darunia": REGION_DARUNIA,
    "_Spell_Location_New_Kasuto": REGION_NEW_KASUTO,
    "_Spell_Location_Old_Kasuto": REGION_OLD_KASUTO,
    # Bulblin wise-man (Summon) — quest-2 only.
    "_Spell_Location_Bulblin": REGION_BULBLIN,
    "JUMP spell room": REGION_RUTO,
    "Target Minigame location": REGION_SARIA,
    "PBag: FAIRY spell room": REGION_MIDO,
    "Nabooru MAP item location": REGION_NABOORU,
    "PBag: Nabooru Chimney PBag location": REGION_NABOORU,
    "Mido Fairy Container Piece location": REGION_MIDO,
    "_Skill_Location_Mido": REGION_MIDO,
    "_Skill_Location_Darunia": REGION_DARUNIA,
    "PBag: FIRE spell room": REGION_NABOORU,
    "MEAT location": REGION_SARIA2,
    "PBag: West Saria River Waterfall": REGION_SARIA2,
    "PBag: Forest above Saria Lake": REGION_SARIA2,
    "Darunia Minigame Reward location": REGION_DARUNIA,
    "BRACELET location": REGION_NEW_KASUTO,
    "PBag: BRACELET room": REGION_NEW_KASUTO,
    "New Kasuto Quest Reward location": REGION_NEW_KASUTO,
    "New Kasuto MAP item location": REGION_NEW_KASUTO,
    "Old Kasuto magic piece location": REGION_OLD_KASUTO,
}

# Content regions that participate in the shuffle
SHUFFLED_TOWN_REGIONS = {TOWN_TO_REGION[t] for t in SHUFFLE_TOWNS}
INTERIOR_TOWN_LOCATIONS = {
    loc for loc, region in TOWN_LOC_TO_REGION.items() if region in SHUFFLED_TOWN_REGIONS
}


def _dungeon_region_for_loc(loc_name: str, loc_num: int = 0) -> str:
    """Map a dungeon location to its palace region by name or location number."""
    name_lower = loc_name.lower()
    if "great palace" in name_lower or "p7" in name_lower.split():
        return REGION_GREAT_PALACE
    tokens = set(
        name_lower.replace(":", " ")
        .replace(",", " ")
        .replace("(", " ")
        .replace(")", " ")
        .split()
    )
    if "p1" in tokens or "parapa" in name_lower:
        return REGION_PARAPA_PALACE
    if "p2" in tokens or "midoro" in name_lower:
        return REGION_MIDORO_PALACE
    if "p3" in tokens or "island" in name_lower:
        return REGION_ISLAND_PALACE
    if "p4" in tokens or "maze" in name_lower:
        return REGION_MAZE_PALACE
    if "p5" in tokens or "palace on the sea" in name_lower:
        return REGION_PALACE_ON_THE_SEA
    if "p6" in tokens or "three eye" in name_lower:
        return REGION_THREE_EYE_PALACE
    # Fall back to loc number ranges from the JSON data
    if loc_num >= 83 and loc_num <= 88:
        return REGION_PARAPA_PALACE
    if loc_num >= 89 and loc_num <= 95:
        return REGION_MIDORO_PALACE
    if loc_num >= 96 and loc_num <= 106:
        return REGION_ISLAND_PALACE
    if loc_num >= 107 and loc_num <= 118:
        return REGION_MAZE_PALACE
    if loc_num >= 119 and loc_num <= 130:
        return REGION_PALACE_ON_THE_SEA
    if loc_num >= 131 and loc_num <= 147:
        return REGION_THREE_EYE_PALACE
    if loc_num >= 148:
        return REGION_GREAT_PALACE
    return REGION_CRYSTAL_HOLDER


def build_region_dict() -> Dict[str, List[str]]:
    grouped: Dict[str, List[str]] = {
        REGION_MENU: [],
        REGION_Z1_AREA: [],
        REGION_EAST: [],
        REGION_KASUTO_AREA: [],
        REGION_MAZE_ISL: [],
        REGION_MIDORO_FIELD: [],
        REGION_MORUGE_SWAMP: [],
        REGION_DARUNIA_FIELD: [],
        REGION_ROYAL_CEMETERY: [],
        REGION_SARIA: [],
        REGION_SARIA2: [],
        REGION_VALLEY_OF_DEATH: [],
        REGION_SOUTH_CONTINENT: [],
        REGION_DEATH_MTN: [],
        REGION_NORTH_ISLANDS: [],
        REGION_RUTO_MTNS: [],
        REGION_RUTO_MTN_RUINS: [],
        REGION_DRAGMIRE: [],
        REGION_RAURU: [],
        REGION_RUTO: [],
        REGION_MIDO: [],
        REGION_NABOORU: [],
        REGION_DARUNIA: [],
        REGION_NEW_KASUTO: [],
        REGION_OLD_KASUTO: [],
        REGION_BULBLIN: [],
        REGION_PARAPA_PALACE: [],
        REGION_MIDORO_PALACE: [],
        REGION_ISLAND_PALACE: [],
        REGION_MAZE_PALACE: [],
        REGION_PALACE_ON_THE_SEA: [],
        REGION_THREE_EYE_PALACE: [],
        REGION_GREAT_PALACE: [],
        REGION_DRAGMIRE_TOWER: [],
        REGION_CRYSTAL_HOLDER: [],
    }

    RMTN_LOC_TO_REGION = {
        "PBag: N Ruto Mtn Ruins Plaforming Challenge": REGION_RUTO_MTN_RUINS,
        "PBag: N Ruto Mtn Ruins Rocky Alcove": REGION_RUTO_MTN_RUINS,
        "RescueFairy Location": REGION_RUTO_MTN_RUINS,
    }

    WEST02_LOC_TO_REGION = {
        "PBag: Secret tile SW of Royal Cemetery": REGION_ROYAL_CEMETERY,
        "Royal Cemetery Container Piece location": REGION_ROYAL_CEMETERY,
        "Under Kings Tomb location (SHIELD)": REGION_ROYAL_CEMETERY,
    }

    NISL01_LOC_TO_REGION = {
        "PBag: Island N of Tantari Desert": REGION_Z1_AREA,
        "PBag: Sea Cave N end of Ruto Mtns": REGION_Z1_AREA,
        "North Isl Container Piece location": REGION_Z1_AREA,
    }

    DMTN01_LOC_TO_REGION = {
        "MIRROR location": REGION_SARIA2,
        "PBag: Island between Death Mtn and Royal Cemetery": REGION_ROYAL_CEMETERY,
    }

    # Individual Kakusu (Gold Slime) locs -> the exact region
    KAKUSU_REGIONS = [
        REGION_Z1_AREA,  # 1 North Castle
        REGION_PARAPA_PALACE,  # 2 Parapa Palace
        REGION_Z1_AREA,  # 3 Death Mountain (reached from Z1)
        REGION_ROYAL_CEMETERY,  # 4 Death Mountain top bridge
        REGION_RUTO_MTN_RUINS,  # 5 North Ruto Mountains
        REGION_ISLAND_PALACE,  # 6 Island Palace
        REGION_DARUNIA,  # 7 Darunia
        REGION_DARUNIA_FIELD,  # 8 Darunia Forest
        REGION_MAZE_ISL,  # 9 Maze Island
        REGION_THREE_EYE_PALACE,  # 10 Three Eye Rock Palace
        REGION_KASUTO_AREA,  # 11 Kasuto Cemetery
        REGION_NORTH_ISLANDS,  # 12 North Islands
    ]
    KAKUSU_LOC_TO_REGION = {
        name: KAKUSU_REGIONS[i] for i, name in enumerate(KAKUSU_LOCATION_NAMES)
    }

    for loc_name, loc_data in Locations.location_dict.items():
        if (
            loc_name in Locations.location_dict_crystals
            or loc_name in Locations.location_dict_boss_items
        ):
            continue
        cat = loc_data.category
        region_name = CATEGORY_TO_REGION.get(cat)
        if cat == "_Dngn01":
            loc_num = (loc_data.code - BASE_ID) + 1 if loc_data.code is not None else 0
            region_name = _dungeon_region_for_loc(loc_name, loc_num)
        elif cat == "_Town01":
            region_name = TOWN_LOC_TO_REGION.get(loc_name, region_name)
        elif cat == "_Kaku01":
            region_name = KAKUSU_LOC_TO_REGION.get(loc_name, region_name)
        elif cat == "_RMtn01":
            region_name = RMTN_LOC_TO_REGION.get(loc_name, region_name)
        elif cat == "_West02":
            region_name = WEST02_LOC_TO_REGION.get(loc_name, region_name)
        elif cat == "_NIsl01":
            region_name = NISL01_LOC_TO_REGION.get(loc_name, region_name)
        elif cat == "_DMtn01":
            region_name = DMTN01_LOC_TO_REGION.get(loc_name, region_name)
        if region_name and region_name in grouped:
            grouped[region_name].append(loc_name)

    return grouped


region_dict: Dict[str, List[str]] = build_region_dict()


def _grouped_for_player(world) -> Dict[str, List[str]]:
    """region_dict with town interiors relocated to the position their content
    occupies. Only _Town01 interiors move; overworld/Kakusu locations bound to a
    town region stay put."""
    grouped: Dict[str, List[str]] = {
        name: list(locs) for name, locs in region_dict.items()
    }

    # "GP PBag: Next to fast travel" (Area_PalcG room $3C — no requirement)
    _gp_tile_parent = world.dungeon_to_parent[REGION_GREAT_PALACE]
    if GP_OUTSIDE_LOCATION in grouped.get(REGION_GREAT_PALACE, []):
        grouped[REGION_GREAT_PALACE].remove(GP_OUTSIDE_LOCATION)
        grouped.setdefault(_gp_tile_parent, []).append(GP_OUTSIDE_LOCATION)

    if not world.options.randomize_town_locations.value:
        return grouped
    # Strip interiors from every shuffled town region
    for region_name in SHUFFLED_TOWN_REGIONS:
        grouped[region_name] = [
            n for n in grouped[region_name] if n not in INTERIOR_TOWN_LOCATIONS
        ]
    for content_town, position in world.town_position.items():
        content_region = TOWN_TO_REGION[content_town]
        if content_region not in SHUFFLED_TOWN_REGIONS:
            continue  # Bulblin: fixed, interiors already in place
        interiors = [
            n for n in region_dict[content_region] if n in INTERIOR_TOWN_LOCATIONS
        ]
        grouped[TOWN_TO_REGION[position]].extend(interiors)
    return grouped


def create_regions(world, player: int):
    multiworld = world.multiworld
    grouped = _grouped_for_player(world)

    # Expose the per-seed random subset of Kakusu chosen
    selected_kakusu = {
        KAKUSU_LOCATION_NAMES[i - 1] for i in world.kakusu_selected_indices
    }
    excluded_kakusu = set(KAKUSU_LOCATION_NAMES) - selected_kakusu

    # Only build locs that exist in the chosen quest
    _quest = world.options.starting_quest.value
    for region_name in region_dict:
        region = Region(region_name, player, multiworld)
        names = [
            n
            for n in grouped.get(region_name, [])
            if n not in excluded_kakusu and Locations.location_in_quest(n, _quest)
        ]
        _set_region_locations(region, names, player)
        multiworld.regions.append(region)
    _create_event_locations(world, player)
    connect_regions(world, player)


def _set_region_locations(region: Region, location_names: List[str], player: int):
    region.locations = [
        Locations.ZALiALocation(
            player, name, Locations.location_dict[name].code, region
        )
        for name in location_names
        if name in Locations.location_dict
    ]


def _create_event_locations(world, player: int):
    multiworld = world.multiworld

    # Crystal loc in each palace
    for palace_name, (crystal_item, crystal_loc_name) in PALACE_CRYSTAL.items():
        palace_region = multiworld.get_region(palace_name, player)
        loc = Locations.ZALiALocation(
            player,
            crystal_loc_name,
            Locations.location_dict[crystal_loc_name].code,
            palace_region,
        )
        loc.place_locked_item(world.create_item(crystal_item))
        palace_region.locations.append(loc)

    # Optional boss-item loc at each palace boss
    if world.options.boss_item_locations.value:
        for palace_name, boss_item_loc_name in PALACE_BOSS_ITEM.items():
            palace_region = multiworld.get_region(palace_name, player)
            loc = Locations.ZALiALocation(
                player,
                boss_item_loc_name,
                Locations.location_dict[boss_item_loc_name].code,
                palace_region,
            )
            palace_region.locations.append(loc)

    # Victory event. Quest 1 ends at the Great Palace
    # Quest 2 at Ganon fight
    if world.options.starting_quest.value == 2:
        victory_region = multiworld.get_region(REGION_DRAGMIRE_TOWER, player)
    else:
        victory_region = multiworld.get_region(REGION_GREAT_PALACE, player)
    if "Victory" not in Locations.location_dict:
        loc = Locations.ZALiALocation(player, "Victory", None, victory_region)
        loc.place_locked_item(world.create_item(EVENT_VICTORY))
        victory_region.locations.append(loc)


def _connect(
    world, player: int, source: str, target: str, name: str = None
) -> Entrance:
    multiworld = world.multiworld
    src = multiworld.get_region(source, player)
    dst = multiworld.get_region(target, player)
    if name is None:
        name = f"{source} → {target}"
    conn = Entrance(player, name, src)
    src.exits.append(conn)
    conn.connect(dst)
    return conn


def connect_regions(world, player: int):
    multiworld = world.multiworld

    # Menu → Z1 Area
    _connect(world, player, REGION_MENU, REGION_Z1_AREA, "Enter Z1 Area")

    # Overworld town POSITIONS
    for position, parent_region in TOWN_POSITION_PARENT.items():
        _connect(world, player, parent_region, TOWN_TO_REGION[position])

    # Rauru → Midoro Field (3 routes)
    _connect(world, player, REGION_RAURU, REGION_MIDORO_FIELD, "Rauru Pass")
    _connect(world, player, REGION_RAURU, REGION_MIDORO_FIELD, "Rauru to Midoro Cave")
    _connect(world, player, REGION_RAURU, REGION_MIDORO_FIELD, "JUMP Cave")

    # Mido → Midoro Field (the Mido boulder)
    _connect(world, player, REGION_MIDO, REGION_MIDORO_FIELD)

    # Saria → Midoro Field
    _connect(world, player, REGION_SARIA, REGION_MIDORO_FIELD)

    # Mido fast travel to Saria
    _connect(world, player, REGION_MIDO, REGION_SARIA, "Mido to Saria Fast Travel")

    # Z1 Area → Mido directly via the Fire-Vines Cave
    _connect(world, player, REGION_Z1_AREA, REGION_MIDO, "Z1 Area → Mido via Fire Cave")

    # Mido harbour → Royal Cemetery
    _connect(
        world, player, REGION_MIDO, REGION_ROYAL_CEMETERY, "Mido to Royal Cemetery"
    )

    # Midoro Field → Royal Cemetery (main path, boulder-gated)
    _connect(world, player, REGION_MIDORO_FIELD, REGION_ROYAL_CEMETERY)

    # Midoro Field → Moruge Swamp (adjacent)
    _connect(world, player, REGION_MIDORO_FIELD, REGION_MORUGE_SWAMP)

    # Saria ↔ Saria2 (Saria Bridge, bidirectional)
    _connect(world, player, REGION_SARIA, REGION_SARIA2, "Saria Bridge")
    _connect(world, player, REGION_SARIA2, REGION_SARIA, "Saria Bridge Reverse")

    # Saria2 ↔ Death Mountain (bidirectional)
    _connect(world, player, REGION_SARIA2, REGION_DEATH_MTN)
    _connect(world, player, REGION_DEATH_MTN, REGION_SARIA2, "Death Mountain to Saria2")

    # Royal Cemetery ↔ Death Mountain (bidirectional)
    _connect(world, player, REGION_ROYAL_CEMETERY, REGION_DEATH_MTN)
    _connect(
        world,
        player,
        REGION_DEATH_MTN,
        REGION_ROYAL_CEMETERY,
        "Death Mountain to Royal Cemetery",
    )

    # Royal Cemetery → Z1 Area (back way)
    _connect(
        world, player, REGION_ROYAL_CEMETERY, REGION_Z1_AREA, "Royal Cemetery to Z1"
    )

    # Death Mountain → Z1 Area (back way)
    _connect(world, player, REGION_DEATH_MTN, REGION_Z1_AREA, "Death Mountain to Z1")

    # Death Mountain → East (south exit reaches Mido harbour)
    _connect(
        world, player, REGION_DEATH_MTN, REGION_EAST, "Death Mountain to East via Raft"
    )

    # Mido → East continent (raft crossing from Mido harbour)
    _connect(world, player, REGION_MIDO, REGION_EAST, "Raft to East")

    # Z1 Area → North Islands (raft + mountain pass)
    _connect(
        world, player, REGION_Z1_AREA, REGION_NORTH_ISLANDS, "Raft to North Islands"
    )

    # North Islands → Mido (the GML "Whale Isl warp to Mido"
    _connect(world, player, REGION_NORTH_ISLANDS, REGION_MIDO, "North Islands → Mido")

    # Dungeon regions — dynamically connected based on shuffle
    for dungeon_region, parent_region in world.dungeon_to_parent.items():
        _connect(world, player, parent_region, dungeon_region)

    # East continent connections
    _connect(world, player, REGION_EAST, REGION_KASUTO_AREA)

    # East → Darunia Field (via Nabooru)
    _connect(world, player, REGION_NABOORU, REGION_DARUNIA_FIELD)
    _connect(world, player, REGION_EAST, REGION_DARUNIA_FIELD)

    # Darunia Field → Maze Island
    _connect(world, player, REGION_DARUNIA_FIELD, REGION_MAZE_ISL)

    # Kasuto Area → Valley of Death → Dragmire
    _connect(world, player, REGION_KASUTO_AREA, REGION_VALLEY_OF_DEATH)
    _connect(world, player, REGION_VALLEY_OF_DEATH, REGION_DRAGMIRE)
    _connect(world, player, REGION_KASUTO_AREA, REGION_DRAGMIRE_TOWER)

    # Ruto → Ruto Mountains
    _connect(world, player, REGION_RUTO, REGION_RUTO_MTNS)

    # Ruto Mountains → Ruto Mountains Ruins
    _connect(world, player, REGION_RUTO_MTNS, REGION_RUTO_MTN_RUINS)

    # East → South Continent (Kakusu area)
    _connect(world, player, REGION_EAST, REGION_SOUTH_CONTINENT)

    # East → Maze Island
    _connect(world, player, REGION_EAST, REGION_MAZE_ISL)

    # Z1 Area → Crystal Holder
    _connect(world, player, REGION_Z1_AREA, REGION_CRYSTAL_HOLDER)
