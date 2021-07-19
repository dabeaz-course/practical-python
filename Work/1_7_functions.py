# 1.7 Functions

def sumcount(n):
	'''
	Returns the sum of the first n integers.
	'''

	total = 0

	while n >0:
		total += n
		n -= 1
	return total


for line in f:
	fields = line.split()
	try:
		shares = int(fields[1])
	except ValueError:
		print("Couldn't parse", line)


