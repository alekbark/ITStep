# Практическая работа №10: Работа с датой и временем. Файлы и каталоги

# Задание №1

# import datetime
# from time import strftime
#
# print(dir(datetime.datetime.now()))
#
# now = datetime.datetime.now()
# print(now)
# print(now.year)
# print(now.month)
# print(now.isocalendar().week)
# print(now.weekday())
# print(now.timetuple().tm_yday)
# print(now.day)
# print(strftime("%A"))
# print(strftime("%a"))

# Задание №2

# import datetime
#
# year = int(input("Введите год: "))
#
# last_day_feb = (
#     datetime.date(year, 3, 1) -
#     datetime.timedelta(days=1)
# ).day
#
# if last_day_feb == 29:
#     print("Этот год является високосным!")
# else:
#     print("Этот год не является високосным!")

# Задание №3

# import datetime
#
# date_string = "1 января 2014 14:43"
#
# months = {
#     "января": "01",
#     "февраля": "02",
#     "марта": "03",
#     "апреля": "04",
#     "мая": "05",
#     "июня": "06",
#     "июля": "07",
#     "августа": "08",
#     "сентября": "09",
#     "октября": "10",
#     "ноября": "11",
#     "декабря": "12"
# }
#
# parts = date_string.split()
# day = parts[0].zfill(2)
# month = months[parts[1]]
# year = parts[2]
# time = parts[3]
#
# new_date_string = f"{day} {month} {year} {time}"
#
# result = datetime.datetime.strptime(new_date_string, "%d %m %Y %H:%M")
#
# print(result)

# Задание №4

# import datetime
#
# now = datetime.datetime.now()
# current_time = now.time()
# print(current_time)

# Работа с датой и временем

# Задание №1 и задание №2 (так совпало, что получилось универсальное решение)
# import datetime
#
# date = datetime.date(1995, 6, 12)
#
# if date.month == 12:
#     new_date = datetime.date(date.year + 1, 1, 1)
# else:
#     new_date = datetime.date(date.year, date.month + 1, 1)
#
# last_day = (new_date - datetime.timedelta(days=1)).day
#
# print(last_day)

# Задание №3

# import datetime
#
# for year in range(2015, 2017):
#     count = 0
#
#     for month in range(1, 13):
#         date = datetime.date(year, month, 1)
#         if date.weekday() == 0:
#             count += 1
#     print(f"{year}: {count}")

# Задание №4

# import time
#
# for i in range(5):
#     print("Печать строки")
#     time.sleep(3)

# Задание №5

# import datetime
# today = datetime.date.today()
# delta = datetime.timedelta(days=30)
# date_before = today - delta
# date_after = today + delta
# print(f"Today: {today}")
# print(f"30 days before: {date_before}")
# print(f"30 days after: {date_after}")

# Задание №1

# import re
#
# input_file = "input.txt"
# output_file = "output.txt"
#
# with open(input_file, "r", encoding="utf-8") as f:
#     text = f.read()
#
# words = re.findall(r"[A-Za-zА-Яа-я]{7,}", text)
#
# with open(output_file, "w", encoding="utf-8") as f:
#     for word in words:
#         f.write(word + "\n")

# Задание №2

# input_file = "input.txt"
# output_file = "output2.txt"
#
# with open(input_file, "r", encoding="utf-8") as src:
#     lines = src.readlines()
#
# with open(output_file, "w", encoding="utf-8") as dst:
#     for line in lines:
#         dst.write(line)

# Задание №3

# input_file = "input.txt"
# output_file = "output3.txt"
#
# with open(input_file, "r", encoding="utf-8") as src:
#     lines = src.readlines()
#
# with open(output_file, "w", encoding="utf-8") as dst:
#     for line in reversed(lines):
#         dst.write(line)

# Задание №4

# input_file = "input.txt"
# output_file = "output4.txt"
#
# with open(input_file, "r", encoding="utf-8") as src:
#     lines = src.readlines()
#
# insert_index = None
#
# for i, line in enumerate(lines):
#     if "," not in line:
#         insert_index = i
#
# stars_line = "************\n"
#
# if insert_index is not None:
#     lines.insert(insert_index + 1, stars_line)
# else:
#     lines.append(stars_line)
#
# with open(output_file, "w", encoding="utf-8") as dst:
#     dst.writelines(lines)



