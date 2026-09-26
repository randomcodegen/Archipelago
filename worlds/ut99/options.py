from dataclasses import dataclass

from Options import Choice, OptionDict, OptionError, OptionSet, PerGameCommonOptions, Range, Toggle
from .catalog import MAPS, PICKUPS


PICKUP_CLASSES = frozenset(pickup["class"] for pickup in PICKUPS)


class IncludedMaps(OptionSet):
    """Stock DM, CTF, DOM, and AS maps to include. Select at least two."""
    display_name = "Included Maps"
    valid_keys = frozenset(MAPS)
    default = tuple(sorted(MAPS))


class MapPoolSize(Range):
    """Random maps to select, up to the number included."""
    display_name = "Map Pool Size"
    range_start = 2
    range_end = len(MAPS)
    default = 10


class FragCheckIncrement(Range):
    """One check per X enemy kills in each arena."""
    display_name = "Frag Check Increment"
    range_start = 1
    range_end = 25
    default = 5


class MatchFragLimit(Range):
    """Deathmatch win target and per-arena frag-check cap in every mode."""
    display_name = "Match Frag Limit"
    range_start = 1
    range_end = 100
    default = 20


class GoalPercentage(Range):
    """Percentage of selected maps to win."""
    display_name = "Goal Percentage"
    range_start = 1
    range_end = 100
    default = 50


class BotSkill(Range):
    """Bot difficulty: 0 Novice through 7 Godlike."""
    display_name = "Bot Skill"
    range_start = 0
    range_end = 7
    default = 2


class BotCount(Range):
    """Bots per match."""
    display_name = "Bot Count"
    range_start = 1
    range_end = 7
    default = 3


class WeaponLogicPercentage(Range):
    """Weapon families needed to enter an arena, as a percentage."""
    display_name = "Weapon Logic Percentage"
    range_start = 0
    range_end = 100
    default = 25


class MaximumStartingWeapons(Range):
    """Cap on weapon unlocks granted for starting arena access."""
    display_name = "Maximum Starting Weapons"
    range_start = 0
    range_end = 9
    default = 2


class CustomIncludedLocations(OptionDict):
    """Percent of each pickup class to turn into AP locations.
    Removed classes remain vanilla spawns."""

    display_name = "Custom Included Locations"
    valid_keys = PICKUP_CLASSES
    default = {classname: 100 for classname in valid_keys}

    def verify(self, world, player_name, plando_options) -> None:
        super().verify(world, player_name, plando_options)
        invalid = {
            key: value for key, value in self.value.items()
            if not isinstance(value, int) or isinstance(value, bool) or not 0 <= value <= 100
        }
        if invalid:
            raise OptionError(f"Player {player_name} has invalid location percentages: {invalid}")


class PickupUnlockMode(Choice):
    """Family: shared unlock for e.g. health items. 
    Type: one unlock per pickup model."""
    display_name = "Pickup Unlock Mode"
    option_family = 0
    option_type = 1
    default = 0


class DeathLink(Toggle):
    """Share arena deaths with other DeathLink players."""
    display_name = "DeathLink"
    default = 0


@dataclass
class UT99Options(PerGameCommonOptions):
    included_maps: IncludedMaps
    map_pool_size: MapPoolSize
    frag_check_increment: FragCheckIncrement
    match_frag_limit: MatchFragLimit
    goal_percentage: GoalPercentage
    bot_skill: BotSkill
    bot_count: BotCount
    weapon_logic_percentage: WeaponLogicPercentage
    maximum_starting_weapons: MaximumStartingWeapons
    custom_included_locations: CustomIncludedLocations
    pickup_unlock_mode: PickupUnlockMode
    death_link: DeathLink
