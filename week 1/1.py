x = float(input('x='))

insurance = x*7 / 100
print('insurance=', insurance)

tax = x*10 / 100
print('tax=', tax)

salary = x - (insurance+tax)
print('salary=', salary)
