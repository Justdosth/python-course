def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

def fibonacci(n): return 1 if not n or not n - 1 else fibonacci(n - 1) + fibonacci(n - 2)

n = int(input('n='))
# print(fib(n))

y1 = 0
y2 = 1

if n==y1:
    print(y1)
elif n==y2:
    print(y1)
    print(y2)
else:
    print(y1)
    print(y2)
    i = 3
    while i<=n:
        y = y1+y2
        print(y)
        y1 = y2
        y2 = y
        i += 1

def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    elif n==0:
        print(0)
    elif n==1:
        print(1)
    else:
        m=(Fibonacci(n-1)+Fibonacci(n-2) )
        print(m)

Fibonacci(n)