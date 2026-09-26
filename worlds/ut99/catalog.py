"""Stable IDs: append entries."""
import json
from pathlib import Path
from pkgutil import get_data

GAME = "Unreal Tournament 99"
SCHEMA_VERSION = 11
ITEM_BASE = 19990000
LOCATION_BASE = 19991000
PICKUP_BASE = 19996000
TEAM_FRAG_BASE = 20001000
DM_MAPS = (
    "DM-Oblivion", "DM-Stalwart", "DM-Fractal", "DM-Turbine", "DM-Codex",
    "DM-Pressure", "DM-Grinder", "DM-KGalleon", "DM-Tempest", "DM-Barricade",
    "DM-Liandri", "DM-Conveyor", "DM-Peak", "DM-HyperBlast", "DM-Deck16][",
    "DM-Curse][", "DM-Morpheus", "DM-Phobos", "DM-Fetid", "DM-StalwartXL",
    "DM-Zeto", "DM-Gothic",
    "DM-Agony", "DM-ArcaneTemple", "DM-Bishop", "DM-Closer", "DM-Crane",
    "DM-Cybrosis][", "DM-Grit-TOURNEY", "DM-HealPod][", "DM-Malevolence", "DM-Mojo][",
    "DM-Morbias][", "DM-Pyramid", "DM-Shrapnel][", "DM-SpaceNoxx", "DM-Viridian-TOURNEY",
)
CTF_MAPS = (
    "CTF-Beatitude", "CTF-Command", "CTF-Coret", "CTF-Cybrosis][", "CTF-Darji16",
    "CTF-Dreary", "CTF-EpicBoy", "CTF-EternalCave", "CTF-Face", "CTF-Face-SE",
    "CTF-Face][", "CTF-Gauntlet", "CTF-HallOfGiants", "CTF-High", "CTF-Hydro16",
    "CTF-Kosov", "CTF-LavaGiant", "CTF-Niven", "CTF-November", "CTF-Noxion16",
    "CTF-Nucleus", "CTF-Orbital", "CTF-Ratchet",
)
DOM_MAPS = (
    "DOM-Bullet", "DOM-Cidom", "DOM-Cinder", "DOM-Condemned", "DOM-Cryptic",
    "DOM-Cybrosis][", "DOM-Gearbolt", "DOM-Ghardhen", "DOM-Lament", "DOM-Lament][",
    "DOM-Leadworks", "DOM-MetalDream", "DOM-Olden", "DOM-Sesmar", "DOM-WolfsBay",
)
AS_MAPS = ("AS-Frigate", "AS-Guardia", "AS-HiSpeed", "AS-Mazon", "AS-OceanFloor",
           "AS-Overlord", "AS-Rook")
MAPS = DM_MAPS + CTF_MAPS + DOM_MAPS + AS_MAPS
ASSAULT_OBJECTIVES = {
    "AS-Frigate": (("FortStandard0", "The Missiles"), ("FortStandard1", "The Ship"),
                   ("FortStandard2", "The Hydraulic Compressor")),
    "AS-Guardia": (("FortStandard0", "The Lava Bridge"), ("FortStandard1", "The Fuse"),
                   ("FortStandard2", "The Garage Door"), ("FortStandard3", "The Tank Turret"),
                   ("FortStandard4", "The Cavern")),
    "AS-HiSpeed": (("FortStandard0", "The Control Cabin"), ("FortStandard1", "The CAR 3"),
                   ("FortStandard2", "The CAR 2"), ("FortStandard3", "The CAR 1"),
                   ("FortStandard4", "The Control Cabin Access Switch")),
    "AS-Mazon": (("FortStandard0", "The Front Doors"), ("FortStandard1", "The Chain 2"),
                 ("FortStandard2", "The Chain 1"), ("FortStandard5", "The Crystal"),
                 ("FortStandard6", "The Reactor Room Doors")),
    "AS-OceanFloor": (("FortStandard0", "The Terminal 3"), ("FortStandard1", "The Terminal 1"),
                      ("FortStandard2", "The Terminal 2"), ("FortStandard3", "The Terminal 4")),
    "AS-Overlord": (("FortStandard0", "The Beachhead"), ("FortStandard3", "Assault Target"),
                    ("FortStandard4", "The Boiler Room")),
    "AS-Rook": (("FortStandard0", "Objective 1"), ("FortStandard1", "Objective 2"),
                ("FortStandard2", "The Main Doors"), ("FortStandard3", "Objective 3"),
                ("FortStandard6", "The Library")),
}


