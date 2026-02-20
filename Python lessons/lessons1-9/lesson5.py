"""
a = 1
while a < 10:
    print(a)
    a += 1
"""
"""
a = 1
while a==1:
    b = input("What's your name? ")
    print(b, ", you're welcome!")
"""
"""
a = 1
while a < 5:
    a += 1
    print("условие верно")
else:
    print("условие не верно")
"""
"""
a = 1
while a < 5:
    a += 1
    if a == 3:
        break
    print(a)
print(a)
"""
"""
a = 1
while a < 5:
    a += 1
    if a == 3:
        continue
    print(a)
"""
"""
for i in "hello world":
    print(i*2, end="")
"""
"""
languages = ["C", "C++", "Perl", "Python", "Go", "Java", "JavaScript"]
for language in languages:
    print(language)
"""
"""
for i in range(4):
    print(i)
    print(i**2)
"""
""" # вот тут не догнал сразу
sum = 0
n = 5
for i in range(1, n + 1):
    sum += i
print(sum)
"""
"""
fibonacci = [0,1,1,2,3,5,8,13,21]

for i in range(len(fibonacci)):
    print(i,fibonacci[i])
"""
"""
edibles = ["отбивные", "пельмени", "яйца", "орехи"]

for food in edibles:
    if food == "пельмени":
        print("Я не ем пельмени")
        break
    print("Отлично, вкусные " + food)
else:
    print("Хорошо, что не было пельменей")
print("Ужин окончен")
"""
"""
edibles = ["отбивные", "пельмени", "яйца", "орехи"]

for food in edibles:
    if food == "пельмени":
        print("Я не ем пельмени")
        continue
    print("Отлично, вкусные " + food)
else:
    print("Хорошо, что не было пельменей")
print("Ужин окончен")
"""
"""
my_list = ['яблоко','банан', 'вишня', 'персик']

for c, value in enumerate(my_list, 1):
    print(c, value)
"""
"""
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="\t")
    print()
"""
"""
n = int(input())
m = int(input())
for i in range(n):
    for j in range(m):
        print("*", end="")
    print()
"""


