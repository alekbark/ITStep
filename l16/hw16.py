# Домашнее задание №16: Объектно-ориентированное
# программирование
# Выполните следующее задания:
# Задание №1
# Создайте класс Device, который содержит информацию об устройстве. С помощью
# механизма наследования, реализуйте класс CoffeeMachine (содержит информацию о
# кофемашине), класс Blender (содержит информацию о блендере), класс MeatGrinder
# (содержит информацию о мясорубке). Каждый из классов должен содержать необходимые
# для работы методы.

# class Device:
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power
#         self.is_on = False
#
#     def turn_on(self):
#         self.is_on = True
#         print(f"{self.name} turned on.")
#
#     def turn_off(self):
#         self.is_on = False
#         print(f"{self.name} turned off.")
#
# class CoffeeMachine(Device):
#     def make_coffee(self):
#         if self.is_on:
#             print("Making coffee.")
#         else:
#             print(f"The coffee machine is turned off.")
#
# class Blender(Device):
#     def blend(self):
#         if self.is_on:
#             print("Blending ingredients.")
#         else:
#             print(f"The blender is turned off.")
#
# class MeatGrinder(Device):
#     def grind_meat(self):
#         if self.is_on:
#             print("Grinding meat.")
#         else:
#             print(f"The meat grinder is turned off.")
#
# coffee = CoffeeMachine("Coffee Machine", 1500)
# blender = Blender("Blender", 800)
# grinder = MeatGrinder("Grinder", 1200)
#
# coffee.turn_on()
# coffee.make_coffee()
#
# blender.turn_on()
# blender.blend()
#
# grinder.turn_on()
# grinder.grind_meat()



# Задание №2
# Создайте класс Ship, который содержит информацию о корабле. С помощью механизма
# наследования, реализуйте класс Frigate (содержит информацию о фрегате), класс Destroyer
# (содержит информацию об эсминце), класс Cruiser (содержит информацию о крейсере).
# Каждый из классов должен содержать необходимые для работы методы.

# class Ship:
#     def __init__(self, name, speed, armor):
#         self.name = name
#         self.speed = speed
#         self.armor = armor
#         self.is_moving = False
#
#     def move(self):
#         self.is_moving = True
#         print(f"{self.name} is moving at {self.speed} knots")
#
#     def stop(self):
#         self.is_moving = False
#         print(f"{self.name} has stopped.")
#
# class Frigate(Ship):
#     def sonar_scan(self):
#         print("Frigate is scanning with sonar")
#
# class Destroyer(Ship):
#     def launch_missile(self):
#         print("Destroyer launched a missile")
#
# class Cruiser(Ship):
#     def fire_main_gun(self):
#         print("Cruiser fired the main gun")
#
# frigate = Frigate("Falcon", 30, 200)
# destroyer = Destroyer("Storm", 35, 300)
# cruiser = Cruiser("Titan", 28, 500)
#
# frigate.move()
# frigate.sonar_scan()
#
# destroyer.move()
# destroyer.launch_missile()
#
# cruiser.move()
# cruiser.fire_main_gun()



# ООП. Множественное следование
# Выполните следующее задания:
# Задание №1
# Используя понятие множественного наследования, разработайте класс «Окружность,
# вписанная в квадрат».

# import math
#
# class Square:
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return self.side ** 2
#
#     def perimeter(self):
#         return 4 * self.side
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius**2
#
#     def circumference(self):
#         return 2 * math.pi * self.radius
#
# class InscribedCircle(Square, Circle):
#     def __init__(self, side):
#         Square.__init__(self, side)
#         Circle.__init__(self, side / 2)
#
# figure = InscribedCircle(10)
# print("Square area:", figure.area())
# print("Square perimeter:", figure.perimeter())
# print("Circle area:", Circle.area(figure))
# print("Circle circumference:", figure.circumference())



# Задание №2
# Используя механизм множественного наследования разработайте класс “Автомобиль”.
# Должны быть классы «Колеса», «Двигатель», «Двери».

