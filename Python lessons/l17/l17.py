# from datetime import date
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# # a class method to create a Person object by birth year.
#     @classmethod
#     def fromBirthYear(cls, name, year):
#         return cls(name, date.today().year - year)
#
# # a static method to check if a Person is adult or not.
#     @staticmethod
#     def isAdult(age):
#         return age > 18
#
# person1 = Person('mayank', 21)
# person2 = Person.fromBirthYear('mayank', 1996)
# print(person1.age)
# print(person2.age)
# # print the result
# print(Person.isAdult(22))

# class Man:
#     instances_count = 0
#     def __init__(self,name):
#         self.name=name
#         Man.instances_count+=1
#     @staticmethod
#     def counter():
#         return Man.instances_count
# a=Man("a")
# b=Man("aa")
# c=Man("fga")
# print(Man.counter())

class Point2D:
    instances_count = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point2D.instances_count += 1
    def __str__(self):
        return 'Точка 2D ({}, {})'.format(self.x, self.y)
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Point2D(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            self.x += other
            self.y += other
            return self
        else:
            raise TypeError("Не могу добавить {1} к {0}".format(self.__class__, type(other)))
    def __sub__(self, other):
        return Point2D(self.x - other.x, self.y - other.y)
    def __neg__(self):
        return Point2D(-self.x, -self.y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __ne__(self, other):
        return not (self == other)
    @staticmethod
    def sum(*points):
        assert len(points) > 0, "Количество суммируемых точек = 0!"
        res = points[0]
        for point in points[1:]:
            res += point
        return res
    @classmethod
    def from_string(cls, str_value):
        values = [float(x) for x in str_value.split(',')]
        assert len(values) == 2
        return cls(*values)

if __name__ == "__main__":
    p1 = Point2D(0, 5)
    p2 = Point2D(-5, 10)
    p3 = Point2D.from_string("5, 6")
    print(p1 + p3) # Точка 2D (5.0, 11.0)
    print(Point2D.instances_count) # 4 (p1, p2, p3, p1 + p2)
    p4 = Point2D.sum(p1, p2, p3, Point2D(0, -21))
    print(p4)