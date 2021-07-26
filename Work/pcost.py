def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename) as f:
        next(f)
        for line in f:
            name, shares, price = line.strip().split(',')
            try:
                shares = int(shares)
                price = float(price)
            except ValueError:
                print(f'Error occurred while parsing line: {line!r}')
                continue
            total_cost += shares * price
    return total_cost


cost = portfolio_cost('Data/missing.csv')
print(f'Total cost: {cost}')
