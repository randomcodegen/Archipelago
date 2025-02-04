from BaseClasses import Region

from ..base_classes import Q1Level


class E2M2(Q1Level):
    name = "The Ogre Citadel"
    mapfile = "e2m2"
    keys = ["Gold"]
    location_defs = [
        {
            "id": 1,
            "name": "Megahealth (1)",
            "classname": "item_health",
            "uuid": 18365367778714231749,
            "density": 2,
        },
        {
            "id": 2,
            "name": "Rockets (2)",
            "classname": "item_rockets",
            "uuid": 16347836082726786253,
            "density": 1,
        },
        {
            "id": 3,
            "name": "Large Medkit (3)",
            "classname": "item_health",
            "uuid": 16681426178661996238,
            "density": 3,
        },
        {
            "id": 4,
            "name": "Large Medkit (4)",
            "classname": "item_health",
            "uuid": 1431357254881000869,
            "density": 1,
        },
        {
            "id": 5,
            "name": "Small Medkit (5)",
            "classname": "item_health",
            "uuid": 5067580972518932525,
            "density": 4,
        },
        {
            "id": 6,
            "name": "Small Medkit (6)",
            "classname": "item_health",
            "uuid": 8873036915502190951,
            "density": 4,
        },
        {
            "id": 7,
            "name": "Weapon (7)",
            "classname": "item_weapon",
            "uuid": 15140036664533756861,
            "density": 0,
        },
        {
            "id": 8,
            "name": "Large Medkit (8)",
            "classname": "item_health",
            "uuid": 7857745403737594305,
            "density": 1,
        },
        {
            "id": 9,
            "name": "Shells (9)",
            "classname": "item_shells",
            "uuid": 14817572207581423424,
            "density": 3,
        },
        {
            "id": 10,
            "name": "Large Medkit (10)",
            "classname": "item_health",
            "uuid": 4743401937457982754,
            "density": 4,
        },
        {
            "id": 11,
            "name": "Large Medkit (11)",
            "classname": "item_health",
            "uuid": 6578779792175716623,
            "density": 4,
        },
        {
            "id": 12,
            "name": "Large Medkit (12)",
            "classname": "item_health",
            "uuid": 4720399969158461233,
            "density": 3,
        },
        {
            "id": 13,
            "name": "Shells (13)",
            "classname": "item_shells",
            "uuid": 7669292788717335701,
            "density": 4,
        },
        {
            "id": 14,
            "name": "Megahealth (14)",
            "classname": "item_health",
            "uuid": 2232645518373383377,
            "density": 2,
        },
        {
            "id": 15,
            "name": "Green Armor (15)",
            "classname": "item_armor1",
            "uuid": 14849509220947019639,
            "density": 0,
        },
        {
            "id": 16,
            "name": "Red Armor (16)",
            "classname": "item_armorInv",
            "uuid": 18160457576355044574,
            "density": 5,
        },
        {
            "id": 17,
            "name": "Yellow Armor (17)",
            "classname": "item_armor2",
            "uuid": 5230684986746027165,
            "density": 0,
        },
        {
            "id": 18,
            "name": "Grenadelauncher (18)",
            "classname": "weapon_grenadelauncher",
            "uuid": 17004986947002863700,
            "density": 5,
        },
        {
            "id": 19,
            "name": "Rocketlauncher (19)",
            "classname": "weapon_rocketlauncher",
            "uuid": 9215139315308103496,
            "density": 5,
        },
        {
            "id": 20,
            "name": "Supernailgun (20)",
            "classname": "weapon_supernailgun",
            "uuid": 4063500887306899926,
            "density": 5,
        },
        {
            "id": 21,
            "name": "Supershotgun (21)",
            "classname": "weapon_supershotgun",
            "uuid": 2118721353786864390,
            "density": 5,
        },
        {
            "id": 22,
            "name": "Nailgun (22)",
            "classname": "weapon_nailgun",
            "uuid": 7039265785670948057,
            "density": 5,
        },
        {
            "id": 23,
            "name": "Rockets (23)",
            "classname": "item_rockets",
            "uuid": 15079753033869591020,
            "density": 5,
        },
        {
            "id": 24,
            "name": "Rockets (24)",
            "classname": "item_rockets",
            "uuid": 15252020573026444930,
            "density": 5,
        },
        {
            "id": 25,
            "name": "Small Medkit (25)",
            "classname": "item_health",
            "uuid": 7191568517390985630,
            "density": 1,
        },
        {
            "id": 26,
            "name": "Shells (26)",
            "classname": "item_shells",
            "uuid": 787081767527070053,
            "density": 3,
        },
        {
            "id": 27,
            "name": "Gold Key (27)",
            "classname": "item_key2",
            "uuid": 1402986048140627833,
            "density": 0,
        },
        {
            "id": 28,
            "name": "Spikes (28)",
            "classname": "item_spikes",
            "uuid": 5275956032062048439,
            "density": 3,
        },
        {
            "id": 29,
            "name": "Large Medkit (29)",
            "classname": "item_health",
            "uuid": 15677443420661687625,
            "density": 1,
        },
        {
            "id": 30,
            "name": "Supershotgun (30)",
            "classname": "weapon_supershotgun",
            "uuid": 14999842322755341953,
            "density": 0,
        },
        {
            "id": 31,
            "name": "Shells (31)",
            "classname": "item_shells",
            "uuid": 11836790667001825221,
            "density": 0,
        },
        {
            "id": 32,
            "name": "Nailgun (32)",
            "classname": "weapon_nailgun",
            "uuid": 2974629652179455968,
            "density": 0,
        },
        {
            "id": 33,
            "name": "Large Medkit (33)",
            "classname": "item_health",
            "uuid": 16465211265956965870,
            "density": 3,
        },
        {
            "id": 34,
            "name": "Large Medkit (34)",
            "classname": "item_health",
            "uuid": 10125581890617501009,
            "density": 1,
        },
        {
            "id": 35,
            "name": "Large Medkit (35)",
            "classname": "item_health",
            "uuid": 16585362634103376448,
            "density": 4,
        },
        {
            "id": 36,
            "name": "Spikes (36)",
            "classname": "item_spikes",
            "uuid": 3178368333279169908,
            "density": 3,
        },
        {
            "id": 37,
            "name": "Shells (37)",
            "classname": "item_shells",
            "uuid": 1251563197975477801,
            "density": 1,
        },
        {
            "id": 38,
            "name": "Grenadelauncher (38)",
            "classname": "weapon_grenadelauncher",
            "uuid": 988136741119682502,
            "density": 2,
        },
        {
            "id": 39,
            "name": "Exit",
            "classname": "trigger_changelevel",
            "uuid": 6912380172586247107,
            "density": 0,
        },
        {
            "id": 40,
            "name": "Shells (40)",
            "classname": "item_shells",
            "uuid": 1625117765189351094,
            "density": 1,
        },
        {
            "id": 41,
            "name": "Small Medkit (41)",
            "classname": "item_health",
            "uuid": 3006073659314392657,
            "density": 4,
        },
        {
            "id": 42,
            "name": "Secret (42)",
            "classname": "trigger_secret",
            "uuid": 12569708575548327084,
            "density": 0,
        },
        {
            "id": 43,
            "name": "Secret (43)",
            "classname": "trigger_secret",
            "uuid": 7675241514988716000,
            "density": 0,
        },
        {
            "id": 44,
            "name": "Secret (44)",
            "classname": "trigger_secret",
            "uuid": 4449142097410431352,
            "density": 0,
        },
        {
            "id": 45,
            "name": "Shells (45)",
            "classname": "item_shells",
            "uuid": 6009186205385459139,
            "density": 0,
        },
        {
            "id": 46,
            "name": "Rockets (46)",
            "classname": "item_rockets",
            "uuid": 13802268324470646527,
            "density": 5,
        },
        {
            "id": 47,
            "name": "Rockets (47)",
            "classname": "item_rockets",
            "uuid": 1199305622799939845,
            "density": 5,
        },
        {
            "id": 48,
            "name": "Shells (48)",
            "classname": "item_shells",
            "uuid": 12605435091102933124,
            "density": 0,
        },
        {
            "id": 49,
            "name": "Lightning (49)",
            "classname": "weapon_lightning",
            "uuid": 7643742113115451436,
            "density": 5,
        },
        {
            "id": 50,
            "name": "Quad Damage (50)",
            "classname": "item_artifact_super_damage",
            "uuid": 7321327161874702397,
            "density": 0,
        },
        {
            "id": 51,
            "name": "Cells (51)",
            "classname": "item_cells",
            "uuid": 5351983792930731206,
            "density": 5,
        },
        {
            "id": 52,
            "name": "Cells (52)",
            "classname": "item_cells",
            "uuid": 10568323400097354200,
            "density": 5,
        },
        {
            "id": 53,
            "name": "Cells (53)",
            "classname": "item_cells",
            "uuid": 5573524705522663900,
            "density": 5,
        },
        {
            "id": 54,
            "name": "Grenadelauncher (54)",
            "classname": "weapon_grenadelauncher",
            "uuid": 5897484177831578046,
            "density": 0,
        },
    ]

    def main_region(self) -> Region:
        r = self.rules

        ret = self.region(
            self.name,
            [
                "Small Medkit (25)",
                "Lightning (49)",
                "Cells (51)",
                "Green Armor (15)",
                "Shells (26)",
                "Shells (45)",
            ],
        )
        self.restrict("Shells (45)", r.jump)

        castle_moat_area = self.region(
            "Castle Moat Area",
            [
                "Secret (42)",
                "Megahealth (14)",
                "Secret (43)",
                "Grenadelauncher (38)",
            ],
        )
        self.connect(ret, castle_moat_area)

        castle_behind_bars_area = self.region(
            "Castle Behind Bars Area",
            [
                "Spikes (28)",
                "Rockets (24)",
                "Large Medkit (29)",
                "Gold Key (27)",
            ],
        )
        self.connect(
            castle_moat_area, castle_behind_bars_area, (r.can_jump & r.can_rj_hard)
        )

        castle_outside_secret_area = self.region(
            "Castle Outside Secret Area",
            [
                "Yellow Armor (17)",
                "Secret (44)",
                "Supernailgun (20)",
                "Megahealth (1)",
            ],
        )
        self.connect(
            castle_moat_area, castle_outside_secret_area, (r.can_jump & r.can_rj_hard)
        )

        castle_inside_area = self.region(
            "Castle Inside Area",
            [
                "Shells (31)",
                "Rockets (2)",
                "Nailgun (22)",
                "Supershotgun (30)",
                "Cells (52)",
                "Large Medkit (4)",
                "Large Medkit (3)",
                "Small Medkit (5)",
                "Small Medkit (6)",
                "Weapon (7)",
                "Large Medkit (8)",
                "Shells (9)",
                "Supershotgun (21)",
                "Shells (13)",
                "Grenadelauncher (18)",
                "Nailgun (32)",
                "Quad Damage (50)",
                "Shells (37)",
                "Shells (48)",
                "Large Medkit (34)",
                "Cells (53)",
                "Red Armor (16)",
                "Large Medkit (33)",
                "Large Medkit (35)",
                "Spikes (36)",
                "Small Medkit (41)",
            ],
        )
        self.connect(castle_outside_secret_area, castle_inside_area, r.jump)
        self.connect(castle_inside_area, castle_outside_secret_area, r.jump)
        self.connect(ret, castle_inside_area, r.can_shootswitch)
        self.connect(castle_inside_area, castle_behind_bars_area, r.can_button)

        past_gold_door_area = self.region(
            "Past Gold Door Area",
            [
                "Shells (40)",
                "Grenadelauncher (54)",
                "Large Medkit (12)",
                "Large Medkit (10)",
                "Large Medkit (11)",
                "Rocketlauncher (19)",
                "Rockets (47)",
                "Rockets (46)",
                "Exit",
            ],
        )
        self.connect(castle_inside_area, past_gold_door_area, self.gold_key)
        self.restrict("Exit", r.can_door)

        return ret
