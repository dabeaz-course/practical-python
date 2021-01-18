# pcost.py
#
# Exercise 1.27
from pathlib import Path

path = Path() / 'Work' / 'Data' / 'portfolio.csv'

with open(path, 'rt') as f:
    hname, hshare, hprice = next(f).split(',')
    print(f'{hname:^7}| {hshare:^7}| {hprice:^7}')

    # for line in f:
    #     ticker, shares, price = line.strip().split(',')
    #     print(f'{ticker:<7}| {shares:<7}| ${price:<7}')

    total_cost = sum(int(line.strip().split(',')[1]) * float(line.strip().split(',')[2])
                         for line in f)
    print(f'Total cost: ${total_cost:.2f}')
