from BaseClasses import Region

from ..base_classes import Q1Level


class end(Q1Level):
    name = "Shub-Niggurath's Pit"
    mapfile = "end"
    keys = []
    location_defs = [
        {
            "id": 1,
            "name": "Small Medkit (1)",
            "classname": "item_health",
            "uuid": 2807406081173671798,
            "density": 3,
        },
        {
            "id": 2,
            "name": "Cells (2)",
            "classname": "item_cells",
            "uuid": 1646409664802239924,
            "density": 0,
        },
        {
            "id": 3,
            "name": "Rocketlauncher (3)",
            "classname": "weapon_rocketlauncher",
            "uuid": 9388522423299389943,
            "density": 0,
        },
        {
            "id": 4,
            "name": "Supernailgun (4)",
            "classname": "weapon_supernailgun",
            "uuid": 8020637891806663272,
            "density": 1,
        },
        {
            "id": 5,
            "name": "Nailgun (5)",
            "classname": "weapon_nailgun",
            "uuid": 8671673196265361239,
            "density": 0,
        },
        {
            "id": 6,
            "name": "Grenadelauncher (6)",
            "classname": "weapon_grenadelauncher",
            "uuid": 12504333327443376963,
            "density": 1,
        },
        {
            "id": 7,
            "name": "Supershotgun (7)",
            "classname": "weapon_supershotgun",
            "uuid": 16264927517586760079,
            "density": 0,
        },
        {
            "id": 8,
            "name": "Lightning (8)",
            "classname": "weapon_lightning",
            "uuid": 4389128396142960065,
            "density": 0,
        },
        {
            "id": 9,
            "name": "Cells (9)",
            "classname": "item_cells",
            "uuid": 11786520369844374978,
            "density": 1,
        },
        {
            "id": 10,
            "name": "Cells (10)",
            "classname": "item_cells",
            "uuid": 1146784057048151711,
            "density": 0,
        },
        {
            "id": 11,
            "name": "Cells (11)",
            "classname": "item_cells",
            "uuid": 3394876640350365692,
            "density": 3,
        },
        {
            "id": 12,
            "name": "Rockets (12)",
            "classname": "item_rockets",
            "uuid": 8053633075359384557,
            "density": 4,
        },
        {
            "id": 13,
            "name": "Shells (13)",
            "classname": "item_shells",
            "uuid": 12197371829806644241,
            "density": 1,
        },
        {
            "id": 14,
            "name": "Spikes (14)",
            "classname": "item_spikes",
            "uuid": 9639616739261645954,
            "density": 4,
        },
        {
            "id": 15,
            "name": "Large Medkit (15)",
            "classname": "item_health",
            "uuid": 9635621304669487963,
            "density": 3,
        },
        {
            "id": 16,
            "name": "Large Medkit (16)",
            "classname": "item_health",
            "uuid": 10156214422356551421,
            "density": 4,
        },
        {
            "id": 17,
            "name": "Spikes (17)",
            "classname": "item_spikes",
            "uuid": 9224706568130284338,
            "density": 1,
        },
        {
            "id": 18,
            "name": "Spikes (18)",
            "classname": "item_spikes",
            "uuid": 7788206883076179695,
            "density": 4,
        },
        {
            "id": 19,
            "name": "Large Medkit (19)",
            "classname": "item_health",
            "uuid": 618146399911142619,
            "density": 0,
        },
        {
            "id": 20,
            "name": "Large Medkit (20)",
            "classname": "item_health",
            "uuid": 12765703854339288503,
            "density": 1,
        },
        {
            "id": 21,
            "name": "Large Medkit (21)",
            "classname": "item_health",
            "uuid": 16273779103524307657,
            "density": 4,
        },
        {
            "id": 22,
            "name": "Large Medkit (22)",
            "classname": "item_health",
            "uuid": 10545602394889184012,
            "density": 3,
        },
        {
            "id": 23,
            "name": "Large Medkit (23)",
            "classname": "item_health",
            "uuid": 7764979426238857615,
            "density": 4,
        },
        {
            "id": 24,
            "name": "Large Medkit (24)",
            "classname": "item_health",
            "uuid": 4156242784660783687,
            "density": 4,
        },
        {
            "id": 25,
            "name": "Large Medkit (25)",
            "classname": "item_health",
            "uuid": 4179518622371157802,
            "density": 0,
        },
        {
            "id": 26,
            "name": "Rockets (26)",
            "classname": "item_rockets",
            "uuid": 61576815941776782,
            "density": 1,
        },
        {
            "id": 27,
            "name": "Rockets (27)",
            "classname": "item_rockets",
            "uuid": 18198534632908671579,
            "density": 3,
        },
        {
            "id": 28,
            "name": "Large Medkit (28)",
            "classname": "item_health",
            "uuid": 2153267490360316031,
            "density": 0,
        },
        {
            "id": 29,
            "name": "Large Medkit (29)",
            "classname": "item_health",
            "uuid": 652840507600943400,
            "density": 3,
        },
        {
            "id": 30,
            "name": "Spikes (30)",
            "classname": "item_spikes",
            "uuid": 16857214123120725673,
            "density": 3,
        },
        {
            "id": 31,
            "name": "Cells (31)",
            "classname": "item_cells",
            "uuid": 9537097473659600302,
            "density": 0,
        },
        {
            "id": 32,
            "name": "Rockets (32)",
            "classname": "item_rockets",
            "uuid": 7337608181362407663,
            "density": 3,
        },
        {
            "id": 33,
            "name": "Large Medkit (33)",
            "classname": "item_health",
            "uuid": 14399993509494165761,
            "density": 1,
        },
        {
            "id": 34,
            "name": "Large Medkit (34)",
            "classname": "item_health",
            "uuid": 18002526218333277871,
            "density": 4,
        },
        {
            "id": 35,
            "name": "Large Medkit (35)",
            "classname": "item_health",
            "uuid": 9617423028119325118,
            "density": 4,
        },
        {
            "id": 36,
            "name": "Quad Damage (36)",
            "classname": "item_artifact_super_damage",
            "uuid": 15488683914213003845,
            "density": 2,
        },
        {
            "id": 37,
            "name": "Secret (37)",
            "classname": "trigger_secret",
            "uuid": 2217994458590689848,
            "density": 0,
        },
        {
            "id": 38,
            "name": "Exit",
            "classname": "trigger_changelevel",
            "uuid": 1717686674820885145,
            "density": 0,
        },
        # stuck in shubby
        {
            "id": 39,
            "name": "Rocketlauncher (39)",
            "classname": "weapon_rocketlauncher",
            "uuid": 6911995736438897685,
            "density": 5,
        },
        {
            "id": 40,
            "name": "Supernailgun (40)",
            "classname": "weapon_supernailgun",
            "uuid": 13917066065880497695,
            "density": 5,
        },
        {
            "id": 41,
            "name": "Grenadelauncher (41)",
            "classname": "weapon_grenadelauncher",
            "uuid": 9789601791109247293,
            "density": 5,
        },
        {
            "id": 42,
            "name": "Red Armor (42)",
            "classname": "item_armorInv",
            "uuid": 2890181567574919794,
            "density": 5,
        },
        {
            "id": 43,
            "name": "Shells (43)",
            "classname": "item_shells",
            "uuid": 1726262295847131919,
            "density": 1,
        },
    ]

    has_boss = True

    def main_region(self) -> Region:
        r = self.rules

        ret = self.region(
            self.name,
            [],
        )

        dive_area = self.region(
            "Dive Area",
            [
                "Shells (43)",
                "Lightning (8)",
                "Red Armor (42)",
            ],
        )
        self.connect(ret, dive_area, r.can_dive)

        past_door_area = self.region(
            "Past Door",
            [
                "Rockets (12)",
                "Small Medkit (1)",
                "Shells (13)",
                "Supershotgun (7)",
                "Spikes (14)",
                "Cells (9)",
                "Cells (10)",
                "Cells (11)",
                "Large Medkit (24)",
                "Large Medkit (23)",
                "Large Medkit (25)",
                "Rockets (26)",
                "Rockets (27)",
                "Rocketlauncher (3)",
                "Supernailgun (4)",
                "Large Medkit (22)",
                "Large Medkit (21)",
                "Nailgun (5)",
                "Grenadelauncher (6)",
                "Large Medkit (29)",
                "Spikes (18)",
                "Large Medkit (28)",
            ],
        )
        self.connect(dive_area, past_door_area, r.can_door)

        ledge_area = self.region(
            "Ledge Area",
            [
                "Cells (2)",
                "Large Medkit (15)",
                "Spikes (17)",
                "Large Medkit (16)",
                "Large Medkit (19)",
                "Large Medkit (20)",
                "Spikes (30)",
                "Large Medkit (34)",
                "Supernailgun (40)",
                "Cells (31)",
                "Large Medkit (33)",
                "Rockets (32)",
                "Large Medkit (35)",
                "Grenadelauncher (41)",
                "Secret (37)",
                "Quad Damage (36)",
                "Exit",
            ],
        )
        self.connect(past_door_area, ledge_area, r.jump)

        return ret
