import csv
from typing import Any, Dict, List, Tuple


def read_portfolio(filename: str) -> List[Dict[str, Any]]:
    """
    Read a csv-file `filename` to a list of portfolio holdings and return the list.
    """
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


def read_prices(filename: str) -> Dict[str, float]:
    """
    Read a csv-file `filename` of price data into a dict mapping names to prices
    and return the dict.
    """
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices


def make_report(
        portfolio: List[Dict[str, Any]],
        prices: Dict[str, float]
) -> List[Tuple[str, int, float, float]]:
    """
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    """
    report = []
    for holding in portfolio:
        name = holding['name']
        shares = holding['shares']
        price = prices[name]
        change = price - holding['price']
        report.append((name, shares, price, change))
    return report


def print_report(report: List[Tuple[str, int, float, float]]) -> None:
    """
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    """
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('{:>10s} {:>10s} {:>10s} {:>10s}'.format(*headers))
    print('-' * 10, '-' * 10, '-' * 10, '-' * 10)
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {"$" + str(round(price, 2)):>10s} {change:>10.2f}')


def print_gain(
        portfolio: List[Dict[str, Any]],
        prices: Dict[str, float]
) -> None:
    """
    Print whether `portfolio` gain revenue in current `prices`.
    """
    start_cost = 0
    current_cost = 0
    for holding in portfolio:
        start_cost += holding['shares'] * holding['price']
        current_cost += holding['shares'] * prices[holding['name']]
    print(f'Start cost: {start_cost:.2f}')
    print(f'Current cost: {current_cost:.2f}')
    print(f'Gain: {current_cost - start_cost:.2f}')


def portfolio_report(portfolio_filename: str, prices_filename: str) -> None:
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)
    print_gain(portfolio, prices)


if __name__ == '__main__':
    import sys


    def main():
        portfolio_filename = sys.argv[1] if len(sys.argv) >= 2 else 'Data/portfolio.csv'
        prices_filename = sys.argv[2] if len(sys.argv) == 3 else 'Data/prices.csv'
        portfolio_report(portfolio_filename, prices_filename)


    main()
