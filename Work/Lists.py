symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
symslist = symbols.split(',')
print(symslist)
print(symslist[0])
print(symslist[1])
print(symslist[-1])
print(symslist[-2])
symslist[2] = 'AIG'
print(symslist)
print(symslist[0:3])
print(symslist[-4:-1])
mysyms = []
mysyms.append('LOL')
print(mysyms)
symslist[-2:] = mysyms
print(symslist)
for s in symslist:
	if s == "AIG":
		print('AIG is in the list')
for s in symslist:
	if s == "AA":
		print('AA is in the list')
if 'CAT' not in symslist:
	print('CAT is not in the list')
symslist.append('RHT')
symslist.insert(1, 'AA')
symslist.remove('MSFT')

