principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month_number = 1

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month_payment = payment
    if extra_payment_start_month <= month_number <= extra_payment_end_month:
        month_payment += extra_payment
    principal = principal * (1 + rate / 12) - month_payment
    total_paid = total_paid + month_payment
    print(month_number, round(total_paid, 2))
    month_number += 1

print('Total paid', round(total_paid, 2))
