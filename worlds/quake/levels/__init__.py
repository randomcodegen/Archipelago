from ..base_classes import Q1Episode
from .e1m1 import E1M1
from .e1m2 import E1M2
from .e1m3 import E1M3
from .e1m4 import E1M4
from .e1m5 import E1M5
from .e1m6 import E1M6
from .e1m7 import E1M7
from .e1m8 import E1M8
from .e2m1 import E2M1
from .e2m2 import E2M2
from .e2m3 import E2M3
from .e2m4 import E2M4
from .e2m5 import E2M5
from .e2m6 import E2M6
from .e2m7 import E2M7
from .e3m1 import E3M1
from .e3m2 import E3M2
from .e3m3 import E3M3
from .e3m4 import E3M4
from .e3m5 import E3M5
from .e3m6 import E3M6
from .e3m7 import E3M7
from .e4m1 import E4M1
from .e4m2 import E4M2
from .e4m3 import E4M3
from .e4m4 import E4M4
from .e4m5 import E4M5
from .e4m6 import E4M6
from .e4m7 import E4M7
from .e4m8 import E4M8
from .start import start
from .end import end


class E1(Q1Episode):
    name = "Doomed Dimension"
    levels = [E1M1(), E1M2(), E1M3(), E1M4(), E1M5(), E1M6(), E1M7(), E1M8()]
    maxlevel = len(levels)


class E2(Q1Episode):
    name = "Realm of Black Magic"
    levels = [E2M1(), E2M2(), E2M3(), E2M4(), E2M5(), E2M6(), E2M7()]
    maxlevel = len(levels)


class E3(Q1Episode):
    name = "Netherworld"
    levels = [E3M1(), E3M2(), E3M3(), E3M4(), E3M5(), E3M6(), E3M7()]
    maxlevel = len(levels)


class E4(Q1Episode):
    name = "The Elder World"
    levels = [E4M1(), E4M2(), E4M3(), E4M4(), E4M5(), E4M6(), E4M7(), E4M8()]
    maxlevel = len(levels)


class SL(Q1Episode):
    name = "Special Levels"
    levels = [start(), end()]
    maxlevel = len(levels)


all_episodes = [E1(), E2(), E3(), E4()]
all_eps_incl_special = [E1(), E2(), E3(), E4(), SL()]
all_levels = [level for ep in all_episodes for level in ep.levels]
all_levels_incl_special = [level for ep in all_eps_incl_special for level in ep.levels]
