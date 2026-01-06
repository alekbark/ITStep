# Домашнее задание №09: Итераторы, контейнеры и перечисления

# 1

# list_a = [1, 2, 3, 4, 5, 6, 7]
#
# dict_b = {x: x**3 for x in list_a if x % 2 != 0}
# print(dict_b)


# 2

# list_a = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
#
# set_b = {x for x in list_a if x % 2 == 0}
# print(set_b)

# 3

# list_a = [x for x in range(0, 100, 10)]
# print(list_a)

# 4

# def gen_seven(n):
#     for i in range(0, n + 1):
#         if i % 7 == 0:
#             yield i
#
# for j in gen_seven(50):
#     print(j)

# Итераторы, контейнеры и перечисления

# from itertools import permutations
#
# data = input()
# letters_only = ''.join(c for c in data if c.isalpha())
# words = set()
#
# for length in range(1,len(letters_only)+1):
#     for p in permutations(letters_only, length):
#         words.add("".join(p))
#
# sorted_words = sorted(words, key=len)
# print(len(words))
# for word in sorted_words:
#     print(word)