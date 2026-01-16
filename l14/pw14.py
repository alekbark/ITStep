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
