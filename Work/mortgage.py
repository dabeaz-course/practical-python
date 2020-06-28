# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
# Start pay extra at year 5
extra_payment_start_month = 12*5
# Pay extra for 4 years
extra_payment_end_month = extra_payment_start_month + 12*4
# Extra payment amount
extra_payment = 1000
# Month counter
current_month = 0
print('Month\tTotal Paid\tPrincipal')
while principal > 0:
    # Increase month counter
    current_month += 1
    # Calculate standard payment
    principal = principal * (1+rate/12) - payment
    total_paid += payment
    # Pay extra if needed
    if current_month >= extra_payment_start_month and \
       current_month <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment
    # If we've overpaid, return overpaid amount
    if principal < 0:
        principal = 0
        total_paid += principal        
    print(f'{current_month}\t{round(total_paid,2)}\t{round(principal,2)}')

print('\nTotal paid\t\t', round(total_paid, 2))
print('Months\t\t\t', current_month)
