import math as m

a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + m.sqrt(delta)) / 2*a
    x2 = (-b - m.sqrt(delta)) / 2*a
    print("x1=",x1)
    print("x2=",x2)
elif delta == 0 :
    x = -b / 2*a
    print("x=",x)
else:
     print("root is not found")
     