# class Wheels:
#     def __init__(self, wheels_count):
#         self.wheels_count = wheels_count
#
#     def rotate(self):
#         print(f"{self.wheels_count} wheels are rotating")
#
# class Engine:
#     def __init__(self, power):
#         self.power = power
#         self.engine_on = False
#
#     def start_engine(self):
#         self.engine_on = True
#         print(f"Engine started with {self.power} HP")
#
#     def stop_engine(self):
#         self.engine_on = False
#         print("Engine stopped")
#
# class Doors:
#     def __init__(self, doors_count):
#         self.doors_count = doors_count
#
#     def open_doors(self):
#         print(f"{self.doors_count} doors opened")
#
#     def close_doors(self):
#         print(f"{self.doors_count} doors closed")
#
# class Car(Wheels, Engine, Doors):
#     def __init__(self, wheels, power, doors):
#         Wheels.__init__(self, wheels)
#         Engine.__init__(self, power)
#         Doors.__init__(self, doors)
#
#     def drive(self):
#         if self.engine_on:
#             self.rotate()
#             print("Car is driving")
#         else:
#             print("Cannot drive. Engine is off")
#
# car = Car(4, 150, 4)
#
# car.open_doors()
# car.close_doors()
#
# car.start_engine()
# car.drive()
#
# car.stop_engine()



# Задание №3
# Создайте базовый класс Shape для рисования плоских фигур.
# Определите методы:
# Show() — вывод на экран информации о фигуре;
# Save() — сохранение фигуры в файл;
# Load() — считывание фигуры из файла.
# Определите производные классы:
# Square — квадрат, который характеризуется координатами левого верхнего угла и
# длиной стороны;
# Rectangle — прямоугольник с заданными координатами верхнего левого угла и
# размерами;
# 1
# Circle — окружность с заданными координатами центра и радиусом;
# Ellipse — эллипс с заданными координатами верхнего угла, описанного вокруг него
# прямоугольника со сторонами, параллельными осям координат, и размерами этого
# прямоугольника. Создайте список фигур, сохраните фигуры в файл, загрузите в другой список
# и отобразите информацию о каждой из фигур.

# import json
#
# class Shape:
#     def Show(self):
#         pass
#
#     def Save(self):
#         pass
#
# class Square(Shape):
#     def __init__(self, x, y, side):
#         self.x = x
#         self.y = y
#         self.side = side
#
#     def Show(self):
#         return (f"Квадрат с координатами левого верхнего угла {self.x}, {self.y}, "
#                 f"и стороной {self.side}.")
#
#     def Save(self):
#         return {
#             "type": "Square",
#             "params": {
#                 "x": self.x,
#                 "y": self.y,
#                 "side": self.side
#             }
#         }
#
# class Rectangle(Shape):
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#
#     def Show(self):
#         return (f"Прямоугольник с координатами левого верхнего угла {self.x}, {self.y}, "
#                 f"шириной {self.width} и высотой {self.height}.")
#
#     def Save(self):
#         return {
#             "type": "Rectangle",
#             "params": {
#                 "x": self.x,
#                 "y": self.y,
#                 "width": self.width,
#                 "height": self.height
#             }
#         }
#
# class Circle(Shape):
#     def __init__(self, x, y, radius):
#         self.x = x
#         self.y = y
#         self.radius = radius
#
#     def Show(self):
#         return (f"Окружность с координатами центра {self.x}, {self.y} "
#                 f"и радиусом {self.radius}.")
#
#     def Save(self):
#         return {
#             "type": "Circle",
#             "params": {
#                 "x": self.x,
#                 "y": self.y,
#                 "radius": self.radius
#             }
#         }
#
# class Ellipse(Shape):
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#
#     def Show(self):
#         return (f"Эллипс с координатами левого верхнего угла описывающего прямоугольника {self.x}, {self.y}, "
#                 f"шириной {self.width} и высотой {self.height}.")
#
#     def Save(self):
#         return {
#             "type": "Ellipse",
#             "params": {
#                 "x": self.x,
#                 "y": self.y,
#                 "width": self.width,
#                 "height": self.height
#             }
#         }
#
# shapes = [
#     Square(1, 2, 3),
#     Rectangle(1, 2, 3, 4),
#     Circle(2, 3, 4),
#     Ellipse(1, 2, 3, 4),
# ]
#
# data = []
#
# for shape in shapes:
#     data.append(shape.Save())
#
# with open("Shapes.json","w", encoding="utf-8") as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)
#
# with open("Shapes.json","r", encoding="utf-8") as f:
#     loaded_data = json.load(f)
#
# classes = {
#     "Square": Square,
#     "Rectangle": Rectangle,
#     "Circle": Circle,
#     "Ellipse": Ellipse,
# }
#
# loaded_shapes = []
# for shape in loaded_data:
#     type_of_shape = shape["type"]
#     cls = classes[type_of_shape]
#     obj = cls(**shape["params"])
#     loaded_shapes.append(obj)
#
# for shape in loaded_shapes:
#     print(shape.Show())