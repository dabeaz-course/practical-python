from typing import Any, Dict, List, Tuple

from fileparse import parse_csv


def read_portfolio(filename: str) -> List[Dict[str, Any]]:
    """
    Read a csv-file `filename` to a list of portfolio holdings and return the list.
    """
    with open(filename) as f:
        return parse_csv(
            f,
            select=('name', 'shares', 'price'),
            types=(str, int, float)
        )


def read_prices(filename: str) -> Dict[str, float]:
    """
    Read a csv-file `filename` of price data into a dict mapping names to prices
    and return the dict.
    """
    with open(filename) as f:
        return dict(parse_csv(
            f,
            types=(str, float),
            has_header=False
        ))


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


def main(args: List[str]) -> None:
    if len(args) != 3:
        raise SystemExit(f'Usage: {args[0]} PORTFOLIO_FILE PRICE_FILE')
    portfolio_report(args[1], args[2])


if __name__ == '__main__':
    import sys

    main(sys.argv)
