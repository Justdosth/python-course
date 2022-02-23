hours = int(input('hours='))
payment = 100000

if hours > 160:
    aditional = hours - 160
    if aditional > 40:
        salary = 160*payment + 40*(payment/2)
    else:
        salary = 160*payment + aditional*(payment/2)
else:
    salary = hours*payment

print('salary=',salary)