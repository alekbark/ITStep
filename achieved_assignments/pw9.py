# 1

# list_a = [-2, -1, 0, 1, 2, 3, 4]
#
# list_b = [x ** 3 if x < 0 else x ** 2 for x in list_a if x % 2 == 0]
# print(list_b)

# 2

#
# list_a1 = ["ab", "bcd", "cdefg", "defgh", "efghijk", "fghijklmnop"]
#
# list_b1 = [len(i) for i in list_a1]
# print(list_b1)

# 3

# list_a2 = [-2, -1, 0, 1, 2, 3, 4]
#
# list_b2 = [x ** 2 for x in list_a2 if x % 2 == 0]
# print(list_b2)

# 4

# list_a3 = [-7, -5, -4, 0, 3, 6, 10, 13, 15, 23, 30]
#
# list_b3 = [0 if x < 0 else x for x in list_a3 if x < 0 or  (x > 0 and x % 5 == 0)]
# print(list_b3)

# 5

# string1 = str(input())
#
# list_str_vowels = [i for i in string1 if i.lower() in 'aeiou']
# print(list_str_vowels)

# Итераторы, контейнеры и перечисления. Задание №1, №2, №3

# def tag_i_decorator(func):
#     def wrapper():
#         result = func()
#         return f"<i>{result}</i>"
#     return wrapper
#
# def tag_strong_decorator(func):
#     def wrapper():
#         result = func()
#         return f"<strong>{result}</strong>"
#     return wrapper
#
# @tag_strong_decorator
# @tag_i_decorator
# def get_text():
#     return "some text"
#
# print(get_text())

# Задние №4

# def createdbyme(func):
#     def wrapper():
#         return func()
#     if func.__doc__ is None:
#         wrapper.__doc__ = "Ivan Petrov"
#     else:
#         wrapper.__doc__ = func.__doc__ + "\nIvan Petrov"
#
#     return wrapper
#
# @createdbyme
# def a():
#     return 1
#
# print(a.__doc__)

