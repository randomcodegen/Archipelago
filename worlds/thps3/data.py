from __future__ import annotations

import json
import math
import pkgutil
import random
import zlib
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

GAME_NAME = "Tony Hawk's Pro Skater 3"
CLIENT_PROTOCOL_VERSION = 1

TRICK_CATEGORY_ITEMS: tuple[str, ...] = (
    "Flip Tricks",
    "Grab Tricks",
    "Grind Tricks",
    "Manual Tricks",
    "Lip Tricks",
    "Reverts",
    "Special Tricks",
)


@dataclass(frozen=True)
class LevelData:
    key: str
    name: str
    level_num: int
    competition: bool = False


@dataclass(frozen=True)
class SkaterData:
    key: str
    name: str
    trick_style: str


@dataclass(frozen=True)
class GoalData:
    level_key: str
    goal_id: int
    name: str

    @property
    def location_name(self) -> str:
        return f"{LEVEL_BY_KEY[self.level_key].name} - {self.name}"

    @property
    def item_name(self) -> str:
        return f"Unlock {LEVEL_BY_KEY[self.level_key].name} - {self.name}"


@dataclass(frozen=True)
class StatPointData:
    level_key: str
    point_id: int

    @property
    def location_name(self) -> str:
        return f"{LEVEL_BY_KEY[self.level_key].name} - " f"Stat Point {self.point_id}"


@dataclass(frozen=True)
class DeckData:
    level_key: str

    @property
    def location_name(self) -> str:
        return f"{LEVEL_BY_KEY[self.level_key].name} - Hidden Deck"


@dataclass(frozen=True)
class GapData:
    level_key: str
    checksum: int
    name: str
    required_trick_items: frozenset[str] = frozenset()
    required_all_trick_items: frozenset[str] = frozenset()
    required_goal_ids: frozenset[int] = frozenset()

    @property
    def location_name(self) -> str:
        return f"{LEVEL_BY_KEY[self.level_key].name} - Gap: {self.name}"


LEVELS: tuple[LevelData, ...] = (
    LevelData("foundry", "Foundry", 1),
    LevelData("canada", "Canada", 2),
    LevelData("rio", "Rio", 3, competition=True),
    LevelData("suburbia", "Suburbia", 4),
    LevelData("airport", "Airport", 5),
    LevelData("skater_island", "Skater Island", 6, competition=True),
    LevelData("los_angeles", "Los Angeles", 7),
    LevelData("tokyo", "Tokyo", 8, competition=True),
    LevelData("cruise_ship", "Cruise Ship", 9),
)

LEVEL_BY_KEY = {level.key: level for level in LEVELS}


# Keep this in native master_skater_list order; the client uses the same order.
SKATERS: tuple[SkaterData, ...] = (
    SkaterData("tony_hawk", "Tony Hawk", "vert"),
    SkaterData("steve_caballero", "Steve Caballero", "street"),
    SkaterData("kareem_campbell", "Kareem Campbell", "street"),
    SkaterData("rune_glifberg", "Rune Glifberg", "vert"),
    SkaterData("eric_koston", "Eric Koston", "street"),
    SkaterData("bucky_lasek", "Bucky Lasek", "vert"),
    SkaterData("bam_margera", "Bam Margera", "street"),
    SkaterData("rodney_mullen", "Rodney Mullen", "street"),
    SkaterData("chad_muska", "Chad Muska", "street"),
    SkaterData("andrew_reynolds", "Andrew Reynolds", "street"),
    SkaterData("geoff_rowley", "Geoff Rowley", "street"),
    SkaterData("elissa_steamer", "Elissa Steamer", "street"),
    SkaterData("jamie_thomas", "Jamie Thomas", "street"),
    SkaterData("darth_maul", "Darth Maul", "vert"),
    SkaterData("wolverine", "Wolverine", "street"),
    SkaterData("officer_dick", "Officer Dick", "street"),
    SkaterData("private_carrera", "Private Carrera", "street"),
    SkaterData("ollie_the_magic_bum", "Ollie the Magic Bum", "street"),
    SkaterData("kelly_slater", "Kelly Slater", "street"),
    SkaterData("demoness", "Demoness", "street"),
    SkaterData("neversoft_eyeball", "Neversoft Eyeball", "street"),
    SkaterData("doom_guy", "DOOM Guy", "street"),
    SkaterData("custom_skater", "Custom Skater", "street"),
)

SKATER_BY_NAME = {skater.name: skater for skater in SKATERS}


NORMAL_GOAL_NAMES: tuple[str, ...] = (
    "High Score",
    "Pro Score",
    "Sick Score",
    "Collect S-K-A-T-E",
    "Trick Spot",
    "Secret Tape",
    "Scripted Goal 1",
    "Scripted Goal 2",
    "Scripted Goal 3",
)

