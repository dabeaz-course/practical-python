# mortgage.py
#
# Exercise 1.7

principal = 500000
rate = 0.05
payment = 2684.11
total_paid = 0
months = 0

extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000



while principal > 0:
    if  extra_payment_start_month < months <= extra_payment_end_month:
        payment = 2684.11 + extra_payment
    else:
        payment = 2684.11
    if principal > payment:
        principal = principal * (1 + rate/12) - payment
        total_paid = total_paid + payment
    else:
        principal = 0
        total_paid += principal
    months += 1
    print(months, total_paid, principal)
