# pcost.py
#
# Exercise 1.27
# with open('Data/portfolio.csv', 'rt') as f:
#     for line in f:
#         print(line.split(','))
total_cost = 0

f = open('Data/portfolio.csv', 'rt')
headers = next(f).split(',')

for line in f:
    row = line.split(',')
    total_cost = total_cost + (int(row[1]) * float(row[2]))

print('Total cost', total_cost)