SCRIPTED_GOAL_NAMES_BY_LEVEL: dict[str, tuple[str, str, str]] = {
    "foundry": ("Grind the Molten Bucket", "Un-Jam 5 Valves", "Soak the Foreman"),
    "canada": ("Bury that Bully!", "Impress the Skaters", "Get Chuck Unstuck"),
    "suburbia": ("Help The Thin Man", "Restore Power To The Dish", "Squash 5 Pumpkins"),
    "airport": ("Get the tickets to your Skate Buddy", "Stop the pickpockets", "Visit 10 countries"),
    "los_angeles": ("Start the Earthquake", "Block the Car Chase", "Free Ballin'"),
    "cruise_ship": ("Raise the Ferry", "Trash the Museum", "Impress the Neversoft Girls"),
}

COMPETITION_GOAL_NAMES: tuple[str, ...] = (
    "Bronze Medal",
    "Silver Medal",
    "Gold Medal",
)


def _build_goals() -> tuple[GoalData, ...]:
    goals: list[GoalData] = []
    for level in LEVELS:
        goal_names = (
            COMPETITION_GOAL_NAMES
            if level.competition
            else NORMAL_GOAL_NAMES[:6] + SCRIPTED_GOAL_NAMES_BY_LEVEL[level.key]
        )
        for goal_id, goal_name in enumerate(goal_names):
            goals.append(
                GoalData(
                    level_key=level.key,
                    goal_id=goal_id,
                    name=goal_name,
                )
            )
    return tuple(goals)


GOALS = _build_goals()
GOALS_BY_LEVEL = {
    level.key: tuple(goal for goal in GOALS if goal.level_key == level.key)
    for level in LEVELS
}
GOAL_BY_LEVEL_AND_ID = {(goal.level_key, goal.goal_id): goal for goal in GOALS}


STAT_POINTS: tuple[StatPointData, ...] = tuple(
    StatPointData(level.key, point_id) for level in LEVELS for point_id in range(1, 6)
)
STAT_POINTS_BY_LEVEL = {
    level.key: tuple(
        stat_point for stat_point in STAT_POINTS if stat_point.level_key == level.key
    )
    for level in LEVELS
}


DECKS: tuple[DeckData, ...] = tuple(DeckData(level.key) for level in LEVELS)
DECK_BY_LEVEL = {deck.level_key: deck for deck in DECKS}


_objective_requirement_bytes = (
    pkgutil.get_data(__package__, "objective_stat_requirements.json")
    if __package__
    else Path(__file__).with_name("objective_stat_requirements.json").read_bytes()
)
if _objective_requirement_bytes is None:
    raise RuntimeError("packaged objective/stat requirements are missing")
OBJECTIVE_STAT_REQUIREMENTS = json.loads(
    _objective_requirement_bytes.decode("utf-8-sig")
)
SKATER_LAYOUTS = OBJECTIVE_STAT_REQUIREMENTS["skater_layouts"]
OBJECTIVE_REQUIREMENTS = OBJECTIVE_STAT_REQUIREMENTS["objectives"]
SKATE_LETTER_REQUIREMENTS = OBJECTIVE_STAT_REQUIREMENTS["skate_letters"]
HIDDEN_DECK_REQUIREMENTS = OBJECTIVE_STAT_REQUIREMENTS["hidden_decks"]
STAT_POINT_REQUIREMENTS = OBJECTIVE_STAT_REQUIREMENTS["stat_points"]


def _gap_checksum(name: str) -> int:
    return zlib.crc32(name.encode("ascii").lower()) ^ 0xFFFFFFFF


_gap_requirement_bytes = (
    pkgutil.get_data(__package__, "gap_requirements_manual.json")
    if __package__
    else Path(__file__).with_name("gap_requirements_manual.json").read_bytes()
)
if _gap_requirement_bytes is None:
    raise RuntimeError("packaged gap requirements are missing")
_gap_requirement_data = json.loads(_gap_requirement_bytes.decode("utf-8-sig"))
GAP_REQUIREMENTS_BY_NAME = {
    (level_key, gap_name): requirement
    for level_key, gaps in _gap_requirement_data.items()
    if level_key != "_instructions"
    for gap_name, requirement in gaps.items()
}


def _parse_gap_requirement(
    requirement: object,
) -> tuple[frozenset[str], frozenset[str], frozenset[int]]:
    if requirement is None:
        return frozenset(), frozenset(), frozenset()
    if isinstance(requirement, list):
        return frozenset(requirement), frozenset(), frozenset()
    if isinstance(requirement, dict):
        goal_ids = set(requirement.get("goal_ids", ()))
        if "goal_id" in requirement:
            goal_ids.add(requirement["goal_id"])
        return (
            frozenset(requirement.get("any", ())),
            frozenset(requirement.get("all", ())),
            frozenset(goal_ids),
        )
    raise TypeError(f"invalid gap requirement: {requirement!r}")


