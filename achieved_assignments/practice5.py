
"""
i = 0
while i < 21:
    print(2**i)
    i += 1
"""

"""
i = 0
while i < 5:
    print('*')
    if i % 2 == 0:
        print('**')
    if i > 2:
        print('***')
    i = i + 1

# The answer is 17
"""

"""
i = 0
while True:
    n = int(input("Enter a number: "))
    if n == 0:
        break
    i += n
print(i)
"""


"""
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))


for i in range(a, b + 1):
   print(i, end=" ")
print()


for i in range(a, b + 1):
    if i % 2 != 0:
        print(i, end=" ")
print()


for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, end=" ")
print()


for i in range(b, a - 1, -1):
    print(i, end=" ")
print()
"""

"""
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter another number: "))
d = int(input("Enter another number: "))

if a <= b <= 10 and c <= d <= 10:
    print("\t", end="")
    for n in range(c, d + 1):
        print(n, end="\t")
    print()
    for i in range(a, b + 1):
        print(i, end="\t")
        for j in range(c, d + 1):
            print(i * j, end="\t")
        print()
else:
    print("Incorrect input")
"""

"""
for i in range(5):
    for j in range(i):
        print("*", end="")
    print()
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
"""

"""
while True:
    n = int(input("Enter a number: "))
    if n < 10:
        continue
    elif n > 100:
        break
    print(n)
"""

"""
for n in range(1, 101):
    nums = []
    a = int()
    for i in range(1, n):
        if n % i == 0:
            nums.append(i)
    for j in nums:
        a += j
    if a == n:
        print(n)
    else:
        continue
"""

