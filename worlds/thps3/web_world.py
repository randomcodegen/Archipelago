from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .data import GAME_NAME
from .options import option_groups, option_presets


class THPS3WebWorld(WebWorld):
    game = GAME_NAME
    theme = "partyTime"

    tutorials = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up Tony Hawk's Pro Skater 3 for Archipelago.",
            "English",
            "setup_en.md",
            "setup/en",
            ["Rando"],
        )
    ]

    option_groups = option_groups
    options_presets = option_presets
