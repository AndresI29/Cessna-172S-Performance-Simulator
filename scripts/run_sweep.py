import os
import numpy as np
import matplotlib.pyplot as plt

from src.aircraft import cessna_172s
from src.atmosphere import isa
from src.propulsion import power_available
from src.performance import (stall_speed, max_speed, max_rate_of_climb, service_ceiling, power_required, G)

MS_TO_KT = 1.94384
MS_TO_FPM = 196.85
M_TO_FT = 3.28084
W_TO_HP = 1 / 745.7

os.makedirs("plots", exist_ok=True)
ac = cessna_172s()
w_n = ac.weight_kg * G

vmax = max_speed(ac, 0)
print(f"Stall speed:     {stall_speed(ac, 0) * MS_TO_KT:.1f} kt")
print(f"Max speed:       {vmax * MS_TO_KT:.1f} kt")
print(f"Max climb rate:  {max_rate_of_climb(ac, 0) * MS_TO_FPM:.0f} ft/min")
print(f"Service ceiling: {service_ceiling(ac) * M_TO_FT:.0f} ft")

plt.figure()
for h in [0, 2000, 4000]:
    _, _, rho, _ = isa(h)
    v = np.linspace(stall_speed(ac, h), 80, 200)
    pr = [power_required(ac, rho, vi, w_n) * W_TO_HP for vi in v]
    pa = power_available(ac, rho) * W_TO_HP
    line, = plt.plot(v * MS_TO_KT, pr, label=f"Required, {h * M_TO_FT:.0f} ft")
    plt.axhline(pa, color=line.get_color(), linestyle="--")
plt.xlabel("Airspeed (kt)")
plt.ylabel("Power (hp)")
plt.title("Power required (solid) vs available (dashed)")
plt.legend()
plt.grid(True)
plt.savefig("plots/power_curves.png", dpi=200)

alts = np.arange(0, 6001, 250)
plt.figure()
for wt in [1000, ac.weight_kg, 1100]:
    roc = [max_rate_of_climb(ac, h, wt) * MS_TO_FPM for h in alts]
    plt.plot(roc, alts * M_TO_FT, label=f"{wt:.0f} kg")
plt.axvline(100, color="gray", linestyle=":")
plt.xlabel("Max rate of climb (ft/min)")
plt.ylabel("Altitude (ft)")
plt.title("Climb performance vs altitude and weight")
plt.legend()
plt.grid(True)
plt.savefig("plots/climb_vs_altitude.png", dpi=200)

vs = [stall_speed(ac, h) * MS_TO_KT for h in alts]
vm = [(max_speed(ac, h) or np.nan) * MS_TO_KT for h in alts]
plt.figure()
plt.plot(vs, alts * M_TO_FT, label="Stall speed")
plt.plot(vm, alts * M_TO_FT, label="Max speed")
plt.xlabel("Airspeed (kt)")
plt.ylabel("Altitude (ft)")
plt.title("Speed envelope vs altitude")
plt.legend()
plt.grid(True)
plt.savefig("plots/speed_envelope.png", dpi=200)

plt.show()