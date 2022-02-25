x = [1 , -5, 9, 23, 12, 1]

index = x.index(12)
x.insert(index,'reza')
print(x)

x.remove(9)
x.remove(23)
print(x)

x.pop(0)
x.insert(0,'ali')
print(x)