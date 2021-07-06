# mortgage.py
#
# Exercise 1.8

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal * (1+rate/12) - (payment + extra_payment)
        total_paid = total_paid + payment + extra_payment
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

    if not principal > 0:
        total_paid = total_paid - abs(principal)
        principal = principal + abs(principal)

    print(f'{month:>5}  {total_paid:0.2f}  {principal:0.2f}')
    
    month = month + 1

print('Total paid', round(total_paid,1))
print('Months', month-1)
