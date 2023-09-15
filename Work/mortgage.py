# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
month = 0

while principal > 0:
    if (month >= extra_payment_start_month and month <= extra_payment_end_month):
        correct_payment = extra_payment + payment
    else:
        correct_payment = payment

    principal = principal * (1 + rate / 12) - correct_payment
    total_paid = total_paid + payment
    month += 1

    print(month, " ", round(total_paid,2), " ", principal)

print('Total paid', round(total_paid,2))

# while principal > 0:
#     principal = principal * (1 + rate / 12) - payment
#     total_paid = total_paid + payment
#     month += 1
#
#     if (month >= extra_payment_start_month and month <= extra_payment_end_month):
#         principal -= extra_payment
#         total_paid += extra_payment
#
#     print(month, " ", round(total_paid,2), " ", principal)
#
# print('Total paid', round(total_paid,2))