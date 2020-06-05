# pcost.py
#
# Exercise 1.27
# total_cost = 0
# with open('/home/hp/practical-python/Work/Data/portfolio.csv', 'rt') as f:
#     headers = next(f)
#     for line in f:
#         row_list = line.split(',')
#         shares = int(row_list[1])
#         price = float(row_list[2])
#         total_cost += shares*price

# print(f'Total cost {round(total_cost, 2)}')

# Exercise 1.30, 1.31
def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'rt') as f:
        headers = next(f)
        for line in f:
            row_list = line.split(',')
            try:
                shares = int(row_list[1])
            except ValueError:
                print(f'Could not parse {line}')
                
            try:
                price = float(row_list[2])
            except ValueError:
                print(f"Could not parse {line}")
            
            total_cost += shares*price
    return print(f"Total cost: {round(total_cost,2)}")


portfolio_cost('/home/hp/practical-python/Work/Data/missing.csv')