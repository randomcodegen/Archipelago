from BaseClasses import Region

from ..base_classes import Q1Level


class E4M8(Q1Level):
    name = "The Nameless City"
    mapfile = "e4m8"
    keys = ["Silver", "Gold"]
    location_defs = [
        {
            "id": 1,
            "name": "Large Medkit (1)",
            "classname": "item_health",
            "uuid": 11130801480244191504,
            "density": 0,
        },
        {
            "id": 2,
            "name": "Large Medkit (2)",
            "classname": "item_health",
            "uuid": 13093743429866044850,
            "density": 0,
        },
        {
            "id": 3,
            "name": "Megahealth (3)",
            "classname": "item_health",
            "uuid": 3000312207286062780,
            "density": 0,
        },
        {
            "id": 4,
            "name": "Small Medkit (4)",
            "classname": "item_health",
            "uuid": 11963023041245228376,
            "density": 0,
        },
        {
            "id": 5,
            "name": "Small Medkit (5)",
            "classname": "item_health",
            "uuid": 10312750959736451545,
            "density": 0,
        },
        {
            "id": 6,
            "name": "Small Medkit (6)",
            "classname": "item_health",
            "uuid": 5891574630176544891,
            "density": 0,
        },
        {
            "id": 7,
            "name": "Small Medkit (7)",
            "classname": "item_health",
            "uuid": 4102747506802278685,
            "density": 0,
        },
        {
            "id": 8,
            "name": "Small Medkit (8)",
            "classname": "item_health",
            "uuid": 17694139733124737124,
            "density": 0,
        },
        {
            "id": 9,
            "name": "Spikes (9)",
            "classname": "item_spikes",
            "uuid": 7615326323566944372,
            "density": 0,
        },
        {
            "id": 10,
            "name": "Large Medkit (10)",
            "classname": "item_health",
            "uuid": 11466539703211579399,
            "density": 0,
        },
        {
            "id": 11,
            "name": "Spikes (11)",
            "classname": "item_spikes",
            "uuid": 16269338401385522488,
            "density": 0,
        },
        {
            "id": 12,
            "name": "Shells (12)",
            "classname": "item_shells",
            "uuid": 6518154092837284614,
            "density": 0,
        },
        {
            "id": 13,
            "name": "Spikes (13)",
            "classname": "item_spikes",
            "uuid": 13165744560417049417,
            "density": 0,
        },
        {
            "id": 14,
            "name": "Large Medkit (14)",
            "classname": "item_health",
            "uuid": 7633463973176567799,
            "density": 0,
        },
        {
            "id": 15,
            "name": "Shells (15)",
            "classname": "item_shells",
            "uuid": 12003403441758828933,
            "density": 0,
        },
        {
            "id": 16,
            "name": "Rockets (16)",
            "classname": "item_rockets",
            "uuid": 2401307588473463466,
            "density": 0,
        },
        {
            "id": 17,
            "name": "Shells (17)",
            "classname": "item_shells",
            "uuid": 15886364399393411541,
            "density": 0,
        },
        {
            "id": 18,
            "name": "Large Medkit (18)",
            "classname": "item_health",
            "uuid": 12818614926706142286,
            "density": 0,
        },
        {
            "id": 19,
            "name": "Large Medkit (19)",
            "classname": "item_health",
            "uuid": 17216028469582177665,
            "density": 0,
        },
        {
            "id": 20,
            "name": "Shells (20)",
            "classname": "item_shells",
            "uuid": 18382863623423424295,
            "density": 0,
        },
        {
            "id": 21,
            "name": "Large Medkit (21)",
            "classname": "item_health",
            "uuid": 8886775799482881003,
            "density": 0,
        },
        {
            "id": 22,
            "name": "Large Medkit (22)",
            "classname": "item_health",
            "uuid": 9350977796443942960,
            "density": 0,
        },
        {
            "id": 23,
            "name": "Grenadelauncher (23)",
            "classname": "weapon_grenadelauncher",
            "uuid": 15489591998659227383,
            "density": 0,
        },
        {
            "id": 24,
            "name": "Nailgun (24)",
            "classname": "weapon_nailgun",
            "uuid": 12593447727554405741,
            "density": 0,
        },
        {
            "id": 25,
            "name": "Rocketlauncher (25)",
            "classname": "weapon_rocketlauncher",
            "uuid": 453299517442368358,
            "density": 0,
        },
        {
            "id": 26,
            "name": "Large Medkit (26)",
            "classname": "item_health",
            "uuid": 6543020680590738217,
            "density": 0,
        },
        {
            "id": 27,
            "name": "Rockets (27)",
            "classname": "item_rockets",
            "uuid": 4278115206368645760,
            "density": 0,
        },
        {
            "id": 28,
            "name": "Green Armor (28)",
            "classname": "item_armor1",
            "uuid": 4156571853318931489,
            "density": 0,
        },
        {
            "id": 29,
            "name": "Gold Key (29)",
            "classname": "item_key2",
            "uuid": 9244892672899700249,
            "density": 0,
        },
        {
            "id": 30,
            "name": "Rockets (30)",
            "classname": "item_rockets",
            "uuid": 4595213201883044475,
            "density": 0,
        },
        {
            "id": 31,
            "name": "Spikes (31)",
            "classname": "item_spikes",
            "uuid": 8900017944978920194,
            "density": 0,
        },
        {
            "id": 32,
            "name": "Small Medkit (32)",
            "classname": "item_health",
            "uuid": 8979999138201985766,
            "density": 0,
        },
        {
            "id": 33,
            "name": "Small Medkit (33)",
            "classname": "item_health",
            "uuid": 14555067245593971171,
            "density": 0,
        },
        {
            "id": 34,
            "name": "Green Armor (34)",
            "classname": "item_armor1",
            "uuid": 6632672595408139174,
            "density": 0,
        },
        {
            "id": 35,
            "name": "Shells (35)",
            "classname": "item_shells",
            "uuid": 2411127724025001403,
            "density": 0,
        },
        {
            "id": 36,
            "name": "Large Medkit (36)",
            "classname": "item_health",
            "uuid": 6332206903077578415,
            "density": 0,
        },
        {
            "id": 37,
            "name": "Rockets (37)",
            "classname": "item_rockets",
            "uuid": 4940803249877454721,
            "density": 0,
        },
        {
            "id": 38,
            "name": "Spikes (38)",
            "classname": "item_spikes",
            "uuid": 13577270466066981081,
            "density": 0,
        },
        {
            "id": 39,
            "name": "Shells (39)",
            "classname": "item_shells",
            "uuid": 9699943163596346705,
            "density": 0,
        },
        {
            "id": 40,
            "name": "Large Medkit (40)",
            "classname": "item_health",
            "uuid": 5445969462539511437,
            "density": 0,
        },
        {
            "id": 41,
            "name": "Large Medkit (41)",
            "classname": "item_health",
            "uuid": 11434194650448219117,
            "density": 0,
        },
        {
            "id": 42,
            "name": "Shells (42)",
            "classname": "item_shells",
            "uuid": 10361368970983217349,
            "density": 0,
        },
        {
            "id": 43,
            "name": "Shells (43)",
            "classname": "item_shells",
            "uuid": 6936819036169867105,
            "density": 0,
        },
        {
            "id": 44,
            "name": "Small Medkit (44)",
            "classname": "item_health",
            "uuid": 11870342153210847369,
            "density": 0,
        },
        {
            "id": 45,
            "name": "Large Medkit (45)",
            "classname": "item_health",
            "uuid": 10127356580409216612,
            "density": 0,
        },
        {
            "id": 46,
            "name": "Spikes (46)",
            "classname": "item_spikes",
            "uuid": 6509543446354535965,
            "density": 0,
        },
        {
            "id": 47,
            "name": "Small Medkit (47)",
            "classname": "item_health",
            "uuid": 18127495476491283101,
            "density": 0,
        },
        {
            "id": 48,
            "name": "Red Armor (48)",
            "classname": "item_armorInv",
            "uuid": 11817105378178108916,
            "density": 0,
        },
        {
            "id": 49,
            "name": "Large Medkit (49)",
            "classname": "item_health",
            "uuid": 11962377750744861414,
            "density": 0,
        },
        {
            "id": 50,
            "name": "Rockets (50)",
            "classname": "item_rockets",
            "uuid": 15862578442047527396,
            "density": 0,
        },
        {
            "id": 51,
            "name": "Rockets (51)",
            "classname": "item_rockets",
            "uuid": 16342670172656107279,
            "density": 0,
        },
        {
            "id": 52,
            "name": "Large Medkit (52)",
            "classname": "item_health",
            "uuid": 159710190417101322,
            "density": 0,
        },
        {
            "id": 53,
            "name": "Spikes (53)",
            "classname": "item_spikes",
            "uuid": 6205337804875891598,
            "density": 0,
        },
        {
            "id": 54,
            "name": "Large Medkit (54)",
            "classname": "item_health",
            "uuid": 14515238310028068688,
            "density": 0,
        },
        {
            "id": 55,
            "name": "Silver Key (55)",
            "classname": "item_key1",
            "uuid": 11863699659851810578,
            "density": 0,
        },
        {
            "id": 56,
            "name": "Exit",
            "classname": "trigger_changelevel",
            "uuid": 10355493501450641971,
            "density": 0,
        },
        {
            "id": 57,
            "name": "Rocketlauncher (57)",
            "classname": "weapon_rocketlauncher",
            "uuid": 11457593199143503391,
            "density": 0,
        },
        {
            "id": 58,
            "name": "Quad Damage (58)",
            "classname": "item_artifact_super_damage",
            "uuid": 12639254643843653699,
            "density": 0,
        },
        {
            "id": 59,
            "name": "Quad Damage (59)",
            "classname": "item_artifact_super_damage",
            "uuid": 7237021987099270416,
            "density": 0,
        },
        {
            "id": 60,
            "name": "Quad Damage (60)",
            "classname": "item_artifact_super_damage",
            "uuid": 6275166178405031492,
            "density": 0,
        },
        {
            "id": 61,
            "name": "Invulnerability (61)",
            "classname": "item_artifact_invulnerability",
            "uuid": 15022824402051491206,
            "density": 0,
        },
        {
            "id": 62,
            "name": "Megahealth (62)",
            "classname": "item_health",
            "uuid": 12317631110904036890,
            "density": 0,
        },
        {
            "id": 63,
            "name": "Secret (63)",
            "classname": "trigger_secret",
            "uuid": 14450346568991222332,
            "density": 0,
        },
        {
            "id": 64,
            "name": "Secret (64)",
            "classname": "trigger_secret",
            "uuid": 16496562281409682013,
            "density": 0,
        },
        {
            "id": 65,
            "name": "Secret (65)",
            "classname": "trigger_secret",
            "uuid": 3482189951690709428,
            "density": 0,
        },
        {
            "id": 66,
            "name": "Lightning (66)",
            "classname": "weapon_lightning",
            "uuid": 13637061747027760288,
            "density": 0,
        },
        {
            "id": 67,
            "name": "Rocketlauncher (67)",
            "classname": "weapon_rocketlauncher",
            "uuid": 11808920331161240958,
            "density": 0,
        },
        {
            "id": 68,
            "name": "Supernailgun (68)",
            "classname": "weapon_supernailgun",
            "uuid": 13624723925459901125,
            "density": 0,
        },
        {
            "id": 69,
            "name": "Grenadelauncher (69)",
            "classname": "weapon_grenadelauncher",
            "uuid": 17742865860191680819,
            "density": 0,
        },
        {
            "id": 70,
            "name": "Supershotgun (70)",
            "classname": "weapon_supershotgun",
            "uuid": 14157778957303120121,
            "density": 0,
        },
        {
            "id": 71,
            "name": "Nailgun (71)",
            "classname": "weapon_nailgun",
            "uuid": 11901046016676051762,
            "density": 0,
        },
        {
            "id": 72,
            "name": "Cells (72)",
            "classname": "item_cells",
            "uuid": 4133135731607687398,
            "density": 0,
        },
        {
            "id": 73,
            "name": "Invisibility (73)",
            "classname": "item_artifact_invisibility",
            "uuid": 14282346061165560029,
            "density": 0,
        },
        {
            "id": 74,
            "name": "Supershotgun (74)",
            "classname": "weapon_supershotgun",
            "uuid": 18374064174021753319,
            "density": 0,
        },
        {
            "id": 75,
            "name": "Supernailgun (75)",
            "classname": "weapon_supernailgun",
            "uuid": 754254762610403691,
            "density": 0,
        },
        {
            "id": 76,
            "name": "Supershotgun (76)",
            "classname": "weapon_supershotgun",
            "uuid": 10125854243001859451,
            "density": 0,
        },
        {
            "id": 77,
            "name": "Supernailgun (77)",
            "classname": "weapon_supernailgun",
            "uuid": 1596451430907293786,
            "density": 0,
        },
        {
            "id": 78,
            "name": "Grenadelauncher (78)",
            "classname": "weapon_grenadelauncher",
            "uuid": 10877227159070685125,
            "density": 0,
        },
        {
            "id": 79,
            "name": "Secret (79)",
            "classname": "trigger_secret",
            "uuid": 11587666468855692498,
            "density": 0,
        },
        {
            "id": 80,
            "name": "Cells (80)",
            "classname": "item_cells",
            "uuid": 11879144106290602524,
            "density": 0,
        },
        {
            "id": 81,
            "name": "Cells (81)",
            "classname": "item_cells",
            "uuid": 15942260815318126864,
            "density": 0,
        },
        {
            "id": 82,
            "name": "Cells (82)",
            "classname": "item_cells",
            "uuid": 289167874658501172,
            "density": 0,
        },
        {
            "id": 83,
            "name": "Cells (83)",
            "classname": "item_cells",
            "uuid": 4925526038698134170,
            "density": 0,
        },
        {
            "id": 84,
            "name": "Cells (84)",
            "classname": "item_cells",
            "uuid": 16029241782015829950,
            "density": 0,
        },
        {
            "id": 85,
            "name": "Cells (85)",
            "classname": "item_cells",
            "uuid": 4757550739000125695,
            "density": 0,
        },
        {
            "id": 86,
            "name": "Cells (86)",
            "classname": "item_cells",
            "uuid": 10141682738220735609,
            "density": 0,
        },
        {
            "id": 87,
            "name": "Cells (87)",
            "classname": "item_cells",
            "uuid": 8268609811517610230,
            "density": 0,
        },
        {
            "id": 88,
            "name": "Cells (88)",
            "classname": "item_cells",
            "uuid": 5033164391365597313,
            "density": 0,
        },
        {
            "id": 89,
            "name": "Cells (89)",
            "classname": "item_cells",
            "uuid": 7406524273842490543,
            "density": 0,
        },
        {
            "id": 90,
            "name": "Cells (90)",
            "classname": "item_cells",
            "uuid": 396155739546877388,
            "density": 0,
        },
        {
            "id": 91,
            "name": "Cells (91)",
            "classname": "item_cells",
            "uuid": 5040570327749195327,
            "density": 0,
        },
        {
            "id": 92,
            "name": "Cells (92)",
            "classname": "item_cells",
            "uuid": 16030567163058520364,
            "density": 0,
        },
        {
            "id": 93,
            "name": "Cells (93)",
            "classname": "item_cells",
            "uuid": 15908221401928757583,
            "density": 0,
        },
        {
            "id": 94,
            "name": "Rockets (94)",
            "classname": "item_rockets",
            "uuid": 9347142149647254827,
            "density": 0,
        },
        {
            "id": 95,
            "name": "Lightning (95)",
            "classname": "weapon_lightning",
            "uuid": 8845034171778789452,
            "density": 0,
        },
        {
            "id": 96,
            "name": "Rockets (96)",
            "classname": "item_rockets",
            "uuid": 15233412255631254110,
            "density": 0,
        },
        {
            "id": 97,
            "name": "Cells (97)",
            "classname": "item_cells",
            "uuid": 14031381916861551091,
            "density": 0,
        },
        {
            "id": 98,
            "name": "Cells (98)",
            "classname": "item_cells",
            "uuid": 14573553284016353109,
            "density": 0,
        },
        {
            "id": 99,
            "name": "Cells (99)",
            "classname": "item_cells",
            "uuid": 1117144623151907664,
            "density": 0,
        },
        {
            "id": 100,
            "name": "Quad Damage (100)",
            "classname": "item_artifact_super_damage",
            "uuid": 4316900688286433244,
            "density": 0,
        },
        {
            "id": 101,
            "name": "Invisibility (101)",
            "classname": "item_artifact_invisibility",
            "uuid": 14608878427628410595,
            "density": 0,
        },
        {
            "id": 102,
            "name": "Large Medkit (102)",
            "classname": "item_health",
            "uuid": 18146726965115071434,
            "density": 0,
        },
        {
            "id": 103,
            "name": "Large Medkit (103)",
            "classname": "item_health",
            "uuid": 17544056790685361505,
            "density": 0,
        },
    ]

    def main_region(self) -> Region:
        r = self.rules

        ret = self.region(
            self.name,
            [
                "Megahealth (62)",
                "Cells (92)",
                "Grenadelauncher (23)",
                "Shells (20)",
                "Large Medkit (19)",
                "Large Medkit (45)",
                "Large Medkit (18)",
                "Spikes (46)",
                "Lightning (66)",
                "Supershotgun (74)",
                "Green Armor (34)",
                "Shells (17)",
                "Supershotgun (76)",
                "Shells (35)",
                "Small Medkit (6)",
                "Large Medkit (40)",
                "Large Medkit (2)",
                "Secret (64)",
                "Rocketlauncher (25)",
                "Quad Damage (59)",
                "Cells (80)",
                "Large Medkit (26)",
                "Shells (39)",
                "Spikes (38)",
                "Rockets (37)",
                "Rocketlauncher (67)",
                "Large Medkit (36)",
                "Cells (82)",
                "Cells (83)",
                "Shells (42)",
                "Green Armor (28)",
                "Shells (43)",
                "Rockets (30)",
                "Small Medkit (44)",
                "Spikes (31)",
                "Large Medkit (14)",
                "Shells (15)",
                "Cells (81)",
                "Spikes (13)",
            ],
        )
        self.restrict("Cells (82)", r.can_jump | r.can_rj_hard | r.can_gj_extr)
        self.restrict("Cells (83)", r.can_jump | r.can_rj_hard | r.can_gj_extr)
        self.restrict("Shells (42)", r.can_button | (r.bigjump & r.difficulty("hard")))
        self.restrict(
            "Green Armor (28)", r.can_button | (r.bigjump & r.difficulty("hard"))
        )
        self.restrict("Shells (43)", r.can_door)
        self.restrict("Rockets (30)", r.can_door)
        self.restrict("Small Medkit (44)", r.can_door)
        self.restrict("Spikes (31)", r.can_door)

        self.restrict("Large Medkit (14)", r.can_shootswitch)
        self.restrict("Shells (15)", r.can_shootswitch)
        self.restrict("Cells (81)", r.can_shootswitch)
        self.restrict("Spikes (13)", r.can_shootswitch)

        button_elevator_area = self.region(
            "Button Elevator",
            [
                "Large Medkit (49)",
                "Small Medkit (47)",
                "Rockets (50)",
            ],
        )
        self.connect(ret, button_elevator_area, r.can_button & r.can_shootswitch)

        elevator_jump_area = self.region(
            "Elevator Jump",
            [
                "Large Medkit (102)",
                "Cells (86)",
                "Large Medkit (103)",
                "Cells (72)",
                "Invisibility (73)",
                "Cells (89)",
                "Supernailgun (75)",
                "Cells (88)",
                "Rockets (94)",
                "Invulnerability (61)",
                "Cells (87)",
            ],
        )
        self.connect(button_elevator_area, elevator_jump_area, r.jump)
        self.connect(ret, elevator_jump_area, r.can_button)

        self.restrict("Large Medkit (102)", r.can_door)
        self.restrict("Cells (86)", r.can_door)
        self.restrict("Large Medkit (103)", r.can_door)
        self.restrict("Rockets (94)", r.can_door)
        self.restrict("Invulnerability (61)", r.can_door)
        self.restrict("Cells (87)", r.can_door)

        past_button_area = self.region(
            "Past Button",
            [
                "Large Medkit (10)",
                "Cells (84)",
                "Supernailgun (68)",
                "Cells (85)",
                "Quad Damage (100)",
                "Cells (99)",
                "Large Medkit (52)",
                "Cells (93)",
                "Spikes (53)",
                "Large Medkit (54)",
                "Lightning (95)",
                "Rockets (51)",
                "Cells (98)",
                "Invisibility (101)",
                # TODO: Silver Key might need some ammo requirements
                "Silver Key (55)",
            ],
        )
        self.connect(
            ret,
            past_button_area,
            (r.can_button & r.can_jump)
            | r.can_rj_hard
            | r.can_gj_extr
            | (r.bigjump & r.difficulty("medium")),
        )
        self.restrict("Invisibility (101)", r.can_door)

        jump_button_secret = self.region(
            "Jump Button",
            [
                "Large Medkit (21)",
                "Large Medkit (22)",
                "Rockets (27)",
                "Large Medkit (41)",
                "Quad Damage (58)",
                "Secret (79)",
                "Red Armor (48)",
            ],
        )
        self.connect(
            ret,
            jump_button_secret,
            (r.jump & r.can_button) | (r.bigjump & r.difficulty("extreme")),
        )

        past_silver_door_area = self.region(
            "Past Silver Door",
            [
                "Supershotgun (70)",
                "Secret (63)",
                "Grenadelauncher (69)",
                "Megahealth (3)",
                "Cells (90)",
                "Rockets (16)",
                "Exit",
            ],
        )
        self.connect(elevator_jump_area, past_silver_door_area, self.silver_key)

        past_gold_door_area = self.region(
            "Past Gold Door",
            [
                "Secret (65)",
                "Cells (91)",
                "Nailgun (24)",
                "Large Medkit (1)",
            ],
        )
        self.connect(ret, past_gold_door_area, self.gold_key)

        return ret
