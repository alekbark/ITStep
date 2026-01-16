# def get_student_names(students: dict) -> list:
#     return sorted(students.keys())
#
# students = {
#     "Ivan": 90,
#     "Anna": 85,
#     "Petr": 78
# }
# print(get_student_names(students))


# class Car:
#     def start_engine(self):
#         engine_on = True # К сожалению, не сработает
#     def drive_to(self, city):
#         if engine_on: # Ошибка NameError
#             print("Едем в город {}.".format(city))
#         else:
#             print("Машина не заведена, никуда не едем")
# c = Car()
# c.start_engine()
# c.drive_to('Владивосток')

# class Car:
# # создание атрибутов класса
#     car_count = 0
# # создание методов класса
#     def __init__(self):
#         Car.car_count +=1
# car = Car()
# car2 = Car()
# print(Car.car_count)

# class Car:
#     def __init__(self):
#         self.engine_on = False
#     def start_engine(self):
#         self.engine_on = True
#     def drive_to(self, city):
#         if self.engine_on:
#             print("Едем в город {}.".format(city))
#         else:
#             print("Машина не заведена, никуда не едем.")
# car1 = Car()
# car1.start_engine()
# car1.drive_to('Владивосток')
# car2 = Car()
# car2.drive_to('Лиссабон')
# # Едем в город Владивосток.
# # Машина не заведена, никуда не едем.

# # создаем класс Car
# class Car:
# # создаем конструктор класса Car
#     def __init__(self, model):
# # Инициализация свойств.
#         self.model = model
# # создаем свойство модели.
#     @property
#     def model(self):
#         return self.__model
# # Сеттер для создания свойств.
#     @model.setter
#     def model(self, model):
#         if model < 2000:
#             self.__model = 2000
#         elif model > 2018:
#             self.__model = 2018
#         else:
#             self.__model = model
#     def getCarModel(self):
#         return "Год выпуска модели " + str(self.model)
# carA = Car(2088)
# print(carA.getCarModel())