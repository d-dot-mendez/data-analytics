pay_rate     = eval(input("How much do you get paid hourly? $"))
hours_worked = eval(input("How much did you work this week? "))
gross_pay    = round((pay_rate * hours_worked ), 2)
annual_pay   = (gross_pay * 52) 

if hours_worked > 40:
    gross_pay = round(((pay_rate * 40) + ((pay_rate *1.5)*(hours_worked-40))), 2)

if annual_pay <12000:
    print("5% tax rate")
if annual_pay >= 12000 and annual_pay <= 24999.99:
    print("10% tax rate")
if annual_pay >= 25000 and annual_pay <= 74999.99:
    print("15% tax rate")
if annual_pay >= 75000:
    print("20% tax rate")


