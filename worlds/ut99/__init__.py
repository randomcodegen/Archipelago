from BaseClasses import Item, ItemClassification, Location, Region, Tutorial
from Options import OptionError
from worlds.AutoWorld import WebWorld, World

from .catalog import (AMMO_FILLERS, GAME, ITEM_NAME_TO_ID, LOCATION_NAME_TO_ID, MAPS, PICKUP_BASE,
                      PICKUP_CLASS_FAMILY, PICKUP_FAMILIES, PICKUP_NAMES, PICKUPS,
                      PICKUP_TYPE_CLASSES, PICKUP_TYPE_NAMES, objective_labels,
                      SCHEMA_VERSION, WEAPONS)
from .options import UT99Options


class UT99Item(Item):
    game = GAME


class UT99Location(Location):
    game = GAME


class UT99Web(WebWorld):
    tutorials = [Tutorial("Multiworld Setup Guide", "Play UT99 with an UnrealScript AP client.",
                          "English", "setup_en.md", "setup/en", ["Rando"])]


def required_count(total: int, percentage: int) -> int:
    return (total * percentage + 99) // 100


class UT99World(World):
    """Unlock maps, weapons, and pickups. Win bot matches."""
    game = GAME
    web = UT99Web()
    options_dataclass = UT99Options
    options: UT99Options
    item_name_to_id = ITEM_NAME_TO_ID
    location_name_to_id = LOCATION_NAME_TO_ID

    def generate_early(self):
        eligible = [name for name in MAPS if name in self.options.included_maps.value]
        if len(eligible) < 2:
            raise OptionError("Unreal Tournament 99 needs at least two included maps")
        weapon_names = {name for name, _ in WEAPONS}
        stage_weapons = {name: set() for name in eligible}
        for pickup in PICKUPS:
            name = MAPS[pickup["map"]]
            if name in stage_weapons:
                family = PICKUP_CLASS_FAMILY[pickup["class"].lower()]
                if family in weapon_names:
                    stage_weapons[name].add(f"{family} Unlock")
        self.stage_weapons = {name: tuple(sorted(unlocks)) for name, unlocks in stage_weapons.items()}
        percentage = self.options.weapon_logic_percentage.value
        candidates = [name for name in eligible if required_count(
            len(self.stage_weapons[name]), percentage) <= self.options.maximum_starting_weapons.value]
        if not candidates:
            raise OptionError("Maximum Starting Weapons is too low for Weapon Logic Percentage")
        self.starting_map = self.random.choice(candidates)
        self.selected_maps = sorted([self.starting_map] + self.random.sample(
            [name for name in eligible if name != self.starting_map],
            min(self.options.map_pool_size.value, len(eligible)) - 1), key=MAPS.index)
        arena_weapons = {unlock for name in self.selected_maps for unlock in self.stage_weapons[name]}
        self.filler_items = ("Health Refill", "Armor Refill") + tuple(
            filler for (weapon, _), (filler, _, _) in zip(WEAPONS, AMMO_FILLERS)
            if f"{weapon} Unlock" in arena_weapons)
        self.goal_required = (len(self.selected_maps) * self.options.goal_percentage.value + 99) // 100
        self.frag_checks = self.options.match_frag_limit.value // self.options.frag_check_increment.value
        percentages = self.options.custom_included_locations.value
        self.included_pickups = {
            index for index, pickup in enumerate(PICKUPS)
            if MAPS[pickup["map"]] in self.selected_maps
            and self.random.random() < percentages.get(pickup["class"], 0) / 100
        }

    def create_regions(self):
        menu = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu)
        for name in self.selected_maps:
            region = Region(name, self.player, self.multiworld)
            self.multiworld.regions.append(region)
            weapons = self.stage_weapons[name]
            required = required_count(len(weapons), self.options.weapon_logic_percentage.value)
            menu.connect(region, f"Enter {name}",
                         lambda state, name=name, weapons=weapons, required=required:
                         state.has(f"{name} Unlock", self.player) and
                         state.has_from_list_unique(weapons, self.player, required))
            labels = ["Win", *objective_labels(name, self.frag_checks)]
            if name in MAPS[37:]:
                labels += [f"Frag Milestone {i}" for i in range(1, self.frag_checks + 1)]
            for label in labels:
                loc = f"{name} - {label}"
                region.locations.append(UT99Location(self.player, loc, LOCATION_NAME_TO_ID[loc], region))
            for index, (pickup, loc) in enumerate(zip(PICKUPS, PICKUP_NAMES)):
                if index in self.included_pickups and MAPS[pickup["map"]] == name:
                    location = UT99Location(self.player, loc, LOCATION_NAME_TO_ID[loc], region)
                    classname = pickup["class"].lower()
                    unlock = (f"{PICKUP_CLASS_FAMILY[classname]} Unlock"
                              if self.options.pickup_unlock_mode.value == 0 else
                              PICKUP_TYPE_NAMES[PICKUP_TYPE_CLASSES.index(classname)])
                    location.access_rule = lambda state, unlock=unlock: state.has(
                        unlock, self.player)
                    region.locations.append(location)
            # Winning uses the same arena entry rules
            event = UT99Location(self.player, f"{name} Cleared", None, region)
            event.place_locked_item(UT99Item(f"{name} Cleared", ItemClassification.progression,
                                            None, self.player))
            region.locations.append(event)

    def create_items(self):
        needed = required_count(len(self.stage_weapons[self.starting_map]),
                                self.options.weapon_logic_percentage.value)
        precollected = {self.starting_map + " Unlock", *self.random.sample(
            self.stage_weapons[self.starting_map], needed)}
        names = [name + " Unlock" for name in self.selected_maps]
        names += [name + " Unlock" for name, _ in WEAPONS]
        if self.options.pickup_unlock_mode.value == 0:
            names += [name + " Unlock" for name in PICKUP_FAMILIES]
        else:
            names += PICKUP_TYPE_NAMES
        count = len(self.multiworld.get_unfilled_locations(self.player))
        available = [name for name in names if name not in precollected]
        precollected.update(self.random.sample(available, max(0, len(available) - count)))
        for name in sorted(precollected):
            self.multiworld.push_precollected(self.create_item(name))
        pool = [self.create_item(name) for name in names if name not in precollected]
        pool.extend(self.create_item(self.get_filler_item_name()) for _ in range(count - len(pool)))
        self.multiworld.itempool.extend(pool)

    def create_item(self, name):
        if name in {"Health Refill", "Armor Refill"} or name in {
                filler for filler, _, _ in AMMO_FILLERS}:
            classification = ItemClassification.filler
        elif (self.options.pickup_unlock_mode.value == 1 and
              self.options.weapon_logic_percentage.value == 0 and
              name in {f"{weapon} Unlock" for weapon, _ in WEAPONS}):
            classification = ItemClassification.useful
        else:
            classification = ItemClassification.progression
        return UT99Item(name, classification, ITEM_NAME_TO_ID[name], self.player)

    def get_filler_item_name(self):
        return self.random.choice(self.filler_items)

    def set_rules(self):
        cleared = [f"{name} Cleared" for name in self.selected_maps]
        self.multiworld.completion_condition[self.player] = lambda state: (
            state.has_from_list_unique(cleared, self.player, self.goal_required))

    def fill_slot_data(self):
        return {
            "schema_version": SCHEMA_VERSION,
            "selected_maps": [MAPS.index(name) for name in self.selected_maps],
            "starting_map": MAPS.index(self.starting_map),
            "goal_required": self.goal_required,
            "pickup_catalog_version": 2,
            "pickup_locations": [PICKUP_BASE + index for index in sorted(self.included_pickups)],
            "pickup_unlock_mode": self.options.pickup_unlock_mode.value,
            "death_link": bool(self.options.death_link.value),
            **self.options.as_dict("frag_check_increment", "match_frag_limit", "bot_skill", "bot_count",
                                   "weapon_logic_percentage"),
        }
