import csv


def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row_number, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                shares = int(record['shares'])
                price = float(record['price'])
            except ValueError:
                print(f'Row {row_number}: Could\'t convert: {row!r}')
                continue
            total_cost += shares * price
    return total_cost


if __name__ == '__main__':
    import sys


    def main():
        if len(sys.argv) == 2:
            filename = sys.argv[1]
        else:
            filename = 'Data/portfolio.csv'

        cost = portfolio_cost(filename)
        print(f'Total cost: {cost}')


    main()
