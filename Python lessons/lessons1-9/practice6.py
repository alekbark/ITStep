"""
# Задание № 1.
a, b = input("Enter two numbers in one line: ").split()
a = int(a)
b = int(b)

def calc(a, b):
    return a + b, a - b
result = calc(a, b)
print(f"The sum of numbers is {result[0]}, the difference of numbers is {result[1]}.")
"""

"""
# Задание №2.
def even_num():
    num_list = []
    for i in range(4, 30):
        if i % 2 == 0:
            num_list.append(i)
    return num_list
print(even_num())
"""

"""
import math
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
print(distance(x1, y1, x2, y2))
"""

"""
# Задание №3.
a = int(input("Enter a number: "))
n = int(input("Enter a power of the number: "))
def power(a, n):
        pow_a = a
        for i in range(n-1):
            pow_a *= a
        return pow_a
print(power(a, n))
"""

"""
# Задание №4
balances = {"USD": 1000, "EUR": 1000, "KZT": 500000}

def withdraw(balance, amount_w):
    if balance >= amount_w:
        return balance - amount_w
    else:
        print("Not enough money")
        return balance

def deposit(balance, amount_d):
    return balance + amount_d

def show_balance():
    answer = input("Do you want to check your balance? (Yes/No): ")
    if answer == "Yes":
        while True:
            valuta_show = input("Please choose the valuta (USD, EUR, KZT): ")
            if valuta_show in balances:
                print(f"Your balance is {balances[valuta_show]} {valuta_show}")
                break
            else:
                print("Invalid valuta, try again")

operation = input("Do you want withdraw or deposit money?: ")

while True:
    valuta = input("Please choose the valuta (USD, EUR, KZT): ")

    if valuta in balances:
        if operation == "withdraw":
            amount = int(input("Enter an amount: "))
            balances[valuta] = withdraw(balances[valuta], amount)
            show_balance()
            break

        elif operation == "deposit":
            amount = int(input("Enter an amount: "))
            balances[valuta] = deposit(balances[valuta], amount)
            show_balance()
            break

        else:
            print("Invalid operation, try again")
            break

    else:
        print("Invalid valuta, try again")
"""

"""
# Функции. Задание №1.
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)
values = input("Enter numbers: ").split()
a = int(values[0])
n = int(values[1])
print(f"{a} to the {n} power is {power(a, n)}")
"""

"""
# Функции. Задание №2.
def sum_scope(a, b):
    if a == b:
        return a
    else:
        return b + sum_scope(a, b - 1)
values = input("Enter numbers: ").split()
a = int(values[0])
b = int(values[1])
print(f"Sum from {a} to {b} is {sum_scope(a, b)}")
"""

"""
# Функции. Задание №3.
def stars(n):
    if n == 0:
        return
    print("*", end=" ")
    stars(n - 1)
stars(int(input("Enter amount of stars: ")))
"""

"""
# Функции. Задание №4.
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)
a = int(input())
n = int(input())
print(f"{power(a, n)}")
"""