_parsed_gap_requirements = {
    (level_key, _gap_checksum(gap_name)): _parse_gap_requirement(requirement)
    for (level_key, gap_name), requirement in GAP_REQUIREMENTS_BY_NAME.items()
}
GAP_REQUIREMENT_OVERRIDES = {
    key: any_items
    for key, (any_items, _, _) in _parsed_gap_requirements.items()
    if any_items
}
GAP_ALL_REQUIREMENT_OVERRIDES = {
    key: all_items
    for key, (_, all_items, _) in _parsed_gap_requirements.items()
    if all_items
}
GAP_GOAL_REQUIREMENT_OVERRIDES = {
    key: goal_ids
    for key, (_, _, goal_ids) in _parsed_gap_requirements.items()
    if goal_ids
}
GAP_NO_REQUIREMENT_OVERRIDES = {
    key
    for key, requirement in _parsed_gap_requirements.items()
    if requirement == (frozenset(), frozenset(), frozenset())
}


def _gap(level_key: str, name: str) -> GapData:
    checksum = _gap_checksum(name)
    return GapData(
        level_key,
        checksum,
        name,
        GAP_REQUIREMENT_OVERRIDES.get((level_key, checksum), frozenset()),
        GAP_ALL_REQUIREMENT_OVERRIDES.get((level_key, checksum), frozenset()),
        GAP_GOAL_REQUIREMENT_OVERRIDES.get((level_key, checksum), frozenset()),
    )


FOUNDRY_GAPS: tuple[GapData, ...] = tuple(
    _gap("foundry", name)
    for name in (
        "TC's Rail",
        "Over the Pipe!",
        "Press Box Kink",
        "Furnace Walk",
        "Round the Bend!!!",
        "Up and Over!!!",
        "Back End Rail 2 Rail",
        "Bucket o' Hot Sauce!",
        "Catwalk Balancing Act",
        "Catwalk Grind",
        "Catwalk Tight Lip",
        "CG's SKDK 2 STFK",
        "Circus Act Around The Bend!",
        "Control Booth Transfer",
        "Deep Fried Transfer",
        "Don't Look Down!",
        "Edge O' the Tub Extension",
        "From Way Down Town!",
        "Furnace Row Extension",
        "Furnace Topper Rail",
        "Furnace Walk Rail 2 Rail!",
        "Generator Hop",
        "Generator Transfer",
        "Hardway Over the Hot Tub",
        "High Voltage Walkway Lip",
        "Hot Tub Jump",
        "Just Passing Through",
        "Lil' Rail Hop",
        "Low Current Walkway Lip",
        "Nausea Grind!!!",
        "Nice View Up Here!",
        "Poolside Over Under Gap",
        "Porch Rail Tap",
        "Press Booth Rail 2 Rail",
        "Press Walk Rail 2 Rail!",
        "Rail Hop",
        "Railin' On Furnace Row",
        "Roll In Hop",
        "Roll In Transfer",
        "Split the Wickets!",
        "Stair Steppin'",
        "Stomp the Presses!",
        "Tub Rail Tap",
        "Walkin' A Thin Line!",
    )
)

CANADA_GAPS: tuple[GapData, ...] = tuple(
    _gap("canada", name)
    for name in (
        "Curb Hoppin",
        "Parking Lot Mini Gap",
        "Crossover the Hard Way",
        "Crossover the Easy Way",
        "Fence Hoppin",
        "Fence Bomb",
        "Air Over the Blade Grind",
        "Fence Transfer",
        "Flying Fenceman",
        "Cut the Corner",
        "Rail Stomp",
        "Rail Bank Shot",
        "Breezy Pants Gap",
        "Crooked Extension",
        "Mandatory Videogame Mine Cart Ride",
        "Mine Cart Launch",
        "Grind the Pine",
        "Good Eye!",
        "Hitch Knot Gap",
        "Nice shootin'...",
        "Felled Oak",
        "Banner Ad Dot Com",
        "Park to Lot Launch",
        "IPO Funding",
        "AHHH!  MY HEAD!",
        "Fence Extension",
        "Funbox to Rail Stomp",
        "Rail Cheater",
        "Bowl to Rail",
        "Go long and Grind",
        "Around The Horn",
        "Look, Ma!  No Talent!",
        "Hillside Rail Stomp",
        "Smooth As Silk",
        "Walkin' the Riffles",
        "The Panhandler",
        "Is Not Gold",
        "Whoa.  That was Cool.",
        "Tree to Corral Grind",
        "The Rush Is On",
        "eniM detnuaH ehT",
        "ROCKSLIDE!!!",
        "Rail to Bowl",
        "Bowl to Bowl",
        "Prospector Path",
        "All that Glitters",
        "Mountain Man Mine Stomp",
        "Sap Slapper",
        "Nice Save, cheater",
        "The Haunted Mine",
        "Chainsaw Buzzin'",
        "Steam Stomp!",
        "Dozer Blade Gap",
        "Curb Bomb",
        "Car Gap",
        "Flying Fence Stomp",
        "Big Air Fence Stomp",
        "Airin' Up and Out",
        "Funbox Hop",
        "Over The Blade",
        "We Dont Need No Steeenking Rails",
        "Climb the Tree",
        "Tree Air Gap",
        "Hillside Tree Path Launch",
        "River Hop",
        "There's gold in them thar hills.",
        "Corral Gap Transfer",
        "...Tex!",
        "Manual Transmission",
        "Load and Go",
        "The Old Wing Dam",
        "Saved by the Generator",
        "Comin Out of the Sky",
        "Light it up!",
        "Buck Wild",
        "Breezy Channel Gap",
        "Still Bootleggin'",
        "Aurora Burly-alis!",
        "...Just Went Bankrupt.",
        "Antenna Stomp",
        "Corral to Tree Transfer",
        "Corral to Tree Grind",
        "You're Over the Hill!",
        "Over the Hump",
        "Dead Man's Slide",
        "PickAxe Sluice",
    )
)

