# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
extra = 1000
total_paid = 0.0
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > payment:
    month += 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if extra_payment_start_month <= month <= extra_payment_end_month:
        principal = principal - extra
        total_paid = total_paid + extra

    print(month, total_paid, principal)

month += 1
total_paid = total_paid + principal
principal = 0

print(month, total_paid, principal)

print('The total paid is ' f'${total_paid:0.2f} over {month} months')

# The answer to Ex 1.9 is: Total paid 880074.0999999964