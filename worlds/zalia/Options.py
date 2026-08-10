from dataclasses import dataclass
from typing import Dict, Any

from Options import (
    PerGameCommonOptions,
    DeathLink,
    StartInventoryPool,
    Choice,
    DefaultOnToggle,
    Range,
    Toggle,
    OptionGroup,
)


class RandomizeItemLocations(DefaultOnToggle):
    """Items included in the mix: Main Items, Quest Items, Treasure Maps, Container Pieces, 1-Up Dolls."""

    display_name = "Randomize Item Locations"


class RandomizePBagLocations(Toggle):
    """Include P-Bags in the mix."""

    display_name = "Randomize P-Bag Locations"


class RandomizeKeyLocations(Toggle):
    """Include keys in the mix. Force-equips the Magical Key to its vanilla location.\n
    To view key info: open the spell menu and hold the Y button.\n
    Recommended to turn off Randomize Magical Key Location for this setting."""

    display_name = "Randomize Key Locations"


class RandomizeAllKeyLocation(Toggle):
    """Includes the Magical/Skeleton Key in the shuffle instead of force-equipping it to
    its vanilla Great Palace location, letting it potentially turn up as an early item.
    Independent of Randomize Key Locations, which only affects the per-dungeon small keys.
    """

    display_name = "Randomize Magical Key Location"


class LimitObscureLocations(Toggle):
    """Some item locations are obscure, making the time it takes to get to one fairly lengthy.\n
    Enabling this limits the chance a progression item will be placed at an obscure location.
    """

    display_name = "Limit Obscure Locations"


class DarkRoomDifficulty(Range):
    """Controls whether dark rooms can be traversed without a light source.\n\n
    0: CANDLE or FIRE required for every dark room — most restrictive.\n
    1: dark rooms of moderate difficulty can be traversed without light;\n
        only the hardest dark rooms require CANDLE or FIRE.\n
    2: CANDLE or FIRE is never required — all dark rooms passable without light."""

    display_name = "Dark Room Difficulty"
    range_start = 0
    range_end = 2
    default = 0


class HardLogicTricks(Toggle):
    """Allow precise/difficult tricks in the logic.\n\n
    Off (default): locations that can only be reached itemlessly through a very
    precise trick instead require the intended item.\n
    On: precise alternatives are assumed, including itemless fire-pillar crossings
    and upthrust-less routes where GLOVE and JUMP are still required. Only enable if
    you are comfortable executing precise movement."""

    display_name = "Hard Logic Tricks"


class ItemLocationHints(DefaultOnToggle):
    """NPCs and dialogue objects with a '?' above them will give a hint to the location of an item.\n
    To view found hints: open the spell menu and hold the B button."""

    display_name = "Item Location Hints"


class ZeldaHint(Choice):
    """Zelda gives a hint to the location of an item.\n
    To view found hints: open the spell menu and hold the B button."""

    display_name = "Zelda Hint"
    option_none = 0
    option_flute = 1
    option_magical_key = 2
    option_jump_town = 3
    default = option_none


class HintGiverPercent(Range):
    """Percentage of in-game hint-givers (NPCs/objects marked with a '?') that actually
    give a useful item-location hint. The rest simply say they know nothing.\n
    100 = every hint-giver has a hint (the old behavior); 25 (default) = about a quarter do.\n
    Has no effect if Item Location Hints is disabled."""

    display_name = "Hint Giver Percent"
    range_start = 0
    range_end = 100
    default = 25


class ShuffleSpellsAmongWiseMen(Toggle):
    """Shuffle which spell each Wise Man teaches you. Spells stay locked to
    Wise Man locations -- only the town-to-spell mapping is randomized.\n
    Ignored if Randomize Spell Locations is enabled."""

    display_name = "Shuffle Spells Among Wise Men"


class RandomizeSpellLocations(Toggle):
    """Put spells into the general item/location pool instead of keeping them
    locked to Wise Man locations. Spells can then turn up anywhere (dungeons,
    P-Bags, etc.), and Wise Men can give out any item instead of just a
    spell.\n
    Overrides Shuffle Spells Among Wise Men."""

    display_name = "Randomize Spell Locations"


class RandomizeSpellCost(DefaultOnToggle):
    """Randomize spell MP costs. Variation: -25% to +10%."""

    display_name = "Randomize Spell Costs"


class RandomizeDungeonRooms(Toggle):
    """Randomize dungeon room layouts."""

    display_name = "Randomize Dungeon Rooms"


class RandomizeDungeonLocations(Toggle):
    """Assigns each overworld dungeon tile a dungeon from a shuffled list.\n
    Includes all 7 1st Quest dungeons in the shuffle. Requires Item Rando enabled."""

    display_name = "Randomize Dungeon Locations"


