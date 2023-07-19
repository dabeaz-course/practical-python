# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
extra = 1000
total_paid = 0.0
month = 1
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    month += 1
    while extra_payment_start_month <= month <= extra_payment_end_month:
        principal = principal * (1 + rate / 12) - (payment + extra)
        total_paid = total_paid + (payment + extra)
        month += 1

print('Total paid', total_paid)

# The answer to Ex 1.9 is: Total paid 880074.0999999964