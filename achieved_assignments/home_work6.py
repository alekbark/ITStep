# Задание №1.
"""
n = int(input("Enter a number: "))
lst = input(f"Enter {n} numbers: ").split()
if len(lst) != n:
    print("Invalid input")
new_list = []
for i in range(n):
    new_list.append(int(lst[i]))

even = []
odd = []
for x in new_list:
    if x % 2 == 0:
        even.append(x)
    elif x % 2 != 0:
        odd.append(x)

for z in odd:
    print(z, end=" ")
print()
for b in even:
    print(b, end=" ")
print()

if len(odd) > len(even):
    print("Нет")
else:
    print("Да")
"""

# Задание №2
"""
matrix = []
for i in range(3):
    lst = input("Enter 3 numbers: ")
    row = [int(x) for x in lst.split()]
    if len(row) != 3:
        print("Invalid input")
        break
    else:
        matrix.append(row)
diag = 0
for j in range(3):
    diag += (matrix[j][j])
print(diag)
"""

# Функции. Задание №1
"""
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
a = int(input("Enter a number: "))
print(fibonacci(a))
"""

# Функции. Задание №2
"""
def exp_2(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 != 0:
        return False
    return exp_2(n // 2)
"""