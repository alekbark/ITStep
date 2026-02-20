# Домашнее задание №17: Объектно-ориентированное
# программирование
# Задание №1
# Создайте класс Circle (окружность). Для данного класса реализуйте ряд перегруженных
# операторов:
# Проверка на равенство радиусов двух окружностей (операция = =);
# Сравнения длин двух окружностей (операции >, <, <=,>=);
# Пропорциональное изменение размеров окружности, путем изменения ее радиуса
# (операции + - += -=).

# import math
# from functools import total_ordering
# from numbers import Real
#
# @total_ordering
# class Circle:
#     def __init__(self, radius):
#         if radius <= 0:
#             raise ValueError("Radius cannot be negative")
#         self.radius = radius
#
#     @property
#     def circumference(self):
#         return 2 * math.pi * self.radius
#
#     def __eq__(self, other):
#         if not isinstance(other, Circle):
#             return NotImplemented
#         return self.radius == other.radius
#     def __lt__(self, other):
#         if not isinstance(other, Circle):
#             return NotImplemented
#         return self.circumference < other.circumference
#
#     def __add__(self, other):
#         if not isinstance(other, Real):
#             return NotImplemented
#         return Circle(self.radius + other)
#
#     def __sub__(self, other):
#         if not isinstance(other, Real):
#             return NotImplemented
#         return Circle(self.radius - other)
#
#     def __iadd__(self, other):
#         if not isinstance(other, Real):
#             return NotImplemented
#         self.radius = self.__add__(other).radius
#         return self
#
#     def __isub__(self, other):
#         if not isinstance(other, Real):
#             return NotImplemented
#         self.radius = self.__sub__(other).radius
#         return self
#
#     def __repr__(self):
#         return f"Circle(radius={self.radius}, circumference={self.circumference})"
#
# # код для проверки от чата
#
# def demo():
#     print("Создание окружностей")
#     c1 = Circle(10)
#     c2 = Circle(5)
#     c3 = Circle(10)
#
#     print("c1:", c1)
#     print("c2:", c2)
#     print("c3:", c3)
#
#     print("\n== (равенство радиусов)")
#     print("c1 == c3 ->", c1 == c3)
#     print("c1 == c2 ->", c1 == c2)
#
#     print("\nСравнение длин окружностей")
#     print("c1 > c2 ->", c1 > c2)
#     print("c1 < c2 ->", c1 < c2)
#     print("c1 >= c3 ->", c1 >= c3)
#     print("c2 <= c1 ->", c2 <= c1)
#
#     print("\n+ и - (новые объекты)")
#     c4 = c1 + 3
#     c5 = c1 - 4
#     print("c1:", c1)
#     print("c4 = c1 + 3 ->", c4)
#     print("c5 = c1 - 4 ->", c5)
#
#     print("\n+= и -= (изменение на месте)")
#     c1 += 2
#     print("c1 += 2 ->", c1)
#
#     c1 -= 5
#     print("c1 -= 5 ->", c1)
#
#     print("\nПроверка ошибок")
#     try:
#         print("c1 - 100")
#         c1 - 100
#     except ValueError as e:
#         print("Ошибка:", e)
#
#     try:
#         print("c1 -= 100")
#         c1 -= 100
#     except ValueError as e:
#         print("Ошибка:", e)
#
#
# demo()
