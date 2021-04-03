
Mortgage = 500000
Month = 0
Interest = float(0.05/12)
monthlypayment = 2684.11
total_payed = 0
while int(Month) < 360: #int(Mortgage) > 0
	Month = Month + 1
	Mortgage = (float(Mortgage) -  float(monthlypayment))
	Mortgage = float(Mortgage)  + (float(Mortgage) * Interest)
	print(float(Mortgage), int(Month))
	total_payed = total_payed + monthlypayment

print(float(Month), "Months that passed.")
print(float(total_payed), "Total amount of money payed.")