class RandomizeDungeonBoss(Toggle):
    """Assigns each of the 6 crystal dungeons a boss from a shuffled list.\n
    Includes all 6 crystal dungeon bosses in the shuffle."""

    display_name = "Randomize Dungeon Boss"


class BossItemLocations(Toggle):
    """Add an extra AP location at each of the 6 crystal palace bosses, holding a
    normal randomized item -- on top of the crystal the boss already grants.\n
    Each boss item is gated on the full palace clear, exactly like the crystal, and
    is checked at the same moment (when the crystal is placed)."""

    display_name = "Boss Item Locations"


class RandomizeTownLocations(Toggle):
    """Assigns each overworld town tile a town from a shuffled list.\n
    Includes all 8 1st Quest towns in the shuffle."""

    display_name = "Randomize Town Locations"


class EnemyDifficulty(Range):
    """Difficulty rank of enemies that get randomized (1-4)."""

    display_name = "Enemy Difficulty"
    range_start = 1
    range_end = 4
    default = 1


class EnemyRandomizationMethod(Choice):
    """How enemies are randomized:\n
    Vanilla: no enemy randomization.\n
    Spawns: shuffle enemy spawn locations (recommended).\n
    Types: shuffle enemy types (may turn common enemies into much harder ones)."""

    display_name = "Enemy Randomization Method"
    option_vanilla = 0
    option_random_spawns = 1
    option_random_types = 2
    default = option_vanilla


class RandomizeEnemySpawners(Toggle):
    """Shuffle the spawn locations of enemy spawners.\n
    Drop spawners keep their vanilla locations, but the enemy that spawns from each drop is randomized.
    """

    display_name = "Randomize Enemy Spawners"


class EnemyEnigma(Toggle):
    """Enemies transform into a random enemy instead of a basic Blue Slime when under the Enigma spell."""

    display_name = "Enemy Enigma"


class RandomizeEnemyHP(Toggle):
    """Randomize enemy HP. Variation: -25% to +25%."""

    display_name = "Randomize Enemy HP"


class RandomizeEnemyDamage(Toggle):
    """Randomize enemy damage. Variation: -25% to +25%."""

    display_name = "Randomize Enemy Damage"


class RandomizeLevelCost(DefaultOnToggle):
    """Randomize level-up costs. Variation: -25% to +25%."""

    display_name = "Randomize Level Cost"


class RandomizeXP(DefaultOnToggle):
    """Randomize XP gains from enemies and P-Bags. Variation: -25% to +25%."""

    display_name = "Randomize XP"


class RandomizePalette(Toggle):
    """Randomize color palettes. Can be adjusted in the options menu once in-game."""

    display_name = "Randomize Palettes"


class RandomizeDungeonTileset(Toggle):
    """Assigns each dungeon graphics from a shuffled list.\n
    Includes all original and custom dungeon graphics in the shuffle."""

    display_name = "Randomize Dungeon Tileset"


class StartingQuest(Choice):
    """Which quest to start on (Quest 1 or Quest 2)."""

    display_name = "Starting Quest"
    option_quest_1 = 1
    option_quest_2 = 2
    default = option_quest_1


class StartingAttackLevel(Range):
    """What Attack level to start at.\n\nNote: this is a handicap and does not affect randomization logic."""

    display_name = "Starting Attack Level"
    range_start = 1
    range_end = 9
    default = 1


class StartingMagicLevel(Range):
    """What Magic level to start at.\n\nNote: this is a handicap and does not affect randomization logic."""

    display_name = "Starting Magic Level"
    range_start = 1
    range_end = 9
    default = 1


class StartingLifeLevel(Range):
    """What Life level to start at.\n\nNote: this is a handicap and does not affect randomization logic."""

    display_name = "Starting Life Level"
    range_start = 1
    range_end = 9
    default = 1


class ForceQuitPenalty(DefaultOnToggle):
    """Penalty for game-over warping:\n
    On (Vanilla): XP loss of 75%.\n
    Off (Recommended): no penalty.\n\n
    Game-over warping is when a game over is forced by holding LT+RT+SELECT.\n
    Backtracking is much more likely in rando, so freely warping back to town saves time.\n
    Note: losing all lives still incurs the vanilla 75% penalty."""

    display_name = "Force Quit Penalty"


class KakusuRequiredCount(Range):
    """Number of Gold Slimes (Kakusu) required for their reward."""

    display_name = "Required Kakusu Count"
    range_start = 0
    range_end = 12
    default = 7


class KakusuIndividualLocationCount(Range):
    """Exposes this many of the 12 Gold Slime (Kakusu) kills as their own individual AP locations.\n
    The remaining (unexposed) kills still count toward the bundled
    kakusu_required_count reward as before --\nthis option only adds extra locations, it never
    removes anything from the bundled reward's requirement."""

    display_name = "Individual Kakusu Locations"
    range_start = 0
    range_end = 12
    default = 0


