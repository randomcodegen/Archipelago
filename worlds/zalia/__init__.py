import json
from typing import ClassVar, Dict, Any, Type, List
from BaseClasses import ItemClassification as ItemClass, Tutorial
from Options import PerGameCommonOptions
from worlds.AutoWorld import World, WebWorld

from . import Options, Items, Locations
from .Constants import *


class ZALiAWeb(WebWorld):
    theme = "grass"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up ZALiA for Archipelago multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Rando"],
    )
    tutorials = [setup_en]
    options_presets = Options.presets
    option_groups = Options.groups


class ZALiAWorld(World):
    game = GAME_NAME
    web = ZALiAWeb()
    required_client_version = (0, 6, 8)

    topology_present = False

    item_name_to_id = {
        key: value.code
        for key, value in (Items.item_dict.items() - Items.item_dict_events.items())
    }
    location_name_to_id = {
        key: value.code
        for key, value in (
            Locations.location_dict.items() - Locations.location_dict_events.items()
        )
    }

    item_name_groups = {
        "Tools": {key for key in Items.item_dict_tools.keys()},
        "Spells": {key for key in Items.item_dict_spells.keys()},
        "Skills": {key for key in Items.item_dict_skills.keys()},
        "Keys": {key for key in Items.item_dict_keys.keys()},
        "Containers": {key for key in Items.item_dict_useful.keys()},
        "Crystals": {key for key in Items.item_dict_crystals.keys()},
        "Filler": {key for key in Items.item_dict_filler.keys()},
    }

    options_dataclass: ClassVar[Type[PerGameCommonOptions]] = Options.ZALiAOptions
    options: Options.ZALiAOptions

    def __init__(self, multiworld, player: int):
        super().__init__(multiworld, player)
        # UT re-gen: recover the original gen seed from

        import random

        passthrough = getattr(multiworld, "re_gen_passthrough", {}).get(GAME_NAME, None)
        if isinstance(passthrough, dict):
            self._ut_seed = passthrough.get("ut_seed", 0)
        elif passthrough is not None:
            self._ut_seed = passthrough
        else:
            self._ut_seed = self.random.getrandbits(64)
        self.random = random.Random(self._ut_seed)

    def _restore_options_from_slot_data(self, slot_data: Dict[str, Any]) -> None:
        """Overwrite this world's options with the values recorded in slot_data.
        Required for Universal Tracker."""
        option_hints = self.options_dataclass.type_hints
        for key, value in slot_data.items():
            opt_type = option_hints.get(key)
            if opt_type is not None:
                setattr(self.options, key, opt_type.from_any(value))

    def interpret_slot_data(self, slot_data: Dict[str, Any]) -> Dict[str, Any]:
        """Universal Tracker hook. Returns the full slot_data so the
        tracker re-generates this world with re_gen_passthrough set to it."""
        self._restore_options_from_slot_data(slot_data)
        return slot_data

    def generate_early(self) -> None:
        # UT re-gen:
        passthrough = getattr(self.multiworld, "re_gen_passthrough", {}).get(
            GAME_NAME, None
        )
        if isinstance(passthrough, dict):
            self._restore_options_from_slot_data(passthrough)

        # Town shuffle
        self.town_position: dict = {t: t for t in TOWN_POSITIONS}
        if self.options.randomize_town_locations.value:
            # Bulblin is fixed (not in SHUFFLE_TOWNS)
            shuffled = list(SHUFFLE_TOWNS)
            self.random.shuffle(shuffled)
            for pos, town in zip(SHUFFLE_TOWNS, shuffled):
                self.town_position[town] = pos

        # Old Kasuto's invisible enemies need CROSS

        self.town_needs_cross: set = {self.town_position["Old Kasuto"]}

        # town → parent region of the position it occupies
        self.town_to_parent: dict = {
            town: TOWN_POSITION_PARENT[pos] for town, pos in self.town_position.items()
        }

        # Build dungeon → parent region mapping

        positions = list(DUNGEON_POSITION_PARENT.keys())
        shuffled_dungeons = list(positions)
        if self.options.randomize_dungeon_locations.value:
            self.random.shuffle(shuffled_dungeons)
        self.dungeon_to_parent = {
            dungeon: DUNGEON_POSITION_PARENT[pos]
            for dungeon, pos in zip(positions, shuffled_dungeons)
        }
        # content→position palace layout
        self.dungeon_position = dict(zip(positions, shuffled_dungeons))

        # Rauru Pass version currently fixed to 3
        self.ruaru_pass_version: int = 3

        # Spell-sequence puzzles
        self.spell_sequences: Dict[str, List[str]] = self._generate_spell_sequences()

        # Individual Kakusu checks: pick a RANDOM subset of the 12
        _kakusu_count = min(
            max(self.options.kakusu_individual_location_count.value, 0),
            len(KAKUSU_LOCATION_NAMES),
        )
        self.kakusu_selected_indices: List[int] = sorted(
            self.random.sample(range(1, len(KAKUSU_LOCATION_NAMES) + 1), _kakusu_count)
        )

    # Tier groups + per-sequence anchor, mirroring gml
    _SPELL_SEQ_COUNT: int = 3
    _SPELL_SEQ_GROUP1 = (SPELL_PROTECT, SPELL_JUMP, SPELL_FIRE)
    _SPELL_SEQ_GROUP2 = (SPELL_HEAL, SPELL_FAIRY)
    _SPELL_SEQ_GROUP3 = (SPELL_REFLECT, SPELL_ENIGMA)
    # "01": Kings Tomb, "02": Carock 2, "03": Kasuto Cemetery
    _SPELL_SEQ_ANCHORS = {"01": SPELL_REFLECT, "02": SPELL_ENIGMA, "03": SPELL_ENIGMA}

    def _generate_spell_sequences(self) -> Dict[str, List[str]]:
        count = self._SPELL_SEQ_COUNT
        sequences: Dict[str, List[str]] = {}
        for key, anchor in self._SPELL_SEQ_ANCHORS.items():
            g1 = list(self._SPELL_SEQ_GROUP1)
            g2 = list(self._SPELL_SEQ_GROUP2)
            g3 = list(self._SPELL_SEQ_GROUP3)
            self.random.shuffle(g1)
            self.random.shuffle(g2)
            self.random.shuffle(g3)
            seq = [anchor]
            if count > 1:
                seq.append(g1[0])
            if count > 2:
                seq.append(g2[0])
            if count > 3:
                seq.append(g1[1] if key in ("01", "02") else g3[0])
            self.random.shuffle(seq)
            sequences[key] = seq
        return sequences

    def create_regions(self) -> None:
        from .Regions import create_regions

        create_regions(self, self.player)

    def create_items(self) -> None:
        items_made: int = 0
        preplaced_count: int = 0

        keys_to_preplace = set()
        preplace_allkey = False
        spells_to_preplace = {}

        is_quest2 = (
            self.options.starting_quest.value == Options.StartingQuest.option_quest_2
        )

        for item_name, item_data in Items.item_dict.items():
            if item_data.code is None:
                continue
            if item_name == SPELL_SUMMON and not is_quest2:
                # Summon is quest-2 content: it is learned at Bulblin town
                continue
            if item_name in Items.item_dict_crystals:
                # Crystals are force-locked to their palace boss locs
                preplaced_count += item_data.count
                continue
            if (
                item_name in Items.item_dict_keys
                and not self.options.randomize_key_locations.value
            ):
                keys_to_preplace.add(item_name)
                preplaced_count += item_data.count
                continue
            if (
                item_name == ITEM_KEY
                and not self.options.randomize_allkey_location.value
            ):
                # AllKey / Magical Key stays at its vanilla loc (Great Palace)
                preplace_allkey = True
                preplaced_count += 1
                continue
            if (
                item_name in Items.item_dict_spells
                and not self.options.randomize_spell_locations.value
            ):
                spells_to_preplace[item_name] = item_data
                preplaced_count += item_data.count
                continue
            for i in range(item_data.count):
                self.multiworld.itempool.append(self.create_item(item_name))
                items_made += 1
            for i in range(item_data.count_extra):
                self.multiworld.itempool.append(self.create_item(item_name))
                items_made += 1

        if not self.options.randomize_key_locations.value:
            self._preplace_keys(keys_to_preplace)
        if preplace_allkey:
            preplaced_count = self._preplace_allkey(preplaced_count)

        if not self.options.randomize_spell_locations.value:
            preplaced_count = self._preplace_spells(spells_to_preplace, preplaced_count)

        location_count = sum(
            1
            for loc in self.multiworld.get_locations(self.player)
            if loc.address is not None
        )
        junk_count = location_count - items_made - preplaced_count

        for i in range(junk_count):
            self.multiworld.itempool.append(
                self.create_item(self.get_filler_item_name())
            )

    def _preplace_keys(self, key_names: set) -> None:
        palace_key_map = {
            "P1": KEY_PARAPA,
            "P2": KEY_MIDORO,
            "P3": KEY_ISLAND,
            "P4": KEY_MAZE,
            "P5": KEY_SEA,
            "P6": KEY_THREE_EYE,
        }
        for region in self.multiworld.get_regions(self.player):
            for loc in region.locations:
                if loc.address is None:
                    continue
                for prefix, key_name in palace_key_map.items():
                    if loc.name.startswith(prefix + " Key") and key_name in key_names:
                        item = self.create_item(key_name)
                        loc.place_locked_item(item)
                        break

    def _preplace_allkey(self, preplaced_count: int) -> int:
        """Place AllKey at its vanilla location: Great Palace SKELETON KEY room.
        Returns updated preplaced_count (reduces by 1 if location missing)."""
        loc_name = "Great Palace Item location (SKELETON KEY)"
        try:
            loc = self.multiworld.get_location(loc_name, self.player)
        except KeyError:
            # loc missing: AllKey becomes a normal pool item.
            self.multiworld.itempool.append(self.create_item(ITEM_KEY))
            return preplaced_count
        item = self.create_item(ITEM_KEY)
        loc.place_locked_item(item)
        return preplaced_count

    def _preplace_spells(self, spell_items: dict, preplaced_count: int) -> int:
        spell_names = [name for name in SPELL_TO_TOWN if name in spell_items]
        town_names = [SPELL_TO_TOWN[name] for name in spell_names]
        if self.options.shuffle_spells_among_wise_men.value:
            # Wiseman requires jump to access in Nabooru
            _WISEMAN_REQUIRED_SPELLS = {"Nabooru": {SPELL_JUMP}}
            # Keep Summon fixed at the Bulblin wise-man (quest 2)
            _free = [i for i, t in enumerate(town_names) if t != "Bulblin"]
            _towns = [town_names[i] for i in _free]

            def _self_stranded(assignment) -> bool:
                return any(
                    spell_names[_i] in _WISEMAN_REQUIRED_SPELLS.get(_t, ())
                    for _i, _t in zip(_free, assignment)
                )

            for _ in range(100):
                self.random.shuffle(_towns)
                if not _self_stranded(_towns):
                    break

            for _a in range(len(_free)):
                if spell_names[_free[_a]] not in _WISEMAN_REQUIRED_SPELLS.get(
                    _towns[_a], ()
                ):
                    continue
                for _b in range(len(_free)):
                    if _b == _a:
                        continue
                    if spell_names[_free[_a]] not in _WISEMAN_REQUIRED_SPELLS.get(
                        _towns[_b], ()
                    ) and spell_names[_free[_b]] not in _WISEMAN_REQUIRED_SPELLS.get(
                        _towns[_a], ()
                    ):
                        _towns[_a], _towns[_b] = _towns[_b], _towns[_a]
                        break

            for _i, _t in zip(_free, _towns):
                town_names[_i] = _t
        for spell_name, town_name in zip(spell_names, town_names):
            loc_name = f"_Spell_Location_{town_name.replace(' ', '_')}"
            try:
                loc = self.multiworld.get_location(loc_name, self.player)
            except KeyError:
                # Spell loc missing from data, add to pool instead
                self.multiworld.itempool.append(self.create_item(spell_name))
                continue
            item = self.create_item(spell_name)
            loc.place_locked_item(item)
        return preplaced_count

    def create_item(self, name: str) -> Items.ZALiAItem:
        item = Items.item_dict[name].create_item(self.player)
        # The Bottle is only a useful item in quest 1
        # but in quest 2 its progression
        if (
            name == ITEM_BOTTLE
            and self.options.starting_quest.value
            == Options.StartingQuest.option_quest_2
        ):
            item.classification = ItemClass.progression
        return item

    def get_filler_item_name(self) -> str:
        filler_list = list(Items.item_dict_filler.keys())
        return self.random.choice(filler_list)

    def set_rules(self):
        from .Rules import set_rules

        set_rules(self)

    def extend_hint_information(self, hint_data: Dict[int, Dict[int, str]]) -> None:
        """Attach "<content> @ <tile>" context to relocated palace/dungeon and town checks.
        This is the hint-tab counterpart to the UT region relabel in Rules.set_rules.
        """
        from .Regions import INTERIOR_TOWN_LOCATIONS

        info: Dict[int, str] = {}

        # Palaces: label every check in a relocated palace
        for content_region in self.dungeon_to_parent:
            tile = self.dungeon_position.get(content_region)
            if tile is None or tile == content_region:
                continue  # palace on its home tile
            label = f"{content_region} @ {tile}"
            for loc in self.multiworld.get_region(
                content_region, self.player
            ).locations:
                if loc.address is not None:
                    info[loc.address] = label

        # Towns: label only the moved interiors
        content_at = {pos: content for content, pos in self.town_position.items()}
        for position, content in content_at.items():
            if content == position:
                continue  # town on its home tile
            label = f"{content} @ {position}"
            tile_region = self.multiworld.get_region(
                TOWN_TO_REGION[position], self.player
            )
            for loc in tile_region.locations:
                if loc.address is not None and loc.name in INTERIOR_TOWN_LOCATIONS:
                    info[loc.address] = label

        if info:
            hint_data[self.player] = info

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data = self.options.as_dict(
            "death_link",
            "randomize_item_locations",
            "randomize_pbag_locations",
            "randomize_key_locations",
            "shuffle_spells_among_wise_men",
            "randomize_spell_locations",
            "randomize_spell_cost",
            "limit_obscure_locations",
            "dark_room_difficulty",
            "hard_logic_tricks",
            "item_location_hints",
            "zelda_hint",
            "hint_giver_percent",
            "enemy_difficulty",
            "enemy_randomization_method",
            "randomize_enemy_spawners",
            "enemy_enigma",
            "randomize_enemy_hp",
            "randomize_enemy_damage",
            "randomize_level_cost",
            "randomize_xp",
            "randomize_palette",
            "randomize_dungeon_tileset",
            "randomize_dungeon_rooms",
            "randomize_dungeon_locations",
            "randomize_dungeon_boss",
            "boss_item_locations",
            "randomize_town_locations",
            "force_quit_penalty",
            "starting_quest",
            "starting_attack_level",
            "starting_magic_level",
            "starting_life_level",
            "kakusu_required_count",
            "kakusu_individual_location_count",
            "crystals_required_count",
        )
        # Store seed for UT re-gen passthrough
        slot_data["ut_seed"] = self._ut_seed
        # Legacy seed for game-side gen (matches GML rando)
        slot_data["seed"] = (self.multiworld.seed + self.player) & 0xFFFFFFFF

        # Lets the client verify its live loc table
        slot_data["location_data_checksum"] = Locations.LOCATION_DATA_CHECKSUM

        # Per-seed set of created ZALiA locations.
        # Each hex character stores four consecutive
        # catalog locations, least-significant bit first.
        _created_offsets = {
            loc.address - BASE_ID
            for loc in self.multiworld.get_locations(self.player)
            if loc.address is not None and loc.address >= BASE_ID
        }
        _catalog_size = max(
            (
                location_id - BASE_ID + 1
                for location_id in self.location_name_to_id.values()
            ),
            default=0,
        )
        _hex_digits = "0123456789abcdef"
        _created_nibbles = []
        for _nibble_start in range(0, _catalog_size, 4):
            _nibble = 0
            for _bit in range(4):
                if _nibble_start + _bit in _created_offsets:
                    _nibble |= 1 << _bit
            _created_nibbles.append(_hex_digits[_nibble])
        slot_data["location_manifest_version"] = 2
        slot_data["location_catalog_size"] = _catalog_size
        slot_data["created_location_bits"] = "".join(_created_nibbles)

        # The GML client needs authoritative ids for the six virtual boss checks,
        # which are not represented by native GML location records.
        slot_data["boss_item_location_ids"] = json.dumps(
            {
                str(dungeon_num): self.location_name_to_id[location_name]
                for dungeon_num, location_name in enumerate(
                    PALACE_BOSS_ITEM.values(), start=1
                )
            }
        )

        # Expose dynamically-generated mappings for tracker logic
        slot_data["town_position"] = json.dumps(self.town_position)
        slot_data["town_to_parent"] = json.dumps(self.town_to_parent)
        slot_data["dungeon_to_parent"] = json.dumps(self.dungeon_to_parent)
        # dungeon_position is content→position mapping
        slot_data["dungeon_position"] = json.dumps(self.dungeon_position)
        slot_data["town_needs_cross"] = json.dumps(list(self.town_needs_cross))
        slot_data["ruaru_pass_version"] = self.ruaru_pass_version

        # Spell-sequence puzzles
        slot_data["spell_sequences"] = json.dumps(
            {key: "|".join(seq) for key, seq in self.spell_sequences.items()}
        )

        # Which of the 12 Gold Slimes (by fixed 1..12 index) were randomly picked
        slot_data["kakusu_selected_indices"] = json.dumps(
            {str(i): 1 for i in self.kakusu_selected_indices}
        )
        slot_data["kakusu_location_ids"] = json.dumps(
            {
                str(i + 1): self.location_name_to_id[name]
                for i, name in enumerate(KAKUSU_LOCATION_NAMES)
            }
        )

        # Zelda's hint (zelda_hint option) reveals one target
        _zelda_target = {1: ITEM_FLUTE, 2: ITEM_KEY, 3: SPELL_JUMP}.get(
            self.options.zelda_hint.value
        )
        if _zelda_target is not None:
            for loc in self.multiworld.get_locations():
                if (
                    loc.item is not None
                    and loc.item.player == self.player
                    and loc.item.name == _zelda_target
                ):
                    slot_data["zelda_hint_item"] = _zelda_target
                    slot_data["zelda_hint_location"] = loc.name
                    slot_data["zelda_hint_player"] = loc.player
                    # loc id within its owning world.
                    # When the target sits in other worlds, hint system is used.
                    slot_data["zelda_hint_location_id"] = loc.address
                    break

        return slot_data
