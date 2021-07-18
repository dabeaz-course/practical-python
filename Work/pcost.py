# pcost.py
#
# Exercise 1.27

with open('Data/portfolio.csv','rt') as file:
    header = next(file)
    data = []
    cost = 0
    for line in file:
        data = line.split(',')
        shares = int(data[1])
        cost += shares * float(data[2])
    
    print(f"Total cost {cost}")


import gzip                                         
with gzip.open('Data/portfolio.csv.gz', 'rt') as f: 
     for line in f:
             print(line, end='')        
