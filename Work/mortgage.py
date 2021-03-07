# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

paymentPlus = payment + 1000
for m in range(1,13):
    principal = principal * (1 + rate/12) - paymentPlus
    total_paid += paymentPlus
    months += 1
while principal > 0:
    principal = principal * (1 + rate/12) - payment
    total_paid += payment
    months += 1

print("Total paid: ", round(total_paid, 2))
print("It took " + str(months) + " months to payoff loan")
