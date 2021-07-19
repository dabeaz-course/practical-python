# pcost.py
#
# Exercise 1.27

# Exercise 1.27


def portfolio_cost(filename):
    with open(filename,'rt') as file:
        header = next(file)
        data = []
        cost = 0
        for line in file:
            data = line.split(',')
            try:
                shares = int(data[1])
                cost += shares * float(data[2])
            except ValueError:
                print(f'This is an improper line: {data}')
        return cost