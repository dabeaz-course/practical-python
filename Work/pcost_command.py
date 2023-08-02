# Excersize 1.33

from pcost import pcost
import sys

print(sys.argv)
print()

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = pcost(filename)
print(f'Total cost ${cost:,.2f}')