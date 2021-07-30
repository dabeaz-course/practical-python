from typing import Dict, List, Tuple

from fileparse import parse_csv
from portfolio import Portfolio
from stock import Stock
from tableformat import TableFormatter, create_formatter


def read_portfolio(filename: str, **kwargs) -> Portfolio:
    """
    Read a csv-file `filename` to a list of portfolio holdings and return the list.
    """
    with open(filename) as f:
        portfolio_as_dicts = parse_csv(
            f,
            select=('name', 'shares', 'price'),
            types=(str, int, float),
            **kwargs
        )
        portfolio = [Stock(**d) for d in portfolio_as_dicts]
        return Portfolio(portfolio)


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
        portfolio: Portfolio,
        prices: Dict[str, float]
) -> List[Tuple[str, int, float, float]]:
    """
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    """
    report = []
    for holding in portfolio:
        name = holding.name
        shares = holding.shares
        price = prices[name]
        change = price - holding.price
        report.append((name, shares, price, change))
    return report


def print_report(
        report: List[Tuple[str, int, float, float]],
        formatter: TableFormatter
) -> None:
    """
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    """
    formatter.headings(('Name', 'Shares', 'Price', 'Change'))
    for name, shares, price, change in report:
        row_data = [f'{name}', f'{shares}', f'{price:.2f}', f'{change:.2f}']
        formatter.row(row_data)


def print_gain(
        portfolio: Portfolio,
        prices: Dict[str, float]
) -> None:
    """
    Print whether `portfolio` gain revenue in current `prices`.
    """
    start_cost = 0
    current_cost = 0
    for holding in portfolio:
        start_cost += holding.cost
        current_cost += holding.shares * prices[holding.name]
    print(f'Start cost: {start_cost:.2f}')
    print(f'Current cost: {current_cost:.2f}')
    print(f'Gain: {current_cost - start_cost:.2f}')


def portfolio_report(
        portfolio_filename: str,
        prices_filename: str,
        fmt: str = 'txt'
) -> None:
    # Read data files.
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    # Create report data.
    report = make_report(portfolio, prices)

    # Print report data.
    formatter = create_formatter(fmt)
    print_report(report, formatter)
    print_gain(portfolio, prices)


def main(args: List[str]) -> None:
    if len(args) not in (3, 4):
        raise SystemExit(f'Usage: {args[0]} PORTFOLIO_FILE PRICE_FILE [REPORT_FORMAT: txt, csv, html]')
    if len(args) == 3:
        portfolio_report(portfolio_filename=args[1], prices_filename=args[2])
    else:
        portfolio_report(portfolio_filename=args[1], prices_filename=args[2], fmt=args[3])


if __name__ == '__main__':
    import sys

    main(sys.argv)
