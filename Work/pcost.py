# pcost.py
#
# Exercise 1.27
def portfolioCost(filename):
    totalCost = 0
    with open(filename, 'rt') as f:
        headers = next(f).split(',')
        try:
            for line in f:
                row = line.split(',')
                nshares = int(row[1])
                price = float(row[2])
                totalCost += nshares * price
        except ValueError:
            print('Missing or Bad value')
            next(f)
    return totalCost
# print(f'Total cost: {portfolioCost('Data/portfolio.csv'):.2f}')