RIO_GAPS: tuple[GapData, ...] = tuple(
    _gap("rio", name)
    for name in (
        "Short Wall Stomp",
        "Corner Stomp",
        "Tunnel Gap",
        "Big Tunnel Gap",
        "Take It To Da Bridge!",
        "Cake Walk Ledge 2 Ledge",
        "Channel Gap",
        "Ramp Hop",
        "High Wire Act",
        "Whoopty Rail Gap",
        "Ghetto Rail Gap",
        "Bank Ledge Gap",
        "Bus Stop Stomp",
        "Spectator Box Stomp",
        "Ramp 2 Ramp Transfer",
        "Red Line Grind",
        "Ruby Red Lip",
        "Ghetto Extension",
        "Quarter Back Extension",
        "Lip 2 Box",
        "2 Wheeled Whoopty Gap",
        "2 Wheeled Box Gap",
        "Bench Trippin'",
        "Dumpster Dive",
        "Over the Platform",
        "Over the Break",
        "Over the Bank",
    )
)

SUBURBIA_GAPS: tuple[GapData, ...] = tuple(
    _gap("suburbia", name)
    for name in (
        "Where's Your Hard Hat?",
        "So Cold...",
        "Picnic Lip Tric!",
        "Smells like some BBQ!",
        "Grabbin' Pine!",
        "Plywood Pop",
        "2X4 Hop",
        "Ding Dong Ditch Transfer",
        "Utopia Sign Gap",
        "Hop The Fence",
        "Trailer Fence Hop",
        "Up n'Over",
        "Street Transfer",
        "Trailer Hop",
        "Spooky Drop",
        "Trailer Roof Gap",
        "ChainlinkGap",
        "Twister Bait Gap",
        "Riches to Riches mini-gap",
        "Headless Horseman Gap",
        "Roof Rage Level I",
        "Roof Rage Level II",
        "Return To The Living",
        "The Holly Matchet Rules Transfer",
        "Between The Ramps",
        "Mansion on Wheels Transfer",
        "Hot Foot",
        "Corner Cut Construction",
        "Wall Hoppin'",
        "Social Climber",
        "Over Under Construction",
        "Fire Fighter",
        "Nude Fence Gap",
        "I got a bad feeling about this!",
        "Look Out Behind You!",
        "Haunted Stair Set I",
        "Haunted Stair Set II",
        "No Man's Land Gap",
        "Cash Money Transfer",
        "On Site Construction",
        "Howdy Neighbor Part I",
        "Howdy Neighbor Part II",
        "Raisin' the Roof!",
        "Trick up a Tree!",
        "Scary Tree Plant",
        "Whose House?...Skillz House!",
        "Raisin' the Bar!",
        "Smack City Gap",
        "Rich Hump Hop",
        "Airplane Drop",
        "Leave This Place",
        "Wake The Dead Grind",
        "Stop Gap",
        "Fence Trippin'",
        "Manual the Sac!",
        "No Rest For The Wicked Grind",
        "Power Up Gap",
    )
)

AIRPORT_GAPS: tuple[GapData, ...] = tuple(
    _gap("airport", name)
    for name in (
        "Start to Finish!!!",
        "Gate Transfer!",
        "Spiral Stairs South!",
        "Illuminatin'",
        "The Hard Way Up!",
        "Lighten up!",
        "Last High Light",
        "Baggage Claimed!",
        "Droppin' Science!",
        "Skyin!",
        "Economy Class Grind",
        "Economy Class Lip",
        "Business Class Grind!",
        "Business Class Lip!",
        "Spiral Stairs North!",
        "1st Class Grind!!",
        "1st Class Lip!!",
        "Draining the Vein",
        "Look Out!!",
        "O the S",
        "Local call",
        "Long Distance",
        "Through the Pad!",
        "Grind Baggage Claim",
        "Adios Chopper!",
        "Spotted Bags",
        "Mulin'",
        "Flying High In the Sky",
        "Walkway Ride 1!",
        "Walkway Ride 2!",
        "X-RAY",
        "Walkway Hop",
        "Off the Couch",
        "Escalator Hop",
        "Heliport Baggage",
        "Rail Hop",
        "Light Hop!",
        "Light Pop!",
        "Gate Hop!",
        "Takin' the High Road",
        "Escalatin' the Situation!",
        "Claim Hop!",
        "Musical Chairs",
        "American Made",
        "Tea Time",
        "Zdrasvuite!",
        "HOLA!",
        "Parlez-Vous Skate?",
        "Golden!",
        "Welcome, eh?",
        "Welcom to the Triangle",
        "Country of 700 islands",
        "G'Day",
    )
)

