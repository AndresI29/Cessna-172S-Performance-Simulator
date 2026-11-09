from src.atmosphere import RHO0

def power_available(ac, rho):
    engine_power = ac.power_sl_w * (rho / RHO0)
    return engine_power * ac.prop_eff

def thrust_available(ac, rho, velocity):
    return power_available(ac, rho) / velocity