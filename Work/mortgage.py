# mortgage.py
#
# Exercise 1.7
mortgage = 500000       # dollars
loan_period = 30 * 12   # months
interest_rate = .05
monthly_payment = 2684.11
amt_paid = 0

while mortgage > 0:
    amt_paid += monthly_payment
    mortgage = mortgage * (1 + interest_rate / 12) - monthly_payment

print(f'left: ${mortgage:.2f}, paid: ${amt_paid:,.2f}')
