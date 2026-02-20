# class Polygon:                      # объявляем класс Polygon
#     def __init__(self, no_of_sides): # конструктор, вызывается при создании объекта
#         self.n = no_of_sides         # сохраняем количество сторон
#         self.sides = [0 for i in range(no_of_sides)]
#                                      # создаём список сторон, заполненный нулями
#
#     def inputSides(self):            # метод ввода сторон
#         self.sides = [
#             float(input("Введите сторону " + str(i+1) + " : "))
#             for i in range(self.n)
#         ]                             # по очереди вводим длину каждой стороны
#
#     def dispSides(self):             # метод вывода сторон
#         for i in range(self.n):      # перебираем все стороны
#             print("Сторона", i+1, " — ", self.sides[i])
#                                      # выводим номер и длину стороны
#
# class Triangle(Polygon):             # Triangle наследуется от Polygon
#     def __init__(self):
#         Polygon.__init__(self, 3)    # вызываем конструктор Polygon и задаём 3 стороны
#
#     def findArea(self):              # метод вычисления площади треугольника
#         a, b, c = self.sides         # распаковываем список сторон в три переменные
#         s = (a + b + c) / 2          # вычисляем полупериметр
#         area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
#                                      # формула Герона для площади
#         print('Площадь треугольника равна %0.2f' % area)
#                                      # выводим площадь с округлением до 2 знаков
#
# t = Triangle()
# t.inputSides()
# t.dispSides()
# t.findArea()





# from math import pi                 # импортируем число π
#
# class Shape:                        # базовый класс для фигур
#     def describe(self):             # метод описания объекта
#         print("Класс: {}".format(self.__class__.__name__))
#                                      # __class__ — класс объекта
#                                      # __name__ — имя класса
#
# class Circle(Shape):                # Circle наследуется от Shape
#     def __init__(self, radius):     # конструктор круга
#         self.r = radius             # сохраняем радиус
#
#     def area(self):                 # метод площади
#         return pi * self.r ** 2     # формула площади круга
#
#     def perimeter(self):            # метод периметра
#         return 2 * pi * self.r      # длина окружности
#
# class Rectangle(Shape):             # Rectangle наследуется от Shape
#     def __init__(self, a, b):       # конструктор прямоугольника
#         self.a = a                  # сохраняем сторону a
#         self.b = b                  # сохраняем сторону b
#
#     def area(self):                 # метод площади
#         return self.a * self.b      # a × b
#
#     def perimeter(self):            # метод периметра
#         return 2 * (self.a + self.b)# 2 × (a + b)
#
# class Square(Rectangle):            # Square наследуется от Rectangle
#     pass                            # ничего не добавляем
#
# side = 5                            # длина стороны
# sq = Square(side, side)             # вызывается Rectangle.__init__
# print(sq.area())                    # используется Rectangle.area → 25
# print(sq.perimeter())               # используется Rectangle.perimeter → 20
#
# class Square(Rectangle):            # Square — частный случай Rectangle
#     def __init__(self, size):       # свой конструктор
#         print('Создаём квадрат')    # дополнительное действие
#         super().__init__(size, size)# вызываем Rectangle.__init__
#
# sq = Square(2)                      # выводится "Создаём квадрат"
# print(sq.area())                    # 2 × 2 → 4
# print(sq.perimeter())               # 2 × (2 + 2) → 8
# print(sq.a)                         # a создан в Rectangle → 2

# from math import pi                          # импортируем число π
#
# class Shape:                                # базовый класс фигур
#     def describe(self):                     # метод описания фигуры
#         print("Периметр: {}\nПлощадь: {}".format(
#             self.perimeter(),               # вызывается метод perimeter() конкретного объекта
#             self.area()                     # вызывается метод area() конкретного объекта
#         ))
#
# class Circle(Shape):                        # круг наследуется от Shape
#     def __init__(self, radius):             # конструктор круга
#         self.r = radius                     # сохраняем радиус
#
#     def area(self):                         # площадь круга
#         return pi * self.r ** 2             # формула площади
#
#     def perimeter(self):                    # периметр круга
#         return 2 * pi * self.r              # длина окружности
#
# class Rectangle(Shape):                     # прямоугольник наследуется от Shape
#     def __init__(self, a, b):               # конструктор
#         self.a = a                          # первая сторона
#         self.b = b                          # вторая сторона
#
#     def area(self):                         # площадь прямоугольника
#         return self.a * self.b              # a × b
#
#     def perimeter(self):                    # периметр прямоугольника
#         return 2 * (self.a + self.b)        # 2 × (a + b)
#
# class Square(Rectangle):                    # квадрат — частный случай прямоугольника
#     def __init__(self, size):               # свой конструктор
#         super().__init__(size, size)        # вызываем Rectangle.__init__(a, b)
#
# sq = Square(2)                              # создаём квадрат со стороной 2
# sq.describe()                               # полиморфный вызов методов area и perimeter





# from math import tan, pi                              # импортируем tan (тангенс) и pi (π)
#
# class Shape:                                         # базовый класс фигур
#     def describe(self):                              # универсальный метод описания
#         print("Класс: {}\nПериметр: {}\nПлощадь: {}".format(
#             self.__class__.__name__,                 # имя реального класса объекта
#             self.perimeter(),                        # вызывается perimeter() наследника
#             self.area()                              # вызывается area() наследника
#         ))
#
# class Rectangle(Shape):                              # прямоугольник
#     def __init__(self, a, b):                        # конструктор прямоугольника
#         self.a = a                                   # первая сторона
#         self.b = b                                   # вторая сторона
#
#     def area(self):                                  # площадь прямоугольника
#         return self.a * self.b                       # a × b
#
#     def perimeter(self):                             # периметр прямоугольника
#         return 2 * (self.a + self.b)                 # 2 × (a + b)
#
# class RegularPolygon:                                # правильный многоугольник
#     def __init__(self, side, n):                     # side — длина стороны, n — число сторон
#         self.side = side                             # сохраняем длину стороны
#         self.n = n                                   # сохраняем количество сторон
#
#     def inscribed_circle_radius(self):               # радиус вписанной окружности
#         return self.side / (2 * tan(pi / self.n))    # формула радиуса вписанной окружности
#
# class Square(Rectangle, RegularPolygon):             # квадрат наследуется от Rectangle и RegularPolygon
#     def __init__(self, a):                           # конструктор квадрата
#         Rectangle.__init__(self, a, a)               # явно вызываем Rectangle.__init__
#         RegularPolygon.__init__(self, a, 4)          # явно вызываем RegularPolygon.__init__ (4 стороны)
#
# s = Square(5)                                        # создаём квадрат со стороной 5
# s.describe()                                        # метод из Shape, использует методы Rectangle
# print(s.inscribed_circle_radius())                  # метод из RegularPolygon
#
# print(Square.__mro__)