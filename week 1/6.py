name = input('string=')
new_name = ''
print(name)
for i, n in enumerate(name):
    if i%2!=0:
        new_name = new_name+n+' '
    else:
        new_name = new_name+n
print(new_name)