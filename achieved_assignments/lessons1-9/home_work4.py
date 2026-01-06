"""
a = int(input('Enter a number: '))
b = int(input('Enter another number: '))
c = int(input('Enter another number: '))
if a+b > c and b+c > a and c+a > b:
    print("true")
else:
    print("false")
"""

"""
a = int(input('Enter a number: '))
if a % 2 == 0:
    print("true")
else:
    print("false")
"""

"""
a = int(input('Enter a number: '))
b = int(input('Enter another number: '))
c = int(input('Enter another number: '))
if a+b > c:
    print("true")
else:
    print("false")
"""

"""
a = int(input('Enter a number: '))
b = int(input('Enter another number: '))
if a>b:
    print("true")
else:
    print("false")
"""

"""
login = input('Enter a username: ')
password = input('Enter a password: ')
if login == "user" and password == "qwerty":
    print("Authentication completed")
else:
    print("Invalid login or password")
"""

"""
kzt = int(input('Insert amount in KZT: '))
curr = int(input('Choose currency:'
                 '[1] USD '
                 '[2] EUR '
                 '[3] RUB '))
if curr == 1:
    print(f'{round(kzt / 420, 2)} USD')
elif curr == 2:
    print(f'{round(kzt / 510, 2)} EUR')
elif curr == 3:
    print(f'{round(kzt / 5.8, 2)} RUB')
"""

"""
s = int(input('Enter a cost of subscription: '))
p = int(input('Enter a cost of pizza: '))
m = int(input('Enter a Petya\'s salary: '))
if m >= s+p:
    print("Да")
else:
    print("Нет")
"""

"""
ticket = input('Enter a ticket: ')
t1 = int(ticket[0])
t2 = int(ticket[1])
t3 = int(ticket[2])
t4 = int(ticket[3])
t5 = int(ticket[4])
t6 = int(ticket[5])

if t1+t2+t3 == t4+t5+t6:
    print("Счастливый")
else:
    print("Обычный")
"""


