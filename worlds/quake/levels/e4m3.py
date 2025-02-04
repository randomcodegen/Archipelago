from BaseClasses import Region

from ..base_classes import Q1Level


class E4M3(Q1Level):
    name = "The Elder God Shrine"
    mapfile = "e4m3"
    keys = ["Silver", "Gold"]
    location_defs = [
        {
            "id": 1,
            "name": "Large Medkit (1)",
            "classname": "item_health",
            "uuid": 15761594790704459630,
            "density": 4,
        },
        {
            "id": 2,
            "name": "Large Medkit (2)",
            "classname": "item_health",
            "uuid": 1546782975300533748,
            "density": 3,
        },
        {
            "id": 3,
            "name": "Shells (3)",
            "classname": "item_shells",
            "uuid": 5547300218547497500,
            "density": 1,
        },
        {
            "id": 4,
            "name": "Large Medkit (4)",
            "classname": "item_health",
            "uuid": 2001476606140063734,
            "density": 1,
        },
        {
            "id": 5,
            "name": "Spikes (5)",
            "classname": "item_spikes",
            "uuid": 6806182981768470147,
            "density": 3,
        },
        {
            "id": 6,
            "name": "Small Medkit (6)",
            "classname": "item_health",
            "uuid": 16387035033250039981,
            "density": 4,
        },
        {
            "id": 7,
            "name": "Large Medkit (7)",
            "classname": "item_health",
            "uuid": 14138847767242433499,
            "density": 0,
        },
        {
            "id": 8,
            "name": "Small Medkit (8)",
            "classname": "item_health",
            "uuid": 5787274399497723785,
            "density": 0,
        },
        {
            "id": 9,
            "name": "Shells (9)",
            "classname": "item_shells",
            "uuid": 1357767518778708256,
            "density": 3,
        },
        {
            "id": 10,
            "name": "Small Medkit (10)",
            "classname": "item_health",
            "uuid": 11360400561200938862,
            "density": 3,
        },
        {
            "id": 11,
            "name": "Shells (11)",
            "classname": "item_shells",
            "uuid": 13434800103865653178,
            "density": 4,
        },
        {
            "id": 12,
            "name": "Rockets (12)",
            "classname": "item_rockets",
            "uuid": 2957638148678929655,
            "density": 0,
        },
        {
            "id": 13,
            "name": "Large Medkit (13)",
            "classname": "item_health",
            "uuid": 14736648646704306427,
            "density": 1,
        },
        {
            "id": 14,
            "name": "Spikes (14)",
            "classname": "item_spikes",
            "uuid": 5166229677132794929,
            "density": 1,
        },
        {
            "id": 15,
            "name": "Spikes (15)",
            "classname": "item_spikes",
            "uuid": 14721216815415919625,
            "density": 4,
        },
        {
            "id": 16,
            "name": "Spikes (16)",
            "classname": "item_spikes",
            "uuid": 5927983445365849722,
            "density": 4,
        },
        {
            "id": 17,
            "name": "Spikes (17)",
            "classname": "item_spikes",
            "uuid": 1843834661303079561,
            "density": 1,
        },
        {
            "id": 18,
            "name": "Green Armor (18)",
            "classname": "item_armor1",
            "uuid": 12791722574774038454,
            "density": 0,
        },
        {
            "id": 19,
            "name": "Spikes (19)",
            "classname": "item_spikes",
            "uuid": 450912705831782071,
            "density": 4,
        },
        {
            "id": 20,
            "name": "Grenadelauncher (20)",
            "classname": "weapon_grenadelauncher",
            "uuid": 9249338313042502260,
            "density": 0,
        },
        {
            "id": 21,
            "name": "Megahealth (21)",
            "classname": "item_health",
            "uuid": 9227556425277965061,
            "density": 1,
        },
        {
            "id": 22,
            "name": "Rockets (22)",
            "classname": "item_rockets",
            "uuid": 4586290731985904368,
            "density": 3,
        },
        {
            "id": 23,
            "name": "Rockets (23)",
            "classname": "item_rockets",
            "uuid": 3027725418530133852,
            "density": 4,
        },
        {
            "id": 24,
            "name": "Spikes (24)",
            "classname": "item_spikes",
            "uuid": 12290200673017846063,
            "density": 1,
        },
        {
            "id": 25,
            "name": "Silver Key (25)",
            "classname": "item_key1",
            "uuid": 825675624028462295,
            "density": 0,
        },
        {
            "id": 26,
            "name": "Spikes (26)",
            "classname": "item_spikes",
            "uuid": 13038678942923309466,
            "density": 3,
        },
        {
            "id": 27,
            "name": "Spikes (27)",
            "classname": "item_spikes",
            "uuid": 9044593715553557543,
            "density": 4,
        },
        {
            "id": 28,
            "name": "Megahealth (28)",
            "classname": "item_health",
            "uuid": 2383680860032180268,
            "density": 0,
        },
        {
            "id": 29,
            "name": "Rockets (29)",
            "classname": "item_rockets",
            "uuid": 15718620762711007246,
            "density": 0,
        },
        {
            "id": 30,
            "name": "Yellow Armor (30)",
            "classname": "item_armor2",
            "uuid": 5072611397776792033,
            "density": 0,
        },
        {
            "id": 31,
            "name": "Large Medkit (31)",
            "classname": "item_health",
            "uuid": 15790624122476084801,
            "density": 4,
        },
        {
            "id": 32,
            "name": "Gold Key (32)",
            "classname": "item_key2",
            "uuid": 9686135577733236203,
            "density": 0,
        },
        {
            "id": 33,
            "name": "Red Armor (33)",
            "classname": "item_armorInv",
            "uuid": 8042962346297145277,
            "density": 2,
        },
        {
            "id": 34,
            "name": "Rockets (34)",
            "classname": "item_rockets",
            "uuid": 27938546152472179,
            "density": 3,
        },
        {
            "id": 35,
            "name": "Large Medkit (35)",
            "classname": "item_health",
            "uuid": 15090734116213717924,
            "density": 4,
        },
        {
            "id": 36,
            "name": "Large Medkit (36)",
            "classname": "item_health",
            "uuid": 3686106775282685508,
            "density": 4,
        },
        {
            "id": 37,
            "name": "Large Medkit (37)",
            "classname": "item_health",
            "uuid": 16047288600720490627,
            "density": 3,
        },
        {
            "id": 38,
            "name": "Small Medkit (38)",
            "classname": "item_health",
            "uuid": 14000711451726154924,
            "density": 1,
        },
        {
            "id": 39,
            "name": "Spikes (39)",
            "classname": "item_spikes",
            "uuid": 10689808719492275355,
            "density": 1,
        },
        {
            "id": 40,
            "name": "Shells (40)",
            "classname": "item_shells",
            "uuid": 1386062936536695671,
            "density": 0,
        },
        {
            "id": 41,
            "name": "Rockets (41)",
            "classname": "item_rockets",
            "uuid": 12551735446659766530,
            "density": 0,
        },
        {
            "id": 42,
            "name": "Shells (42)",
            "classname": "item_shells",
            "uuid": 11930615074492784659,
            "density": 1,
        },
        {
            "id": 43,
            "name": "Large Medkit (43)",
            "classname": "item_health",
            "uuid": 6506115811545609464,
            "density": 4,
        },
        {
            "id": 44,
            "name": "Shells (44)",
            "classname": "item_shells",
            "uuid": 6363355446907782727,
            "density": 4,
        },
        {
            "id": 45,
            "name": "Shells (45)",
            "classname": "item_shells",
            "uuid": 6920247562713562573,
            "density": 3,
        },
        {
            "id": 46,
            "name": "Grenadelauncher (46)",
            "classname": "weapon_grenadelauncher",
            "uuid": 11060361246207066901,
            "density": 0,
        },
        {
            "id": 47,
            "name": "Rockets (47)",
            "classname": "item_rockets",
            "uuid": 1956855501681883748,
            "density": 1,
        },
        {
            "id": 48,
            "name": "Large Medkit (48)",
            "classname": "item_health",
            "uuid": 5906250631573590341,
            "density": 4,
        },
        {
            "id": 49,
            "name": "Spikes (49)",
            "classname": "item_spikes",
            "uuid": 18171277084260661413,
            "density": 1,
        },
        {
            "id": 50,
            "name": "Small Medkit (50)",
            "classname": "item_health",
            "uuid": 1095849690209467905,
            "density": 1,
        },
        {
            "id": 51,
            "name": "Exit",
            "classname": "trigger_changelevel",
            "uuid": 8903821253751488702,
            "density": 0,
        },
        {
            "id": 52,
            "name": "Large Medkit (52)",
            "classname": "item_health",
            "uuid": 9649386200592751538,
            "density": 4,
        },
        {
            "id": 53,
            "name": "Quad Damage (53)",
            "classname": "item_artifact_super_damage",
            "uuid": 395572097508428641,
            "density": 0,
        },
        {
            "id": 54,
            "name": "Quad Damage (54)",
            "classname": "item_artifact_super_damage",
            "uuid": 6854484422833493608,
            "density": 0,
        },
        {
            "id": 55,
            "name": "Megahealth (55)",
            "classname": "item_health",
            "uuid": 4971549929756561070,
            "density": 0,
        },
        {
            "id": 56,
            "name": "Large Medkit (56)",
            "classname": "item_health",
            "uuid": 17780958345382264192,
            "density": 2,
        },
        {
            "id": 57,
            "name": "Large Medkit (57)",
            "classname": "item_health",
            "uuid": 3626534716533468672,
            "density": 3,
        },
        {
            "id": 58,
            "name": "Secret (58)",
            "classname": "trigger_secret",
            "uuid": 12365435492275040287,
            "density": 0,
        },
        {
            "id": 59,
            "name": "Secret (59)",
            "classname": "trigger_secret",
            "uuid": 16637844468135486844,
            "density": 0,
        },
        {
            "id": 60,
            "name": "Nailgun (60)",
            "classname": "weapon_nailgun",
            "uuid": 10686753102538252514,
            "density": 5,
        },
        {
            "id": 61,
            "name": "Nailgun (61)",
            "classname": "weapon_nailgun",
            "uuid": 9875881924555297743,
            "density": 5,
        },
        {
            "id": 62,
            "name": "Supershotgun (62)",
            "classname": "weapon_supershotgun",
            "uuid": 16781770318278403430,
            "density": 5,
        },
        {
            "id": 63,
            "name": "Lightning (63)",
            "classname": "weapon_lightning",
            "uuid": 9128240606266942570,
            "density": 5,
        },
        {
            "id": 64,
            "name": "Grenadelauncher (64)",
            "classname": "weapon_grenadelauncher",
            "uuid": 5776456715938692422,
            "density": 5,
        },
        {
            "id": 65,
            "name": "Cells (65)",
            "classname": "item_cells",
            "uuid": 1768573811119980636,
            "density": 5,
        },
        {
            "id": 66,
            "name": "Cells (66)",
            "classname": "item_cells",
            "uuid": 9448358355178499635,
            "density": 5,
        },
        {
            "id": 67,
            "name": "Quad Damage (67)",
            "classname": "item_artifact_super_damage",
            "uuid": 6453202365945630338,
            "density": 3,
        },
        {
            "id": 68,
            "name": "Green Armor (68)",
            "classname": "item_armor1",
            "uuid": 15726711857217927346,
            "density": 3,
        },
        {
            "id": 69,
            "name": "Supershotgun (69)",
            "classname": "weapon_supershotgun",
            "uuid": 10783040152594567380,
            "density": 2,
        },
        {
            "id": 70,
            "name": "Rocketlauncher (70)",
            "classname": "weapon_rocketlauncher",
            "uuid": 6082195541732975394,
            "density": 5,
        },
        {
            "id": 71,
            "name": "Lightning (71)",
            "classname": "weapon_lightning",
            "uuid": 1697945015819249631,
            "density": 5,
        },
        {
            "id": 72,
            "name": "Quad Damage (72)",
            "classname": "item_artifact_super_damage",
            "uuid": 16408695099182349000,
            "density": 5,
        },
        {
            "id": 73,
            "name": "Invisibility (73)",
            "classname": "item_artifact_invisibility",
            "uuid": 3008524786920849077,
            "density": 5,
        },
        {
            "id": 74,
            "name": "Rocketlauncher (74)",
            "classname": "weapon_rocketlauncher",
            "uuid": 6883320408120858277,
            "density": 5,
        },
        {
            "id": 75,
            "name": "Supernailgun (75)",
            "classname": "weapon_supernailgun",
            "uuid": 4543417612369120164,
            "density": 5,
        },
        {
            "id": 76,
            "name": "Shells (76)",
            "classname": "item_shells",
            "uuid": 16962521192401290665,
            "density": 1,
        },
        {
            "id": 77,
            "name": "Spikes (77)",
            "classname": "item_spikes",
            "uuid": 2482273266167427553,
            "density": 3,
        },
        {
            "id": 78,
            "name": "Quad Damage (78)",
            "classname": "item_artifact_super_damage",
            "uuid": 9190210804979694049,
            "density": 0,
        },
        {
            "id": 79,
            "name": "Spikes (79)",
            "classname": "item_spikes",
            "uuid": 4841839984631187964,
            "density": 3,
        },
        {
            "id": 80,
            "name": "Spikes (80)",
            "classname": "item_spikes",
            "uuid": 2857707764206758069,
            "density": 4,
        },
        {
            "id": 81,
            "name": "Rockets (81)",
            "classname": "item_rockets",
            "uuid": 4574549905671064064,
            "density": 3,
        },
        {
            "id": 82,
            "name": "Spikes (82)",
            "classname": "item_spikes",
            "uuid": 3072411123897089079,
            "density": 3,
        },
        {
            "id": 83,
            "name": "Invisibility (83)",
            "classname": "item_artifact_invisibility",
            "uuid": 9702844477754384125,
            "density": 5,
        },
        {
            "id": 84,
            "name": "Secret (84)",
            "classname": "trigger_secret",
            "uuid": 1483928915432705123,
            "density": 0,
        },
        {
            "id": 85,
            "name": "Spikes (85)",
            "classname": "item_spikes",
            "uuid": 5808282553179752183,
            "density": 0,
        },
        {
            "id": 86,
            "name": "Shells (86)",
            "classname": "item_shells",
            "uuid": 190652569478174030,
            "density": 1,
        },
        {
            "id": 87,
            "name": "Invisibility (87)",
            "classname": "item_artifact_invisibility",
            "uuid": 14562135202562479897,
            "density": 0,
        },
        {
            "id": 88,
            "name": "Small Medkit (88)",
            "classname": "item_health",
            "uuid": 6938794786215391761,
            "density": 1,
        },
        {
            "id": 89,
            "name": "Invisibility (89)",
            "classname": "item_artifact_invisibility",
            "uuid": 10111509878285745578,
            "density": 5,
        },
        {
            "id": 90,
            "name": "Shells (90)",
            "classname": "item_shells",
            "uuid": 11886205458535022059,
            "density": 4,
        },
        {
            "id": 91,
            "name": "Shells (91)",
            "classname": "item_shells",
            "uuid": 15147524366737799050,
            "density": 3,
        },
        {
            "id": 92,
            "name": "Quad Damage (92)",
            "classname": "item_artifact_super_damage",
            "uuid": 7547614093850721080,
            "density": 0,
        },
        {
            "id": 93,
            "name": "Small Medkit (93)",
            "classname": "item_health",
            "uuid": 17238516651199192632,
            "density": 1,
        },
    ]

    def main_region(self) -> Region:
        r = self.rules

        ret = self.region(
            self.name,
            [
                "Small Medkit (6)",
                "Nailgun (61)",
                "Small Medkit (10)",
                "Spikes (39)",
                "Megahealth (55)",
            ],
        )

        start_upper_area = self.region(
            "Start Upper",
            [
                "Megahealth (28)",
                "Rockets (29)",
            ],
        )
        self.connect(
            ret,
            start_upper_area,
            (r.can_jump & r.difficulty("hard"))
            | r.can_gj_extr
            | r.can_rj_hard
            | (r.bigjump & r.difficulty("hard")),
        )

        upper_past_door_area = self.region(
            "Upper Past Door",
            [
                "Spikes (85)",
                "Shells (90)",
                "Spikes (26)",
                "Spikes (27)",
                "Shells (86)",
                "Yellow Armor (30)",
                "Supernailgun (75)",
                "Small Medkit (38)",
                "Invisibility (87)",
                "Large Medkit (37)",
                "Small Medkit (88)",
                "Rockets (81)",
                "Shells (76)",
                "Shells (40)",
                "Shells (91)",
                "Large Medkit (4)",
                "Grenadelauncher (64)",
                "Quad Damage (54)",
                "Secret (58)",
                "Large Medkit (57)",
                "Large Medkit (56)",
                "Rockets (12)",
                "Large Medkit (13)",
                "Spikes (5)",
                "Large Medkit (48)",
                "Rockets (41)",
                "Shells (42)",
            ],
        )
        self.connect(start_upper_area, upper_past_door_area, r.can_door)
        self.connect(upper_past_door_area, start_upper_area, r.can_door)

        past_timed_floor_area = self.region(
            "Past Timed Floor",
            [
                "Invisibility (73)",
                "Spikes (79)",
                "Large Medkit (43)",
                "Grenadelauncher (46)",
                "Quad Damage (72)",
                "Rockets (47)",
                "Large Medkit (31)",
                "Silver Key (25)",
                "Lightning (71)",
            ],
        )
        self.connect(
            upper_past_door_area,
            past_timed_floor_area,
            r.difficulty("hard") | r.can_run,
        )

        start_past_shoot_area = self.region(
            "Shootswitch Area",
            [
                "Quad Damage (53)",
                "Spikes (15)",
                "Shells (11)",
                "Spikes (82)",
                "Spikes (49)",
            ],
        )
        self.connect(ret, start_past_shoot_area, r.can_shootswitch)

        past_lower_door_area = self.region(
            "Past Lower Door",
            [
                "Small Medkit (8)",
                "Shells (3)",
                "Large Medkit (2)",
                "Spikes (19)",
                "Spikes (16)",
                "Large Medkit (1)",
                "Supershotgun (62)",
                "Green Armor (18)",
                "Spikes (17)",
                "Shells (9)",
            ],
        )
        self.connect(start_past_shoot_area, past_lower_door_area, r.can_door)

        past_button_area = self.region(
            "Past Button",
            [
                "Spikes (14)",
                "Large Medkit (52)",
                "Shells (45)",
                "Invisibility (83)",
                "Spikes (24)",
                "Large Medkit (7)",
            ],
        )
        self.connect(past_lower_door_area, past_button_area, r.can_button)

        past_button_jumpdive_area = self.region(
            "Past Button Jump-dive",
            [
                "Small Medkit (50)",
                "Grenadelauncher (20)",
                "Quad Damage (78)",
                "Megahealth (21)",
                "Rockets (22)",
                "Nailgun (60)",
                "Rockets (23)",
            ],
        )
        self.connect(past_button_area, past_button_jumpdive_area, r.can_dive & r.jump)
        self.connect(past_button_jumpdive_area, upper_past_door_area)

        button_secret_area = self.region(
            "Button Secret",
            [
                "Secret (59)",
                "Green Armor (68)",
                "Shells (44)",
                "Cells (65)",
                "Supershotgun (69)",
                "Spikes (80)",
                "Quad Damage (67)",
                "Cells (66)",
            ],
        )
        self.connect(upper_past_door_area, button_secret_area, r.can_button)

        button_secret_upper_area = self.region(
            "Button Secret Upper",
            [
                "Red Armor (33)",
                "Large Medkit (36)",
                "Lightning (63)",
                "Rockets (34)",
                "Secret (84)",
                "Spikes (77)",
                "Large Medkit (35)",
            ],
        )
        self.connect(
            upper_past_door_area,
            button_secret_upper_area,
            r.bigjump & r.difficulty("hard"),
        )
        self.connect(button_secret_area, button_secret_upper_area)

        past_gold_door_area = self.region(
            "Past Gold Door",
            [
                "Rocketlauncher (70)",
                "Exit",
            ],
        )
        self.connect(upper_past_door_area, past_gold_door_area, self.gold_key)

        past_silver_door_area = self.region(
            "Past Silver Door",
            [
                "Quad Damage (92)",
                "Invisibility (89)",
                "Small Medkit (93)",
                "Rocketlauncher (74)",
                "Gold Key (32)",
            ],
        )
        self.connect(upper_past_door_area, past_silver_door_area, self.silver_key)

        return ret
