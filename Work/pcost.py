# pcost.py
#
# Exercise 1.27
from pathlib import Path

def read_file(filepath):
    with open(filepath, 'rt') as f:
        # hname, hshare, hprice = next(f).split(',')
        # print(f'{hname:^7}| {hshare:^7}| {hprice:^7}')

        # for line in f:
        #     ticker, shares, price = line.strip().split(',')
        #     print(f'{ticker:<7}| {shares:<7}| ${price:<7}')

        total_cost = sum(int(l.strip().split(',')[1]) * float(l.strip().split(',')[2])
                         for l in f
                         if l.startswith('"'))
        print(f'Total cost: ${total_cost:.2f}')


portfolio = Path() / 'Work' / 'Data' / 'portfolio.csv'
read_file(portfolio)
