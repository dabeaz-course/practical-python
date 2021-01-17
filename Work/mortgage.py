# mortgage.py
#
# Exercise 1.7
mortgage = 500000       # dollars
loan_period = 30 * 12   # months
interest_rate = .05
monthly_payment = 2684.11
amt_paid = 0
pmt_cnt = 0


extra_payment = int(input('Enter extra payment amount: '))
extra_payment_start_month = int(input('Enter extra payment start month: '))
extra_payment_end_month = int(input('Enter extra payment end month: '))

# extra_payment_start_month = 61
# extra_payment_end_month = 108
# extra_payment = 1000

while mortgage > 0:
    if extra_payment_start_month <= pmt_cnt <= extra_payment_end_month:
        amt_paid += extra_payment + monthly_payment
        mortgage = mortgage * (1 + interest_rate / 12) - (monthly_payment + extra_payment)
    else:
        amt_paid += monthly_payment
        mortgage = mortgage * (1 + interest_rate / 12) - monthly_payment
    pmt_cnt += 1

print(f'left: ${mortgage:.2f}, paid: ${amt_paid:,.2f}, num_payments: {pmt_cnt}')
