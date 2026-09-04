from typing import TYPE_CHECKING, List
from BaseClasses import CollectionState, Location, Entrance, LocationProgressType
from worlds.generic.Rules import set_rule, add_rule
from .Constants import *
from . import Locations

if TYPE_CHECKING:
    from . import ZALiAWorld


def set_rules(world: "ZALiAWorld"):
    multiworld = world.multiworld
    player = world.player

    _is_quest2 = world.options.starting_quest.value == 2

    def _has(state: CollectionState, item: str) -> bool:
        return state.has(item, player)

    def _any(state: CollectionState, *items: str) -> bool:
        return any(state.has(item, player) for item in items)

    def _has_key_count(state: CollectionState, key_name: str, count: int) -> bool:
        """AllKey opens every lock; otherwise require the palace's small-key count."""
        return _has(state, ITEM_KEY) or state.count(key_name, player) >= count

    def _dark_room_ok(state: CollectionState, threshold: int = 1) -> bool:
        """Dark room is passable if the difficulty option >= threshold or player has a light source.
        0: always need CANDLE/FIRE. 1: threshold-1 rooms free. 2: all rooms free."""
        dark_opt = world.options.dark_room_difficulty.value
        return dark_opt >= threshold or _any(state, ITEM_CANDLE, SPELL_FIRE)

    # Fixed at gen time
    _hard_logic = bool(world.options.hard_logic_tricks.value)

    # Rauru → Midoro Field via Rauru Pass
    _rauru_ver = world.ruaru_pass_version
    if _rauru_ver == 1:
        set_rule(
            world.get_entrance("Rauru Pass"), lambda state: _has(state, ITEM_HAMMER)
        )
    elif _rauru_ver == 2:
        set_rule(
            world.get_entrance("Rauru Pass"), lambda state: _has(state, ITEM_FLUTE)
        )
    else:
        set_rule(
            world.get_entrance("Rauru Pass"),
            lambda state: _any(state, ITEM_GLOVE, ITEM_BRACELET),
        )

    # Rauru → Midoro Field via cave
    set_rule(
        world.get_entrance("Rauru to Midoro Cave"),
        lambda state: _any(state, ITEM_GLOVE, ITEM_BRACELET),
    )

    # Rauru → Midoro Field via JUMP Cave
    set_rule(
        world.get_entrance("JUMP Cave"),
        lambda state: _has(state, SPELL_JUMP) and _dark_room_ok(state, 1),
    )

    # Midoro Field → Royal Cemetery — HAMMER to break boulder
    set_rule(
        world.get_entrance("Midoro Field → Royal Cemetery"),
        lambda state: _has(state, ITEM_HAMMER),
    )

    # Saria Bridge (both directions): BAGU_NOTE or JUMP+FAIRY to cross
    set_rule(
        world.get_entrance("Saria Bridge"),
        lambda state: _has(state, ITEM_NOTE)
        or (_has(state, SPELL_JUMP) and _has(state, SPELL_FAIRY)),
    )
    set_rule(
        world.get_entrance("Saria Bridge Reverse"),
        lambda state: _has(state, ITEM_NOTE)
        or (_has(state, SPELL_JUMP) and _has(state, SPELL_FAIRY)),
    )

    # Saria2 → Death Mountain — dark room >= 2
    set_rule(
        world.get_entrance("Saria2 → Death Mountain"),
        lambda state: _dark_room_ok(state, 2),
    )

    # Death Mountain → Saria2 (back way, reverse of the above)
    set_rule(
        world.get_entrance("Death Mountain to Saria2"),
        lambda state: _dark_room_ok(state, 2),
    )

    # Royal Cemetery → Death Mountain — dark room >= 2
    set_rule(
        world.get_entrance("Royal Cemetery → Death Mountain"),
        lambda state: _dark_room_ok(state, 2),
    )

    # Death Mountain → Royal Cemetery — dark room >= 2
    set_rule(
        world.get_entrance("Death Mountain to Royal Cemetery"),
        lambda state: _dark_room_ok(state, 2),
    )

    # Royal Cemetery → Z1 Area (back way) — BOOTS or dark room
    set_rule(
        world.get_entrance("Royal Cemetery to Z1"),
        lambda state: _has(state, ITEM_BOOTS) or _dark_room_ok(state, 1),
    )

    # Death Mountain → Z1 Area (back way) — dark room >= 2
    set_rule(
        world.get_entrance("Death Mountain to Z1"),
        lambda state: _dark_room_ok(state, 2),
    )

    # Death Mountain → East via raft (south exit to Mido)
    set_rule(
        world.get_entrance("Death Mountain to East via Raft"),
        lambda state: _dark_room_ok(state, 1) and _has(state, ITEM_RAFT),
    )

    ### Raft-reachable regions

    # Mido → East continent — needs RAFT (HAMMER/FIRE to reach)
    set_rule(world.get_entrance("Raft to East"), lambda state: _has(state, ITEM_RAFT))

    # Z1 Area → North Islands — RAFT + HAMMER + (JUMP or FAIRY)
    set_rule(
        world.get_entrance("Raft to North Islands"),
        lambda state: _has(state, ITEM_RAFT)
        and _has(state, ITEM_HAMMER)
        and _any(state, SPELL_JUMP, SPELL_FAIRY),
    )

    # Kasuto Area → Valley of Death (invisible enemies need cross)
    set_rule(
        world.get_entrance("Kasuto Area → Valley of Death"),
        lambda state: _has(state, ITEM_CROSS),
    )

    # Ruto → Ruto Mountains (near shore -- JUMP only)
    set_rule(
        world.get_entrance("Ruto → Ruto Mountains"),
        lambda state: _has(state, SPELL_JUMP),
    )

    # Ruto Mountains → Ruto Mountains Ruins
    set_rule(
        world.get_entrance("Ruto Mountains → Ruto Mountains Ruins"),
        lambda state: _any(state, SKILL_STAB_DOWN, SPELL_FAIRY)
        and _dark_room_ok(state, 1),
    )

    ### East continent interior connections

    # East → Kasuto Area: FLUTE (past the River Devil) OR boots
    set_rule(
        world.get_entrance("East → Kasuto Area"),
        lambda state: _has(state, ITEM_FLUTE)
        or (_has(state, ITEM_BRACELET) and _has(state, ITEM_BOOTS)),
    )

    # Darunia Field → Maze Island — needs STABDOWN
    set_rule(
        world.get_entrance("Darunia Field → Maze Island"),
        lambda state: _has(state, SKILL_STAB_DOWN),
    )

    # East → Maze Island
    set_rule(
        world.get_entrance("East → Maze Island"),
        lambda state: _has(state, SKILL_STAB_DOWN),
    )

    # Valley of Death → Dragmire (Quest 2 only). Matches GML
    set_rule(
        world.get_entrance("Valley of Death → Dragmire"),
        lambda state: _is_quest2
        and _has(state, ITEM_CROSS)
        and _has(state, ITEM_BOOTS)
        and _has(state, ITEM_RAFT),
    )

    # Requirements shared by every check in a palace's content.
    DUNGEON_BASE_RULES = {
        # Parapa's "dark room" is the Parapa Shore CAVE you cross
        REGION_PARAPA_PALACE: None,
        REGION_MIDORO_PALACE: None,  # GML: just Rando_can_reach_MidoroField()
        # Every Island Palace check passes the fast-falling block room.
        REGION_ISLAND_PALACE: lambda state: _has(state, ITEM_GLOVE),
        REGION_MAZE_PALACE: None,  # REFLECT only needed for the boss/item, not
        # Palace on the Sea: BOOTS (ocean walk to the tile) is a
        REGION_PALACE_ON_THE_SEA: None,
        # Three Eye's FLUTE (reveals the hidden palace on the overworld)
        REGION_THREE_EYE_PALACE: None,
        REGION_GREAT_PALACE: None,  # handled below with crystal count
    }

    # Cap at 6 (only 6 palace crystals exist; the Great Palace
    required_crystals = min(world.options.crystals_required_count.value, 6)
    palace_crystals = CRYSTAL_ITEMS

    def _has_crystals(state: CollectionState) -> bool:
        return sum(state.has(c, player) for c in palace_crystals) >= required_crystals

    for dungeon_region, parent_region in world.dungeon_to_parent.items():
        base_rule = DUNGEON_BASE_RULES[dungeon_region]
        ent_name = f"{parent_region} → {dungeon_region}"
        if dungeon_region == REGION_GREAT_PALACE:
            # Great Palace CONTENT: the crystal goal follows the

            if required_crystals > 0:
                set_rule(world.get_entrance(ent_name), _has_crystals)
        elif base_rule is not None:
            set_rule(world.get_entrance(ent_name), base_rule)

    # Overworld-access requirements
    position_access_rules = {
        REGION_PARAPA_PALACE: lambda state: _dark_room_ok(state, 1),
        # Island tile: FAIRY+JUMP to cross the large body of water
        REGION_ISLAND_PALACE: lambda state: _has(state, SPELL_FAIRY)
        and _has(state, SPELL_JUMP)
        and _dark_room_ok(state, 1),
        # Maze Island tile: STABDOWN to cross the Darunia Field room
        REGION_MAZE_PALACE: lambda state: _has(state, SKILL_STAB_DOWN),
        REGION_PALACE_ON_THE_SEA: lambda state: _has(state, ITEM_BOOTS),
        REGION_THREE_EYE_PALACE: lambda state: _has(state, ITEM_FLUTE),
        REGION_GREAT_PALACE: lambda state: (
            _has(state, ITEM_CROSS)
            and _any(state, SPELL_JUMP, SPELL_FAIRY)
            and _dark_room_ok(state, 2)
            and state.can_reach_region(REGION_KASUTO_AREA, player)
        ),
    }

    # dungeon_position is content -> tile; invert to tile -> content.
    position_to_content = {
        tile: content for content, tile in world.dungeon_position.items()
    }
    for position_region, access_rule in position_access_rules.items():
        content_region = position_to_content.get(position_region, position_region)
        parent_region = world.dungeon_to_parent[content_region]
        add_rule(world.get_entrance(f"{parent_region} → {content_region}"), access_rule)

    # "GP PBag: Next to fast travel" is the Great Palace's requirement-less loc
    _gp_tile = world.dungeon_position[REGION_GREAT_PALACE]
    _gp_tile_access = position_access_rules.get(_gp_tile)
    _gp_needs_jump = _gp_tile == REGION_ISLAND_PALACE
    if _gp_tile_access is not None or _gp_needs_jump:
        try:
            _gp_outside_loc = multiworld.get_location(GP_OUTSIDE_LOCATION, player)
        except KeyError:
            _gp_outside_loc = None
        if _gp_outside_loc is not None:
            set_rule(
                _gp_outside_loc,
                lambda state, ta=_gp_tile_access, nj=_gp_needs_jump: (
                    (ta is None or ta(state)) and (not nj or _has(state, SPELL_JUMP))
                ),
            )

    # Per-loc key requirements within each palace
    if world.options.randomize_key_locations.value:
        for region in multiworld.get_regions(player):
            for loc in region.locations:
                req = LOCATION_KEY_REQS.get(loc.name)
                if req:
                    key_name, threshold = req
                    loc.access_rule = lambda state, kn=key_name, th=threshold: (
                        _has_key_count(state, kn, th)
                    )

    # Dragmire Tower (Palc_H) — the Quest-2 Ganon fight
    set_rule(
        world.get_entrance("Kasuto Area → Dragmire Tower"),
        lambda state: _is_quest2
        and _has(state, ITEM_CROSS)
        and _has(state, ITEM_BOOTS)
        and _has(state, ITEM_RAFT)
        and _has(state, ITEM_BRACELET)
        and _has(state, ITEM_MASK)
        and _has(state, SPELL_JUMP)
        and _has(state, SKILL_STAB_DOWN)
        and _dark_room_ok(state, 2),
    )

    # Bulblin town — GML STR_Bulblin qual
    for entrance in multiworld.get_region(REGION_BULBLIN, player).entrances:
        add_rule(
            entrance,
            lambda state: (
                _is_quest2
                and _has(state, ITEM_CROSS)
                and _has(state, ITEM_BOOTS)
                and _has(state, ITEM_RAFT)
                and _has(state, ITEM_BRACELET)
                and _has(state, SPELL_JUMP)
                and _dark_room_ok(state, 2)
            ),
        )

    # Obscurity — soft-deprioritize obscure locs if option is set
    if world.options.limit_obscure_locations.value:
        # obscurity tier -> chance the loc is excluded
        OBSCURITY_EXCLUDE_CHANCE = {2: 0.70, 3: 0.90}
        for region in multiworld.get_regions(player):
            for loc in region.locations:
                if loc.address is None:
                    continue
                loc_data = Locations.location_dict.get(loc.name)
                if loc_data is None:
                    continue
                chance = OBSCURITY_EXCLUDE_CHANCE.get(loc_data.obscurity)
                if chance is not None and world.random.random() < chance:
                    loc.progress_type = LocationProgressType.EXCLUDED

    # Town entrances — per-town access rules

    # Mido position access
    set_rule(
        world.get_entrance("Midoro Field → Mido"),
        lambda state: _has(state, ITEM_HAMMER),
    )
    set_rule(
        world.get_entrance("Z1 Area → Mido via Fire Cave"),
        lambda state: _has(state, SPELL_FIRE),
    )

    # Mido → Midoro Field (Mido boulder, exit side) — HAMMER

    set_rule(
        world.get_entrance("Mido → Midoro Field"),
        lambda state: _has(state, ITEM_HAMMER),
    )

    # New Kasuto POSITION terrain — GML case STR_New_Kasuto:
    for entrance in multiworld.get_region(REGION_NEW_KASUTO, player).entrances:
        add_rule(
            entrance,
            lambda state: (
                _has(state, ITEM_HAMMER)
                and (
                    (_has(state, ITEM_BOOTS) and _has(state, ITEM_BRACELET))
                    or (_has(state, ITEM_FLUTE) and _dark_room_ok(state, 2))
                )
            ),
        )

    # CROSS — the position hosting Old Kasuto needs CROSS
    _old_kasuto_position = world.town_position["Old Kasuto"]
    _old_kasuto_region = TOWN_TO_REGION[_old_kasuto_position]
    for entrance in multiworld.get_region(_old_kasuto_region, player).entrances:
        add_rule(entrance, lambda state: _has(state, ITEM_CROSS))

    # Town interior — per-loc quest gates.

    # Ruto: guard needs TROPHY from Parapa Palace boss
    for loc_name in ("JUMP spell room", "_Spell_Location_Ruto"):
        loc = multiworld.get_location(loc_name, player)
        if loc:
            loc.access_rule = lambda state, _trophy=ITEM_TROPHY: _has(state, _trophy)

    # Saria: wise man needs MIRROR to access
    loc = multiworld.get_location("_Spell_Location_Saria", player)
    if loc:
        loc.access_rule = lambda state: _has(state, ITEM_MIRROR)

    # Mido: give FLOWER to the girl
    for loc_name in ("PBag: FAIRY spell room", "_Spell_Location_Mido"):
        loc = multiworld.get_location(loc_name, player)
        if loc:
            loc.access_rule = lambda state, _flower=ITEM_FLOWER: _has(state, _flower)

    # Nabooru's well stays on the vanilla Nabooru tile when the town moves.
    def _can_finish_nabooru_well(state):
        return state.can_reach_region(REGION_NABOORU, player) and _all(
            state, ITEM_GLOVE, SKILL_STAB_DOWN, SPELL_JUMP
        )

    loc = multiworld.get_location("_Spell_Location_Nabooru", player)
    if loc:
        loc.access_rule = _can_finish_nabooru_well

    loc = multiworld.get_location("PBag: FIRE spell room", player)
    if loc:
        loc.access_rule = lambda state: _can_finish_nabooru_well(state) and _has(
            state, SPELL_FIRE
        )

    # Darunia: rescue the CHILD → wise man teaches Reflect
    loc = multiworld.get_location("_Spell_Location_Darunia", player)
    if loc:
        loc.access_rule = lambda state, _child=ITEM_CHILD: _has(state, _child)

    # Per-loc overworld rules

    def _gloc(name: str):
        """Safe get_location that returns None if missing. Resolves the pre-rename
        location literals used throughout this file to their palace-prefixed
        display names (see Locations.LOCATION_NAME_ALIASES)."""
        name = Locations.LOCATION_NAME_ALIASES.get(name, name)
        try:
            return multiworld.get_location(name, player)
        except KeyError:
            return None

    def _all(state: CollectionState, *items: str) -> bool:
        return all(state.has(item, player) for item in items)

    # --- Tantari Cave (TROPHY) -- dark room needs light ---
    loc = _gloc("TROPHY location")
    if loc:
        loc.access_rule = lambda state: _any(state, ITEM_CANDLE, SPELL_FIRE)

    # --- North Castle Cave Container Piece -- dark room 1 ---
    loc = _gloc("North Castle Cave Container Piece location")
    if loc:
        loc.access_rule = lambda state: _dark_room_ok(state, 1)

    # --- Parapa Shore Container Piece -- dark room 1 ---
    loc = _gloc("Parapa Shore Container Piece location")
    if loc:
        loc.access_rule = lambda state: _dark_room_ok(state, 1)

    # --- South Parapa Container Piece -- dark room 1
    loc = _gloc("South Parapa Container Piece location")
    if loc:
        loc.access_rule = lambda state: _dark_room_ok(state, 1)

    # --- Midoro Field Cave Container Piece -- HAMMER + dark
    loc = _gloc("Midoro Field Cave Container Piece location")
    if loc:
        loc.access_rule = lambda state: _has(state, ITEM_HAMMER) and _dark_room_ok(
            state, 1
        )

    # --- PBag: Cave N of Midoro Swamp -- dark room
    loc = _gloc("PBag: Cave N of Midoro Swamp")
    if loc:
        loc.access_rule = lambda state: _dark_room_ok(state, 1)

    # --- FLOWER loc -- MorugeSwamp + HAMMER + dark >= + jump/fairy
    loc = _gloc("FLOWER location")
    if loc:
        loc.access_rule = lambda state: (
            _has(state, ITEM_HAMMER)
            and _dark_room_ok(state, 2)
            and _any(state, SPELL_JUMP, SPELL_FAIRY)
        )

    # --- HAMMER loc -- Death Mtn dark room
    loc = _gloc("HAMMER location")
    if loc:
        loc.access_rule = lambda state: _dark_room_ok(state, 2)

    # --- Death Mtn Shoals Container Piece -- BOOTS ---
    loc = _gloc("Death Mtn Shoals Container Piece location")
    if loc:
        loc.access_rule = lambda state: _has(state, ITEM_BOOTS)

    # --- Death Mtn Hole Container Piece -- HAMMER ---
    loc = _gloc("Death Mtn Hole Container Piece location")
    if loc:
        loc.access_rule = lambda state: _has(state, ITEM_HAMMER)

    # --- Death Mtn Maze Container Piece (HEART) -- dark >= 2
    loc = _gloc("Death Mtn Maze Container Piece location (HEART)")
    if loc:
        loc.access_rule = lambda state: _dark_room_ok(state, 2)

    # --- Death Mtn Maze Container Piece (MAGIC) -- dark >= 2
    loc = _gloc("Death Mtn Maze Container Piece location (MAGIC)")
    if loc:
        loc.access_rule = lambda state: _dark_room_ok(state, 2)

    # --- Death Mtn 1up -- dark >= 2 (light only, no JUMP/FAIRY in hard logic)
    # has a precise jump
    loc = _gloc("Death Mtn 1up location")
    if loc:
        loc.access_rule = lambda state: _dark_room_ok(state, 2) and (
            _any(state, SPELL_JUMP, SPELL_FAIRY) or _hard_logic
        )

    # --- MEAT loc -- Saria2 + FIRE + JUMP ---
    loc = _gloc("MEAT location")
    if loc:
        loc.access_rule = lambda state: _has(state, SPELL_FIRE) and _has(
            state, SPELL_JUMP
        )

    # --- Under Kings Tomb (SHIELD) -- RoyalCemetery region + spell sequence
    loc = _gloc("Under Kings Tomb location (SHIELD)")
    if loc:
        _seq01 = tuple(world.spell_sequences["01"])
        loc.access_rule = lambda state, _s=_seq01: (
            _has(state, ITEM_BOOK) and all(state.has(sp, player) for sp in _s)
        )

    # --- Boulder Circle Reward (RING)
    # The puzzle needs dialogue from seven of the eight Quest-1 wise men.
    loc = _gloc("Boulder Circle Reward location (RING)")
    if loc:
        _BOULDER_WISEMAN_LOCS = tuple(
            f"_Spell_Location_{town.replace(' ', '_')}"
            for town in (
                "Rauru",
                "Ruto",
                "Saria",
                "Mido",
                "Nabooru",
                "Darunia",
                "New Kasuto",
                "Old Kasuto",
            )
        )

        def _boulder_circle_rule(state: CollectionState) -> bool:
            if not _has(state, ITEM_HAMMER):
                return False
            return (
                sum(
                    multiworld.get_location(name, player).can_reach(state)
                    for name in _BOULDER_WISEMAN_LOCS
                )
                >= 7
            )

        loc.access_rule = _boulder_circle_rule

    # Whale Isl (BOOK) -- complex quest
    loc = _gloc("Whale Isl Item location (BOOK)")
    if loc:
        # GML also gates on reaching Rauru (Anju's house is part of the chain)
        loc.access_rule = lambda state: (
            _has(state, ITEM_RAFT)
            and _has(state, ITEM_BOOTS)
            and _has(state, ITEM_HAMMER)
            and _any(state, SPELL_JUMP, SPELL_FAIRY)
            and state.can_reach_region(REGION_RAURU, player)
        )

    # Carock 2 (PENDANT) -- DaruniaField + BOOTS + BOOK + sequence + Reflect
    loc = _gloc("Carock 2 location (PENDANT)")
    if loc:
        _seq02 = tuple(world.spell_sequences["02"])
        loc.access_rule = lambda state, _s=_seq02: (
            _has(state, ITEM_BOOTS)
            and _has(state, ITEM_BOOK)
            and _has(state, SPELL_REFLECT)
            and all(state.has(sp, player) for sp in _s)
        )

    # CHILD loc -- MazeIsl + dark room >=1
    loc = _gloc("CHILD location")
    if loc:
        loc.access_rule = lambda state: _dark_room_ok(state, 1)

    # Shoals above P4 (1-Up Doll) -- MazeIsl + BOOTS
    loc = _gloc("Shoals above P4")
    if loc:
        loc.access_rule = lambda state: _has(state, ITEM_BOOTS)

    # East continent locs requiring BOOTS
    for name in (
        "P5 Sea Container Piece location",
        "Pendant Isl Container Piece location",
        "Nabooru Bay Cave Container Piece location",
        "River Devil Lake Container Piece location",
        "VOD Container Piece location",
    ):
        loc = _gloc(name)
        if loc:
            loc.access_rule = lambda state, _n=name: _has(state, ITEM_BOOTS)

    # --- Kasuto-Lake shoals -- BOOTS ---
    loc = _gloc("Kasuto-Lake shoals")
    if loc:
        loc.access_rule = lambda state: _has(state, ITEM_BOOTS)

    # BOOTS-requiring PBags
    for name in (
        "PBag: Island between Death Mtn and Royal Cemetery",
        "PBag: Sea Cave N end of Ruto Mtns",
    ):
        loc = _gloc(name)
        if loc:
            loc.access_rule = lambda state, _n=name: _has(state, ITEM_BOOTS)

    # Dark-room PBags
    for name, thresh in (
        ("PBag: Cave N of Midoro Swamp", 1),
        ("PBag: Cave S of Nabooru", 2),
        ("PBag: Kasuto Swamp cave", 2),
    ):
        loc = _gloc(name)
        if loc:
            loc.access_rule = lambda state, _t=thresh: _dark_room_ok(state, _t)

    # PBag: West Saria River Waterfall + Forest above Saria
    for name in ("PBag: West Saria River Waterfall", "PBag: Forest above Saria Lake"):
        loc = _gloc(name)
        if loc:
            loc.access_rule = lambda state, _n=name: (
                _has(state, SPELL_FIRE) and _has(state, SPELL_JUMP)
            )

    # PBag: Secret desert tile S of P5 -- HAMMER/BOOTS + JUMP
    loc = _gloc("PBag: Secret desert tile S of P5")
    if loc:
        loc.access_rule = lambda state: (
            _any(state, ITEM_HAMMER, ITEM_BOOTS) and _has(state, SPELL_JUMP)
        )

    # PBag: Secret tile in VOD -- CROSS + JUMP/RESCUE_FAIRY
    loc = _gloc("PBag: Secret tile in VOD")
    if loc:
        loc.access_rule = lambda state: (
            _has(state, ITEM_CROSS) and _any(state, SPELL_JUMP, ITEM_RESCUE_FAIRY)
        )

    # Nabooru Chimney PBag -- JUMP
    loc = _gloc("PBag: Nabooru Chimney PBag location")
    if loc:
        loc.access_rule = lambda state: _has(state, SPELL_JUMP)

    # PBag: Cave ruins under North Castle Lake -- STABDOWN + GLOVE + JUMP
    loc = _gloc("PBag: Cave ruins under North Castle Lake")
    if loc:
        loc.access_rule = lambda state: (
            _all(state, SKILL_STAB_DOWN, ITEM_GLOVE, SPELL_JUMP)
        )

    # PBag: Upper North Castle Hallway + PBag: North Castle
    for name in (
        "PBag: Upper North Castle Hallway",
        "PBag: North Castle vertical climb challenge",
        "PBag: Secret tile above North Castle",
    ):
        loc = _gloc(name)
        if loc:
            loc.access_rule = lambda state, _n=name: _has(state, SPELL_JUMP)

    # Ruto Mtn Ruins locs
    for name in ("RescueFairy Location", "PBag: N Ruto Mtn Ruins Plaforming Challenge"):
        loc = _gloc(name)
        if loc:
            loc.access_rule = lambda state, _n=name: _any(
                state, ITEM_CANDLE, SPELL_FIRE
            )

    # PBag: Nabooru quest cave system -- well access
    loc = _gloc("PBag: Nabooru quest cave system 1 (right of well bottom)")
    if loc:
        loc.access_rule = lambda state: _all(state, ITEM_GLOVE, SKILL_STAB_DOWN)

    loc = _gloc("PBag: Nabooru quest cave system 2 (above last big vertical drop)")
    if loc:
        loc.access_rule = lambda state: (
            _all(state, ITEM_GLOVE, SKILL_STAB_DOWN, SPELL_JUMP)
            and _any(state, SPELL_JUMP, ITEM_RESCUE_FAIRY)
        )

    # BRACELET loc -- needs ENIGMA to see hidden room
    loc = _gloc("BRACELET location")
    if loc:
        loc.access_rule = lambda state: _has(state, SPELL_ENIGMA)

    loc = _gloc("PBag: BRACELET room")
    if loc:
        loc.access_rule = lambda state: _all(state, SPELL_ENIGMA, ITEM_BRACELET)

    # Skill locs — region-gated to town; extra item rule here
    loc = _gloc("_Skill_Location_Mido")
    if loc:
        loc.access_rule = lambda state: (
            _any(state, SPELL_JUMP, SPELL_FAIRY)
            and (not _is_quest2 or _has(state, ITEM_GLOVE))
        )

    loc = _gloc("_Skill_Location_Darunia")
    if loc:
        loc.access_rule = lambda state: _any(state, SPELL_JUMP, SKILL_STAB_DOWN)

    # Near-shore raft islands -- RAFT only
    for name in (
        "PBag: Island N of Tantari Desert",
        "North Isl Container Piece location",
    ):
        loc = _gloc(name)
        if loc:
            loc.access_rule = lambda state, _n=name: _has(state, ITEM_RAFT)

    # PBag: Sea cave N of Darunia -- DaruniaField + BOOTS
    loc = _gloc("PBag: Sea cave N of Darunia")
    if loc:
        loc.access_rule = lambda state: _has(state, ITEM_BOOTS)

    # Spell room items (in-town pickups)
    loc = _gloc("JUMP spell room")
    if loc:
        loc.access_rule = lambda state: _has(state, ITEM_TROPHY) and _has(
            state, SPELL_JUMP
        )

    loc = _gloc("PBag: FAIRY spell room")
    if loc:
        loc.access_rule = lambda state: _has(state, ITEM_FLOWER) and _has(
            state, SPELL_FAIRY
        )

    loc = _gloc("PBag: FIRE spell room")
    if loc:
        loc.access_rule = lambda state: _all(
            state, ITEM_GLOVE, SKILL_STAB_DOWN, SPELL_JUMP
        ) and _has(state, SPELL_FIRE)

    # Mido Fairy Container Piece -- NPC gives reward on rescue fairy return
    loc = _gloc("Mido Fairy Container Piece location")
    if loc:
        loc.access_rule = lambda state: _has(state, ITEM_RESCUE_FAIRY)

    # Darunia Minigame Reward -- STABDOWN
    loc = _gloc("Darunia Minigame Reward location")
    if loc:
        loc.access_rule = lambda state: _has(state, SKILL_STAB_DOWN)

    # New Kasuto town interiors carry NO content-side terrain

    # Old Kasuto magic piece -- CROSS
    loc = _gloc("Old Kasuto magic piece location")
    if loc:
        loc.access_rule = lambda state: _has(state, ITEM_CROSS)

    # Kakusu Reward Area (SWORD + PBag) -- X-task gating
    def _reach(state: CollectionState, region: str) -> bool:
        return state.can_reach_region(region, player)

    # Each KAKUSU check pulled out into its own named loc
    def _kakusu_01(state: CollectionState) -> bool:
        # KAKUSU01: North Castle. JUMP
        return state.has(SPELL_JUMP, player)

    def _kakusu_02(state: CollectionState) -> bool:
        # KAKUSU02: Parapa Palace. (CANDLE || FIRE) -- to light torches
        return _reach(state, REGION_PARAPA_PALACE) and _any(
            state, ITEM_CANDLE, SPELL_FIRE
        )

    def _kakusu_03(state: CollectionState) -> bool:
        # KAKUSU03: DthMt HAMMER caves (physical Kakusu001).
        return _reach(state, REGION_DEATH_MTN)

    def _kakusu_04(state: CollectionState) -> bool:
        # KAKUSU04: DthMt bridge. Royal Cemetery + (JUMP || FAIRY)
        return _reach(state, REGION_ROYAL_CEMETERY) and _any(
            state, SPELL_JUMP, SPELL_FAIRY
        )

    def _kakusu_05(state: CollectionState) -> bool:
        # KAKUSU05: Ruto Mtns. Stab down from top.
        return _reach(state, REGION_RUTO_MTN_RUINS) and state.has(
            SKILL_STAB_DOWN, player
        )

    def _kakusu_06(state: CollectionState) -> bool:
        # KAKUSU06: P3 (Island Palace). GLOVE + STABDOWN to kill
        four_island = _has_key_count(state, KEY_ISLAND, 4)
        return (
            _reach(state, REGION_ISLAND_PALACE)
            and four_island
            and state.has(ITEM_GLOVE, player)
            and state.has(SKILL_STAB_DOWN, player)
        )

    def _kakusu_07(state: CollectionState) -> bool:
        # KAKUSU07: Darunia. STABDOWN + GLOVE + JUMP + (STABUP or hard logic)
        return (
            _reach(state, REGION_DARUNIA)
            and state.has(SKILL_STAB_DOWN, player)
            and (_hard_logic or state.has(SKILL_STAB_UP, player))
            and state.has(ITEM_GLOVE, player)
            and state.has(SPELL_JUMP, player)
        )

    def _kakusu_08(state: CollectionState) -> bool:
        # KAKUSU08: Darunia Forest
        return _reach(state, REGION_DARUNIA_FIELD)

    def _kakusu_09(state: CollectionState) -> bool:
        # KAKUSU09: Maze Isl.
        return _reach(state, REGION_MAZE_ISL) and state.has(SPELL_FAIRY, player)

    def _kakusu_10(state: CollectionState) -> bool:
        # KAKUSU10: P6 (Three Eye Rock Palace, already needs FLUTE)
        six_eye = _has_key_count(state, KEY_THREE_EYE, 6)
        return (
            _reach(state, REGION_THREE_EYE_PALACE)
            and six_eye
            and state.has(SPELL_FAIRY, player)
            and state.has(SPELL_JUMP, player)
            and state.has(SKILL_STAB_DOWN, player)
            and state.has(ITEM_GLOVE, player)
        )

    _seq03 = tuple(world.spell_sequences["03"])

    def _kakusu_11(state: CollectionState) -> bool:
        # KAKUSU11: Kasuto Cemetery. CROSS + BOOK + sequence
        return (
            _reach(state, REGION_KASUTO_AREA)
            and state.has(ITEM_CROSS, player)
            and state.has(ITEM_BOOK, player)
            and all(state.has(sp, player) for sp in _seq03)
        )

    def _kakusu_12(state: CollectionState) -> bool:
        # KAKUSU12: THUNDER Kakusu. North Islands
        return _reach(state, REGION_NORTH_ISLANDS) and state.has(SPELL_THUNDER, player)

    _KAKUSU_CHECKS = (
        _kakusu_01,
        _kakusu_02,
        _kakusu_03,
        _kakusu_04,
        _kakusu_05,
        _kakusu_06,
        _kakusu_07,
        _kakusu_08,
        _kakusu_09,
        _kakusu_10,
        _kakusu_11,
        _kakusu_12,
    )

    def _kakusu_count(state: CollectionState) -> int:
        return sum(1 for check in _KAKUSU_CHECKS if check(state))

    def _kakusu_ok(state: CollectionState) -> bool:
        required = min(world.options.kakusu_required_count.value, 12)
        return (
            _all(state, ITEM_GLOVE, SKILL_STAB_DOWN)
            and _kakusu_count(state) >= required
        )

    set_rule(world.get_entrance("East → South Continent"), _kakusu_ok)

    # Individually-exposed Kakusu locs
    for i in world.kakusu_selected_indices:
        loc = _gloc(KAKUSU_LOCATION_NAMES[i - 1])
        if loc:
            loc.access_rule = _KAKUSU_CHECKS[i - 1]

    # Palace interior per-loc item requirements
    def _add_loc_rule(loc, extra_fn):
        """AND an extra access function onto an existing location rule."""
        if loc is None:
            return
        base = loc.access_rule

        def _combined(state, _b=base, _e=extra_fn):
            ok = _b(state) if _b else True
            return ok and _e(state)

        loc.access_rule = _combined

    # Quest-2 Dragmire / MASK / Bulblin field locs
    _add_loc_rule(
        _gloc("PBag: Raft ride in the sea"), lambda state: _has(state, SPELL_JUMP)
    )
    _add_loc_rule(
        _gloc("PBag: Dragmire shoals location"), lambda state: _has(state, SPELL_JUMP)
    )

    # MASK loc + its two room PBags:
    def _mask_rule(state):
        return _all(
            state, ITEM_HAMMER, ITEM_BRACELET, ITEM_GLOVE, SPELL_JUMP
        ) and _dark_room_ok(state, 2)

    _add_loc_rule(_gloc("MASK location"), _mask_rule)
    _add_loc_rule(_gloc("PBag: MASK room, bag 1"), _mask_rule)
    _add_loc_rule(_gloc("PBag: MASK room, bag 2"), _mask_rule)

    # Bulblin wise-man (Summon):
    _add_loc_rule(
        _gloc("_Spell_Location_Bulblin"), lambda state: _has(state, ITEM_MASK)
    )

    # Key-gated PBag locs inside palaces
    _keys = world.options.randomize_key_locations.value

    # Crystal locs — gated on actually clearing the palace
    def _crystal_keys(state: CollectionState, key_name: str, n: int) -> bool:
        if not _keys:
            return True
        return _has_key_count(state, key_name, n)

    # Per-palace "cleared the palace" rule (reach the crystal)
    _palace_clear_rules = {
        # Parapa (1): hardest dark room + 3 keys
        REGION_PARAPA_PALACE: lambda state: (
            _dark_room_ok(state, 2) and _crystal_keys(state, KEY_PARAPA, 3)
        ),
        # Midoro (2): GLOVE + hardest dark room + 4 keys
        REGION_MIDORO_PALACE: lambda state: (
            _has(state, ITEM_GLOVE)
            and _dark_room_ok(state, 2)
            and _crystal_keys(state, KEY_MIDORO, 4)
        ),
        # Island (3): GLOVE + STABDOWN (defeat Rebonack) + 4 keys
        REGION_ISLAND_PALACE: lambda state: (
            _has(state, ITEM_GLOVE)
            and _has(state, SKILL_STAB_DOWN)
            and _crystal_keys(state, KEY_ISLAND, 4)
        ),
        # Maze Island (4): 6 keys + REFLECT (defeat Carock)
        REGION_MAZE_PALACE: lambda state: (
            _crystal_keys(state, KEY_MAZE, 6) and _has(state, SPELL_REFLECT)
        ),
        # Palace on the Sea (5): FAIRY + 5 keys
        REGION_PALACE_ON_THE_SEA: lambda state: (
            _has(state, SPELL_FAIRY) and _crystal_keys(state, KEY_SEA, 5)
        ),
        # Three Eye Rock (6): GLOVE + JUMP + STABDOWN + fairy + 6 keys
        REGION_THREE_EYE_PALACE: lambda state: (
            _has(state, ITEM_GLOVE)
            and _has(state, SPELL_JUMP)
            and _has(state, SKILL_STAB_DOWN)
            and _has(state, SPELL_FAIRY)
            and _crystal_keys(state, KEY_THREE_EYE, 6)
        ),
    }

    # Apply to each palace's crystal loc
    for _region, _clear_rule in _palace_clear_rules.items():
        crystal_loc = _gloc(PALACE_CRYSTAL[_region][1])
        if crystal_loc:
            crystal_loc.access_rule = _clear_rule
        boss_item_loc = _gloc(PALACE_BOSS_ITEM[_region])
        if boss_item_loc:
            boss_item_loc.access_rule = _clear_rule

    # --- Palace 1 (Parapa) ---

    _add_loc_rule(_gloc("P1 Key 3"), lambda state: _any(state, SPELL_FAIRY, ITEM_GLOVE))
    # Key 2 (room $02): dark room + 1 key
    _add_loc_rule(_gloc("P1 Key 2"), lambda state: _dark_room_ok(state, 1))
    _add_loc_rule(
        _gloc("PBag: P1 crumbling bridge"),
        lambda state: _dark_room_ok(state, 1),
    )
    _add_loc_rule(_gloc("PBag: P2 entrance"), lambda state: _has(state, SPELL_JUMP))

    # --- Palace 2 (Midoro) ---

    _add_loc_rule(_gloc("P2 Key 3"), lambda state: _has(state, ITEM_GLOVE))
    # Key 4 (room $10): dark room
    _add_loc_rule(_gloc("P2 Key 4"), lambda state: _dark_room_ok(state, 2))
    # Container Piece (room $15): GLOVE + 1 key
    _add_loc_rule(
        _gloc("P2 Container Piece location"), lambda state: _has(state, ITEM_GLOVE)
    )
    # 1-Up (room $16): GLOVE
    _add_loc_rule(_gloc("P2 1up location"), lambda state: _has(state, ITEM_GLOVE))
    _add_loc_rule(_gloc("PBag: P2 falling-block room"), lambda state: _has(state, ITEM_GLOVE))
    _add_loc_rule(_gloc("PBag: P2 Iron Knuckle room"), lambda state: _has(state, ITEM_GLOVE))

    # --- Palace 3 (Island) ---

    _add_loc_rule(
        _gloc("P3 Key 1"), lambda state: _all(state, SKILL_STAB_DOWN, ITEM_GLOVE)
    )
    # Key 2 ($06): GLOVE only
    _add_loc_rule(_gloc("P3 Key 2"), lambda state: _has(state, ITEM_GLOVE))
    # Key 3 ($07): GLOVE + 3 keys
    _add_loc_rule(_gloc("P3 Key 3"), lambda state: _has(state, ITEM_GLOVE))
    # Key 4 ($0A): GLOVE + 3 keys
    _add_loc_rule(_gloc("P3 Key 4"), lambda state: _has(state, ITEM_GLOVE))
    # Item ($12): GLOVE + 4 keys
    _add_loc_rule(_gloc("P3 Item location"), lambda state: _has(state, ITEM_GLOVE))
    # Container Piece ($13): GLOVE + FAIRY + 4 keys
    _add_loc_rule(
        _gloc("P3 Container Piece location"),
        lambda state: _has(state, ITEM_GLOVE) and _has(state, SPELL_FAIRY),
    )
    if _keys:
        _add_loc_rule(
            _gloc("PBag: Mau Spawner room"),
            lambda state: _has(state, ITEM_GLOVE)
            and _has_key_count(state, KEY_ISLAND, 3),
        )
        _add_loc_rule(
            _gloc("PBag: On blocks on top of pillar"),
            lambda state: _has(state, ITEM_GLOVE)
            and _has_key_count(state, KEY_ISLAND, 4)
            and _has(state, SPELL_JUMP),
        )
        _add_loc_rule(
            _gloc("PBag: Room left of Rebonack"),
            lambda state: _has(state, ITEM_GLOVE)
            and _has_key_count(state, KEY_ISLAND, 4),
        )
    # P3 "PBag: Locked by upthrust" (GML Area_PalcC+'08')

    _add_loc_rule(
        _gloc("PBag: Locked by upthrust"),
        lambda state: _all(state, ITEM_GLOVE, SPELL_JUMP)
        and (_hard_logic or state.has(SKILL_STAB_UP, player)),
    )
    _add_loc_rule(
        _gloc("PBag: P3 under blocks next to key"),
        lambda state: _all(state, SKILL_STAB_DOWN, ITEM_GLOVE),
    )

    # --- Palace 4 (Maze Island) ---

    _add_loc_rule(_gloc("P4 Key 1"), lambda state: _has(state, ITEM_GLOVE))
    # Key 2 ($02): JUMP + GLOVE + (STABUP or hard logic)

    _add_loc_rule(
        _gloc("P4 Key 2"),
        lambda state: _all(state, SPELL_JUMP, ITEM_GLOVE)
        and (_hard_logic or state.has(SKILL_STAB_UP, player)),
    )
    # Key 4 ($0A) and Key 6 ($14): reached by crossing fire

    _add_loc_rule(
        _gloc("P4 Key 4"),
        lambda state: _hard_logic or _any(state, SPELL_JUMP, ITEM_GLOVE),
    )
    # Key 5 ($11): GLOVE, no key threshold
    _add_loc_rule(_gloc("P4 Key 5"), lambda state: _has(state, ITEM_GLOVE))
    _add_loc_rule(
        _gloc("P4 Key 6"),
        lambda state: _hard_logic or _any(state, SPELL_JUMP, ITEM_GLOVE),
    )
    # Container Piece ($09): FAIRY only
    _add_loc_rule(
        _gloc("P4 Container Piece location"), lambda state: _has(state, SPELL_FAIRY)
    )
    # P4 Item (BOOTS, room $10): GML Area_PalcD+'10'

    _add_loc_rule(
        _gloc("PBag: 2 Doomknockers and a key"),
        lambda state: _has(state, ITEM_GLOVE) and _has_key_count(state, KEY_MAZE, 4),
    )
    _add_loc_rule(
        _gloc("PBag: Room with blocks on top of pillars"),
        lambda state: _has(state, SPELL_JUMP) and _has_key_count(state, KEY_MAZE, 6),
    )

    # --- Palace 5 (Palace on the Sea) ---

    _add_loc_rule(_gloc("P5 Key 2"), lambda state: _any(state, SPELL_JUMP, ITEM_GLOVE))
    # Key 3 ($0F): FAIRY + 1 key + JUMP (threshold in
    _add_loc_rule(_gloc("P5 Key 3"), lambda state: _has(state, SPELL_JUMP))
    # Key 4 ($13): FAIRY + 1 key + JUMP (threshold in
    _add_loc_rule(_gloc("P5 Key 4"), lambda state: _has(state, SPELL_JUMP))
    _add_loc_rule(_gloc("PBag: P5 Entrance"), lambda state: _has(state, SPELL_JUMP))
    if _keys:
        _add_loc_rule(
            _gloc("PBag: JUMP locked above elevator"),
            lambda state: _has(state, SPELL_JUMP) and _has_key_count(state, KEY_SEA, 1),
        )
        # GML Area_PalcE+'0B' (GLOVE 1): 4 keys

        _add_loc_rule(
            _gloc("PBag: Locked by upthrust and GLOVE 1"),
            lambda state: _all(state, ITEM_GLOVE, SKILL_STAB_DOWN, SPELL_JUMP)
            and (_hard_logic or state.has(SKILL_STAB_UP, player))
            and _has_key_count(state, KEY_SEA, 4),
        )
        _add_loc_rule(
            _gloc("PBag: Locked by upthrust and GLOVE 2"),
            lambda state: _all(state, ITEM_GLOVE, SKILL_STAB_DOWN, SPELL_JUMP)
            and (_hard_logic or state.has(SKILL_STAB_UP, player))
            and _has_key_count(state, KEY_SEA, 1),
        )
        _add_loc_rule(
            _gloc("PBag: JUMP or STABUP locked on top of blocks"),
            lambda state: _has(state, SPELL_JUMP) and _has_key_count(state, KEY_SEA, 4),
        )

    # P5 Container Piece needs FAIRY
    _add_loc_rule(
        _gloc("P5 Container Piece location"), lambda state: _has(state, SPELL_FAIRY)
    )

    # FAIRY gates every Palace-on-the-Sea loc EXCEPT entrance

    _p5_entrance_pbag = _gloc("PBag: P5 Entrance")
    for _p5_loc in multiworld.get_region(REGION_PALACE_ON_THE_SEA, player).locations:
        if _p5_loc is not _p5_entrance_pbag:
            _add_loc_rule(_p5_loc, lambda state: _has(state, SPELL_FAIRY))

    # --- Palace 6 (Three Eye Rock) ---

    _add_loc_rule(
        _gloc("P6 Container Piece location"),
        lambda state: _all(state, SPELL_FAIRY, SPELL_JUMP, ITEM_GLOVE, SKILL_STAB_DOWN),
    )
    _add_loc_rule(
        _gloc("P6 Item location"),
        lambda state: _all(state, SPELL_JUMP, ITEM_GLOVE, SKILL_STAB_DOWN),
    )
    _add_loc_rule(
        _gloc("PBag: GLOVE and STABUP locked 1"),
        lambda state: _all(state, ITEM_GLOVE, SPELL_JUMP)
        and (_hard_logic or state.has(SKILL_STAB_UP, player)),
    )
    _add_loc_rule(
        _gloc("PBag: P6 Bottom room of pit to boss"),
        lambda state: _all(state, SPELL_FAIRY, SPELL_JUMP, ITEM_GLOVE, SKILL_STAB_DOWN)
        and _has_key_count(state, KEY_THREE_EYE, 6),
    )
    _add_loc_rule(
        _gloc("PBag: Room below Kakusu room"),
        lambda state: _all(state, SPELL_FAIRY, SPELL_JUMP, ITEM_GLOVE, SKILL_STAB_DOWN)
        and _has_key_count(state, KEY_THREE_EYE, 6),
    )
    _add_loc_rule(
        _gloc("PBag: Under blocks with Mau Spawner"),
        lambda state: _all(state, SPELL_FAIRY, SPELL_JUMP, ITEM_GLOVE)
        and _has_key_count(state, KEY_THREE_EYE, 4),
    )
    _add_loc_rule(
        _gloc("PBag: GLOVE locked 2"),
        lambda state: _has(state, ITEM_GLOVE)
        and _has_key_count(state, KEY_THREE_EYE, 5),
    )
    _add_loc_rule(
        _gloc("PBag: Room with Atta"),
        (
            (lambda state: _has_key_count(state, KEY_THREE_EYE, 5))
            if _keys
            else (lambda state: _has(state, ITEM_GLOVE))
        ),
    )
    _add_loc_rule(
        _gloc("PBag: Endless pit 3"),
        (
            (lambda state: _has_key_count(state, KEY_THREE_EYE, 1))
            if _keys
            else (lambda state: True)
        ),
    )
    _add_loc_rule(
        _gloc("PBag: GLOVE locked 1"),
        lambda state: _all(state, ITEM_BRACELET, SKILL_STAB_UP, ITEM_GLOVE),
    )

    # P6 Key requirements (beyond key thresholds)
    _add_loc_rule(
        _gloc("P6 Key 1"),
        lambda state: _all(state, ITEM_BRACELET, SKILL_STAB_UP, ITEM_GLOVE),
    )

    _add_loc_rule(
        _gloc("P6 Key 3"),
        (
            (lambda state: _all(state, ITEM_BRACELET, SKILL_STAB_UP, ITEM_GLOVE))
            if not _keys
            else (lambda state: _has_key_count(state, KEY_THREE_EYE, 5))
        ),
    )
    # Key 5 (room $17): FAIRY + JUMP (cross lava) + GLOVE
    _add_loc_rule(
        _gloc("P6 Key 5"),
        lambda state: _all(state, SPELL_FAIRY, SPELL_JUMP, ITEM_GLOVE),
    )
    _add_loc_rule(
        _gloc("P6 Key 6"),
        lambda state: _all(state, SPELL_FAIRY, SPELL_JUMP, ITEM_GLOVE, SKILL_STAB_DOWN),
    )
    # These checks can only contain items that are stabbable.
    _stabbable = {
        KEY_PARAPA,
        KEY_MIDORO,
        KEY_ISLAND,
        KEY_MAZE,
        KEY_SEA,
        KEY_THREE_EYE,
        ITEM_KEY,
        FILLER_ITEM_PBAG,
    }
    for name in (
        "P6 Key 4 (falling key)",
        "PBag: P1 crumbling bridge",
        "PBag: P2 falling-block room",
        "PBag: P2 Iron Knuckle room",
        "PBag: P5 Ra room",
        "PBag: GP elevator junction",
    ):
        loc = _gloc(name)
        if loc:
            loc.item_rule = (
                lambda item: item.game != GAME_NAME or item.name in _stabbable
            )

    # "Item must have gravity" placement guards.
    def _needs_gravity(item):
        return item.player != player or item.name != ITEM_RESCUE_FAIRY

    for name in (
        "Target Minigame location",
        "PBag: Nabooru quest cave system 1 (right of well bottom)",
        "PBag: Locked by upthrust and GLOVE 1",  # P5 (PalcE_0B)
        "PBag: Locked by upthrust and GLOVE 2",  # P5 (PalcE_13)
        "PBag: JUMP or STABUP locked on top of blocks",  # P5 (PalcE_12)
        "PBag: GLOVE locked 1",  # P6 (PalcF_01_2)
        "P6 Key 1",
    ):  # P6 (PalcF_01_1)
        loc = _gloc(name)
        if loc:
            loc.item_rule = _needs_gravity

    # --- Palace 7 (Great Palace) ---
    _add_loc_rule(
        _gloc("Great Palace Item location (SKELETON KEY)"),
        lambda state: _has(state, ITEM_GLOVE),
    )
    _add_loc_rule(_gloc("PBag: GP elevator junction"), lambda state: _has(state, ITEM_GLOVE))
    _add_loc_rule(
        _gloc("Great Palace 1up location"),
        lambda state: _all(state, ITEM_KEY, ITEM_GLOVE, SKILL_STAB_DOWN),
    )
    _add_loc_rule(
        _gloc("PBag: Room with 1up doll"),
        lambda state: _all(state, ITEM_KEY, ITEM_GLOVE, SKILL_STAB_DOWN),
    )
    _add_loc_rule(
        _gloc("PBag: Dead end room right of 1st elevator"), lambda state: True
    )  # GML: just P7 access
    _add_loc_rule(
        _gloc("PBag: Room with 2 Fokkeru and a pit down under block bridge"),
        lambda state: _has(state, ITEM_GLOVE),
    )
    _add_loc_rule(
        _gloc("PBag: L7 room left side"),
        lambda state: _all(state, ITEM_KEY, ITEM_GLOVE, SKILL_STAB_DOWN),
    )
    _add_loc_rule(
        _gloc("PBag: Pit down room to Thunderbird path 2"),
        lambda state: _all(state, ITEM_KEY, ITEM_GLOVE, SKILL_STAB_DOWN),
    )
    _add_loc_rule(
        _gloc("PBag: Location right of L7 room"),
        lambda state: _all(state, ITEM_KEY, ITEM_GLOVE, SKILL_STAB_DOWN),
    )
    _add_loc_rule(
        _gloc("PBag: Room below L7 room"),
        lambda state: _all(state, ITEM_KEY, ITEM_GLOVE, SKILL_STAB_DOWN),
    )
    # "PBag: Next to fast travel" (GP room $3C)
    _add_loc_rule(
        _gloc("PBag: Dead end room below top right falling blocks room"),
        lambda state: _all(state, ITEM_KEY, ITEM_GLOVE),
    )
    # Victory condition

    if _is_quest2:
        _add_loc_rule(
            _gloc("Victory"),
            lambda state: (
                _all(
                    state,
                    ITEM_BOTTLE,
                    SPELL_SUMMON,
                    ITEM_KEY,
                    ITEM_GLOVE,
                    SKILL_STAB_DOWN,
                )
                and sum(state.has(c, player) for c in palace_crystals)
                >= required_crystals
            ),
        )

    multiworld.completion_condition[player] = lambda state: state.has(
        EVENT_VICTORY, player
    )

    # UT display: label relocated palaces / towns "<content> @ <tile>"

    _passthrough = getattr(multiworld, "re_gen_passthrough", None)
    if isinstance(_passthrough, dict) and _passthrough.get(GAME_NAME):
        from BaseClasses import Region
        from .Regions import INTERIOR_TOWN_LOCATIONS, SHUFFLED_TOWN_REGIONS

        # Palaces are pure content regions (no fixed terrain)
        for _content_region in world.dungeon_to_parent:
            _tile = world.dungeon_position.get(_content_region)
            if _tile is None or _tile == _content_region:
                continue  # sits on its own tile
            multiworld.get_region(_content_region, player).name = (
                f"{_content_region} @ {_tile}"
            )

        # Towns:
        content_at = {pos: content for content, pos in world.town_position.items()}
        for _position, _content in content_at.items():
            if _content == _position:
                continue  # town sits on its own tile
            _tile_region = multiworld.get_region(TOWN_TO_REGION[_position], player)
            _moved = [
                loc
                for loc in _tile_region.locations
                if loc.name in INTERIOR_TOWN_LOCATIONS
            ]
            if not _moved:
                continue
            _child = Region(f"{_content} @ {_position}", player, multiworld)
            for _loc in _moved:
                _tile_region.locations.remove(_loc)
                _loc.parent_region = _child
                _child.locations.append(_loc)
            multiworld.regions.append(_child)
            _edge = Entrance(
                player, f"{_tile_region.name} → {_content} interior", _tile_region
            )
            _tile_region.exits.append(_edge)
            _edge.connect(_child)
