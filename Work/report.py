import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = dict(zip(headers, (row[0], int(row[1]), float(row[2]))))
            portfolio.append(holding)
        return portfolio
