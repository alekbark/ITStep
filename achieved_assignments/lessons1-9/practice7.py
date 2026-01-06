"""
number = lambda x: x + 15
print(number(10))
"""
"""
number = lambda x, y: x * y
print(number(12, 4))
"""
"""
lst = [78, 2, 13, 46, 5, 61, 74, 81, 94, 10]
even_lst = list(filter(lambda x: x % 2 == 0, lst))
print(even_lst)
odd_lst = list(filter(lambda x: x % 2 != 0, lst))
print(odd_lst)
"""
"""
import datetime
now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.time())
"""
"""
import random as rnd
multiplied = lambda x: x * rnd.randint(1, 10)
print(multiplied(48))
"""
"""
lst = [147, 241, 39, 5, 778, 18, 0, 10]
print(len(list(filter(lambda x: x % 2 == 0, lst))))
print(len(list(filter(lambda x: x % 2 != 0, lst))))
"""
# Модули и пакеты
# В первых четырех заданиях нужно раскомментить numpy
#import numpy as np
"""
my_array = np.random.randint(1, 500, (10, 10))
print(my_array.min(), my_array.max())
"""
"""
lst = np.random.randint(1, 500, 30)
print(lst.mean())
"""
"""
z_n_o = np.zeros((5, 5))
z_n_o[:, 0] = 1
z_n_o[:, -1] = 1
z_n_o[0, :] = 1
z_n_o[-1, :] = 1
print(z_n_o)
"""
"""
arr = np.zeros((5, 5))
arr[1, 0] = 1
arr[2, 1] = 2
arr[3, 2] = 3
arr[4, 3] = 4
print(arr)
"""
"""
import datetime as dt
start_date = dt.date(2022, 8, 1)
end_date = dt.date(2022, 8, 31)
while start_date <= end_date:
    print(start_date)
    start_date += dt.timedelta(days=1)
"""