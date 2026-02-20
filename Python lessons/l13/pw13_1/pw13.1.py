# Задание №1.
# Напишите программу, которая запрашивает ввод двух значений. Если хотя бы одно из
# них не является числом, то должна выполняться конкатенация, то есть соединение, строк. В
# остальных случаях введенные числа суммируются.


# a, b = input("Первое значение: "), input("Второе значение: ")
# try:
#     result = float(a) + float(b)
# except ValueError:
#     result = a + b
#
# print("Результат: ", result)



# Задание №2.
# Напишите программу, в которой я ввожу трехзначное число. Найти сумму,
# произведение его цифр. В случае ввода текста, или деления на 0 выведите сообщение.

# x = input("Введите трехзначное число: ")
#
# try:
#     n = int(x)
#
#     a = n // 100
#     b = (n // 10) % 10
#     c = n % 10
#
#     if a == 0 and b == 0 and c == 0:
#         raise ZeroDivisionError
#
#     print("Сумма: ", a + b + c)
#     print("Произведение: ", a * b * c)
#
# except ZeroDivisionError:
#     print("Вы не можете делить на ноль")
# except ValueError:
#     print("Ошибка: введен текст, а не число")



# Задание №3.
# Заданы две клетки шахматной доски. Если они покрашены в один цвет, то выведите
# слово YES, а если в разные цвета — то NO.
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и
# номер строки сначала для первой клетки, потом для второй клетки.

# try:
#     x1, y1, x2, y2 = map(int, input().split())
#
#     if not all(1 <= v <= 8 for v in (x1, x2, y1, y2)):
#         raise ValueError
#     color1 = (x1 + y1) % 2
#     color2 = (x2 + y2) % 2
#
#     print("YES" if color1 == color2 else "NO")
#
# except ValueError:
#     print("Error, try again")



# Требуется определить, бьет ли ладья, стоящая на клетке с указанными координатами
# (номер строки и номер столбца), фигуру, стоящую на другой указанной клетке.
# Вводятся четыре числа: координаты ладьи (два числа) и координаты другой фигуры (два
# числа), каждое число вводится в отдельной строке. Координаты - целые числа в интервале от 1 до 8.
# Требуется вывести слово YES, если ладья сможет побить фигуру за 1 ход и NO - в
# противном случае. Ладья ходит по прямым линиям (горизонтальным и вертикальным).
# Обработайте исключение если человек введет координаты в не правильном порядке.

# try:
#     r1, c1, r2, c2 = map(int, input().split())
#
#     if not all(1 <= v <= 8 for v in (r1, c1, r2, c2)):
#         raise ValueError
#
#     print("YES" if r1 == r2 or c1 == c2 else "NO")
#
# except ValueError:
#     print("Error, try again")



# Задание №4.
# Дополните предыдущий код, фигурой короля и его действиями.
# Создайте диалог с пользователем, узнайте какой из фигур будет выполнять ход игрок.
# Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку.
# Даны две различные клетки шахматной доски, определите, может ли король попасть
# с первой клетки на вторую одним ходом.
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и
# номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести YES,
# если из первой клетки ходом короля можно попасть во вторую или NO в противном случае.
# Обработайте все исключения, которые могут встретиться в программе.

# try:
#     piece = input("Фигура (rook / king): ").lower()
#
#     r1, c1, r2, c2 = map(int, input().split())
#
#     if piece not in ("rook", "king"):
#         raise ValueError
#
#     if not all(1 <= v <= 8 for v in (r1, c1, r2, c2)):
#         raise ValueError
#     if piece == "rook":
#         can_move = r1 == r2 or c1 == c2
#     else:
#         can_move = max(abs(r1 - r2), abs(c1 - c2)) == 1
#
#     print("YES" if can_move else "NO")
#
# except ValueError:
#     print("Error, try again")



# Обработка исключений
# Задание №1
# Программа написана верно, однако содержат места потенциальных ошибок.
# Для каждой задачи: найдите потенциальные источники ошибок (укажите номера строк
# в строке документации); используя конструкцию try добавьте в код обработку
# соответствующих исключений.

# def avg(a, b):
#     return (a * b) ** 0.5
#
# try:
#     a = float(input("a = "))
#     b = float(input("b = "))
#
#     if a * b < 0:
#         raise ValueError
#
#     c = avg(a, b)
#     print("Среднее геометрическое = {:.2f}".format(c))
#
# except ValueError:
#     print("Ошибка, введены некорректные данные")



# Задание №2
# Римское число
# Создайте класс Roman (РимскоеЧисло), представляющий римское число и
# поддерживающий операции +, -, *, /.
# При реализации класса:
# операции +, -, *, / реализуйте как специальные методы;
# методы преобразования как статические методы.
# Опишите все исключения, возможные в программе. (Например, неверный ввод, ошибка
# деления на 0).

