import random

print("Welcome to password generator")

max = 10
char = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*0123456789')
number = input('Banyak password untuk dibuat : ')
number = int(number)
if number > max:
    print("Password terlalu Banyak")
    quit()

length = input('Panjang of password : ')
length = int(length)
if length > max:
    print("Password terlalu panjang")
    quit()

print('\nIni password mu')

for pwd in range(number):
        password = ''
        for c in range(length):
            password += random.choice(char) 
        print(password)