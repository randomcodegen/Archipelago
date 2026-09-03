from BaseClasses import Tutorial
from Options import OptionError
from worlds.AutoWorld import WebWorld, World

from .data.generated import (
    AMMO_FILLERS,
    CATALOG_HASH,
    ITEM_NAME_TO_ID,
    LOCATION_NAME_TO_ID,
    MAPS,
    MAP_BY_KEY,
)
from .items import FILLER_ITEMS, Quake3Item, create_item, overflow_unlocks
from .options import Quake3Options
from .regions import create_regions
from .rules import required_count, set_rules


class Quake3Web(WebWorld):
    theme = "dirt"
    tutorials = [
        Tutorial(
            "Multiworld Setup Guide",
            "Install the Quake III Arena Archipelago client and connect using baseq3 or CPMA.",
            "English",
            "setup_en.md",
            "setup/en",
            ["Rando"],
        )
    ]


class Quake3World(World):
    """Quake III Arena stage, pickup, and frag checks using a custom Quake3e client."""

    game = "Quake III Arena"
    web = Quake3Web()
    options_dataclass = Quake3Options
    options: Quake3Options
    topology_present = False
    item_name_to_id = ITEM_NAME_TO_ID
    location_name_to_id = LOCATION_NAME_TO_ID

    selected_map_keys: list[str]
    included_pickup_locations: set[str]
    included_traversal_locations: set[str]
    starting_map_key: str
    goal_required: int
    quad_token_total: int

    def generate_early(self) -> None:
        requested_maps = {
            key
            for option in (self.options.q3_maps, self.options.cpma_maps)
            for key, enabled in option.value.items()
            if enabled
        }
        if not self.options.cpma.value and any(
            key.startswith("cpm") for key in requested_maps
        ):
            raise OptionError("CPMA maps require the CPMA option")
        eligible_maps = [
            map_data for map_data in MAPS if map_data["key"] in requested_maps
        ]
        if not eligible_maps:
            raise OptionError("Q3 Maps and CPMA Maps must enable at least one map")
        pool_size = min(self.options.map_pool_size.value or len(eligible_maps), len(eligible_maps))

        weapon_percentage = self.options.weapon_logic_percentage.value
        weapon_cap = self.options.maximum_starting_weapons.value
        starting_maps = [
            map_data
            for map_data in eligible_maps
            if required_count(len(map_data["weapon_families"]), weapon_percentage)
            <= weapon_cap
        ]
        if not starting_maps:
            raise OptionError(
                "Maximum Starting Weapons is too low for Weapon Logic Percentage"
            )
        starting_map = self.random.choice(starting_maps)
        selected = (
            (
                self.random.sample(
                    [
                        map_data
                        for map_data in eligible_maps
                        if map_data is not starting_map
                    ],
                    pool_size - 1,
                )
                + [starting_map]
            )
            if pool_size < len(eligible_maps)
            else eligible_maps
        )
        selected.sort(key=lambda map_data: map_data["map_index"])
        self.selected_map_keys = [map_data["key"] for map_data in selected]
        weapon_families = {family for map_data in selected for family in map_data["weapon_families"]}
        unused_ammo = {name for name, family, _ in AMMO_FILLERS if family not in weapon_families}
        self.filler_items = tuple(name for name in FILLER_ITEMS if name not in unused_ammo)
        percentages = self.options.custom_included_locations.value
        self.included_pickup_locations = {
            pickup["location_name"]
            for map_data in selected
            for pickup in map_data["pickups"]
            if self.random.random()
            < max(percentages.get(classname, 0) for classname in pickup["classnames"])
            / 100
        }
        self.included_traversal_locations = {
            traversal["location_name"]
            for map_data in selected
            for traversal in map_data["traversals"]
            if self.random.random()
            < percentages.get(
                (
                    "trigger_push"
                    if traversal["kind"] == "jump_pad"
                    else "trigger_teleport"
                ),
                0,
            )
            / 100
        }
        self.starting_map_key = starting_map["key"]
        self.goal_required = (
            required_count(len(selected), self.options.goal_percentage.value)
            if self.options.goal.value == 0
            else 0
        )
        self.quad_token_total = 0

    def create_regions(self) -> None:
        create_regions(self)

    def create_item(self, name: str) -> Quake3Item:
        return create_item(self.player, name)

    def get_filler_item_name(self) -> str:
        return self.random.choice(self.filler_items)

    def create_items(self) -> None:
        selected_maps = [MAP_BY_KEY[key] for key in self.selected_map_keys]
        progression_names = [map_data["stage_item_name"] for map_data in selected_maps]
        weapon_families = list(
            dict.fromkeys(
                family
                for map_data in selected_maps
                for family in map_data["weapon_families"]
            )
        )
        nonweapon_families = list(
            dict.fromkeys(
                family
                for map_data in selected_maps
                for family in map_data["nonweapon_families"]
            )
        )
        progression_names.extend(f"{family} Unlock" for family in weapon_families)
        progression_names.extend(f"{family} Unlock" for family in nonweapon_families)

        starting_map = MAP_BY_KEY[self.starting_map_key]
        precollected = {starting_map["stage_item_name"]}
        for families, percentage in (
            (
                starting_map["weapon_families"],
                self.options.weapon_logic_percentage.value,
            ),
            (
                starting_map["nonweapon_families"],
                self.options.item_logic_percentage.value,
            ),
        ):
            count = required_count(len(families), percentage)
            precollected.update(
                f"{family} Unlock"
                for family in self.random.sample(list(families), count)
            )
        for name in precollected:
            self.multiworld.push_precollected(self.create_item(name))

        pool_names = [name for name in progression_names if name not in precollected]
        unfilled_count = len(self.multiworld.get_unfilled_locations(self.player))
        precollected_overflow = overflow_unlocks(
            pool_names, unfilled_count, self.random
        )
        if precollected_overflow:
            for name in precollected_overflow:
                self.multiworld.push_precollected(self.create_item(name))
            pool_names = [
                name for name in pool_names if name not in precollected_overflow
            ]
        if len(pool_names) > unfilled_count:
            raise OptionError("Quake III Arena stage items exceed available checks")
        pool = [self.create_item(name) for name in pool_names]
        if self.options.goal.value == 1:
            self.quad_token_total = required_count(
                unfilled_count - len(pool),
                self.options.quad_token_pool_percentage.value,
            )
            if not self.quad_token_total:
                raise OptionError("Quad Token Hunt has no available item slots")
            self.goal_required = required_count(
                self.quad_token_total, self.options.quad_token_goal_percentage.value
            )
            pool.extend(
                self.create_item("Quad Token") for _ in range(self.quad_token_total)
            )
        pool.extend(
            self.create_item(self.get_filler_item_name()) for _ in range(unfilled_count - len(pool))
        )
        self.multiworld.itempool.extend(pool)

    def set_rules(self) -> None:
        set_rules(self)

    def fill_slot_data(self) -> dict:
        return {
            "schema_version": 8,
            "cpma": self.options.cpma.value,
            "catalog_hash": CATALOG_HASH,
            "selected_maps": list(self.selected_map_keys),
            "pickup_locations": sorted(
                pickup["location_id"]
                for key in self.selected_map_keys
                for pickup in MAP_BY_KEY[key]["pickups"]
                if pickup["location_name"] in self.included_pickup_locations
            )
            + sorted(
                traversal["location_id"]
                for key in self.selected_map_keys
                for traversal in MAP_BY_KEY[key]["traversals"]
                if traversal["location_name"] in self.included_traversal_locations
            ),
            "starting_map": self.starting_map_key,
            "goal_type": self.options.goal.value,
            "goal_required": self.goal_required,
            "kill_check_increment": self.options.kill_check_increment.value,
            "weapon_logic_percentage": self.options.weapon_logic_percentage.value,
            "item_logic_percentage": self.options.item_logic_percentage.value,
        }
