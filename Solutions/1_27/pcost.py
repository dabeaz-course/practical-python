# pcost.py

total_cost = 0                                                                 
f = open("../../Work/Data/portfolio.csv", 'rt')                                # reading file line by line
all_data = f.readlines()                                                       # reading all of the lines
for data in all_data:                                                          
    data = data.split(",")                                                     # splitting csv fomat
    total_cost = int(data[1]) * float(data[2])                                 # doing the arithmetic (you don't neet it to be int use float instead!!)
print(f"Total_cos: {t}")                                                         
