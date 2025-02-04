from BaseClasses import Region

from ..base_classes import Q1Level


class E3M3(Q1Level):
    name = "The Tomb of Terror"
    mapfile = "e3m3"
    keys = ["Silver"]
    location_defs = [
        {
            "id": 1,
            "name": "Shells (1)",
            "classname": "item_shells",
            "uuid": 15458790294150385629,
            "density": 0,
        },
        {
            "id": 2,
            "name": "Large Medkit (2)",
            "classname": "item_health",
            "uuid": 108378633608109802,
            "density": 3,
        },
        {
            "id": 3,
            "name": "Spikes (3)",
            "classname": "item_spikes",
            "uuid": 7702488720961186462,
            "density": 0,
        },
        {
            "id": 4,
            "name": "Large Medkit (4)",
            "classname": "item_health",
            "uuid": 9028457035131353062,
            "density": 1,
        },
        {
            "id": 5,
            "name": "Large Medkit (5)",
            "classname": "item_health",
            "uuid": 16225605479225794449,
            "density": 3,
        },
        {
            "id": 6,
            "name": "Shells (6)",
            "classname": "item_shells",
            "uuid": 8933026983423145579,
            "density": 1,
        },
        {
            "id": 7,
            "name": "Shells (7)",
            "classname": "item_shells",
            "uuid": 7734381793887951756,
            "density": 1,
        },
        {
            "id": 8,
            "name": "Silver Key (8)",
            "classname": "item_key1",
            "uuid": 7970936057708470485,
            "density": 0,
        },
        {
            "id": 9,
            "name": "Megahealth (9)",
            "classname": "item_health",
            "uuid": 13492835010153385729,
            "density": 2,
        },
        {
            "id": 10,
            "name": "Large Medkit (10)",
            "classname": "item_health",
            "uuid": 9789017994924715194,
            "density": 0,
        },
        {
            "id": 11,
            "name": "Large Medkit (11)",
            "classname": "item_health",
            "uuid": 15266126129233875463,
            "density": 1,
        },
        {
            "id": 12,
            "name": "Shells (12)",
            "classname": "item_shells",
            "uuid": 6350674749292620541,
            "density": 0,
        },
        {
            "id": 13,
            "name": "Large Medkit (13)",
            "classname": "item_health",
            "uuid": 11360088957167102328,
            "density": 4,
        },
        {
            "id": 14,
            "name": "Large Medkit (14)",
            "classname": "item_health",
            "uuid": 12738170438827125613,
            "density": 3,
        },
        {
            "id": 15,
            "name": "Large Medkit (15)",
            "classname": "item_health",
            "uuid": 1127568305662854371,
            "density": 3,
        },
        {
            "id": 16,
            "name": "Exit",
            "classname": "trigger_changelevel",
            "uuid": 7088288719396417441,
            "density": 0,
        },
        {
            "id": 17,
            "name": "Secret (17)",
            "classname": "trigger_secret",
            "uuid": 17763144484288875019,
            "density": 0,
        },
        {
            "id": 18,
            "name": "Red Armor (18)",
            "classname": "item_armorInv",
            "uuid": 9472413720624382010,
            "density": 0,
        },
        {
            "id": 19,
            "name": "Large Medkit (19)",
            "classname": "item_health",
            "uuid": 13888097031883314642,
            "density": 0,
        },
        {
            "id": 20,
            "name": "Megahealth (20)",
            "classname": "item_health",
            "uuid": 8877300386703782167,
            "density": 0,
        },
        {
            "id": 21,
            "name": "Supernailgun (21)",
            "classname": "weapon_supernailgun",
            "uuid": 11170694437342959678,
            "density": 0,
        },
        {
            "id": 22,
            "name": "Rocketlauncher (22)",
            "classname": "weapon_rocketlauncher",
            "uuid": 13275795400728488045,
            "density": 5,
        },
        {
            "id": 23,
            "name": "Secret (23)",
            "classname": "trigger_secret",
            "uuid": 7606530785663140553,
            "density": 0,
        },
        {
            "id": 24,
            "name": "Large Medkit (24)",
            "classname": "item_health",
            "uuid": 12953359096075534655,
            "density": 4,
        },
        {
            "id": 25,
            "name": "Large Medkit (25)",
            "classname": "item_health",
            "uuid": 14386251358879726169,
            "density": 4,
        },
        {
            "id": 26,
            "name": "Invisibility (26)",
            "classname": "item_artifact_invisibility",
            "uuid": 15964532781884271991,
            "density": 5,
        },
        {
            "id": 27,
            "name": "Nailgun (27)",
            "classname": "weapon_nailgun",
            "uuid": 3813475103751774505,
            "density": 5,
        },
        {
            "id": 28,
            "name": "Rocketlauncher (28)",
            "classname": "weapon_rocketlauncher",
            "uuid": 427162540671871411,
            "density": 5,
        },
        {
            "id": 29,
            "name": "Yellow Armor (29)",
            "classname": "item_armor2",
            "uuid": 12331287903641196134,
            "density": 5,
        },
        {
            "id": 30,
            "name": "Yellow Armor (30)",
            "classname": "item_armor2",
            "uuid": 15513927851306889788,
            "density": 0,
        },
        {
            "id": 31,
            "name": "Small Medkit (31)",
            "classname": "item_health",
            "uuid": 10569620697868590149,
            "density": 1,
        },
        {
            "id": 32,
            "name": "Small Medkit (32)",
            "classname": "item_health",
            "uuid": 1124263723772076335,
            "density": 3,
        },
        {
            "id": 33,
            "name": "Rockets (33)",
            "classname": "item_rockets",
            "uuid": 16535079629668878005,
            "density": 4,
        },
        {
            "id": 34,
            "name": "Spikes (34)",
            "classname": "item_spikes",
            "uuid": 11821739960788987310,
            "density": 3,
        },
        {
            "id": 35,
            "name": "Spikes (35)",
            "classname": "item_spikes",
            "uuid": 14746852844891602031,
            "density": 4,
        },
        {
            "id": 36,
            "name": "Supershotgun (36)",
            "classname": "weapon_supershotgun",
            "uuid": 904419384178674083,
            "density": 5,
        },
        {
            "id": 37,
            "name": "Small Medkit (37)",
            "classname": "item_health",
            "uuid": 18147714042563107309,
            "density": 0,
        },
        {
            "id": 38,
            "name": "Small Medkit (38)",
            "classname": "item_health",
            "uuid": 3037754555076668836,
            "density": 1,
        },
        {
            "id": 39,
            "name": "Spikes (39)",
            "classname": "item_spikes",
            "uuid": 10280043091407260716,
            "density": 3,
        },
        {
            "id": 40,
            "name": "Rockets (40)",
            "classname": "item_rockets",
            "uuid": 15461058413757500333,
            "density": 1,
        },
        {
            "id": 41,
            "name": "Small Medkit (41)",
            "classname": "item_health",
            "uuid": 15073684570173534564,
            "density": 1,
        },
        {
            "id": 42,
            "name": "Spikes (42)",
            "classname": "item_spikes",
            "uuid": 6447850111615184924,
            "density": 3,
        },
        {
            "id": 43,
            "name": "Spikes (43)",
            "classname": "item_spikes",
            "uuid": 4876006873026341411,
            "density": 3,
        },
        {
            "id": 44,
            "name": "Rockets (44)",
            "classname": "item_rockets",
            "uuid": 13914722555823997559,
            "density": 0,
        },
        {
            "id": 45,
            "name": "Spikes (45)",
            "classname": "item_spikes",
            "uuid": 2058307782453061548,
            "density": 4,
        },
        {
            "id": 46,
            "name": "Spikes (46)",
            "classname": "item_spikes",
            "uuid": 12305248103545853469,
            "density": 0,
        },
        {
            "id": 47,
            "name": "Shells (47)",
            "classname": "item_shells",
            "uuid": 4082658922365688805,
            "density": 1,
        },
        {
            "id": 48,
            "name": "Large Medkit (48)",
            "classname": "item_health",
            "uuid": 13198831767491158688,
            "density": 1,
        },
        {
            "id": 49,
            "name": "Spikes (49)",
            "classname": "item_spikes",
            "uuid": 2350118028436562984,
            "density": 1,
        },
        {
            "id": 50,
            "name": "Spikes (50)",
            "classname": "item_spikes",
            "uuid": 10261353040796476554,
            "density": 1,
        },
        {
            "id": 51,
            "name": "Spikes (51)",
            "classname": "item_spikes",
            "uuid": 8833286139119392623,
            "density": 4,
        },
        {
            "id": 52,
            "name": "Shells (52)",
            "classname": "item_shells",
            "uuid": 11214826752766912473,
            "density": 3,
        },
        {
            "id": 53,
            "name": "Shells (53)",
            "classname": "item_shells",
            "uuid": 2375797021030138253,
            "density": 4,
        },
        {
            "id": 54,
            "name": "Shells (54)",
            "classname": "item_shells",
            "uuid": 685782732854508522,
            "density": 0,
        },
        {
            "id": 55,
            "name": "Supershotgun (55)",
            "classname": "weapon_supershotgun",
            "uuid": 714889770821926920,
            "density": 5,
        },
        {
            "id": 56,
            "name": "Grenadelauncher (56)",
            "classname": "weapon_grenadelauncher",
            "uuid": 15493846133547784883,
            "density": 5,
        },
        {
            "id": 57,
            "name": "Rockets (57)",
            "classname": "item_rockets",
            "uuid": 8207248540795749559,
            "density": 0,
        },
        {
            "id": 58,
            "name": "Spikes (58)",
            "classname": "item_spikes",
            "uuid": 3064504696268474675,
            "density": 0,
        },
        {
            "id": 59,
            "name": "Green Armor (59)",
            "classname": "item_armor1",
            "uuid": 2614788019587439520,
            "density": 0,
        },
    ]

    def main_region(self) -> Region:
        r = self.rules

        ret = self.region(
            self.name,
            [
                "Large Medkit (2)",
                "Spikes (49)",
                "Shells (1)",
            ],
        )

        past_button_area = self.region(
            "Past Button",
            [
                "Yellow Armor (30)",
                "Small Medkit (31)",
                "Small Medkit (32)",
                "Supernailgun (21)",
                "Shells (7)",
                "Spikes (35)",
                "Spikes (34)",
                "Shells (6)",
                "Rockets (57)",
                "Supershotgun (36)",
                "Small Medkit (37)",
                "Small Medkit (38)",
                "Spikes (43)",
                "Large Medkit (24)",
                "Large Medkit (25)",
                "Shells (12)",
                "Rockets (40)",
                "Spikes (39)",
                "Grenadelauncher (56)",
                "Large Medkit (11)",
                "Large Medkit (10)",
                "Rockets (33)",
                "Large Medkit (5)",
                "Secret (23)",
                "Megahealth (9)",
                "Spikes (3)",
                "Large Medkit (4)",
            ],
        )
        self.connect(ret, past_button_area, r.can_button)
        self.restrict("Spikes (3)", r.can_door)
        self.restrict("Large Medkit (4)", r.can_door)
        self.restrict("Secret (23)", r.can_dive)
        self.restrict("Megahealth (9)", r.can_dive)

        lava_secret_area = self.region(
            "Lava Secret",
            [
                "Secret (17)",
                "Rocketlauncher (22)",
                "Red Armor (18)",
            ],
        )
        self.connect(
            past_button_area,
            lava_secret_area,
            r.can_shootswitch | (r.bigjump & r.difficulty("hard")),
        )
        self.restrict("Secret (17)", r.can_shootswitch)

        start_upper_area = self.region(
            "Start Upper",
            [
                "Megahealth (20)",
                "Nailgun (27)",
            ],
        )
        self.connect(ret, start_upper_area, r.bigjump & r.difficulty("hard"))
        self.connect(past_button_area, start_upper_area, r.can_door)

        past_lava_area = self.region(
            "Past Lava",
            [
                "Spikes (42)",
                "Small Medkit (41)",
                "Silver Key (8)",
                "Invisibility (26)",
            ],
        )
        self.connect(start_upper_area, past_lava_area, r.can_button)

        past_silver_door_area = self.region(
            "Past Silver Door",
            [
                "Large Medkit (13)",
                "Large Medkit (14)",
                "Spikes (50)",
                "Rockets (44)",
                "Shells (54)",
                "Supershotgun (55)",
                "Shells (52)",
                "Spikes (45)",
                "Spikes (46)",
            ],
        )
        self.connect(ret, past_silver_door_area, self.silver_key)

        past_silver_button = self.region(
            "Past Silver Button",
            [
                "Shells (53)",
                "Spikes (51)",
                "Large Medkit (15)",
                "Large Medkit (19)",
                "Spikes (58)",
                "Shells (47)",
                "Yellow Armor (29)",
                "Large Medkit (48)",
                "Green Armor (59)",
                "Exit",
            ],
        )
        self.connect(past_silver_door_area, past_silver_button, r.can_button)

        return ret
