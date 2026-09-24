from src.features import hourly_return


def test_hourly_return():
    assert abs(hourly_return(100.0, 102.0) - 0.02) < 1e-12
