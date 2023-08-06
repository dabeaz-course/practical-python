from report import read_portfolio, read_portfolio_2_5, read_prices_2_6, get_gainloss_2_7

def test_read_portfolio_2_4():
    portfolio = read_portfolio('Data/portfolio.csv')
    assert portfolio == [
        ('AA', 100, 32.2),
        ('IBM', 50, 91.1),
        ('CAT', 150, 83.44),
        ('MSFT', 200, 51.23),
        ('GE', 95, 40.37),
        ('MSFT', 50, 65.1),
        ('IBM', 100, 70.44)
    ]

def test_read_portfolio_2_5():
    portfolio = read_portfolio_2_5('Data/portfolio.csv')
    assert portfolio == [
        {'name': 'AA', 'shares': 100, 'price': 32.2}, {'name': 'IBM', 'shares': 50, 'price': 91.1},
        {'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'MSFT', 'shares': 200, 'price': 51.23},
        {'name': 'GE', 'shares': 95, 'price': 40.37}, {'name': 'MSFT', 'shares': 50, 'price': 65.1},
        {'name': 'IBM', 'shares': 100, 'price': 70.44}
    ]

def test_read_prices_2_6():
    prices = read_prices_2_6('Data/prices.csv')
    assert prices['AA'] == 9.22
    assert prices['AXP'] == 24.85
    assert prices['IBM'] == 106.28
    assert prices['MSFT'] == 20.89

def test_get_gainloss_2_7():
    gain_loss = get_gainloss_2_7('Data/portfolio.csv', 'Data/prices.csv')
    assert round(gain_loss, 2) == -15985.05