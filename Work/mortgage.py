# mortgage.py
#
# Exercise 1.7

from distutils.command.build_scripts import first_line_re


principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
nb_months = 0
#------------ Extra payment ----------
extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment_lenght = extra_payment_end_month - extra_payment_start_month
#-------------------------------------

if extra_payment_start_month == 0 :
    while principal > 0 and extra_payment_lenght > 0 :

        principal = principal * (1+rate/12) - (payment + extra_payment)
        total_paid = total_paid + payment
        nb_months += 1
        extra_payment_lenght -= 1
        print(nb_months, total_paid, principal)

else :
    while principal > 0 and extra_payment_start_month != nb_months :
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        nb_months += 1
        print(nb_months, total_paid, principal)

if principal > 0 and extra_payment_start_month == nb_months :
    while principal > 0 and extra_payment_lenght > 0 :

        principal = principal * (1+rate/12) - (payment + extra_payment)
        total_paid = total_paid + payment
        nb_months += 1
        extra_payment_lenght -= 1
        print(nb_months, total_paid, principal)

if principal > 0 :
    while principal > 0 :
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        nb_months += 1
        print(nb_months, total_paid, principal)


print('Total paid :', total_paid)
print('Months :', nb_months)
