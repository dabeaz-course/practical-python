from mortgage import mortgage

def test_mortgage_1_7():
    assert round(mortgage(), 1) == 966266.9

def test_mortgage_1_8():
    assert round(mortgage(1, 12, 1000), 2) == 927989.46