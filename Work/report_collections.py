from collections import Counter, defaultdict, deque
import csv

def read_portfolio_dict(file_name):
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

portfolio =  read_portfolio_dict('Data/portfolio.csv')

total_shares = Counter()
for (name, shares, price) in portfolio:
    total_shares[name] += (shares)

print("COUNTER: ",total_shares['IBM'])

holdings = defaultdict(list)
for name, shares, price in portfolio:
    holdings[name].append((shares, price))

print("DEFAULT_DICT", holdings['IBM'])  # [ (50, 91.1), (100, 45.23) ]

