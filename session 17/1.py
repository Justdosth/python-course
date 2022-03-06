file1 = open('session 17/a.txt','w+')

numbers = ['10','11','12','13','14','15','16','17','18','19','20']

file1.writelines(numbers)
file1.close()

file2 = open('session 17/a.txt','r')
n = len(numbers)
s = 0
for x in range(n):
    number = float(file2.read(2))
    s += number
mean = s / n
print('mean=',mean)
file2.close()
