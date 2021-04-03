symbols = 'AAPL, IBM, MSFT, YHOO, SCO'
a = symbols[0]
b = symbols[1]
c = symbols[2]
d = symbols[-1]
e = symbols[-2]
print(a.lower())
symbols = symbols + ', GOOG'
print(symbols)
symbols = 'HPQ, ' + symbols
print(len(symbols)) #HPQ, AAPL, IBM, MSFT, YHOO, SCO, GOOG
print(symbols[11:14]) #IBM
print(symbols[5:7]) #AA
print(symbols[-8],symbols[6],symbols[-18]) #CAT
print(symbols.lower())
print(symbols)
lowersyms = symbols.lower()
symbols.find('MSFT')
print(symbols[13:17])
symbols = symbols.replace('SCO', 'DOA')
print(symbols)
