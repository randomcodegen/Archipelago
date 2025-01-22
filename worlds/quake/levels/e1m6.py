from BaseClasses import Region

from ..base_classes import Q1Level


class E1M6(Q1Level):
    name = "The Door To Chthon"
    mapfile = "e1m6"
    keys = ["Silver", "Gold"]
    location_defs = [
        {
            "id": 1,
            "name": "Gold Key (1)",
            "classname": "item_key2",
            "uuid": 62472425901730654,
            "density": 0,
        },
        {
            "id": 2,
            "name": "Silver Key (2)",
            "classname": "item_key1",
            "uuid": 14065850060276691230,
            "density": 0,
        },
        {
            "id": 3,
            "name": "Supernailgun (3)",
            "classname": "weapon_supernailgun",
            "uuid": 7938161801874819308,
            "density": 0,
        },
        {
            "id": 4,
            "name": "Large Medkit (4)",
            "classname": "item_health",
            "uuid": 10759627786875032033,
            "density": 0,
        },
        {
            "id": 5,
            "name": "Large Medkit (5)",
            "classname": "item_health",
            "uuid": 817128844994753832,
            "density": 0,
        },
        {
            "id": 6,
            "name": "Large Medkit (6)",
            "classname": "item_health",
            "uuid": 4246855658235781481,
            "density": 0,
        },
        {
            "id": 7,
            "name": "Large Medkit (7)",
            "classname": "item_health",
            "uuid": 3325369842710666608,
            "density": 0,
        },
        {
            "id": 8,
            "name": "Megahealth (8)",
            "classname": "item_health",
            "uuid": 4707738429988205998,
            "density": 0,
        },
        {
            "id": 9,
            "name": "Megahealth (9)",
            "classname": "item_health",
            "uuid": 7929202652540526223,
            "density": 0,
        },
        {
            "id": 10,
            "name": "Shells (10)",
            "classname": "item_shells",
            "uuid": 1541743044851937782,
            "density": 0,
        },
        {
            "id": 11,
            "name": "Supershotgun (11)",
            "classname": "weapon_supershotgun",
            "uuid": 1884982346870901673,
            "density": 0,
        },
        {
            "id": 12,
            "name": "Rocketlauncher (12)",
            "classname": "weapon_rocketlauncher",
            "uuid": 14116489373174057617,
            "density": 0,
        },
        {
            "id": 13,
            "name": "Rockets (13)",
            "classname": "item_rockets",
            "uuid": 9764512594981462861,
            "density": 0,
        },
        {
            "id": 14,
            "name": "Shells (14)",
            "classname": "item_shells",
            "uuid": 18035640491225870544,
            "density": 0,
        },
        {
            "id": 15,
            "name": "Large Medkit (15)",
            "classname": "item_health",
            "uuid": 14018452738023773615,
            "density": 0,
        },
        {
            "id": 16,
            "name": "Rockets (16)",
            "classname": "item_rockets",
            "uuid": 13311147603784758177,
            "density": 0,
        },
        {
            "id": 17,
            "name": "Spikes (17)",
            "classname": "item_spikes",
            "uuid": 17429223549890125864,
            "density": 0,
        },
        {
            "id": 18,
            "name": "Yellow Armor (18)",
            "classname": "item_armor2",
            "uuid": 4030425061721248967,
            "density": 0,
        },
        {
            "id": 19,
            "name": "Yellow Armor (19)",
            "classname": "item_armor2",
            "uuid": 6398168170760029764,
            "density": 0,
        },
        {
            "id": 20,
            "name": "Secret (20)",
            "classname": "trigger_secret",
            "uuid": 9057785361091990607,
            "density": 0,
        },
        {
            "id": 21,
            "name": "Rockets (21)",
            "classname": "item_rockets",
            "uuid": 16220013393548160340,
            "density": 0,
        },
        {
            "id": 22,
            "name": "Secret (22)",
            "classname": "trigger_secret",
            "uuid": 3902772197350461445,
            "density": 0,
        },
        {
            "id": 23,
            "name": "Secret (23)",
            "classname": "trigger_secret",
            "uuid": 2216014167285467641,
            "density": 0,
        },
        {
            "id": 24,
            "name": "Spikes (24)",
            "classname": "item_spikes",
            "uuid": 10528964680205280695,
            "density": 0,
        },
        {
            "id": 25,
            "name": "Exit",
            "classname": "trigger_changelevel",
            "uuid": 7921180550884025243,
            "density": 0,
        },
        {
            "id": 26,
            "name": "Large Medkit (26)",
            "classname": "item_health",
            "uuid": 9992770898993642517,
            "density": 0,
        },
        {
            "id": 27,
            "name": "Shells (27)",
            "classname": "item_shells",
            "uuid": 11098798892930653222,
            "density": 0,
        },
        {
            "id": 28,
            "name": "Spikes (28)",
            "classname": "item_spikes",
            "uuid": 5414347826657034042,
            "density": 0,
        },
        {
            "id": 29,
            "name": "Large Medkit (29)",
            "classname": "item_health",
            "uuid": 15232958627832029480,
            "density": 0,
        },
        {
            "id": 30,
            "name": "Large Medkit (30)",
            "classname": "item_health",
            "uuid": 13172494375702036677,
            "density": 0,
        },
        {
            "id": 31,
            "name": "Rockets (31)",
            "classname": "item_rockets",
            "uuid": 14378887412243510762,
            "density": 0,
        },
        {
            "id": 32,
            "name": "Large Medkit (32)",
            "classname": "item_health",
            "uuid": 2277994046000996121,
            "density": 0,
        },
        {
            "id": 33,
            "name": "Large Medkit (33)",
            "classname": "item_health",
            "uuid": 16765058462931367239,
            "density": 0,
        },
        {
            "id": 34,
            "name": "Quad Damage (34)",
            "classname": "item_artifact_super_damage",
            "uuid": 17706703358698504229,
            "density": 0,
        },
        {
            "id": 35,
            "name": "Megahealth (35)",
            "classname": "item_health",
            "uuid": 7485304358346487464,
            "density": 0,
        },
        {
            "id": 36,
            "name": "Yellow Armor (36)",
            "classname": "item_armor2",
            "uuid": 2845241778946759237,
            "density": 0,
        },
        {
            "id": 37,
            "name": "Secret (37)",
            "classname": "trigger_secret",
            "uuid": 15810978266195218050,
            "density": 0,
        },
        {
            "id": 38,
            "name": "Spikes (38)",
            "classname": "item_spikes",
            "uuid": 2532074184515788248,
            "density": 0,
        },
        {
            "id": 39,
            "name": "Large Medkit (39)",
            "classname": "item_health",
            "uuid": 17530651812898294345,
            "density": 0,
        },
        {
            "id": 40,
            "name": "Large Medkit (40)",
            "classname": "item_health",
            "uuid": 16201046885298216184,
            "density": 0,
        },
        {
            "id": 41,
            "name": "Large Medkit (41)",
            "classname": "item_health",
            "uuid": 972107351389793149,
            "density": 0,
        },
        {
            "id": 42,
            "name": "Rockets (42)",
            "classname": "item_rockets",
            "uuid": 8817083392236961850,
            "density": 0,
        },
        {
            "id": 43,
            "name": "Yellow Armor (43)",
            "classname": "item_armor2",
            "uuid": 14147936563132980899,
            "density": 0,
        },
        {
            "id": 44,
            "name": "Shells (44)",
            "classname": "item_shells",
            "uuid": 254670596436146821,
            "density": 0,
        },
        {
            "id": 45,
            "name": "Spikes (45)",
            "classname": "item_spikes",
            "uuid": 2235854052741403130,
            "density": 0,
        },
        {
            "id": 46,
            "name": "Large Medkit (46)",
            "classname": "item_health",
            "uuid": 2594336487774498042,
            "density": 0,
        },
        {
            "id": 47,
            "name": "Spikes (47)",
            "classname": "item_spikes",
            "uuid": 11675556324824908289,
            "density": 0,
        },
        {
            "id": 48,
            "name": "Rockets (48)",
            "classname": "item_rockets",
            "uuid": 4673804438894620606,
            "density": 0,
        },
        {
            "id": 49,
            "name": "Large Medkit (49)",
            "classname": "item_health",
            "uuid": 8035072949250481622,
            "density": 0,
        },
        {
            "id": 50,
            "name": "Spikes (50)",
            "classname": "item_spikes",
            "uuid": 2307762779942217371,
            "density": 0,
        },
        {
            "id": 51,
            "name": "Small Medkit (51)",
            "classname": "item_health",
            "uuid": 17959571713327917271,
            "density": 0,
        },
        {
            "id": 52,
            "name": "Small Medkit (52)",
            "classname": "item_health",
            "uuid": 3283154149725265700,
            "density": 0,
        },
        {
            "id": 53,
            "name": "Spikes (53)",
            "classname": "item_spikes",
            "uuid": 12675509445804840646,
            "density": 0,
        },
        {
            "id": 54,
            "name": "Rocketlauncher (54)",
            "classname": "weapon_rocketlauncher",
            "uuid": 10069991232957787029,
            "density": 0,
        },
        {
            "id": 55,
            "name": "Supernailgun (55)",
            "classname": "weapon_supernailgun",
            "uuid": 17667632366168721207,
            "density": 0,
        },
        {
            "id": 56,
            "name": "Supershotgun (56)",
            "classname": "weapon_supershotgun",
            "uuid": 10916211653236426891,
            "density": 0,
        },
        {
            "id": 57,
            "name": "Supernailgun (57)",
            "classname": "weapon_supernailgun",
            "uuid": 10488578583324183380,
            "density": 0,
        },
    ]

    events = ["Gold Bridge Moved"]

    def main_region(self) -> Region:
        r = self.rules

        ret = self.region(
            self.name,
            [
                "Large Medkit (7)",
                "Rockets (13)",
                "Shells (14)",
                "Large Medkit (6)",
                "Spikes (24)",
                "Large Medkit (26)",
            ],
        )

        past_gold_key_door_area = self.region(
            "Past Gold Key Door Area",
            [
                "Shells (44)",
            ],
        )
        self.connect(ret, past_gold_key_door_area, self.gold_key)

        gold_door_past_button_area = self.region(
            "Gold Key Door Area - Past Button",
            [
                "Rockets (42)",
                "Spikes (38)",
                "Large Medkit (41)",
                "Supernailgun (55)",
                "Large Medkit (39)",
                "Large Medkit (40)",
                "Yellow Armor (43)",
                "Exit",
            ],
        )
        self.connect(past_gold_key_door_area, gold_door_past_button_area, r.can_button)

        past_button_upper_area = self.region(
            "Past Button Upper Area",
            [
                "Supernailgun (3)",
                "Spikes (28)",
                "Yellow Armor (36)",
            ],
        )

        # can get to this without button ability through the gap above
        self.connect(ret, past_button_upper_area, r.bigjump | r.can_button)

        past_button_area = self.region(
            "Past Button Area",
            [
                "Megahealth (35)",
                "Spikes (53)",
                "Secret (23)",
                "Quad Damage (34)",
                "Rockets (48)",
                "Supershotgun (56)",
                "Large Medkit (49)",
                "Large Medkit (5)",
                "Large Medkit (4)",
                "Rocketlauncher (54)",
                "Shells (27)",
            ],
        )
        self.connect(ret, past_button_area, r.can_button)

        self.restrict(
            "Megahealth (35)", (r.bigjump & r.difficulty("hard")) | r.can_door
        )
        self.restrict("Spikes (53)", (r.bigjump & r.difficulty("hard")) | r.can_door)

        self.restrict("Secret (23)", r.can_shootswitch | r.bigjump)
        self.restrict("Quad Damage (34)", r.can_shootswitch | r.bigjump)

        past_staircase_area = self.region(
            "Past Staircase",
            [
                "Spikes (50)",
                "Small Medkit (51)",
                "Small Medkit (52)",
                "Silver Key (2)",
                "Rocketlauncher (12)",
                "Shells (10)",
                # requires door for lower path
                "Rockets (16)",
                "Megahealth (9)",
                "Secret (37)",
            ],
        )

        self.connect(
            past_button_area,
            past_staircase_area,
            r.can_door
            | (r.bigjump & r.difficulty("medium"))
            | (r.can_jump & r.difficulty("hard"))
            | r.can_gj_hard
            | r.can_rj_hard,
        )
        self.restrict("Rockets (16)", r.can_door)
        self.restrict("Megahealth (9)", r.can_door)
        self.restrict("Secret (37)", r.can_door)

        # you can go past the dark path by lighting it up with shotgun shots, quad damage etc. (or jump towards the top right)
        dark_path_area = self.region(
            "Dark Path Area",
            [
                "Rockets (31)",
                "Supershotgun (11)",
                "Spikes (47)",
                "Large Medkit (29)",
                "Large Medkit (30)",
                "Large Medkit (15)",
            ],
        )
        self.connect(ret, dark_path_area, r.difficulty("medium") | r.can_button)

        self.restrict("Large Medkit (15)", r.can_door)

        gold_key_pickup_area = self.region(
            "Gold Key Pickup Area",
            [
                "Gold Key (1)",
                "Yellow Armor (18)",
            ],
        )

        self.connect(
            ret,
            gold_key_pickup_area,
            (r.difficulty("extreme") & r.can_jump)
            | r.can_rj_hard
            | r.can_gj_extr
            | (r.bigjump & r.difficulty("medium"))
            | self.event("Gold Bridge Moved"),
        )

        behind_silver_door_area = self.region(
            "Behind Silver Door Area",
            [
                "Gold Bridge Moved",
                "Large Medkit (32)",
                "Large Medkit (33)",
            ],
        )
        self.restrict("Gold Bridge Moved", r.can_button)
        self.connect(
            dark_path_area,
            behind_silver_door_area,
            self.silver_key
            & (
                ((r.can_rj_ez | r.can_gj_ez | r.can_jump) & r.difficulty("hard"))
                | r.can_button
            ),
        )
        silver_bridge_door_area = self.region(
            "Silver Bridge Door Area",
            [
                "Spikes (45)",
                "Large Medkit (46)",
            ],
        )
        self.connect(
            dark_path_area, silver_bridge_door_area, self.event("Gold Bridge Moved")
        )

        stair_secret_area = self.region(
            "Stair Secret Area",
            [
                "Secret (20)",
                "Rockets (21)",
                "Secret (22)",
                "Megahealth (8)",
            ],
        )
        self.restrict(
            "Megahealth (8)",
            # slopejump + rj/gj off of the stairslope
            (r.can_shootswitch & r.jump) | (r.difficulty("extreme") & r.bigjump),
        )
        self.restrict("Secret (22)", r.can_shootswitch)
        self.restrict("Rockets (21)", r.can_shootswitch)
        self.restrict("Secret (20)", r.can_shootswitch)
        self.connect(dark_path_area, stair_secret_area, r.can_button)

        return ret
