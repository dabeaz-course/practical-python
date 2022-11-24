# report.py
#
# Exercise 2.4
import csv

def read_portfolio_tuples(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            temp = (row[0], int(row[1]), float(row[2]))
            portfolio.append(temp)
    return portfolio

def read_portfolio_dict(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            temp = {'name' : row[0], 'shares': int(row[1]), 'price': float(row[2])}
            portfolio.append(temp)
    return portfolio

def read_prices(filename):
    prices_dict = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                name, price = row
                prices_dict[name] = float(price)
            except:
                pass
    return prices_dict

def gain_loss_calculator(portfolio_filename, prices_filename):
    portfolio = read_portfolio_dict(portfolio_filename)
    prices = read_prices(prices_filename)
    Total_gain = 0.0
    whole_portfolio_price = 0.0

    for temp in portfolio:
        current_price = prices[temp['name']]
        print (temp['name'], 'current price is', current_price)
        print (temp['name'], 'price was', temp['price'])
        whole_portfolio_price += current_price * temp['shares']
        print(temp['name'], 'Difference is', (current_price - temp['price']) * temp['shares'])
        Total_gain += (current_price - temp['price']) * temp['shares']
    print('Whole portfolio price is', whole_portfolio_price)

    if (Total_gain > 0):
        print('Total gain is',Total_gain)
    elif(Total_gain < 0):
        print('Total loss is',Total_gain)
    else:
        print('There is no gain or loss')

gain_loss_calculator('Data/portfolio.csv', 'Data/prices.csv')