SKATER_ISLAND_GAPS: tuple[GapData, ...] = tuple(
    _gap("skater_island", name)
    for name in (
        "Rail 2 Rail Hop",
        "Coping 2 Rail Pop",
        "High Rail Stomp",
        "The Law Transfer",
        "The Flame Transfer",
        "The Rollerboy Gap",
        "Hell No H2O Gap",
        "Handrail Hop",
        "That's a Mouthful",
        "Skull N'bones",
        "Stars N'Stripes",
        "Crowd Pleaser I",
        "Mr. O'Donnell Hop",
        "Piedmont, North Dakota Gap",
        "The Drop",
        "At The 50",
        "At The 10",
        "At The 5",
        "Touchdown!",
        "Stair Hop",
        "Dancin' on The Tables Transfer",
        "The Boss Gap",
        "The Heartbreaker Gap",
        "The Jersey Nun Gap",
        "Drive Thru Window",
        "Street Park Re-entry Rail",
        "Keel Haul Gap",
        "A Burning Sensation",
        "Shore Leave",
        "Cannon Grind",
        "Fiji Mermaid Hop",
        "42 Miles to NYC Hop",
        "Crowd Pleaser II",
        "Swab The Deck Gap",
        "South Amboy, NJ Gap",
        "Blast 'em",
        "The Aaron C. Roll-in of Death Gap",
        "Palm Tree Hop",
        "Stair Set",
        "Cannon Fodder",
        "Mast Transfer",
        "Land Lubber",
        "Sail Rip",
        "Roof Bustin'",
        "Bowl Transfer",
        "Hit The Stairs",
        "Front Mast Back Grind",
        "How'd You Find That?",
        "The Dreamer Gap",
        "Fearless Shark Hop",
        "Treasure Trip",
        "Violet's Gap",
        "Russian Tease Gap",
        "Surf's Up",
        "Look Out Below!",
    )
)

LOS_ANGELES_GAPS: tuple[GapData, ...] = tuple(
    _gap("los_angeles", name)
    for name in (
        "Passin' Gas!",
        "Burrito Grande",
        "Cold Chillin'",
        "Wash Transfer'",
        "alley-oop!",
        "Ridin' the XXX",
        "overpass leap",
        "Electrified!",
        "To the Ladder!",
        "Lip Wash",
        "To the Stairs!",
        "Hotel Lip Smackin'",
        "WesternTremor!",
        "NorthernTremor!",
        "SouthernTremor!",
        "EasternTremor!",
        "Purple Skippin'",
        "East Side!'",
        "West Side!'",
        "Bustin Cherries!",
        "Bye-bye",
        "Burrito Carnitas",
        "Grind Illin''",
        "Shoots n' Ladders!",
        "Indiana Style!",
        "don't fall!!!",
        "Wire Drop!!!",
        "Washin' Windows",
        "Northern Washerp Lip",
        "Southern Washerp Lip",
        "They're GRATE!",
        "Purple Transfer'",
        "Hung Over'",
        "NoseBleed Time",
        "Goin' Ballistic",
        "Gettin a Learn On!",
        "Stair Skip!",
        "Bunker",
        "down the stairs",
        "All The Way",
        "Over the Yellow Stone Shack",
        "Over the Fountain!",
        "Triple X Hop!",
        "Yellow Cutter!",
        "Yellow Fall",
        "Pure Air!",
        "Wire Ridin 1!",
        "Wire Ridin 2!!",
        "Wire Ridin 3!!",
        "Tower South",
        "Hot, hot, hot!",
        "Doorway Hop",
        "Earthquake!!!",
        "Tower Poppin'",
        "To Get To The Other Side, Baby!",
        "Tower Rails GAP",
        "Fountain Hop",
        "Pershing Ramp",
        "Overpass Aftershock",
        "Tower Rail Swap!",
        "Nice Move!",
        "Rail Skip!",
        "Sqeaky Clean!",
        "Tower Lockin'",
        "Venting Frustration",
        "KIOSK!",
        "Ped Props!",
    )
)

