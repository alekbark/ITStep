# Домашнее задание №15: ООП. Полиморфизм
# Выполните следующее задание:
# Опишите класс Vehicle с методом drive(), который выводит сообщение о том, как
# транспортное средство двигается. Вы создаете экземпляры классов Car, Bicycle и Boat,
# каждый из которых реализует метод drive() по-разному, выводя соответствующие сообщения
# для каждого типа транспорта. Затем вы создаете экземпляры этих классов и вызываете их
# методы drive(). Каждый объект выдаст сообщение о движении, соответствующее его типу.

class Vehicle:
    def drive(self):
        raise NotImplementedError

class Car(Vehicle):
    def drive(self):
        print("Car drives on the road using an engine")

class Bicycle(Vehicle):
    def drive(self):
        print("Bicycle moves by pedaling")

class Boat(Vehicle):
    def drive(self):
        print("Boat sails on water")

vehicles = [Bicycle(), Car(), Boat()]

for vehicle in vehicles:
    vehicle.drive()