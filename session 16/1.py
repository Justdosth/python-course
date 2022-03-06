import re

name = input('name: ')
national_number = input('national number: ')
phone = input('phone: ')
password = input('password: ')

check_words = [name,national_number,phone]

#first solution
if any(x in password for x in check_words):
    print("This password cat't be used")
else:
    print('Password is set')

#second solution
cheking_0 = re.search(name, password)
cheking_1 = re.search(national_number, password)
cheking_2 = re.search(phone, password)
if cheking_0 or cheking_1 or cheking_2:
    print("This password cat't be used")
else:
    print('Password is set')