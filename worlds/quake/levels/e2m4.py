from BaseClasses import Region

from ..base_classes import Q1Level


class E2M4(Q1Level):
    name = "The Ebon Fortress"
    mapfile = "e2m4"
    keys = ["Silver", "Gold"]
    location_defs = [
        {
            "id": 1,
            "name": "Silver Key (1)",
            "classname": "item_key1",
            "uuid": 6510556378627355569,
            "density": 0,
        },
        {
            "id": 2,
            "name": "Green Armor (2)",
            "classname": "item_armor1",
            "uuid": 221315245835791155,
            "density": 0,
        },
        {
            "id": 3,
            "name": "Biosuit (3)",
            "classname": "item_artifact_envirosuit",
            "uuid": 16315203349143512455,
            "density": 0,
        },
        {
            "id": 4,
            "name": "Red Armor (4)",
            "classname": "item_armorInv",
            "uuid": 5432988763535033032,
            "density": 0,
        },
        {
            "id": 5,
            "name": "Shells (5)",
            "classname": "item_shells",
            "uuid": 13298359260080220525,
            "density": 0,
        },
        {
            "id": 6,
            "name": "Large Medkit (6)",
            "classname": "item_health",
            "uuid": 13296320775708917890,
            "density": 0,
        },
        {
            "id": 7,
            "name": "Large Medkit (7)",
            "classname": "item_health",
            "uuid": 7180742541294776499,
            "density": 0,
        },
        {
            "id": 8,
            "name": "Shells (8)",
            "classname": "item_shells",
            "uuid": 15774421896271519678,
            "density": 0,
        },
        {
            "id": 9,
            "name": "Exit",
            "classname": "trigger_changelevel",
            "uuid": 12597541049749024528,
            "density": 0,
        },
        {
            "id": 10,
            "name": "Rocketlauncher (10)",
            "classname": "weapon_rocketlauncher",
            "uuid": 9551742857270627187,
            "density": 0,
        },
        {
            "id": 11,
            "name": "Large Medkit (11)",
            "classname": "item_health",
            "uuid": 6300101404090615283,
            "density": 0,
        },
        {
            "id": 12,
            "name": "Rockets (12)",
            "classname": "item_rockets",
            "uuid": 6059458314502054376,
            "density": 0,
        },
        {
            "id": 13,
            "name": "Rockets (13)",
            "classname": "item_rockets",
            "uuid": 11689702558467175275,
            "density": 0,
        },
        {
            "id": 14,
            "name": "Shells (14)",
            "classname": "item_shells",
            "uuid": 17849160217757372054,
            "density": 0,
        },
        {
            "id": 15,
            "name": "Small Medkit (15)",
            "classname": "item_health",
            "uuid": 2166124430156776187,
            "density": 0,
        },
        {
            "id": 16,
            "name": "Yellow Armor (16)",
            "classname": "item_armor2",
            "uuid": 13358971438921331179,
            "density": 0,
        },
        {
            "id": 17,
            "name": "Supernailgun (17)",
            "classname": "weapon_supernailgun",
            "uuid": 10652297857103120677,
            "density": 0,
        },
        {
            "id": 18,
            "name": "Shells (18)",
            "classname": "item_shells",
            "uuid": 10915737593548321098,
            "density": 0,
        },
        {
            "id": 19,
            "name": "Yellow Armor (19)",
            "classname": "item_armor2",
            "uuid": 9245240603282396285,
            "density": 0,
        },
        {
            "id": 20,
            "name": "Spikes (20)",
            "classname": "item_spikes",
            "uuid": 6852420351836579776,
            "density": 0,
        },
        {
            "id": 21,
            "name": "Nailgun (21)",
            "classname": "weapon_nailgun",
            "uuid": 15294961952014116024,
            "density": 0,
        },
        {
            "id": 22,
            "name": "Large Medkit (22)",
            "classname": "item_health",
            "uuid": 3084568379150868241,
            "density": 0,
        },
        {
            "id": 23,
            "name": "Small Medkit (23)",
            "classname": "item_health",
            "uuid": 4140288344057154733,
            "density": 0,
        },
        {
            "id": 24,
            "name": "Spikes (24)",
            "classname": "item_spikes",
            "uuid": 13744947716742235748,
            "density": 0,
        },
        {
            "id": 25,
            "name": "Secret (25)",
            "classname": "trigger_secret",
            "uuid": 15431912947576149857,
            "density": 0,
        },
        {
            "id": 26,
            "name": "Large Medkit (26)",
            "classname": "item_health",
            "uuid": 9666834922512868781,
            "density": 0,
        },
        {
            "id": 27,
            "name": "Secret (27)",
            "classname": "trigger_secret",
            "uuid": 10418507992357759926,
            "density": 0,
        },
        {
            "id": 28,
            "name": "Secret (28)",
            "classname": "trigger_secret",
            "uuid": 8972371874609155419,
            "density": 0,
        },
        {
            "id": 29,
            "name": "Megahealth (29)",
            "classname": "item_health",
            "uuid": 4640297775002855794,
            "density": 0,
        },
        {
            "id": 30,
            "name": "Rockets (30)",
            "classname": "item_rockets",
            "uuid": 17481218612713508300,
            "density": 0,
        },
        {
            "id": 31,
            "name": "Shells (31)",
            "classname": "item_shells",
            "uuid": 7396995688158336298,
            "density": 0,
        },
        {
            "id": 32,
            "name": "Large Medkit (32)",
            "classname": "item_health",
            "uuid": 12316369789883279644,
            "density": 0,
        },
        {
            "id": 33,
            "name": "Rockets (33)",
            "classname": "item_rockets",
            "uuid": 6479843243670526948,
            "density": 0,
        },
        {
            "id": 34,
            "name": "Spikes (34)",
            "classname": "item_spikes",
            "uuid": 4024208076749566129,
            "density": 0,
        },
        {
            "id": 35,
            "name": "Green Armor (35)",
            "classname": "item_armor1",
            "uuid": 6216304921956904078,
            "density": 0,
        },
        {
            "id": 36,
            "name": "Quad Damage (36)",
            "classname": "item_artifact_super_damage",
            "uuid": 3662354067323661281,
            "density": 0,
        },
        {
            "id": 37,
            "name": "Small Medkit (37)",
            "classname": "item_health",
            "uuid": 9263747266987613178,
            "density": 0,
        },
        {
            "id": 38,
            "name": "Large Medkit (38)",
            "classname": "item_health",
            "uuid": 1251207813982120076,
            "density": 0,
        },
        {
            "id": 39,
            "name": "Large Medkit (39)",
            "classname": "item_health",
            "uuid": 6134004955191412652,
            "density": 0,
        },
        {
            "id": 40,
            "name": "Rockets (40)",
            "classname": "item_rockets",
            "uuid": 17041507741201547284,
            "density": 0,
        },
        {
            "id": 41,
            "name": "Spikes (41)",
            "classname": "item_spikes",
            "uuid": 2402385227567862493,
            "density": 0,
        },
        {
            "id": 42,
            "name": "Large Medkit (42)",
            "classname": "item_health",
            "uuid": 15002462410648144344,
            "density": 0,
        },
        {
            "id": 43,
            "name": "Large Medkit (43)",
            "classname": "item_health",
            "uuid": 16871402396930941911,
            "density": 0,
        },
        {
            "id": 44,
            "name": "Large Medkit (44)",
            "classname": "item_health",
            "uuid": 1502828889166557819,
            "density": 0,
        },
        {
            "id": 45,
            "name": "Small Medkit (45)",
            "classname": "item_health",
            "uuid": 15889632334836820137,
            "density": 0,
        },
        {
            "id": 46,
            "name": "Spikes (46)",
            "classname": "item_spikes",
            "uuid": 14248055043383962702,
            "density": 0,
        },
        {
            "id": 47,
            "name": "Yellow Armor (47)",
            "classname": "item_armor2",
            "uuid": 13311569058313202329,
            "density": 0,
        },
        {
            "id": 48,
            "name": "Gold Key (48)",
            "classname": "item_key2",
            "uuid": 11304146690600016768,
            "density": 0,
        },
        {
            "id": 49,
            "name": "Grenadelauncher (49)",
            "classname": "weapon_grenadelauncher",
            "uuid": 6849364826418975120,
            "density": 0,
        },
        {
            "id": 50,
            "name": "Rockets (50)",
            "classname": "item_rockets",
            "uuid": 14098282130203524215,
            "density": 0,
        },
        {
            "id": 51,
            "name": "Large Medkit (51)",
            "classname": "item_health",
            "uuid": 17691520255290812965,
            "density": 0,
        },
        {
            "id": 52,
            "name": "Large Medkit (52)",
            "classname": "item_health",
            "uuid": 1419298879113937232,
            "density": 0,
        },
        {
            "id": 53,
            "name": "Small Medkit (53)",
            "classname": "item_health",
            "uuid": 13182169675663338782,
            "density": 0,
        },
        {
            "id": 54,
            "name": "Large Medkit (54)",
            "classname": "item_health",
            "uuid": 14129472961119088569,
            "density": 0,
        },
        {
            "id": 55,
            "name": "Shells (55)",
            "classname": "item_shells",
            "uuid": 16042621280665579089,
            "density": 0,
        },
        {
            "id": 56,
            "name": "Spikes (56)",
            "classname": "item_spikes",
            "uuid": 17235086316802238477,
            "density": 0,
        },
        {
            "id": 57,
            "name": "Shells (57)",
            "classname": "item_shells",
            "uuid": 13111309900951064849,
            "density": 0,
        },
        {
            "id": 58,
            "name": "Large Medkit (58)",
            "classname": "item_health",
            "uuid": 13077179525747711534,
            "density": 0,
        },
        {
            "id": 59,
            "name": "Small Medkit (59)",
            "classname": "item_health",
            "uuid": 10206620922226883960,
            "density": 0,
        },
        {
            "id": 60,
            "name": "Shells (60)",
            "classname": "item_shells",
            "uuid": 2941854281539041865,
            "density": 0,
        },
        {
            "id": 61,
            "name": "Shells (61)",
            "classname": "item_shells",
            "uuid": 12639046169934010357,
            "density": 0,
        },
        {
            "id": 62,
            "name": "Rockets (62)",
            "classname": "item_rockets",
            "uuid": 18026053480655456058,
            "density": 0,
        },
        {
            "id": 63,
            "name": "Small Medkit (63)",
            "classname": "item_health",
            "uuid": 6877102419321597961,
            "density": 0,
        },
        {
            "id": 64,
            "name": "Grenadelauncher (64)",
            "classname": "weapon_grenadelauncher",
            "uuid": 11565290359729541007,
            "density": 0,
        },
        {
            "id": 65,
            "name": "Spikes (65)",
            "classname": "item_spikes",
            "uuid": 8326483106049027592,
            "density": 0,
        },
        {
            "id": 66,
            "name": "Biosuit (66)",
            "classname": "item_artifact_envirosuit",
            "uuid": 16344051228500906611,
            "density": 0,
        },
        {
            "id": 67,
            "name": "Shells (67)",
            "classname": "item_shells",
            "uuid": 1525060539555787682,
            "density": 0,
        },
        {
            "id": 68,
            "name": "Shells (68)",
            "classname": "item_shells",
            "uuid": 3381132135827646033,
            "density": 0,
        },
        {
            "id": 69,
            "name": "Quad Damage (69)",
            "classname": "item_artifact_super_damage",
            "uuid": 9650020929978725118,
            "density": 0,
        },
        {
            "id": 70,
            "name": "Quad Damage (70)",
            "classname": "item_artifact_super_damage",
            "uuid": 12173380503484776661,
            "density": 0,
        },
        {
            "id": 71,
            "name": "Megahealth (71)",
            "classname": "item_health",
            "uuid": 3104589074171609263,
            "density": 0,
        },
        {
            "id": 72,
            "name": "Spikes (72)",
            "classname": "item_spikes",
            "uuid": 14627959669964208033,
            "density": 0,
        },
        {
            "id": 73,
            "name": "Rockets (73)",
            "classname": "item_rockets",
            "uuid": 16815657400307567179,
            "density": 0,
        },
        {
            "id": 74,
            "name": "Invulnerability (74)",
            "classname": "item_artifact_invulnerability",
            "uuid": 1158006098533227368,
            "density": 0,
        },
        {
            "id": 75,
            "name": "Secret (75)",
            "classname": "trigger_secret",
            "uuid": 18052025553512803093,
            "density": 0,
        },
        {
            "id": 76,
            "name": "Lightning (76)",
            "classname": "weapon_lightning",
            "uuid": 5672302365582838570,
            "density": 0,
        },
        {
            "id": 77,
            "name": "Cells (77)",
            "classname": "item_cells",
            "uuid": 14059543538820552793,
            "density": 0,
        },
        {
            "id": 78,
            "name": "Cells (78)",
            "classname": "item_cells",
            "uuid": 4232486699128407908,
            "density": 0,
        },
        {
            "id": 79,
            "name": "Cells (79)",
            "classname": "item_cells",
            "uuid": 15941396770432958396,
            "density": 0,
        },
        {
            "id": 80,
            "name": "Cells (80)",
            "classname": "item_cells",
            "uuid": 9384092384426434154,
            "density": 0,
        },
        {
            "id": 81,
            "name": "Megahealth (81)",
            "classname": "item_health",
            "uuid": 10476912197565079072,
            "density": 0,
        },
        {
            "id": 82,
            "name": "Spikes (82)",
            "classname": "item_spikes",
            "uuid": 6345015749669124071,
            "density": 0,
        },
        {
            "id": 83,
            "name": "Large Medkit (83)",
            "classname": "item_health",
            "uuid": 12865012533451037429,
            "density": 0,
        },
        {
            "id": 84,
            "name": "Large Medkit (84)",
            "classname": "item_health",
            "uuid": 16596777200629249796,
            "density": 0,
        },
        {
            "id": 85,
            "name": "Rockets (85)",
            "classname": "item_rockets",
            "uuid": 10609096349004999957,
            "density": 0,
        },
    ]

    must_bio = True

    def main_region(self) -> Region:
        r = self.rules

        ret = self.region(
            self.name,
            [
                "Shells (31)",
                "Large Medkit (22)",
                "Small Medkit (23)",
                "Spikes (24)",
            ],
        )

        dive_area = self.region(
            "Dive Area",
            [
                "Shells (68)",
                "Large Medkit (26)",
                "Rockets (85)",
                "Spikes (82)",
                "Supernailgun (17)",
                "Nailgun (21)",
                "Grenadelauncher (64)",
                "Secret (27)",
                "Shells (18)",
                "Quad Damage (69)",
                "Spikes (20)",
                "Yellow Armor (19)",
                "Rockets (13)",
                "Rockets (73)",
                "Grenadelauncher (49)",
                "Large Medkit (51)",
                "Rockets (50)",
                "Rockets (12)",
                "Large Medkit (11)",
                "Shells (14)",
                "Large Medkit (52)",
                "Rocketlauncher (10)",
                "Green Armor (35)",
                "Small Medkit (15)",
                "Small Medkit (53)",
                "Cells (79)",
                "Cells (80)",
                "Gold Key (48)",
                "Yellow Armor (47)",
            ],
        )
        self.connect(ret, dive_area, r.can_dive)

        past_acid_lake_area = self.region(
            "Past Acid Lake",
            [
                "Large Medkit (38)",
                "Large Medkit (39)",
                "Small Medkit (59)",
                "Large Medkit (58)",
                "Quad Damage (36)",
            ],
        )
        self.connect(dive_area, past_acid_lake_area, (r.bigjump & r.difficulty("hard")))
        self.restrict(
            "Quad Damage (36)", r.can_dive & (r.biosuit(1) | r.difficulty("hard"))
        )

        upper_secret_area = self.region(
            "Upper Secret Area",
            [
                "Quad Damage (70)",
                "Megahealth (71)",
                "Spikes (72)",
            ],
        )
        self.connect(
            past_acid_lake_area, upper_secret_area, r.can_door & r.can_shootswitch
        )
        acid_lake_middle = self.region(
            "Acid Lake Middle",
            [
                "Shells (67)",
                "Small Medkit (37)",
                "Green Armor (2)",
                "Large Medkit (83)",
                "Large Medkit (84)",
                "Secret (25)",
                "Red Armor (4)",
                "Biosuit (3)",
            ],
        )
        # TODO Check if this amount is correct
        silver_key_platform = self.region(
            "Silver Key Platform",
            [
                "Silver Key (1)",
                "Spikes (56)",
                "Shells (57)",
            ],
        )
        self.connect(
            acid_lake_middle,
            silver_key_platform,
            (r.bigjump & r.difficulty("hard")) | (r.can_button & r.jump),
        )
        self.connect(
            past_acid_lake_area, acid_lake_middle, r.bigjump & r.difficulty("hard")
        )
        self.restrict(
            "Secret (25)", (r.can_dive & r.biosuit(1)) | r.difficulty("extreme")
        )
        self.restrict(
            "Red Armor (4)", (r.can_dive & r.biosuit(1)) | r.difficulty("extreme")
        )
        self.restrict(
            "Biosuit (3)", (r.can_dive & r.biosuit(1)) | r.difficulty("extreme")
        )

        past_barrier = self.region(
            "Past Barrier",
            [
                "Large Medkit (54)",
                "Spikes (34)",
                "Rockets (33)",
                "Large Medkit (32)",
                "Large Medkit (42)",
                "Spikes (41)",
                "Rockets (40)",
                "Shells (55)",
                "Spikes (46)",
                "Large Medkit (43)",
                "Large Medkit (44)",
                "Small Medkit (45)",
                "Biosuit (66)",
            ],
        )
        self.connect(
            dive_area, past_barrier, (r.bigjump & r.difficulty("hard")) | r.can_button
        )

        past_gold_door_area = self.region(
            "Past Gold Door",
            [
                "Yellow Armor (16)",
                "Spikes (65)",
            ],
        )
        self.connect(past_barrier, past_gold_door_area, self.gold_key)
        self.connect(past_barrier, acid_lake_middle, r.can_button)
        self.connect(acid_lake_middle, past_acid_lake_area)

        barrier_secrets_area = self.region(
            "Barrier Secrets",
            [
                "Secret (28)",
                "Rockets (30)",
                "Megahealth (29)",
                "Secret (75)",
                "Megahealth (81)",
                "Invulnerability (74)",
            ],
        )
        self.connect(past_barrier, barrier_secrets_area, r.can_shootswitch)

        past_silver_door_area = self.region(
            "Past Silver Door",
            [
                "Shells (60)",
                "Rockets (62)",
                "Shells (61)",
                "Small Medkit (63)",
            ],
        )
        self.connect(past_acid_lake_area, past_silver_door_area, self.silver_key)

        silver_upstairs_area = self.region(
            "Silver Upstairs Area",
            [
                "Cells (77)",
                "Lightning (76)",
                "Cells (78)",
            ],
        )
        self.connect(
            past_silver_door_area,
            silver_upstairs_area,
            r.can_button | (r.bigjump & r.difficulty("hard")),
        )
        final_area = self.region(
            "Final Area",
            [
                "Shells (5)",
                "Large Medkit (6)",
                "Large Medkit (7)",
                "Shells (8)",
                "Exit",
            ],
        )
        self.connect(silver_upstairs_area, final_area, r.can_shootswitch & r.can_button)
        self.restrict("Exit", r.can_door)

        return ret
