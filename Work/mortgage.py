# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    principal = principal * (1 + rate/12) - payment
    total_paid += payment
    months += 1

    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment
print(f"Month: {months:17}\nTotalPaid: {total_paid:19.2f}\nPrincipalRemaining: {principal:6.2f}")

print(f"Total paid: {total_paid:18.2f}")
print(f"It took {months} months to payoff loan")
