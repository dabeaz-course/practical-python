# mortgage.py
#
# Exercise 1.7

def mortgage(extra_payment_start_month=0,
             extra_payment_end_month=0,
             extra_payment=0.0):
    principal = 500000.0
    rate = 0.05
    default_payment = 2684.11
    paid = 0.0
    month = 0

    print(f'{"Mo":>3} {"Paid":>11} {"Principal":>11}')
    while principal > 0:
        month += 1
        payment = default_payment

        if month >= extra_payment_start_month and month <= extra_payment_end_month:
            payment += extra_payment
        
        if payment > principal:
            payment = principal
            principal = 0
        else:
            principal = principal * (1 + rate / 12) - payment
        
        paid = paid + payment
        print(f'{month:>3} {f"${paid:,.2f}":>11} {f"${principal:,.2f}":>11}')
    
    print('------------------')
    print(f'Total paid: ${round(paid, 2):,.2f}')
    print('Months:    ', month)
    print('------------------')
    return round(paid, 2)

mortgage(61, 108, 1000)