import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row_number, row in enumerate(rows, start=1):
            holding = dict(zip(headers, row))
            try:
                holding['shares'] = int(holding['shares'])
                holding['price'] = float(holding['price'])
            except ValueError:
                print(f'Row {row_number}: Could\'t convert: {row!r}')
                continue
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
    import sys


    def main():
        if len(sys.argv) == 2:
            filename = sys.argv[1]
        else:
            filename = 'Data/portfolio.csv'

        portfolio = read_portfolio(filename)
        prices = read_prices('Data/prices.csv')
        report = make_report(portfolio, prices)

        headers = ('Name', 'Shares', 'Price', 'Change')
        print('{:>10s} {:>10s} {:>10s} {:>10s}'.format(*headers))
        print('-' * 10, '-' * 10, '-' * 10, '-' * 10)

        for name, shares, price, change in report:
            print(f'{name:>10s} {shares:>10d} {"$" + str(round(price, 2)):>10s} {change:>10.2f}')

        start_cost = 0
        current_cost = 0
        for holding in portfolio:
            start_cost += holding['shares'] * holding['price']
            current_cost += holding['shares'] * prices[holding['name']]
        print(f'Start cost: {start_cost:.2f}')
        print(f'Current cost: {current_cost:.2f}')
        print(f'Gain: {current_cost - start_cost:.2f}')


    main()