TOKYO_GAPS: tuple[GapData, ...] = tuple(
    _gap("tokyo", name)
    for name in (
        "MEGA MECHA MAYHEM!!!",
        "WEAK ASSED CALIFORNIA ROLLIN RAIL",
        "HAMAGURI GAP",
        "TAIRAGAI GAP",
        "GYOZA GAP",
        "SHUMAI GAP",
        "CHAKINZUSHI GAP",
        "TORIGAI GAP",
        "HIDARI AOYAGI",
        "HIDARI MEN",
        "MIGI MEN",
        "MIGI AOYAGI",
        "MEN AGARI",
        "HOKKIGAI GAP",
        "AKAGAI GAP",
        "HAMO GAP",
        "KAPPA MAKI",
        "KANPACHI GAP",
        "CHUTORO MAKI",
        "TOSHIKOSHI SOBA OTOSHI",
        "AMAEBI GAP",
        "EDOMAE GAP",
        "MEJI GAP",
        "MAGURO GAP",
        "TORO GAP",
        "NIGIRI GAP",
        "TAKOYAKI GAP",
        "CHILI CHEESE OKONOMIYAKI",
        "OKONOMIYAKI GAP",
        "FUGU JUJU GAP",
        "KAME HAME GAP",
        "ZARUSOBA GAP",
        "AMAZAKE GAP",
        "SHOCHU GAP",
        "KICHIGAI KISHA GAP",
        "WARIBASHI GAP",
        "HIRAME GAP",
        "TSUBUGAI GAP",
        "SUNAGIMO GAP",
        "SUZUME GAP",
        "HASAMI GAP",
        "MOTSU GAP",
        "YAKITORI GAP",
        "TEBASAKI GAP",
        "NEGIMA GAP",
        "AGEDASHI TOFU GAP",
        "ONIGIRI GAP",
        "YAKISOBA GAP",
        "NORI MAKI GAP",
        "MIRUGAI GAP",
        "TENDON GAP",
        "FUTO MAKI GAP",
        "KATSUDON GAP",
        "UNAGIDON GAP",
        "SOMEN GAP",
        "TOSHIKOSHI SOBA GAP",
        "FUGU HARUMAKI GAP",
        "FUGU NO HONE GAP",
        "FUGU GAP",
        "BENTO BOX GAP",
        "EBI GAP",
        "SHAKO GAP",
        "KAZUNOKO GAP",
        "WEAK ASSED CALIFORNIA ROLLIN TRANSFER",
        "TRICKY ONIGIRI TRANSFER",
        "ONIGIRI LAUNCH",
        "HARUMAKI LAUNCH",
        "WUSSY HARUMAKI TRANSFER",
        "LUCKY HARUMAKI TRANSFER",
        "COCKY SUKIYAKI TRANSFER",
        "DONBURI TO DONBURI TRANSFER",
        "MOCHI AGE GAP",
        "KAIBASHIRA AGE GAP",
        "GESO KARA AGE GAP",
        "TORI KARA AGE GAP",
        "KAREI KARA AGE GAP",
        "HIRAME KARA AGE GAP",
        "FUGU NO NAKA GAP",
        "DONBURI WARI GAP",
        "HAMACHI NO MICHI RAIL",
        "HAMACHI KAMA GAP",
        "SHABU SHABU GAP",
        "DOJO NABE",
        "YANAGAWA NABE GAP",
        "UDON SUKI NABE GAP",
        "CHIRI NABE GAP",
        "TARA CHIRI NABE GAP",
        "MIZUTAKI GAP",
        "KAMO NABE GAP",
        "ANKO NABE GAP",
        "ISHIKARI NABE GAP",
        "CHANKO NABE GAP",
        "SUPPON NABE GAP",
        "INOSHISHI NABE GAP",
        "BOTAN NABE GAP",
        "SAKURA NABE GAP",
        "TORI NIKU GAP",
        "BUTA NIKU GAP",
        "GYU NIKU GAP",
    )
)

CRUISE_SHIP_GAPS: tuple[GapData, ...] = tuple(
    _gap("cruise_ship", name)
    for name in (
        "Pane in the Glass",
        "Sweet Temptation!",
        "Star Spangled Splatter",
        "God Save the Cake!",
        "Buffet 2 Fountain",
        "Up to Awning",
        "Ferry Support Shuffle",
        "Support Lines to Awning",
        "Nice Landing!",
        "To The Ferry Supports",
        "Awning Pop",
        "Aaaaaeeeiiii!",
        "Gap the Pool",
        "Spiral Slide!",
        "Spiral Staircase!",
        "Spiral Sculpture!",
        "Box-to-Box Action",
        "Box 2 808",
        "Box 2 Rail",
        "808 2 Box",
        "Rail 2 Box",
        "Atrium High Lines",
        "Ramp 2 Rail",
        "Takin' the High Road",
        "Lower Comm Lip",
        "Upper Comm Lip",
        "Air Over the Slide",
        "Pop Over the Slide",
        "Balcony Hop",
        "Railing Hop",
        "Tricky Pop!",
        "Bumper Hop",
        "Embarking",
        "Disembarking",
        "Um...",
        "A Linkin' the Chain",
        "Flag Line Hop",
        "Anchor Chain Air",
        "Blind Faith!!",
        "Drop a Deck!",
        "Drop ANOTHER Deck!!",
        "Sun Block",
        "Sun Worshipper Pop",
        "Cresting the Peaks",
        "Itsy Bitsy",
        "Teeny Weeny",
        "Purple Polka Dotted",
        "String Bikini",
        "Tan Air",
        "Lounge Clearance",
        "Chaise Cool",
        "Silicone",
        "Cherry",
        "Catchin' Wood",
        "Are those Real?",
        "Hey, My Hair!",
        "Over the Tan Line",
        "No, Don't Get Up",
        "Over the Atrium Wall",
        "Wall 2 Wall",
        "Sprinkle Yer Shorts!",
        "Over the Pillar",
        "Over the Planter",
        "Complete 808!",
        "Top o' the Atrium 2 Ya!",
        "Leaping to the Life Line",
        "Shop 'n' Pop",
        "Air Support!",
        "Crazy Lifeboat Transfer!!",
        "New Boat!",
        "Netting Sidetrack Quickie!",
        "Sure About That?",
        "Ten Point Landing",
        "Awning to Ferry Support",
        "Ride a Bit o' Slide",
        "Manual a Bit o' Slide",
        "Ride Half the Slide!",
        "Manual Half the Slide!",
        "Ride the WHOLE Slide!!",
        "Manual the WHOLE Slide!!",
        "Captain's Gap",
        "Don't Look Down!!!",
        "Down in Front!",
        "Bow Down Before Me!",
        "King of the World!",
        "Loading Deck Air",
        "Abandon Atrium!",
        "Over Comm, Comm Over!",
        "Prop Air!",
        "Shop-Side Manual",
        "Passin' Thru!",
        "Ahoy, Cap'n!",
        "Pop the Notch",
        "Sprinkler Extension",
        "Lower Glass Support",
        "Upper Glass Support!",
        "Pipe Extension",
        "Railing Stomp",
        "Gaffer's Perch",
        "The Flagline Spectacular!",
        "Wave Wall Plant",
        "Table Pop",
        "One Umbrella...",
        "Two Umbrella...",
        "Three Umbrella..!",
        "Four!!!",
    )
)

