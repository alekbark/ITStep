# №1

# def InsertionSort(A):
#     for i in range(1, len(A)):
#         key = A[i]
#         j = i - 1
#         while j >= 0 and A[j] > key:
#             A[j + 1] = A[j]
#             j = j - 1
#         A[j + 1] = key
#     return A
#
# print(InsertionSort([10, -1, 3, 0, 5, -7]))


# №2

# def SelectionSort(A):
#     result = []
#     while A:
#         max_value = A[0]
#         max_index = 0
#         for i in range(len(A)):
#             if A[i] > max_value:
#                 max_value = A[i]
#                 max_index = i
#         result.append(A.pop(max_index))
#     return result
#
# print(SelectionSort([10, -1, 3, 0, 5, -7]))

# Сортировка №1

# def sum_with_sales(A):
#     A.sort(reverse=True)
#     total = 0
#     for i in range(len(A)):
#         if (i + 1) % 3 != 0:
#             total += A[i]
#     return total
#
# print(sum_with_sales([1, 5, 4, 3, 5, 7]))

# №2

# def closest_pair(A):
#     A.sort()
#     current1, current2 = A[0], A[1]
#     diff = A[1] - A[0]
#     for i in range(len(A) - 1):
#         if A[i + 1] - A[i] < diff:
#             diff = A[i + 1] - A[i]
#             current1, current2 = A[i], A[i + 1]
#     return current1, current2
#
# print(closest_pair([9, 4, 6, 1]))

# №1

# def aling_string(lines):
#     max_line = max(lines, key=len)
#     for i in lines:
#         print((len(max_line) - len(i)) * "*" + i)
#
#
# lines = []
# while True:
#     line = input("Enter a line: ")
#     if line == "":
#         break
#     else:
#         lines.append(line)
#
# aling_string(lines)

# №2

# def balance_array(A):
#     s_pos = 0
#     s_neg = 0
#     for w in A:
#         if w < 0:
#             s_neg += w
#         else:
#             s_pos += w
#
#     if s_pos != abs(s_neg):
#         A.append(-(s_neg + s_pos))
#     return s_pos, s_neg, A
#
#
#
# for j in balance_array([-3,-2,1,2,3,4]):
#     print(j)

# Регулярные выражения Задание №1.

import re
#
# emails = [
#     "test@gmail.com",
#     "admin@mail.ru",
#     "user123@my-site.org"
# ]
#
# domains = [re.findall(r"@([a-zA-Z0-9.-]+)", email)[0] for email in emails]
#
# print(domains)

# Задание №2

# text = "apple tree orange sky idea under sun"
#
# words = re.findall(r"[\b[aeiouAEIOU][a-zA-Z]*", text)
# print(words)

# Задание №3

# text = "one,two;;three|four,,five"
# parts = re.split(r'[,|;]+', text)
# print(parts)