# mortgage.py
#
# Exercise 1.7
mortgage = 500000       # dollars
loan_period = 30 * 12   # months
interest_rate = .05
monthly_payment = 2684.11
amt_paid = 0
pmt_cnt = 0

while mortgage > 0:
    if pmt_cnt < 12:
        amt_paid += 1000 + monthly_payment
        mortgage = mortgage * (1 + interest_rate / 12) - (monthly_payment + 1000)
    else:
        amt_paid += monthly_payment
        mortgage = mortgage * (1 + interest_rate / 12) - monthly_payment
    pmt_cnt += 1

print(f'left: ${mortgage:.2f}, paid: ${amt_paid:,.2f}, num_payments: {pmt_cnt}')