class CrystalsRequiredCount(Range):
    """Number of crystals required to enter the Great Palace."""

    display_name = "Required Crystal Count"
    range_start = 0
    range_end = 6
    default = 6


@dataclass
class ZALiAOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool

    # Item options
    randomize_item_locations: RandomizeItemLocations
    randomize_pbag_locations: RandomizePBagLocations
    randomize_key_locations: RandomizeKeyLocations
    randomize_allkey_location: RandomizeAllKeyLocation
    limit_obscure_locations: LimitObscureLocations
    dark_room_difficulty: DarkRoomDifficulty
    hard_logic_tricks: HardLogicTricks
    item_location_hints: ItemLocationHints
    zelda_hint: ZeldaHint
    hint_giver_percent: HintGiverPercent

    # Spell options
    shuffle_spells_among_wise_men: ShuffleSpellsAmongWiseMen
    randomize_spell_locations: RandomizeSpellLocations
    randomize_spell_cost: RandomizeSpellCost

    # Dungeon options
    randomize_dungeon_rooms: RandomizeDungeonRooms
    randomize_dungeon_locations: RandomizeDungeonLocations
    randomize_dungeon_boss: RandomizeDungeonBoss
    boss_item_locations: BossItemLocations
    randomize_town_locations: RandomizeTownLocations

    # Enemy options
    enemy_difficulty: EnemyDifficulty
    enemy_randomization_method: EnemyRandomizationMethod
    randomize_enemy_spawners: RandomizeEnemySpawners
    enemy_enigma: EnemyEnigma
    randomize_enemy_hp: RandomizeEnemyHP
    randomize_enemy_damage: RandomizeEnemyDamage

    # Misc
    randomize_level_cost: RandomizeLevelCost
    randomize_xp: RandomizeXP
    randomize_palette: RandomizePalette
    randomize_dungeon_tileset: RandomizeDungeonTileset
    force_quit_penalty: ForceQuitPenalty
    starting_quest: StartingQuest
    starting_attack_level: StartingAttackLevel
    starting_magic_level: StartingMagicLevel
    starting_life_level: StartingLifeLevel

    # Goal
    kakusu_required_count: KakusuRequiredCount
    kakusu_individual_location_count: KakusuIndividualLocationCount
    crystals_required_count: CrystalsRequiredCount

    # Connectivity
    death_link: DeathLink


groups = [
    OptionGroup(
        "Item Options",
        [
            RandomizeItemLocations,
            RandomizePBagLocations,
            RandomizeKeyLocations,
            RandomizeAllKeyLocation,
            LimitObscureLocations,
            DarkRoomDifficulty,
            HardLogicTricks,
            ItemLocationHints,
            ZeldaHint,
            HintGiverPercent,
        ],
    ),
    OptionGroup(
        "Spell Options",
        [
            ShuffleSpellsAmongWiseMen,
            RandomizeSpellLocations,
            RandomizeSpellCost,
        ],
    ),
    OptionGroup(
        "Dungeon Options",
        [
            RandomizeDungeonRooms,
            RandomizeDungeonLocations,
            RandomizeDungeonBoss,
            BossItemLocations,
            RandomizeTownLocations,
            RandomizeDungeonTileset,
        ],
    ),
    OptionGroup(
        "Enemy Options",
        [
            EnemyDifficulty,
            EnemyRandomizationMethod,
            RandomizeEnemySpawners,
            EnemyEnigma,
            RandomizeEnemyHP,
            RandomizeEnemyDamage,
        ],
    ),
    OptionGroup(
        "Other Options",
        [
            RandomizeLevelCost,
            RandomizeXP,
            RandomizePalette,
            ForceQuitPenalty,
            StartingQuest,
            StartingAttackLevel,
            StartingMagicLevel,
            StartingLifeLevel,
            KakusuRequiredCount,
            KakusuIndividualLocationCount,
            CrystalsRequiredCount,
            DeathLink,
        ],
    ),
]

presets = {
    "Vanilla-like": {
        "randomize_item_locations": True,
        "randomize_pbag_locations": False,
        "randomize_key_locations": False,
        "shuffle_spells_among_wise_men": False,
        "randomize_spell_locations": False,
        "limit_obscure_locations": False,
        "dark_room_difficulty": 0,
        "item_location_hints": True,
        "death_link": False,
    },
    "Full Randomizer": {
        "randomize_item_locations": True,
        "randomize_pbag_locations": True,
        "randomize_key_locations": True,
        "shuffle_spells_among_wise_men": True,
        "randomize_spell_locations": True,
        "randomize_spell_cost": True,
        "randomize_dungeon_locations": True,
        "randomize_dungeon_boss": True,
        "randomize_town_locations": True,
        "limit_obscure_locations": True,
        "dark_room_difficulty": 2,
        "item_location_hints": True,
        "death_link": False,
    },
}
