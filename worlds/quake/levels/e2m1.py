from BaseClasses import Region

from ..base_classes import Q1Level


class E2M1(Q1Level):
    name = "The Installation"
    mapfile = "e2m1"
    keys = ["Silver", "Gold"]
    location_defs = [
        {
            "id": 1,
            "name": "Large Medkit (1)",
            "classname": "item_health",
            "uuid": 18042096948245972096,
            "density": 0,
        },
        {
            "id": 2,
            "name": "Large Medkit (2)",
            "classname": "item_health",
            "uuid": 10716399031454063545,
            "density": 0,
        },
        {
            "id": 3,
            "name": "Large Medkit (3)",
            "classname": "item_health",
            "uuid": 18202566381558730076,
            "density": 0,
        },
        {
            "id": 4,
            "name": "Large Medkit (4)",
            "classname": "item_health",
            "uuid": 15412089550125955233,
            "density": 0,
        },
        {
            "id": 5,
            "name": "Green Armor (5)",
            "classname": "item_armor1",
            "uuid": 2036119659446599433,
            "density": 0,
        },
        {
            "id": 6,
            "name": "Shells (6)",
            "classname": "item_shells",
            "uuid": 6027728167817124818,
            "density": 0,
        },
        {
            "id": 7,
            "name": "Rockets (7)",
            "classname": "item_rockets",
            "uuid": 16457058357725113026,
            "density": 0,
        },
        {
            "id": 8,
            "name": "Spikes (8)",
            "classname": "item_spikes",
            "uuid": 3462753840345750248,
            "density": 0,
        },
        {
            "id": 9,
            "name": "Spikes (9)",
            "classname": "item_spikes",
            "uuid": 2585383623667136251,
            "density": 0,
        },
        {
            "id": 10,
            "name": "Rockets (10)",
            "classname": "item_rockets",
            "uuid": 14604460587920252238,
            "density": 0,
        },
        {
            "id": 11,
            "name": "Spikes (11)",
            "classname": "item_spikes",
            "uuid": 333035142507179098,
            "density": 0,
        },
        {
            "id": 12,
            "name": "Shells (12)",
            "classname": "item_shells",
            "uuid": 14604883810566654754,
            "density": 0,
        },
        {
            "id": 13,
            "name": "Small Medkit (13)",
            "classname": "item_health",
            "uuid": 15612302864070446014,
            "density": 0,
        },
        {
            "id": 14,
            "name": "Red Armor (14)",
            "classname": "item_armorInv",
            "uuid": 17527780960175809054,
            "density": 0,
        },
        {
            "id": 15,
            "name": "Rockets (15)",
            "classname": "item_rockets",
            "uuid": 9557837914726841452,
            "density": 0,
        },
        {
            "id": 16,
            "name": "Small Medkit (16)",
            "classname": "item_health",
            "uuid": 18332404333680074451,
            "density": 0,
        },
        {
            "id": 17,
            "name": "Small Medkit (17)",
            "classname": "item_health",
            "uuid": 16147706197090087358,
            "density": 0,
        },
        {
            "id": 18,
            "name": "Shells (18)",
            "classname": "item_shells",
            "uuid": 17667408151335331381,
            "density": 0,
        },
        {
            "id": 19,
            "name": "Spikes (19)",
            "classname": "item_spikes",
            "uuid": 7479299425165821499,
            "density": 0,
        },
        {
            "id": 20,
            "name": "Rockets (20)",
            "classname": "item_rockets",
            "uuid": 1168398719536068923,
            "density": 0,
        },
        {
            "id": 21,
            "name": "Megahealth (21)",
            "classname": "item_health",
            "uuid": 6809906935508825147,
            "density": 0,
        },
        {
            "id": 22,
            "name": "Red Armor (22)",
            "classname": "item_armorInv",
            "uuid": 6175477700044988635,
            "density": 0,
        },
        {
            "id": 23,
            "name": "Large Medkit (23)",
            "classname": "item_health",
            "uuid": 15852745702585835322,
            "density": 0,
        },
        {
            "id": 24,
            "name": "Large Medkit (24)",
            "classname": "item_health",
            "uuid": 6528023009515514455,
            "density": 0,
        },
        {
            "id": 25,
            "name": "Large Medkit (25)",
            "classname": "item_health",
            "uuid": 841474359105826395,
            "density": 0,
        },
        {
            "id": 26,
            "name": "Large Medkit (26)",
            "classname": "item_health",
            "uuid": 2680012298887648233,
            "density": 0,
        },
        {
            "id": 27,
            "name": "Megahealth (27)",
            "classname": "item_health",
            "uuid": 2010929341372034402,
            "density": 0,
        },
        {
            "id": 28,
            "name": "Spikes (28)",
            "classname": "item_spikes",
            "uuid": 8136164774706607213,
            "density": 0,
        },
        {
            "id": 29,
            "name": "Shells (29)",
            "classname": "item_shells",
            "uuid": 17851219634655348583,
            "density": 0,
        },
        {
            "id": 30,
            "name": "Shells (30)",
            "classname": "item_shells",
            "uuid": 11796234358783109652,
            "density": 0,
        },
        {
            "id": 31,
            "name": "Shells (31)",
            "classname": "item_shells",
            "uuid": 1571891741286696385,
            "density": 0,
        },
        {
            "id": 32,
            "name": "Supershotgun (32)",
            "classname": "weapon_supershotgun",
            "uuid": 11673895759988009763,
            "density": 0,
        },
        {
            "id": 33,
            "name": "Rockets (33)",
            "classname": "item_rockets",
            "uuid": 12809322500894971751,
            "density": 0,
        },
        {
            "id": 34,
            "name": "Spikes (34)",
            "classname": "item_spikes",
            "uuid": 17713500615573807861,
            "density": 0,
        },
        {
            "id": 35,
            "name": "Shells (35)",
            "classname": "item_shells",
            "uuid": 5010192372980412183,
            "density": 0,
        },
        {
            "id": 36,
            "name": "Yellow Armor (36)",
            "classname": "item_armor2",
            "uuid": 3351839516526583835,
            "density": 0,
        },
        {
            "id": 37,
            "name": "Supershotgun (37)",
            "classname": "weapon_supershotgun",
            "uuid": 10546313313577986012,
            "density": 0,
        },
        {
            "id": 38,
            "name": "Grenadelauncher (38)",
            "classname": "weapon_grenadelauncher",
            "uuid": 6608333453499799383,
            "density": 0,
        },
        {
            "id": 39,
            "name": "Rocketlauncher (39)",
            "classname": "weapon_rocketlauncher",
            "uuid": 110099793261844774,
            "density": 0,
        },
        {
            "id": 40,
            "name": "Red Armor (40)",
            "classname": "item_armorInv",
            "uuid": 12984190670509583560,
            "density": 0,
        },
        {
            "id": 41,
            "name": "Gold Key (41)",
            "classname": "item_key2",
            "uuid": 2177673008264897208,
            "density": 0,
        },
        {
            "id": 42,
            "name": "Green Armor (42)",
            "classname": "item_armor1",
            "uuid": 1345821246466337287,
            "density": 0,
        },
        {
            "id": 43,
            "name": "Spikes (43)",
            "classname": "item_spikes",
            "uuid": 9901410440473228119,
            "density": 0,
        },
        {
            "id": 44,
            "name": "Shells (44)",
            "classname": "item_shells",
            "uuid": 17397571466961763877,
            "density": 0,
        },
        {
            "id": 45,
            "name": "Shells (45)",
            "classname": "item_shells",
            "uuid": 10550943264642079813,
            "density": 0,
        },
        {
            "id": 46,
            "name": "Large Medkit (46)",
            "classname": "item_health",
            "uuid": 12708122102808965486,
            "density": 0,
        },
        {
            "id": 47,
            "name": "Large Medkit (47)",
            "classname": "item_health",
            "uuid": 6028552011574621770,
            "density": 0,
        },
        {
            "id": 48,
            "name": "Large Medkit (48)",
            "classname": "item_health",
            "uuid": 13009123172967780369,
            "density": 0,
        },
        {
            "id": 49,
            "name": "Small Medkit (49)",
            "classname": "item_health",
            "uuid": 17860881637276942799,
            "density": 0,
        },
        {
            "id": 50,
            "name": "Shells (50)",
            "classname": "item_shells",
            "uuid": 1105737432532320741,
            "density": 0,
        },
        {
            "id": 51,
            "name": "Large Medkit (51)",
            "classname": "item_health",
            "uuid": 13078573959619452268,
            "density": 0,
        },
        {
            "id": 52,
            "name": "Nailgun (52)",
            "classname": "weapon_nailgun",
            "uuid": 1723538390719059610,
            "density": 0,
        },
        {
            "id": 53,
            "name": "Large Medkit (53)",
            "classname": "item_health",
            "uuid": 10060508714996330650,
            "density": 0,
        },
        {
            "id": 54,
            "name": "Large Medkit (54)",
            "classname": "item_health",
            "uuid": 4630712558538783629,
            "density": 0,
        },
        {
            "id": 55,
            "name": "Small Medkit (55)",
            "classname": "item_health",
            "uuid": 4222458504079357537,
            "density": 0,
        },
        {
            "id": 56,
            "name": "Large Medkit (56)",
            "classname": "item_health",
            "uuid": 2491104974041126983,
            "density": 0,
        },
        {
            "id": 57,
            "name": "Large Medkit (57)",
            "classname": "item_health",
            "uuid": 8648826337317275985,
            "density": 0,
        },
        {
            "id": 58,
            "name": "Shells (58)",
            "classname": "item_shells",
            "uuid": 5538078575805394905,
            "density": 0,
        },
        {
            "id": 59,
            "name": "Shells (59)",
            "classname": "item_shells",
            "uuid": 14049602451180033054,
            "density": 0,
        },
        {
            "id": 60,
            "name": "Small Medkit (60)",
            "classname": "item_health",
            "uuid": 12438197491528001468,
            "density": 0,
        },
        {
            "id": 61,
            "name": "Large Medkit (61)",
            "classname": "item_health",
            "uuid": 12811123638231362192,
            "density": 0,
        },
        {
            "id": 62,
            "name": "Large Medkit (62)",
            "classname": "item_health",
            "uuid": 426499816499759392,
            "density": 0,
        },
        {
            "id": 63,
            "name": "Spikes (63)",
            "classname": "item_spikes",
            "uuid": 17637385827133083337,
            "density": 0,
        },
        {
            "id": 64,
            "name": "Biosuit (64)",
            "classname": "item_artifact_envirosuit",
            "uuid": 13297030875085241694,
            "density": 0,
        },
        {
            "id": 65,
            "name": "Secret (65)",
            "classname": "trigger_secret",
            "uuid": 2512857204079307490,
            "density": 0,
        },
        {
            "id": 66,
            "name": "Secret (66)",
            "classname": "trigger_secret",
            "uuid": 2514299409708273733,
            "density": 0,
        },
        {
            "id": 67,
            "name": "Secret (67)",
            "classname": "trigger_secret",
            "uuid": 4088277775888731740,
            "density": 0,
        },
        {
            "id": 68,
            "name": "Secret (68)",
            "classname": "trigger_secret",
            "uuid": 15203264721366475424,
            "density": 0,
        },
        {
            "id": 69,
            "name": "Secret (69)",
            "classname": "trigger_secret",
            "uuid": 9243347163150006211,
            "density": 0,
        },
        {
            "id": 70,
            "name": "Secret (70)",
            "classname": "trigger_secret",
            "uuid": 6220079770389825254,
            "density": 0,
        },
        {
            "id": 71,
            "name": "Invulnerability (71)",
            "classname": "item_artifact_invulnerability",
            "uuid": 14051447045961805262,
            "density": 0,
        },
        {
            "id": 72,
            "name": "Quad Damage (72)",
            "classname": "item_artifact_super_damage",
            "uuid": 14146575901511372592,
            "density": 0,
        },
        {
            "id": 73,
            "name": "Secret (73)",
            "classname": "trigger_secret",
            "uuid": 6800189208285312692,
            "density": 0,
        },
        {
            "id": 74,
            "name": "Silver Key (74)",
            "classname": "item_key1",
            "uuid": 3216448107344573648,
            "density": 0,
        },
        {
            "id": 75,
            "name": "Exit",
            "classname": "trigger_changelevel",
            "uuid": 7556143448377913985,
            "density": 0,
        },
        {
            "id": 76,
            "name": "Spikes (76)",
            "classname": "item_spikes",
            "uuid": 13684166607523884399,
            "density": 0,
        },
        {
            "id": 77,
            "name": "Large Medkit (77)",
            "classname": "item_health",
            "uuid": 8498129478505109285,
            "density": 0,
        },
        {
            "id": 78,
            "name": "Lightning (78)",
            "classname": "weapon_lightning",
            "uuid": 937430990335512333,
            "density": 0,
        },
        {
            "id": 79,
            "name": "Supernailgun (79)",
            "classname": "weapon_supernailgun",
            "uuid": 59977736463786864,
            "density": 0,
        },
        {
            "id": 80,
            "name": "Silver Key (80)",
            "classname": "item_key1",
            "uuid": 7372249635066669512,
            "density": 0,
        },
    ]

    def main_region(self) -> Region:
        r = self.rules

        ret = self.region(
            self.name,
            [
                "Shells (59)",
                "Large Medkit (46)",
                "Large Medkit (47)",
                "Large Medkit (48)",
                "Small Medkit (49)",
                "Shells (50)",
                "Spikes (28)",
                "Large Medkit (51)",
                "Gold Key (41)",
                "Large Medkit (2)",
                "Large Medkit (1)",
                "Green Armor (5)",
                "Large Medkit (4)",
                "Large Medkit (3)",
                "Spikes (8)",
            ],
        )

        past_ledge_area = self.region(
            "Past Ledge Area",
            [
                "Shells (45)",
                "Megahealth (21)",
                "Silver Key (74)",
                "Supernailgun (79)",
                "Secret (70)",
                "Megahealth (27)",
            ],
        )
        self.connect(ret, past_ledge_area, r.jump | r.can_door)
        self.restrict("Secret (70)", r.can_jump | r.can_rj_hard | r.can_gj_extr)
        self.restrict("Megahealth (27)", r.can_jump | r.can_rj_hard | r.can_gj_extr)

        final_area = self.region(
            "Final Area",
            [
                "Spikes (34)",
                "Shells (35)",
                "Large Medkit (57)",
                "Large Medkit (56)",
                "Lightning (78)",
                "Large Medkit (77)",
                "Spikes (76)",
                "Exit",
            ],
        )
        self.connect(
            ret,
            final_area,
            (r.bigjump & r.difficulty("medium") | (r.can_jump & r.difficulty("hard"))),
        )
        # this requires door because a trigger is linked to it
        self.restrict("Lightning (78)", r.can_door)

        upper_floor_area = self.region(
            "Upper Floor Area",
            [
                "Small Medkit (55)",
                "Large Medkit (54)",
                "Large Medkit (53)",
                "Rockets (20)",
                "Spikes (19)",
                "Shells (31)",
                "Shells (29)",
                "Rocketlauncher (39)",
                "Shells (30)",
                "Shells (6)",
                "Silver Key (80)",
                "Spikes (63)",
                "Rockets (7)",
                "Green Armor (42)",
                "Nailgun (52)",
                "Large Medkit (61)",
                "Small Medkit (60)",
                "Large Medkit (62)",
            ],
        )
        # TODO: Other Path to this
        self.connect(
            ret, upper_floor_area, (r.bigjump & r.difficulty("hard")) | self.gold_key
        )

        first_dive_area = self.region(
            "First Dive Area",
            [
                "Secret (69)",
                "Large Medkit (25)",
                "Supershotgun (37)",
                "Shells (44)",
                "Red Armor (22)",
                "Large Medkit (23)",
                "Large Medkit (26)",
                "Large Medkit (24)",
                "Secret (68)",
                "Red Armor (40)",
                "Spikes (43)",
                "Spikes (9)",
            ],
        )
        self.connect(ret, first_dive_area, r.can_dive)

        second_dive_area = self.region(
            "Second Dive Area",
            [
                "Biosuit (64)",
                "Secret (65)",
                "Shells (12)",
                "Small Medkit (13)",
                "Spikes (11)",
                "Rockets (10)",
                "Grenadelauncher (38)",
                "Secret (66)",
                "Invulnerability (71)",
            ],
        )

        self.connect(past_ledge_area, second_dive_area, r.can_dive & r.can_shootswitch)
        silver_door_area = self.region(
            "Silver Door Area",
            [
                "Shells (58)",
                "Small Medkit (17)",
                "Small Medkit (16)",
                "Shells (18)",
                "Rockets (15)",
                "Secret (67)",
                "Yellow Armor (36)",
                "Red Armor (14)",
                "Secret (73)",
                "Quad Damage (72)",
            ],
        )
        self.connect(upper_floor_area, silver_door_area, r.can_button)
        self.restrict("Secret (73)", r.can_shootswitch)
        self.restrict("Quad Damage (72)", r.can_shootswitch)

        past_silver_door_area = self.region(
            "Past Silver Door Area",
            [
                "Supershotgun (32)",
            ],
        )
        self.connect(final_area, past_silver_door_area, r.can_button)
        self.connect(silver_door_area, past_silver_door_area, self.silver_key)

        return ret
