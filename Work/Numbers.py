Mortgage = 500000
Month = 0
Interest = float(0.05/12)
monthlypayment = 2684.11
total_payed = 0

while int(Month) < 12: #int(Mortgage) > 0
	Month = Month + 1
	Mortgage = (float(Mortgage) -  float(monthlypayment)) - 1000
	Mortgage = float(Mortgage)  + (float(Mortgage) * Interest)
	total_payed = total_payed + monthlypayment + 1000

while float(Mortgage) > 0: #int(Mortgage) > 0
	Month = Month + 1
	Mortgage = (float(Mortgage) -  float(monthlypayment))
	Mortgage = float(Mortgage)  + (float(Mortgage) * Interest)
	total_payed = total_payed + monthlypayment

print(float(Month), "Months that passed.")
print(float(total_payed), "Total amount of money payed.")
