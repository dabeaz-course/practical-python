# pcost.py
#
# Exercise 1.27 + 1.30 + 1.31
def portfolio_cost(filename):
    counterOfLines = 0
    try:
        with open(filename, 'rt') as f:
            name, shares, price = next(f).split(',')
            counterOfLines += 1
            Total_cost = 0.00
            for lines in f:
                try:
                    name, shares, price = lines.split(',')
                    Total_cost += int(shares) * float(price)
                    counterOfLines += 1
                    print('Промежуточный итог:', Total_cost)
                except ValueError:
                    print('Проблема со строкой', counterOfLines, ': не хватает информации')
                    pass    
        return Total_cost
    except FileNotFoundError:
        print('Ну ты чего, братишка? Такого файла нет!')
cost = portfolio_cost('Data/portfolioTest.csv')
print('Total cost:', cost)