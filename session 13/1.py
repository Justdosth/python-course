x = {'a0':10,'a1':40,'a2':20,'a3':100,'a4':50,'a5':70,'a6':90,'a7':250,'a8':500,'a9':340}
n = int(input('number of penalties: '))
s = 0
for i in range(n):
    penalty_name = input('code of penalty: ')
    s = s + x[penalty_name]
print('sum of penlaties is',s)