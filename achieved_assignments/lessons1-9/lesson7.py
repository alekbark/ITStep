
"""
double = lambda x: x ** 2
print(double(5))
"""
"""
lst = [4, 56, 98, 52, 963, 741, 25, 8]
new_list = list(filter(lambda x: x % 2 == 0, lst))
print(new_list)
"""
"""
lst = [4, 56, 98, 52, 963, 741, 25, 8]
new_list = list(map(lambda x: x * 2, lst))
print(new_list)
"""
"""
lst = [4, 56, 98, 52, 963, 741, 25, 8]
new_list = list(map(lambda x: x % 2 == 0, lst))
print(new_list)
"""
"""
import functools
lst = [4, 56, 98, 52, 963, 741, 25, 8]
ld = functools.reduce(lambda x, y: x + y, lst)
print(ld)
"""
"""
tbl = [lambda x = x: x * 10 for x in range(1, 11)]
for t in tbl:
    print(t())
"""
"""
maxim = lambda a, b: a if a > b else b
print(maxim(3, 5))
"""
"""
import math
print(dir(math))
print(help(math.sin))
"""
"""
import collections
c = collections.Counter()
for word in ["spam", "eggs", "ham", "spam"]:
    c[word] += 1
print(c)
# не успел ниче понять
"""