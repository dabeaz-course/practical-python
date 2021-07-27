from report import read_portfolio


def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    return sum(h['shares'] * h['price'] for h in portfolio)


if __name__ == '__main__':
    import sys


    def main():
        portfolio_filename = sys.argv[1] if len(sys.argv) == 2 else 'Data/portfolio.csv'
        cost = portfolio_cost(portfolio_filename)
        print(f'Total cost: {cost}')


    main()
