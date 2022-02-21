import math as m

n = int(input('n='))
s= 0

for i in range(n+1):
    s = s + i**2

print('s=',s)
ss = m.sqrt(s)
print('ss=',ss)