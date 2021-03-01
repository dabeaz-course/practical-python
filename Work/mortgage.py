# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

month = 0
while principal > 0:
    month += 1
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        current_payment = payment + extra_payment
    else:
        current_payment = payment

    if current_payment >= principal * (1+rate/12):
        current_payment = principal * (1+rate/12)

    principal = principal * (1+rate/12) - current_payment
    total_paid = total_paid + current_payment

    print(month, round(principal, 2), round(total_paid, 2))

print('Total paid', total_paid, "Total months", month)
