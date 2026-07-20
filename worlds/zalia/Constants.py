GAME_NAME: str = "ZALiA"
BASE_ID: int = 0x005A414C4941  # ZALIA

# Filler item names
FILLER_ITEM_PBAG: str = "P-Bag"

# Useful items (permanent upgrades, multiple copies exist
ITEM_CONTAINER_HP: str = "Container Piece (HP)"
ITEM_CONTAINER_MP: str = "Container Piece (MP)"
ITEM_1UP_DOLL: str = "1-Up Doll"

# Progression items - overworld tools
ITEM_CANDLE: str = "Candle"
ITEM_GLOVE: str = "Glove"
ITEM_RAFT: str = "Raft"
ITEM_BOOTS: str = "Boots"
ITEM_FLUTE: str = "Flute"
ITEM_CROSS: str = "Cross"
ITEM_HAMMER: str = "Hammer"
ITEM_BRACELET: str = "Bracelet"
ITEM_MIRROR: str = "Mirror"
ITEM_FLOWER: str = "Flower"
ITEM_BOOK: str = "Book"
ITEM_MEAT: str = "Meat"
ITEM_SHIELD: str = "Shield"
ITEM_KEY: str = "AllKey"
ITEM_PENDANT: str = "Pendant"
ITEM_SWORD: str = "Sword"
ITEM_TROPHY: str = "Trophy"
ITEM_RING: str = "Ring"
ITEM_MASK: str = "Mask"
ITEM_NOTE: str = "Note"
ITEM_MAP1: str = "Map (Nabooru)"
ITEM_MAP2: str = "Map (New Kasuto)"
ITEM_CHILD: str = "Child"
ITEM_RESCUE_FAIRY: str = "Rescue Fairy"
ITEM_BOTTLE: str = "Bottle"

# Spells
SPELL_PROTECT: str = "Spell: Shield"
SPELL_JUMP: str = "Spell: Jump"
SPELL_HEAL: str = "Spell: Heal"
SPELL_FAIRY: str = "Spell: Fairy"
SPELL_FIRE: str = "Spell: Fire"
SPELL_REFLECT: str = "Spell: Reflect"
SPELL_ENIGMA: str = "Spell: Enigma"
SPELL_THUNDER: str = "Spell: Thunder"
SPELL_SUMMON: str = "Spell: Summon"

# Skills
SKILL_STAB_DOWN: str = "Skill: Stab Down"
SKILL_STAB_UP: str = "Skill: Stab Up"


# Event items
EVENT_VICTORY: str = "Victory"

# Region names
REGION_MENU: str = "Menu"
REGION_Z1_AREA: str = "Z1 Area"
REGION_EAST: str = "East"
REGION_KASUTO_AREA: str = "Kasuto Area"
REGION_MAZE_ISL: str = "Maze Island"
REGION_MIDORO_FIELD: str = "Midoro Field"
REGION_MORUGE_SWAMP: str = "Moruge Swamp"
REGION_DARUNIA_FIELD: str = "Darunia Field"
REGION_ROYAL_CEMETERY: str = "Royal Cemetery"
REGION_SARIA: str = "Saria"
REGION_SARIA2: str = "Saria2"
REGION_NABOORU: str = "Nabooru"
REGION_DARUNIA: str = "Darunia"
REGION_RUTO: str = "Ruto"
REGION_MIDO: str = "Mido"
REGION_RAURU: str = "Rauru"
REGION_NEW_KASUTO: str = "New Kasuto"
REGION_OLD_KASUTO: str = "Old Kasuto"
REGION_BULBLIN: str = "Bulblin"
REGION_DEATH_MTN: str = "Death Mountain"
REGION_NORTH_ISLANDS: str = "North Islands"
REGION_RUTO_MTNS: str = "Ruto Mountains"
REGION_RUTO_MTN_RUINS: str = "Ruto Mountains Ruins"
REGION_VALLEY_OF_DEATH: str = "Valley of Death"
REGION_SOUTH_CONTINENT: str = "South Continent"
REGION_DRAGMIRE: str = "Dragmire"
REGION_PARAPA_PALACE: str = "Parapa Palace"
REGION_MIDORO_PALACE: str = "Midoro Palace"
REGION_ISLAND_PALACE: str = "Island Palace"
REGION_MAZE_PALACE: str = "Maze Island Palace"
REGION_PALACE_ON_THE_SEA: str = "Palace on the Sea"
REGION_THREE_EYE_PALACE: str = "Three Eye Rock Palace"
REGION_GREAT_PALACE: str = "Great Palace"
REGION_DRAGMIRE_TOWER: str = "Dragmire Tower"
REGION_CRYSTAL_HOLDER: str = "Crystal Holder"

# "Outside, back entrance" P-Bag at the Great Palace
# no requirements
GP_OUTSIDE_LOCATION: str = "GP PBag: Next to fast travel"

