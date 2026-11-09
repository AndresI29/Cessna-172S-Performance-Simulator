from src.aircraft import cessna_172s
from src.aero import cl_max_ld, lift_to_drag

def test_max_ld_is_peak():
    ac = cessna_172s()
    cl = cl_max_ld(ac)
    peak = lift_to_drag(ac, cl)
    assert peak > lift_to_drag(ac, cl * 0.8)
    assert peak > lift_to_drag(ac, cl * 1.2)

def test_max_ld_reasonable():
    ac = cessna_172s()
    peak = lift_to_drag(ac, cl_max_ld(ac))
    assert 9 < peak < 13