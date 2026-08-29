from dataclasses import dataclass

from Options import (
    Choice,
    OptionCounter,
    OptionGroup,
    OptionSet,
    PerGameCommonOptions,
    Range,
    Toggle,
)

from .data import (
    DECKS,
    GAPS_BY_LEVEL,
    GOALS,
    LEVELS,
    NORMAL_GOAL_NAMES,
    SKATERS,
    STAT_POINTS,
)
from .items import FILLER_ITEMS

LOCATION_TYPES = ("objectives", "stat points", "hidden decks", "gaps")


class SkaterPool(OptionSet):
    """
    The pool from which the player's skater is selected.
    """

    display_name = "Skater Pool"
    valid_keys = frozenset(skater.name for skater in SKATERS)
    default = frozenset(skater.name for skater in SKATERS)


class LevelPool(OptionCounter):
    """Level Pool Size picks from this set of levels."""

    display_name = "Level Pool"
    valid_keys = frozenset(level.name for level in LEVELS)
    min = 0
    max = 1
    default = {level.name: 1 for level in LEVELS}


class LevelPoolSize(Range):
    """Number of levels randomly selected. Zero uses the whole pool."""

    display_name = "Level Pool Size"
    range_start = 0
    range_end = len(LEVELS)
    default = 0


class MaxObjectivesPerLevel(Range):
    """Maximum objective locations available in each level."""

    display_name = "Maximum Objectives Per Level"
    range_start = 1
    range_end = len(NORMAL_GOAL_NAMES)
    default = range_end


class GapChecksPercentage(Range):
    """
    Percentage of gaps selected for every level.
    A nonzero percentage rounds up, so a level
    always receives at least one gap location.
    """

    display_name = "Gap Checks Percentage"
    range_start = 0
    range_end = 100
    default = 0


class StatPointChecks(Toggle):
    """Include the five stat points in each level as locations."""

    display_name = "Stat Point Checks"
    default = 1


class HiddenDeckChecks(Toggle):
    """Include each level's hidden deck as a location."""

    display_name = "Hidden Deck Checks"
    default = 1


class LocationTypeFilter(OptionCounter):
    """
    Location categories that exist in the generated world. Use 1 to include a
    category and 0 (or omit it) to exclude that category entirely.
    """

    display_name = "Location Type Filter"
    valid_keys = frozenset(LOCATION_TYPES)
    min = 0
    max = 1
    default = {key: 1 for key in LOCATION_TYPES}


class FillerItemWeights(OptionCounter):
    """Relative weights used when choosing filler items. Omitted items have zero weight."""

    display_name = "Filler Item Weights"
    valid_keys = FILLER_ITEMS
    min = 1
    default = {name: 50 for name in FILLER_ITEMS}


class CompletionGoal(Choice):
    """
    Choose a victory condition:

    Objectives: Complete the required objectives count.
    Levels: Fully complete the required levels count.
    Cruise Ship: Complete every selected Cruise Ship objective.
    Gold Medals: Earn the required number Gold Medals.
    Goal Type: Complete the chosen goal type in every active non-competition level.
    Gap Hunt: Complete the required percentage of gaps.
    Collectibles: Collect the required number of stat points and hidden decks.
    Total Checks: Complete the required checks across all enabled location types.
    Level Tour: Complete the number of required objectives per active Level.
    """

    display_name = "Completion Goal"
    option_objectives = 0
    option_levels = 1
    option_cruise_ship = 2
    option_gold_medals = 3
    option_goal_type = 4
    option_gap_hunt = 5
    option_collectibles = 6
    option_total_checks = 7
    option_level_tour = 8
    default = option_objectives


class CompletionGoalType(Choice):
    """Career objective type required by the goal_type completion goal."""

    display_name = "Completion Goal Type"
    option_high_score = 0
    option_pro_score = 1
    option_sick_score = 2
    option_collect_skate = 3
    option_trick_spot = 4
    option_secret_tape = 5
    option_scripted_goal_1 = 6
    option_scripted_goal_2 = 7
    option_scripted_goal_3 = 8
    default = option_secret_tape


