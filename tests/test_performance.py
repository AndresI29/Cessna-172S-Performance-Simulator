from src.aircraft import cessna_172s
from src.performance import (stall_speed, max_speed, max_rate_of_climb, service_ceiling, max_range, max_endurance)

def test_stall_speed_sea_level():
    ac = cessna_172s()
    assert 25 < stall_speed(ac, 0) < 32

def test_heavier_stalls_faster():
    ac = cessna_172s()
    assert stall_speed(ac, 0, weight_kg = 1200) > stall_speed(ac, 0, weight_kg = 1000)

def test_max_speed_sea_level():
    ac = cessna_172s()
    assert 60 < max_speed(ac, 0) < 80

def test_rate_of_climb_positive_and_drops_with_altitude():
    ac = cessna_172s()
    assert max_rate_of_climb(ac, 0) > max_rate_of_climb(ac, 3000) > 0

def test_service_ceiling_reasonable():
    ac = cessna_172s()
    assert 4000 < service_ceiling(ac) < 10000

#----------
def test_range_reasonable():
    ac = cessna_172s()
    assert 1.0e6 < max_range(ac) < 2.5e6        # meters

def test_endurance_reasonable():
    ac = cessna_172s()
    assert 18000 < max_endurance(ac) < 90000    # seconds, 5-25 hr

def test_less_fuel_less_range():
    ac = cessna_172s()
    assert max_range(ac, fuel_kg=50) < max_range(ac, fuel_kg=100)