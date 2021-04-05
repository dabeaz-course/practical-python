def sumcount(n):
	'''
	Returns the sum of the first n integers
	'''
	total = 0
	while n > 0:
		total += n
		n -= 1
		return total
a = sumcount(100)
print(a)

import math
x = math.sqrt(100)
print(x)
import urllib.request
u = urllib.request.urlopen('http://www.python.org/')
data = u.read()
#print(data)
