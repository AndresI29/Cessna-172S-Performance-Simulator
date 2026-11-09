from src.aircraft import cessna_172s

def test_aspect_ratio():
    ac = cessna_172s()
    assert 7.0 < ac.aspect_ratio < 7.6