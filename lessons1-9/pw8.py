# 1

# def IsAscending(A):
#     for i in range(1, len(A)):
#         if A[i] <= A[i-1]:
#             return "NO"
#     return "YES"
#
# print(IsAscending([1, 7, 9]))
# print(IsAscending([1, 7, 7]))


#2

# def KthAppearance(A, a, k):
#     cnt = 0
#     for i in range(len(A)):
#         if A[i] == a:
#             cnt += 1
#             if cnt == k:
#                 return i
#     return -1
#
# print(KthAppearance([1, 2, 1, 3, 2, 3, 2, 3, 2, 2], 3, 2))


# Сортировка №1

# volumes = [200, 50]
#
# def max_users(S, volumes_list):
#     count_users = 0
#     current_memory = 0
#     for i in sorted(volumes_list):
#         if current_memory + i <= S:
#             count_users += 1
#             current_memory += i
#     return count_users
#
# print(max_users(100, volumes))


# №2

# distances = [10, 20, 30]
# tariffs = [50, 20, 30]
#
# def min_sum(dsts, trfs):
#     sum_charge = 0
#     for i, j in zip(sorted(trfs), sorted(dsts, reverse=True)):
#         sum_charge += i * j
#     return sum_charge
#
# print(min_sum(distances, tariffs))

# №1

# def count_numbers(counts):
#     for i in range(9):
#         print(counts[i], end=" ")
#
# counts = [0] * 9
#
# while True:
#     x = int(input())
#     if x == 0:
#         count_numbers(counts)
#         break
#     elif 1 <= x <= 9:
#         counts[x - 1] += 1
#         continue
#     else:
#         print("Invalid input")
#         continue


# №2

# def find_num(lst, num):
#     for i in range(len(lst)):
#         if lst[i] == num:
#             return i
#     return -1
#
# print(find_num([7,9,5,6,-99,-32,10,-6,45,14], -32))


# Регулярные выражения

import re

# №1

# s = input()
# result = re.match(r"\w+", s)
#
# print(result.group())

# №2

# s = input()
# result = re.search(r"\d{2}/\d{2}/\d{4}", s)
# print(result.group())

# №3

# pattern = r"^(\+7\d{10}|8\d{10}|\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}|\+7-\d{3}-\d{3}-\d{2}-\d{2})$"
#
# phone = input("Enter your phone number: ")
#
# if re.fullmatch(pattern, phone):
#     print("Valid Phone Number")
# else:
#     print("Invalid Phone Number")

# №4

# html = """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Test Page</title>
# </head>
# <body>
#     <h1>Main Heading</h1>
#
#     <p>This is the first paragraph.</p>
#     <p>This is the second paragraph.</p>
#
#     <a href="https://example.com">Example link</a>
#     <a href="https://google.com">Google</a>
#
#     <div>
#         <p>Paragraph inside div</p>
#     </div>
# </body>
# </html>
# """
#
# pattern = r"<.*?>"
#
# text = re.sub(pattern, "", html)
# print(text)