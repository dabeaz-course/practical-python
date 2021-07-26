with open('Data/portfolio.csv') as f:
    next(f)
    total_cost = 0.0
    for line in f:
        name, shares, price = line.strip().split(',')
        shares = int(shares)
        price = float(price)
        total_cost += shares * price

print(f'Total cost {total_cost}')
