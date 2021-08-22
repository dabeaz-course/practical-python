import math as m
def rectangular(r, theta):
	x = r*m.cos(theta)
	y = r*m.sin(theta)
	return x,y

print(rectangular(5, 60))

import sys
#print(sys.modules.keys())

print(sys.path)
