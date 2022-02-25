sentence = input('enter your sentence:')
sentence = sentence.lower()
words = ['python','language']
sentence = sentence.split()
new_sen = ''
for x in sentence:
    if x not in words:
        new_sen += x
        new_sen += ' '
    else:
        new_sen += '_'
        new_sen += ' '

print(new_sen)