# pcost.py
#
# Exercise 1.27

with open('Work/Data/portfolio.csv','rt') as f :
    headers = next(f)
    for line in f:
        row = line.split(',')
        nshares = int(row[1])
        price = float(row[2])
        total_cost += nshares * price

print('Total cost', total_cost)
