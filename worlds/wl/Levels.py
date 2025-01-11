from .Names import LocationName


class WLLevel:
    levelName: str
    levelIDAddress: int
    levelID: int
    exit1Path: int
    exit2Path: int

    def __init__(
        self,
        levelName: str,
        levelIDAddress: int,
        levelID: int,
        exit1Path: int = None,
        exit2Path: int = None,
    ):
        self.levelName = levelName
        self.levelIDAddress = levelIDAddress
        self.levelID = levelID
        self.exit1Path = exit1Path
        self.exit2Path = exit2Path


level_info_dict = {
    # Rice Beach Default
    0x07: WLLevel(LocationName.ricebeach_1_region, 0x23EF2, 0x07, 0x0F),
    0x0F: WLLevel(LocationName.ricebeach_2_region, 0x23EFA, 0x0F, 0x0E),
    0x0E: WLLevel(LocationName.ricebeach_3_region, 0x23EF9, 0x0E, 0x0C, 0x29),
    0x0C: WLLevel(LocationName.ricebeach_4_region, 0x23EF7, 0x0C, 0x19),
    0x19: WLLevel(LocationName.ricebeach_5_region, 0x23F04, 0x19),
    0x29: WLLevel(LocationName.ricebeach_6_region, 0x23F14, 0x29),
    # TODO: Potentially special case for level shuffle
    # Flooded Rice Beach
    # 0x17:       WLLevel(LocationName.ricebeach_1_region, 0x23f02, 0x17,),
    # 0x24:       WLLevel(LocationName.ricebeach_3_region, 0x23ef9, 0x24,),
    0x06: WLLevel(LocationName.mtteapot_7_region, 0x23EF1, 0x06, 0x10),
    # TODO: Special case? exit 2 connects to sherbet
    0x10: WLLevel(LocationName.mtteapot_8_region, 0x23EFB, 0x10, 0x0D),
    0x0D: WLLevel(LocationName.mtteapot_9_region, 0x23EF8, 0x0D, 0x05),
    0x05: WLLevel(LocationName.mtteapot_10_region, 0x23EF0, 0x05, 0x11),
    0x11: WLLevel(LocationName.mtteapot_11_region, 0x23EFC, 0x11, 0x09),
    0x09: WLLevel(LocationName.mtteapot_12_region, 0x23EF4, 0x09, 0x0A),
    0x0A: WLLevel(LocationName.mtteapot_13_region, 0x23EF5, 0x0A),
    0x21: WLLevel(LocationName.sherbetland_14_region, 0x23F0C, 0x21, 0x02),
    0x02: WLLevel(LocationName.sherbetland_15_region, 0x23EED, 0x02, 0x04, 0x08),
    0x04: WLLevel(LocationName.sherbetland_16_region, 0x23EEF, 0x04, 0x18, 0x20),
    0x08: WLLevel(LocationName.sherbetland_17_region, 0x23EF3, 0x08, 0x18),
    0x20: WLLevel(LocationName.sherbetland_18_region, 0x23F0B, 0x20),
    0x18: WLLevel(LocationName.sherbetland_19_region, 0x23F03, 0x18),  # ,0x04),
    0x03: WLLevel(LocationName.stovecanyon_20_region, 0x23EEE, 0x03, 0x15),
    0x15: WLLevel(LocationName.stovecanyon_21_region, 0x23F00, 0x15, 0x16),
    0x16: WLLevel(LocationName.stovecanyon_22_region, 0x23F01, 0x16, 0x27),
    0x27: WLLevel(LocationName.stovecanyon_23_region, 0x23F12, 0x27, 0x1C, 0x1B),
    0x1B: WLLevel(LocationName.stovecanyon_24_region, 0x23F06, 0x1B),
    0x1C: WLLevel(LocationName.stovecanyon_25_region, 0x23F07, 0x1C),
    0x00: WLLevel(LocationName.ssteacup_26_region, 0x23EEB, 0x00, 0x1E),
    0x1E: WLLevel(LocationName.ssteacup_27_region, 0x23F09, 0x1E, 0x1F),
    0x1F: WLLevel(LocationName.ssteacup_28_region, 0x23F0A, 0x1F, 0x0B),
    0x0B: WLLevel(LocationName.ssteacup_29_region, 0x23EF6, 0x0B, 0x14),
    0x14: WLLevel(LocationName.ssteacup_30_region, 0x23EFF, 0x14),
    # TODO: Special case for level shuffle?
    # Drained Parsley Woods
    0x2A: WLLevel(
        LocationName.parsleywoods_31_region,
        0x23F02,
        0x17,
    ),
    0x26: WLLevel(LocationName.parsleywoods_31_region, 0x23F11, 0x26, 0x1D),
    0x1D: WLLevel(LocationName.parsleywoods_32_region, 0x23F08, 0x1D, 0x01),
    0x01: WLLevel(LocationName.parsleywoods_33_region, 0x23EEC, 0x01, 0x13),
    0x13: WLLevel(LocationName.parsleywoods_34_region, 0x23EFE, 0x13, 0x12),
    0x12: WLLevel(LocationName.parsleywoods_35_region, 0x23EFD, 0x12, 0x1A),
    0x1A: WLLevel(LocationName.parsleywoods_36_region, 0x23F05, 0x1A),
    0x25: WLLevel(LocationName.syrupcastle_37_region, 0x23F10, 0x25, 0x22),
    0x22: WLLevel(LocationName.syrupcastle_38_region, 0x23F0D, 0x22, 0x23),
    0x23: WLLevel(LocationName.syrupcastle_39_region, 0x23F0E, 0x23, 0x28),
    0x28: WLLevel(LocationName.syrupcastle_40_region, 0x23F13, 0x28),
}

