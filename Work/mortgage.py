# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment_start_month = int(input('Enter the first extra payment month number: '))
extra_payment_end_month = int(input('Enter the last extra payment month number: '))
extra_payment = float(input('Enter the amount of the extra payment: '))


while principal > 0:
    months += 1
    principal = principal * (1+rate/12) - payment
    total_paid += payment

    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    if principal <= payment: # 1.11 Bonus
        print(f"{months} {round(total_paid, 2)} {round(principal, 2)}")
        payment = principal
        total_paid = total_paid + payment
        principal = principal - payment

    print(f"{months} {round(total_paid, 2)} {round(principal, 2)}")

print('Total paid', round(total_paid, 1))
print('Months', months)