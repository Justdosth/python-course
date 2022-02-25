a=[]
n=int(input("n="))
m=int(input("m="))
s = 0
for i in range(n):
    newlist=[]
    for j in range(m):
        x=float(input("x="))
        newlist=newlist+[x]
        if i==j:
            s += x
    a=a+[newlist]

print('sum is=',s)