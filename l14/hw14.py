# Домашнее задание №14: Объектно-ориентированное программирование
# Задание №1
# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса: название модели,
# год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте методы класса
# для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

# class Car:
#     def __init__(self):
#         self.__model = ""
#         self.__year = 0
#         self.__manufacture = ""
#         self.__engine_volume = 0.0
#         self.__color = ""
#         self.__price = 0
#
#     def input_data(self):
#         self.__model = input("Please enter the model: ")
#         self.__year = int(input("Please enter the year: "))
#         self.__manufacture = input("Please enter the manufacture: ")
#         self.__engine_volume = float(input("Please enter the engine volume: "))
#         self.__color = input("Please enter the color: ")
#         self.__price = int(input("Please enter the price: "))
#
#     def output_data(self):
#         print(
#             f"Model: {self.__model}\n"
#             f"Year of manufacture: {self.__year}\n"
#             f"Manufacture: {self.__manufacture}\n"
#             f"Engine Volume: {self.__engine_volume}\n"
#             f"Color: {self.__color}\n"
#             f"Price: {self.__price}\n"
#         )
#
#     def get_model(self):
#         return self.__model
#
#     def set_model(self, model):
#         self.__model = model
#
#     def get_price(self):
#         return self.__price
#
#     def set_price(self, price):
#         if price < 0:
#             raise ValueError("Price cannot be less than 0")
#         self.__price = price
#
#
# car = Car()
# car.input_data()
# car.output_data()
#
# car.set_price(15000000)
# print(car.get_model())



# Задание №2
# Реализуйте класс «Книга». Необходимо хранить в полях класса: название книги, год
# выпуска, издателя, жанр, автора, цену. Реализуйте методы класса для ввода данных, вывода
# данных, реализуйте доступ к отдельным полям через методы класса.

# class Book:
#     def __init__(self):
#         self.__title = ""
#         self.__year = 0
#         self.__publisher = ""
#         self.__genre = ""
#         self.__author = ""
#         self.__price = 0
#
#     def input_data(self):
#         self.__title = input("Enter Book Title: ")
#         self.__year = int(input("Enter Book Year: "))
#         self.__publisher = input("Enter Book Publisher: ")
#         self.__genre = input("Enter Book Genre: ")
#         self.__author = input("Enter Book Author: ")
#         self.__price = int(input("Enter Book Price: "))
#
#     def output_data(self):
#         print(
#             f"Title: {self.__title}\n"
#             f"Year: {self.__year}\n"
#             f"Publisher: {self.__publisher}\n"
#             f"Genre: {self.__genre}\n"
#             f"Author: {self.__author}\n"
#             f"Price: {self.__price}\n"
#         )
#
#     def get_title(self):
#         return self.__title
#
#     def set_title(self, title):
#         self.__title = title
#
#     def det_price(self):
#         return self.__price
#
#     def set_price(self, price):
#         if price < 0:
#             raise ValueError("The price cannot be negative")
#         self.__price = price
#
# book = Book()
# book.input_data()
# book.output_data()
#
# book.set_price(4500)
# print(book.get_title())



# Задание №3
# Реализуйте класс «Стадион». Необходимо хранить в полях класса: название стадиона,
# дату открытия, страну, город, вместимость. Реализуйте методы класса для ввода данных,
# вывода данных, реализуйте доступ к отдельным полям через методы класса.

# class Stadium:
#     def __init__(self):
#         self.__name = ""
#         self.__open_date = ""
#         self.__country = ""
#         self.__city = ""
#         self.__capacity = 0
#
#     def input_data(self):
#         self.__name = input("Enter the stadium name: ")
#         self.__open_date = input("Enter the opening date: ")
#         self.__country = input("Enter the country: ")
#         self.__city = input("Enter the city: ")
#         self.__capacity = input("Enter the capacity: ")
#
#     def output_data(self):
#         print(
#             f"Stadium Name: {self.__name}\n"
#             f"Opening Date: {self.__open_date}\n"
#             f"Country: {self.__country}\n"
#             f"City: {self.__city}\n"
#             f"Capacity: {self.__capacity}\n"
#         )
#
#     def get_capacity(self):
#         return self.__capacity
#
#     def set_capacity(self, capacity):
#         if capacity < 0:
#             raise ValueError("Capacity cannot be negative")
#         self.__capacity = capacity
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, name):
#         self.__name = name
#
# s = Stadium()
# s.input_data()
# s.output_data()
#
# s.set_capacity(45000)
# print(s.get_capacity())



# ООП. Инкапсуляция
# Напишите программу, в которой есть главный класс с текстовым полем. В главное классе
# должен быть метод для присваивания значения полю: без аргументов и с одним текстовым
# аргументом. Объект главного класса создаётся передачей одного текстового аргумента
# конструктору. На основе главного класса создается класса потомок. В классе-потомке нужно
# добавить числовое поле. У конструктора класса-потомка два аргумента.

# class Base:
#     def __init__(self, text):
#         self.__text = text
#
#     def set_text(self, text=None):
#         if text is None:
#             self.__text = ""
#         else:
#             self.__text = text
#
#     def get_text(self):
#         return self.__text
#
# class Child(Base):
#     def __init__(self, text, number):
#         super().__init__(text)
#         self.__number = number
#
#     def set_number(self, number):
#         self.__number = number
#
#     def get_number(self):
#         return self.__number
#
# b = Base("Hello")
# print(b.get_text())
#
# b.set_text()
# print(b.get_text())
#
# c = Child("Child text", 42)
# print(c.get_text(), c.get_number())
