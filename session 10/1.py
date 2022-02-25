x = ('sasan','reza','neda','omid','reza','ali','Zahra','mahan','ashkan','reza')
x_list = list(x)

for i in x_list:
    if i=='reza':
        x_list.remove('reza')

x_tuple = tuple(x_list)
print('x=',x_tuple)