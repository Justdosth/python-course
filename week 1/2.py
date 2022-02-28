p1 = float(input('price in this year:'))
p2 = float(input('price in last year:'))

inflation = (p2 - p1) / p1
print ('inflation is=',inflation*100)

p3 = p2 + (p2 * inflation)
print('price for the next year=', p3)