GAP_CATALOG_BY_LEVEL: dict[str, tuple[GapData, ...]] = {
    "foundry": FOUNDRY_GAPS,
    "canada": CANADA_GAPS,
    "rio": RIO_GAPS,
    "suburbia": SUBURBIA_GAPS,
    "airport": AIRPORT_GAPS,
    "skater_island": SKATER_ISLAND_GAPS,
    "los_angeles": LOS_ANGELES_GAPS,
    "tokyo": TOKYO_GAPS,
    "cruise_ship": CRUISE_SHIP_GAPS,
}

# Gaps that don't work in release 1.1 because of faulty gap scripts.
UNAVAILABLE_GAPS = {
    ("airport", "Skyin!"),
    ("skater_island", "Treasure Trip"),
    ("skater_island", "Violet's Gap"),
    ("los_angeles", "Earthquake!!!"),
    ("los_angeles", "Ped Props!"),
    ("cruise_ship", "Wall 2 Wall"),
    ("cruise_ship", "Pop Over the Slide"),
}
GAPS_BY_LEVEL = {
    level: tuple(gap for gap in gaps if (level, gap.name) not in UNAVAILABLE_GAPS)
    for level, gaps in GAP_CATALOG_BY_LEVEL.items()
}


def select_gap_checks(
    gaps: Sequence[GapData],
    percentage: int,
    rng: random.Random,
) -> tuple[GapData, ...]:
    """Select a fixed percentage of a level's gaps with the world's seeded RNG."""
    if percentage < 0 or percentage > 100:
        raise ValueError("gap percentage must be between 0 and 100")
    if percentage == 0 or not gaps:
        return ()

    count = math.ceil(len(gaps) * percentage / 100)
    return tuple(sorted(rng.sample(list(gaps), count), key=lambda gap: gap.checksum))


def select_skater(skater_names: Iterable[str], rng: random.Random) -> str:
    pool = sorted(set(skater_names), key=str.casefold)
    if not pool:
        raise ValueError("skater pool cannot be empty")
    unknown_names = set(pool) - SKATER_BY_NAME.keys()
    if unknown_names:
        raise ValueError(f"unknown skaters: {', '.join(sorted(unknown_names))}")
    return rng.choice(pool)


def select_all_gap_checks(
    percentage: int,
    rng: random.Random,
    gaps_by_level: dict[str, Sequence[GapData]] = GAPS_BY_LEVEL,
) -> tuple[GapData, ...]:
    selected: list[GapData] = []
    for level in LEVELS:
        selected.extend(select_gap_checks(gaps_by_level[level.key], percentage, rng))
    return tuple(selected)


