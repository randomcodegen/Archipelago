from dataclasses import dataclass

from Options import Choice, NamedRange, PerGameCommonOptions, Toggle


class SkillLevel(Choice):
    """In-Game difficulty. Primarily affects number of Enemies spawned"""

    display_name = "Skill Level"
    option_easy = 0
    option_medium = 1
    option_hard = 2
    option_nightmare = 3
    default = 1


class Difficulty(Choice):
    """Randomizer difficulty. Higher levels offer less resources and worse items in the pool"""

    display_name = "Difficulty"
    option_easy = 0
    option_medium = 1
    option_hard = 2
    option_extreme = 3
    default = 1


class LogicDifficulty(Choice):
    """Trick difficulty for logic. Higher levels require harder tricks such precise Rocket/Grenade Jumps and airstrafes"""

    display_name = "Logic Difficulty"
    option_easy = 0
    option_medium = 1
    option_hard = 2
    option_extreme = 3
    default = 1


class UnlockAbilities(Toggle):
    """Unlock Jumping, Diving, Running, Rocket/Grenade Jumps as items"""

    display_name = "Unlock Abilities"
    default = True


class DamageRemoverAbilities(Toggle):
    """Unlock the ability to not get hurt when doing rocket/grenade jumps"""

    display_name = "Unlock Damage Removal"
    default = True


class UnlockInteract(Toggle):
    """Unlock using buttons, shooting switches and opening doors as items"""

    display_name = "Unlock Interaction"
    default = True


# class AllowSaving(Toggle):
#    """Enables saving to store mid level progress. If disabled, levels always have to be played from the start"""
#
#    display_name = "Allow Saving"
#    default = True


class AreaMaps(Choice):
    """Select if full game maps are available in the in-game map view"""

    display_name = "Area Maps"
    option_none = 0
    option_unlockable = 1
    option_start_with = 2
    default = 2


class Goal(Choice):
    """Choose the goal of the game"""

    display_name = "Goal"
    option_beat_all_bosses = 0
    option_beat_all_levels = 1
    option_collect_all_secrets = 2
    option_all = 3
    default = 3


class GoalPercentage(NamedRange):
    """Percentage of chosen goals that need to be reached to win the game"""

    display_name = "Percentage of Goals required"
    range_start = 25
    range_end = 100
    special_range_names: {
        "half": 50,
        "all": 100,
    }
    default = 100


class IncludeSecrets(Toggle):
    """Include secret areas into the location pool. This only has an effect if they are not already
    included as goal locations"""

    display_name = "Include Secrets as Locations"
    default = False


class LocationDensity(Choice):
    """Choose the amount of vanilla pickup spots that get converted into location checks. Higher values may create
    an item density that is (potentially much) higher than other Archipelago games"""

    display_name = "Location Density"
    option_iconic = 0
    option_balanced = 1
    # 2 is reserved internally for balanced with secrets disabled as checks. It is implicitly selected as a variant
    # of balanced based on other options
    option_dense = 3
    option_all = 4
    option_include_mp_only_pickups = 5
    default = 1


class Episode1(Toggle):
    """Include Episode 1: Doomed Dimension in the randomizer"""

    display_name = "Use Episode 1"
    default = True


class Episode2(Toggle):
    """Include Episode 2: Realm of Black Magic in the randomizer"""

    display_name = "Use Episode 2"
    default = True


class Episode3(Toggle):
    """Include Episode 3: Netherworld in the randomizer"""

    display_name = "Use Episode 3"
    default = True


class Episode4(Toggle):
    """Include Episode 4: The Elder World in the randomizer"""

    display_name = "Use Episode 4"
    default = True


class IncludeHub(Toggle):
    """Include the Hub Level in the randomizer"""

    display_name = "Use Hub Level"
    default = False


class IncludeEnd(Toggle):
    """Include the End Level in the randomizer"""

    display_name = "Use End Level"
    default = True


class LevelCount(NamedRange):
    """
    Number of maps that should be included in the shuffle. Maps are picked from the enabled episodes. If this count
    exceeds the maximum number of levels in those episodes, all of them will be included.
    """

    display_name = "Level Count"
    range_start = 2
    range_end = 32
    default = 9
    special_range_names: {
        "all": 32,
    }


class ShuffleStartingLevels(Toggle):
    """If enabled will pick levels unlocked by default at random instead of the first of each episode"""

    display_name = "Shuffle Starting Levels"
    default = True


class ProgressiveWeapons(Toggle):
    """
    Replace weapon unlocks and ammunition capacity upgrades with progressive versions.
    This greatly increases access to weapons to your world.
    """

    display_name = "Progressive Weapons"
    default = True


class ProgressiveInventories(Toggle):
    """
    Replace Inventory unlocks and their capacity upgrades with progressive versions.
    This increases access to their abilities in your world.
    """

    display_name = "Progressive Inventory"
    default = True


class ShellRecharge(Toggle):
    """
    Recharges 1 shell (ammo) every second.
    QoL to make the early game less painful on hard+ difficulties.
    """

    display_name = "Recharge Shells"
    default = False


class TrapPercentage(NamedRange):
    """Percentage of filler items that should be traps"""

    display_name = "Trap Percentage"
    range_start = 0
    range_end = 90
    default = 10


@dataclass
class Q1Options(PerGameCommonOptions):
    difficulty: Difficulty
    logic_difficulty: LogicDifficulty
    skill_level: SkillLevel
    unlock_abilities: UnlockAbilities
    damage_remover_abilities: DamageRemoverAbilities
    unlock_interact: UnlockInteract
    # allow_saving: AllowSaving
    area_maps: AreaMaps
    goal: Goal
    goal_percentage: GoalPercentage
    location_density: LocationDensity
    include_secrets: IncludeSecrets
    episode1: Episode1
    episode2: Episode2
    episode3: Episode3
    episode4: Episode4
    include_hub: IncludeHub
    include_end: IncludeEnd
    level_count: LevelCount
    shuffle_starting_levels: ShuffleStartingLevels
    progressive_weapons: ProgressiveWeapons
    progressive_inventories: ProgressiveInventories
    trap_percentage: TrapPercentage
    shell_recharge: ShellRecharge
