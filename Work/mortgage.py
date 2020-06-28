# mortgage.py
#
# Exercise 1.7

# Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?
#
# Modify the program to incorporate this extra payment.
# Have it print the total amount paid along with the number of months required.
#
# When you run the new program, it should report a total payment of 929,965.62 over 342 months.

# How much will Dave pay if he pays an extra $1000/month for 4 years starting in year 5 of the mortgage?

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000
extra_payment_start_month = 60
extra_payment_end_month = 108

month = 0

while principal > 0:
    month = month + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    if (month >= extra_payment_start_month) & (month < extra_payment_end_month):
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    print( month, total_paid, principal)
total_paid = total_paid - abs(principal)

print('Total paid', total_paid)
print('Total months', month)