X = ('reza','mahsa',12,3,4,9,'neda')
Y = (125,12,1,0,'sasan','reza')
X = set(X)
Y = set(Y)
uni = X.intersection(Y)
dif = X.union(Y) - uni
uni = tuple(uni)
dif = tuple(dif)
print('union= ',uni)
print('differnce=',dif)