# Town position names (all overworld town positions)
TOWN_POSITIONS: list = [
    "Rauru",
    "Ruto",
    "Saria",
    "Mido",
    "Nabooru",
    "Darunia",
    "New Kasuto",
    "Old Kasuto",
    "Bulblin",
]

# Towns that participate in the position shuffle.
# Bulblin is fixed.
SHUFFLE_TOWNS: list = [
    "Rauru",
    "Ruto",
    "Saria",
    "Mido",
    "Nabooru",
    "Darunia",
    "New Kasuto",
    "Old Kasuto",
]

# Parent region for each overworld town position
TOWN_POSITION_PARENT: dict = {
    "Rauru": REGION_Z1_AREA,
    "Ruto": REGION_Z1_AREA,
    "Saria": REGION_MIDORO_FIELD,
    "Mido": REGION_MIDORO_FIELD,
    "Nabooru": REGION_EAST,
    "Darunia": REGION_EAST,  # GML STR_Darunia == can_reach_DaruniaField ==
    "New Kasuto": REGION_EAST,  # GML STR_New_Kasuto adds
    "Old Kasuto": REGION_KASUTO_AREA,  # GML STR_Old_Kasuto == can_reach_KasutoArea
    "Bulblin": REGION_EAST,
}

# Town name → its region.
TOWN_TO_REGION: dict = {
    "Rauru": REGION_RAURU,
    "Ruto": REGION_RUTO,
    "Saria": REGION_SARIA,
    "Mido": REGION_MIDO,
    "Nabooru": REGION_NABOORU,
    "Darunia": REGION_DARUNIA,
    "New Kasuto": REGION_NEW_KASUTO,
    "Old Kasuto": REGION_OLD_KASUTO,
    "Bulblin": REGION_BULBLIN,
}

# Crystal items — one real progression item per crystal
CRYSTAL_ITEMS: list = [
    "Crystal of Parapa",
    "Crystal of Midoro",
    "Crystal of Island",
    "Crystal of Maze",
    "Crystal of Sea",
    "Crystal of Three Eye",
]

# Palace region → (crystal item, crystal loc name)
PALACE_CRYSTAL: dict = {
    REGION_PARAPA_PALACE: (CRYSTAL_ITEMS[0], "Parapa Palace: Crystal"),
    REGION_MIDORO_PALACE: (CRYSTAL_ITEMS[1], "Midoro Palace: Crystal"),
    REGION_ISLAND_PALACE: (CRYSTAL_ITEMS[2], "Island Palace: Crystal"),
    REGION_MAZE_PALACE: (CRYSTAL_ITEMS[3], "Maze Island Palace: Crystal"),
    REGION_PALACE_ON_THE_SEA: (CRYSTAL_ITEMS[4], "Palace on the Sea: Crystal"),
    REGION_THREE_EYE_PALACE: (CRYSTAL_ITEMS[5], "Three Eye Rock Palace: Crystal"),
}

# TODO: Implement as actual location + option
# Optional extra loc at each palace boss holding a crystal
PALACE_BOSS_ITEM: dict = {
    REGION_PARAPA_PALACE: "Parapa Palace: Boss Item",
    REGION_MIDORO_PALACE: "Midoro Palace: Boss Item",
    REGION_ISLAND_PALACE: "Island Palace: Boss Item",
    REGION_MAZE_PALACE: "Maze Island Palace: Boss Item",
    REGION_PALACE_ON_THE_SEA: "Palace on the Sea: Boss Item",
    REGION_THREE_EYE_PALACE: "Three Eye Rock Palace: Boss Item",
}

# Key names per palace
KEY_PARAPA: str = "Small Key (Parapa)"
KEY_MIDORO: str = "Small Key (Midoro)"
KEY_ISLAND: str = "Small Key (Island)"
KEY_MAZE: str = "Small Key (Maze)"
KEY_SEA: str = "Small Key (Sea)"
KEY_THREE_EYE: str = "Small Key (Three Eye)"

SPELL_TO_TOWN: dict = {
    SPELL_PROTECT: "Rauru",
    SPELL_JUMP: "Ruto",
    SPELL_HEAL: "Saria",
    SPELL_FAIRY: "Mido",
    SPELL_FIRE: "Nabooru",
    SPELL_REFLECT: "Darunia",
    SPELL_ENIGMA: "New Kasuto",
    SPELL_THUNDER: "Old Kasuto",
    SPELL_SUMMON: "Bulblin",
}

KEY_COUNTS: dict = {
    REGION_PARAPA_PALACE: (KEY_PARAPA, 3),
    REGION_MIDORO_PALACE: (KEY_MIDORO, 4),
    REGION_ISLAND_PALACE: (KEY_ISLAND, 4),
    REGION_MAZE_PALACE: (KEY_MAZE, 6),
    REGION_PALACE_ON_THE_SEA: (KEY_SEA, 5),
    REGION_THREE_EYE_PALACE: (KEY_THREE_EYE, 6),
}

