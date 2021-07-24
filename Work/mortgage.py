principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month_number = 1

while principal > 0:
    month_payment = payment
    if month_number <= 12:
        month_payment += 1000.0
    principal = principal * (1 + rate / 12) - month_payment
    total_paid = total_paid + month_payment
    print(month_number, round(total_paid, 2))
    month_number += 1

print('Total paid', round(total_paid, 2))
