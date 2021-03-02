# report.py
#
# Exercise 2.4

from fileparse import parse_csv


def read_portfolio(filename):

    with open(filename) as f:
        file_content = parse_csv(f, types=[str, int, float])
    return file_content


def read_prices(filename):

    with open(filename) as f:
        file_content = parse_csv(f, has_headers=False, types=[str, float])
    return dict(file_content)


def make_report(portfolio, prices):
    report = []

    for stock in portfolio:
        holding = (stock["name"], stock["shares"], stock["price"], prices[stock["name"]] - stock["price"])
        report.append(holding)

    return report


def print_report(report, headers):
    sep = "----------"
    print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
    print(f"{sep:>10s} {sep:>10s} {sep:>10s} {sep:>10s}")
    for name, shares, price, change in report:
        print(f"{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}")


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    total_cost = 0
    total_actual_value = 0
    for stock in portfolio:
        total_cost += stock["shares"] * stock["price"]
        total_actual_value += stock["shares"] * prices[stock["name"]]

    report = make_report(portfolio, prices)
    headers = ('Name', 'Shares', 'Price', 'Change')
    print_report(report, headers)


def main(argv):
    if len(argv) != 3:
        print("Using default data source: `Data/portfolio.csv` and `Data/prices.csv`")
        portfolio_report("Data/portfolio.csv", "Data/prices.csv")
    else:
        portfolio_report(argv[1], argv[2])

if __name__ == "__main__":
    import sys
    main(sys.argv)
