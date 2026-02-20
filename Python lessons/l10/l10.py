# import datetime
# from time import strftime

#
# dt_now = datetime.datetime.now()
# print(dt_now)

# from datetime import date
#
# current_date = date.today()
# print(current_date)


# current_date_time = datetime.datetime.now()
# print(current_date_time)
#
# current_time = current_date_time.time()
# print(current_time)


#
# attr = dir(datetime)
# print(attr)



# time_obj = datetime.time(hour=8, minute=48, second=45)
# print(time_obj)

# time_obj = datetime.datetime(2020,10, 17)
# print(time_obj)

# td_obj = datetime.timedelta(hours=10000)
# print(td_obj)
# print(td_obj.seconds)

# first_date = datetime.date(2020, 1, 1)
# second_date = datetime.date(2025, 6, 18)
#
# delta = second_date - first_date
# print(delta)

# date_now = datetime.datetime.now(datetime.timezone.utc)
# print(date_now)

import pytz

# tz_karachi = pytz.timezone('Asia/Karachi')
# print(datetime.datetime.now(tz_karachi))

# day = datetime.datetime.now()
# print(day.strftime("%Y-%m-%d %H:%M:%S"))
# print(day.weekday())
# print(day.strftime("%A"))
# print(day.strftime("%a"))
# print(day.strftime("%c"))
# print(day.strftime("%X"))
# print(day.strftime("%S"))
# print(day.strftime("%Y"))
# print(day.strftime("%w"))
# print(day.strftime("%u"))
# print(day.strftime("%m"))
# print(day.strftime("%u"))
# print(day.strftime("%m"))

# time = datetime.time(15, 33, 33, 122)
# print(time, type(time))
# print(time.hour)


# date_string = "21 September. 1999"
# time_obj = datetime.datetime.strptime(date_string, "%d %B. %Y")
# print(time_obj)

# myfile = open("hello_txt", "w")
# myfile.write("hello world")
# myfile.close()

# try:
#     somefile = open('somefile.txt','w')
#     try:
#         somefile.write("hello world")
#     except Exception as e:
#         print(e)
#     finally:
#         somefile.close()
# except Exception as ex:
#     print(ex)

# with open("hello_txt", "w") as some_file:
#     some_file.write("hello world")

# with open("hello_txt", "w") as some_file:
#     some_file.write("\nhello world")

# with open("hello_txt", "a") as some_file:
#     print("hello world", file = some_file)

# with open("hello_txt", "r") as f:
#     str1 = f.readline()
#     print(str1, end="")
#     str2 = f.readline()
#     print(str2, end="")
#     str3 = f.readline()
#     print(str3, end="")

# with open("hello_txt", "r") as f:
#     contents = f.readlines()
#     str1 = contents[0]
#     str2 = contents[1]
#     str3 = contents[2]
#     print(str1, end="")
#     print(str2, end="")
#     print(str3, end="")

# import os

# print(os.name)
# print(os.environ)
# print(os.getcwd())
# print(os.path.exists('D:/python_projects/ITStep/l10.py'))

# os.mkdir(r"C:\Users\Пользователь\Desktop\example")

# os.makedirs(r"C:\Users\Пользователь\Desktop\example\first\second\third")

# os.remove(r"C:\Users\Пользователь\Desktop\example\first\second\third\Новый точечный рисунок.bmp")

# os.rmdir(r"C:\Users\Пользователь\Desktop\example\first\second\third")

# os.removedirs(r"C:\Users\Пользователь\Desktop\example\first\second")

# os.startfile(r"D:\python_projects\ITStep\hello_txt")

# print(os.path.basename(r"D:/python_projects/ITStep/l10.py"))
#
# print(os.path.dirname(r"D:/python_projects/ITStep/l10.py"))

# print(os.path.getsize(r"D:/python_projects/ITStep/l10.py"))

# os.mkdir(r"C:\Users\Пользователь\Desktop\example1")

# os.rename(r"C:\Users\Пользователь\Desktop\example", r"C:\Users\Пользователь\Desktop\example707")

# os.renames(r"C:\Users\Пользователь\Desktop\example707\example1", r"C:\Users\Пользователь\Desktop\example303\example2")

# print(os.listdir(r"C:\Users\Пользователь\Desktop"))

# import csv

# тут ничего не писал, слишком долго
