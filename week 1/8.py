n = int(input('length of the list='))
words = []

for i in range(n):
    n = input('word=')
    words.append(n)
print('longest word is=',max(words, key=len))

j = ''
for i in words:
    if len(i)>len(j):
        j = i
print('longest word is=', j)