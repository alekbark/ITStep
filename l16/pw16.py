# Практическая работа №16: Объектно-ориентированное
# программирование
# Выполните следующее задание:
# В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее
# уникальный номер объекта, и свойство, в котором хранится принадлежность команде. У
# солдат есть метод "иду за героем", который в качестве аргумента принимает объект типа
# "герой". У героев есть метод увеличения собственного уровня.
# В основной ветке программы создается по одному герою для каждой команды. В цикле
# генерируются объекты-солдаты. Их принадлежность команде определяется случайно.
# Солдаты разных команд добавляются в разные списки.
# Измеряется длина списков солдат противоборствующих команд и выводится на экран.
# У героя, принадлежащего команде с более длинным списком, увеличивается уровень.
# Отправьте одного из солдат первого героя следовать за ним. Выведите на экран
# идентификационные номера этих двух юнитов.

# import random
#
# class Unit:
#     _id_counter = 1
#
#     def __init__(self, team):
#         self.id = Unit._id_counter
#         Unit._id_counter += 1
#         self.team = team
#
# class Hero(Unit):
#     def __init__(self, team):
#         super().__init__(team)
#         self.level = 1
#
#     def level_up(self):
#         self.level += 1
#
# class Soldier(Unit):
#     def __init__(self, team):
#         super().__init__(team)
#         self.hero = None
#
#     def follow(self, hero):
#         if isinstance(hero, Hero) and hero.team == self.team:
#             self.hero = hero
#
# teams = ["red", "blue"]
#
# heroes = {team: Hero(team) for team in teams}
#
# soldiers = {team: [] for team in teams}
#
# for _ in range(10):
#     team = random.choice(teams)
#     soldiers[team].append(Soldier(team))
#
# for team in teams:
#     print(team, "солдат:", len(soldiers[team]))
#
# team_with_more = max(teams, key=lambda t: len(soldiers[t]))
#
# heroes[team_with_more].level_up()
#
# first_team = teams[0]
# soldier = soldiers[first_team][0]
# hero = heroes[first_team]
#
# soldier.follow(hero)
#
# print("ID солдата:", soldier.id)
# print("ID героя:", hero.id)



# ООП. Множественное наследование
# Выполните следующие задания:
# Задание № 1
# Задан класс Point, описывающий точку с координатами x, y на координатной плоскости.
# Используя механизм наследования, нужно расширить возможности класса Point путем
# добавления нового атрибута цвета. Для этого реализовать подкласс PointColor.
# В классе Point реализовать следующие атрибуты:
# − координаты точки;
# − метод иницализации, который получает 2 параметра — координаты точки x, y;
# − метод вычисления расстояния от точки до начала координат;
# − метод getPoint(), который возвращает точку в виде списка.
# В подклассе PointColor реализовать следующие атрибуты:
# − цвет точки color;
# − метод начальной инициализации, который получает 3 параметра: координаты точки
# и цвет;
# − метод доступа к цвету color с именем getColor().

# import math
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def distance_from_origin(self):
#         return math.sqrt(self.x**2 + self.y**2)
#
#     def getPoint(self):
#         return [self.x, self.y]
#
# class PointColor(Point):
#     def __init__(self, x, y, color):
#         super().__init__(x, y)
#         self.color = color
#
#     def getColor(self):
#         return self.color
#
# p = Point(3, 4)
# print(p.getPoint())
# print(p.distance_from_origin())
#
# pc = PointColor(1, 2, "red")
# print(pc.getPoint())
# print(pc.getColor())
# print(pc.distance_from_origin())



# Задание № 2
# Создать базовый класс «Домашнее животное» и производные классы «Собака»,
# «Кошка», «Попугай», «Хомяк». С помощью конструктора установить имя каждого животного
# и его характеристики. Реализуйте для каждого из классов методы:
# • Sound — издает звук животного (пишем текстом в консоль);
# 1
# • Show — отображает имя животного;
# • Type — отображает название его подвида.

# class Pet:
#     def __init__(self, name, characteristics):
#         self.name = name
#         self.characteristics = characteristics
#
#     def Sound(self):
#         pass
#
#     def Show(self):
#         print(self.name)
#
#     def Type(self):
#         pass
#
# class Dog(Pet):
#     def Sound(self):
#         print("Гав-гав")
#
#     def Type(self):
#         print("Собака")
#
# class Cat(Pet):
#     def Sound(self):
#         print("Мяу")
#
#     def Type(self):
#         print("Кошка")
#
# class Parrot(Pet):
#     def Sound(self):
#         print("Попка-дурак")
#
#     def Type(self):
#         print("Попугай")
#
# class Hamster(Pet):
#     def Sound(self):
#         print("Покупаем криптовалюту")
#
#     def Type(self):
#         print("Хомяк")
#
# dog = Dog("Бобик", "большой, надежный")
# cat = Cat("Мурка", "ласковая, игривая")
# parrot = Parrot("Кеша", "говорящий")
# hamster = Hamster("Пух", "маленький, пушистый")
#
# for pet in [dog, cat, parrot, hamster]:
#     pet.Show()
#     pet.Type()
#     pet.Sound()
#     print()



# Задание № 3
# Создать базовый класс Employer (служащий) с функцией Print(). Она должна выводить
# информацию о служащем. В случае базового класса это может быть строка с надписью This
# is Employer class.
# Создайте от него три производных класса: President, Manager, Worker.
# Переопределите функцию Print() для вывода информации, соответствующей каждому
# типу служащего.

# class Employer:
#     def Print(self):
#         print("This is Employer class")
#
# class President(Employer):
#     def Print(self):
#         print("This is President class")
#
# class Manager(Employer):
#     def Print(self):
#         print("This is Manager class")
#
# class Worker(Employer):
#     def Print(self):
#         print("This is Worker class")
#
# employees = [
#     Employer(),
#     President(),
#     Manager(),
#     Worker(),
# ]
#
# for employee in employees:
#     employee.Print()
