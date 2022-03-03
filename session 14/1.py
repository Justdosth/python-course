n = int(input('n='))
x = {}
y = {}
for i in range(n):
    name = input('name=')
    age = int(input('age='))
    x = {name:age}
    y.update(x)
print('our dictionary is',y)