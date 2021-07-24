principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

print(f"""{'month'} {'total paid':>15} {'left':>15}""")
while principal > 0:
    month += 1
    month_payment = payment
    if extra_payment_start_month <= month <= extra_payment_end_month:
        month_payment += extra_payment
    principal = principal * (1 + rate / 12) - month_payment
    if principal < 0:
        month_payment -= abs(principal)
        principal = 0
    total_paid = total_paid + month_payment
    print(f'{month:5} {total_paid:>15,.2f} {principal:>15,.2f}')

print(f'\nTotal paid: {total_paid:,.2f}')
print(f'Months: {month}')