# class Roman:
#     _map = {
#         'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
#     }
#
#     def __init__(self, value: str):
#         self.value = value
#         self.number = self.to_int(value)
#
#     @staticmethod
#     def to_int(roman: str) -> int:
#         if not roman or not all(c in Roman._map for c in roman):
#             raise ValueError("Неверный ввод римского числа")
#
#         total = 0
#         prev = 0
#
#         for c in reversed(roman):
#             cur = Roman._map[c]
#             if cur < prev:
#                 total -= cur
#             else:
#                 total += cur
#             prev = cur
#
#         return total
#
#     @staticmethod
#     def to_roman(num: int) -> str:
#         if num <= 0:
#             raise ValueError("Римское число должно быть > 0")
#
#         vals = [
#             (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
#             (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'),
#             (5, 'V'), (4, 'IV'), (1, 'I')
#         ]
#
#         res = ""
#
#         for v, s in vals:
#             while num >= v:
#                 res += s
#                 num -= v
#         return  res
#
#     def __op(self, other, func):
#         if not isinstance(other, Roman):
#             raise TypeError("Ожидался Roman")
#         result = func(self.number, other.number)
#         return Roman(self.to_roman(result))
#
#     def __add__(self, other):
#         return self.__op(other, lambda a, b: a + b)
#
#     def __sub__(self, other):
#         return self.__op(other, lambda a, b: a - b)
#
#     def __mul__(self, other):
#         return self.__op(other, lambda a, b: a * b)
#
#     def __truediv__(self, other):
#         if other.number == 0:
#             raise ZeroDivisionError("Деление на ноль")
#         return self.__op(other, lambda a, b: a // b)
#
#     def __str__(self):
#         return self.value
#
# x = Roman("IV")
# y = Roman("XI")
#
# print(x + y)
# print(x * y)
# print(y / x)
# print(y - x)



# Задание №1
# Создайте собственное исключение, которое будет вызываться в случае, если в функцию
# check_name() передано имя длиннее четырёх символов.
# Подсказка:
# Создайте класс исключения, наследующийся от другого класса исключения.

# class NameTooLongError(ValueError):
#     pass
#
# def check_name(name: str):
#     if len(name) > 4:
#         raise NameTooLongError("Имя длиннее 4 символов")
#     return "OK"
#
# try:
#     check_name("Alex")
#     check_name("Alexander")
# except NameTooLongError as err:
#     print(err)
#
# print(check_name("Alek"))



# Задание №2
# Банк предлагает ряд вкладов для физических лиц:
# Срочный вклад: расчет прибыли осуществляется по формуле простых процентов;
# Бонусный вклад: бонус начисляется в конце периода как % от прибыли, если вклад
# больше определенной суммы;
# Вклад с капитализацией процентов.
# Реализуйте приложение, которое бы позволило подобрать клиенту вклад по заданным
# параметрам.
# Опишите все исключения, возможные в программе. (Например, неверный вод, ошибка
# деления на 0 и т.д.).

# def term_deposit(amount, rate, years):
#     profit = amount * rate / 100 * years
#     return profit
#
# def bonus_deposit(amount, rate, years, bonus_limit, bonus_rate):
#     profit = amount * rate / 100 * years
#     if amount > bonus_limit:
#         bonus = profit * bonus_rate / 100
#         profit += bonus
#     return profit
#
# def capitalization_deposit(amount, rate, years):
#     if years <= 0:
#         raise ValueError("Срок должен быть больше 0")
#     rate = rate / 100
#     total = amount * (1 + rate) ** years
#     return total - amount
#
# try:
#     amount = float(input("Введите сумму вклада: "))
#     years = int(input("Введите срок в годах: "))
#     rate = float(input("Введите процентную ставку: "))
#
#     if amount <= 0 or years <= 0 or rate <= 0:
#         raise ValueError("Все значения должны быть больше 0")
#
#     deposit_type = input(
#         "Тип вклада (term/bonus/capital): "
#     ).lower()
#
#     if deposit_type == "term":
#         profit = term_deposit(amount, rate, years)
#     elif deposit_type == "bonus":
#         bonus_limit = 200_000
#         bonus_rate = 5
#
#         profit = bonus_deposit(amount, rate, years, bonus_limit, bonus_rate)
#     elif deposit_type == "capital":
#         profit = capitalization_deposit(amount, rate, years)
#     else:
#         raise ValueError("Неверный тип вклада")
#
#     print(f"Прибыль по вкладу: {profit:.2f}")
# except ValueError as e:
#     print("Ошибка:", e)
# except ZeroDivisionError:
#     print("Ошибка: деление на 0")
# except Exception as e:
#     print("Неизвестная ошибка:", e)