# Individual Gold Slime (Kakusu) check locs
KAKUSU_LOCATION_NAMES: list = [
    "Kakusu: North Castle, room above East entrance",  # 1 WestA_32
    "Kakusu: Parapa Palace, light all torches",  # 2 PalcA_FC
    "Kakusu: Death Mountain, jump on all pillars",  # 3 DthMt_0F
    "Kakusu: Death Mountain, under the top bridge",  # 4 DthMt_2C
    "Kakusu: North Ruto Mountains",  # 5 WestA_F8
    "Kakusu: Island Palace, fall and downstab",  # 6 PalcC_11
    "Kakusu: Darunia, killed by falling block",  # 7 TownA_7E
    "Kakusu: Darunia Forest, hidden in the dark",  # 8 EastA_23
    "Kakusu: Maze Island, statue under rocky ground",  # 9 MazIs_09
    "Kakusu: Three Eye Rock Palace",  # 10 PalcF_1E
    "Kakusu: Kasuto Cemetery, spell combo to reveal",  # 11 EastA_36
    "Kakusu: North Islands, high pillar needs THUNDER",  # 12 EastA_37
]

# Dungeon position → parent region
DUNGEON_POSITION_PARENT: dict = {
    REGION_PARAPA_PALACE: REGION_Z1_AREA,
    REGION_MIDORO_PALACE: REGION_MIDORO_FIELD,
    REGION_ISLAND_PALACE: REGION_ROYAL_CEMETERY,
    REGION_MAZE_PALACE: REGION_DARUNIA_FIELD,
    REGION_PALACE_ON_THE_SEA: REGION_EAST,
    REGION_THREE_EYE_PALACE: REGION_KASUTO_AREA,
    REGION_GREAT_PALACE: REGION_CRYSTAL_HOLDER,
}

# Per-loc key thresholds (moves key check from entrance to


LOCATION_KEY_REQS: dict = {
    # ---- Parapa Palace (3 keys) ----
    "P1 Key 3": None,
    "P1 Key 1": (KEY_PARAPA, 1),
    "P1 Key 2": (KEY_PARAPA, 1),
    "P1 Container Piece location": (KEY_PARAPA, 1),
    "P1 Item location": (KEY_PARAPA, 3),
    # ---- Midoro Palace (4 keys) ----
    "P2 Key 1": (KEY_MIDORO, 1),
    "P2 Key 2": None,
    "P2 Key 3": (KEY_MIDORO, 1),  # GML $0E: GLOVE + 1 key
    # Key 4 (room $10): reachable with no locked doors
    "P2 Key 4": None,
    "P2 Container Piece location": (KEY_MIDORO, 1),
    "P2 Item location": (KEY_MIDORO, 4),
    # ---- Island Palace (4 keys) ----
    "P3 Key 1": None,
    "P3 Key 2": None,
    "P3 Key 3": (KEY_ISLAND, 3),
    "P3 Key 4": (KEY_ISLAND, 3),
    "P3 Item location": (KEY_ISLAND, 4),
    "P3 Container Piece location": (KEY_ISLAND, 4),
    # ---- Maze Island Palace (6 keys) ----
    "P4 Key 1": (KEY_MAZE, 4),
    "P4 Key 2": (KEY_MAZE, 3),
    "P4 Key 3": (KEY_MAZE, 4),
    "P4 Key 4": None,
    "P4 Key 5": None,
    "P4 Key 6": None,
    "P4 Container Piece location": None,
    "P4 Item location": (KEY_MAZE, 6),
    # ---- Palace on the Sea (5 keys) ----
    "P5 Key 1": None,
    "P5 Key 2": (KEY_SEA, 1),
    "P5 Key 3": (KEY_SEA, 1),
    "P5 Key 4": (KEY_SEA, 1),
    "P5 Key 5": (KEY_SEA, 4),
    "P5 Container Piece location": None,
    "P5 Item location": (KEY_SEA, 5),
    # ---- Three Eye Rock Palace (6 keys) ----
    "P6 Key 1": None,
    "P6 Key 2": (KEY_THREE_EYE, 1),
    "P6 Key 3": (KEY_THREE_EYE, 2),
    "P6 Key 4 (falling key)": (KEY_THREE_EYE, 1),  # GML $13: 1 key
    "P6 Key 5": (KEY_THREE_EYE, 4),
    "P6 Key 6": (KEY_THREE_EYE, 4),  # GML $1F: 4 keys
    "P6 Item location": (KEY_THREE_EYE, 5),
    "P6 Container Piece location": (KEY_THREE_EYE, 6),
    # ---- Great Palace ----
    "Great Palace Item location (SKELETON KEY)": None,
}
