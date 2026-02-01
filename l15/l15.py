# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#
#         print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")
#     def make_sound(self):
#         print("Meow")
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#
#         print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")
#     def make_sound(self):
#         print("Bark")
# cat1 = Cat("Kitty", 2.5)
# dog1 = Dog("Fluffy", 4)
# for animal in (cat1, dog1):
#     animal.make_sound()
#     animal.info()
#     animal.make_sound()

# class T1:
#     def __init__(self):
#         self.n = 10
#     def total(self, a):
#         return self.n + int(a)
# class T2:
#     def __init__(self):
#         self.string = 'Hi'
#
#     def total(self, a):
#         return len(self.string + str(a))
# t1 = T1()
# t2 = T2()
# print(t1.total(35)) # Вывод: 45
# print(t2.total(35)) # Вывод: 4
#
# print(dir(t1), "\n", dir(T1))