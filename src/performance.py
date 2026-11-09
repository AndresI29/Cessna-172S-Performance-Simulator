import math
from scipy.optimize import brentq
from src.atmosphere import isa
from src.aero import drag_force, drag_coefficient, lift_to_drag, cl_max_ld
from src.propulsion import power_available

G = 9.80665
CEILING_ROC = 0.508

def _weight_n(ac, weight_kg):
    mass = ac.weight_kg if weight_kg is None else weight_kg
    return mass * G

def stall_speed(ac, altitude_m, weight_kg = None):
    _, _, rho, _ = isa(altitude_m)
    w = _weight_n(ac, weight_kg)
    return math.sqrt(2 * w / (rho * ac.wing_area_m2 * ac.cl_max))

def power_required(ac, rho, velocity, weight_n):
    return drag_force(ac, rho, velocity, weight_n) * velocity

def excess_power(ac, altitude_m, velocity, weight_kg = None):
    _, _, rho, _ = isa(altitude_m)
    w = _weight_n(ac, weight_kg)
    return power_available(ac, rho) - power_required(ac, rho, velocity, w)

def v_min_power(ac, altitude_m, weight_kg = None):
    _, _, rho, _ = isa(altitude_m)
    w = _weight_n(ac, weight_kg)
    cl = math.sqrt(3 * math.pi * ac.oswald_e * ac.aspect_ratio * ac.cd0)
    return math.sqrt(2 * w / (rho * ac.wing_area_m2 * cl))

def max_speed(ac, altitude_m, weight_kg = None):
    v_lo = v_min_power(ac, altitude_m, weight_kg)
    if excess_power(ac, altitude_m, v_lo, weight_kg) <= 0:
        return None
    return brentq(lambda v: excess_power(ac, altitude_m, v, weight_kg), v_lo, 200)

def max_rate_of_climb(ac, altitude_m, weight_kg = None):
    v = max(v_min_power(ac, altitude_m, weight_kg), stall_speed(ac, altitude_m, weight_kg))
    return excess_power(ac, altitude_m, v, weight_kg) / _weight_n(ac, weight_kg)

def service_ceiling(ac, weight_kg = None):
    return brentq(lambda h: max_rate_of_climb(ac, h, weight_kg) - CEILING_ROC, 0, 11000)

#------

def max_range(ac, fuel_kg=None, weight_kg=None):
    fuel = ac.fuel_kg if fuel_kg is None else fuel_kg
    w0 = _weight_n(ac, weight_kg)
    w1 = w0 - fuel * G
    ld = lift_to_drag(ac, cl_max_ld(ac))
    c = ac.bsfc_kg_per_j * G
    return ac.prop_eff / c * ld * math.log(w0 / w1)

def max_endurance(ac, altitude_m=0, fuel_kg=None, weight_kg=None):
    fuel = ac.fuel_kg if fuel_kg is None else fuel_kg
    _, _, rho, _ = isa(altitude_m)
    w0 = _weight_n(ac, weight_kg)
    w1 = w0 - fuel * G
    cl = math.sqrt(3 * math.pi * ac.oswald_e * ac.aspect_ratio * ac.cd0)
    cd = drag_coefficient(ac, cl)
    c = ac.bsfc_kg_per_j * G
    return (ac.prop_eff / c * cl ** 1.5 / cd
            * math.sqrt(2 * rho * ac.wing_area_m2)
            * (w1 ** -0.5 - w0 ** -0.5))