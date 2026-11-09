import json
from pathlib import Path
from src.aircraft import cessna_172s, LB_TO_KG
from src.performance import (stall_speed, max_speed, max_rate_of_climb, service_ceiling, max_range)

MS_TO_KT = 1.94384
MS_TO_FPM = 196.85
M_TO_FT = 3.28084
M_TO_NM = 1 / 1852

RESERVE_FUEL_KG = 0.75 * 5.7 * 6 * LB_TO_KG

def load_poh():
    path = Path(__file__).resolve().parent.parent / "data" / "poh_172s.json"
    with open(path) as f:
        return json.load(f)

def percent_error(model, ref):
    return (model - ref) / ref * 100

def compare(ac=None):
    ac = ac or cessna_172s()
    poh = load_poh()
    usable = ac.fuel_kg - RESERVE_FUEL_KG
    pairs = [
        ("Stall speed, clean (kt)", stall_speed(ac, 0) * MS_TO_KT, poh["stall_clean_kias"]),
        ("Max speed, sea level (kt)", max_speed(ac, 0) * MS_TO_KT, poh["max_speed_sl_kt"]),
        ("Max climb rate, SL (ft/min)", max_rate_of_climb(ac, 0) * MS_TO_FPM, poh["roc_sl_fpm"]),
        ("Service ceiling (ft)", service_ceiling(ac) * M_TO_FT, poh["service_ceiling_ft"]),
        ("Max range w/ reserve (nm)", max_range(ac, fuel_kg=usable) * M_TO_NM, poh["range_nm"]),
    ]
    return [(n, m, r, percent_error(m, r)) for n, m, r in pairs]

def print_table(rows):
    print(f"{'Quantity':<30}{'Model':>10}{'POH':>10}{'Error %':>10}")
    for name, model, ref, err, in rows:
        print(f"{name:<30}{model:>10.1f}{ref:>10.1f}{err:>+10.1f}")

if __name__ == "__main__":
    print_table(compare())