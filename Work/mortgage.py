# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
totalPaid = 0.0
# extraPayment = 1000.0
month = 0

extraPayment = input('how much did you want to pay extra? ')
extraPaymentStartMonth = input('what month to start extra payment? ')
extraPaymentEndMonth = input('what month to end extra payment? ')

while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    # if month <= 12:
    #     principal -= extraPayment
    #     totalPaid += extraPayment
    #     month += 1
    if month >= int(extraPaymentStartMonth) and month <= int(extraPaymentEndMonth):
        principal -= float(extraPayment)
        totalPaid += float(extraPayment)
    month += 1
    totalPaid = totalPaid + payment
    
    # over payment
    if principal < 0:
        # add principal back to total paid
        totalPaid = totalPaid + principal
        principal -= principal

    # print(month, round(totalPaid,2), round(principal,2))
    print(f'{month}, ${totalPaid:0.2f}, ${principal:0.2f}')
# print('Total paid: ', round(totalPaid,2))
print(f'Total paid: ${totalPaid:0.2f}')
print('Months: ', month)

