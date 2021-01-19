# pcost.py
#
# Exercise 1.27
# from pathlib import Path
import csv
import sys

# def extract_sinfo(line, idx):
#     try:
#         if idx == 1:
#             info = int(line.strip().split(',')[idx])
#         else:
#             info = float(line.strip().split(',')[idx])

#     except ValueError:
#         info = 0

#     return info

# def shares_x_price(line):
#     ticker, shares, price = line.strip().split(',')

#     try:
#         shares = int(shares)
#     except ValueError:
#         print(f'could not convert {ticker} shares to int: {shares}')
#         shares = 0

#     try:
#         price = float(price)
#     except ValueError:
#         print(f"could not convert {ticker} price to float: {price}")
#         price = 0

#     return shares * price


# def read_file(filepath):
#     with open(filepath, 'rt') as f:
        # hname, hshare, hprice = next(f).split(',')
        # print(f'{hname:^7}| {hshare:^7}| {hprice:^7}')

        # for line in f:
        #     ticker, shares, price = line.strip().split(',')
        #     print(f'{ticker:<7}| {shares:<7}| ${price:<7}')

        # return sum(shares_x_price(line)
        #            for line in f
        #            if line.startswith('"'))

        # return sum(extract_sinfo(l, 1) * extract_sinfo(l, 2)
        #            for l in f
        #            if l.startswith('"'))

        # return sum(int(l.strip().split(',')[1] or 0) * float(l.strip().split(',')[2] or 0)
        #                for l in f
        #                if l.startswith('"'))


# def shares_x_price(line):
#     _, shares, price = line.strip().split(',')
#     shares = int(shares) if shares.isdigit() else 0
#     price = float(price) if price.replace('.', '').isdigit() else 0
#     return shares * price



def portfolio_cost(filepath):
    with open(filepath, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        totals = []

        for idx, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))

            try:
                shares = int(record['shares'])
                price = float(record['price'])
                totals.append(shares * price)

            except ValueError:
                print(f'Row {idx}: Couldn\'t convert: {row}')

        return sum(totals)


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work/Data/portfoliodate.csv'

if __name__ == '__main__':
    portfolio_cost = portfolio_cost(filename)
    print(f'Total cost: ${portfolio_cost:.2f}')
