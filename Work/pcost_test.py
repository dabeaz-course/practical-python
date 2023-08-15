from pcost import pcost
from os import path

data_dir = path.join(path.dirname(__file__), 'Data')

def test_pcost_1_27():
    assert pcost(path.join(data_dir, 'portfolio.csv')) == 44671.15

def test_pcost_1_31():
    assert pcost(path.join(data_dir, 'missing.csv')) == 27381.15

def test_pcost_2_16():
    assert pcost(path.join(data_dir, 'portfoliodate.csv')) == 44671.15