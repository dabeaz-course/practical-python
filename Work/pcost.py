# pcost.py
#
# Exercise 1.27
with open('Data/portfolio.csv', 'rt') as f:
	for line in f:
		print(line, end='')
f = open('Data/portfolio.csv', 'rt')
f = str(f)
print(f)
List = []
for line in f:
	stripped_line = line.strip
	line_list = stripped_line.split()
	List.append(line_list)
print(List)

#line = str(line)
#line.remove('AA')
#line.remove('IBM')
#line.remove('CAT')
#line.remove('MSFT')
#line.remove('GE')
#line.remove('MSFT')
#line.remove('IBM')
