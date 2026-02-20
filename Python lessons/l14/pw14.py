# Задание № 1
# Реализуйте класс «Человек». Необходимо хранить в полях класса: ФИО, дату рождения,
# контактный телефон, город, страну, домашний адрес. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
from os import name


# class Person:
#     def __init__(self):
#         self.__fio = ""
#         self.__birth_date = ""
#         self.__phone = ""
#         self.__city = ""
#         self.__country = ""
#         self.__address = ""
#
#     def input_data(self):
#         self.__fio = input("ФИО: ")
#         self.__birth_date = input("Дата рождения: ")
#         self.__phone = input("Телефон: ")
#         self.__city = input("Город: ")
#         self.__country = input("Страна: ")
#         self.__address = input("Адрес: ")
#
#     def output_data(self):
#         print(
#             f"ФИО: {self.__fio}\n"
#             f"Дата рождения: {self.__birth_date}\n"
#             f"Телефон: {self.__phone}\n"
#             f"Город: {self.__city}\n"
#             f"Страна: {self.__country}\n"
#             f"Адрес: {self.__address}\n"
#         )
#
#     def get_fio(self):
#         return self.__fio
#     def set_fio(self, fio):
#         self.__fio = fio
#     def get_phone(self):
#         return self.__phone
#     def set_phone(self, phone):
#         self.__phone = phone
#
# p = Person()
# p.input_data()
# p.output_data()
#
# p.set_fio("Петров Иван Сергеевич")
# print(p.get_fio())



# Задание № 2
# Создайте класс «Город». Необходимо хранить в полях класса: название города, название
# региона, название страны, количество жителей в городе, почтовый индекс города,
# телефонный код города. Реализуйте методы класса для ввода данных, вывода данных,
# реализуйте доступ к отдельным полям через методы класса.

# class City:
#     def __init__(self):
#         self.__name = ""
#         self.__region = ""
#         self.__country = ""
#         self.__population = 0
#         self.__postal_code = ""
#         self.__phone_code = ""
#
#     def input_data(self):
#         self.__name = input("Название города: ")
#         self.__region = input("Регион: ")
#         self.__country = input("Страна: ")
#         self.__population = int(input("Количество жителей: "))
#         self.__postal_code = input("Почтовый индекс: ")
#         self.__phone_code = input("Телефонный код: ")
#
#     def output_data(self):
#         print(
#             f"Город: {self.__name}\n"
#             f"Регион: {self.__region}\n"
#             f"Страна: {self.__country}\n"
#             f"Население: {self.__population}\n"
#             f"Почтовый индекс: {self.__postal_code}\n"
#             f"Телефонный код: {self.__phone_code}"
#         )
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_population(self):
#         return self.__population
#
#     def set_population(self, population):
#         self.__population = population
#
# city = City()
# city.input_data()
# city.output_data()
#
# city.set_population(1200000)
# print(city.get_population())



# Задание № 3
# Создайте класс «Страна». Необходимо хранить в полях класса: название страны,
# название континента, количество жителей в стране, телефонный код страны, название
# столицы, название городов страны. Реализуйте методы класса для ввода данных, вывода
# данных, реализуйте доступ к отдельным полям через методы класса.

# class Country:
#     def __init__(self):
#         self.__name = ""
#         self.__continent = ""
#         self.__population = 0
#         self.__phone_code = ""
#         self.__capital = ""
#         self.__cities = []
#
#     def input_data(self):
#         self.__name = input("Название страны: ")
#         self.__continent = input("Континент: ")
#         self.__population = int(input("Количество жителей: "))
#         self.__phone_code = input("Телефонный код: ")
#         self.__capital = input("Столица: ")
#         self.__cities = input("Города (через запятую): ").split(",")
#
#     def output_data(self):
#         print(
#             f"Страна: {self.__name}\n"
#             f"Континент: {self.__continent}\n"
#             f"Население: {self.__population}\n"
#             f"Телефонный код: {self.__phone_code}\n"
#             f"Столица: {self.__capital}\n"
#             f"Города: {", ".join(self.__cities)}."
#         )
#
#     def get_name(self):
#         return self.__name
#     def set_name(self, name):
#         self.__name = name
#     def get_population(self):
#         return self.__population
#     def set_population(self, population):
#         self.__population = population
#     def get_cities(self):
#         return self.__cities
#     def add_city(self, city):
#         self.__cities.append(city)
#
# country = Country()
# country.input_data()
# country.output_data()
#
# country.add_city("Караганда")
# print(country.get_cities())



# Задание № 4
# Создайте класс «Дробь». Необходимо хранить в полях класса: числитель и знаменатель.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса. Также создайте методы класса для выполнения арифметических
# операций (сложение, вычитание, умножение, деление).

