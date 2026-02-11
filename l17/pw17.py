# Практическая работа №17: Объектно-ориентированное
# программирование
# Выполните следующие задания:
# Задание №1
# Создайте класс Число (или используйте уже ранее созданный вами). Класс число хранит
# внутри одно значение. Используя перегрузку операторов реализуйте для него
# арифметические операции для работы с числом (операции +, -, *, /).

# class Number:
#     def __init__(self, value):
#         if isinstance(value, bool):
#             raise TypeError('value must be int or float')
#         if isinstance(value, int) or isinstance(value, float):
#             self.value = value
#         else:
#             raise TypeError('value must be int or float')
#
#     def __add__(self, other):
#         if isinstance(other, Number):
#             return Number(self.value + other.value)
#         elif isinstance(other, int) or isinstance(other, float):
#             return Number(self.value + other)
#         else:
#             return NotImplemented
#
#     def __radd__(self, other):
#         return self.__add__(other)
#
#     def __sub__(self, other):
#         if isinstance(other, Number):
#             return Number(self.value - other.value)
#         elif isinstance(other, int) or isinstance(other, float):
#             return Number(self.value - other)
#         else:
#             return NotImplemented
#
#     def __mul__(self, other):
#         if isinstance(other, Number):
#             return Number(self.value * other.value)
#         elif isinstance(other, int) or isinstance(other, float):
#             return Number(self.value * other)
#         else:
#             return NotImplemented
#
#     def __rmul__(self, other):
#         return self.__mul__(other)
#
#     def __truediv__(self, other):
#         if isinstance(other, Number):
#             return Number(self.value / other.value)
#         elif isinstance(other, int) or isinstance(other, float):
#             return Number(self.value / other)
#         else:
#             return NotImplemented
#
#     def __repr__(self):
#         return f'{self.__class__.__name__}({self.value})'
#
# n1 = Number(94)
# n2 = Number(6)
# print(n1 + n2)
# print(n1 - n2)
# print(n1 * n2)
# print(n1 / n2)
# print(n1*3)
# print(3*n1)
# print(n1/3)
# print(n1, n2)



# Задание №2
# Создайте класс Дробь (или используйте уже ранее созданный вами). Используя
# перегрузку операторов реализуйте для него арифметические операции для работы с дробями
# (операции +, -, *, /).

# import math
#
# class Fraction:
#     def __init__(self, numerator=0, denominator=1):
#         if denominator == 0:
#             raise ValueError("Знаменатель не может быть равен 0")
#         if denominator < 0:
#             numerator *= -1
#             denominator *= -1
#         cd = math.gcd(numerator, denominator)
#         numerator //= cd
#         denominator //= cd
#         self.__num = numerator
#         self.__den = denominator
#
#     def __repr__(self):
#         return f"Fraction({self.__num}, {self.__den})"
#
#     def __add__(self, other):
#         if not isinstance(other, Fraction):
#             return NotImplemented
#         return Fraction(
#             self.__num * other.__den + other.__num * self.__den, self.__den * other.__den
#         )
#
#     def __sub__(self, other):
#         if not isinstance(other, Fraction):
#             return NotImplemented
#         return Fraction(
#             self.__num * other.__den - other.__num * self.__den, self.__den * other.__den
#         )
#
#     def __mul__(self, other):
#         if not isinstance(other, Fraction):
#             return NotImplemented
#         return Fraction(
#             self.__num * other.__num, self.__den * other.__den
#         )
#
#     def __truediv__(self, other):
#         if not isinstance(other, Fraction):
#             return NotImplemented
#         if other.__num == 0:
#             raise ZeroDivisionError("Знаменатель не может быть равен 0 (проверьте числитель дроби-делителя)")
#         return Fraction(
#             self.__num * other.__den, self.__den * other.__num
#         )
#
# # попросил чат дать код для проверки класса Fraction
#
# def test_fraction():
#     # создание и нормализация
#     f1 = Fraction(2, 4)
#     f2 = Fraction(-3, -6)
#     f3 = Fraction(1, -2)
#     f4 = Fraction(0, 5)
#
#     print(f1)  # Fraction(1, 2)
#     print(f2)  # Fraction(1, 2)
#     print(f3)  # Fraction(-1, 2)
#     print(f4)  # Fraction(0, 1)
#
#     # сложение
#     print(Fraction(1, 2) + Fraction(1, 3))   # Fraction(5, 6)
#
#     # вычитание
#     print(Fraction(3, 4) - Fraction(1, 2))   # Fraction(1, 4)
#
#     # умножение
#     print(Fraction(2, 3) * Fraction(3, 5))   # Fraction(2, 5)
#
#     # деление
#     print(Fraction(2, 3) / Fraction(4, 5))   # Fraction(5, 6)
#
#     # цепочки операций
#     result = Fraction(1, 2) + Fraction(1, 3) * Fraction(3, 4)
#     print(result)  # Fraction(3, 4)
#
#     # проверка NotImplemented
#     try:
#         print(Fraction(1, 2) + 1)
#     except TypeError as e:
#         print("TypeError ok:", e)
#
#     # деление на ноль
#     try:
#         print(Fraction(1, 2) / Fraction(0, 1))
#     except ZeroDivisionError as e:
#         print("ZeroDivisionError ok:", e)
#
#
# test_fraction()