full_level_list = [
    0x07,
    0x0F,
    0x0E,
    0x0C,
    0x19,
    0x29,
    0x06,
    0x10,
    0x0D,
    0x05,
    0x11,
    0x09,
    0x0A,
    0x21,
    0x02,
    0x04,
    0x08,
    0x20,
    0x18,
    0x03,
    0x15,
    0x16,
    0x27,
    0x1B,
    0x1C,
    0x00,
    0x1E,
    0x1F,
    0x0B,
    0x14,
    0x26,
    0x1D,
    0x01,
    0x13,
    0x12,
    0x1A,
    0x25,
    0x22,
    0x23,
    0x28,
]

location_id_to_level_id = {
    # 0x17 when flooded
    LocationName.ricebeach_1_exit_1: [0x07, 0],
    LocationName.ricebeach_2_exit_1: [0x0F, 0],
    # 0x24 when flooded
    LocationName.ricebeach_3_exit_1: [0x0E, 0],
    LocationName.ricebeach_3_exit_2: [0x0E, 1],
    LocationName.ricebeach_3_treasure: [0x0E, 2],
    LocationName.ricebeach_4_exit_1: [0x0C, 0],
    LocationName.ricebeach_5_exit_1: [0x19, 0],
    LocationName.ricebeach_6_exit_1: [0x29, 0],
    LocationName.ricebeach_boss: [0x19, 1],
    LocationName.mtteapot_7_exit_1: [0x06, 0],
    LocationName.mtteapot_8_exit_1: [0x10, 0],
    LocationName.mtteapot_8_exit_2: [0x10, 1],
    LocationName.mtteapot_9_exit_1: [0x0D, 0],
    LocationName.mtteapot_9_treasure: [0x0D, 2],
    LocationName.mtteapot_10_exit_1: [0x05, 0],
    LocationName.mtteapot_11_exit_1: [0x11, 0],
    LocationName.mtteapot_11_treasure: [0x11, 2],
    LocationName.mtteapot_12_exit_1: [0x09, 0],
    LocationName.mtteapot_13_exit_1: [0x0A, 0],
    LocationName.mtteapot_boss: [0x0A, 0],
    LocationName.sherbetland_14_exit_1: [0x21, 0],
    LocationName.sherbetland_15_exit_1: [0x02, 0],
    LocationName.sherbetland_15_exit_2: [0x02, 1],
    LocationName.sherbetland_16_exit_1: [0x04, 0],
    LocationName.sherbetland_16_exit_2: [0x04, 1],
    LocationName.sherbetland_16_treasure: [0x04, 2],
    LocationName.sherbetland_17_exit_1: [0x08, 0],
    LocationName.sherbetland_17_treasure: [0x08, 2],
    LocationName.sherbetland_18_exit_1: [0x20, 0],
    LocationName.sherbetland_18_treasure: [0x20, 2],
    LocationName.sherbetland_19_exit_1: [0x18, 0],
    LocationName.sherbetland_boss: [0x18, 0],
    LocationName.stovecanyon_20_exit_1: [0x03, 0],
    LocationName.stovecanyon_20_treasure: [0x03, 2],
    LocationName.stovecanyon_21_exit_1: [0x15, 0],
    LocationName.stovecanyon_22_exit_1: [0x16, 0],
    LocationName.stovecanyon_23_exit_1: [0x27, 1],
    LocationName.stovecanyon_23_exit_2: [0x27, 1],
    LocationName.stovecanyon_24_exit_1: [0x1B, 0],
    LocationName.stovecanyon_24_treasure: [0x1B, 2],
    LocationName.stovecanyon_25_exit_1: [0x1C, 0],
    LocationName.stovecanyon_boss: [0x1C, 0],
    LocationName.ssteacup_26_exit_1: [0x00, 0],
    LocationName.ssteacup_26_treasure: [0x00, 2],
    LocationName.ssteacup_27_exit_1: [0x1E, 0],
    LocationName.ssteacup_28_exit_1: [0x1F, 0],
    LocationName.ssteacup_29_exit_1: [0x0B, 0],
    LocationName.ssteacup_29_treasure: [0x0B, 2],
    LocationName.ssteacup_30_exit_1: [0x14, 0],
    LocationName.ssteacup_30_treasure: [0x14, 2],
    LocationName.ssteacup_boss: [0x14, 0],
    # 0x2A when drained
    LocationName.parsleywoods_31_exit_1: [0x26, 0],
    LocationName.parsleywoods_31_treasure: [0x26, 2],
    LocationName.parsleywoods_32_exit_1: [0x1D, 0],
    LocationName.parsleywoods_33_exit_1: [0x01, 0],
    LocationName.parsleywoods_34_exit_1: [0x13, 0],
    LocationName.parsleywoods_34_treasure: [0x13, 2],
    LocationName.parsleywoods_35_exit_1: [0x12, 0],
    LocationName.parsleywoods_36_exit_1: [0x1A, 0],
    LocationName.parsleywoods_boss: [0x1A, 0],
    LocationName.syrupcastle_37_exit_1: [0x25, 0],
    LocationName.syrupcastle_37_treasure: [0x25, 2],
    LocationName.syrupcastle_38_exit_1: [0x22, 0],
    LocationName.syrupcastle_39_exit_1: [0x23, 0],
    LocationName.syrupcastle_39_treasure: [0x23, 2],
    # LocationName.syrupcastle_40_exit_1:     [0x28, 0],
    LocationName.syrupcastle_boss: [0x28, 0],
}


def generate_level_list(world, player):
    """
    # TODO: Implement level shuffle
    if not world.level_shuffle[player]:
        out_level_list = full_level_list.copy()
        return out_level_list

    shuffled_level_list = []
    full_level_list_copy = full_level_list.copy()
    shuffled_level_list.append(world.random.shuffle(full_level_list_copy))
    """
    shuffled_level_list = full_level_list.copy()
    return shuffled_level_list
