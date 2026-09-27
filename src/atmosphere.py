#Sea level constants
T0 = 288.15 #sea-level stnd. temp. K
P0 = 101325.0 # sea-level stnd. P.
RHO0 = 1.225 # sea-level stnd. air-density
L = 0.0065 # temp. lapse rate
R = 287.05 # specific gas constant (air)
G0 = 9.80665 # gravitational accel.
GAMMA = 1.4 # ratio of specific heats

def isa(altitude_m):
    if altitude_m>11000:
        raise ValueError
    T = T0 - L * altitude_m
    P = P0 * (T / T0) ** (G0 / (R * L))
    rho = P / (R * T)
    a = (GAMMA * R * T) ** 0.5
    return T, P, rho, a