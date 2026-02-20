# Практическая работа №15: ООП. Полиморфизм
# Задания №1
# В качестве практической работы попробуйте самостоятельно перегрузить оператор
# сложения. Для его перегрузки используется метод __add__(). Он вызывается, когда объекты
# класса, имеющего данный метод, фигурируют в операции сложения, причем с левой стороны.
# Это значит, что в выражении a + b у объекта a должен быть метод __add__(). Объект b может
# быть чем угодно, но чаще всего он бывает объектом того же класса. Объект b будет
# автоматически передаваться в метод __add__() в качестве второго аргумента (первый – self).
# Отметим, в Python также есть правосторонний метод перегрузки сложения - __radd__().
# Согласно полиморфизму ООП, возвращать метод __add__() может что угодно. Может
# вообще ничего не возвращать, а "молча" вносить изменения в какие-то уже существующие
# объекты. Допустим, в вашей программе метод перегрузки сложения будет возвращать новый
# объект того же класса.

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplemented
#         return Vector(self.x + other.x, self.y + other.y)
#
#     def __radd__(self, other):
#         if other == 0:
#             return self
#         return NotImplemented
#
#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"
#
# v1 = Vector(2, 3)
# v2 = Vector(5, 7)
#
#
# v4 = v1 + v2
# print(v4)
# v3 = sum([v1, v2])
# print(v3)



# Задания №2
# Пересмотрите алгоритм решения прошлой практической работы, с использованием
# инкапсуляции. Реализуйте старый алгоритм с использованием полиморфизма.
# Опишите четыре класса PCGames, PS4Games, XboxGames, MobileGames. Добавьте
# каждому классу дополнительные поля и также опишите метод getName, который возвращает
# имя игры.

# class Games:
#     Year = None
#
#     def __init__(self, year, name):
#         self.Year = year
#         self.name = name
#
#     def _details(self):
#         return ""
#
#     def getName(self):
#         return f"{self.name}{self._details()}"
#
# class PCGames(Games):
#     def __init__(self, year, name, min_specs):
#         super().__init__(year, name)
#         self.min_specs = min_specs
#
#     def _details(self):
#         return f", min specs: {self.min_specs}"
#
# class PS4Games(Games):
#     def __init__(self, year, name, exclusive):
#         super().__init__(year, name)
#         self.exclusive = exclusive
#
#     def _details(self):
#         return f", exclusive: {self.exclusive}"
#
# class XboxGames(Games):
#     def __init__(self, year, name, game_pass):
#         super().__init__(year, name)
#         self.game_pass = game_pass
#
#     def _details(self):
#         return f", Game Pass: {self.game_pass}"
#
# class MobileGames(Games):
#     def __init__(self, year, name, ads):
#         super().__init__(year, name)
#         self.ads = ads
#
#     def _details(self):
#         return f", ads: {self.ads}"
#
# games = [
#     PCGames(2013, "Dota 2", "8 GB RAM"),
#     PS4Games(2018, "God of War", True),
#     XboxGames(2020, "Forza", True),
#     MobileGames(2016, "Clash Royale", True),
# ]
#
# for game in games:
#     print(game.getName())



# Задания №3
# Пересмотрите алгоритм решения прошлой практической работы, с использованием инкапсуляции.
# Реализуйте старый алгоритм с использованием полиморфизма.
# Опишите классы Russia, Canada, Germany. Добавьте каждому классу поле population и опишите
# метод setPopulation и getPopulation.

# class Country:
#     def __init__(self):
#         self.__population = 0
#
#     def setPopulation(self, population):
#         if population < 0:
#             raise ValueError("Население не может быть отрицательным числом")
#         self.__population = population
#
#     def getPopulation(self):
#         return self.__population
#
# class Russia(Country):
#     pass
#
# class Canada(Country):
#     pass
#
# class Germany(Country):
#     pass
#
# countries = [Russia(), Canada(), Germany()]
#
# for country in countries:
#     country.setPopulation(100)
#     print(country.getPopulation())

