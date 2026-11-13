pay_rate     = eval(input("How much do you get paid hourly? $"))
hours_worked = eval(input("How much did you work this week? "))
gross_pay = round((pay_rate * hours_worked ), 2)

if hours_worked > 40:
    gross_pay = round(((pay_rate * 40) + ((pay_rate *1.5)*(hours_worked-40))), 2)

print(gross_pay)
