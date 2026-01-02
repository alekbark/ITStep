"""
nums = [3, 1, 4, 2]
print(sorted(nums))
print(nums)
nums.sort()
print(nums)
"""

"""
str = "h31110 23 cat 444.4 rabbit 11 2 dog"
print([float(s) for s in str.split() if s.replace(".", "", 1).isdigit()])
"""

"""
print("test"[::-1])
"""

"""
print(" Some text ".strip())
print(" Some text ".lstrip())
print(" Some text ".rstrip())
"""

"""
import copy

a = ["кот", "слон", "змея"]
e = copy.copy(a)
print(id(a), id(e), a, e)

f = copy.deepcopy(a)
print(id(a), id(f), a, f)
"""

"""
import copy

a = [1, 2, [3, 4]]
b = copy.deepcopy(a)  # глубокая копия (нужна редко, только для списков со вложенными списками)

b[2][0] = 99
print(a)  # [1, 2, [3, 4]] — оригинал не изменился
print(b)  # [1, 2, [99, 4]]
"""

"""
nums = [1, 2, 3, 4, 5]
rev = reversed(nums)
rev_slise = nums[::-1]
print(nums, list(rev), rev_slise)
"""

"""
words = ["one", "two", "three", "one", "three"]
print(set(words))
"""

"""
a = []
if not a:
    print("список пуст!")
    print(a)
"""

"""
n = (tuple(i for i in range(0, 10)))
print(n)
"""

"""
#namedtuple полезен, когда нужно хранить небольшие структурированные данные без создания полноценного класса
from collections import namedtuple
Flower = namedtuple("Flower", "color cost comment")
rose = Flower("red", 5, "beautiful")
print(rose.cost)
print(rose.color)
print(rose.comment)
"""

"""
a = (3, 1, 5, 2, 6, 7)
a = tuple(sorted(a))
print(a)
"""

"""
#Так можно сделать, когда у тебя есть последовательность пар (список или кортеж кортежей), 
#где каждая пара состоит из двух элементов: ключ и значение.
a = (('a', 2), ('b', 4))
a = dict(a)
print(a)
"""

"""
not_sure = {}
print(type(not_sure))
"""


