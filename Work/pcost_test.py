from pcost import pcost

def test_pcost_1_27():
    assert pcost('Data/portfolio.csv') == 44671.15

def test_pcost_1_31():
    assert pcost('Data/missing.csv') == 27381.15