# class Fraction:
#     def __init__(self, numerator=0, denominator=1):
#         if denominator == 0:
#             raise ValueError("Знаменатель не может быть равен 0")
#         self.__num = numerator
#         self.__den = denominator
#
#     def input_data(self):
#         self.__num = int(input("Числитель: "))
#         self.__den = int(input("Знаменатель: "))
#         if self.__den == 0:
#             raise ValueError("Знаменатель не может быть равен 0")
#
#     def output_data(self):
#         print(f"{self.__num}/{self.__den}")
#
#     def get_numerator(self):
#         return self.__num
#
#     def set_numerator(self, value):
#         self.__num = value
#
#     def get_denominator(self):
#         return self.__den
#
#     def set_denominator(self, value):
#         if value == 0:
#             raise ValueError("Знаменатель не может быть равен 0")
#         self.__den = value
#
#     def add(self, other):
#         return Fraction(
#             self.__num * other.__den + other.__num * self.__den, self.__den * other.__den
#         )
#     def sub(self, other):
#         return Fraction(
#             self.__num * other.__den - other.__num * self.__den, self.__den * other.__den
#         )
#     def mul(self, other):
#         return Fraction(
#             self.__num * other.__num, self.__den * other.__den
#         )
#     def div(self, other):
#         if self.__den == 0:
#             raise ValueError("Знаменатель не может быть равен 0")
#         return Fraction(
#             self.__num * other.__den, self.__den * other.__num
#         )
#
# f1 = Fraction(1, 2)
# f2 = Fraction(3, 4)
#
# f3 = f1.add(f2)
# f4 = f1.mul(f2)
# f5 = f1.div(f2)
# f6 = f1.sub(f2)
# f3.output_data()
# f4.output_data()
# f5.output_data()
# f6.output_data()
#
# f7 = Fraction(5, 0)



# ООП. Инкапсуляция
# Задания №1
# Разработайте класс с "полной инкапсуляцией", доступ к атрибутам которого и
# изменение данных реализуются через вызовы методов. В объектно-ориентированном
# программировании принято имена методов для извлечения данных начинать со слова get
# (взять), а имена методов, в которых свойствам присваиваются значения, – со слова set
# (установить). Например, get_field, set_field.

# class User:
#     def __init__(self):
#         self.__login = ""
#         self.__password = ""
#
#     def get_login(self):
#         return self.__login
#
#     def set_login(self, login):
#         self.__login = login
#
#     def get_password(self):
#         return self.__password
#
#     def set_password(self, password):
#         self.__password = password



# Задания №2
# Написать программу, в которой есть главный класс Games со статическим полем Year,
# опишите конструктор присваивающий значение полю Year, также опишите метод getName,
# который возвращает имя игры. На основе главного класса путем наследования опишите
# четыре класса PCGames, PS4Games, XboxGames, MobileGames. Добавьте каждому классу
# дополнительные поля и переопределите у всех классов метод getName.

# class Games:
#     Year = None
#
#     def __init__(self, year, name):
#         Games.Year = year
#         self._name = name
#
#     def getName(self):
#         return self._name
#
# class PCGames(Games):
#     def __init__(self, year, name, min_specs):
#         super().__init__(year, name)
#         self.min_specs = min_specs
#
#     def getName(self):
#         return f"PC Game: {self._name}, min specs: {self.min_specs}"
#
# class PS4Games(Games):
#     def __init__(self, year, name, exclusive):
#         super().__init__(year, name)
#         self.exclusive = exclusive
#
#     def getName(self):
#         return f"PS4 Game: {self._name}, exclusive: {self.exclusive}"
#
# class XboxGames(Games):
#     def __init__(self, year, name, game_pass):
#         super().__init__(year, name)
#         self.game_pass = game_pass
#
#     def getName(self):
#         return f"Xbox Game: {self._name}, Game Pass: {self.game_pass}"
#
# class MobileGames(Games):
#     def __init__(self, year, name, ads):
#         super().__init__(year, name)
#         self.ads = ads
#
#     def getName(self):
#         return f"Mobile Game: {self._name}, ads: {self.ads}"
#
#
# pc = PCGames(2023, "Cyberpunk", "GTX 1060")
# ps = PS4Games(2022, "God of War", True)
#
# print(pc.getName())
# print(ps.getName())
# print(Games.Year)



# Задание №3
# Напишите программу с пустым классом Country. Опишите наследуемые от класса
# Country классы Russia, Canada, Germany. Добавьте каждому классу поле population и опишите
# метод setPopulation и getPopulation.

# class Country:
#     pass
#
# class Russia(Country):
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
# class Canada(Country):
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
# class Germany(Country):
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
# r = Russia()
# r.setPopulation(146_000_000)
# print(r.getPopulation())
#
# c = Canada()
# c.setPopulation(38_000_000)
# print(c.getPopulation())