from BaseClasses import Region

from ..base_classes import Q1Level


class E4M2(Q1Level):
    name = "The Tower of Despair"
    mapfile = "e4m2"
    keys = ["Silver"]
    location_defs = [
        {
            "id": 1,
            "name": "Rocketlauncher (1)",
            "classname": "weapon_rocketlauncher",
            "uuid": 12121758931081694155,
            "density": 0,
        },
        {
            "id": 2,
            "name": "Spikes (2)",
            "classname": "item_spikes",
            "uuid": 12606203976803145468,
            "density": 0,
        },
        {
            "id": 3,
            "name": "Shells (3)",
            "classname": "item_shells",
            "uuid": 3728357093248118230,
            "density": 0,
        },
        {
            "id": 4,
            "name": "Shells (4)",
            "classname": "item_shells",
            "uuid": 6465288233463519422,
            "density": 0,
        },
        {
            "id": 5,
            "name": "Small Medkit (5)",
            "classname": "item_health",
            "uuid": 9092583591582214268,
            "density": 0,
        },
        {
            "id": 6,
            "name": "Small Medkit (6)",
            "classname": "item_health",
            "uuid": 14301115397770382779,
            "density": 0,
        },
        {
            "id": 7,
            "name": "Spikes (7)",
            "classname": "item_spikes",
            "uuid": 15931274047764816712,
            "density": 0,
        },
        {
            "id": 8,
            "name": "Spikes (8)",
            "classname": "item_spikes",
            "uuid": 2492709502513815217,
            "density": 0,
        },
        {
            "id": 9,
            "name": "Shells (9)",
            "classname": "item_shells",
            "uuid": 3611198983714633311,
            "density": 0,
        },
        {
            "id": 10,
            "name": "Large Medkit (10)",
            "classname": "item_health",
            "uuid": 4746918654739321174,
            "density": 0,
        },
        {
            "id": 11,
            "name": "Shells (11)",
            "classname": "item_shells",
            "uuid": 1520701174054809520,
            "density": 0,
        },
        {
            "id": 12,
            "name": "Large Medkit (12)",
            "classname": "item_health",
            "uuid": 7367860271061901091,
            "density": 0,
        },
        {
            "id": 13,
            "name": "Shells (13)",
            "classname": "item_shells",
            "uuid": 10059242790201376292,
            "density": 0,
        },
        {
            "id": 14,
            "name": "Spikes (14)",
            "classname": "item_spikes",
            "uuid": 5419541139339388523,
            "density": 0,
        },
        {
            "id": 15,
            "name": "Spikes (15)",
            "classname": "item_spikes",
            "uuid": 10880241247513028606,
            "density": 0,
        },
        {
            "id": 16,
            "name": "Shells (16)",
            "classname": "item_shells",
            "uuid": 9398340497512285982,
            "density": 0,
        },
        {
            "id": 17,
            "name": "Small Medkit (17)",
            "classname": "item_health",
            "uuid": 787453709308521250,
            "density": 0,
        },
        {
            "id": 18,
            "name": "Megahealth (18)",
            "classname": "item_health",
            "uuid": 5583480817290608171,
            "density": 0,
        },
        {
            "id": 19,
            "name": "Small Medkit (19)",
            "classname": "item_health",
            "uuid": 11682920356225214453,
            "density": 0,
        },
        {
            "id": 20,
            "name": "Small Medkit (20)",
            "classname": "item_health",
            "uuid": 1569449419506927377,
            "density": 0,
        },
        {
            "id": 21,
            "name": "Spikes (21)",
            "classname": "item_spikes",
            "uuid": 1703619372058942520,
            "density": 0,
        },
        {
            "id": 22,
            "name": "Small Medkit (22)",
            "classname": "item_health",
            "uuid": 13792318269222581822,
            "density": 0,
        },
        {
            "id": 23,
            "name": "Yellow Armor (23)",
            "classname": "item_armor2",
            "uuid": 14745352986714900649,
            "density": 0,
        },
        {
            "id": 24,
            "name": "Large Medkit (24)",
            "classname": "item_health",
            "uuid": 13314810238130542963,
            "density": 0,
        },
        {
            "id": 25,
            "name": "Megahealth (25)",
            "classname": "item_health",
            "uuid": 17660118447950704947,
            "density": 0,
        },
        {
            "id": 26,
            "name": "Green Armor (26)",
            "classname": "item_armor1",
            "uuid": 9263109594720823315,
            "density": 0,
        },
        {
            "id": 27,
            "name": "Invisibility (27)",
            "classname": "item_artifact_invisibility",
            "uuid": 9781341883959189135,
            "density": 0,
        },
        {
            "id": 28,
            "name": "Quad Damage (28)",
            "classname": "item_artifact_super_damage",
            "uuid": 15103575184650256130,
            "density": 0,
        },
        {
            "id": 29,
            "name": "Megahealth (29)",
            "classname": "item_health",
            "uuid": 4045720591006061548,
            "density": 0,
        },
        {
            "id": 30,
            "name": "Lightning (30)",
            "classname": "weapon_lightning",
            "uuid": 15497470815816197192,
            "density": 0,
        },
        {
            "id": 31,
            "name": "Green Armor (31)",
            "classname": "item_armor1",
            "uuid": 744024611980245912,
            "density": 0,
        },
        {
            "id": 32,
            "name": "Supershotgun (32)",
            "classname": "weapon_supershotgun",
            "uuid": 11591481979686530806,
            "density": 0,
        },
        {
            "id": 33,
            "name": "Cells (33)",
            "classname": "item_cells",
            "uuid": 17911323178141369366,
            "density": 0,
        },
        {
            "id": 34,
            "name": "Supershotgun (34)",
            "classname": "weapon_supershotgun",
            "uuid": 15654637470746432758,
            "density": 0,
        },
        {
            "id": 35,
            "name": "Grenadelauncher (35)",
            "classname": "weapon_grenadelauncher",
            "uuid": 10486165865129758961,
            "density": 0,
        },
        {
            "id": 36,
            "name": "Secret (36)",
            "classname": "trigger_secret",
            "uuid": 13159782356065761812,
            "density": 0,
        },
        {
            "id": 37,
            "name": "Secret (37)",
            "classname": "trigger_secret",
            "uuid": 5426713586365670698,
            "density": 0,
        },
        {
            "id": 38,
            "name": "Secret (38)",
            "classname": "trigger_secret",
            "uuid": 2212764226839319699,
            "density": 0,
        },
        {
            "id": 39,
            "name": "Yellow Armor (39)",
            "classname": "item_armor2",
            "uuid": 3752316385684952523,
            "density": 0,
        },
        {
            "id": 40,
            "name": "Megahealth (40)",
            "classname": "item_health",
            "uuid": 1739596142252902895,
            "density": 0,
        },
        {
            "id": 41,
            "name": "Small Medkit (41)",
            "classname": "item_health",
            "uuid": 1688728614421842468,
            "density": 0,
        },
        {
            "id": 42,
            "name": "Small Medkit (42)",
            "classname": "item_health",
            "uuid": 11662138319218222252,
            "density": 0,
        },
        {
            "id": 43,
            "name": "Rocketlauncher (43)",
            "classname": "weapon_rocketlauncher",
            "uuid": 16420025789164056611,
            "density": 0,
        },
        {
            "id": 44,
            "name": "Supernailgun (44)",
            "classname": "weapon_supernailgun",
            "uuid": 6927304094955933839,
            "density": 0,
        },
        {
            "id": 45,
            "name": "Grenadelauncher (45)",
            "classname": "weapon_grenadelauncher",
            "uuid": 12351944850522736616,
            "density": 0,
        },
        {
            "id": 46,
            "name": "Lightning (46)",
            "classname": "weapon_lightning",
            "uuid": 14387722976623165056,
            "density": 0,
        },
        {
            "id": 47,
            "name": "Cells (47)",
            "classname": "item_cells",
            "uuid": 14612531245361484268,
            "density": 0,
        },
        {
            "id": 48,
            "name": "Secret (48)",
            "classname": "trigger_secret",
            "uuid": 6242357266256306548,
            "density": 0,
        },
        {
            "id": 49,
            "name": "Exit",
            "classname": "trigger_changelevel",
            "uuid": 17378040218368898388,
            "density": 0,
        },
        {
            "id": 50,
            "name": "Cells (50)",
            "classname": "item_cells",
            "uuid": 2442051327000169924,
            "density": 0,
        },
        {
            "id": 51,
            "name": "Nailgun (51)",
            "classname": "weapon_nailgun",
            "uuid": 3072431061924846208,
            "density": 0,
        },
        {
            "id": 52,
            "name": "Grenadelauncher (52)",
            "classname": "weapon_grenadelauncher",
            "uuid": 8486515590915483150,
            "density": 0,
        },
        {
            "id": 53,
            "name": "Rockets (53)",
            "classname": "item_rockets",
            "uuid": 12468008194699545923,
            "density": 0,
        },
        {
            "id": 54,
            "name": "Large Medkit (54)",
            "classname": "item_health",
            "uuid": 11747162314922026557,
            "density": 0,
        },
        {
            "id": 55,
            "name": "Invulnerability (55)",
            "classname": "item_artifact_invulnerability",
            "uuid": 16138850130885984869,
            "density": 0,
        },
        {
            "id": 56,
            "name": "Spikes (56)",
            "classname": "item_spikes",
            "uuid": 3951498287352557703,
            "density": 0,
        },
        {
            "id": 57,
            "name": "Quad Damage (57)",
            "classname": "item_artifact_super_damage",
            "uuid": 2474477848821341317,
            "density": 0,
        },
        {
            "id": 58,
            "name": "Shells (58)",
            "classname": "item_shells",
            "uuid": 18409910274009407520,
            "density": 0,
        },
        {
            "id": 59,
            "name": "Cells (59)",
            "classname": "item_cells",
            "uuid": 5255724773257394942,
            "density": 0,
        },
        {
            "id": 60,
            "name": "Shells (60)",
            "classname": "item_shells",
            "uuid": 15234622571300772355,
            "density": 0,
        },
        {
            "id": 61,
            "name": "Small Medkit (61)",
            "classname": "item_health",
            "uuid": 17506696326657386638,
            "density": 0,
        },
        {
            "id": 62,
            "name": "Supershotgun (62)",
            "classname": "weapon_supershotgun",
            "uuid": 10325719825950154462,
            "density": 0,
        },
        {
            "id": 63,
            "name": "Spikes (63)",
            "classname": "item_spikes",
            "uuid": 14799991071883957651,
            "density": 0,
        },
        {
            "id": 64,
            "name": "Shells (64)",
            "classname": "item_shells",
            "uuid": 15354478059965475879,
            "density": 0,
        },
        {
            "id": 65,
            "name": "Invulnerability (65)",
            "classname": "item_artifact_invulnerability",
            "uuid": 10731947855224086360,
            "density": 0,
        },
        {
            "id": 66,
            "name": "Silver Key (66)",
            "classname": "item_key1",
            "uuid": 10264540938219921141,
            "density": 0,
        },
        {
            "id": 67,
            "name": "Silver Key (67)",
            "classname": "item_key1",
            "uuid": 9488628489137100746,
            "density": 0,
        },
        {
            "id": 68,
            "name": "Large Medkit (68)",
            "classname": "item_health",
            "uuid": 857785879636585043,
            "density": 0,
        },
        {
            "id": 69,
            "name": "Small Medkit (69)",
            "classname": "item_health",
            "uuid": 6778647802520694391,
            "density": 0,
        },
        {
            "id": 70,
            "name": "Secret (70)",
            "classname": "trigger_secret",
            "uuid": 1702593927320847381,
            "density": 0,
        },
    ]

    def main_region(self) -> Region:
        r = self.rules

        ret = self.region(
            self.name,
            [
                "Megahealth (29)",
                "Shells (4)",
                "Shells (60)",
                "Small Medkit (5)",
                "Invulnerability (65)",
                "Small Medkit (41)",
                "Small Medkit (42)",
                "Large Medkit (54)",
                "Rockets (53)",
                "Cells (50)",
                "Small Medkit (19)",
                "Quad Damage (28)",
                "Spikes (15)",
                "Small Medkit (61)",
                "Spikes (8)",
                "Small Medkit (17)",
            ],
        )

        shootswitch_area = self.region(
            "Shootswitch Secret",
            [
                "Secret (36)",
                "Invisibility (27)",
                "Spikes (2)",
            ],
        )
        self.connect(ret, shootswitch_area, r.can_shootswitch)

        shootswitch_button_area = self.region(
            "Shootswitch Button Secret",
            [
                "Secret (37)",
                "Spikes (63)",
                "Grenadelauncher (35)",
                "Green Armor (31)",
                "Supershotgun (34)",
                "Secret (38)",
                "Shells (3)",
            ],
        )
        self.connect(ret, shootswitch_button_area, r.can_shootswitch & r.can_button)

        water_drop_area = self.region(
            "Water Drop",
            [
                "Supershotgun (62)",
                "Shells (64)",
                "Large Medkit (24)",
                "Shells (13)",
                "Nailgun (51)",
                "Invulnerability (55)",
                "Spikes (14)",
                "Rocketlauncher (1)",
                "Shells (16)",
            ],
        )
        self.connect(ret, water_drop_area, r.difficulty("medium") | r.jump)
        self.restrict(
            "Rocketlauncher (1)", r.can_button | (r.bigjump & r.difficulty("medium"))
        )
        self.restrict(
            "Shells (16)", r.can_button | (r.bigjump & r.difficulty("medium"))
        )

        water_drop_upper_area = self.region(
            "Water Drop Upper",
            [
                "Shells (9)",
                "Grenadelauncher (52)",
                "Cells (33)",
                "Small Medkit (22)",
                "Supershotgun (32)",
                "Megahealth (18)",
                "Secret (48)",
                "Quad Damage (57)",
                "Spikes (21)",
                "Small Medkit (20)",
            ],
        )
        self.connect(
            ret, water_drop_upper_area, r.can_jump | r.can_gj_extr | r.can_rj_hard
        )

        past_window_area = self.region(
            "Past Window",
            [
                "Rocketlauncher (43)",
                "Spikes (7)",
                "Small Medkit (6)",
                "Secret (70)",
                "Small Medkit (69)",
                "Large Medkit (68)",
                "Shells (58)",
                "Large Medkit (12)",
                "Spikes (56)",
                "Cells (59)",
                "Grenadelauncher (45)",
                "Large Medkit (10)",
                "Shells (11)",
                "Supernailgun (44)",
                "Exit",
            ],
        )
        self.connect(water_drop_upper_area, past_window_area, r.can_shootswitch)
        self.restrict(
            "Exit", self.silver_key | (r.can_door & r.difficulty("extreme") & r.jump)
        )

        past_button_area = self.region(
            "Past Button",
            [
                "Lightning (46)",
                "Megahealth (40)",
                "Yellow Armor (23)",
                "Cells (47)",
                "Silver Key (66)",
            ],
        )
        self.connect(water_drop_upper_area, past_button_area, r.can_button)

        return ret
