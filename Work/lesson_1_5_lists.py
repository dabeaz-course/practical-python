# Exercise 1.19
symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
symlist = symbols.split(',')

# Create an empty list and append an item to it:

mysyms = []
mysyms.append('GOOG')


# Exercise 1.20
# Looping over list items

for s in symlist:
	print('s = ', s)

# Exercise 1.22
# Use the append() method to add the symbol 'RHT' to end of symlist.

symlist.append('RHT')


# Use the insert() method to insert the symbol 'AA' as the second item in the list.
symlist.insert('AA',1)

# Use the remove() method to remove 'MSFT' from the list.
symlist.remove('MSFT')

# Append a duplicate entry for 'YHOO' at the end of the list.
symlist.append('YHOO')

# Use the index() method to find the first position of 'YHOO' in the list.

symlist.index('YHOO')