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


def read_prices(filename):
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices


def make_report(portfolio, prices):
    report = []
    for holding in portfolio:
        name = holding['name']
        shares = holding['shares']
        price = prices[name]
        change = price - holding['price']
        report.append((name, shares, price, change))
    return report


if __name__ == '__main__':
    def main():
        portfolio = read_portfolio('Data/portfolio.csv')
        prices = read_prices('Data/prices.csv')
        start_cost = 0
        current_cost = 0
        for holding in portfolio:
            start_cost += holding['shares'] * holding['price']
            current_cost += holding['shares'] * prices[holding['name']]
        print(f'Start cost: {start_cost:.2f}')
        print(f'Current cost: {current_cost:.2f}')
        print(f'Gain: {current_cost - start_cost:.2f}')


    main()