class RequiredObjectives(Range):
    """
    Career goal and medal locations required for the objectives goal.
    """

    display_name = "Required Objectives"
    range_start = 1
    range_end = len(GOALS)
    default = 20


class RequiredLevels(Range):
    """
    Fully completed levels required for the level victory. A normal level
    requires every career goal, a competition requires every medal location.
    """

    display_name = "Required Levels"
    range_start = 1
    range_end = len(LEVELS)
    default = 5


class RequiredGoldMedals(Range):
    """Gold Medal locations required for the gold_medals victory."""

    display_name = "Required Gold Medals"
    range_start = 1
    range_end = sum(level.competition for level in LEVELS)
    default = range_end


class RequiredGapPercentage(Range):
    """Percentage of selected gap locations required for gap_hunt victory."""

    display_name = "Required Gap Percentage"
    range_start = 1
    range_end = 100
    default = 20


class RequiredCollectibles(Range):
    """Stat-point and hidden-deck locations required for collectibles victory."""

    display_name = "Required Collectibles"
    range_start = 1
    range_end = len(STAT_POINTS) + len(DECKS)
    default = 20


class RequiredChecks(Range):
    """Needed locations for a total_checks victory."""

    display_name = "Required Checks"
    range_start = 1
    range_end = (
        len(GOALS)
        + len(STAT_POINTS)
        + len(DECKS)
        + sum(map(len, GAPS_BY_LEVEL.values()))
    )
    default = 50


class RequiredObjectivesPerLevel(Range):
    """Career objectives required in every level by the level_tour goal."""

    display_name = "Required Objectives Per Level"
    range_start = 1
    range_end = len(NORMAL_GOAL_NAMES)
    default = 1


@dataclass
class THPS3Options(PerGameCommonOptions):
    skater_pool: SkaterPool
    level_pool: LevelPool
    level_pool_size: LevelPoolSize
    gap_checks_percentage: GapChecksPercentage
    stat_point_checks: StatPointChecks
    hidden_deck_checks: HiddenDeckChecks
    location_type_filter: LocationTypeFilter
    filler_item_weights: FillerItemWeights
    max_objectives_per_level: MaxObjectivesPerLevel
    completion_goal: CompletionGoal
    completion_goal_type: CompletionGoalType
    required_objectives: RequiredObjectives
    required_levels: RequiredLevels
    required_gold_medals: RequiredGoldMedals
    required_gap_percentage: RequiredGapPercentage
    required_collectibles: RequiredCollectibles
    required_checks: RequiredChecks
    required_objectives_per_level: RequiredObjectivesPerLevel


option_groups = [
    OptionGroup(
        "Game Configuration",
        [SkaterPool, LevelPool, LevelPoolSize],
    ),
    OptionGroup(
        "Locations",
        [
            LocationTypeFilter,
            MaxObjectivesPerLevel,
            GapChecksPercentage,
            StatPointChecks,
            HiddenDeckChecks,
        ],
    ),
    OptionGroup(
        "Items",
        [FillerItemWeights],
    ),
    OptionGroup(
        "Victory",
        [
            CompletionGoal,
            CompletionGoalType,
            RequiredObjectives,
            RequiredLevels,
            RequiredGoldMedals,
            RequiredGapPercentage,
            RequiredCollectibles,
            RequiredChecks,
            RequiredObjectivesPerLevel,
        ],
    ),
]


option_presets = {
    "Goals Only": {
        "skater_pool": SkaterPool.default,
        "level_pool": LevelPool.default,
        "level_pool_size": 0,
        "gap_checks_percentage": 0,
        "stat_point_checks": False,
        "hidden_deck_checks": False,
        "location_type_filter": LocationTypeFilter.default,
        "filler_item_weights": FillerItemWeights.default,
        "max_objectives_per_level": MaxObjectivesPerLevel.default,
        "completion_goal": "objectives",
        "completion_goal_type": "secret_tape",
        "required_objectives": 20,
        "required_levels": 5,
        "required_gold_medals": 3,
        "required_gap_percentage": 20,
        "required_collectibles": 20,
        "required_checks": 50,
        "required_objectives_per_level": 1,
    },
}
