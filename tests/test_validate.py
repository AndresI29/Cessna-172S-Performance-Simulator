from src.validate import compare, percent_error

def test_percent_error():
    assert abs(percent_error(110, 100) - 10) < 1e-9

def test_compare_resturns_all_rows():
    rows = compare()
    assert len(rows) == 5
    assert all(r[2] > 0 for r in rows)