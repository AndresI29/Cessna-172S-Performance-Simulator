# scripts/tune.py
from dataclasses import replace
from src.aircraft import cessna_172s
from src.validate import compare

base = cessna_172s()
print(f"{'cd0':>6}{'eta':>6}{'Vmax %':>9}{'ROC %':>9}{'Ceil %':>9}{'Range %':>9}")
for cd0 in [0.027, 0.030, 0.033, 0.036]:
    for eta in [0.55, 0.65, 0.75, 0.80]:
        ac = replace(base, cd0=cd0, prop_eff=eta)
        try:
            rows = compare(ac)
            e = [r[3] for r in rows]   # stall, vmax, roc, ceiling, range
            print(f"{cd0:>6.3f}{eta:>6.2f}{e[1]:>+9.1f}{e[2]:>+9.1f}{e[3]:>+9.1f}{e[4]:>+9.1f}")
        except (TypeError, ValueError):
            print(f"{cd0:>6.3f}{eta:>6.2f}   model fails at these values")