def validate_static_data(gaps: Iterable[GapData] | None = None) -> None:
    level_keys = [level.key for level in LEVELS]
    if len(level_keys) != len(set(level_keys)):
        raise ValueError("duplicate level keys")

    level_numbers = [level.level_num for level in LEVELS]
    if len(level_numbers) != len(set(level_numbers)):
        raise ValueError("duplicate THPS3 level numbers")

    skater_names = [skater.name for skater in SKATERS]
    if len(skater_names) != len(set(skater_names)):
        raise ValueError("duplicate skater names")
    if any(skater.trick_style not in {"street", "vert"} for skater in SKATERS):
        raise ValueError("unknown skater trick style")

    goal_keys = [(goal.level_key, goal.goal_id) for goal in GOALS]
    if len(goal_keys) != len(set(goal_keys)):
        raise ValueError("duplicate goal identities")

    stat_point_keys = [
        (stat_point.level_key, stat_point.point_id) for stat_point in STAT_POINTS
    ]
    if len(stat_point_keys) != len(set(stat_point_keys)):
        raise ValueError("duplicate stat-point identities")

    deck_keys = [deck.level_key for deck in DECKS]
    if len(deck_keys) != len(set(deck_keys)):
        raise ValueError("duplicate hidden-deck identities")

    gap_values = (
        tuple(gaps)
        if gaps is not None
        else tuple(gap for level_gaps in GAPS_BY_LEVEL.values() for gap in level_gaps)
    )
    gap_keys = [(gap.level_key, gap.checksum) for gap in gap_values]
    if len(gap_keys) != len(set(gap_keys)):
        raise ValueError("duplicate gap identities")

    gap_key_set = set(gap_keys)
    gap_override_keys = (
        GAP_REQUIREMENT_OVERRIDES.keys()
        | GAP_ALL_REQUIREMENT_OVERRIDES.keys()
        | GAP_GOAL_REQUIREMENT_OVERRIDES.keys()
        | GAP_NO_REQUIREMENT_OVERRIDES
    )
    if not gap_override_keys <= gap_key_set:
        raise ValueError("requirement override references an unknown gap")
    gap_name_keys = {(gap.level_key, gap.name) for gap in gap_values}
    if GAP_REQUIREMENTS_BY_NAME.keys() != gap_name_keys:
        raise ValueError("packaged gap requirements do not match the gap catalogue")
    if any(
        (level_key, goal_id) not in GOAL_BY_LEVEL_AND_ID
        for (level_key, _), goal_ids in GAP_GOAL_REQUIREMENT_OVERRIDES.items()
        for goal_id in goal_ids
    ):
        raise ValueError("gap goal requirements must reference a goal in their level")

    if not {skater.key for skater in SKATERS} <= SKATER_LAYOUTS.keys():
        raise ValueError("packaged requirements are missing a skater layout")
    if set(OBJECTIVE_REQUIREMENTS) != set(level_keys):
        raise ValueError("objective requirements do not match the levels")
    if set(SKATE_LETTER_REQUIREMENTS) != {"1", "2", "3"}:
        raise ValueError("S-K-A-T-E requirements do not contain three layouts")
    if set(HIDDEN_DECK_REQUIREMENTS) != {"1", "2", "3"}:
        raise ValueError("hidden-deck requirements do not contain three layouts")
    if set(STAT_POINT_REQUIREMENTS) != {"1", "2", "3", "4"}:
        raise ValueError("stat-point requirements do not contain four layouts")

    trick_requirements: set[str] = set()

    def validate_requirement(requirement, level_key: str) -> None:
        if requirement is None:
            raise ValueError("unreviewed objective/stat requirement")
        if isinstance(requirement, str):
            trick_requirements.add(requirement)
        elif isinstance(requirement, list):
            for entry in requirement:
                validate_requirement(entry, level_key)
        elif isinstance(requirement, dict):
            if set(requirement) - {"any", "all", "count", "goal_id", "street", "vert"}:
                raise ValueError("unknown objective/stat requirement key")
            if "count" in requirement and not (
                1 <= requirement["count"] <= len(requirement.get("any", ()))
            ):
                raise ValueError("invalid objective/stat requirement count")
            if (
                "goal_id" in requirement
                and (level_key, requirement["goal_id"]) not in GOAL_BY_LEVEL_AND_ID
            ):
                raise ValueError(
                    "objective/stat requirement references an unknown goal"
                )
            for key in ("any", "all", "street", "vert"):
                for entry in requirement.get(key, ()):
                    validate_requirement(entry, level_key)
        else:
            raise ValueError("invalid objective/stat requirement")

    for level_key, requirements_by_name in OBJECTIVE_REQUIREMENTS.items():
        expected = {
            goal.name
            for goal in GOALS_BY_LEVEL[level_key]
            if goal.name != "Collect S-K-A-T-E"
        }
        if set(requirements_by_name) != expected:
            raise ValueError("objective requirements do not match the goals")
        for requirement in requirements_by_name.values():
            validate_requirement(requirement, level_key)
    for layouts in (SKATE_LETTER_REQUIREMENTS, HIDDEN_DECK_REQUIREMENTS):
        for requirements_by_level in layouts.values():
            for level_key, requirement in requirements_by_level.items():
                validate_requirement(requirement, level_key)
    for requirements_by_level in STAT_POINT_REQUIREMENTS.values():
        for level_key, requirements_by_name in requirements_by_level.items():
            for requirement in requirements_by_name.values():
                validate_requirement(requirement, level_key)

    gap_requirements = (
        requirement
        for gap in gap_values
        for requirement in (
            *gap.required_trick_items,
            *gap.required_all_trick_items,
        )
    )
    if not trick_requirements | set(gap_requirements) <= set(TRICK_CATEGORY_ITEMS):
        raise ValueError("unknown trick-category requirement")


validate_static_data()
