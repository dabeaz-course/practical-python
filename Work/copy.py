import csv
types = [str, float, str, str, float, float, float, float, int]

f = open('Data/dowstocks.csv')
rows = csv.reader(f)
header = next(rows)
row = next(rows)

print(type(row[0]))
print(type(row[1]))
print(type(row[2]))
print(type(row[3]))
print(type(row[4]))
print(type(row[5]))
print(type(row[6]))
print(type(row[7]))
print(type(row[8]))

converted = []
for func, val in zip(types, row):
	converted.append(func(val))
print(converted)
print(dict(zip(header, converted)))

f.close()
