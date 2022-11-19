# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
numberOfMonths = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    numberOfMonths += 1
    principal = principal * (1 + rate/12) - (payment + extra_payment * int(extra_payment_start_month <= numberOfMonths <= extra_payment_end_month))
    total_paid = total_paid + payment + (extra_payment * int(extra_payment_start_month <= numberOfMonths <= extra_payment_end_month))
    if (principal < 0):
        total_paid = total_paid - principal
        principal = 0
    print(numberOfMonths, round(total_paid, 2), round(principal, 2))

print('Total paid', round(total_paid, 2))
print('Number of months', numberOfMonths)