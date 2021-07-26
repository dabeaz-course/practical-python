def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename) as f:
        next(f)
        for line in f:
            name, shares, price = line.strip().split(',')
            shares = int(shares)
            price = float(price)
            total_cost += shares * price
    return total_cost


cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost: {cost}')
