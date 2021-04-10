#s = ('GOOG', 100, 490.1)
#name = s[0]
#shares = s[1]
#price = s[2]
#name, shares, prices = s
#print('Cost', "$", shares * price)
#s = {
#	'name' : 'GOOG',
#	'shares': 100,
#	'price': 490.10,
#}
#print(s)
#print(s['name'], "has", s['shares'], "shares.")
#print("The price per share is", s['price'], "Dollars.")
#s['date'] = '4/10/2021'
#print(s['date'])
#del s['date']
#print(s['date']) date doesn't exist anymore, deleted
#d = ['name', 'shares', 'price', 'date', 'account']
#for k in d:
#	print('k =', k)
#d = ('AA', int(75), float(32.2), '04/10/2021', 'Anonynmous')
#for k in d:
#	print('k =', k)
#keys = d.keys()
#print(keys)
#d = ['name', 'shares', 'price', 'date', 'account']
#list(d)
#for k in d:
#	print('k =', k)

d = {
	'name' : 'AA',
	'shares' : int(75),
	'price' : float(32.20),
	'date' : '04/10/2021',
	'account' : 'Anonymous',
}
print(d)
print(list(d)) #prints keys/names assigned to values
for k in d:
	print('k =', k)
for k in d:
	print(k,  '=', d[k])
keys = d.keys()
print(keys)
del d['account']
print(d)
items = d.items()
print(items)
d = dict(items)
print(d)