# Задание №3
# Создайте класс Библиотека. Класс предназначен для хранения информации о
# библиотеке (название, адрес, количество книг). Реализуйте необходимые для класса методы.
# Используя перегрузку операторов реализуйте для него следующие арифметические операции:
# + добавляет к количеству книг указанное значение;
# - вычитает из количества книг указанное значение;
# += добавляет к количеству книг указанное значение;
# -= вычитает из количества книг указанное значение; Используя перегрузку
# операторов реализуйте (сравнение по количеству книг):
# <;
# >;
# <=;
# >=;
# ==;
# !=.

# from functools import total_ordering
#
# @total_ordering
# class Library:
#     def __init__(self, name, address, books):
#         if not isinstance(books, int):
#             raise TypeError("books should be an integer")
#         if books < 0:
#             raise ValueError("books should be >= 0")
#         self.name = name
#         self.address = address
#         self.books = books
#
#     def __add__(self, other):
#         if not isinstance(other, int):
#             return NotImplemented
#         if self.books + other < 0:
#             raise ValueError("books should be >= 0")
#         return Library(self.name, self.address, self.books + other)
#
#     def __sub__(self, other):
#         if not isinstance(other, int):
#             return NotImplemented
#         return Library.__add__(self, -other)
#
#     def __iadd__(self, other):
#         if not isinstance(other, int):
#             return NotImplemented
#         if self.books + other < 0:
#             raise ValueError("books should be >= 0")
#         self.books += other
#         return self
#
#     def __isub__(self, other):
#         if not isinstance(other, int):
#             return NotImplemented
#         return Library.__iadd__(self, -other)
#
#     def __eq__(self, other):
#         if isinstance(other, int):
#             return self.books == other
#         elif isinstance(other, Library):
#             return self.books == other.books
#         else:
#             return NotImplemented
#
#     def __lt__(self, other):
#         if isinstance(other, int):
#             return self.books < other
#         elif isinstance(other, Library):
#             return self.books < other.books
#         else:
#             return NotImplemented
#
# # просим чат сгенерировать код для проверки
#
# def test_library():
#     lib = Library("Central", "Main st", 100)
#
#     # базовые поля
#     print(lib.name, lib.address, lib.books)  # Central Main st 100
#
#     # + (не изменяет объект)
#     lib2 = lib + 50
#     print(lib.books)   # 100
#     print(lib2.books)  # 150
#
#     # - (не изменяет объект)
#     lib3 = lib - 30
#     print(lib.books)   # 100
#     print(lib3.books)  # 70
#
#     # += (изменяет объект)
#     lib += 20
#     print(lib.books)   # 120
#
#     # -= (изменяет объект)
#     lib -= 50
#     print(lib.books)   # 70
#
#     # сравнение с int
#     print(lib == 70)   # True
#     print(lib < 100)   # True
#     print(lib > 50)    # True
#     print(lib >= 70)   # True
#     print(lib <= 69)   # False
#
#     # сравнение Library ↔ Library
#     lib_a = Library("A", "X", 30)
#     lib_b = Library("B", "Y", 50)
#
#     print(lib_a < lib_b)    # True
#     print(lib_a == lib_b)   # False
#     print(lib_b > lib_a)    # True
#
#     # NotImplemented → TypeError
#     try:
#         print(lib + "10")
#     except TypeError:
#         print("TypeError ok (+ str)")
#
#     try:
#         print(lib < "100")
#     except TypeError:
#         print("TypeError ok (< str)")
#
#     # уход в минус → ValueError
#     try:
#         lib - 1000
#     except ValueError:
#         print("ValueError ok (negative books)")
#
#     try:
#         lib -= 1000
#     except ValueError:
#         print("ValueError ok (negative books, in-place)")
#
#     print("ALL TESTS PASSED")
#
#
# test_library()



