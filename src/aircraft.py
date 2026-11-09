from dataclasses import dataclass
import math

LB_TO_KG = 0.45359237
FT_TO_M = 0.3048
FT2_TO_M2 = 0.09290304
HP_TO_W = 745.7

@dataclass
class Aircraft:
    name: str
    weight_kg: float
    wing_area_m2: float
    wingspan_m: float
    cd0: float
    oswald_e: float
    cl_max: float
    power_sl_w: float
    prop_eff: float

    @property
    def aspect_ratio(self):
        return self.wingspan_m ** 2 / self.wing_area_m2
def cessna_172s():
    return Aircraft(
        name="Cessna 172S",
        weight_kg=2550 * LB_TO_KG,
        wing_area_m2=174 * FT2_TO_M2,
        wingspan_m=36.08 * FT_TO_M,
        cd0 = 0.027,
        oswald_e = 0.75,
        cl_max = 1.5,
        power_sl_w = 180 * HP_TO_W,
        prop_eff = 0.80,
    )
