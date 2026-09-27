from src.atmosphere import isa

def test_sea_level():
    T, P, rho, a = isa(0)
    assert abs(T-288.15) < 0.01
    assert abs(P-101325) < 1
    assert abs(rho - 1.225) < 0.001

def test_11km():
    T, P, rho, a = isa(11000)
    assert abs(T - 216.65) < 0.5