def objective_labels(name, frag_checks=100):
    if name in DM_MAPS:
        return [f"Frag Milestone {i}" for i in range(1, frag_checks + 1)]
    if name in CTF_MAPS:
        return [f"Capture {i}" for i in range(1, 4)]
    if name in DOM_MAPS:
        return [f"Score {i * 25}" for i in range(1, 5)]
    return [f"Objective {label}" for _, label in ASSAULT_OBJECTIVES[name]]
WEAPONS = (
    ("Shock Rifle", "Botpack.ShockRifle"),
    ("Bio Rifle", "Botpack.UT_BioRifle"),
    ("Pulse Gun", "Botpack.PulseGun"),
    ("Ripper", "Botpack.Ripper"),
    ("Minigun", "Botpack.Minigun2"),
    ("Flak Cannon", "Botpack.UT_FlakCannon"),
    ("Rocket Launcher", "Botpack.UT_Eightball"),
    ("Sniper Rifle", "Botpack.SniperRifle"),
    ("Redeemer", "Botpack.WarheadLauncher"),
)
AMMO_FILLERS = (
    ("+2 Shock Cores", 2, "Botpack.ShockCore"),
    ("+5 Biosludge", 5, "Botpack.BioAmmo"),
    ("+5 Pulse Cells", 5, "Botpack.PAmmo"),
    ("+5 Razor Blades", 5, "Botpack.BladeHopper"),
    ("+10 Bullets", 10, "Botpack.MiniAmmo"),
    ("+2 Flak Shells", 2, "Botpack.FlakAmmo"),
    ("+2 Rockets", 2, "Botpack.RocketPack"),
    ("+2 Rifle Rounds", 2, "Botpack.BulletBox"),
    ("+1 Redeemer Missile", 1, "Botpack.WarHeadAmmo"),
)
PICKUP_FAMILIES = ("Health", "Mega Health", "Armor", "Damage Amplifier",
                   "Invisibility", "Jump Boots", "Trap", "Special Pickup")
PICKUP_CLASS_FAMILY = {key.lower(): family for key, family in {
    "Botpack.ShockRifle": "Shock Rifle", "Botpack.ShockCore": "Shock Rifle",
    "Botpack.ut_biorifle": "Bio Rifle", "Botpack.bioammo": "Bio Rifle",
    "Botpack.PulseGun": "Pulse Gun", "Botpack.PAmmo": "Pulse Gun",
    "Botpack.ripper": "Ripper", "Botpack.BladeHopper": "Ripper",
    "Botpack.Minigun2": "Minigun", "Botpack.Miniammo": "Minigun",
    "Botpack.UT_FlakCannon": "Flak Cannon", "Botpack.flakammo": "Flak Cannon",
    "Botpack.UT_Eightball": "Rocket Launcher", "Botpack.RocketPack": "Rocket Launcher",
    "Botpack.SniperRifle": "Sniper Rifle", "Botpack.BulletBox": "Sniper Rifle",
    "Botpack.RifleShell": "Sniper Rifle", "Botpack.WarheadLauncher": "Redeemer",
    "Botpack.MedBox": "Health", "Botpack.HealthVial": "Health",
    "Botpack.HealthPack": "Mega Health",
    "Botpack.armor2": "Armor", "Botpack.ThighPads": "Armor",
    "Botpack.UT_ShieldBelt": "Armor", "Botpack.UDamage": "Damage Amplifier",
    "Botpack.UT_invisibility": "Invisibility", "Botpack.ut_jumpboots": "Jump Boots",
    "Botpack.TrapSpringer": "Trap", "Botpack.TournamentPickup": "Special Pickup",
    "Botpack.Enforcer": "Special Pickup", "Botpack.EClip": "Special Pickup",
    "UnrealShare.ScubaGear": "Special Pickup",
}.items()}
PICKUP_TYPE_LABELS = {key.lower(): label for key, label in {
    "Botpack.ShockRifle": "Shock Rifle", "Botpack.ShockCore": "Shock Core",
    "Botpack.ut_biorifle": "Bio Rifle", "Botpack.bioammo": "Bio Ammo",
    "Botpack.PulseGun": "Pulse Gun", "Botpack.PAmmo": "Pulse Ammo",
    "Botpack.ripper": "Ripper", "Botpack.BladeHopper": "Razor Blades",
    "Botpack.Minigun2": "Minigun", "Botpack.Miniammo": "Minigun Ammo",
    "Botpack.UT_FlakCannon": "Flak Cannon", "Botpack.flakammo": "Flak Ammo",
    "Botpack.UT_Eightball": "Rocket Launcher", "Botpack.RocketPack": "Rocket Pack",
    "Botpack.SniperRifle": "Sniper Rifle", "Botpack.BulletBox": "Rifle Ammo Box",
    "Botpack.RifleShell": "Rifle Round", "Botpack.WarheadLauncher": "Redeemer",
    "Botpack.MedBox": "Med Box", "Botpack.HealthVial": "Health Vial",
    "Botpack.HealthPack": "Super Health",
    "Botpack.armor2": "Body Armor", "Botpack.ThighPads": "Thigh Pads",
    "Botpack.UT_ShieldBelt": "Shield Belt", "Botpack.UDamage": "Damage Amplifier",
    "Botpack.UT_invisibility": "Invisibility", "Botpack.ut_jumpboots": "Jump Boots",
    "Botpack.TrapSpringer": "Trap Springer", "Botpack.TournamentPickup": "Tournament Pickup",
    "Botpack.Enforcer": "Enforcer", "Botpack.EClip": "Enforcer Clip",
    "UnrealShare.ScubaGear": "Scuba Gear",
}.items()}
PICKUP_TYPE_CLASSES = tuple(PICKUP_CLASS_FAMILY)
PICKUP_TYPE_NAMES = tuple(PICKUP_TYPE_LABELS[classname] + " Pickup Unlock"
                          for classname in PICKUP_TYPE_CLASSES)