# Задание №4
# Создайте класс Date, который будет содержать информацию о дате (день, месяц, год). С
# помощью механизма перегрузки операторов, определите операцию разности двух дат
# (результат в виде количества дней между датами), а также операцию увеличения даты на
# определенное количество дней.

# import datetime
#
# class Date:
#     def __init__(self, day, month, year):
#         self._date = datetime.date(year, month, day)
#     def __sub__(self, other):
#         if not isinstance(other, Date):
#             return NotImplemented
#         return (self._date - other._date).days
#     def __add__(self, other):
#         if isinstance(other, int):
#             delta = datetime.timedelta(days=other)
#         elif isinstance(other, datetime.timedelta):
#             delta = other
#         else:
#             return NotImplemented
#         new_date = self._date + delta
#         return Date(new_date.day, new_date.month, new_date.year)
#     def __radd__(self, other):
#         return self.__add__(other)
#     def __iadd__(self, other):
#         if isinstance(other, int):
#             delta = datetime.timedelta(days=other)
#         elif isinstance(other, datetime.timedelta):
#             delta = other
#         else:
#             return NotImplemented
#         self._date += delta
#         return self
#     def __repr__(self):
#         return str(self._date)
#
# # берем код для проверки
#
# def test_date():
#     d1 = Date(1, 1, 2024)
#     d2 = Date(10, 1, 2024)
#
#     # разность дат
#     print(d2 - d1)   # 9
#     print(d1 - d2)   # -9
#
#     # сложение с int
#     d3 = d1 + 10
#     print(d3 - d1)   # 10
#     print(d1 - Date(1, 1, 2024))  # 0 (d1 не изменился)
#
#     # сложение с timedelta
#     d4 = d1 + datetime.timedelta(days=15)
#     print(d4 - d1)   # 15
#
#     # обратное сложение
#     d5 = 20 + d1
#     print(d5 - d1)   # 20
#
#     d6 = datetime.timedelta(days=7) + d1
#     print(d6 - d1)   # 7
#
#     # += (изменение даты)
#     d7 = Date(1, 1, 2024)
#     d7 += 5
#     print(d7 - Date(1, 1, 2024))  # 5
#
#     d7 += datetime.timedelta(days=10)
#     print(d7 - Date(1, 1, 2024))  # 15
#
#     print(d7)
#
#     # неподдерживаемые типы
#     try:
#         d1 + "10"
#     except TypeError:
#         print("TypeError ok (+ str)")
#
#     try:
#         d1 - "2024-01-01"
#     except TypeError:
#         print("TypeError ok (- str)")
#
#     try:
#         d1 += "5"
#     except TypeError:
#         print("TypeError ok (+= str)")
#
#     # некорректная дата
#     try:
#         Date(31, 2, 2024)
#     except ValueError:
#         print("ValueError ok (invalid date)")
#
#     print("ALL DATE TESTS PASSED")
#
#
# test_date()