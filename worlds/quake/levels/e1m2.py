from BaseClasses import Region

from ..base_classes import Q1Level


class E1M2(Q1Level):
    name = "Castle Of The Damned"
    mapfile = "e1m2"
    keys = ["Silver"]
    location_defs = [
        {
            "id": 1,
            "name": "Large Medkit (1)",
            "classname": "item_health",
            "uuid": 1409029857405709812,
            "density": 0,
        },
        {
            "id": 2,
            "name": "Shells (2)",
            "classname": "item_shells",
            "uuid": 2433775846149071001,
            "density": 1,
        },
        {
            "id": 3,
            "name": "Small Medkit (3)",
            "classname": "item_health",
            "uuid": 4105132447142659826,
            "density": 3,
        },
        {
            "id": 4,
            "name": "Small Medkit (4)",
            "classname": "item_health",
            "uuid": 4629238764012756291,
            "density": 4,
        },
        {
            "id": 5,
            "name": "Shells (5)",
            "classname": "item_shells",
            "uuid": 3604086654854443495,
            "density": 3,
        },
        {
            "id": 6,
            "name": "Shells (6)",
            "classname": "item_shells",
            "uuid": 14872053162631078997,
            "density": 0,
        },
        {
            "id": 7,
            "name": "Large Medkit (7)",
            "classname": "item_health",
            "uuid": 11228783866952304614,
            "density": 3,
        },
        {
            "id": 8,
            "name": "Shells (8)",
            "classname": "item_shells",
            "uuid": 12868255636777211477,
            "density": 0,
        },
        {
            "id": 9,
            "name": "Small Medkit (9)",
            "classname": "item_health",
            "uuid": 15365426050422635064,
            "density": 3,
        },
        {
            "id": 10,
            "name": "Small Medkit (10)",
            "classname": "item_health",
            "uuid": 5258178309457803174,
            "density": 4,
        },
        {
            "id": 11,
            "name": "Large Medkit (11)",
            "classname": "item_health",
            "uuid": 15377291529512861021,
            "density": 0,
        },
        {
            "id": 12,
            "name": "Shells (12)",
            "classname": "item_shells",
            "uuid": 16151136218961990525,
            "density": 3,
        },
        {
            "id": 13,
            "name": "Small Medkit (13)",
            "classname": "item_health",
            "uuid": 6003784234319407475,
            "density": 0,
        },
        {
            "id": 14,
            "name": "Small Medkit (14)",
            "classname": "item_health",
            "uuid": 1414159706696452461,
            "density": 1,
        },
        {
            "id": 15,
            "name": "Large Medkit (15)",
            "classname": "item_health",
            "uuid": 449902422361958447,
            "density": 1,
        },
        {
            "id": 16,
            "name": "Large Medkit (16)",
            "classname": "item_health",
            "uuid": 11676127693424011386,
            "density": 2,
        },
        {
            "id": 17,
            "name": "Silver Key (17)",
            "classname": "item_key1",
            "uuid": 17699975139733900493,
            "density": 0,
        },
        {
            "id": 18,
            "name": "Yellow Armor (18)",
            "classname": "item_armor2",
            "uuid": 2871137869114253747,
            "density": 0,
        },
        {
            "id": 19,
            "name": "Small Medkit (19)",
            "classname": "item_health",
            "uuid": 5023982601909374826,
            "density": 4,
        },
        {
            "id": 20,
            "name": "Small Medkit (20)",
            "classname": "item_health",
            "uuid": 15349181839504805968,
            "density": 3,
        },
        {
            "id": 21,
            "name": "Small Medkit (21)",
            "classname": "item_health",
            "uuid": 17582347477907818309,
            "density": 1,
        },
        {
            "id": 22,
            "name": "Large Medkit (22)",
            "classname": "item_health",
            "uuid": 13126360092107807849,
            "density": 0,
        },
        {
            "id": 23,
            "name": "Large Medkit (23)",
            "classname": "item_health",
            "uuid": 13887596127428986716,
            "density": 4,
        },
        {
            "id": 24,
            "name": "Shells (24)",
            "classname": "item_shells",
            "uuid": 1382298795613558041,
            "density": 1,
        },
        {
            "id": 25,
            "name": "Shells (25)",
            "classname": "item_shells",
            "uuid": 8847698388556907262,
            "density": 1,
        },
        {
            "id": 26,
            "name": "Large Medkit (26)",
            "classname": "item_health",
            "uuid": 429110477834272982,
            "density": 3,
        },
        {
            "id": 27,
            "name": "Large Medkit (27)",
            "classname": "item_health",
            "uuid": 3241051768267496314,
            "density": 0,
        },
        {
            "id": 28,
            "name": "Small Medkit (28)",
            "classname": "item_health",
            "uuid": 16772449277553423739,
            "density": 1,
        },
        {
            "id": 29,
            "name": "Small Medkit (29)",
            "classname": "item_health",
            "uuid": 11071959234583589871,
            "density": 3,
        },
        {
            "id": 30,
            "name": "Large Medkit (30)",
            "classname": "item_health",
            "uuid": 18074326311466837808,
            "density": 2,
        },
        {
            "id": 31,
            "name": "Large Medkit (31)",
            "classname": "item_health",
            "uuid": 16768496114949115526,
            "density": 3,
        },
        {
            "id": 32,
            "name": "Shells (32)",
            "classname": "item_shells",
            "uuid": 15801006067271169401,
            "density": 4,
        },
        {
            "id": 33,
            "name": "Supershotgun (33)",
            "classname": "weapon_supershotgun",
            "uuid": 17757147278524920955,
            "density": 0,
        },
        {
            "id": 34,
            "name": "Shells (34)",
            "classname": "item_shells",
            "uuid": 9195137752836611481,
            "density": 0,
        },
        {
            "id": 35,
            "name": "Exit",
            "classname": "trigger_changelevel",
            "uuid": 2335171492410132488,
            "density": 0,
        },
        {
            "id": 36,
            "name": "Rocketlauncher (36)",
            "classname": "weapon_rocketlauncher",
            "uuid": 10195510468093458094,
            "density": 5,
        },
        {
            "id": 37,
            "name": "Nailgun (37)",
            "classname": "weapon_nailgun",
            "uuid": 17991593787240340270,
            "density": 5,
        },
        {
            "id": 38,
            "name": "Supernailgun (38)",
            "classname": "weapon_supernailgun",
            "uuid": 6055691930219534780,
            "density": 5,
        },
        {
            "id": 39,
            "name": "Megahealth (39)",
            "classname": "item_health",
            "uuid": 7298841465347289325,
            "density": 5,
        },
        {
            "id": 40,
            "name": "Spikes (40)",
            "classname": "item_spikes",
            "uuid": 2103499210758252252,
            "density": 5,
        },
        {
            "id": 41,
            "name": "Spikes (41)",
            "classname": "item_spikes",
            "uuid": 13076891737070974975,
            "density": 5,
        },
        {
            "id": 42,
            "name": "Spikes (42)",
            "classname": "item_spikes",
            "uuid": 1581320588989726960,
            "density": 5,
        },
        {
            "id": 43,
            "name": "Spikes (43)",
            "classname": "item_spikes",
            "uuid": 2189043739878260738,
            "density": 5,
        },
        {
            "id": 44,
            "name": "Large Medkit (44)",
            "classname": "item_health",
            "uuid": 14657441240802175488,
            "density": 4,
        },
        {
            "id": 45,
            "name": "Small Medkit (45)",
            "classname": "item_health",
            "uuid": 4660445621846511594,
            "density": 0,
        },
        {
            "id": 46,
            "name": "Green Armor (46)",
            "classname": "item_armor1",
            "uuid": 10385944785279750657,
            "density": 0,
        },
        {
            "id": 47,
            "name": "Secret (47)",
            "classname": "trigger_secret",
            "uuid": 14512101561927784164,
            "density": 0,
        },
        {
            "id": 48,
            "name": "Secret (48)",
            "classname": "trigger_secret",
            "uuid": 6916474007411299166,
            "density": 0,
        },
        {
            "id": 49,
            "name": "Spikes (49)",
            "classname": "item_spikes",
            "uuid": 4818965855266913306,
            "density": 0,
        },
        {
            "id": 50,
            "name": "Spikes (50)",
            "classname": "item_spikes",
            "uuid": 4529151902918910349,
            "density": 3,
        },
        {
            "id": 51,
            "name": "Spikes (51)",
            "classname": "item_spikes",
            "uuid": 10155472878782860033,
            "density": 3,
        },
        {
            "id": 52,
            "name": "Rockets (52)",
            "classname": "item_rockets",
            "uuid": 14375970658261781045,
            "density": 5,
        },
        {
            "id": 53,
            "name": "Spikes (53)",
            "classname": "item_spikes",
            "uuid": 2316698005752648022,
            "density": 4,
        },
        {
            "id": 54,
            "name": "Shells (54)",
            "classname": "item_shells",
            "uuid": 9932649564319371585,
            "density": 4,
        },
        {
            "id": 55,
            "name": "Spikes (55)",
            "classname": "item_spikes",
            "uuid": 5741606930160855063,
            "density": 1,
        },
        {
            "id": 56,
            "name": "Shells (56)",
            "classname": "item_shells",
            "uuid": 3538479015880972349,
            "density": 0,
        },
        {
            "id": 57,
            "name": "Grenadelauncher (57)",
            "classname": "weapon_grenadelauncher",
            "uuid": 16099357754105827822,
            "density": 5,
        },
        {
            "id": 58,
            "name": "Rockets (58)",
            "classname": "item_rockets",
            "uuid": 2791322477650624308,
            "density": 5,
        },
        {
            "id": 59,
            "name": "Secret (59)",
            "classname": "trigger_secret",
            "uuid": 12723690712667282411,
            "density": 0,
        },
        {
            "id": 60,
            "name": "Quad Damage (60)",
            "classname": "item_artifact_super_damage",
            "uuid": 13600214693885068131,
            "density": 2,
        },
        {
            "id": 61,
            "name": "Spikes (61)",
            "classname": "item_spikes",
            "uuid": 14017430481648715413,
            "density": 1,
        },
        {
            "id": 62,
            "name": "Large Medkit (62)",
            "classname": "item_health",
            "uuid": 8786697592565361024,
            "density": 3,
        },
        {
            "id": 63,
            "name": "Supernailgun (63)",
            "classname": "weapon_supernailgun",
            "uuid": 697882699754131839,
            "density": 5,
        },
    ]

    events = ["Bridge Moved", "Bridge Door Open"]

    def main_region(self) -> Region:
        r = self.rules

        ret = self.region(
            self.name,
            [
                "Small Medkit (28)",
                "Small Medkit (29)",
                "Spikes (41)",
                "Spikes (42)",
                "Spikes (43)",
                "Shells (8)",
                "Nailgun (37)",
                "Large Medkit (1)",
                "Shells (2)",
                "Small Medkit (3)",
                "Small Medkit (4)",
                "Supershotgun (33)",
                "Shells (54)",
                "Shells (5)",
                "Large Medkit (44)",
                "Shells (6)",
                "Large Medkit (7)",
                "Small Medkit (10)",
                "Small Medkit (9)",
                "Shells (56)",
                "Spikes (61)",
                "Supernailgun (63)",
                "Large Medkit (62)",
                "Large Medkit (15)",
                "Green Armor (46)",
                "Yellow Armor (18)",
            ],
        )
        self.restrict(
            "Yellow Armor (18)",
            (r.jump & r.can_shootswitch)
            | (r.can_jump & (r.can_gj_hard | r.can_rj_hard)),
        )
        self.restrict("Large Medkit (15)", r.jump | r.can_door)
        self.restrict("Green Armor (46)", r.jump | r.can_door)

        past_first_doors = self.region(
            "Past First Door Area",
            [
                "Secret (48)",
                "Large Medkit (16)",
                "Spikes (50)",
                "Small Medkit (45)",
                "Spikes (51)",
                "Grenadelauncher (57)",
                "Bridge Moved",
            ],
        )
        self.connect(ret, past_first_doors, r.can_door)
        self.restrict("Bridge Moved", r.can_button)

        bridge_door_area = self.region(
            "Bridge Door Area",
            [
                "Bridge Door Open",
                "Silver Key (17)",
                "Rockets (58)",
            ],
        )
        self.connect(ret, bridge_door_area)

        self.restrict(
            "Bridge Door Open",
            self.event("Bridge Moved")
            | r.can_door
            | (r.difficulty("extreme") & r.can_gj_ez),
        )

        self.restrict(
            "Silver Key (17)",
            self.event("Bridge Moved") | (r.difficulty("hard") & r.jump),
        )

        self.restrict(
            "Rockets (58)",
            self.event("Bridge Moved") | (r.difficulty("hard") & r.jump),
        )

        underwater_secret_area = self.region(
            "Underwater Secret Area",
            [
                "Secret (47)",
                "Shells (32)",
                "Rocketlauncher (36)",
                "Large Medkit (30)",
                "Large Medkit (31)",
                "Spikes (49)",
            ],
        )
        self.connect(
            ret,
            underwater_secret_area,
            r.can_dive,
        )

        silver_key_door_area = self.region(
            "Silver Key Door Area",
            [
                "Small Medkit (19)",
                "Small Medkit (20)",
                "Small Medkit (21)",
                "Shells (34)",
                "Large Medkit (11)",
                "Shells (24)",
            ],
        )
        self.connect(
            ret, silver_key_door_area, self.event("Bridge Door Open") | r.can_door
        )

        alcove_secret_area = self.region(
            "Alcove Secret Area",
            [
                "Secret (59)",
                "Quad Damage (60)",
            ],
        )
        self.connect(silver_key_door_area, alcove_secret_area, r.can_button)

        past_silver_door = self.region(
            "Past Silver Door Area",
            [
                "Shells (25)",
                "Large Medkit (26)",
                "Large Medkit (27)",
            ],
        )
        self.connect(silver_key_door_area, past_silver_door, self.silver_key)

        past_silver_door_upper = self.region(
            "Past Silver Door Upper Area",
            [
                "Large Medkit (22)",
                "Large Medkit (23)",
                "Megahealth (39)",
                "Rockets (52)",
                "Spikes (53)",
                "Spikes (55)",
            ],
        )
        self.connect(past_silver_door, past_silver_door_upper, r.bigjump | r.can_button)

        final_area = self.region(
            "Final Area",
            [
                "Shells (12)",
                "Small Medkit (13)",
                "Small Medkit (14)",
                "Supernailgun (38)",
                "Spikes (40)",
                "Exit",
            ],
        )
        self.connect(past_silver_door, final_area, r.can_button)

        return ret
