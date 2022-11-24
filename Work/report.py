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

def report_formatted_out(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    for e in headers:
        print('-' * 10, end =' ')
    print()
    for name, shares, price, change in report:
        temp_price = '$' + f'{price:>0.2f}'
        print(f'{name:>10s} {shares:>10d} {temp_price:>10s} {change:>10.2f}')

def gain_loss_calculator(portfolio_filename, prices_filename):
    portfolio = read_portfolio_dict(portfolio_filename)
    prices = read_prices(prices_filename)
    Total_gain = 0.0
    whole_portfolio_price = 0.0

    for temp in portfolio:
        current_price = prices[temp['name']]
        whole_portfolio_price += current_price * temp['shares']
        Total_gain += (current_price - temp['price']) * temp['shares']

    if (Total_gain > 0):
        print('Total gain is',Total_gain)
    elif(Total_gain < 0):
        print('Total loss is',Total_gain)
    else:
        print('There is no gain or loss')

def make_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio_dict(portfolio_filename)
    prices = read_prices(prices_filename)
    result = []
    for temp in portfolio:
        name = temp['name']
        shares = temp['shares']
        price = prices[temp['name']]
        change = float(price) - float(temp['price'])
        cur_tuple = (name, shares, price, change)
        result.append(cur_tuple)
    return result

report = make_report('Data/portfolio.csv', 'Data/prices.csv')
report_formatted_out(report)