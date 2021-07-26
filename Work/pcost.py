import csv


def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            name, shares, price = row
            try:
                shares = int(shares)
                price = float(price)
            except ValueError:
                print(f'Error occurred while parsing line: {row!r}')
                continue
            total_cost += shares * price
    return total_cost


cost = portfolio_cost('Data/missing.csv')
print(f'Total cost: {cost}')
