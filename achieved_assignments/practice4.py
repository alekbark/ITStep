"""
a = int(input('Enter a number: '))
b = int(input('Enter another number: '))
if a>b:
    print("true")
else:
    print("false")
"""

"""
a = int(input('Enter a number: '))
b = int(input('Enter another number: '))
c = int(input('Enter another number: '))

if a+b>c:
    print("true")
else:
    print("false")
"""

"""
a = int(input('Enter a number: '))
if a%2==0:
    print("true")
else:
    print("false")
"""

"""
a = int(input('Enter a number: '))
if a%2==0:
    print("четное")
else:
    print("нечетное")
"""

"""
a = int(input('Enter a day of the week: '))
if 1<=a<=5:
    print("Это будний день")
elif a==6 or a==7:
    print("Это выходной")
else:
    print("Число не соответствует диапазону недели")
"""

"""
a = int(input('Enter a number: '))
if a>20:
    print(a/6)
else:
    print(a*6)
"""

"""
n = int(input('Enter a number: '))
if n>0:
    print(n+1)
elif n==0:
    print(10)
else:
    print(n-2)
"""

"""
a = int(input('Enter a number: '))
b = int(input('Enter another number: '))
if a!=b:
    s=a+b
    a=s
    b=s
    print(a)
    print(b)
else:
    a=0
    b=0
    print(a)
    print(b)
"""

"""
a = int(input('Enter a number: '))
if a>0:
    a+=1
    print(a)
else:
    print(a)
"""

"""
a = int(input('Enter a number: '))
b = int(input('Enter another number: '))
if a%b==0:
    print("divisible")
else:
    print("not divisible")
"""

"""
A = int(input('Enter a number: '))
B = int(input('Enter another number: '))
H = int(input('Enter another number: '))
if A<=H<=B:
    print("Это нормально")
elif H<A:
    print("Недосып")
elif H>B:
    print("Пересып")
"""

"""
year = int(input('Enter a year: '))
if year%4==0 and year%100!=0 or year%400==0:
    print("Високосный")
else:
    print("Обычный")
"""

"""
a = int(input('Enter a number: '))
if -15<a<=12 or 14<a<17 or 19<=a:
    print(True)
else:
    print(False)
"""

"""
type_of_room = str(input("Print a type of the room (triangle, rectangle or circle) "))
if type_of_room == "triangle":
    a = int(input('Enter the first side of the triangle: '))
    b = int(input('Enter the second side of the triangle: '))
    c = int(input('Enter the third side of the triangle: '))
    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(S)
elif type_of_room == "rectangle":
    a = int(input('Enter the first side of the rectangle: '))
    b = int(input('Enter the second side of the rectangle: '))
    S = a * b
    print(S)
elif type_of_room == "circle":
    r = int(input('Enter the radius of the circle: '))
    S = 3.14 * r * r
    print(S)
else:
    print("Wrong input")
"""

"""
num = int(input('Enter a number of programmers: '))
if 11 <= num % 100 <= 14:
    print(str(num) + " программистов")
elif num % 10 == 1:
    print(str(num) + " программист")
elif 2 <= num % 10 <= 4:
    print(str(num) + " программиста")
else:
    print(str(num) + " программистов")
"""
