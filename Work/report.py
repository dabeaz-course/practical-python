# report.py
#
# Exercise 2.4
import csv

def read_prices(file_name):
    prices = {}
    try:
        with open(file_name, 'rt') as file:
            rows = csv.reader(file)
            for row in rows:
                try:
                    prices[row[0]] = float(row[1])
                except IndexError:
                    print("Error:", row)
                    pass
    except FileNotFoundError:
        print(f"Invalid: Couldn't find {file_name}")
    return prices

def read_portfolio(file_name):
    portfolio = []
    try:
        with open(file_name, 'rt') as file:
            rows = csv.reader(file)
            header = next(rows)
            for row in rows:
                holding = (row[0], int(row[1]), float(row[2]))
                portfolio.append(holding)
    except FileNotFoundError:
        print(f"Invalid: Couldn't find {file_name}")
    return portfolio

def read_portfolio_dict(file_name):
    portfolio = []
    try:
        with open(file_name, 'rt') as file:
            rows = csv.reader(file)
            header = next(rows)
            for row in rows:
                holding = {'name': row[0], 'shares': int(row[1]), 'prices': float(row[2])}
                portfolio.append(holding)
    except FileNotFoundError:
        print(f"Invalid: Couldn't find {file_name}")
    return portfolio

portfolio =  read_portfolio_dict('Data/portfolio.csv')
prices =  read_prices('Data/prices.csv')
selling_value = 0.0
purchase_value = 0.0

for item in portfolio:
    selling_value += item['shares'] * item['prices']
    purchase_value += item['shares'] * prices[item['name']]

print("Purchase Value:", purchase_value, "Selling Value:", selling_value, "Gain:", purchase_value-selling_value)
