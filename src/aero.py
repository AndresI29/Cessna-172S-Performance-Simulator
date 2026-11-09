import math

def lift_coefficient(weight_n, rho, velocity, wing_area):
    return 2 * weight_n / (rho * velocity ** 2 * wing_area)

def drag_coefficient(ac, cl):
    return ac.cd0 + cl ** 2 / (math.pi * ac.oswald_e * ac.aspect_ratio)

def lift_to_drag(ac, cl):
    return cl / drag_coefficient(ac, cl)

def cl_max_ld(ac):
    return math.sqrt(math.pi * ac.oswald_e * ac.aspect_ratio * ac.cd0)

def drag_force(ac, rho, velocity, weight_n):
    cl = lift_coefficient(weight_n, rho, velocity, ac.wing_area_m2)
    cd = drag_coefficient(ac, cl)
    return 0.5 * rho * velocity ** 2 * ac.wing_area_m2 * cd