ITEM_NAME_TO_ID = {f"{name} Unlock": ITEM_BASE + i for i, name in enumerate(MAPS)}
ITEM_NAME_TO_ID.update({f"{name} Unlock": ITEM_BASE + 100 + i
                        for i, (name, _) in enumerate(WEAPONS)})
ITEM_NAME_TO_ID.update({f"{name} Unlock": ITEM_BASE + 300 + i
                        for i, name in enumerate(PICKUP_FAMILIES)})
ITEM_NAME_TO_ID.update({name: ITEM_BASE + 400 + i
                        for i, name in enumerate(PICKUP_TYPE_NAMES)})
ITEM_NAME_TO_ID.update({"Health Refill": ITEM_BASE + 201,
                        "Armor Refill": ITEM_BASE + 202})
ITEM_NAME_TO_ID.update({name: ITEM_BASE + 204 + i
                        for i, (name, _, _) in enumerate(AMMO_FILLERS)})
LOCATION_NAME_TO_ID = {
    f"{name} - Win": LOCATION_BASE + i * 101
    for i, name in enumerate(DM_MAPS)
}
LOCATION_NAME_TO_ID.update({
    f"{name} - Frag Milestone {step}": LOCATION_BASE + i * 101 + step
    for i, name in enumerate(DM_MAPS)
    for step in range(1, 101)
})
for i, name in enumerate(MAPS[len(DM_MAPS):], len(DM_MAPS)):
    base = LOCATION_BASE + len(DM_MAPS) * 101 + (i - len(DM_MAPS)) * 20
    LOCATION_NAME_TO_ID[f"{name} - Win"] = base
    LOCATION_NAME_TO_ID.update({f"{name} - {label}": base + step
                                for step, label in enumerate(objective_labels(name), 1)})
    LOCATION_NAME_TO_ID.update({
        f"{name} - Frag Milestone {step}": TEAM_FRAG_BASE + (i - len(DM_MAPS)) * 101 + step
        for step in range(1, 101)
    })
PICKUPS = json.loads(get_data(__package__, "pickups.json") if __package__
                     else Path(__file__).with_name("pickups.json").read_bytes())
assert {pickup["class"].lower() for pickup in PICKUPS} == set(PICKUP_CLASS_FAMILY)
assert set(PICKUP_TYPE_LABELS) == set(PICKUP_CLASS_FAMILY)
PICKUP_NAMES = [f"{MAPS[p['map']]} - Pickup {p['actor']}" for p in PICKUPS]
LOCATION_NAME_TO_ID.update({name: PICKUP_BASE + i for i, name in enumerate(PICKUP_NAMES)})
