"""
a = int(input("Enter the number of participants on the biologists’ team: "))
b = int(input("Enter the number of participants on the computer scientists’ team: "))
if a % b == 0:
    print(a)
elif b % a == 0:
    print(b)
else:
    c = int()
    if a > b:
        c = a
    elif b >= a:
        c = b
    while c % a != 0 or c % b != 0:
        c += 1
    print(c)
"""


"""
n = int(input("Enter the number: "))
sum_of_f = 0
fact = 1
for i in range(1, n + 1):
    fact = fact * i
    sum_of_f += fact
print(sum_of_f)
"""


"""
n = int(input("Enter the number: "))
if n <= 9:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
else:
    print("Please enter a number less than or equal to 9")
"""


# В задании с потерянной карточкой я привел два решения
"""
n = int(input("Enter the number of cards: "))
desk = list(range(1, n + 1))
while len(desk) != 1:
    i = int(input("Enter numbers of the rest of the cards one by one: "))
    desk.remove(i)
print(desk[0])
"""
"""
n = int(input("Enter the number of cards: "))
sum_of_cards = 0
for i in range(1, n + 1):
    sum_of_cards += i
for j in range(1, n):
    rest = int(input("Enter the rest of the cards one by one: "))
    sum_of_cards -= rest
print(sum_of_cards)
"""


"""
n = int(input("Enter the number: "))
for i in range(1, n + 1):
    if i**2 <= n:
        print(i**2, end=" ")
    else:
        break
"""