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
        print(month, paid, principal)
    
    print('Total paid', round(paid, 2))
    print('Months', month)
    return round(paid, 2)

print('1.7', mortgage())
print('1.8', mortgage(1, 12, 1000))
print('1.9', mortgage(61, 108, 1000))