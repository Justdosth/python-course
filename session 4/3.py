import math as m

def d(x1,x2,y1,y2):
    distance = m.sqrt((x1-x2)**2 + (y1-y2)**2)
    print('The distance is',distance)

x1 = float(input('x1='))
x2 = float(input('x2='))
y1 = float(input('y1='))
y2 = float(input('y2='))
d(x1,x2,y1,y2)