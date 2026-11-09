from src.aircraft import cessna_172s
from src.atmosphere import isa, RHO0
from src.propulsion import power_available, thrust_available

def test_sea_level_power():
    ac = cessna_172s()
    assert abs(power_available(ac, RHO0) - ac.power_sl_w * ac.prop_eff) < 1

def test_power_drops_with_altitude():
    ac = cessna_172s()
    _, _, rho_low, _ = isa(0)
    _, _, rho_high, _ = isa(3000)
    assert power_available(ac, rho_high) < power_available(ac, rho_low)

def test_thrust_drops_with_speed():
    ac = cessna_172s()
    assert thrust_available(ac, RHO0, 40) > thrust_available(ac, RHO0, 60)