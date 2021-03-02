# report.py
#
# Exercise 2.4

from fileparse import parse_csv
import tableformat
from stock import Stock


def read_portfolio(filename):

    with open(filename) as f:
        portdicts = parse_csv(f, types=[str, int, float])
    # Generate a list of Stock instances
    portfolio = [Stock(d['name'], d['shares'], d['price']) for d in portdicts]

    return portfolio


def read_prices(filename):

    with open(filename) as f:
        file_content = parse_csv(f, has_headers=False, types=[str, float])
    return dict(file_content)


def make_report(portfolio, prices):
    report = []

    for stock in portfolio:
        holding = (stock.name, stock.shares, stock.price, prices[stock.name] - stock.price)
        report.append(holding)

    return report


def print_report(report, formatter):

    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)


def portfolio_report(portfolio_filename, prices_filename, fmt="txt"):
    """Print a report in a nicely formatted way.

    Parameters:
    fmt (str): Format type. Types of format available: txt (default), csv, html
    """

    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    total_cost = 0
    total_actual_value = 0
    for stock in portfolio:
        total_cost += stock.shares * stock.price
        total_actual_value += stock.shares * prices[stock.name]

    report = make_report(portfolio, prices)
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(argv):
    if len(argv) != 4:
        print("Using default data source: `Data/portfolio.csv` and `Data/prices.csv`")
        portfolio_report("Data/portfolio.csv", "Data/prices.csv", "txt")
    else:
        portfolio_report(argv[1], argv[2], argv[3])

if __name__ == "__main__":
    import sys
    main(sys.argv)
