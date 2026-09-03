from dataclasses import dataclass

from Options import (
    Choice,
    OptionCounter,
    OptionDict,
    OptionError,
    PerGameCommonOptions,
    Range,
    Toggle,
)

from .data.generated import MAPS

PICKUP_CLASSNAMES = frozenset(
    classname
    for map_data in MAPS
    for pickup in map_data["pickups"]
    for classname in pickup["classnames"]
)
TRAVERSAL_CLASSNAMES = frozenset(("trigger_push", "trigger_teleport"))


class Q3Maps(OptionCounter):
    """Stock Quake III maps eligible for selection. Set a map key to 1 to include it."""

    display_name = "Q3 Maps"
    valid_keys = frozenset(
        map_data["key"] for map_data in MAPS if map_data["key"].startswith("q3")
    )
    min = 0
    max = 1
    default = {key: 1 for key in valid_keys}


class CPMAMaps(OptionCounter):
    """CPMA maps eligible for selection. Set a map key to 1 to include it."""

    display_name = "CPMA Maps"
    valid_keys = frozenset(
        map_data["key"] for map_data in MAPS if map_data["key"].startswith("cpm")
    )
    min = 0
    max = 1
    default = {key: 0 for key in valid_keys}


class CPMA(Toggle):
    """Enable CPMA mod support. Required when CPMA maps are enabled."""

    display_name = "CPMA"


class MapPoolSize(Range):
    """Number of eligible maps selected at random, capped at the number enabled.
    Zero uses the whole enabled map pool."""

    display_name = "Map Pool Size"
    range_start = 0
    range_end = len(MAPS)
    default = 10


class KillCheckIncrement(Range):
    """Create a location at every X frags. 1 creates a location for every frag."""

    display_name = "Kill Check Increment"
    range_start = 1
    range_end = 50
    default = 5


class CustomIncludedLocations(OptionDict):
    """Classnames to turn into Archipelago locations in percentages.
    Deletes classnames remain vanilla spawns."""

    display_name = "Custom Included Locations"
    valid_keys = PICKUP_CLASSNAMES | TRAVERSAL_CLASSNAMES
    default = {classname: 100 for classname in valid_keys}

    def verify(self, world, player_name, plando_options) -> None:
        super().verify(world, player_name, plando_options)
        invalid = {
            key: value
            for key, value in self.value.items()
            if not isinstance(value, int)
            or isinstance(value, bool)
            or not 0 <= value <= 100
        }
        if invalid:
            raise OptionError(
                f"Player {player_name} has invalid location percentages: {invalid}"
            )


class Goal(Choice):
    """Victory condition for this seed."""

    display_name = "Goal"
    option_stage_clears = 0
    option_quad_token_hunt = 1
    default = 0


class GoalPercentage(Range):
    """Percentage of selected stages that must be cleared."""

    display_name = "Goal Percentage"
    range_start = 1
    range_end = 100
    default = 50


class QuadTokenPoolPercentage(Range):
    """Percentage of filler slots replaced with Quad Tokens."""

    display_name = "Quad Token Pool Percentage"
    range_start = 1
    range_end = 100
    default = 25


class QuadTokenGoalPercentage(Range):
    """Percentage of generated Quad Tokens required for victory."""

    display_name = "Quad Token Goal Percentage"
    range_start = 1
    range_end = 100
    default = 80


class WeaponLogicPercentage(Range):
    """Percentage of a stage's weapon unlocks required in logic."""

    display_name = "Weapon Logic Percentage"
    range_start = 0
    range_end = 100
    default = 25


class MaximumStartingWeapons(Range):
    """Maximum weapon unlocks precollected for the starting stage."""

    display_name = "Maximum Starting Weapons"
    range_start = 1
    range_end = 8
    default = 2


class ItemLogicPercentage(Range):
    """Percentage of a stage's item unlocks required in logic."""

    display_name = "Item Logic Percentage"
    range_start = 0
    range_end = 100
    default = 25


@dataclass
class Quake3Options(PerGameCommonOptions):
    cpma: CPMA
    q3_maps: Q3Maps
    cpma_maps: CPMAMaps
    map_pool_size: MapPoolSize
    kill_check_increment: KillCheckIncrement
    custom_included_locations: CustomIncludedLocations
    goal: Goal
    goal_percentage: GoalPercentage
    quad_token_pool_percentage: QuadTokenPoolPercentage
    quad_token_goal_percentage: QuadTokenGoalPercentage
    weapon_logic_percentage: WeaponLogicPercentage
    maximum_starting_weapons: MaximumStartingWeapons
    item_logic_percentage: ItemLogicPercentage
